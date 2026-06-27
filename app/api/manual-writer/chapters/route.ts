import { NextResponse } from "next/server"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function GET(request: Request) {
  const url = new URL(request.url)
  const bookId = url.searchParams.get("bookId") || undefined

  const agent = new ManualWriterAgent(new FileWikiStore(getWikiRoot()))
  const chapters = await agent.listChapters(bookId)

  return NextResponse.json({ chapters })
}

