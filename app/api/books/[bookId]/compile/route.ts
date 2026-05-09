import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { BookWriterAgent } from "@/src/server/agents/book-writer-agent"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function POST(
  _request: Request,
  context: { params: Promise<{ bookId: string }> }
) {
  const { bookId } = await context.params
  const agent = new BookWriterAgent(new FileWikiStore(getWikiRoot()))
  const result = await agent.compileDemoBook(bookId)

  return NextResponse.json(result)
}

