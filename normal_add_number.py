import random
from fastmcp import FastMCP

mcp = FastMCP(name='MCP_DEMO_SERVER')

@mcp.tool
def roll_dice(n_dice : int = 1) -> list[int]:
    """Roll n dice and return the results as a list of integers."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a : int, b : int) -> int:
    """
    Adds two numbers
    """
    return a + b

if __name__ == "__main__":
    mcp.run(transport='http')