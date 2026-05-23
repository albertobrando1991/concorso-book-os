import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { importSourceForHermes, type HermesSourceImportInput } from "@/src/server/hermes/source-import"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export const runtime = "nodejs"

export async function POST(request: Request) {
  if (!isAuthorized(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const input = (await request.json()) as HermesSourceImportInput

  if (!input.url && !input.query) {
    return NextResponse.json({ error: "url or query is required" }, { status: 400 })
  }

  try {
    const result = await importSourceForHermes(input, new FileWikiStore(getWikiRoot()))

    return NextResponse.json(result)
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Hermes source import failed" },
      { status: 500 }
    )
  }
}

function isAuthorized(request: Request) {
  const secret = process.env.HERMES_WEBHOOK_SECRET

  if (!secret) return true

  return request.headers.get("authorization") === `Bearer ${secret}`
}
