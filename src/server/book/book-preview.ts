import { readdir, stat } from "node:fs/promises"
import path from "node:path"
import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"

export type ChapterContentState = "written" | "draft" | "structure"

export interface MarkdownBlock {
  type: "heading" | "paragraph" | "list" | "image" | "code"
  text?: string
  level?: number
  items?: string[]
  ordered?: boolean
  path?: string
  alt?: string
}

export interface BookStudioChapter {
  path: string
  title: string
  outlineSection: string
  status: string
  draftStage: string
  reviewRequired: boolean
  topics: string[]
  sourceRefs: string[]
  wordCount: number
  contentState: ChapterContentState
  blocks: MarkdownBlock[]
}

export interface BookStudioAsset {
  path: string
  name: string
  size: number
  updatedAt: string
}

export interface BookStudioData {
  bookId: string
  title: string
  updatedAt: string
  summary: {
    chapters: number
    written: number
    draft: number
    structure: number
    reviewRequired: number
    assets: number
  }
  chapters: BookStudioChapter[]
  assets: BookStudioAsset[]
}

const EDITORIAL_PLACEHOLDERS = [
  "da sviluppare con manual writer agent",
  "da sviluppare",
  "bozza da generare"
]

const IMAGE_EXTENSIONS = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif"])

export async function buildBookStudioData(store: FileWikiStore, bookId = "il-metodo-bando"): Promise<BookStudioData> {
  const bookPath = `books/${bookId}/index.md`
  const bookContent = await store.exists(bookPath).then((exists) => exists ? store.readText(bookPath) : "")
  const book = parseFrontmatter(bookContent)
  const chapterFiles = (await store.listMarkdown(`books/${bookId}/chapters`))
    .filter((file) => file.endsWith(".md"))
  const chapters: BookStudioChapter[] = []

  for (const file of chapterFiles) {
    const content = await store.readText(file)
    const parsed = parseFrontmatter(content)
    const preview = selectPreviewMarkdown(parsed.body)

    chapters.push({
      path: file,
      title: String(parsed.data.title || titleFromPath(file)),
      outlineSection: String(parsed.data.outline_section || ""),
      status: String(parsed.data.status || "draft"),
      draftStage: String(parsed.data.draft_stage || ""),
      reviewRequired: Boolean(parsed.data.review_required),
      topics: asStringArray(parsed.data.topics),
      sourceRefs: asStringArray(parsed.data.source_refs),
      wordCount: countWords(preview.markdown),
      contentState: preview.state,
      blocks: markdownToBlocks(preview.markdown)
    })
  }

  chapters.sort(compareStudioChapters)
  const assets = await listBookAssets(store, bookId)

  return {
    bookId,
    title: String(book.data.title || "Il Metodo BANDO"),
    updatedAt: new Date().toISOString(),
    summary: {
      chapters: chapters.length,
      written: chapters.filter((chapter) => chapter.contentState === "written").length,
      draft: chapters.filter((chapter) => chapter.contentState === "draft").length,
      structure: chapters.filter((chapter) => chapter.contentState === "structure").length,
      reviewRequired: chapters.filter((chapter) => chapter.reviewRequired).length,
      assets: assets.length
    },
    chapters,
    assets
  }
}

export function normalizeAssetPath(value: string) {
  const normalized = value.replace(/\\/g, "/").replace(/^\/+/, "")

  if (!normalized.startsWith("raw/assets/")) {
    throw new Error("Asset path non valido")
  }

  if (normalized.includes("..")) {
    throw new Error("Asset path non valido")
  }

  return normalized
}

export function getAssetContentType(filePath: string) {
  const extension = path.extname(filePath).toLowerCase()

  if (extension === ".png") return "image/png"
  if (extension === ".jpg" || extension === ".jpeg") return "image/jpeg"
  if (extension === ".webp") return "image/webp"
  if (extension === ".gif") return "image/gif"

  return "application/octet-stream"
}

function selectPreviewMarkdown(body: string): { state: ChapterContentState; markdown: string } {
  const editorial = extractHeadingSection(body, "Testo editoriale")

  if (isSubstantial(editorial)) {
    return { state: "written", markdown: editorial }
  }

  const agentDraft = extractHeadingSection(body, "Bozza agente")

  if (isSubstantial(agentDraft)) {
    return { state: "draft", markdown: agentDraft }
  }

  const bodyWithoutEmptyEditorial = removeEmptyEditorialSections(body)

  if (isSubstantial(bodyWithoutEmptyEditorial)) {
    return { state: "draft", markdown: bodyWithoutEmptyEditorial }
  }

  return {
    state: "structure",
    markdown: "## Struttura capitolo\nQuesto capitolo e' presente nell'outline, ma deve ancora essere sviluppato dal Manual Writer Agent."
  }
}

function removeEmptyEditorialSections(value: string) {
  let next = value

  for (const heading of ["Testo editoriale", "Bozza agente"]) {
    const section = extractHeadingSection(next, heading)

    if (section && !isSubstantial(section)) {
      next = replaceHeadingSectionWithPlaceholder(next, heading)
    }
  }

  return next.trim()
}

function replaceHeadingSectionWithPlaceholder(content: string, heading: string) {
  const lines = content.replace(/\r\n/g, "\n").split("\n")
  const start = findHeading(lines, heading)

  if (start === -1) return content

  const level = headingLevel(lines[start])
  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    const nextLevel = headingLevel(lines[index])

    if (nextLevel > 0 && nextLevel <= level) {
      end = index
      break
    }
  }

  return [...lines.slice(0, start), ...lines.slice(end)].join("\n")
}

function extractHeadingSection(content: string, heading: string) {
  const lines = content.replace(/\r\n/g, "\n").split("\n")
  const start = findHeading(lines, heading)

  if (start === -1) return ""

  const level = headingLevel(lines[start])
  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    const nextLevel = headingLevel(lines[index])

    if (nextLevel > 0 && nextLevel <= level) {
      end = index
      break
    }
  }

  return lines.slice(start + 1, end).join("\n").trim()
}

function markdownToBlocks(markdown: string): MarkdownBlock[] {
  const blocks: MarkdownBlock[] = []
  const lines = markdown.replace(/\r\n/g, "\n").split("\n")
  let paragraph: string[] = []
  let listItems: string[] = []
  let listOrdered = false
  let codeLines: string[] = []
  let inCode = false

  function flushParagraph() {
    const text = paragraph.join(" ").replace(/\s+/g, " ").trim()

    if (text) {
      blocks.push({ type: "paragraph", text: cleanInlineText(text) })
    }

    paragraph = []
  }

  function flushList() {
    if (listItems.length > 0) {
      blocks.push({ type: "list", items: listItems.map(cleanInlineText), ordered: listOrdered })
    }

    listItems = []
    listOrdered = false
  }

  function flushCode() {
    if (codeLines.length > 0) {
      blocks.push({ type: "code", text: codeLines.join("\n") })
    }

    codeLines = []
  }

  for (const rawLine of lines) {
    const line = rawLine.trimEnd()

    if (line.trim().startsWith("```")) {
      if (inCode) {
        inCode = false
        flushCode()
      } else {
        flushParagraph()
        flushList()
        inCode = true
      }
      continue
    }

    if (inCode) {
      codeLines.push(rawLine)
      continue
    }

    const image = parseImage(line.trim())

    if (image) {
      flushParagraph()
      flushList()
      blocks.push(image)
      continue
    }

    const heading = /^(#{1,6})\s+(.+?)\s*$/.exec(line)

    if (heading) {
      flushParagraph()
      flushList()
      blocks.push({
        type: "heading",
        level: Math.min(heading[1].length, 4),
        text: cleanInlineText(heading[2])
      })
      continue
    }

    const unordered = /^\s*[-*]\s+(.+)$/.exec(line)
    const ordered = /^\s*\d+[.)]\s+(.+)$/.exec(line)

    if (unordered || ordered) {
      flushParagraph()

      if (listItems.length > 0 && listOrdered !== Boolean(ordered)) {
        flushList()
      }

      listOrdered = Boolean(ordered)
      listItems.push((ordered?.[1] || unordered?.[1] || "").trim())
      continue
    }

    if (!line.trim()) {
      flushParagraph()
      flushList()
      continue
    }

    paragraph.push(line.trim())
  }

  flushParagraph()
  flushList()
  flushCode()

  return blocks.slice(0, 260)
}

function parseImage(line: string): MarkdownBlock | null {
  const obsidian = /^!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]$/.exec(line)

  if (obsidian) {
    return {
      type: "image",
      path: obsidian[1].trim(),
      alt: obsidian[2]?.trim() || titleFromPath(obsidian[1])
    }
  }

  const markdown = /^!\[([^\]]*)\]\(([^)]+)\)$/.exec(line)

  if (markdown) {
    return {
      type: "image",
      path: markdown[2].trim(),
      alt: markdown[1].trim() || titleFromPath(markdown[2])
    }
  }

  return null
}

function cleanInlineText(value: string) {
  return value
    .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, "$2")
    .replace(/\[\[([^\]]+)\]\]/g, (_, target: string) => titleFromPath(target))
    .replace(/\*\*(.*?)\*\*/g, "$1")
    .replace(/\*(.*?)\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .trim()
}

async function listBookAssets(store: FileWikiStore, bookId: string): Promise<BookStudioAsset[]> {
  const assetRoot = store.resolve(`raw/assets/books/${bookId}`)
  const root = store.resolve("")

  if (!assetRoot.startsWith(root)) return []

  return walkAssets(assetRoot, root)
}

async function walkAssets(directory: string, wikiRoot: string): Promise<BookStudioAsset[]> {
  let entries: Array<{ name: string; isDirectory(): boolean }>

  try {
    entries = await readdir(directory, { withFileTypes: true })
  } catch {
    return []
  }

  const assets: BookStudioAsset[] = []

  for (const entry of entries) {
    const absolute = path.join(directory, entry.name)

    if (entry.isDirectory()) {
      assets.push(...await walkAssets(absolute, wikiRoot))
      continue
    }

    if (!IMAGE_EXTENSIONS.has(path.extname(entry.name).toLowerCase())) continue

    const details = await stat(absolute)
    assets.push({
      path: path.relative(wikiRoot, absolute).replace(/\\/g, "/"),
      name: entry.name,
      size: details.size,
      updatedAt: details.mtime.toISOString()
    })
  }

  return assets.sort((left, right) => right.updatedAt.localeCompare(left.updatedAt))
}

function findHeading(lines: string[], heading: string) {
  const target = heading.trim().toLowerCase()

  return lines.findIndex((line) => {
    const match = /^(#{1,6})\s+(.+?)\s*$/.exec(line)
    return Boolean(match && match[2].trim().toLowerCase() === target)
  })
}

function headingLevel(line: string) {
  const match = /^(#{1,6})\s+/.exec(line)

  return match ? match[1].length : 0
}

function isSubstantial(value: string) {
  const normalized = value.replace(/\s+/g, " ").trim().toLowerCase()

  if (!normalized) return false
  if (EDITORIAL_PLACEHOLDERS.some((placeholder) => normalized.includes(placeholder))) return false

  return countWords(value) >= 18
}

function countWords(value: string) {
  return value
    .replace(/!\[\[[^\]]+\]\]/g, " ")
    .replace(/!\[[^\]]*\]\([^)]+\)/g, " ")
    .replace(/[#>*_`[\]()]/g, " ")
    .split(/\s+/)
    .filter(Boolean).length
}

function compareStudioChapters(left: BookStudioChapter, right: BookStudioChapter) {
  return outlineRank(left.outlineSection) - outlineRank(right.outlineSection) || left.title.localeCompare(right.title)
}

function outlineRank(value: string) {
  if (!value) return 999
  if (/^\d+$/.test(value)) return Number(value)
  if (/^[A-Z]$/i.test(value)) return 100 + value.toUpperCase().charCodeAt(0) - 64

  return 900
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function titleFromPath(value: string) {
  const base = value.split("/").pop()?.replace(/\.[^.]+$/, "") || value

  return base
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
}
