"""Requires: pip install langgraph. No model or API key needed."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    task: str
    approved: bool
    result: str

def classify(state: State):
    return {"approved": state["task"].startswith("read:")}

def route(state: State) -> str:
    return "execute" if state["approved"] else "deny"

def execute(state: State):
    return {"result": "Completed safe read-only demo"}

def deny(state: State):
    return {"result": "Denied: requires approval"}

builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("execute", execute)
builder.add_node("deny", deny)
builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route, {"execute": "execute", "deny": "deny"})
builder.add_edge("execute", END)
builder.add_edge("deny", END)
graph = builder.compile()

if __name__ == "__main__":
    print(graph.invoke({"task": "read: status", "approved": False, "result": ""}))
