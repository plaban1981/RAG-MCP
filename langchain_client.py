import asyncio
import nest_asyncio
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import httpx
from langchain.tools import Tool
from typing import Optional, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Enable nested asyncio for Jupyter-like environments
nest_asyncio.apply()

class LangchainMCPClient:
    def __init__(self, mcp_server_url="http://localhost:8000"):
        logger.info("Initializing LangchainMCPClient...")
        self.llm = ChatOllama(
            model="llama2-70b",
            temperature=0.7,
            streaming=False
        )
        
        # Updated server configuration
        server_config = {
            "default": {
                "url": f"{mcp_server_url}/sse",
                "transport": "sse",
                "options": {
                    "timeout": 30.0,
                    "retry_connect": True,
                    "max_retries": 3,
                    "read_timeout": 25.0,
                    "write_timeout": 10.0,
                    "connect_timeout": 5.0,
                    "keep_alive": True,
                    "headers": {
                        "Accept": "text/event-stream",
                        "Cache-Control": "no-cache"
                    }
                }
            }
        }
        logger.info(f"Connecting to MCP server at {mcp_server_url}...")
        self.mcp_client = MultiServerMCPClient(server_config)
        self.chat_history = []
        
        # System prompt for the agent
        self.SYSTEM_PROMPT = """You are an AI assistant that helps users search the web and analyze information using RAG.
        You can:
        1. Search the web for current information
        2. Analyze search results using RAG
        3. Present information in a clear, organized way
        
        Always:
        1. Think through each step carefully
        2. Cite your sources
        3. Provide clear summaries of the information"""

    async def check_server_connection(self):
        """Check if the MCP server is accessible"""
        base_url = self.mcp_client.connections["default"]["url"].replace("/sse", "")
        try:
            logger.info(f"Testing connection to {base_url}...")
            async with httpx.AsyncClient() as client:
                # First check the base endpoint
                try:
                    response = await client.get(base_url, timeout=5.0)
                    logger.info(f"Base endpoint response: {response.status_code}")
                except httpx.TimeoutError:
                    logger.warning("Base endpoint timeout - this is normal")
                    pass

                # Then check SSE endpoint
                sse_url = f"{base_url}/sse"
                logger.info(f"Checking SSE endpoint at {sse_url}...")
                try:
                    response = await client.get(
                        sse_url,
                        headers={"Accept": "text/event-stream"},
                        timeout=5.0
                    )
                    if response.status_code == 200:
                        logger.info("SSE endpoint is accessible")
                        return True
                except httpx.ReadTimeout:
                    # This is expected for SSE connections
                    logger.info("SSE endpoint timeout - this is normal for SSE")
                    return True
                except Exception as e:
                    logger.error(f"SSE endpoint error: {str(e)}")
                    return False

            return False
        except Exception as e:
            logger.error(f"Error connecting to MCP server: {type(e).__name__} - {str(e)}")
            return False

    async def initialize_agent(self):
        """Initialize the agent with tools and prompt template"""
        logger.info("Initializing agent...")
        if not await self.check_server_connection():
            raise ConnectionError("Cannot connect to MCP server")
            
        try:
            logger.info("Getting available tools...")
            mcp_tools = await self.mcp_client.get_tools()
            
            # Create wrapper for search_and_analyze
            async def search_and_analyze_wrapper(query: str):
                try:
                    tool = mcp_tools[0]  # search_and_analyze tool
                    result = await tool.ainvoke({
                        "query": query,
                        "num_results": 10,
                        "rag_results": 5
                    })
                    return result
                except Exception as e:
                    logger.error(f"Error in search_and_analyze: {str(e)}")
                    return f"Error performing search and analysis: {str(e)}"

            # Create Langchain tool
            self.tools = [
                Tool(
                    name="search_and_analyze",
                    description="Search the web and analyze results using RAG",
                    func=lambda x: "Use async version",
                    coroutine=search_and_analyze_wrapper
                )
            ]
            
            logger.info(f"Initialized {len(self.tools)} tools")
            
            # Create prompt template
            prompt = ChatPromptTemplate.from_messages([
                SystemMessage(content=self.SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{input}")
            ])
            
            logger.info("Agent initialization complete")
            
        except Exception as e:
            logger.error(f"Error initializing agent: {str(e)}")
            raise

    async def process_message(self, user_input: str) -> str:
        """Process a single user message"""
        try:
            logger.info(f"\n{'='*50}")
            logger.info("PROCESSING NEW QUERY")
            logger.info(f"{'='*50}")
            logger.info(f"User Query: {user_input}")
            
            # Call the search_and_analyze tool
            tool = self.tools[0]
            result = await tool.coroutine(user_input)
            
            # Log raw result
            logger.info(f"\n{'='*50}")
            logger.info("RAW RESULT FROM MCP SERVER")
            logger.info(f"{'='*50}")
            logger.info(str(result))
            
            # Return raw result for proper handling in streamlit
            return result
            
        except Exception as e:
            error_msg = f"Error processing message: {str(e)}"
            logger.error(f"\n{'='*50}")
            logger.error("ERROR IN PROCESSING")
            logger.error(f"{'='*50}")
            logger.error(error_msg)
            logger.error(f"{'='*50}\n")
            return {"error": error_msg}

    async def interactive_chat(self):
        """Start an interactive chat session"""
        logger.info("Starting interactive chat session")
        print("Chat session started. Type 'quit' to exit.")
        
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == 'quit':
                logger.info("Ending chat session")
                break
            
            response = await self.process_message(user_input)
            print("\nAgent:", response)

async def main():
    try:
        logger.info("Starting Langchain MCP Client")
        client = LangchainMCPClient()
        
        logger.info("Initializing agent")
        await client.initialize_agent()
        
        logger.info("Starting interactive chat")
        await client.interactive_chat()
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 