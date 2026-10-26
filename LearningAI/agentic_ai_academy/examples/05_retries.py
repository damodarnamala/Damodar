"""Retry transient errors only; do not retry non-idempotent writes blindly."""
import time

def retry(operation, attempts: int = 3, delay: float = 0.01):
    for index in range(attempts):
        try:
            return operation()
        except ConnectionError:
            if index == attempts - 1:
                raise
            time.sleep(delay * (2 ** index))

if __name__ == "__main__":
    calls = [0]
    def flaky():
        calls[0] += 1
        if calls[0] < 3:
            raise ConnectionError("transient")
        return "success"
    print(retry(flaky))
