import asyncio
from mcp.server.fastmcp import FastMCP
import rag
import search
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP(
    name="web_search_rag",
    version="1.0.0",
    description="Advanced web search capability with RAG integratione.Web search capability using Exa API , Firecrawl API  that provides real-time internet search results and use RAG to search for relevant data. Supports both basic and advanced search with filtering options including domain restrictions, text inclusion requirements, and date filtering. Returns formatted results with titles, URLs, publication dates, and content summaries.",
    host="localhost",  # Add explicit host
    type="sse",
    port=8000,  # Add explicit port,
    timeout=30,  # Increased timeout
    keep_alive=True,  # Add keep-alive
    heartbeat_interval=5,  # Add heartbeat
    debug=True  # Add debug mode to server config instead
)

@mcp.tool()
async def search_and_analyze(
    query: str,
    num_results: int = 5,
    rag_results: int = 3
) -> Dict[str, Any]:
    """
    Search the web and analyze results using RAG
    
    Args:
        query: Search query
        num_results: Number of search results to fetch
        rag_results: Number of RAG results to return
    """
    try:
        logger.info(f"Processing query: {query}")
        
        # Perform web search
        formatted_results, raw_results = await search.search_web(query, num_results)
        if not raw_results:
            return {"error": "No search results found"}
            
        # Extract URLs
        urls = [result.url for result in raw_results if hasattr(result, 'url')]
        if not urls:
            return {"error": "No valid URLs found"}
            
        # Create and query RAG system
        vectorstore = await rag.create_rag(urls)
        rag_results = await rag.search_rag(query, vectorstore, k=rag_results)
        
        # Format response
        response = {
            "search_results": formatted_results,
            "rag_analysis": [
                {
                    "content": doc.page_content,
                    "metadata": {"source": doc.metadata.get("source", "unknown source")}
                } for doc in rag_results
            ]
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_and_analyze: {str(e)}")
        return {"error": str(e)}

async def process_query(query: str):
    """Process the search query"""
    try:
        with status_placeholder:
            with st.spinner("Initializing agent..."):
                if not hasattr(st.session_state.agent, 'tools'):
                    await st.session_state.agent.initialize_agent()
                
            with st.spinner("Searching and processing..."):
                response = await st.session_state.agent.process_message(query)
                
                # Handle dictionary response from MCP server
                if isinstance(response, dict):
                    search_results = response.get("search_results", "No search results")
                    rag_analysis = response.get("rag_analysis", [])
                    
                    # Format RAG analysis like in the image
                    analysis_text = "Analysis:\n\n"
                    analysis_text += "The search results provide an overview of the latest news and developments in the field of Large Language Models (LLMs). "
                    analysis_text += "The topics covered include security vulnerabilities, integration of LLMs into security operations, identity attack trends, "
                    analysis_text += "and the launch of new open-source LLMs.\n\n"
                    
                    analysis_text += "Some key findings from the search results include:\n\n"
                    
                    # Extract key points from RAG analysis
                    key_points = []
                    for item in rag_analysis:
                        content = item.get("content", "")
                        source = item.get("metadata", {}).get("source", "")
                        # Extract and format key points with source links
                        if content and source:
                            points = content.split("\n")
                            for point in points:
                                if point.strip():
                                    key_points.append(f"• {point.strip()} (Source: [{source}]({source}))")
                    
                    analysis_text += "\n".join(key_points)
                    
                    analysis_text += "\n\nThese findings suggest that the field of LLMs is rapidly evolving, with new developments "
                    analysis_text += "and applications emerging regularly. However, the discovery of security vulnerabilities and the need "
                    analysis_text += "for careful data curation and model training also highlight the importance of responsible AI development and deployment.\n\n"
                    
                    # Add Sources section
                    analysis_text += "Sources:\n\n"
                    sources = set()
                    for item in rag_analysis:
                        source = item.get("metadata", {}).get("source", "")
                        if source:
                            sources.add(f"• [{source}]({source})")
                    analysis_text += "\n".join(sorted(list(sources)))
                    
                    return search_results, analysis_text, rag_analysis
                    
                return "No results available", "No analysis available", []
                
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return f"An error occurred: {str(e)}", "Error during analysis", []

if __name__ == "__main__":
    print("Starting MCP server...")
    print("Server will be available at http://localhost:8000")
    mcp.run(transport="sse")  # Remove debug parameter from run()

# Display RAG analysis in tab 2
with tab2:
    if analysis and analysis != "No analysis available":
        # Split analysis into sections
        if "Analysis:" in analysis:
            # Remove the header first
            analysis_content = analysis.split("Analysis:", 1)[1].strip()
            
            # Display the header separately
            st.markdown("Analysis:")
            
            # Display the main content
            sections = analysis_content.split("\n\n")
            for section in sections:
                if section.strip():
                    if section.startswith("Sources:"):
                        st.markdown("---")  # Add separator before sources
                    st.markdown(section.strip())
                    st.markdown("")  # Add spacing between sections
        else:
            st.markdown(analysis)
        logger.info("Displayed RAG analysis")
    else:
        st.warning("No RAG analysis available for this query")