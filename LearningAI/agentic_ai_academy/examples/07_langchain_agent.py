"""Requires: pip install langchain langchain-openai and OPENAI_API_KEY."""
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def get_policy(topic: str) -> str:
    """Return the demonstration policy for a topic."""
    return {"refund": "Demo refund window: 14 days."}.get(topic.lower(), "No matching policy")

agent = create_agent(model="openai:gpt-4.1-mini", tools=[get_policy],
                     system_prompt="Answer policy questions; call get_policy when relevant.")

if __name__ == "__main__":
    result = agent.invoke({"messages": [{"role": "user", "content": "Explain refund policy"}]})
    print(result["messages"][-1].content)
