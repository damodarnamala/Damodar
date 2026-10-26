"""No API key needed. A deterministic agent-like tool loop."""
from dataclasses import dataclass

@dataclass
class Action:
    name: str
    a: float = 0
    b: float = 0

def add(a: float, b: float) -> float:
    return a + b

def run(goal: str, max_steps: int = 3) -> str:
    tools = {"add": add}
    history = []
    for _ in range(max_steps):
        if not history:
            action = Action("add", 12, 30) if goal == "add" else Action("final")
        else:
            return f"Result: {history[-1]}"
        if action.name == "final":
            return "Unsupported request"
        if action.name not in tools:
            raise ValueError("Not allowed")
        history.append(tools[action.name](action.a, action.b))
    raise RuntimeError("Step limit")

if __name__ == "__main__":
    assert run("add") == "Result: 42"
    print(run("add"))
