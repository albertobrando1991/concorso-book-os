import { IngestAgent } from "../agents/ingest-agent"
import { ManualWriterAgent, type ManualWriterMode } from "../agents/manual-writer-agent"
import { classifySource } from "../agents/classifier"
import { DEFAULT_BOOK_ID, getWriterConfig } from "../config"
import { extractPdfMarkdownWithGlmOcr } from "../ocr/glm-ocr"
import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import { slugify } from "../wiki/slug"
import type { AgentRunResult, SourceInput } from "../wiki/types"
import { findPdfLinks, searchOfficialSource, type SourceSearchResult } from "./source-search"

export interface HermesSourceImportInput {
  url?: string
  query?: string
  title?: string
  content?: string
  sourceType?: SourceInput["sourceType"]
  sourceDate?: string
  chapterPath?: string
  runWriter?: boolean
  writerMode?: ManualWriterMode
  instruction?: string
  preferPdf?: boolean
}

export interface HermesSourceImportResult {
  status: "completed"
  sourceUrl: string
  sourceTitle: string
  sourcePath: string
  rawMarkdownPath: string
  rawAttachmentPath?: string
  search?: SourceSearchResult
  ingest: AgentRunResult
  linkedChapterPath?: string
  writerResult?: Awaited<ReturnType<ManualWriterAgent["writeChapter"]>>
  warnings: string[]
}

const RAW_FOLDERS: Record<SourceInput["sourceType"], string> = {
  article: "articles",
  law: "laws",
  decree: "decrees",
  manual: "manuals",
  website: "websites",
  transcript: "transcripts"
}

export async function importSourceForHermes(input: HermesSourceImportInput, store: FileWikiStore): Promise<HermesSourceImportResult> {
  const sourceType = input.sourceType || "law"
  const resolved = await resolveSourceRequest(input, sourceType)
  let downloaded = await downloadUrl(resolved.url)
  let sourceUrl = resolved.url
  const warnings: string[] = [...resolved.warnings]

  if (input.preferPdf !== false && !downloaded.isPdf && downloaded.contentType.includes("html")) {
    const pdfLink = findPdfLinks(downloaded.text, sourceUrl, input.query || input.title).at(0)

    if (pdfLink) {
      downloaded = await downloadUrl(pdfLink.url)
      sourceUrl = pdfLink.url
      warnings.push(`Pagina risultato convertita in PDF collegato: ${pdfLink.url}`)
    }
  }

  const title = cleanTitle(input.title || resolved.title || titleFromUrl(sourceUrl))
  const rawAttachmentPath = await maybeSaveAttachment({
    store,
    title,
    sourceType,
    contentType: downloaded.contentType,
    body: downloaded.body,
    url: sourceUrl
  })
  let ocrMarkdown = ""

  if (rawAttachmentPath && !input.content) {
    const ocrResult = await extractPdfMarkdownWithGlmOcr(store.resolve(rawAttachmentPath))
    ocrMarkdown = ocrResult.markdown
    warnings.push(...ocrResult.warnings)
  }

  const sourceContent = buildSourceContent({
    title,
    url: sourceUrl,
    searchQuery: resolved.search?.query,
    providedContent: input.content,
    downloadedText: ocrMarkdown || downloaded.text,
    contentType: downloaded.contentType,
    rawAttachmentPath
  })
  const sourceInput: SourceInput = {
    title,
    content: sourceContent,
    sourceType,
    sourceUrl,
    sourceDate: input.sourceDate,
    authorityLevel: sourceType === "law" || sourceType === "decree" ? "alta" : undefined
  }
  const source = classifySource(sourceInput)
  const sourcePath = `sources/${source.slug}.md`
  const rawMarkdownPath = `raw/${RAW_FOLDERS[sourceType]}/${source.slug}.md`
  const ingest = await new IngestAgent(store).ingest(sourceInput)
  let linkedChapterPath: string | undefined
  let writerResult: HermesSourceImportResult["writerResult"]

  if (rawAttachmentPath) {
    ingest.changedFiles.push(rawAttachmentPath)
    await store.appendHeading(
      sourcePath,
      "Fonti",
      `- Allegato originale scaricato: \`wiki/${rawAttachmentPath}\`.`
    )
  }

  if (!input.content && downloaded.isPdf && !ocrMarkdown) {
    warnings.push("PDF scaricato, ma testo non estratto dal sito. Fai estrarre il testo a Hermes e richiama l'endpoint con content, oppure abilita/configura GLM-OCR.")
  }

  if (input.chapterPath) {
    linkedChapterPath = await linkSourceToChapter({
      store,
      chapterPath: input.chapterPath,
      sourcePath,
      sourceTitle: title
    })
    ingest.changedFiles.push(linkedChapterPath)
  }

  if (input.runWriter && linkedChapterPath) {
    const writerProvider = getWriterConfig().provider

    if (writerProvider === "hermes") {
      warnings.push(
        "runWriter ignorato per evitare una chiamata ricorsiva a Hermes mentre Hermes sta orchestrando l'import. Usa WRITER_PROVIDER=codex/openai/local per il writer automatico da Telegram, oppure lancia il writer dalla dashboard dopo l'import."
      )
    } else {
      writerResult = await new ManualWriterAgent(store).writeChapter({
        chapterPath: linkedChapterPath,
        mode: input.writerMode || "integrate",
        instruction:
          input.instruction ||
          `Integra la nuova fonte consolidata [[${sourcePath.replace(".md", "")}]] nel capitolo. Mantieni tracciabilita, segnala in Note di review eventuali punti da verificare e non usare direttamente raw sources.`
      })
    }
  }

  await store.appendText(
    "log.md",
    `\n- ${new Date().toISOString()} | hermes_import | ${title} | url=${input.url} | source=${sourcePath} | chapter=${linkedChapterPath || "none"} | writer=${writerResult ? "yes" : "no"}`
  )

  return {
    status: "completed",
    sourceUrl,
    sourceTitle: title,
    sourcePath,
    rawMarkdownPath,
    rawAttachmentPath,
    search: resolved.search,
    ingest: {
      ...ingest,
      changedFiles: Array.from(new Set(ingest.changedFiles))
    },
    linkedChapterPath,
    writerResult,
    warnings
  }
}

async function resolveSourceRequest(input: HermesSourceImportInput, sourceType: SourceInput["sourceType"]) {
  if (input.url) {
    validateHttpUrl(input.url)
    return {
      url: input.url,
      title: input.title,
      warnings: [] as string[],
      search: undefined as SourceSearchResult | undefined
    }
  }

  if (!input.query) {
    throw new Error("url or query is required")
  }

  const search = await searchOfficialSource({
    query: input.query,
    sourceType
  })

  return {
    url: search.selected.url,
    title: input.title || search.selected.title,
    warnings: [`Documento selezionato da ricerca: ${search.selected.title} (${search.selected.url})`],
    search
  }
}

async function downloadUrl(url: string) {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), 60000)

  try {
    const response = await fetch(url, {
      signal: controller.signal,
      headers: {
        Accept: "application/pdf,text/html,text/plain,application/xhtml+xml,*/*"
      }
    })

    if (!response.ok) {
      throw new Error(`Download failed ${response.status}: ${await response.text()}`)
    }

    const contentType = response.headers.get("content-type")?.toLowerCase() || ""
    const body = await response.arrayBuffer()
    const text = isTextContent(contentType) ? decodeText(body) : ""
    const isPdf = isPdfDownload(contentType, url, body)

    return { contentType, body, text, isPdf }
  } finally {
    clearTimeout(timer)
  }
}

async function maybeSaveAttachment(input: {
  store: FileWikiStore
  title: string
  sourceType: SourceInput["sourceType"]
  contentType: string
  body: ArrayBuffer
  url: string
}) {
  if (!isPdfDownload(input.contentType, input.url, input.body)) return undefined

  const rawPath = `raw/${RAW_FOLDERS[input.sourceType]}/${slugify(input.title)}.pdf`
  await input.store.writeBinary(rawPath, input.body)

  return rawPath
}

function buildSourceContent(input: {
  title: string
  url: string
  searchQuery?: string
  providedContent?: string
  downloadedText: string
  contentType: string
  rawAttachmentPath?: string
}) {
  const body = input.providedContent?.trim() || textFromDownloaded(input.downloadedText, input.contentType)
  const attachment = input.rawAttachmentPath ? `\n\nAllegato originale scaricato: wiki/${input.rawAttachmentPath}` : ""
  const searchQuery = input.searchQuery ? `\n\nRichiesta originale: ${input.searchQuery}` : ""

  if (body) {
    return [`# ${input.title}`, "", `URL: ${input.url}`, searchQuery.trim(), attachment.trim(), "", body]
      .filter(Boolean)
      .join("\n")
  }

  return [
    `# ${input.title}`,
    "",
    `URL: ${input.url}`,
    searchQuery.trim(),
    attachment.trim(),
    "",
    "Fonte importata automaticamente da Hermes. Il file originale e' stato scaricato, ma il testo non e' ancora stato estratto in modo affidabile.",
    "",
    "## Note di review",
    "- Estrarre il testo del PDF o sostituire questa nota con il testo ufficiale consolidato prima di usare la fonte per affermazioni normative di dettaglio."
  ]
    .filter(Boolean)
    .join("\n")
}

function isPdfDownload(contentType: string, url: string, body: ArrayBuffer) {
  if (contentType.includes("pdf")) return true
  if (new URL(url).pathname.toLowerCase().endsWith(".pdf")) return true

  const header = new TextDecoder("ascii", { fatal: false }).decode(body.slice(0, 5))
  return header === "%PDF-"
}

async function linkSourceToChapter(input: {
  store: FileWikiStore
  chapterPath: string
  sourcePath: string
  sourceTitle: string
}) {
  if (!input.chapterPath.startsWith(`books/${DEFAULT_BOOK_ID}/chapters/`) || !input.chapterPath.endsWith(".md")) {
    throw new Error("chapterPath must target a markdown chapter under the active book")
  }

  if (!(await input.store.exists(input.chapterPath))) {
    throw new Error(`Chapter not found: ${input.chapterPath}`)
  }

  const current = await input.store.readText(input.chapterPath)
  const parsed = parseFrontmatter(current)
  const sourceRefs = Array.isArray(parsed.data.source_refs) ? parsed.data.source_refs.map(String) : []
  const nextSourceRefs = Array.from(new Set([...sourceRefs, input.sourcePath]))

  await input.store.updateFrontmatter(input.chapterPath, {
    source_refs: nextSourceRefs,
    status: "to_expand",
    review_required: true,
    updated_at: new Date().toISOString()
  })
  await input.store.appendHeading(
    input.chapterPath,
    "Note editoriali",
    `- Fonte importata via Hermes/Telegram da integrare: [[${input.sourcePath.replace(".md", "")}]] (${input.sourceTitle}).`
  )

  return input.chapterPath
}

function validateHttpUrl(value: string) {
  let parsed: URL

  try {
    parsed = new URL(value)
  } catch {
    throw new Error("url must be a valid URL")
  }

  if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
    throw new Error("url must use http or https")
  }
}

function isTextContent(contentType: string) {
  return contentType.includes("text/") || contentType.includes("json") || contentType.includes("xml")
}

function decodeText(body: ArrayBuffer) {
  return new TextDecoder("utf-8", { fatal: false }).decode(body)
}

function textFromDownloaded(value: string, contentType: string) {
  if (!value) return ""

  if (contentType.includes("html")) {
    return value
      .replace(/<script[\s\S]*?<\/script>/gi, " ")
      .replace(/<style[\s\S]*?<\/style>/gi, " ")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim()
  }

  return value.replace(/\s+/g, " ").trim()
}

function titleFromUrl(value: string) {
  const url = new URL(value)
  const lastSegment = decodeURIComponent(url.pathname.split("/").filter(Boolean).at(-1) || "fonte-normativa")

  return lastSegment.replace(/\.[a-z0-9]+$/i, "").replace(/[-_]+/g, " ")
}

function cleanTitle(value: string) {
  return value.replace(/\s+/g, " ").trim() || "Fonte normativa"
}
