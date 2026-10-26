"""Requires: pip install 'mcp[cli]'. Example for MCP Python SDK v2."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Learning Tools")

@mcp.tool()
def calculate_total(price: float, quantity: int) -> float:
    """Compute a total, with basic argument validation."""
    if price < 0 or quantity < 0:
        raise ValueError("Non-negative values required")
    return round(price * quantity, 2)

@mcp.resource("guide://intro")
def introduction() -> str:
    return "This server offers learning-only arithmetic tools."

if __name__ == "__main__":
    mcp.run()
