import { NextResponse } from "next/server"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import type { ManualWriterMode } from "@/src/server/agents/manual-writer-agent"

export async function POST(request: Request) {
  const body = (await request.json()) as {
    chapterPath?: string
    instruction?: string
    mode?: ManualWriterMode
  }

  if (!body.chapterPath) {
    return NextResponse.json({ error: "chapterPath is required" }, { status: 400 })
  }

  const mode = body.mode || "draft"

  if (!["draft", "expand", "improve", "integrate", "format"].includes(mode)) {
    return NextResponse.json({ error: "Invalid mode" }, { status: 400 })
  }

  const agent = new ManualWriterAgent(new FileWikiStore(getWikiRoot()))
  const result = await agent.writeChapter({
    chapterPath: body.chapterPath,
    instruction: body.instruction || "",
    mode
  })

  return NextResponse.json(result)
}
