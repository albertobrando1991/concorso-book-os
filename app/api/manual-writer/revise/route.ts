import { NextResponse } from "next/server"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { getWikiRoot, WRITER_PROVIDERS, type WriterProvider } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as {
      chapterPath?: string
      instruction?: string
      provider?: WriterProvider
    }

    if (!body.chapterPath) {
      return NextResponse.json({ error: "chapterPath is required" }, { status: 400 })
    }

    if (body.provider && !WRITER_PROVIDERS.includes(body.provider)) {
      return NextResponse.json({ error: "Invalid provider" }, { status: 400 })
    }

    const agent = new ManualWriterAgent(new FileWikiStore(getWikiRoot()))
    const result = await agent.reviseChapter({
      chapterPath: body.chapterPath,
      instruction: body.instruction || "",
      provider: body.provider
    })

    return NextResponse.json(result)
  } catch (error) {
    const message = error instanceof Error ? error.message : "Humanizer revision failed"
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
