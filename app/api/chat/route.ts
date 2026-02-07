export const runtime = "edge";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const message = body.message;
    const model = body.model ?? "fast";
    const mode = body.mode ?? "core";

    if (!message) {
      return Response.json(
        { error: "Message is required" },
        { status: 400 }
      );
    }

    const MODEL_MAP: Record<string, string> = {
      fast: "models/gemini-1.5-flash",
      deep: "models/gemini-1.5-pro"
    };

    const systemPrompt = `
You are LuxoraAI.
You are calm, precise, and thoughtful.
Mode: ${mode}
Style: ${model === "deep" ? "Reason step by step." : "Be concise."}
`;

    const geminiRes = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/${MODEL_MAP[model]}:generateContent?key=${process.env.GEMINI_API_KEY}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          contents: [
            {
              role: "user",
              parts: [{ text: `${systemPrompt}\n\nUser: ${message}` }]
            }
          ]
        })
      }
    );

    const data = await geminiRes.json();

    const text =
      data?.candidates?.[0]?.content?.parts?.[0]?.text ??
      "LuxoraAI couldn’t generate a response this time.";

    return Response.json({
      ai: "LuxoraAI",
      model,
      response: text
    });

  } catch (err: any) {
    return Response.json(
      {
        error: "LuxoraAI function crashed",
        detail: err?.message ?? "Unknown error"
      },
      { status: 500 }
    );
  }
}
