from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Health check
@app.get("/")
def root():
    return {"status": "Backend is live 🚀"}

@app.get("/test")
def test():
    return {"test": "ok"}

# Request model
class Question(BaseModel):
    question: str

# AI endpoint
@app.post("/ask")
def ask(data: Question):
    return {
        "question": data.question,
        "answer": "This is a sample answer from the backend"
    }
