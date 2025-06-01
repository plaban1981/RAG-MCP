from typing import List, Tuple
from langchain_core.documents import Document
from exa_py import Exa
import asyncio
import os
from dotenv import load_dotenv
import aiohttp
import ssl
import certifi
import requests
from bs4 import BeautifulSoup
import time
import logging
import streamlit as st

# Load .env variables with override
load_dotenv(override=True)

# Initialize the Exa client
exa_api_key = os.getenv("EXA_API_KEY", "")
exa = Exa(api_key=exa_api_key)

# Initialize FireCrawl API key
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY", "")

# SSL context for secure connections
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Constants
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Configure logging
logger = logging.getLogger(__name__)

async def get_web_content(url: str) -> List[Document]:
    """Get web content using requests and BeautifulSoup as fallback."""
    try:
        logger.info(f"Fetching content from URL: {url}")
        headers = {
            "User-Agent": USER_AGENT
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error for {url}: {e.response.status_code} - {e.response.reason}")
            return []
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection Error for {url}: {str(e)}")
            return []
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout Error for {url}: {str(e)}")
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Request Error for {url}: {str(e)}")
            return []
        
        # Parse the HTML content
        logger.info(f"Parsing HTML content from {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        script_count = len(soup(["script", "style"]))
        for script in soup(["script", "style"]):
            script.decompose()
        logger.debug(f"Removed {script_count} script/style elements from {url}")
            
        # Get text content
        text = soup.get_text(separator='\n', strip=True)
        
        # Basic text cleaning
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        content = '\n'.join(lines)
        
        if content:
            content_length = len(content)
            logger.info(f"Successfully extracted {content_length} characters from {url}")
            return [Document(
                page_content=content,
                metadata={"source": url, "length": content_length}
            )]
        
        logger.warning(f"No content extracted from {url}")
        return []
        
    except Exception as e:
        logger.error(f"Unexpected error for {url}: {str(e)}", exc_info=True)
        return []

async def search_and_get_content(query: str, num_results: int = 10) -> Tuple[str, List[Document]]:
    """Combined function to search web and get content."""
    try:
        logger.info(f"Starting web search for query: {query}")
        # First get search results from Exa
        formatted_results, raw_results = await search_web(query, num_results)
        
        if not raw_results:
            logger.warning("No search results found")
            return formatted_results, []
            
        # Extract URLs from search results
        urls = [result.url for result in raw_results if hasattr(result, 'url')]
        logger.info(f"Found {len(urls)} URLs to process")
        
        if not urls:
            logger.warning("No valid URLs found")
            return formatted_results, []
            
        # Get content for each URL in parallel
        logger.info("Fetching content from URLs")
        tasks = [get_web_content(url) for url in urls]
        content_results = await asyncio.gather(*tasks)
        
        # Flatten the list of document lists
        all_documents = []
        for docs in content_results:
            all_documents.extend(docs)
            
        logger.info(f"Retrieved content from {len(all_documents)} documents")
        return formatted_results, all_documents
        
    except Exception as e:
        logger.error(f"Error in search_and_get_content: {str(e)}")
        return "Error occurred during search and content retrieval", []

async def search_web(query: str, num_results: int = 5) -> Tuple[str, list]:
    """Search the web using Exa API."""
    try:
        logger.info(f"Searching web with Exa API. Query: {query}, Results: {num_results}")
        search_results = exa.search_and_contents(
            query,
            num_results=num_results,
            summary={"query": "Main points and key takeaways"}
        )
        logger.info(f"Searching web with Exa API. Query: {query}, Results: {search_results}")
        # Store raw results for UI display - fix the attribute access
        if hasattr(st, 'session_state'):
            # Convert Exa results to dictionary format
            raw_results = []
            for result in search_results.results:
                raw_results.append({
                    'title': result.title if hasattr(result, 'title') else 'No Title',
                    'url': result.url if hasattr(result, 'url') else '',
                    'published_date': result.published_date if hasattr(result, 'published_date') else '',
                    'summary': result.summary if hasattr(result, 'summary') else ''
                })
            st.session_state.raw_results = raw_results

        logger.info("Formatting search results")
        formatted_results = format_search_results(search_results)
        logger.info(f"Found {len(search_results.results)} search results")
        return formatted_results, search_results.results
    except Exception as e:
        logger.error(f"Error in web search: {str(e)}")
        return f"An error occurred while searching with Exa: {e}", []

def format_search_results(search_results):
    """Format search results into readable markdown"""
    if not search_results.results:
        return "No results found."

    formatted_results = "Search Results:\n\n"
    
    # Format each result with title, URL, and publication date
    for idx, result in enumerate(search_results.results, 1):
        title = result.title if hasattr(result, 'title') and result.title else "No title"
        url = result.url
        published_date = result.published_date if hasattr(result, 'published_date') else None
        
        # Format the title with link and publication date
        formatted_results += f"{idx}. [{title}]({url})"
        if published_date:
            formatted_results += f" (Published: {published_date})"
        formatted_results += "\n\n"
        
        # Add summary if available
        if hasattr(result, 'summary') and result.summary:
            formatted_results += f"Summary: {result.summary}\n\n"
            
            # If summary contains bullet points, format them properly
            if "•" in result.summary or "*" in result.summary:
                points = [p.strip() for p in result.summary.split("•") if p.strip()]
                if not points:
                    points = [p.strip() for p in result.summary.split("*") if p.strip()]
                
                formatted_results += "\n".join([f"• {point}" for point in points]) + "\n\n"

    return formatted_results 