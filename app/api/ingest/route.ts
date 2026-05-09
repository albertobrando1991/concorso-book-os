import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { IngestAgent } from "@/src/server/agents/ingest-agent"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import type { SourceInput } from "@/src/server/wiki/types"

export async function POST(request: Request) {
  const input = (await request.json()) as SourceInput

  if (!input.title || !input.content || !input.sourceType) {
    return NextResponse.json(
      { error: "title, content and sourceType are required" },
      { status: 400 }
    )
  }

  const agent = new IngestAgent(new FileWikiStore(getWikiRoot()))
  const result = await agent.ingest(input)

  return NextResponse.json(result)
}

