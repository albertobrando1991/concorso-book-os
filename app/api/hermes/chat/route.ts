import { NextResponse } from "next/server"
import { parseHermesReply, withHermesNoReplyCapability } from "@/src/server/hermes/no-reply"
import { HermesLlmClient } from "@/src/server/llm/hermes-adapter"
import type { LlmMessage } from "@/src/server/llm/openai-adapter"

export const runtime = "nodejs"

interface HermesChatRequest {
  messages?: LlmMessage[]
  allowNoReply?: boolean
  noReply?: boolean
  respond?: boolean
}

export async function POST(request: Request) {
  const body = (await request.json()) as HermesChatRequest

  if (body.respond === false || body.noReply === true) {
    return new Response(null, { status: 204 })
  }

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
  const message = await client.complete(withHermesNoReplyCapability(messages, body.allowNoReply === true))
  const reply = parseHermesReply(message)

  if (body.allowNoReply === true && !reply.shouldReply) {
    return new Response(null, { status: 204 })
  }

  return NextResponse.json({ message: reply.message, shouldReply: reply.shouldReply })
}
