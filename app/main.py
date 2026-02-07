from fastapi import FastAPI
from app.api import chat
from app.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(chat.router, prefix="/api")

@app.get("/")
def health():
    return {"status": "LuxoraAI is running"}
