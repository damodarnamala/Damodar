"""Deterministic prerequisite scheduler and cycle detection."""
def schedule(tasks: dict[str, list[str]]) -> list[str]:
    result, completed = [], set()
    unknown = {d for deps in tasks.values() for d in deps} - set(tasks)
    if unknown:
        raise ValueError(f"Unknown dependencies: {unknown}")
    while len(completed) < len(tasks):
        ready = sorted(k for k, deps in tasks.items()
                       if k not in completed and set(deps) <= completed)
        if not ready:
            raise ValueError("Dependency cycle")
        result.extend(ready)
        completed.update(ready)
    return result

if __name__ == "__main__":
    tasks = {"requirements": [], "code": ["requirements"],
             "tests": ["code"], "review": ["tests"]}
    print(schedule(tasks))
