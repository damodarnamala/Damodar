"""Requires: pip install openai-agents and OPENAI_API_KEY."""
from agents import Agent, Runner, function_tool

@function_tool
def get_shipping_fee(country: str) -> str:
    """Return demonstration shipping fees for a country."""
    return {"India": "₹100", "USA": "$10"}.get(country, "Unknown")

agent = Agent(
    name="Shipping Assistant",
    instructions="Help with demo shipping fee questions. Use the tool for prices.",
    tools=[get_shipping_fee],
)

if __name__ == "__main__":
    result = Runner.run_sync(agent, "What is the shipping fee for India?")
    print(result.final_output)
