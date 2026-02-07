import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODELS = 
    "fast": "models/gemini-1.5-flash",
    "deep": "models/gemini-1.5-pro"
  APP_NAME = "LuxoraAI"

settings = Settings()
