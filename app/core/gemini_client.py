import requests
from app.config import settings

GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/"
    f"{settings.GEMINI_MODEL}:generateContent"
)

def call_gemini(system_prompt: str, user_message: str) -> str:
    headers = {"Content-Type": "application/json"}

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": f"{system_prompt}\n\nUser: {user_message}"}
                ]
            }
        ]
    }

    response = requests.post(
        f"{GEMINI_URL}?key={settings.GEMINI_API_KEY}",
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]
