from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from prompt import medicine_prompt
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio

cfg = RunnableConfig(recursion_limit=100)

def initialize_model(google_api_key: str) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=google_api_key
    )

async def setup_agent(google_api_key: str, youtube_pipedream_url: str):
    tools_config = {
        "youtube": {
            "url": youtube_pipedream_url,
            "transport": "streamable_http"
        }
    }
    mcp_client = MultiServerMCPClient(tools_config)
    tools = await mcp_client.get_tools()
    agent = create_react_agent(initialize_model(google_api_key), tools)
    return agent

def run_agent_sync(google_api_key: str, youtube_pipedream_url: str, user_goal: str) -> dict:
    async def _run():
        agent = await setup_agent(google_api_key, youtube_pipedream_url)
        full_prompt = user_goal + "\n" + medicine_prompt
        result = await agent.ainvoke({"messages": [HumanMessage(content=full_prompt)]}, config=cfg)
        return result

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(_run())
    finally:
        loop.close()
