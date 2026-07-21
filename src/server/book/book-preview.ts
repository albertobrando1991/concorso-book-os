import { readdir, stat } from "node:fs/promises"
import path from "node:path"
import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import {
  TEXT_VOLUME_CATALOG,
  bookIdsForTextVolumeBookId,
  findTextVolumeForBookId,
  isTextVolumeBookId,
  normalizeTextBookId,
  textVolumeBookId,
  type TextVolume
} from "../../catalog/text-volumes"

export { ricettarioModuleLabel } from "./book-studio-labels"

export type ChapterContentState = "written" | "draft" | "structure"

export interface MarkdownBlock {
  type:
    | "heading"
    | "paragraph"
    | "list"
    | "image"
    | "code"
    | "table"
    | "callout"
    | "index-entry"
    | "index-part"
    | "index-chapter"
    | "index-row"
  text?: string
  level?: number
  number?: string
  pageNumber?: number
  items?: string[]
  ordered?: boolean
  start?: number
  path?: string
  alt?: string
  headers?: string[]
  rows?: string[][]
  continued?: boolean
  calloutType?: string
  title?: string
}

export type BookStudioScope = "main" | "ricettario"

export interface BookStudioChapter {
  path: string
  title: string
  outlineSection: string
  bookScope: BookStudioScope
  sectionType: "front_matter" | "chapter"
  frontMatterLayout: string
  indexDetail: string
  status: string
  draftStage: string
  reviewRequired: boolean
  isGenerated?: boolean
  volumeModuleCode?: string
  volumeModuleTitle?: string
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
    mainChapters: number
    ricettarioModules: number
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
  "Note di review",
  "Norme o riferimenti",
  "Quiz collegati",
  "Spiegazione",
  "Punti chiave",
  "Esempi",
  "Errori frequenti"
]

const IMAGE_EXTENSIONS = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"])
const BOOK_ASSET_PATH = /^books\/(?:[a-z0-9-]+\/)*[a-z0-9-]+\/assets\//
const MAX_PREVIEW_BLOCKS = 520
const INDEX_PAGE_BUDGET = 1000
const INDEX_FIRST_PAGE_HEADER_COST = 150
const INDEX_RUNNING_HEADER_COST = 34
const DEFAULT_MAX_TABLE_ROWS_PER_PREVIEW_BLOCK = 4
const VERBOSE_TABLE_ROWS_PER_PREVIEW_BLOCK = 2
const MAX_LIST_ITEMS_PER_PREVIEW_BLOCK = 4
const MAX_PARAGRAPH_WORDS_PER_PREVIEW_BLOCK = 72

export async function buildBookStudioData(store: FileWikiStore, bookId = "il-metodo-bando"): Promise<BookStudioData> {
  const normalizedBookId = normalizeTextBookId(bookId)

  if (isTextVolumeBookId(normalizedBookId)) {
    const volume = findTextVolumeForBookId(normalizedBookId)

    if (volume) {
      return buildVolumeBookStudioData(store, volume)
    }
  }

  return buildSingleBookStudioData(store, normalizedBookId)
}

async function buildSingleBookStudioData(store: FileWikiStore, bookId: string): Promise<BookStudioData> {
  const bookPath = `books/${bookId}/index.md`
  const bookContent = await store.exists(bookPath).then((exists) => exists ? store.readText(bookPath) : "")
  const book = parseFrontmatter(bookContent)
  const frontMatterFiles = (await store.listMarkdown(`books/${bookId}/front-matter`))
    .filter((file) => file.endsWith(".md"))
  const chapterFiles = (await store.listMarkdown(`books/${bookId}/chapters`))
    .filter((file) => file.endsWith(".md"))
  const chapters: BookStudioChapter[] = []

  for (const file of [...frontMatterFiles, ...chapterFiles]) {
    const content = await store.readText(file)
    const parsed = parseFrontmatter(content)
    const preview = selectPreviewMarkdown(parsed.body)
    const sectionType = file.includes("/front-matter/") || parsed.data.type === "front_matter"
      ? "front_matter"
      : "chapter"
    const outlineSection = String(parsed.data.outline_section || "")
    const bookScope = resolveBookStudioScope(bookId, sectionType, outlineSection)

    chapters.push({
      path: file,
      title: String(parsed.data.title || titleFromPath(file)),
      outlineSection,
      bookScope,
      sectionType,
      frontMatterLayout: String(parsed.data.front_matter_layout || ""),
      indexDetail: String(parsed.data.index_detail || ""),
      status: String(parsed.data.status || "draft"),
      draftStage: String(parsed.data.draft_stage || ""),
      reviewRequired: Boolean(parsed.data.review_required),
      isGenerated: false,
      topics: asStringArray(parsed.data.topics),
      sourceRefs: asStringArray(parsed.data.source_refs),
      wordCount: countWords(preview.markdown),
      contentState: sectionType === "front_matter" && preview.state !== "structure" ? "written" : preview.state,
      blocks: markdownToBlocks(preview.markdown, file)
    })
  }

  chapters.sort(compareStudioChapters)
  hydrateGeneratedFrontMatter(chapters, bookId)
  const assets = await listBookAssets(store, bookId)

  return {
    bookId,
    title: String(book.data.title || "Il Metodo BANDO"),
    updatedAt: new Date().toISOString(),
    summary: {
      chapters: chapters.length,
      mainChapters: chapters.filter((chapter) => chapter.bookScope === "main").length,
      ricettarioModules: chapters.filter((chapter) => chapter.bookScope === "ricettario").length,
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

async function buildVolumeBookStudioData(store: FileWikiStore, volume: TextVolume): Promise<BookStudioData> {
  const bookId = textVolumeBookId(volume)
  const moduleBooks = await loadVolumeModuleBooks(store, volume)
  const volumeFrontMatter = buildVolumeFrontMatter(volume, moduleBooks, bookId)
  const moduleSections = moduleBooks.flatMap(({ moduleCode, moduleTitle, chapters }) => [
    buildModuleOpeningSection({
      bookId,
      moduleCode,
      moduleTitle,
      volume,
      chapters
    }),
    ...chapters
  ])
  const chapters = [...volumeFrontMatter, ...moduleSections]
  const assets = moduleBooks.flatMap((moduleBook) => moduleBook.assets)
  const uniqueAssets = Array.from(new Map(assets.map((asset) => [asset.path, asset])).values())
    .sort((left, right) => right.updatedAt.localeCompare(left.updatedAt))

  return {
    bookId,
    title: `${volume.code} - ${volume.title}`,
    updatedAt: new Date().toISOString(),
    summary: {
      chapters: chapters.length,
      mainChapters: chapters.filter((chapter) => chapter.bookScope === "main").length,
      ricettarioModules: 0,
      written: chapters.filter((chapter) => chapter.contentState === "written").length,
      draft: chapters.filter((chapter) => chapter.contentState === "draft").length,
      structure: chapters.filter((chapter) => chapter.contentState === "structure").length,
      reviewRequired: chapters.filter((chapter) => chapter.reviewRequired).length,
      assets: uniqueAssets.length
    },
    chapters,
    assets: uniqueAssets
  }
}

interface VolumeModuleBook {
  bookId: string
  moduleCode: string
  moduleTitle: string
  chapters: BookStudioChapter[]
  assets: BookStudioAsset[]
}

async function loadVolumeModuleBooks(store: FileWikiStore, volume: TextVolume): Promise<VolumeModuleBook[]> {
  const moduleBooks: VolumeModuleBook[] = []

  for (const [index, rawBookId] of volume.bookIds.entries()) {
    const moduleBookId = normalizeTextBookId(rawBookId)

    if (!(await store.exists(`books/${moduleBookId}/index.md`))) continue

    const moduleData = await buildSingleBookStudioData(store, moduleBookId)
    const moduleCode = volume.modules[index] || (moduleBookId === "il-metodo-bando" ? "BASE" : moduleCodeFromBookId(moduleBookId))
    const moduleTitle = moduleData.title
    const chapters = moduleData.chapters
      .filter((chapter) => chapter.sectionType === "chapter" && chapter.bookScope === "main")
      .map((chapter) => ({
        ...chapter,
        bookScope: "main" as const,
        volumeModuleCode: moduleCode,
        volumeModuleTitle: moduleTitle
      }))

    moduleBooks.push({
      bookId: moduleBookId,
      moduleCode,
      moduleTitle,
      chapters,
      assets: moduleData.assets
    })
  }

  return moduleBooks
}

function buildVolumeFrontMatter(volume: TextVolume, moduleBooks: VolumeModuleBook[], bookId: string): BookStudioChapter[] {
  const missingBookIds = volume.bookIds.filter((moduleBookId) =>
    !moduleBooks.some((moduleBook) => moduleBook.bookId === normalizeTextBookId(moduleBookId))
  )

  return [
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Servizi digitali inclusi",
      outlineSection: "FM1",
      frontMatterLayout: "digital-services",
      markdown: buildVolumeDigitalServicesMarkdown(volume)
    }),
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Frontespizio",
      outlineSection: "FM2",
      frontMatterLayout: "title-page",
      markdown: buildVolumeTitlePageMarkdown(volume)
    }),
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Copyright e note editoriali",
      outlineSection: "FM3",
      frontMatterLayout: "copyright",
      markdown: buildVolumeCopyrightMarkdown(volume)
    }),
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Sommario",
      outlineSection: "FM4",
      frontMatterLayout: "summary",
      markdown: buildVolumeSummaryMarkdown(volume, moduleBooks, missingBookIds)
    }),
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Premessa",
      outlineSection: "FM5",
      frontMatterLayout: "preface",
      markdown: buildVolumePrefaceMarkdown(volume, moduleBooks)
    }),
    buildGeneratedFrontMatterSection({
      bookId,
      title: "Indice completo",
      outlineSection: "FM6",
      frontMatterLayout: "analytical-index",
      blocks: buildVolumeIndexBlocks(moduleBooks)
    })
  ]
}

function buildGeneratedFrontMatterSection(input: {
  bookId: string
  title: string
  outlineSection: string
  frontMatterLayout: string
  markdown?: string
  blocks?: MarkdownBlock[]
}): BookStudioChapter {
  const sectionPath = `books/${input.bookId}/front-matter/${input.outlineSection.toLowerCase()}-${slugForGeneratedPath(input.title)}.md`
  const blocks = input.blocks || markdownToBlocks(input.markdown || `# ${input.title}`, sectionPath)

  return {
    path: sectionPath,
    title: input.title,
    outlineSection: input.outlineSection,
    bookScope: "main",
    sectionType: "front_matter",
    frontMatterLayout: input.frontMatterLayout,
    indexDetail: input.frontMatterLayout === "analytical-index" ? "volume-modules" : "",
    status: "generated",
    draftStage: "generated-volume-layout",
    reviewRequired: false,
    isGenerated: true,
    topics: [],
    sourceRefs: [],
    wordCount: countBlockWords(blocks),
    contentState: "written",
    blocks
  }
}

function buildModuleOpeningSection(input: {
  bookId: string
  moduleCode: string
  moduleTitle: string
  volume: TextVolume
  chapters: BookStudioChapter[]
}): BookStudioChapter {
  const path = `books/${input.bookId}/modules/${input.moduleCode.toLowerCase()}/frontespizio-sommario.md`
  const markdown = buildModuleOpeningMarkdown(input.moduleCode, input.moduleTitle, input.volume, input.chapters)
  const blocks = markdownToBlocks(markdown, path)

  return {
    path,
    title: `${input.moduleCode} - ${stripModuleCode(input.moduleTitle)}`,
    outlineSection: input.moduleCode,
    bookScope: "main",
    sectionType: "front_matter",
    frontMatterLayout: "module-opening",
    indexDetail: "",
    status: "generated",
    draftStage: "generated-module-opening",
    reviewRequired: false,
    isGenerated: true,
    volumeModuleCode: input.moduleCode,
    volumeModuleTitle: input.moduleTitle,
    topics: [],
    sourceRefs: [],
    wordCount: countBlockWords(blocks),
    contentState: "written",
    blocks
  }
}

function buildVolumeDigitalServicesMarkdown(volume: TextVolume) {
  return [
    "# Servizi digitali inclusi",
    "",
    `Questo volume (${volume.code}) e collegato ai servizi digitali Capitale Personale: aggiornamenti operativi, schede compilabili, planner, Bando Decoder e materiali di lavoro collegati ai moduli interni.`,
    "",
    "## Cosa aggiunge il digitale",
    "",
    "| Servizio | Funzione |",
    "| --- | --- |",
    "| Bando Decoder | Trasforma il bando in piano di studio e priorita. |",
    "| Planner | Organizza tempi, prove, ripassi e simulazioni. |",
    "| Schede modulo | Adatta il Metodo BANDO alla famiglia concorsuale del volume. |",
    "| Aggiornamenti | Segnala fonti ufficiali da verificare prima della pubblicazione o della prova. |",
    "",
    "> [!TIP]",
    "> Il volume resta utilizzabile anche senza piattaforma: il digitale accelera compilazione, verifica e aggiornamento, ma non sostituisce il libro."
  ].join("\n")
}

function buildVolumeTitlePageMarkdown(volume: TextVolume) {
  return [
    `# ${volume.code}`,
    "",
    `## ${volume.title}`,
    "",
    volume.promise,
    "",
    "### Capitale Personale",
    "",
    `Volume operativo Metodo BANDO per ${volume.audience.toLowerCase()}.`
  ].join("\n")
}

function buildVolumeCopyrightMarkdown(volume: TextVolume) {
  return [
    "# Copyright e note editoriali",
    "",
    "Questo volume appartiene alla linea ConcorsoBook OS / Capitale Personale ed e costruito come libro-workbook per la preparazione ai concorsi pubblici italiani.",
    "",
    "Le informazioni normative e procedurali devono essere verificate sulle fonti ufficiali vive prima dell'uso professionale o della pubblicazione definitiva.",
    "",
    "Il volume non promette copertura totale di ogni bando, ne aggiornamento automatico: offre un metodo riusabile, una struttura modulare e strumenti di lavoro collegati al perimetro editoriale dichiarato.",
    "",
    `Perimetro volume: ${volume.title}.`
  ].join("\n")
}

function buildVolumeSummaryMarkdown(volume: TextVolume, moduleBooks: VolumeModuleBook[], missingBookIds: string[]) {
  const rows = moduleBooks.map((moduleBook) =>
    `| ${escapeTableCell(moduleBook.moduleCode)} | ${escapeTableCell(stripModuleCode(moduleBook.moduleTitle))} | ${moduleBook.chapters.length} sezioni |`
  )
  const missing = missingBookIds.length > 0
    ? [
        "",
        "## Moduli da inizializzare",
        "",
        missingBookIds.map((moduleBookId) => `- ${moduleBookId.replace("moduli/", "")}`).join("\n")
      ].join("\n")
    : ""

  return [
    "# Sommario",
    "",
    volume.promise,
    "",
    "| Modulo | Percorso interno | Stato |",
    "| --- | --- | --- |",
    ...(rows.length > 0 ? rows : ["| - | Nessun modulo disponibile nel vault | Da inizializzare |"]),
    "",
    "## Verticali del volume",
    "",
    volume.verticals.map((vertical) => `- ${vertical}`).join("\n"),
    missing
  ].filter(Boolean).join("\n")
}

function buildVolumePrefaceMarkdown(volume: TextVolume, moduleBooks: VolumeModuleBook[]) {
  const moduleList = moduleBooks.map((moduleBook) => moduleBook.moduleCode).join(", ") || "moduli in preparazione"

  return [
    "# Premessa",
    "",
    `Questo volume tratta ${volume.title.toLowerCase()} come un unico libro. I moduli interni (${moduleList}) non sono libri separati per il lettore: sono sezioni coordinate dello stesso percorso editoriale.`,
    "",
    "La struttura segue una regola precisa: prima le pagine comuni del volume, poi il sommario, la premessa e l'indice completo; solo dopo iniziano i moduli interni, ciascuno con una pagina unica di frontespizio e sommario.",
    "",
    "Il lettore deve poter partire dal volume, capire subito il perimetro, vedere l'indice completo e poi attraversare i moduli nell'ordine previsto, senza incontrare di nuovo servizi digitali, copyright o premessa generale a ogni cambio modulo."
  ].join("\n")
}

function buildModuleOpeningMarkdown(moduleCode: string, moduleTitle: string, volume: TextVolume, chapters: BookStudioChapter[]) {
  const chapterRows = chunk(chapters, Math.max(1, Math.ceil(chapters.length / 4))).map((group, index) => {
    const label = index === 0 ? "Avvio" : index === 1 ? "Sviluppo" : index === 2 ? "Allenamento" : "Strumenti"
    const text = group.map((chapter) => `${compactOutlineLabel(chapter.outlineSection)} ${chapter.title}`.trim()).join("; ")

    return `| ${label} | ${escapeTableCell(text)} |`
  })

  return [
    `# ${moduleCode}`,
    "",
    `## ${stripModuleCode(moduleTitle)}`,
    "",
    `Sezione interna del volume ${volume.code} - ${volume.title}.`,
    "",
    "| Blocco | Sommario del modulo |",
    "| --- | --- |",
    ...(chapterRows.length > 0 ? chapterRows : ["| Struttura | Capitoli da inizializzare |"])
  ].join("\n")
}

function buildVolumeIndexBlocks(moduleBooks: VolumeModuleBook[]): MarkdownBlock[] {
  const blocks: MarkdownBlock[] = [
    { type: "heading", level: 2, text: "Indice completo" }
  ]
  let pageCursor = 1

  for (const moduleBook of moduleBooks) {
    blocks.push({
      type: "index-part",
      number: moduleBook.moduleCode,
      text: stripModuleCode(moduleBook.moduleTitle)
    })
    pageCursor += 1

    for (const chapter of moduleBook.chapters) {
      const estimate = estimateChapterPages(chapter, pageCursor)
      blocks.push({
        type: "index-chapter",
        number: compactIndexLabel(chapter.outlineSection),
        text: chapter.title,
        path: chapter.path,
        pageNumber: pageCursor
      })
      pageCursor += estimate.pageCount
    }
  }

  if (moduleBooks.length === 0) {
    blocks.push({
      type: "paragraph",
      text: "Nessun modulo del volume e ancora disponibile nel vault."
    })
  }

  return blocks
}

function moduleCodeFromBookId(bookId: string) {
  const slug = bookId.split("/").pop() || bookId
  const match = /^(m-[a-z]{2}\d{2})/.exec(slug)

  return match ? match[1].toUpperCase() : slug.toUpperCase()
}

function compactOutlineLabel(outlineSection: string) {
  const normalized = outlineSection.trim()

  if (/^[A-Z]$/i.test(normalized)) return `App. ${normalized.toUpperCase()}`
  if (/^\d+$/.test(normalized)) return normalized

  return normalized
}

function compactIndexLabel(outlineSection: string) {
  const normalized = outlineSection.trim()

  if (/^[A-Z]$/i.test(normalized)) return `App. ${normalized.toUpperCase()}`
  if (/^\d+$/.test(normalized)) return `Cap. ${normalized}`

  return normalized || "Modulo"
}

function stripModuleCode(value: string) {
  return value.replace(/^M-[A-Z]{2}\d{2}\s*[-–]\s*/i, "").trim()
}

function slugForGeneratedPath(value: string) {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "") || "sezione"
}

function escapeTableCell(value: string) {
  return value.replace(/\|/g, "/").replace(/\s+/g, " ").trim()
}

function chunk<T>(items: T[], size: number) {
  const chunks: T[][] = []

  for (let index = 0; index < items.length; index += size) {
    chunks.push(items.slice(index, index + size))
  }

  return chunks
}

function hydrateGeneratedFrontMatter(sections: BookStudioChapter[], bookId: string) {
  const writtenChapters = sections.filter((section) =>
    section.sectionType === "chapter" &&
    section.bookScope === "main" &&
    section.contentState !== "structure"
  )

  for (const section of sections) {
    if (section.frontMatterLayout !== "analytical-index") continue

    section.blocks = buildAnalyticalIndexBlocks(writtenChapters, {
      bookId,
      includeHeadings: section.indexDetail !== "chapters-only"
    })
    section.wordCount = countBlockWords(section.blocks)
    section.contentState = "written"
  }
}

function buildAnalyticalIndexBlocks(
  chapters: BookStudioChapter[],
  options: { bookId: string; includeHeadings: boolean }
): MarkdownBlock[] {
  const blocks: MarkdownBlock[] = [
    { type: "heading", level: 2, text: "Indice" }
  ]
  const chapterPages = buildChapterPageMap(chapters)
  let currentPart = ""

  for (const chapterPage of chapterPages) {
    const { chapter, headings, startPage } = chapterPage
    const part = indexPartForOutline(chapter.outlineSection, options.bookId)
    const chapterNumber = chapterNumberFromOutline(chapter.outlineSection)

    if (part && part.key !== currentPart) {
      currentPart = part.key
      blocks.push({
        type: "index-part",
        number: part.label,
        text: part.title
      })
    }

    blocks.push({
      type: "index-chapter",
      number: chapterIndexLabel(chapter.outlineSection, chapterNumber),
      text: chapter.title,
      path: chapter.path,
      pageNumber: startPage
    })

    if (!options.includeHeadings) continue

    headings.forEach((heading, index) => {
      blocks.push({
        type: "index-row",
        number: chapterNumber ? `${chapterNumber}.${index + 1}` : `${index + 1}`,
        text: stripLeadingHeadingNumber(heading.text),
        pageNumber: heading.pageNumber
      })
    })
  }

  return blocks
}

function buildChapterPageMap(chapters: BookStudioChapter[]) {
  let pageCursor = 1

  return chapters.map((chapter) => {
    const estimate = estimateChapterPages(chapter, pageCursor)
    const current = {
      chapter,
      startPage: pageCursor,
      pageCount: estimate.pageCount,
      headings: estimate.headings
    }
    pageCursor += estimate.pageCount

    return current
  })
}

function estimateChapterPages(chapter: BookStudioChapter, startPage: number) {
  const headings: Array<{ text: string; pageNumber: number }> = []
  let pageOffset = 0
  let used = INDEX_FIRST_PAGE_HEADER_COST

  for (const block of chapter.blocks) {
    const cost = estimatePreviewBlockCost(block)

    if (used > INDEX_RUNNING_HEADER_COST && used + cost > INDEX_PAGE_BUDGET) {
      pageOffset += 1
      used = INDEX_RUNNING_HEADER_COST
    }

    if (block.type === "heading" && (block.level || 0) === 2) {
      const text = cleanIndexText(block.text || "")

      if (isIndexHeading(text, chapter.title)) {
        headings.push({
          text,
          pageNumber: startPage + pageOffset
        })
      }
    }

    used += cost
  }

  return {
    headings,
    pageCount: Math.max(1, pageOffset + 1)
  }
}

function estimatePreviewBlockCost(block: MarkdownBlock) {
  if (block.type === "heading") {
    const level = block.level || 3

    if (level <= 2) return 42
    if (level === 3) return 32

    return 26
  }

  if (block.type === "paragraph") return Math.ceil(countWords(block.text || "") / 17) * 18 + 5
  if (block.type === "list") {
    return (block.items || []).reduce((total, item) => total + Math.ceil(countWords(item) / 16) * 17 + 4, 12)
  }
  if (block.type === "table") return estimateTableBlockCost(block)
  if (block.type === "image") return 315
  if (block.type === "callout") return Math.ceil(countWords(`${block.title || ""} ${block.text || ""}`) / 16) * 18 + 28
  if (block.type === "code") return (block.text || "").split("\n").length * 18 + 24

  return 36
}

function chapterNumberFromOutline(value: string) {
  const normalized = value.trim()

  if (/^[A-Z]$/i.test(normalized)) return normalized.toUpperCase()

  const number = Number.parseInt(value, 10)

  if (!Number.isFinite(number) || number <= 0) return ""

  return String(number)
}

function chapterIndexLabel(outlineSection: string, chapterNumber: string) {
  if (/^[A-Z]$/i.test(outlineSection.trim())) return `Appendice ${chapterNumber}`

  return chapterNumber ? `Capitolo ${chapterNumber}` : "Introduzione"
}

function indexPartForOutline(value: string, bookId: string) {
  const normalized = value.trim()

  if (/^[A-Z]$/i.test(normalized)) {
    return {
      key: "appendici",
      label: "Appendici",
      title: "Strumenti operativi"
    }
  }

  const number = Number.parseInt(value, 10)

  if (!Number.isFinite(number) || number <= 0) return null

  if (bookId.startsWith("moduli/")) {
    if (number <= 3) {
      return {
        key: "modulo-parte-1",
        label: "Parte I",
        title: "Orientarsi nel modulo"
      }
    }
    if (number <= 7) {
      return {
        key: "modulo-parte-2",
        label: "Parte II",
        title: "Amministrazione e profili"
      }
    }
    if (number <= 10) {
      return {
        key: "modulo-parte-3",
        label: "Parte III",
        title: "Materie ad alta probabilita"
      }
    }

    return {
      key: "modulo-parte-4",
      label: "Parte IV",
      title: "Allenamento e strumenti"
    }
  }

  if (number <= 3) {
    return {
      key: "parte-1",
      label: "Parte I",
      title: "Capire il concorso prima di studiare"
    }
  }
  if (number <= 12) {
    return {
      key: "parte-2",
      label: "Parte II",
      title: "Il nucleo comune dei concorsi pubblici"
    }
  }
  if (number <= 18) {
    return {
      key: "parte-3",
      label: "Parte III",
      title: "Allenarsi come in prova"
    }
  }
  if (number <= 22) {
    return {
      key: "parte-4",
      label: "Parte IV",
      title: "Adattare il metodo ai profili concorsuali"
    }
  }
  if (number <= 24) {
    return {
      key: "parte-5",
      label: "Parte V",
      title: "Kit finale del candidato"
    }
  }

  return {
    key: "ricettario-digitale",
    label: "Ricettario digitale",
    title: "Applicazione avanzata"
  }
}

function stripLeadingHeadingNumber(value: string) {
  return value.replace(/^\d+\.\s+/, "").trim()
}

function cleanIndexText(value: string) {
  return value.replace(/\*\*/g, "").replace(/\s+/g, " ").trim()
}

function normalizeIndexText(value: string) {
  return cleanIndexText(value)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
}

function isIndexHeading(value: string, chapterTitle: string) {
  const normalized = normalizeIndexText(value)
  const normalizedTitle = normalizeIndexText(chapterTitle)

  if (!normalized || normalized === normalizedTitle) return false

  return !INDEX_HEADING_EXCLUSIONS.some((pattern) => pattern.test(normalized))
}

const INDEX_HEADING_EXCLUSIONS = [
  /^obiettivi del capitolo$/,
  /^come usare il metodo bando$/,
  /^mappa bando$/,
  /^da sapere in 5 righe$/,
  /^caso guidato/,
  /^domanda da commissario/,
  /^domanda-trappola/,
  /^errore tipico/,
  /^errori tipici/,
  /^mini-esercizio/,
  /^checkpoint finale/,
  /^glossario minimo/,
  /^schema operativo di risposta/,
  /^confini /,
  /^priorita di studio/,
  /^mini-test/,
  /^10 domande ragionate/,
  /^domande frequenti/,
  /^mini-palestra/,
  /^preparare .* con poco tempo/,
  /^collegamenti con gli altri capitoli/,
  /^checklist/,
  /^\d+\.\s*(qualifica|collega|individua|risposta modello|chiusura operativa)/,
  /^risposta modello/,
  /^chiusura operativa/
]

function countBlockWords(blocks: MarkdownBlock[]) {
  return blocks.reduce((total, block) => {
    const values = [
      block.text || "",
      block.title || "",
      ...(block.items || []),
      ...(block.headers || []),
      ...(block.rows || []).flat()
    ]

    return total + countWords(values.join(" "))
  }, 0)
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

  return splitOversizedBlocks(blocks).slice(0, MAX_PREVIEW_BLOCKS)
}

function splitOversizedBlocks(blocks: MarkdownBlock[]) {
  const next: MarkdownBlock[] = []

  for (const block of blocks) {
    if (block.type === "paragraph" && countWords(block.text || "") > MAX_PARAGRAPH_WORDS_PER_PREVIEW_BLOCK) {
      splitTextIntoPreviewChunks(block.text || "", MAX_PARAGRAPH_WORDS_PER_PREVIEW_BLOCK).forEach((text, index) => {
        next.push({
          ...block,
          continued: index > 0,
          text
        })
      })
      continue
    }

    if (block.type === "table" && (block.rows?.length || 0) > DEFAULT_MAX_TABLE_ROWS_PER_PREVIEW_BLOCK) {
      const rows = block.rows || []
      const rowsPerBlock = tableRowsPerPreviewBlock(block)

      for (let index = 0; index < rows.length; index += rowsPerBlock) {
        next.push({
          ...block,
          continued: index > 0,
          rows: rows.slice(index, index + rowsPerBlock)
        })
      }
      continue
    }

    if (block.type === "list" && (block.items?.length || 0) > MAX_LIST_ITEMS_PER_PREVIEW_BLOCK) {
      const items = block.items || []
      const start = block.start || 1

      for (let index = 0; index < items.length; index += MAX_LIST_ITEMS_PER_PREVIEW_BLOCK) {
        next.push({
          ...block,
          continued: index > 0,
          items: items.slice(index, index + MAX_LIST_ITEMS_PER_PREVIEW_BLOCK),
          start: block.ordered ? start + index : undefined
        })
      }
      continue
    }

    next.push(block)
  }

  return next
}

function tableRowsPerPreviewBlock(block: MarkdownBlock) {
  const cells = (block.rows || []).flat().filter(Boolean)
  const averageCellLength = cells.reduce((total, cell) => total + cell.length, 0) / Math.max(1, cells.length)
  const maxCellLength = cells.reduce((max, cell) => Math.max(max, cell.length), 0)

  if (averageCellLength >= 24 || maxCellLength >= 80) return VERBOSE_TABLE_ROWS_PER_PREVIEW_BLOCK

  return DEFAULT_MAX_TABLE_ROWS_PER_PREVIEW_BLOCK
}

function splitTextIntoPreviewChunks(text: string, targetWords: number) {
  const words = text.split(/\s+/).filter(Boolean)

  if (words.length <= targetWords) return [text]

  const chunks: string[] = []
  let current: string[] = []
  const hardLimit = Math.ceil(targetWords * 1.24)

  for (const word of words) {
    current.push(word)

    const normalized = word.replace(/[)"'\]]+$/, "")
    const endsSentence = /[.!?;:]$/.test(normalized)

    if ((current.length >= targetWords && endsSentence) || current.length >= hardLimit) {
      chunks.push(current.join(" "))
      current = []
    }
  }

  if (current.length > 0) chunks.push(current.join(" "))

  return chunks
}

function estimateTableBlockCost(block: MarkdownBlock) {
  const headerCost = block.continued ? 0 : 24
  const rowCost = 22

  return headerCost + (block.rows?.length || 0) * rowCost + 8
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

export function resolveBookStudioScope(
  bookId: string,
  sectionType: BookStudioChapter["sectionType"],
  outlineSection: string
): BookStudioScope {
  if (bookId !== "il-metodo-bando" || sectionType !== "chapter") return "main"

  const number = Number.parseInt(outlineSection, 10)

  return Number.isFinite(number) && number >= 25 ? "ricettario" : "main"
}

function outlineRank(value: string) {
  const normalized = value.trim()
  const frontMatter = /^FM(\d+)$/i.exec(normalized)

  if (frontMatter) return -100 + Number.parseInt(frontMatter[1], 10)
  if (!normalized) return 999
  if (/^\d+$/.test(normalized)) return Number(normalized)
  if (/^[A-Z]$/i.test(normalized)) return 100 + normalized.toUpperCase().charCodeAt(0) - 64

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
