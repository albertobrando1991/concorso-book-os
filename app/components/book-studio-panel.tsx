"use client"

import { useLayoutEffect, useMemo, useRef, useState } from "react"
import {
  BookOpenCheck,
  FileText,
  ImagePlus,
  Loader2,
  RefreshCw,
  Sparkles,
  Upload
} from "lucide-react"
import type { ManualWriterMode } from "@/src/server/agents/manual-writer-agent"
import type { BookStudioChapter, BookStudioData, MarkdownBlock } from "@/src/server/book/book-preview"
import type { WriterProvider } from "@/src/server/config"

interface BookStudioPanelProps {
  initialData: BookStudioData
  writerProvider: WriterProvider
  writerModel: string
  writerReasoningEffort: string
}

interface WriterResult {
  chapterPath: string
  changedFiles: string[]
  draft: string
  warnings: string[]
}

type ViewMode = "chapter" | "book"

interface PreviewPage {
  chapter: BookStudioChapter
  blocks: MarkdownBlock[]
  pageNumber: number
  chapterPageNumber: number
  isFirstPage: boolean
}

const FIRST_PAGE_HEADER_COST = 150
const RUNNING_HEADER_COST = 34
const PAGE_MEASURE_GUARD_SPACE = 48

const modeOptions: Array<{ value: ManualWriterMode; label: string }> = [
  { value: "integrate", label: "Integra richiesta" },
  { value: "format", label: "Sistema impaginazione" },
  { value: "improve", label: "Migliora stile" },
  { value: "expand", label: "Espandi sezione" },
  { value: "draft", label: "Crea bozza" }
]

const providerOptions: Array<{ value: WriterProvider; label: string }> = [
  { value: "codex", label: "Codex / GPT" },
  { value: "claude", label: "Claude" },
  { value: "kimi", label: "Kimi" },
  { value: "openai", label: "OpenAI API" },
  { value: "hermes", label: "Hermes" },
  { value: "local", label: "Locale" }
]

export function BookStudioPanel({
  initialData,
  writerProvider,
  writerModel,
  writerReasoningEffort
}: BookStudioPanelProps) {
  const [data, setData] = useState(initialData)
  const [selectedPath, setSelectedPath] = useState(initialData.chapters[0]?.path || "")
  const [viewMode, setViewMode] = useState<ViewMode>("chapter")
  const [writerMode, setWriterMode] = useState<ManualWriterMode>("integrate")
  const [selectedProvider, setSelectedProvider] = useState<WriterProvider>(writerProvider)
  const [instruction, setInstruction] = useState(
    "Scrivi il capitolo effettivo per il lettore usando prima il cervello wiki: struttura madre, nota capitolo, source notes, topic pages, entity pages e design system. Integra ricerca web ufficiale solo se serve aggiornamento o verifica, poi segnala le fonti da consolidare. Non fare riepiloghi tecnici."
  )
  const [imageFile, setImageFile] = useState<File | null>(null)
  const [caption, setCaption] = useState("")
  const [isRefreshing, setIsRefreshing] = useState(false)
  const [isWriting, setIsWriting] = useState(false)
  const [isUploading, setIsUploading] = useState(false)
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")
  const [lastResult, setLastResult] = useState<WriterResult | null>(null)

  const selectedChapter = useMemo(
    () => data.chapters.find((chapter) => chapter.path === selectedPath) || data.chapters[0],
    [data.chapters, selectedPath]
  )
  const publishableChapters = useMemo(
    () => data.chapters.filter((chapter) => chapter.contentState !== "structure"),
    [data.chapters]
  )
  const previewChapters = useMemo(
    () => (viewMode === "book" ? publishableChapters : selectedChapter ? [selectedChapter] : []),
    [publishableChapters, selectedChapter, viewMode]
  )
  const estimatedPages = useMemo(() => paginateChapters(previewChapters), [previewChapters])
  const measureRef = useRef<HTMLDivElement>(null)
  const [measuredPages, setMeasuredPages] = useState<PreviewPage[] | null>(null)
  const previewPages = measuredPages || estimatedPages

  useLayoutEffect(() => {
    setMeasuredPages(null)
    let cleanupImageListeners: (() => void) | null = null
    let cancelled = false

    function measurePages() {
      if (cancelled) return

      const pages = paginateMeasuredChapters(previewChapters, measureRef.current)
      setMeasuredPages(pages.length > 0 ? pages : null)
    }

    const animationFrame = window.requestAnimationFrame(() => {
      measurePages()

      const pendingImages = Array.from(measureRef.current?.querySelectorAll<HTMLImageElement>("img") || []).filter(
        (image) => !image.complete
      )

      if (pendingImages.length === 0) return

      const handleImageDone = () => measurePages()

      pendingImages.forEach((image) => {
        image.addEventListener("load", handleImageDone, { once: true })
        image.addEventListener("error", handleImageDone, { once: true })
      })

      cleanupImageListeners = () => {
        pendingImages.forEach((image) => {
          image.removeEventListener("load", handleImageDone)
          image.removeEventListener("error", handleImageDone)
        })
      }
    })

    return () => {
      cancelled = true
      window.cancelAnimationFrame(animationFrame)
      cleanupImageListeners?.()
    }
  }, [previewChapters])

  async function refreshStudio() {
    setIsRefreshing(true)
    setError("")

    try {
      const response = await fetch(`/api/book-studio?bookId=${encodeURIComponent(data.bookId)}`)
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Impossibile aggiornare lo Studio Libro")
      }

      setData(payload)
      if (!payload.chapters.some((chapter: BookStudioChapter) => chapter.path === selectedPath)) {
        setSelectedPath(payload.chapters[0]?.path || "")
      }
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsRefreshing(false)
    }
  }

  async function runWriterRequest() {
    if (!selectedChapter) return

    setIsWriting(true)
    setError("")
    setMessage("")
    setLastResult(null)

    try {
      const response = await fetch("/api/manual-writer/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          chapterPath: selectedChapter.path,
          instruction,
          mode: writerMode,
          provider: selectedProvider
        })
      })
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Manual Writer Agent failed")
      }

      setLastResult(payload)
      setMessage("Capitolo aggiornato. Anteprima ricaricata dal vault.")
      await refreshStudio()
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsWriting(false)
    }
  }

  async function uploadImage() {
    if (!imageFile || !selectedChapter) return

    setIsUploading(true)
    setError("")
    setMessage("")

    try {
      const formData = new FormData()
      formData.set("file", imageFile)
      formData.set("bookId", data.bookId)
      formData.set("chapterPath", selectedChapter.path)
      formData.set("caption", caption)

      const response = await fetch("/api/book-studio/assets", {
        method: "POST",
        body: formData
      })
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Upload immagine fallito")
      }

      setImageFile(null)
      setCaption("")
      setMessage(`Immagine aggiunta: ${payload.asset.path}`)
      await refreshStudio()
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <section className="bookStudioPanel" id="studio">
      <header>
        <div>
          <span className="panelKicker">Book Studio</span>
          <h2>Preview visuale e revisione del manuale</h2>
        </div>
        <div className="studioHeaderActions">
          <span className={`writerLlmStatus ${selectedProvider === "local" ? "disabled" : "enabled"}`}>
            <BookOpenCheck size={18} aria-hidden />
            <span>{providerStatusLabel(selectedProvider)}</span>
          </span>
          <button className="studioIconButton" onClick={refreshStudio} disabled={isRefreshing} title="Aggiorna anteprima">
            {isRefreshing ? <Loader2 size={17} className="spin" aria-hidden /> : <RefreshCw size={17} aria-hidden />}
          </button>
        </div>
      </header>

      <div className="studioStats" aria-label="Stato libro">
        <Stat label="Capitoli" value={data.summary.chapters} />
        <Stat label="Scritti" value={data.summary.written} />
        <Stat label="Bozze" value={data.summary.draft} />
        <Stat label="Solo struttura" value={data.summary.structure} />
        <Stat label="Da revisione" value={data.summary.reviewRequired} />
        <Stat label="Immagini" value={data.summary.assets} />
      </div>

      <div className="bookStudioLayout">
        <aside className="bookToc" aria-label="Indice manuale">
          <div className="previewModeToggle">
            <button className={viewMode === "chapter" ? "active" : ""} onClick={() => setViewMode("chapter")}>
              <FileText size={15} aria-hidden />
              Capitolo
            </button>
            <button className={viewMode === "book" ? "active" : ""} onClick={() => setViewMode("book")}>
              <BookOpenCheck size={15} aria-hidden />
              Libro
            </button>
          </div>

          <div className="chapterList">
            {data.chapters.map((chapter) => (
              <button
                className={chapter.path === selectedChapter?.path ? "chapterButton active" : "chapterButton"}
                key={chapter.path}
                onClick={() => {
                  setSelectedPath(chapter.path)
                  setViewMode("chapter")
                }}
              >
                <span>{chapter.outlineSection ? `${chapter.outlineSection}. ` : ""}{chapter.title}</span>
                <small>
                  {chapterStateLabel(chapter.contentState)}
                  {" | "}
                  {chapter.wordCount} parole
                </small>
              </button>
            ))}
          </div>
        </aside>

        <div className="bookPreviewShell">
          <div className="bookPreviewToolbar">
            <div>
              <strong>{data.title}</strong>
              <span>Preview editoriale 16,8 x 24 cm, testo giustificato | aggiornata {formatDate(data.updatedAt)}</span>
            </div>
            <span className="studioBadge">{viewMode === "book" ? "vista libro" : "vista capitolo"}</span>
          </div>

          <div className="bookPages" aria-label="Preview manuale editoriale paginata">
            {previewPages.map((page) => (
              <BookPagePreview page={page} key={`${page.chapter.path}-${page.chapterPageNumber}`} />
            ))}
          </div>

          <div className="paginationMeasure" aria-hidden="true" ref={measureRef}>
            <article className="bookPage paginationMeasurePage">
              {previewChapters.map((chapter) => (
                <div className="paginationMeasureChapter" data-chapter-path={chapter.path} key={chapter.path}>
                  <header className="chapterPreviewHeader paginationFirstHeader">
                    <span className="chapterNumber">{chapter.outlineSection || "Libro"}</span>
                    <div>
                      <h2>{chapter.title}</h2>
                      <BandoPhaseBar chapter={chapter} />
                      <p>
                        {chapterStateLabel(chapter.contentState)}
                        {" | "}
                        {chapter.wordCount} parole
                        {" | "}
                        {chapter.sourceRefs.length} fonti
                      </p>
                    </div>
                  </header>
                  <div className="runningHeader paginationRunningHeader">
                    <span>{chapter.outlineSection ? `${chapter.outlineSection}. ` : ""}{chapter.title}</span>
                    <span>continua</span>
                  </div>
                  <div className="previewBlocks">
                    {chapter.blocks.map((block, index) => (
                      <div className="paginationMeasureBlock" data-block-index={index} key={`${chapter.path}-measure-${index}`}>
                        <PreviewBlock block={block} />
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </article>
          </div>
        </div>

        <aside className="studioControls" aria-label="Controlli revisione libro">
          <section>
            <span className="panelKicker">Capitolo selezionato</span>
            <h3>{selectedChapter?.title || "Nessun capitolo"}</h3>
            {selectedChapter ? (
              <div className="selectedMeta">
                <span>{selectedChapter.path}</span>
                <span>Stato: {chapterStatusLabel(selectedChapter.status)}</span>
                <span>Fonti collegate: {selectedChapter.sourceRefs.length}</span>
                <span>{selectedChapter.reviewRequired ? "Richiede revisione" : "Revisione non richiesta"}</span>
              </div>
            ) : null}
          </section>

          <section>
            <span className="panelKicker">Personalizzazione writer</span>
            <label>
              Azione
              <select value={writerMode} onChange={(event) => setWriterMode(event.target.value as ManualWriterMode)}>
                {modeOptions.map((option) => (
                  <option value={option.value} key={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Modello
              <select value={selectedProvider} onChange={(event) => setSelectedProvider(event.target.value as WriterProvider)}>
                {providerOptions.map((option) => (
                  <option value={option.value} key={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Richiesta
              <textarea value={instruction} onChange={(event) => setInstruction(event.target.value)} rows={8} />
            </label>
            <button className="writerButton full" onClick={runWriterRequest} disabled={isWriting || !selectedChapter}>
              {isWriting ? <Loader2 size={17} className="spin" aria-hidden /> : <Sparkles size={17} aria-hidden />}
              {isWriting ? "Writer in corso" : "Applica al capitolo"}
            </button>
            <small className="controlNote">
              Modello: {providerModelLabel(selectedProvider, writerModel)} | reasoning: {providerReasoningLabel(selectedProvider, writerReasoningEffort)}
            </small>
          </section>

          <section>
            <span className="panelKicker">Immagini e layout</span>
            <label className="fileDrop">
              <ImagePlus size={18} aria-hidden />
              <span>{imageFile ? imageFile.name : "Seleziona immagine"}</span>
              <input
                type="file"
                accept="image/png,image/jpeg,image/webp,image/gif"
                onChange={(event) => setImageFile(event.currentTarget.files?.[0] || null)}
              />
            </label>
            <label>
              Didascalia
              <input value={caption} onChange={(event) => setCaption(event.target.value)} placeholder="Es. Schema Metodo BANDO" />
            </label>
            <button className="secondaryButton full" onClick={uploadImage} disabled={isUploading || !imageFile || !selectedChapter}>
              {isUploading ? <Loader2 size={17} className="spin" aria-hidden /> : <Upload size={17} aria-hidden />}
              {isUploading ? "Caricamento" : "Aggiungi al capitolo"}
            </button>
          </section>

          {data.assets.length > 0 ? (
            <section>
              <span className="panelKicker">Asset libro</span>
              <div className="assetStrip">
                {data.assets.slice(0, 6).map((asset) => (
                  <img src={assetUrl(asset.path)} alt={asset.name} key={asset.path} />
                ))}
              </div>
            </section>
          ) : null}

          {message ? <div className="studioMessage">{message}</div> : null}
          {error ? <div className="writerError">{error}</div> : null}
          {lastResult ? (
            <details className="studioResult">
              <summary>Ultimo output writer</summary>
              <span>{lastResult.chapterPath}</span>
              <pre>{lastResult.draft}</pre>
              {lastResult.warnings.length > 0 ? <small>{lastResult.warnings.join(" | ")}</small> : null}
            </details>
          ) : null}
        </aside>
      </div>
    </section>
  )
}

function chapterStateLabel(state: BookStudioChapter["contentState"]) {
  if (state === "written") return "testo pronto"
  if (state === "draft") return "in revisione"
  return "da sviluppare"
}

function chapterStatusLabel(status: string) {
  const labels: Record<string, string> = {
    draft: "bozza",
    professional_draft: "bozza professionale",
    revised_draft: "revisione editoriale",
    to_expand: "da sviluppare"
  }
  return labels[status] || status.replaceAll("_", " ")
}

function providerStatusLabel(provider: WriterProvider) {
  if (provider === "codex") return "Codex / GPT attivo"
  if (provider === "claude") return "Claude attivo"
  if (provider === "kimi") return "Kimi attivo"
  if (provider === "openai") return "OpenAI API attiva"
  if (provider === "hermes") return "Hermes attivo"

  return "Writer locale"
}

function providerModelLabel(provider: WriterProvider, configuredModel: string) {
  if (provider === "claude") return "claude-opus-4-7"
  if (provider === "kimi") return "kimi-k2.6"
  if (provider === "local") return "local"

  return configuredModel
}

function providerReasoningLabel(provider: WriterProvider, configuredReasoning: string) {
  if (provider === "local" || provider === "kimi" || provider === "openai" || provider === "hermes") return "n/a"

  return configuredReasoning
}

function Stat({ label, value }: { label: string; value: number }) {
  return (
    <div>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
}

function BookPagePreview({ page }: { page: PreviewPage }) {
  const { chapter } = page

  return (
    <article className="bookPage" lang="it">
      {page.isFirstPage ? (
        <header className="chapterPreviewHeader">
          <span className="chapterNumber">{chapter.outlineSection || "Libro"}</span>
          <div>
            <h2>{chapter.title}</h2>
            <BandoPhaseBar chapter={chapter} />
          </div>
        </header>
      ) : (
        <div className="runningHeader">
          <span>{chapter.outlineSection ? `${chapter.outlineSection}. ` : ""}{chapter.title}</span>
          <span>continua</span>
        </div>
      )}

      <div className="previewBlocks">
        {page.blocks.map((block, index) => (
          <PreviewBlock block={block} key={`${chapter.path}-${page.chapterPageNumber}-${index}`} />
        ))}
      </div>

      <footer className="pageFooter">
        <span>Il Metodo BANDO</span>
        <span>{page.pageNumber}</span>
      </footer>
    </article>
  )
}

function PreviewBlock({ block }: { block: MarkdownBlock }) {
  if (block.type === "heading") {
    if ((block.level || 2) <= 2) return <h3>{block.text}</h3>
    if (block.level === 3) return <h4>{block.text}</h4>

    return <h5>{block.text}</h5>
  }

  if (block.type === "list") {
    if (block.ordered) {
      return (
        <ol start={block.start || 1}>
          {(block.items || []).map((item, index) => (
            <li key={`${item}-${index}`}>{item}</li>
          ))}
        </ol>
      )
    }

    return (
      <ul>
        {(block.items || []).map((item, index) => (
          <li key={`${item}-${index}`}>{item}</li>
        ))}
      </ul>
    )
  }

  if (block.type === "image") {
    const src = block.path ? assetUrl(block.path) : ""

    if (!src) {
      return <p className="missingAsset">Immagine non disponibile: {block.path}</p>
    }

    return (
      <figure>
        <img src={src} alt={block.alt || "Immagine capitolo"} />
        {block.alt ? <figcaption>{block.alt}</figcaption> : null}
      </figure>
    )
  }

  if (block.type === "table") {
    return (
      <div className="previewTableWrap">
        <table className="previewTable">
          <thead>
            <tr>
              {(block.headers || []).map((header) => (
                <th key={header}>{header}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {(block.rows || []).map((row, rowIndex) => (
              <tr key={`${row.join("-")}-${rowIndex}`}>
                {row.map((cell, cellIndex) => (
                  <td key={`${cell}-${cellIndex}`}>{cell}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )
  }

  if (block.type === "code") {
    return <pre>{block.text}</pre>
  }

  if (block.type === "callout") {
    if (block.calloutType === "caption") {
      return <p className="previewCaption">{block.text || block.title}</p>
    }

    const className = `previewCallout ${calloutClassName(block.calloutType)}`

    return (
      <aside className={className}>
        {block.title ? <strong>{block.title}</strong> : null}
        {block.text ? <p>{block.text}</p> : null}
      </aside>
    )
  }

  return <p>{block.text}</p>
}

function BandoPhaseBar({ chapter }: { chapter: BookStudioChapter }) {
  const phases = [
    { letter: "B", label: "Bando" },
    { letter: "A", label: "Aree" },
    { letter: "N", label: "Nuclei" },
    { letter: "D", label: "Diario" },
    { letter: "O", label: "Output" }
  ]
  const activeIndex = getBandoPhaseIndex(chapter.outlineSection)

  return (
    <div className="bandoPhaseBar" aria-label="Fasi Metodo BANDO">
      {phases.map((phase, index) => (
        <span className={index === activeIndex ? "active" : ""} key={phase.letter}>
          <strong>{phase.letter}</strong>
          <small>{phase.label}</small>
        </span>
      ))}
    </div>
  )
}

function getBandoPhaseIndex(outlineSection: string) {
  const section = Number.parseInt(outlineSection, 10)

  if (!Number.isFinite(section)) return -1
  if (section <= 3) return 0
  if (section <= 8) return 1
  if (section <= 13) return 2
  if (section <= 18) return 3

  return 4
}

function calloutClassName(calloutType = "") {
  if (calloutType === "warning") return "warning"
  if (calloutType === "tip") return "tip"
  if (calloutType === "important") return "important"
  if (calloutType === "quote") return "quote"

  return "note"
}

function assetUrl(value: string) {
  if (value.startsWith("http://") || value.startsWith("https://") || value.startsWith("/api/")) {
    return value
  }

  const normalized = value.replace(/\\/g, "/").replace(/^\/+/, "")

  if (!isRenderableAssetPath(normalized)) return ""

  return `/api/book-studio/assets/file?path=${encodeURIComponent(normalized)}`
}

function isRenderableAssetPath(value: string) {
  return value.startsWith("raw/assets/") || /^books\/[a-z0-9-]+\/assets\//.test(value)
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("it-IT", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  }).format(new Date(value))
}

function paginateChapters(chapters: BookStudioChapter[]): PreviewPage[] {
  const pages: PreviewPage[] = []
  let pageNumber = 1

  for (const chapter of chapters) {
    const chapterPages = paginateBlocks(chapter)

    for (const page of chapterPages) {
      pages.push({
        ...page,
        pageNumber: pageNumber++
      })
    }
  }

  return pages
}

function paginateMeasuredChapters(chapters: BookStudioChapter[], root: HTMLDivElement | null): PreviewPage[] {
  if (!root) return []

  const measurePage = root.querySelector<HTMLElement>(".paginationMeasurePage")
  if (!measurePage) return []

  const pageStyle = window.getComputedStyle(measurePage)
  const pageHeight = measurePage.getBoundingClientRect().height
  const pageBudget = Math.max(
    0,
    pageHeight - toPixels(pageStyle.paddingTop) - toPixels(pageStyle.paddingBottom) - PAGE_MEASURE_GUARD_SPACE
  )
  const chapterElements = Array.from(root.querySelectorAll<HTMLElement>(".paginationMeasureChapter"))
  const pages: PreviewPage[] = []
  let pageNumber = 1

  chapters.forEach((chapter, chapterIndex) => {
    const chapterElement = chapterElements[chapterIndex]

    if (!chapterElement || pageBudget <= 0) {
      for (const page of paginateBlocks(chapter)) {
        pages.push({ ...page, pageNumber: pageNumber++ })
      }

      return
    }

    const firstHeaderHeight = outerHeight(chapterElement.querySelector<HTMLElement>(".paginationFirstHeader")) || FIRST_PAGE_HEADER_COST
    const runningHeaderHeight = outerHeight(chapterElement.querySelector<HTMLElement>(".paginationRunningHeader")) || RUNNING_HEADER_COST
    const blockElements = Array.from(chapterElement.querySelectorAll<HTMLElement>(".paginationMeasureBlock"))
    const blockHeights = chapter.blocks.map((block, index) => Math.ceil(outerHeight(blockElements[index]) || estimateBlockCost(block)))
    const chapterPages = paginateBlocksByHeight(chapter, blockHeights, pageBudget, firstHeaderHeight, runningHeaderHeight)

    for (const page of chapterPages) {
      pages.push({ ...page, pageNumber: pageNumber++ })
    }
  })

  return pages
}

function paginateBlocksByHeight(
  chapter: BookStudioChapter,
  blockHeights: number[],
  pageBudget: number,
  firstHeaderHeight: number,
  runningHeaderHeight: number
): Array<Omit<PreviewPage, "pageNumber">> {
  const pages: Array<Omit<PreviewPage, "pageNumber">> = []
  let blocks: MarkdownBlock[] = []
  let usedBlockHeights: number[] = []
  let chapterPageNumber = 1
  let used = firstHeaderHeight

  function pushPage() {
    pages.push({
      chapter,
      blocks,
      chapterPageNumber,
      isFirstPage: chapterPageNumber === 1
    })
    chapterPageNumber += 1
    blocks = []
    usedBlockHeights = []
    used = runningHeaderHeight
  }

  for (let index = 0; index < chapter.blocks.length; index += 1) {
    const block = chapter.blocks[index]
    const nextBlock = chapter.blocks[index + 1]
    const blockHeight = blockHeights[index] || estimateBlockCost(block)
    const keepWithNextHeight = shouldKeepWithNext(block, nextBlock) && nextBlock
      ? blockHeights[index + 1] || estimateBlockCost(nextBlock)
      : 0

    if (blocks.length > 0 && used + blockHeight + keepWithNextHeight > pageBudget) {
      const lastBlock = blocks.at(-1)
      const lastBlockHeight = usedBlockHeights.at(-1) || 0

      if (blocks.length === 1 && lastBlock?.type === "heading") {
        // Keep a heading with the following block; an orphan heading is worse than a tight page.
      } else if (blocks.length > 1 && lastBlock?.type === "heading") {
        blocks.pop()
        usedBlockHeights.pop()
        used -= lastBlockHeight
        pushPage()
        blocks.push(lastBlock)
        usedBlockHeights.push(lastBlockHeight)
        used += lastBlockHeight
      } else {
        pushPage()
      }
    }

    blocks.push(block)
    usedBlockHeights.push(blockHeight)
    used += blockHeight
  }

  if (blocks.length > 0 || pages.length === 0) {
    pushPage()
  }

  return pages
}

function paginateBlocks(chapter: BookStudioChapter): Array<Omit<PreviewPage, "pageNumber">> {
  const pages: Array<Omit<PreviewPage, "pageNumber">> = []
  let blocks: MarkdownBlock[] = []
  let usedBlockCosts: number[] = []
  let chapterPageNumber = 1
  let used = FIRST_PAGE_HEADER_COST

  function pushPage() {
    pages.push({
      chapter,
      blocks,
      chapterPageNumber,
      isFirstPage: chapterPageNumber === 1
    })
    chapterPageNumber += 1
    blocks = []
    usedBlockCosts = []
    used = RUNNING_HEADER_COST
  }

  for (let index = 0; index < chapter.blocks.length; index += 1) {
    const block = chapter.blocks[index]
    const nextBlock = chapter.blocks[index + 1]
    const cost = estimateBlockCost(block)
    const keepWithNextCost = shouldKeepWithNext(block, nextBlock) ? estimateBlockCost(nextBlock) : 0
    const budget = 920

    if (blocks.length > 0 && used + cost + keepWithNextCost > budget) {
      const lastBlock = blocks.at(-1)
      const lastBlockCost = usedBlockCosts.at(-1) || 0

      if (blocks.length === 1 && lastBlock?.type === "heading") {
        // Keep a heading with the following block; an orphan heading is worse than a tight page.
      } else if (blocks.length > 1 && lastBlock?.type === "heading") {
        blocks.pop()
        usedBlockCosts.pop()
        used -= lastBlockCost
        pushPage()
        blocks.push(lastBlock)
        usedBlockCosts.push(lastBlockCost)
        used += lastBlockCost
      } else {
        pushPage()
      }
    }

    blocks.push(block)
    usedBlockCosts.push(cost)
    used += cost
  }

  if (blocks.length > 0 || pages.length === 0) {
    pushPage()
  }

  return pages
}

function shouldKeepWithNext(block: MarkdownBlock, nextBlock?: MarkdownBlock) {
  if (!nextBlock) return false

  if (block.type === "heading") {
    return nextBlock.type !== "heading"
  }

  if (block.type === "paragraph" && wordCount(block.text || "") <= 24) {
    return nextBlock.type === "image" || nextBlock.type === "code"
  }

  return false
}

function estimateBlockCost(block: MarkdownBlock) {
  if (block.type === "heading") {
    const level = block.level || 3

    if (level <= 2) return 52
    if (level === 3) return 40

    return 32
  }

  if (block.type === "paragraph") {
    const words = wordCount(block.text || "")
    return Math.ceil(words / 13) * 23 + 8
  }

  if (block.type === "list") {
    return (block.items || []).reduce((total, item) => total + Math.ceil(wordCount(item) / 12) * 19 + 6, 18)
  }

  if (block.type === "table") {
    return ((block.rows?.length || 0) + 1) * 28 + 18
  }

  if (block.type === "image") {
    return 315
  }

  if (block.type === "callout") {
    return Math.ceil(wordCount(`${block.title || ""} ${block.text || ""}`) / 12) * 21 + 34
  }

  if (block.type === "code") {
    return (block.text || "").split("\n").length * 18 + 24
  }

  return 36
}

function wordCount(value: string) {
  return value.split(/\s+/).filter(Boolean).length
}

function outerHeight(element?: HTMLElement | null) {
  if (!element) return 0

  const style = window.getComputedStyle(element)
  return element.getBoundingClientRect().height + toPixels(style.marginTop) + toPixels(style.marginBottom)
}

function toPixels(value: string) {
  const parsed = Number.parseFloat(value)
  return Number.isFinite(parsed) ? parsed : 0
}
