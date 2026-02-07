from fastapi import APIRouter, HTTPException
from app.core.gemini_client import call_gemini
from app.core.luxora_prompt import build_luxora_system_prompt

router = APIRouter()

@router.post("/chat")
def chat(
    message: str,
    mode: str = "core",
    model: str = "fast"
):
    system_prompt = build_luxora_system_prompt(mode=mode)
    response = call_gemini(system_prompt, message, model)

    return {
        "ai": "LuxoraAI",
        "model": model,
        "mode": mode,
        "response": response
    }
