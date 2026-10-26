"""Validated tool registry using only Python standard library."""
from dataclasses import dataclass
from collections.abc import Callable

@dataclass(frozen=True)
class ToolSpec:
    name: str
    fn: Callable[[int, int], int]

def multiply(a: int, b: int) -> int:
    return a * b

REGISTRY = {"multiply": ToolSpec("multiply", multiply)}

def execute(name: str, arguments: dict) -> int:
    if name not in REGISTRY:
        raise PermissionError("Unknown or prohibited tool")
    if set(arguments) != {"a", "b"} or any(type(v) is not int for v in arguments.values()):
        raise ValueError("Arguments must be integer a and b")
    return REGISTRY[name].fn(**arguments)

if __name__ == "__main__":
    print(execute("multiply", {"a": 6, "b": 7}))
