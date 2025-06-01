import streamlit as st
import asyncio
from langchain_client import LangchainMCPClient
import logging
from streamlit.runtime.scriptrunner import add_script_run_ctx
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_session_state():
    """Initialize session state variables"""
    if 'agent' not in st.session_state:
        st.session_state.agent = LangchainMCPClient()
        # Initialize the agent
        asyncio.run(st.session_state.agent.initialize_agent())
    if 'search_results' not in st.session_state:
        st.session_state.search_results = None
    if 'rag_results' not in st.session_state:
        st.session_state.rag_results = None
    if 'chunks' not in st.session_state:
        st.session_state.chunks = None

async def process_query(query: str):
    """Process the search query"""
    try:
        with status_placeholder:
            with st.spinner("Initializing agent..."):
                if not hasattr(st.session_state.agent, 'tools'):
                    await st.session_state.agent.initialize_agent()
                
            with st.spinner("Searching and processing..."):
                response = await st.session_state.agent.process_message(query)
                print(f"Response from MCP server: {response}")
                print(f"Type of response: {type(response)}")
                
                # Convert string response to dictionary if needed
                if isinstance(response, str):
                    try:
                        import json
                        response = json.loads(response)
                    except json.JSONDecodeError as e:
                        logger.error(f"Failed to parse JSON response: {e}")
                        return "Error parsing response", "Error during analysis", []
                
                # Handle dictionary response from MCP server
                if isinstance(response, dict):
                    search_results = response.get("search_results", "No search results")
                    print(f"Search Results: {search_results}")
                    rag_analysis = response.get("rag_analysis", [])
                    print(f"RAG Analysis: {rag_analysis}")
                    
                    # Format RAG analysis
                    analysis_text = "Analysis:\n\n"
                    if rag_analysis:
                        # Add overview
                        analysis_text += f"Based on the search results, here's an {query}:\n\n"
                        
                        # Extract key points from RAG analysis
                        key_points = []
                        for item in rag_analysis:
                            content = item.get("content", "")
                            source = item.get("metadata", {}).get("source", "")
                            
                            # Extract meaningful sentences and add as bullet points
                            sentences = [s.strip() for s in content.split('.') if len(s.strip()) > 20]
                            for sentence in sentences[:3]:  # Take first 3 meaningful sentences
                                if sentence and not sentence.startswith('Sign') and not sentence.startswith('Open'):
                                    key_points.append(f"• {sentence} (Source: [{source}]({source}))")
                        
                        # Add key points to analysis
                        analysis_text += "\nKey Points:\n\n"
                        analysis_text += "\n\n".join(key_points)
                        
                        # Add sources section
                        analysis_text += "\n\nSources:\n"
                        sources = set(item.get("metadata", {}).get("source", "") for item in rag_analysis)
                        for source in sources:
                            if source:
                                analysis_text += f"\n• [{source}]({source})"
                    
                    return search_results, analysis_text, rag_analysis
                    
                return "No results available", "No analysis available", []
                
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        return f"An error occurred: {str(e)}", "Error during analysis", []

# Page configuration
st.set_page_config(
    page_title="Web Search & RAG System MCP with LangChain",
    page_icon="🔍",
    layout="wide"
)

# Add initialization status
try:
    with st.spinner("Initializing system..."):
        init_session_state()
    st.success("System initialized successfully!")
except Exception as e:
    st.error(f"Error initializing system: {str(e)}")
    logger.error(f"Initialization error: {str(e)}", exc_info=True)

# Sidebar with About and Tips
with st.sidebar:
    st.header("About")
    st.info(
        "This app uses LangChain with MCP to provide enhanced search results "
        "and analysis using RAG (Retrieval Augmented Generation)."
    )
    
    st.header("Tips")
    st.markdown("""
    - For best results, use specific queries
    - The system processes multiple URLs, so it may take a moment
    - Results include both search findings and RAG analysis
    """)

    st.markdown("---")
    if st.button("🚪 Quit Application"):
        logger.info("User requested to quit the application")
        st.write("Shutting down... You can close this window.")
        if 'agent' in st.session_state:
            del st.session_state.agent
        sys.exit(0)

# Main content
st.title("Web Search & RAG System MCP with LangChain")
st.write("Enter a query to search the web and get enhanced results with RAG")

# Search query input
query = st.text_input("Search query", placeholder="Get the latest news about LLMs?")

# Create placeholder for status messages
status_placeholder = st.empty()

# Process query when entered
if query:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        progress_bar = st.progress(0)
        status_text = st.empty()
    
    try:
        status_text.text("Searching and processing...")
        progress_bar.progress(25)
        
        # Process the query
        search_results, analysis, chunks = asyncio.run(process_query(query))
        logger.info(f"Received response from agent")
        
        progress_bar.progress(75)
        status_text.text("Processing results...")
        
        # Display results in tabs
        tab1, tab2, tab3 = st.tabs(["📊 Search Results", "🔍 RAG Analysis", "📑 Document Chunks"])
        
        try:
            # Display search results in tab 1
            with tab1:
                if search_results and search_results != "No results available":
                    # Remove duplicate "Search Results:" if present
                    if search_results.startswith("Search Results:"):
                        search_results = search_results.replace("Search Results:", "", 1)
                    st.markdown("Search Results:")
                    st.markdown(search_results.strip())
                else:
                    st.warning("No results available")
                logger.info("Displayed search results")
            
            # Display RAG analysis in tab 2
            with tab2:
                if analysis and analysis != "No analysis available":
                    st.markdown(analysis)
                    logger.info("Displayed RAG analysis")
                else:
                    st.warning("No RAG analysis available for this query")
            
            # Display document chunks in tab 3
            with tab3:
                if chunks:
                    for i, chunk in enumerate(chunks, 1):
                        source = chunk.get("metadata", {}).get("source", "Unknown Source")
                        with st.expander(f"Chunk {i} from {source}", expanded=False):
                            st.markdown(chunk.get("content", "No content available"))
                    logger.info(f"Displayed {len(chunks)} document chunks")
                else:
                    st.warning("No document chunks available for this query")
                    
        except Exception as e:
            st.error(f"An error occurred while displaying results: {str(e)}")
            logger.error(f"Error in display: {str(e)}", exc_info=True)
        
    except Exception as e:
        st.error(f"An error occurred while processing the query: {str(e)}")
        logger.error(f"Error in query processing: {str(e)}", exc_info=True)
    finally:
        progress_bar.progress(100)
        status_text.empty()
        progress_bar.empty()

# Footer
st.markdown("---")
st.markdown(
    "Built with Streamlit, LangChain, and Model Context Protocol (MCP)",
    help="Uses advanced RAG techniques with LangChain for enhanced search results"
)

# Add a session cleanup function
def cleanup_session():
    """Clean up session resources"""
    if 'agent' in st.session_state:
        logger.info("Cleaning up session resources")
        del st.session_state.agent

# Register the cleanup function
st.session_state["_cleanup"] = cleanup_session

# Custom CSS to style the expanders like in the image
st.markdown("""
<style>
    .streamlit-expanderHeader {
        font-size: 1em;
        color: #0066cc;
    }
    .streamlit-expanderContent {
        background-color: white;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True) 