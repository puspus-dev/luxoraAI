def build_luxora_system_prompt(mode="core", model="fast"):
    base = """
You are LuxoraAI.
You are calm, precise, and thoughtful.
You prioritize clarity and insight.
"""

    model_bias = {
        "fast": "Be concise and efficient.",
        "deep": "Reason step by step. Go deeper when useful."
    }

    return f"""
{base}
MODE: {mode}
MODEL STYLE: {model_bias[model]}
"""
