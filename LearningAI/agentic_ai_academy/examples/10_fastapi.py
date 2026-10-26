"""Requires: pip install fastapi uvicorn. Run: uvicorn 10_fastapi:app --reload"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Agent Task Demo")

class TaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=500)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks")
def create_task(request: TaskRequest):
    # Educational stub, not a durable worker queue.
    return {"status": "received", "task": request.task}
