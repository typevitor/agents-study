from mcp.server.fastmcp import FastMCP
import time

mcp = FastMCP(
    "get_time_server", 
    "A simple MCP server that provides the current time."
)

@mcp.tool()
async def get_time() -> str:
    """Get the current time.
    """
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    return curr_clock

if __name__ == "__main__":
    mcp.run(transport='stdio')