import { NextResponse } from "next/server"
import { EditorialReviewerAgent } from "@/src/server/agents/editorial-reviewer-agent"
import { getWikiRoot, WRITER_PROVIDERS, type WriterProvider } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import type { ReviewScope } from "@/src/server/agents/editorial-reviewer-agent"

const VALID_SCOPES: ReviewScope[] = ["full", "chapter", "aspect"]

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as {
      bookId?: string
      scope?: ReviewScope
      chapterPath?: string
      aspect?: string
      provider?: WriterProvider
    }

    if (!body.bookId) {
      return NextResponse.json({ error: "bookId is required" }, { status: 400 })
    }

    if (body.scope && !VALID_SCOPES.includes(body.scope)) {
      return NextResponse.json({ error: "Invalid scope. Use: full, chapter, aspect" }, { status: 400 })
    }

    if (body.provider && !WRITER_PROVIDERS.includes(body.provider)) {
      return NextResponse.json({ error: "Invalid provider" }, { status: 400 })
    }

    if (body.scope === "chapter" && !body.chapterPath) {
      return NextResponse.json({ error: "chapterPath is required when scope is 'chapter'" }, { status: 400 })
    }

    const agent = new EditorialReviewerAgent(new FileWikiStore(getWikiRoot()))
    const result = await agent.runReview({
      bookId: body.bookId,
      scope: body.scope || "full",
      chapterPath: body.chapterPath,
      aspect: body.aspect,
      provider: body.provider
    })

    return NextResponse.json(result)
  } catch (error) {
    const message = error instanceof Error ? error.message : "Revisione editoriale fallita"
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
