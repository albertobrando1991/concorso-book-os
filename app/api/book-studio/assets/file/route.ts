import { readFile } from "node:fs/promises"
import { NextResponse } from "next/server"
import { getAssetContentType, normalizeAssetPath } from "@/src/server/book/book-preview"
import { getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function GET(request: Request) {
  const url = new URL(request.url)
  const requestedPath = url.searchParams.get("path")

  if (!requestedPath) {
    return NextResponse.json({ error: "Parametro path mancante" }, { status: 400 })
  }

  const store = new FileWikiStore(getWikiRoot())

  try {
    const assetPath = normalizeAssetPath(requestedPath)
    const absolutePath = store.resolve(assetPath)
    const buffer = await readFile(absolutePath)

    return new NextResponse(buffer, {
      headers: {
        "Content-Type": getAssetContentType(assetPath),
        "Cache-Control": "no-store"
      }
    })
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Asset non disponibile" },
      { status: 404 }
    )
  }
}
