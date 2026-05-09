import { NextResponse } from "next/server"
import { getObsidianConfig } from "@/src/server/config"
import { ObsidianLocalRestClient } from "@/src/server/obsidian/client"

export async function GET() {
  const client = new ObsidianLocalRestClient(getObsidianConfig())
  const health = await client.health()

  return NextResponse.json(health, { status: health.ok ? 200 : 503 })
}

