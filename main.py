from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/ask")
def ask_agent(data: Question):
    return {
        "answer": (
            "A GenAI agent is a software program that understands your question, "
            "thinks using AI logic, and generates a helpful response automatically."
        )
    }