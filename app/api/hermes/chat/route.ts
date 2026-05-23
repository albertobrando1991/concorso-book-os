import { NextResponse } from "next/server"
import { HermesLlmClient } from "@/src/server/llm/hermes-adapter"
import type { LlmMessage } from "@/src/server/llm/openai-adapter"

export const runtime = "nodejs"

export async function POST(request: Request) {
  const body = (await request.json()) as { messages?: LlmMessage[] }

  if (!Array.isArray(body.messages) || body.messages.length === 0) {
    return NextResponse.json({ error: "messages is required" }, { status: 400 })
  }

  const messages = body.messages.filter((message) =>
    ["system", "user", "assistant"].includes(message.role) && typeof message.content === "string"
  )

  if (messages.length === 0) {
    return NextResponse.json({ error: "messages must contain valid role/content pairs" }, { status: 400 })
  }

  const client = new HermesLlmClient()
  const message = await client.complete(messages)

  return NextResponse.json({ message })
}
