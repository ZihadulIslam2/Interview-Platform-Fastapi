from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(tittle=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Interview Platform API running"}