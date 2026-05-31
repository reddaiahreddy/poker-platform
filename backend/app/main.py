from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="Poker Platform",
    version="1.0.0"
)

app.include_router(v1_router, prefix="/api/v1")
app.include_router(v1_router)

@app.get("/")
def root():
    return {"message": "Poker Platform API running"}