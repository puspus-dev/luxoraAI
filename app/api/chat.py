from fastapi import APIRouter, HTTPException
from app.core.gemini_client import call_gemini
from app.core.luxora_prompt import build_luxora_system_prompt

router = APIRouter()

@router.post("/chat")
def chat_with_luxora(
    message: str,
    role: str = "explore",
    mode: str = "core"
):
    try:
        system_prompt = build_luxora_system_prompt(role, mode)
        response = call_gemini(system_prompt, message)
        return {
            "ai": "LuxoraAI",
            "mode": mode,
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
