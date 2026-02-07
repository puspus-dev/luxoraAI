def call_gemini(system_prompt: str, user_message: str, model: str):
    model_name = settings.GEMINI_MODELS.get(model, "models/gemini-1.5-flash")

    url = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent"

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
        f"{url}?key={settings.GEMINI_API_KEY}",
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
