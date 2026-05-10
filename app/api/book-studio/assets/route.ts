import { mkdir, writeFile } from "node:fs/promises"
import path from "node:path"
import { NextResponse } from "next/server"
import { DEFAULT_BOOK_ID, getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import { slugify } from "@/src/server/wiki/slug"

export const runtime = "nodejs"

const ALLOWED_TYPES = new Set(["image/png", "image/jpeg", "image/webp", "image/gif"])
const ALLOWED_EXTENSIONS = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif"])

export async function POST(request: Request) {
  const formData = await request.formData()
  const uploaded = formData.get("file")
  const caption = String(formData.get("caption") || "").trim()
  const bookId = sanitizeBookId(String(formData.get("bookId") || DEFAULT_BOOK_ID))
  const chapterPath = String(formData.get("chapterPath") || "").trim()

  if (!uploaded || typeof uploaded === "string" || !("arrayBuffer" in uploaded)) {
    return NextResponse.json({ error: "File immagine mancante" }, { status: 400 })
  }

  const file = uploaded as File
  const extension = path.extname(file.name).toLowerCase()

  if (!ALLOWED_TYPES.has(file.type) || !ALLOWED_EXTENSIONS.has(extension)) {
    return NextResponse.json({ error: "Formato immagine non supportato" }, { status: 400 })
  }

  if (chapterPath) {
    try {
      validateChapterPath(chapterPath, bookId)
    } catch (error) {
      return NextResponse.json(
        { error: error instanceof Error ? error.message : "Chapter path non valido" },
        { status: 400 }
      )
    }
  }

  const store = new FileWikiStore(getWikiRoot())
  const safeName = `${Date.now()}-${slugify(path.basename(file.name, extension))}${extension}`
  const assetPath = `raw/assets/books/${bookId}/${safeName}`
  const absolutePath = store.resolve(assetPath)
  const changedFiles = [assetPath]

  await mkdir(path.dirname(absolutePath), { recursive: true })
  await writeFile(absolutePath, Buffer.from(await file.arrayBuffer()))

  if (chapterPath) {
    const addition = [
      `![[${assetPath}]]`,
      caption ? `_${caption}_` : `_Immagine di supporto editoriale per il capitolo._`
    ].join("\n\n")
    const now = new Date().toISOString()

    await store.appendHeading(chapterPath, "Immagini e layout", addition)
    await store.updateFrontmatter(chapterPath, {
      review_required: true,
      updated_at: now
    })
    await store.appendText(
      "log.md",
      `\n- ${now} | book_studio_asset | ${chapterPath} | asset=${assetPath}`
    )
    changedFiles.push(chapterPath, "log.md")
  }

  return NextResponse.json({
    status: "uploaded",
    asset: {
      path: assetPath,
      name: safeName,
      url: `/api/book-studio/assets/file?path=${encodeURIComponent(assetPath)}`
    },
    changedFiles
  })
}

function validateChapterPath(value: string, bookId: string) {
  const normalized = value.replace(/\\/g, "/")

  if (!normalized.startsWith(`books/${bookId}/chapters/`) || !normalized.endsWith(".md") || normalized.includes("..")) {
    throw new Error("Chapter path non valido")
  }
}

function sanitizeBookId(value: string) {
  return /^[a-z0-9-]+$/.test(value) ? value : DEFAULT_BOOK_ID
}
