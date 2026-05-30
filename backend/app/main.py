from fastapi import FastAPI

app = FastAPI(
    title="Poker Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Poker Platform API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }