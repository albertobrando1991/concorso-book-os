import { NextResponse } from "next/server"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { DEFAULT_BOOK_ID, getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function GET(request: Request) {
  const url = new URL(request.url)
  const bookId = sanitizeBookId(url.searchParams.get("bookId") || DEFAULT_BOOK_ID)
  const data = await buildBookStudioData(new FileWikiStore(getWikiRoot()), bookId)

  return NextResponse.json(data)
}

function sanitizeBookId(value: string) {
  return /^[a-z0-9-]+$/.test(value) ? value : DEFAULT_BOOK_ID
}
