# RAG-MCP
RAG with MCP


<img width="626" alt="image" src="https://github.com/user-attachments/assets/8ce8db41-a411-4d8a-9ade-6340f36d2d72" />


<img width="571" alt="image" src="https://github.com/user-attachments/assets/265820e0-8de1-450e-a874-1fb741f5de87" />



#### MCP Server Logs


(.venv) C:\Users\PLNAYAK\Documents\RAG_MCP>python mcp_server.py
Starting MCP server...
Server will be available at http://localhost:8000
INFO:     Started server process [31656]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
INFO:     ::1:52054 - "GET / HTTP/1.1" 404 Not Found
INFO:     ::1:52054 - "GET /sse HTTP/1.1" 200 OK
INFO:     ::1:52057 - "GET /sse HTTP/1.1" 200 OK
INFO:     ::1:52058 - "POST /messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb HTTP/1.1" 202 Accepted
INFO:     ::1:52058 - "POST /messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb HTTP/1.1" 202 Accepted
INFO:     ::1:52058 - "POST /messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb HTTP/1.1" 202 Accepted
INFO:mcp.server.lowlevel.server:Processing request of type ListToolsRequest
INFO:     ::1:52065 - "GET /sse HTTP/1.1" 200 OK
INFO:     ::1:52066 - "POST /messages/?session_id=df7ff329724c434caace362c746400b5 HTTP/1.1" 202 Accepted
INFO:     ::1:52066 - "POST /messages/?session_id=df7ff329724c434caace362c746400b5 HTTP/1.1" 202 Accepted
INFO:     ::1:52066 - "POST /messages/?session_id=df7ff329724c434caace362c746400b5 HTTP/1.1" 202 Accepted
INFO:mcp.server.lowlevel.server:Processing request of type CallToolRequest
INFO:__main__:Processing query: Compare PydanticAI with LangGraph
INFO:search:Searching web with Exa API. Query: Compare PydanticAI with LangGraph, Results: 10
INFO:search:Searching web with Exa API. Query: Compare PydanticAI with LangGraph, Results: Title: Pydantic AI vs LangGraph – Pick The Right Data Validation Tool in 2025! (FULL OVERVIEW!)
URL: https://www.youtube.com/watch?v=tAresTJB9cY
ID: https://www.youtube.com/watch?v=tAresTJB9cY
Score: 0.3477572500705719
Published Date: 2025-03-28T00:00:00.000Z
Author: Tobi Teaches
Image: https://i.ytimg.com/vi/tAresTJB9cY/maxresdefault.jpg
Favicon: https://www.youtube.com/s/desktop/fc303b88/img/logos/favicon_32x32.png
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This YouTube video compares Pydantic AI and LangGraph for data validation and language processing. It explores their features, performance, and use cases to help viewers decide which tool is best for their projects in 2025. The video emphasizes that it is for educational purposes only and viewers should do their own research before making decisions.



Title: LangChain vs LangGraph - AI Agents Comparison
URL: https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph
ID: https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph
Score: 0.3429335057735443
Published Date: 2025-01-01T00:00:00.000Z
Author:
Image: https://firebasestorage.googleapis.com/v0/b/aiagentstore.appspot.com/o/agentLogos%2Flangchain-langchain.png?alt=media&token=ad58b8c8-0dbb-4a20-92ee-f03b6a69eb6b
Favicon: https://aiagentstore.ai/logo.svg
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: LangGraph and LangChain are both frameworks for building AI-powered workflows, but cater to different needs. LangChain is easier to use, has a larger community, and is well-suited for linear task pipelines. LangGraph, with its graph-based approach, offers greater flexibility and autonomy for complex, non-linear workflows with branching and loops, but has a steeper learning curve. Both are open-source, but LangChain may be more cost-effective for simpler applications.



Title: An AI Search Agent Built with PydanticAI and LangGraph Frameworks
URL: https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e
ID: https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e
Score: None
Published Date: 2025-01-27T04:11:37.000Z
Author: Kamal Dhungana
Image: https://miro.medium.com/v2/da:true/resize:fit:1200/0*y8BPx7D6XZYRLyrX
Favicon: https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This article discusses AI agents and two frameworks for building them: Pydantic AI and LangGraph. Pydantic AI simplifies the development of AI applications by integrating with Pydantic for data validation. LangGraph is a library for building stateful, multi-actor applications with LLMs, suitable for complex agent workflows.



Title: PydanticAI + Langgraph: The Ultimate Match for Smarter AI Agents!
URL: https://www.youtube.com/watch?v=P3qH5GVIxD0
ID: https://www.youtube.com/watch?v=P3qH5GVIxD0
Score: None
Published Date: 2025-02-02T00:00:00.000Z
Author: YourTechBud Codes
Image: None
Favicon: https://www.youtube.com/s/desktop/fc303b88/img/logos/favicon_32x32.png
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This YouTube video explores the integration of Langgraph and PydanticAI for building smarter AI agents. It covers the basics of Langgraph, its symbiosis with PydanticAI for simplified workflows, and demonstrates the implementation of a self-correcting AI using both frameworks. Key topics include calling tools, composing complex workflows, and understanding the differences between Langgraph and PydanticAI to determine if Langgraph is necessary for a given project. The video also provides links to a LangGraph quickstart guide, the presenter's code, a LangGraph 101 video, and a video on PydanticAI.



Title: How to use Pydantic Graph (an alternative to LangGraph) – Bartosz Mikulski | Your AI Is Lying to Customers. Let's Fix It Before It Goes Public.
URL: https://mikulskibartosz.name/pydantic-graph
ID: https://mikulskibartosz.name/pydantic-graph
Score: 0.33789506554603577
Published Date: 2025-05-18T00:00:00.000Z
Author: Bartosz Mikulski
Image: None
Favicon: None
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: Pydantic Graph is presented as a potential alternative to LangGraph, emphasizing its superior documentation and reliance on type hints. However, it is acknowledged as being designed for advanced users and potentially overkill for simpler applications. The article outlines the following key aspects of Pydantic Graph:

*   **Installation:** The library is installed as a separate package (`pydantic-graph`) and can be used independently of `pydantic-ai`.
*   **Basic Structure:** Graphs are built from classes inheriting from `BaseNode` with a `run` method that determines the next node to be executed.
*   **Graph Execution:** The graph executes nodes based on the return value of the `run` method, allowing for flexible graph structures with predefined paths.



Title: LangGraph vs. PydanticAI Comparison
URL: https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/
ID: https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/
Score: None
Published Date: 2025-01-01T00:00:00.000Z
Author:
Image: None
Favicon: https://a.fsdn.com/con/img/sandiego/logo-180x180.png
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This webpage compares LangGraph and PydanticAI, but the provided text focuses on related products: Sendbird (an omnichannel AI agent platform), Vertex AI (for building, deploying, and scaling ML models), Jotform (a no-code platform for data collection with AI-powered agents), and Stack AI (for AI agents that interact with users and complete tasks using internal data and APIs). The main point is to showcase alternatives and related tools in the AI and automation space.



Title: Pydantic AI vs LangGraph - Which Data Tool Is Better? (2025)
URL: https://www.youtube.com/watch?v=e0kn7JMH_No
ID: https://www.youtube.com/watch?v=e0kn7JMH_No
Score: 0.33769291639328003
Published Date: 2025-04-24T00:00:00.000Z
Author: Skillcraft AI
Image: None
Favicon: https://www.youtube.com/s/desktop/1520a82c/img/logos/favicon_32x32.png
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This YouTube video compares Pydantic AI and LangGraph to help viewers choose the right tool for their AI or data workflow projects. It encourages viewers to access AI tools, discounts, and webinars through a provided link.



Title: LangChain vs PydanticAI for building an AI Agent - Finn Andersen - Medium
URL: https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d
ID: https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d
Score: None
Published Date: 2025-01-29T11:48:36.000Z
Author: Finn Andersen
Image: https://miro.medium.com/v2/resize:fit:1200/1*g787VN00jm0lQrbjcy7Yag.png
Favicon: https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This article compares LangChain and PydanticAI for building a conversational AI agent with features like dynamic model choice, human-in-the-loop input, tool calling, conversation history, dynamic system prompts, and structured output. It uses the example of an AI waiter taking orders at a restaurant. The author found PydanticAI more approachable and intuitive than LangChain, which they describe as daunting due to its complexity and legacy content. The author then built the same demo project in both frameworks to compare the two.



Title: AutoGen vs CrewAI vs LangGraph vs PydanticAI vs Google ADK vs OpenAI Agents .... Which Multi-Agent Framework is Best?
URL: https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs
ID: https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs
Score: None
Published Date: 2025-04-30T23:51:34.000Z
Author: Victor Dibia, PhD
Image: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd200bddf-a22c-42f6-bba9-5b902b62d970_1804x1341.png
Favicon: https://substackcdn.com/image/fetch/f_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/4904f99a-6f96-4d8d-b190-e683752e69e6/favicon-32x32.png
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: This article compares six multi-agent frameworks—AutoGen, Google ADK, LangGraph, LLamaIndex, OpenAI Agents SDK, and PydanticAI—across 10 dimensions, including developer experience, async capabilities, and state management. It includes an interactive tool with "Hello World" agent implementations for each framework, allowing users to view code, compare implementations, and see quantitative metrics like lines of code and runtime. The article also links to a related article detailing the 10 dimensions used for comparison and guidance on whether a framework is even necessary.



Title: LangGraph: What It Is and How To Use It [Tutorial]
URL: https://lazyprogrammer.me/langgraph/
ID: https://lazyprogrammer.me/langgraph/
Score: 0.34060370922088623
Published Date: 2025-01-18T04:31:14.000Z
Author: Lazy Marketing
Image: https://lazyprogrammer.me/wp-content/uploads/2025/01/image_fx_-43.png
Favicon: None
Extras: None
Subpages: None
Text: None
Highlights: None
Highlight Scores: None
Summary: LangGraph is a framework for building AI agents that can handle complex tasks and workflows. It enables the creation of multi-agent systems where multiple AI agents collaborate, dividing up tasks and working together. LangGraph integrates with tools and platforms through the LangChain ecosystem and can be used for customer support automation and e-commerce.


Autoprompt String: Compare PydanticAI with LangGraph
Resolved Search Type: neural
CostDollars: total=0.015
  - search: {'neural': 0.005}
  - contents: {'summary': 0.01}
2025-06-01 22:02:41.242 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-06-01 22:02:41.243 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`
2025-06-01 22:02:41.243 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
INFO:search:Formatting search results
INFO:search:Found 10 search results
INFO:rag:Creating RAG from 10 URLs
INFO:rag:Processing URLs in parallel
INFO:search:Fetching content from URL: https://www.youtube.com/watch?v=tAresTJB9cY
INFO:search:Parsing HTML content from https://www.youtube.com/watch?v=tAresTJB9cY
INFO:search:Successfully extracted 244 characters from https://www.youtube.com/watch?v=tAresTJB9cY
INFO:search:Fetching content from URL: https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph
INFO:search:Parsing HTML content from https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph
INFO:search:Successfully extracted 5769 characters from https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph
INFO:search:Fetching content from URL: https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e
INFO:search:Parsing HTML content from https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e
INFO:search:Successfully extracted 1970 characters from https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e
INFO:search:Fetching content from URL: https://www.youtube.com/watch?v=P3qH5GVIxD0
INFO:search:Parsing HTML content from https://www.youtube.com/watch?v=P3qH5GVIxD0
INFO:search:Successfully extracted 221 characters from https://www.youtube.com/watch?v=P3qH5GVIxD0
INFO:search:Fetching content from URL: https://mikulskibartosz.name/pydantic-graph
INFO:search:Parsing HTML content from https://mikulskibartosz.name/pydantic-graph
INFO:search:Successfully extracted 10621 characters from https://mikulskibartosz.name/pydantic-graph
INFO:search:Fetching content from URL: https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/
ERROR:search:Connection Error for https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/: HTTPSConnectionPool(host='sourceforge.net', port=443): Max retries exceeded with url: /software/compare/LangGraph-vs-PydanticAI/ (Caused by SSLError(SSLError(1, '[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)')))
INFO:search:Fetching content from URL: https://www.youtube.com/watch?v=e0kn7JMH_No
INFO:search:Parsing HTML content from https://www.youtube.com/watch?v=e0kn7JMH_No
INFO:search:Successfully extracted 216 characters from https://www.youtube.com/watch?v=e0kn7JMH_No
INFO:search:Fetching content from URL: https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d
INFO:search:Parsing HTML content from https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d
INFO:search:Successfully extracted 18351 characters from https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d
INFO:search:Fetching content from URL: https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs
INFO:search:Parsing HTML content from https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs
INFO:search:Successfully extracted 10491 characters from https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs
INFO:search:Fetching content from URL: https://lazyprogrammer.me/langgraph/
INFO:search:Parsing HTML content from https://lazyprogrammer.me/langgraph/
INFO:search:Successfully extracted 9506 characters from https://lazyprogrammer.me/langgraph/
INFO:rag:Retrieved 9 valid documents
INFO:rag:Splitting documents into chunks
INFO:rag:Created 37 chunks
INFO:rag:Creating vector store
INFO:httpx:HTTP Request: POST http://localhost:11434/api/embed "HTTP/1.1 200 OK"
INFO:faiss.loader:Loading faiss with AVX2 support.
INFO:faiss.loader:Successfully loaded faiss with AVX2 support.
INFO:faiss:Failed to load GPU Faiss: name 'GpuIndexIVFFlat' is not defined. Will not load constructor refs for GPU indexes.
INFO:rag:Vector store created successfully
INFO:rag:Searching RAG with query: Compare PydanticAI with LangGraph
INFO:httpx:HTTP Request: POST http://localhost:11434/api/embed "HTTP/1.1 200 OK"
INFO:rag:Found 5 relevant documents




#### Streamlit Logs



.venv) C:\Users\PLNAYAK\Documents\RAG_MCP>streamlit run streamlit_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.2:8501

2025-06-01 22:02:22,880 - langchain_client - INFO - Initializing LangchainMCPClient...
2025-06-01 22:02:22,895 - langchain_client - INFO - Connecting to MCP server at http://localhost:8000...
2025-06-01 22:02:22,895 - langchain_client - INFO - Initializing agent...
2025-06-01 22:02:22,896 - langchain_client - INFO - Testing connection to http://localhost:8000...
2025-06-01 22:02:22,913 - httpx - INFO - HTTP Request: GET http://localhost:8000 "HTTP/1.1 404 Not Found"
2025-06-01 22:02:22,914 - langchain_client - INFO - Base endpoint response: 404
2025-06-01 22:02:22,914 - langchain_client - INFO - Checking SSE endpoint at http://localhost:8000/sse...
2025-06-01 22:02:22,917 - httpx - INFO - HTTP Request: GET http://localhost:8000/sse "HTTP/1.1 200 OK"
2025-06-01 22:02:27,928 - langchain_client - INFO - SSE endpoint timeout - this is normal for SSE
2025-06-01 22:02:27,929 - langchain_client - INFO - Getting available tools...
2025-06-01 22:02:27,929 - mcp.client.sse - INFO - Connecting to SSE endpoint: http://localhost:8000/sse
2025-06-01 22:02:27,943 - httpx - INFO - HTTP Request: GET http://localhost:8000/sse "HTTP/1.1 200 OK"
2025-06-01 22:02:27,943 - mcp.client.sse - INFO - Received endpoint URL: http://localhost:8000/messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb
2025-06-01 22:02:27,944 - mcp.client.sse - INFO - Starting post writer with endpoint URL: http://localhost:8000/messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb
2025-06-01 22:02:27,949 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb "HTTP/1.1 202 Accepted"
2025-06-01 22:02:27,952 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb "HTTP/1.1 202 Accepted"
2025-06-01 22:02:27,954 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=46ddd1414d8e42c4aafde1a2c4407adb "HTTP/1.1 202 Accepted"
2025-06-01 22:02:27,956 - langchain_client - INFO - Initialized 1 tools
2025-06-01 22:02:27,956 - langchain_client - INFO - Agent initialization complete
2025-06-01 22:02:37,051 - langchain_client - INFO -
==================================================
2025-06-01 22:02:37,051 - langchain_client - INFO - PROCESSING NEW QUERY
2025-06-01 22:02:37,051 - langchain_client - INFO - ==================================================
2025-06-01 22:02:37,051 - langchain_client - INFO - User Query: Compare PydanticAI with LangGraph
2025-06-01 22:02:37,053 - mcp.client.sse - INFO - Connecting to SSE endpoint: http://localhost:8000/sse
2025-06-01 22:02:37,075 - httpx - INFO - HTTP Request: GET http://localhost:8000/sse "HTTP/1.1 200 OK"
2025-06-01 22:02:37,076 - mcp.client.sse - INFO - Received endpoint URL: http://localhost:8000/messages/?session_id=df7ff329724c434caace362c746400b5
2025-06-01 22:02:37,077 - mcp.client.sse - INFO - Starting post writer with endpoint URL: http://localhost:8000/messages/?session_id=df7ff329724c434caace362c746400b5
2025-06-01 22:02:37,081 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=df7ff329724c434caace362c746400b5 "HTTP/1.1 202 Accepted"
2025-06-01 22:02:37,083 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=df7ff329724c434caace362c746400b5 "HTTP/1.1 202 Accepted"
2025-06-01 22:02:37,086 - httpx - INFO - HTTP Request: POST http://localhost:8000/messages/?session_id=df7ff329724c434caace362c746400b5 "HTTP/1.1 202 Accepted"
2025-06-01 22:03:00,077 - langchain_client - INFO -
==================================================
2025-06-01 22:03:00,077 - langchain_client - INFO - RAW RESULT FROM MCP SERVER
2025-06-01 22:03:00,077 - langchain_client - INFO - ==================================================
2025-06-01 22:03:00,077 - langchain_client - INFO - {
  "search_results": "Search Results:\n\n1. [Pydantic AI vs LangGraph – Pick The Right Data Validation Tool in 2025! (FULL OVERVIEW!)](https://www.youtube.com/watch?v=tAresTJB9cY) (Published: 2025-03-28T00:00:00.000Z)\n\nSummary: This YouTube video compares Pydantic AI and LangGraph for data validation and language processing. It explores their features, performance, and use cases to help viewers decide which tool is best for their projects in 2025. The video emphasizes that it is for educational purposes only and viewers should do their own research before making decisions.\n\n\n2. [LangChain vs LangGraph - AI Agents Comparison](https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph) (Published: 2025-01-01T00:00:00.000Z)\n\nSummary: LangGraph and LangChain are both frameworks for building AI-powered workflows, but cater to different needs. LangChain is easier to use, has a larger community, and is well-suited for linear task pipelines. LangGraph, with its graph-based approach, offers greater flexibility and autonomy for complex, non-linear workflows with branching and loops, but has a steeper learning curve. Both are open-source, but LangChain may be more cost-effective for simpler applications.\n\n\n3. [An AI Search Agent Built with PydanticAI and LangGraph Frameworks](https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e) (Published: 2025-01-27T04:11:37.000Z)\n\nSummary: This article discusses AI agents and two frameworks for building them: Pydantic AI and LangGraph. Pydantic AI simplifies the development of AI applications by integrating with Pydantic for data validation. LangGraph is a library for building stateful, multi-actor applications with LLMs, suitable for complex agent workflows.\n\n\n4. [PydanticAI + Langgraph: The Ultimate Match for Smarter AI Agents!](https://www.youtube.com/watch?v=P3qH5GVIxD0) (Published: 2025-02-02T00:00:00.000Z)\n\nSummary: This YouTube video explores the integration of Langgraph and PydanticAI for building smarter AI agents. It covers the basics of Langgraph, its symbiosis with PydanticAI for simplified workflows, and demonstrates the implementation of a self-correcting AI using both frameworks. Key topics include calling tools, composing complex workflows, and understanding the differences between Langgraph and PydanticAI to determine if Langgraph is necessary for a given project. The video also provides links to a LangGraph quickstart guide, the presenter's code, a LangGraph 101 video, and a video on PydanticAI.\n\n\n5. [How to use Pydantic Graph (an alternative to LangGraph) – Bartosz Mikulski | Your AI Is Lying to Customers. Let's Fix It Before It Goes Public.](https://mikulskibartosz.name/pydantic-graph) (Published: 2025-05-18T00:00:00.000Z)\n\nSummary: Pydantic Graph is presented as a potential alternative to LangGraph, emphasizing its superior documentation and reliance on type hints. However, it is acknowledged as being designed for advanced users and potentially overkill for simpler applications. The article outlines the following key aspects of Pydantic Graph:\n\n*   **Installation:** The library is installed as a separate package (`pydantic-graph`) and can be used independently of `pydantic-ai`.\n*   **Basic Structure:** Graphs are built from classes inheriting from `BaseNode` with a `run` method that determines the next node to be executed.\n*   **Graph Execution:** The graph executes nodes based on the return value of the `run` method, allowing for flexible graph structures with predefined paths.\n\n\n• Pydantic Graph is presented as a potential alternative to LangGraph, emphasizing its superior documentation and reliance on type hints. However, it is acknowledged as being designed for advanced users and potentially overkill for simpler applications. The article outlines the following key aspects of Pydantic Graph:\n\n*   **Installation:** The library is installed as a separate package (`pydantic-graph`) and can be used independently of `pydantic-ai`.\n*   **Basic Structure:** Graphs are built from classes inheriting from `BaseNode` with a `run` method that determines the next node to be executed.\n*   **Graph Execution:** The graph executes nodes based on the return value of the `run` method, allowing for flexible graph structures with predefined paths.\n\n6. [LangGraph vs. PydanticAI Comparison](https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/) (Published: 2025-01-01T00:00:00.000Z)\n\nSummary: This webpage compares LangGraph and PydanticAI, but the provided text focuses on related products: Sendbird (an omnichannel AI agent platform), Vertex AI (for building, deploying, and scaling ML models), Jotform (a no-code platform for data collection with AI-powered agents), and Stack AI (for AI agents that interact with users and complete tasks using internal data and APIs). The main point is to showcase alternatives and related tools in the AI and automation space.\n\n\n7. [Pydantic AI vs LangGraph - Which Data Tool Is Better? (2025)](https://www.youtube.com/watch?v=e0kn7JMH_No) (Published: 2025-04-24T00:00:00.000Z)\n\nSummary: This YouTube video compares Pydantic AI and LangGraph to help viewers choose the right tool for their AI or data workflow projects. It encourages viewers to access AI tools, discounts, and webinars through a provided link.\n\n\n8. [LangChain vs PydanticAI for building an AI Agent - Finn Andersen - Medium](https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d) (Published: 2025-01-29T11:48:36.000Z)\n\nSummary: This article compares LangChain and PydanticAI for building a conversational AI agent with features like dynamic model choice, human-in-the-loop input, tool calling, conversation history, dynamic system prompts, and structured output. It uses the example of an AI waiter taking orders at a restaurant. The author found PydanticAI more approachable and intuitive than LangChain, which they describe as daunting due to its complexity and legacy content. The author then built the same demo project in both frameworks to compare the two.\n\n\n9. [AutoGen vs CrewAI vs LangGraph vs PydanticAI vs Google ADK vs OpenAI Agents .... Which Multi-Agent Framework is Best?](https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs) (Published: 2025-04-30T23:51:34.000Z)\n\nSummary: This article compares six multi-agent frameworks—AutoGen, Google ADK, LangGraph, LLamaIndex, OpenAI Agents SDK, and PydanticAI—across 10 dimensions, including developer experience, async capabilities, and state management. It includes an interactive tool with \"Hello World\" agent implementations for each framework, allowing users to view code, compare implementations, and see quantitative metrics like lines of code and runtime. The article also links to a related article detailing the 10 dimensions used for comparison and guidance on whether a framework is even necessary.\n\n\n10. [LangGraph: What It Is and How To Use It [Tutorial]](https://lazyprogrammer.me/langgraph/) (Published: 2025-01-18T04:31:14.000Z)\n\nSummary: LangGraph is a framework for building AI agents that can handle complex tasks and workflows. It enables the creation of multi-agent systems where multiple AI agents collaborate, dividing up tasks and working together. LangGraph integrates with tools and platforms through the LangChain ecosystem and can be used for customer support automation and e-commerce.\n\n",
  "rag_analysis": [
    {
      "content": "Pydantic AI vs LangGraph - Which Data Tool Is Better? (2025) - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=e0kn7JMH_No"
      }
    },
    {
      "content": "How to use Pydantic Graph (an alternative to LangGraph)\nBartosz Mikulski | Your AI Is Lying to Customers. Let's Fix It Before It Goes Public.\nConsultation\nKnowledge Base\nEngineering Blog\nAI Use Cases\nTools\nAI Readiness Assessment Tool\nAbout me\nNewsletter\nAI\nPydanticAI\nHow to use Pydantic Graph (an alternative to LangGraph)\nA guide to using Pydantic Graph - a type-safe alternative to LangGraph for building AI workflows.\nBartosz Mikulski\n24 Feb 2025\nâ   10 min read\nA Pydantic Graph may be a better alternative to LangGraph. For sure, Pydantic Graph has way better documentation, but if you compare any documentation to the one from LangChain, you set the bar really low. So, what else does it have to offer? As with every Pydantic project, type hints! However, a graph may be an overkill. The PydanticAI authors state in the documentation: âIf youâre not confident a graph-based approach is a good idea, it might be unnecessary.â and âpydantic-graph is designed for advanced users and makes heavy use of Python generics and types hints. It is not designed to be as beginner-friendly as PydanticAI.â If this doesnât scare you off, letâs see how to use it.\nTable of Contents\nPydantic Graph Installation\nBasic Graph Structure in Pydantic Graph\nGraphs with State\nAdding AI Agents to the Graph\nMonitoring and Debugging\nOne more thing. Graph support is in the very early beta stage. If you read this article a couple months after it was published and the code doesnât work anymore, let me know, I will update the text.\nPydantic Graph Installation\nThe graph library is provided as a separate package:\npydantic-graph\n. It has no dependency on\npydantic-ai\n, so if you want to use AI Agents, you must install both. However, the lack of dependencies makes it possible to use the\npydantic-graph\nlibrary for any project that requires graph-based state machines or workflows.\nI will use the library with OpenAI API, so I need to install the PydanticAI client.\npip\ninstall",
      "metadata": {
        "source": "https://mikulskibartosz.name/pydantic-graph"
      }
    },
    {
      "content": "PydanticAI + Langgraph: The Ultimate Match for Smarter AI Agents! - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=P3qH5GVIxD0"
      }
    },
    {
      "content": "Pydantic AI vs LangGraph – Pick The Right Data Validation Tool in 2025! (FULL OVERVIEW!) - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=tAresTJB9cY"
      }
    },
    {
      "content": "def __init__(self, menu_service: MenuService, order_service: OrderService, args: argparse.Namespace):\n# Initialise tools with dependencies\ntools = [\nGetMenuTool(menu_service=menu_service),\nCreateOrderTool(order_service=order_service),\nStructuredResponseTool(),\n]\nself.agent_executor = get_agent_executor(tools=tools, model_name=args.model, api_key=args.api_key)\nself.static_input_content = {\"restaurant_name\": args.restaurant_name, \"table_number\": args.table_number}\nself.config: RunnableConfig = {\"configurable\": {\"session_id\": \"not-even-used\"}}\ndef make_request(self, user_message: str) -> LLMResponse:\nresult = self.agent_executor.invoke(self.static_input_content | {\"input\": user_message}, self.config)\n# De-serialise structured response into an LLMResponse\nresponse = LLMResponse.model_validate_json(result[\"output\"])\nreturn response\nConclusion\nThis demonstration shows that it is much simpler to create a basic conversational and tool-calling AI agent using the PydanticAI framework than LangChain. LangChain has so many layers of deprecated functionality and is in desperate need of some extensive spring cleaning.\nI also wanted to enable streamed responses however this seemed quite difficult to achieve using LangChain with both tool calling and structured output involved.\nI imagine that the newer LangGraph approach for creating agents addresses many of the limitations and frustrations encountered here. PydanticAI has also recently added a\ngraph library\n, so next time I will explore what full graph-based implementations for both frameworks looks like.\nI hope this helps anyone who wants to choose between the frameworks or learn how they can be used to build cool things with AI!\nThe complete project repository can be found\nhere\n.\nLangchain\nLlm\nAI\nPydantic Ai\nAi Agent\n--\n--\n4\nFollow\nWritten by\nFinn Andersen\n221 followers\n·\n22 following\nTech projects and other things on my mind\nFollow\nResponses (\n4\n)\nSee all responses\nHelp\nStatus\nAbout\nCareers\nPress\nBlog\nPrivacy\nRules\nTerms",
      "metadata": {
        "source": "https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d"
      }
    }
  ]
}
Response from MCP server: {
  "search_results": "Search Results:\n\n1. [Pydantic AI vs LangGraph – Pick The Right Data Validation Tool in 2025! (FULL OVERVIEW!)](https://www.youtube.com/watch?v=tAresTJB9cY) (Published: 2025-03-28T00:00:00.000Z)\n\nSummary: This YouTube video compares Pydantic AI and LangGraph for data validation and language processing. It explores their features, performance, and use cases to help viewers decide which tool is best for their projects in 2025. The video emphasizes that it is for educational purposes only and viewers should do their own research before making decisions.\n\n\n2. [LangChain vs LangGraph - AI Agents Comparison](https://aiagentstore.ai/compare-ai-agents/langchain-vs-langgraph) (Published: 2025-01-01T00:00:00.000Z)\n\nSummary: LangGraph and LangChain are both frameworks for building AI-powered workflows, but cater to different needs. LangChain is easier to use, has a larger community, and is well-suited for linear task pipelines. LangGraph, with its graph-based approach, offers greater flexibility and autonomy for complex, non-linear workflows with branching and loops, but has a steeper learning curve. Both are open-source, but LangChain may be more cost-effective for simpler applications.\n\n\n3. [An AI Search Agent Built with PydanticAI and LangGraph Frameworks](https://medium.com/@kbdhunga/an-ai-search-agent-built-with-pydanticai-and-langgraph-frameworks-eea929dc665e) (Published: 2025-01-27T04:11:37.000Z)\n\nSummary: This article discusses AI agents and two frameworks for building them: Pydantic AI and LangGraph. Pydantic AI simplifies the development of AI applications by integrating with Pydantic for data validation. LangGraph is a library for building stateful, multi-actor applications with LLMs, suitable for complex agent workflows.\n\n\n4. [PydanticAI + Langgraph: The Ultimate Match for Smarter AI Agents!](https://www.youtube.com/watch?v=P3qH5GVIxD0) (Published: 2025-02-02T00:00:00.000Z)\n\nSummary: This YouTube video explores the integration of Langgraph and PydanticAI for building smarter AI agents. It covers the basics of Langgraph, its symbiosis with PydanticAI for simplified workflows, and demonstrates the implementation of a self-correcting AI using both frameworks. Key topics include calling tools, composing complex workflows, and understanding the differences between Langgraph and PydanticAI to determine if Langgraph is necessary for a given project. The video also provides links to a LangGraph quickstart guide, the presenter's code, a LangGraph 101 video, and a video on PydanticAI.\n\n\n5. [How to use Pydantic Graph (an alternative to LangGraph) – Bartosz Mikulski | Your AI Is Lying to Customers. Let's Fix It Before It Goes Public.](https://mikulskibartosz.name/pydantic-graph) (Published: 2025-05-18T00:00:00.000Z)\n\nSummary: Pydantic Graph is presented as a potential alternative to LangGraph, emphasizing its superior documentation and reliance on type hints. However, it is acknowledged as being designed for advanced users and potentially overkill for simpler applications. The article outlines the following key aspects of Pydantic Graph:\n\n*   **Installation:** The library is installed as a separate package (`pydantic-graph`) and can be used independently of `pydantic-ai`.\n*   **Basic Structure:** Graphs are built from classes inheriting from `BaseNode` with a `run` method that determines the next node to be executed.\n*   **Graph Execution:** The graph executes nodes based on the return value of the `run` method, allowing for flexible graph structures with predefined paths.\n\n\n• Pydantic Graph is presented as a potential alternative to LangGraph, emphasizing its superior documentation and reliance on type hints. However, it is acknowledged as being designed for advanced users and potentially overkill for simpler applications. The article outlines the following key aspects of Pydantic Graph:\n\n*   **Installation:** The library is installed as a separate package (`pydantic-graph`) and can be used independently of `pydantic-ai`.\n*   **Basic Structure:** Graphs are built from classes inheriting from `BaseNode` with a `run` method that determines the next node to be executed.\n*   **Graph Execution:** The graph executes nodes based on the return value of the `run` method, allowing for flexible graph structures with predefined paths.\n\n6. [LangGraph vs. PydanticAI Comparison](https://sourceforge.net/software/compare/LangGraph-vs-PydanticAI/) (Published: 2025-01-01T00:00:00.000Z)\n\nSummary: This webpage compares LangGraph and PydanticAI, but the provided text focuses on related products: Sendbird (an omnichannel AI agent platform), Vertex AI (for building, deploying, and scaling ML models), Jotform (a no-code platform for data collection with AI-powered agents), and Stack AI (for AI agents that interact with users and complete tasks using internal data and APIs). The main point is to showcase alternatives and related tools in the AI and automation space.\n\n\n7. [Pydantic AI vs LangGraph - Which Data Tool Is Better? (2025)](https://www.youtube.com/watch?v=e0kn7JMH_No) (Published: 2025-04-24T00:00:00.000Z)\n\nSummary: This YouTube video compares Pydantic AI and LangGraph to help viewers choose the right tool for their AI or data workflow projects. It encourages viewers to access AI tools, discounts, and webinars through a provided link.\n\n\n8. [LangChain vs PydanticAI for building an AI Agent - Finn Andersen - Medium](https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d) (Published: 2025-01-29T11:48:36.000Z)\n\nSummary: This article compares LangChain and PydanticAI for building a conversational AI agent with features like dynamic model choice, human-in-the-loop input, tool calling, conversation history, dynamic system prompts, and structured output. It uses the example of an AI waiter taking orders at a restaurant. The author found PydanticAI more approachable and intuitive than LangChain, which they describe as daunting due to its complexity and legacy content. The author then built the same demo project in both frameworks to compare the two.\n\n\n9. [AutoGen vs CrewAI vs LangGraph vs PydanticAI vs Google ADK vs OpenAI Agents .... Which Multi-Agent Framework is Best?](https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs) (Published: 2025-04-30T23:51:34.000Z)\n\nSummary: This article compares six multi-agent frameworks—AutoGen, Google ADK, LangGraph, LLamaIndex, OpenAI Agents SDK, and PydanticAI—across 10 dimensions, including developer experience, async capabilities, and state management. It includes an interactive tool with \"Hello World\" agent implementations for each framework, allowing users to view code, compare implementations, and see quantitative metrics like lines of code and runtime. The article also links to a related article detailing the 10 dimensions used for comparison and guidance on whether a framework is even necessary.\n\n\n10. [LangGraph: What It Is and How To Use It [Tutorial]](https://lazyprogrammer.me/langgraph/) (Published: 2025-01-18T04:31:14.000Z)\n\nSummary: LangGraph is a framework for building AI agents that can handle complex tasks and workflows. It enables the creation of multi-agent systems where multiple AI agents collaborate, dividing up tasks and working together. LangGraph integrates with tools and platforms through the LangChain ecosystem and can be used for customer support automation and e-commerce.\n\n",
  "rag_analysis": [
    {
      "content": "Pydantic AI vs LangGraph - Which Data Tool Is Better? (2025) - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=e0kn7JMH_No"
      }
    },
    {
      "content": "How to use Pydantic Graph (an alternative to LangGraph)\nBartosz Mikulski | Your AI Is Lying to Customers. Let's Fix It Before It Goes Public.\nConsultation\nKnowledge Base\nEngineering Blog\nAI Use Cases\nTools\nAI Readiness Assessment Tool\nAbout me\nNewsletter\nAI\nPydanticAI\nHow to use Pydantic Graph (an alternative to LangGraph)\nA guide to using Pydantic Graph - a type-safe alternative to LangGraph for building AI workflows.\nBartosz Mikulski\n24 Feb 2025\nâ   10 min read\nA Pydantic Graph may be a better alternative to LangGraph. For sure, Pydantic Graph has way better documentation, but if you compare any documentation to the one from LangChain, you set the bar really low. So, what else does it have to offer? As with every Pydantic project, type hints! However, a graph may be an overkill. The PydanticAI authors state in the documentation: âIf youâre not confident a graph-based approach is a good idea, it might be unnecessary.â and âpydantic-graph is designed for advanced users and makes heavy use of Python generics and types hints. It is not designed to be as beginner-friendly as PydanticAI.â If this doesnât scare you off, letâs see how to use it.\nTable of Contents\nPydantic Graph Installation\nBasic Graph Structure in Pydantic Graph\nGraphs with State\nAdding AI Agents to the Graph\nMonitoring and Debugging\nOne more thing. Graph support is in the very early beta stage. If you read this article a couple months after it was published and the code doesnât work anymore, let me know, I will update the text.\nPydantic Graph Installation\nThe graph library is provided as a separate package:\npydantic-graph\n. It has no dependency on\npydantic-ai\n, so if you want to use AI Agents, you must install both. However, the lack of dependencies makes it possible to use the\npydantic-graph\nlibrary for any project that requires graph-based state machines or workflows.\nI will use the library with OpenAI API, so I need to install the PydanticAI client.\npip\ninstall",
      "metadata": {
        "source": "https://mikulskibartosz.name/pydantic-graph"
      }
    },
    {
      "content": "PydanticAI + Langgraph: The Ultimate Match for Smarter AI Agents! - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=P3qH5GVIxD0"
      }
    },
    {
      "content": "Pydantic AI vs LangGraph – Pick The Right Data Validation Tool in 2025! (FULL OVERVIEW!) - YouTube\nAbout\nPress\nCopyright\nContact us\nCreator\nAdvertise\nDevelopers\nTerms\nPrivacy\nPolicy & Safety\nHow YouTube works\nTest new features\n© 2025 Google LLC",
      "metadata": {
        "source": "https://www.youtube.com/watch?v=tAresTJB9cY"
      }
    },
    {
      "content": "def __init__(self, menu_service: MenuService, order_service: OrderService, args: argparse.Namespace):\n# Initialise tools with dependencies\ntools = [\nGetMenuTool(menu_service=menu_service),\nCreateOrderTool(order_service=order_service),\nStructuredResponseTool(),\n]\nself.agent_executor = get_agent_executor(tools=tools, model_name=args.model, api_key=args.api_key)\nself.static_input_content = {\"restaurant_name\": args.restaurant_name, \"table_number\": args.table_number}\nself.config: RunnableConfig = {\"configurable\": {\"session_id\": \"not-even-used\"}}\ndef make_request(self, user_message: str) -> LLMResponse:\nresult = self.agent_executor.invoke(self.static_input_content | {\"input\": user_message}, self.config)\n# De-serialise structured response into an LLMResponse\nresponse = LLMResponse.model_validate_json(result[\"output\"])\nreturn response\nConclusion\nThis demonstration shows that it is much simpler to create a basic conversational and tool-calling AI agent using the PydanticAI framework than LangChain. LangChain has so many layers of deprecated functionality and is in desperate need of some extensive spring cleaning.\nI also wanted to enable streamed responses however this seemed quite difficult to achieve using LangChain with both tool calling and structured output involved.\nI imagine that the newer LangGraph approach for creating agents addresses many of the limitations and frustrations encountered here. PydanticAI has also recently added a\ngraph library\n, so next time I will explore what full graph-based implementations for both frameworks looks like.\nI hope this helps anyone who wants to choose between the frameworks or learn how they can be used to build cool things with AI!\nThe complete project repository can be found\nhere\n.\nLangchain\nLlm\nAI\nPydantic Ai\nAi Agent\n--\n--\n4\nFollow\nWritten by\nFinn Andersen\n221 followers\n·\n22 following\nTech projects and other things on my mind\nFollow\nResponses (\n4\n)\nSee all responses\nHelp\nStatus\nAbout\nCareers\nPress\nBlog\nPrivacy\nRules\nTerms",
      "metadata": {
        "source": "https://medium.com/@finndersen/langchain-vs-pydanticai-for-building-an-ai-agent-e0a059435e9d"
      }
    }
  ]
}
Type of response: <class 'str'>
2025-06-01 22:03:00,078 - __main__ - INFO - Received response from agent
2025-06-01 22:03:00,080 - __main__ - INFO - Displayed search results
2025-06-01 22:03:02,142 - httpx - INFO - HTTP Request: POST https://api.groq.com/openai/v1/chat/completions "HTTP/1.1 200 OK"






## Search Results


<img width="1253" alt="image" src="https://github.com/user-attachments/assets/f0b642b6-f795-45d1-aba1-7f3493e62822" />




## RAG analysis 


<img width="1250" alt="image" src="https://github.com/user-attachments/assets/0115d097-278e-48e9-888e-ed54abcaa1d9" />



## Document Chunk


<img width="1279" alt="image" src="https://github.com/user-attachments/assets/f82af26f-24eb-4973-8c4a-cd48f5ca22f4" />


