import { NextResponse } from "next/server"
import { HermesLlmClient } from "@/src/server/llm/hermes-adapter"

export async function GET() {
  const health = await new HermesLlmClient().health()

  return NextResponse.json(health, { status: health.ok ? 200 : 503 })
}
