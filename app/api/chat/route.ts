export const runtime = "nodejs";

export async function POST(req: Request) {
  const { message } = await req.json();

  return Response.json({
    ai: "LuxoraAI",
    response: "Node runtime works."
  });
}
