from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is working"}

@app.get("/test")
def test():
    return {"test": "ok"}
