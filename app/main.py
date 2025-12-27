from fastapi import FastAPI
from .config import settings  # relative import

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Backend API for AI Resume Analyzer"
)

@app.get("/health")
def health_check():
    return {"status": "OK", "environment": settings.ENV}

@app.get("/")
def root():
    return {"message": "Welcome to AI Resume Analyzer API"}
