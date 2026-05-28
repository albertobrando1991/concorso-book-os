import { readdir, stat } from "node:fs/promises"
import path from "node:path"
import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"

export type ChapterContentState = "written" | "draft" | "structure"

export interface MarkdownBlock {
  type: "heading" | "paragraph" | "list" | "image" | "code" | "table" | "callout"
  text?: string
  level?: number
  items?: string[]
  ordered?: boolean
  start?: number
  path?: string
  alt?: string
  headers?: string[]
  rows?: string[][]
  calloutType?: string
  title?: string
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

const STAFF_ONLY_HEADINGS = [
  "Obiettivo didattico",
  "Specifica struttura madre",
  "Strumenti da inserire",
  "Schede principali",
  "Testo editoriale",
  "Bozza agente",
  "Note editoriali",
  "Norme o riferimenti",
  "Quiz collegati",
  "Spiegazione",
  "Punti chiave",
  "Esempi",
  "Errori frequenti"
]

const IMAGE_EXTENSIONS = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"])
const BOOK_ASSET_PATH = /^books\/[a-z0-9-]+\/assets\//

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
      blocks: markdownToBlocks(preview.markdown, file)
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

  if (!isAllowedAssetPath(normalized)) {
    throw new Error("Asset path non valido")
  }

  if (normalized.includes("..")) {
    throw new Error("Asset path non valido")
  }

  return normalized
}

function isAllowedAssetPath(value: string) {
  return value.startsWith("raw/assets/") || BOOK_ASSET_PATH.test(value)
}

export function getAssetContentType(filePath: string) {
  const extension = path.extname(filePath).toLowerCase()

  if (extension === ".png") return "image/png"
  if (extension === ".jpg" || extension === ".jpeg") return "image/jpeg"
  if (extension === ".webp") return "image/webp"
  if (extension === ".gif") return "image/gif"
  if (extension === ".svg") return "image/svg+xml"

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

  const bodyWithoutEmptyEditorial = removeHeadingSections(body, ["Testo editoriale", "Bozza agente"])
  const publicBody = removeHeadingSections(bodyWithoutEmptyEditorial, STAFF_ONLY_HEADINGS)

  if (isSubstantial(publicBody)) {
    return { state: "draft", markdown: publicBody }
  }

  return {
    state: "structure",
    markdown: "## Capitolo in preparazione\nQuesto capitolo è previsto nella struttura del manuale e sarà sviluppato nella versione completa."
  }
}

function removeHeadingSections(value: string, headings: string[]) {
  let next = value

  for (const heading of headings) {
    next = replaceHeadingSectionWithPlaceholder(next, heading)
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

function markdownToBlocks(markdown: string, sourcePath: string): MarkdownBlock[] {
  const blocks: MarkdownBlock[] = []
  const lines = markdown.replace(/\r\n/g, "\n").split("\n")
  let paragraph: string[] = []
  let listItems: string[] = []
  let listOrdered = false
  let listStart: number | undefined
  let codeLines: string[] = []
  let tableLines: string[] = []
  let calloutLines: string[] = []
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
      blocks.push({
        type: "list",
        items: listItems.map(cleanInlineText),
        ordered: listOrdered,
        start: listOrdered ? listStart || 1 : undefined
      })
    }

    listItems = []
    listOrdered = false
    listStart = undefined
  }

  function flushTable() {
    if (tableLines.length > 0) {
      const table = parseTable(tableLines)

      if (table) {
        blocks.push(table)
      } else {
        blocks.push({ type: "paragraph", text: tableLines.map(cleanInlineText).join(" ") })
      }
    }

    tableLines = []
  }

  function flushCallout() {
    if (calloutLines.length > 0) {
      blocks.push(parseCallout(calloutLines))
    }

    calloutLines = []
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
        flushTable()
        flushCallout()
        inCode = true
      }
      continue
    }

    if (inCode) {
      codeLines.push(rawLine)
      continue
    }

    const callout = /^>\s?(.*)$/.exec(line.trim())

    if (callout) {
      flushParagraph()
      flushList()
      flushTable()
      calloutLines.push(callout[1].trim())
      continue
    }

    flushCallout()

    const image = parseImage(line.trim(), sourcePath)

    if (image) {
      flushParagraph()
      flushList()
      flushTable()
      blocks.push(image)
      continue
    }

    const heading = /^(#{1,6})\s+(.+?)\s*$/.exec(line)

    if (heading) {
      flushParagraph()
      flushList()
      flushTable()
      blocks.push({
        type: "heading",
        level: Math.min(heading[1].length, 4),
        text: cleanInlineText(heading[2])
      })
      continue
    }

    if (isTableLine(line)) {
      flushParagraph()
      flushList()
      tableLines.push(line.trim())
      continue
    }

    const unordered = /^\s*[-*]\s+(.+)$/.exec(line)
    const ordered = /^\s*(\d+)[.)]\s+(.+)$/.exec(line)

    if (unordered || ordered) {
      flushParagraph()
      flushTable()

      if (listItems.length > 0 && listOrdered !== Boolean(ordered)) {
        flushList()
      }

      listOrdered = Boolean(ordered)
      if (listItems.length === 0 && ordered) {
        listStart = Number.parseInt(ordered[1], 10)
      }
      listItems.push((ordered?.[2] || unordered?.[1] || "").trim())
      continue
    }

    if (!line.trim()) {
      flushParagraph()
      flushList()
      flushTable()
      flushCallout()
      continue
    }

    flushTable()
    paragraph.push(line.trim())
  }

  flushParagraph()
  flushList()
  flushTable()
  flushCallout()
  flushCode()

  return splitOversizedBlocks(blocks).slice(0, 260)
}

function splitOversizedBlocks(blocks: MarkdownBlock[]) {
  const next: MarkdownBlock[] = []
  const maxTableRows = 5
  const maxListItems = 3

  for (const block of blocks) {
    if (block.type === "table" && (block.rows?.length || 0) > maxTableRows) {
      const rows = block.rows || []

      for (let index = 0; index < rows.length; index += maxTableRows) {
        next.push({
          ...block,
          rows: rows.slice(index, index + maxTableRows)
        })
      }
      continue
    }

    if (block.type === "list" && (block.items?.length || 0) > maxListItems) {
      const items = block.items || []
      const start = block.start || 1

      for (let index = 0; index < items.length; index += maxListItems) {
        next.push({
          ...block,
          items: items.slice(index, index + maxListItems),
          start: block.ordered ? start + index : undefined
        })
      }
      continue
    }

    next.push(block)
  }

  return next
}

function parseCallout(lines: string[]): MarkdownBlock {
  const cleaned = lines.map((line) => cleanInlineText(line)).filter(Boolean)
  const marker = /^\[!(\w+)\]/.exec(cleaned[0] || "")
  const calloutType = marker ? marker[1].toLowerCase() : /^figura\s+\d+/i.test(cleaned[0] || "") ? "caption" : "quote"
  const content = marker ? cleaned.slice(1) : cleaned
  const titleLine = content[0] || ""
  const title = titleLine.length <= 64 && content.length > 1 ? titleLine : defaultCalloutTitle(calloutType)
  const body = titleLine.length <= 64 && content.length > 1 ? content.slice(1) : content

  return {
    type: "callout",
    calloutType,
    title,
    text: body.join(" ")
  }
}

function defaultCalloutTitle(calloutType: string) {
  if (calloutType === "warning") return "Attenzione"
  if (calloutType === "tip") return "BANDO in pratica"
  if (calloutType === "important") return "Da ricordare"
  if (calloutType === "caption") return ""

  return "Nota"
}

function isTableLine(line: string) {
  const trimmed = line.trim()

  return trimmed.includes("|") && trimmed.split("|").length >= 3
}

function parseTable(lines: string[]): MarkdownBlock | null {
  if (lines.length < 2) return null

  const parsedRows = lines.map((line) =>
    line
      .replace(/^\|/, "")
      .replace(/\|$/, "")
      .split("|")
      .map((cell) => cleanInlineText(cell.trim()))
  )
  const separatorIndex = parsedRows.findIndex((row) => row.every((cell) => /^:?-{3,}:?$/.test(cell)))

  if (separatorIndex !== 1) return null

  const headers = parsedRows[0]
  const rows = parsedRows.slice(2).filter((row) => row.some(Boolean))

  if (headers.length === 0 || rows.length === 0) return null

  return {
    type: "table",
    headers,
    rows
  }
}

function parseImage(line: string, sourcePath: string): MarkdownBlock | null {
  const obsidian = /^!\[\[([^\]|]+)(?:\|([^\]]+))?\]\]$/.exec(line)

  if (obsidian) {
    const imagePath = resolveMarkdownAssetPath(obsidian[1].trim(), sourcePath)

    return {
      type: "image",
      path: imagePath,
      alt: obsidian[2]?.trim() || titleFromPath(imagePath)
    }
  }

  const markdown = /^!\[([^\]]*)\]\(([^)]+)\)$/.exec(line)

  if (markdown) {
    const imagePath = resolveMarkdownAssetPath(markdown[2].trim(), sourcePath)

    return {
      type: "image",
      path: imagePath,
      alt: markdown[1].trim() || titleFromPath(imagePath)
    }
  }

  return null
}

function resolveMarkdownAssetPath(value: string, sourcePath: string) {
  const normalized = value.replace(/\\/g, "/").trim()

  if (
    normalized.startsWith("http://") ||
    normalized.startsWith("https://") ||
    normalized.startsWith("/api/")
  ) {
    return normalized
  }

  const withoutLeadingSlash = normalized.replace(/^\/+/, "")

  if (isAllowedAssetPath(withoutLeadingSlash)) {
    return withoutLeadingSlash
  }

  const sourceDirectory = path.posix.dirname(sourcePath.replace(/\\/g, "/"))

  return path.posix.normalize(path.posix.join(sourceDirectory, normalized))
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
  const root = store.resolve("")
  const assetsByPath = new Map<string, BookStudioAsset>()
  const assetDirectories = [
    `raw/assets/books/${bookId}`,
    `books/${bookId}/assets`
  ]

  for (const directory of assetDirectories) {
    const assetRoot = store.resolve(directory)

    if (!assetRoot.startsWith(root)) continue

    for (const asset of await walkAssets(assetRoot, root)) {
      assetsByPath.set(asset.path, asset)
    }
  }

  return Array.from(assetsByPath.values()).sort((left, right) => right.updatedAt.localeCompare(left.updatedAt))
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
