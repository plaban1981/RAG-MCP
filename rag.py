from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import asyncio
import os
from typing import List
import search
import time
import logging

# Configure logging
logger = logging.getLogger(__name__)

async def create_rag_from_documents(documents: List[Document]) -> FAISS:
    """
    Create a RAG system directly from a list of documents
    
    Args:
        documents: List of already fetched documents
        
    Returns:
        FAISS: Vector store object
    """
    max_retries = 3
    retry_delay = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1}: Creating RAG from {len(documents)} documents")
            embeddings = OllamaEmbeddings(
                model="mxbai-embed-large:latest",
                base_url="http://localhost:11434"
            )
            
            # Text chunking processing
            logger.info("Splitting documents into chunks")
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=200,
                length_function=len,
            )
            split_documents = text_splitter.split_documents(documents)
            logger.info(f"Created {len(split_documents)} chunks")
            
            logger.info("Creating vector store")
            vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)
            logger.info("Vector store created successfully")
            return vectorstore
            
        except Exception as e:
            logger.error(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error("All attempts failed to create RAG from documents")
                raise

async def create_rag(links: List[str]) -> FAISS:
    """Create a RAG system from a list of URLs"""
    try:
        logger.info(f"Creating RAG from {len(links)} URLs")
        # Use Ollama embeddings instead of OpenAI
        embeddings = OllamaEmbeddings(
            model="mxbai-embed-large:latest",
            base_url="http://localhost:11434"
        )
        
        # Process URLs in parallel
        logger.info("Processing URLs in parallel")
        tasks = [search.get_web_content(url) for url in links]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        documents = []
        for result in results:
            if isinstance(result, List) and result:
                documents.extend(result)
        
        logger.info(f"Retrieved {len(documents)} valid documents")
        
        if not documents:
            logger.error("No valid documents retrieved from URLs")
            raise ValueError("No valid documents retrieved from URLs")
            
        logger.info("Splitting documents into chunks")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len,
        )
        split_documents = text_splitter.split_documents(documents)
        logger.info(f"Created {len(split_documents)} chunks")
        
        logger.info("Creating vector store")
        vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)
        logger.info("Vector store created successfully")
        return vectorstore
    except Exception as e:
        logger.error(f"Error in create_rag: {str(e)}")
        raise

async def search_rag(query: str, vectorstore: FAISS, k: int = 5) -> List[Document]:
    """Search the RAG system for relevant documents"""
    max_retries = 3
    retry_delay = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Searching RAG with query: {query}")
            results = vectorstore.similarity_search(query, k=k)
            logger.info(f"Found {len(results)} relevant documents")
            return results
        except Exception as e:
            logger.error(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error("All attempts failed to search RAG")
                raise 