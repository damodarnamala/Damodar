"""Illustrates approval tied to an exact proposed action digest."""
import hashlib
import json

def digest(action: dict) -> str:
    data = json.dumps(action, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()

class ApprovalGate:
    def __init__(self):
        self.approved = set()

    def authorize(self, action: dict, reviewer: str):
        if not reviewer:
            raise ValueError("Reviewer identity required")
        self.approved.add(digest(action))

    def permitted(self, action: dict) -> bool:
        return digest(action) in self.approved

if __name__ == "__main__":
    gate = ApprovalGate()
    action = {"type": "deploy", "version": "1.0.0"}
    gate.authorize(action, "authorized-reviewer-demo")
    assert gate.permitted(action)
    assert not gate.permitted({**action, "version": "2.0.0"})
    print("Approval is action-specific")
