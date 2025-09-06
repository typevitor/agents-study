from dotenv import load_dotenv
from agents import Agent, Runner, trace
from agents.mcp import MCPServerStdio
from IPython.display import display
import asyncio

load_dotenv(override=True)

params = {"command": "uv", "args": ["run", "server.py"]}

async def get_time() -> str:
    async with MCPServerStdio(
        params=params, 
        client_session_timeout_seconds=30
    ) as mcp_server:
        agent = Agent(
            name="Time Agent", 
            instructions="You are a Time agent that use the tool to get the current time", model="gpt-4o-mini", 
            mcp_servers=[mcp_server]
        )
        with trace("timer_agent"):
            result = await Runner.run(agent, "What is the current time?")
            display(result.final_output)

if __name__ == "__main__":
    asyncio.run(get_time())