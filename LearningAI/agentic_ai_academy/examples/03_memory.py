"""Bounded memory; intentionally no secrets or durable persistence."""
from collections import deque

class ConversationMemory:
    def __init__(self, max_messages: int = 6):
        self.messages = deque(maxlen=max_messages)

    def add(self, role: str, content: str) -> None:
        if role not in ("user", "assistant"):
            raise ValueError("Invalid role")
        self.messages.append({"role": role, "content": content})

    def context(self) -> list[dict[str, str]]:
        return list(self.messages)

if __name__ == "__main__":
    m = ConversationMemory(2)
    m.add("user", "Hello")
    m.add("assistant", "Hi")
    m.add("user", "Again")
    print(m.context())
