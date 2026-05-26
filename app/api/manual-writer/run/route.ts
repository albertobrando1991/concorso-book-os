import { NextResponse } from "next/server"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { getWikiRoot, type WriterProvider } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import type { ManualWriterMode } from "@/src/server/agents/manual-writer-agent"

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as {
      chapterPath?: string
      instruction?: string
      mode?: ManualWriterMode
      provider?: WriterProvider
    }

    if (!body.chapterPath) {
      return NextResponse.json({ error: "chapterPath is required" }, { status: 400 })
    }

    const mode = body.mode || "draft"

    if (!["draft", "expand", "improve", "integrate", "format"].includes(mode)) {
      return NextResponse.json({ error: "Invalid mode" }, { status: 400 })
    }

    if (body.provider && !["codex", "claude", "openai", "hermes", "local"].includes(body.provider)) {
      return NextResponse.json({ error: "Invalid provider" }, { status: 400 })
    }

    const agent = new ManualWriterAgent(new FileWikiStore(getWikiRoot()))
    const result = await agent.writeChapter({
      chapterPath: body.chapterPath,
      instruction: body.instruction || "",
      mode,
      provider: body.provider
    })

    return NextResponse.json(result)
  } catch (error) {
    const message = error instanceof Error ? error.message : "Manual Writer Agent failed"
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
