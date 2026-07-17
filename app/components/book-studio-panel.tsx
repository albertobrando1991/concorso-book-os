"use client"

import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react"
import {
  BookOpenCheck,
  FileText,
  ImagePlus,
  Loader2,
  RefreshCw,
  Sparkles,
  Upload,
  WandSparkles
} from "lucide-react"
import type { ManualWriterMode, RevisionDiffSummary } from "@/src/server/agents/manual-writer-agent"
import type { BookStudioChapter, BookStudioData, MarkdownBlock } from "@/src/server/book/book-preview"
import { ricettarioModuleLabel } from "@/src/server/book/book-studio-labels"
import type { WriterProvider } from "@/src/server/config"

interface BookStudioPanelProps {
  initialData: BookStudioData
  initialChapterPath?: string
  writerProvider: WriterProvider
  writerModel: string
  writerReasoningEffort: string
}

interface WriterResult {
  chapterPath: string
  changedFiles: string[]
  draft: string
  warnings: string[]
  revisionDiff?: RevisionDiffSummary
}

interface BookStudioRefreshDetail {
  bookId?: string
  chapterPath?: string
  message?: string
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
const FRONT_MATTER_FIRST_PAGE_COST = 64
const FRONT_MATTER_RUNNING_PAGE_COST = 36
const MAIN_PAGE_FALLBACK_BUDGET = 920
const FRONT_MATTER_PAGE_BUDGET = 980
const PAGE_MEASURE_GUARD_SPACE = 12
const PAGE_RENDER_GUARD_SPACE = 10

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
  initialChapterPath,
  writerProvider,
  writerModel,
  writerReasoningEffort
}: BookStudioPanelProps) {
  const [data, setData] = useState(initialData)
  const [selectedPath, setSelectedPath] = useState(getInitialChapterPath(initialData, initialChapterPath))
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
  const [isRevising, setIsRevising] = useState(false)
  const [isUploading, setIsUploading] = useState(false)
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")
  const [lastResult, setLastResult] = useState<WriterResult | null>(null)
  const [revisionStatus, setRevisionStatus] = useState("")

  const selectedChapter = useMemo(
    () => data.chapters.find((chapter) => chapter.path === selectedPath) || data.chapters[0],
    [data.chapters, selectedPath]
  )
  const isVolumeBook = data.bookId.startsWith("volumi/")
  const selectedChapterIsGenerated = Boolean(selectedChapter?.isGenerated)
  const mainChapters = useMemo(
    () => data.chapters.filter((chapter) => chapter.bookScope === "main"),
    [data.chapters]
  )
  const ricettarioChapters = useMemo(
    () => data.chapters.filter((chapter) => chapter.bookScope === "ricettario"),
    [data.chapters]
  )
  const publishableChapters = useMemo(
    () =>
      data.chapters.filter(
        (chapter) => chapter.bookScope === "main" && (isVolumeBook || chapter.contentState !== "structure")
      ),
    [data.chapters, isVolumeBook]
  )
  const previewChapters = useMemo(
    () => (viewMode === "book" ? publishableChapters : selectedChapter ? [selectedChapter] : []),
    [publishableChapters, selectedChapter, viewMode]
  )
  const estimatedPages = useMemo(() => paginateChapters(previewChapters), [previewChapters])
  const measureRef = useRef<HTMLDivElement>(null)
  const bookPagesRef = useRef<HTMLDivElement>(null)
  const [measuredPages, setMeasuredPages] = useState<PreviewPage[] | null>(null)
  const previewPages = measuredPages || estimatedPages

  useEffect(() => {
    setData(initialData)
    setSelectedPath(getInitialChapterPath(initialData, initialChapterPath))
    setViewMode("chapter")
    setMessage("")
    setError("")
    setLastResult(null)
    setMeasuredPages(null)
  }, [initialData.bookId, initialChapterPath])

  const openChapter = useCallback((chapter: BookStudioChapter, event?: React.MouseEvent<HTMLAnchorElement>) => {
    event?.preventDefault()
    setSelectedPath(chapter.path)
    setViewMode("chapter")
    setMeasuredPages(null)
    window.history.replaceState(null, "", chapterStudioHref(data.bookId, chapter.path))
  }, [data.bookId])

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

      void document.fonts?.ready.then(() => measurePages())

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
    window.addEventListener("resize", measurePages)

    return () => {
      cancelled = true
      window.cancelAnimationFrame(animationFrame)
      window.removeEventListener("resize", measurePages)
      cleanupImageListeners?.()
    }
  }, [previewChapters])

  useLayoutEffect(() => {
    if (!measuredPages) return

    const animationFrame = window.requestAnimationFrame(() => {
      const refined = refineRenderedPageOverflows(measuredPages, bookPagesRef.current)

      if (refined !== measuredPages) {
        setMeasuredPages(refined)
      }
    })

    return () => window.cancelAnimationFrame(animationFrame)
  }, [measuredPages])

  const refreshStudio = useCallback(async (preferredPath = selectedPath, nextMessage = "") => {
    setIsRefreshing(true)
    setError("")

    try {
      const response = await fetch(`/api/book-studio?bookId=${encodeURIComponent(data.bookId)}`)
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Impossibile aggiornare lo Studio Libro")
      }

      setData(payload)
      if (payload.chapters.some((chapter: BookStudioChapter) => chapter.path === preferredPath)) {
        setSelectedPath(preferredPath)
      } else if (!payload.chapters.some((chapter: BookStudioChapter) => chapter.path === selectedPath)) {
        setSelectedPath(payload.chapters[0]?.path || "")
      }
      if (nextMessage) {
        setMessage(nextMessage)
      }
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsRefreshing(false)
    }
  }, [data.bookId, selectedPath])

  useEffect(() => {
    function handleBookStudioRefresh(event: Event) {
      const detail = (event as CustomEvent<BookStudioRefreshDetail>).detail
      if (!detail?.bookId || detail.bookId !== data.bookId) return

      void refreshStudio(
        detail.chapterPath || selectedPath,
        detail.message || "Preview aggiornata dopo Manual Writer."
      )
    }

    window.addEventListener("book-studio:refresh", handleBookStudioRefresh)

    return () => window.removeEventListener("book-studio:refresh", handleBookStudioRefresh)
  }, [data.bookId, refreshStudio, selectedPath])

  async function runWriterRequest() {
    if (!selectedChapter || selectedChapter.isGenerated) return

    setIsWriting(true)
    setError("")
    setMessage("")
    setLastResult(null)
    setRevisionStatus("")

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
      await refreshStudio(selectedChapter.path)
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsWriting(false)
    }
  }

  async function runHumanizerRevision() {
    if (!selectedChapter || selectedChapter.isGenerated) return

    setIsRevising(true)
    setError("")
    setMessage("")
    setLastResult(null)
    setRevisionStatus("Humanizer sta leggendo il capitolo selezionato e prepara il confronto.")
    const revisionSteps = [
      "Humanizer sta leggendo il capitolo selezionato e prepara il confronto.",
      "Sto cercando frasi artificiali, formule ripetitive e passaggi da rendere piu naturali.",
      "La revisione riscrive solo dove serve e conserva struttura, fonti e Metodo BANDO.",
      "Appena il provider restituisce il testo mostro qui il prima/dopo della revisione."
    ]
    let revisionStepIndex = 0
    const revisionTimer = window.setInterval(() => {
      revisionStepIndex = (revisionStepIndex + 1) % revisionSteps.length
      setRevisionStatus(revisionSteps[revisionStepIndex])
    }, 2800)

    try {
      const response = await fetch("/api/manual-writer/revise", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          chapterPath: selectedChapter.path,
          provider: selectedProvider,
          instruction: "Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti e struttura Metodo BANDO, riscrivi solo i passaggi necessari."
        })
      })
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Revisione humanizer fallita")
      }

      setLastResult(payload)
      setRevisionStatus("Modifiche ricevute. Aggiorno preview e differenze.")
      setMessage(revisionResultMessage(payload))
      await refreshStudio(selectedChapter.path)
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      window.clearInterval(revisionTimer)
      setIsRevising(false)
    }
  }

  async function uploadImage() {
    if (!imageFile || !selectedChapter || selectedChapter.isGenerated) return

    setIsUploading(true)
    setError("")
    setMessage("")

    try {
      const formData = new FormData()
      formData.set("file", imageFile)
      formData.set("bookId", bookIdFromChapterPath(selectedChapter.path) || data.bookId)
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
      await refreshStudio(selectedChapter.path)
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
          <button className="studioIconButton" onClick={() => refreshStudio()} disabled={isRefreshing} title="Aggiorna anteprima">
            {isRefreshing ? <Loader2 size={17} className="spin" aria-hidden /> : <RefreshCw size={17} aria-hidden />}
          </button>
        </div>
      </header>

      <div className="studioStats" aria-label="Stato libro">
        <Stat label="Sezioni" value={data.summary.chapters} />
        <Stat label="Volume" value={data.summary.mainChapters} />
        <Stat label="Ricettario" value={data.summary.ricettarioModules} />
        <Stat label="Scritti" value={data.summary.written} />
        <Stat label="Bozze" value={data.summary.draft} />
        <Stat label="Solo struttura" value={data.summary.structure} />
        <Stat label="Da revisione" value={data.summary.reviewRequired} />
        <Stat label="Immagini" value={data.summary.assets} />
      </div>

      <div className="bookStudioLayout">
        <aside className="bookToc" aria-label="Indice manuale e prime pagine">
          <div className="previewModeToggle">
            <button className={viewMode === "chapter" ? "active" : ""} onClick={() => setViewMode("chapter")}>
              <FileText size={15} aria-hidden />
              Sezione
            </button>
            <button className={viewMode === "book" ? "active" : ""} onClick={() => setViewMode("book")}>
              <BookOpenCheck size={15} aria-hidden />
              Libro
            </button>
          </div>

          <div className="chapterList">
            <p className="tocSectionLabel">{isVolumeBook ? "Volume completo" : "Volume principale"}</p>
            {mainChapters.map((chapter) => (
              <ChapterTocButton
                bookId={data.bookId}
                chapter={chapter}
                isActive={chapter.path === selectedChapter?.path}
                key={chapter.path}
                onSelect={openChapter}
              />
            ))}
            {ricettarioChapters.length > 0 ? (
              <>
                <p className="tocSectionLabel tocSectionLabelRicettario">Ricettario digitale</p>
                {ricettarioChapters.map((chapter) => (
                  <ChapterTocButton
                    bookId={data.bookId}
                    chapter={chapter}
                    isActive={chapter.path === selectedChapter?.path}
                    key={chapter.path}
                    onSelect={openChapter}
                  />
                ))}
              </>
            ) : null}
          </div>
        </aside>

        <div className="bookPreviewShell">
          <div className="bookPreviewToolbar">
            <div>
              <strong>{data.title}</strong>
              <span>Master editoriale A4, testo giustificato | aggiornato {formatDate(data.updatedAt)}</span>
            </div>
            <span className="studioBadge">{viewMode === "book" ? "vista libro" : "vista capitolo"}</span>
          </div>

          {isRevising ? (
            <div className="previewRevisionStatus" role="status" aria-live="polite">
              <Loader2 size={17} className="spin" aria-hidden />
              <span>{revisionStatus || "Revisione Humanizer in corso."}</span>
            </div>
          ) : null}

          <div className="bookPages" aria-label="Preview manuale editoriale paginata" ref={bookPagesRef}>
            {previewPages.map((page) => (
              <BookPagePreview bookId={data.bookId} page={page} key={`${page.chapter.path}-${page.chapterPageNumber}`} />
            ))}
          </div>

          <div className="paginationMeasure" aria-hidden="true" ref={measureRef}>
            <article className="bookPage paginationMeasurePage">
              {previewChapters.map((chapter) => (
                <div className="paginationMeasureChapter" data-chapter-path={chapter.path} key={chapter.path}>
                  <header className="chapterPreviewHeader paginationFirstHeader">
                    {chapter.sectionType === "front_matter" ? (
                      <div className="frontMatterMeasureHeader">
                        <span>{sectionLabel(chapter)}</span>
                      </div>
                    ) : (
                      <>
                        <span className="chapterNumber">{chapterNumberLabel(chapter)}</span>
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
                      </>
                    )}
                  </header>
                  <div className="runningHeader paginationRunningHeader">
                    <span>{sectionLabel(chapter)}</span>
                    <span>continua</span>
                  </div>
                  <div className="previewBlocks">
                    {chapter.blocks.map((block, index) => (
                      <div className="paginationMeasureBlock" data-block-index={index} key={`${chapter.path}-measure-${index}`}>
                        <PreviewBlock block={block} bookId={data.bookId} />
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
            <span className="panelKicker">Sezione selezionata</span>
            <h3>{selectedChapter?.title || "Nessun capitolo"}</h3>
            {selectedChapter ? (
              <div className="selectedMeta">
                <span>{selectedChapter.path}</span>
                {selectedChapter.isGenerated ? <span>Sezione generata dal layout volume</span> : null}
                <span>Stato: {chapterStatusLabel(selectedChapter.status)}</span>
                <span>Fonti collegate: {selectedChapter.sourceRefs.length}</span>
                <span>{selectedChapter.reviewRequired ? "Richiede revisione" : "Revisione non richiesta"}</span>
              </div>
            ) : null}
          </section>

          <section className="revisionBox">
            <span className="panelKicker">REVISIONE</span>
            <h3>Humanizer editoriale</h3>
            <button className="revisionButton full" onClick={runHumanizerRevision} disabled={isRevising || isWriting || !selectedChapter || selectedChapterIsGenerated}>
              {isRevising ? <Loader2 size={17} className="spin" aria-hidden /> : <WandSparkles size={17} aria-hidden />}
              {isRevising ? "Revisione in corso" : "Rivedi e riscrivi dove serve"}
            </button>
            <small className="controlNote">
              Provider: {providerModelLabel(selectedProvider, writerModel)} | skill: humanizer
            </small>
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
            <button className="writerButton full" onClick={runWriterRequest} disabled={isWriting || isRevising || !selectedChapter || selectedChapterIsGenerated}>
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
            <button className="secondaryButton full" onClick={uploadImage} disabled={isUploading || !imageFile || !selectedChapter || selectedChapterIsGenerated}>
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
              <summary>Ultimo testo completo</summary>
              <span>{lastResult.chapterPath}</span>
              <pre>{lastResult.draft}</pre>
              {lastResult.warnings.length > 0 ? <small>{lastResult.warnings.join(" | ")}</small> : null}
            </details>
          ) : null}
        </aside>
      </div>

      {lastResult?.revisionDiff ? <RevisionDiffPanel result={lastResult} /> : null}
    </section>
  )
}

function getInitialChapterPath(data: BookStudioData, requestedPath?: string) {
  if (requestedPath && data.chapters.some((chapter) => chapter.path === requestedPath)) {
    return requestedPath
  }

  return data.chapters[0]?.path || ""
}

function chapterStudioHref(bookId: string, chapterPath: string) {
  return `/?bookId=${encodeURIComponent(bookId)}&chapterPath=${encodeURIComponent(chapterPath)}#studio`
}

function RevisionDiffPanel({ result }: { result: WriterResult }) {
  const diff = result.revisionDiff
  if (!diff) return null

  return (
    <section className="revisionDiffPanel" aria-label="Modifiche Humanizer">
      <header>
        <div>
          <span className="panelKicker">Modifiche Humanizer</span>
          <h3>{diff.changed ? "Cosa e stato riscritto" : "Nessuna modifica testuale rilevata"}</h3>
        </div>
        <div className="revisionDiffStats" aria-label="Statistiche revisione">
          <span className="diffAdded">+{diff.additions}</span>
          <span className="diffRemoved">-{diff.deletions}</span>
          <span>
            {diff.beforeWordCount} a {diff.afterWordCount} parole
          </span>
        </div>
      </header>

      {diff.changed ? (
        <div className="revisionDiffList">
          {diff.previewLines.map((line, index) => (
            <div className={`diffLine ${line.type}`} key={`${line.type}-${line.lineNumber}-${index}`}>
              <span className="diffSign">{line.type === "added" ? "+" : "-"}</span>
              <span className="diffLineNumber">{line.lineNumber}</span>
              <code className="diffText">{line.text}</code>
            </div>
          ))}
          {diff.additions + diff.deletions > diff.previewLines.length ? (
            <p className="diffTruncated">
              Mostrate {diff.previewLines.length} righe modificate su {diff.additions + diff.deletions}.
            </p>
          ) : null}
        </div>
      ) : (
        <p className="diffEmpty">
          Il testo restituito e equivalente al corpo precedente del capitolo: la revisione ha aggiornato solo metadati o non ha trovato passaggi da riscrivere.
        </p>
      )}
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

function revisionResultMessage(result: WriterResult) {
  const diff = result.revisionDiff

  if (!diff) return "REVISIONE applicata. Anteprima ricaricata dal vault."
  if (!diff.changed) return "REVISIONE applicata. Nessuna modifica testuale rilevata; anteprima ricaricata."

  return `REVISIONE applicata: ${diff.additions} righe aggiunte, ${diff.deletions} righe rimosse. Anteprima ricaricata.`
}

function ChapterTocButton({
  bookId,
  chapter,
  isActive,
  onSelect
}: {
  bookId: string
  chapter: BookStudioChapter
  isActive: boolean
  onSelect: (chapter: BookStudioChapter, event: React.MouseEvent<HTMLAnchorElement>) => void
}) {
  return (
    <a
      href={chapterStudioHref(bookId, chapter.path)}
      className={isActive ? "chapterButton active" : "chapterButton"}
      onClick={(event) => onSelect(chapter, event)}
      aria-current={isActive ? "page" : undefined}
    >
      <span>{sectionLabel(chapter)}</span>
      <small>
        {chapterStateLabel(chapter.contentState)}
        {" | "}
        {chapter.wordCount} parole
      </small>
    </a>
  )
}

function sectionLabel(chapter: BookStudioChapter) {
  if (chapter.sectionType === "front_matter") return chapter.title

  if (chapter.volumeModuleCode) {
    const prefix = chapter.outlineSection ? `${chapter.volumeModuleCode} ${compactOutlineLabel(chapter.outlineSection)}` : chapter.volumeModuleCode

    return `${prefix}. ${chapter.title}`
  }

  if (chapter.bookScope === "ricettario") {
    const moduleLabel = ricettarioModuleLabel(chapter.outlineSection)

    return moduleLabel ? `${moduleLabel}. ${chapter.title}` : chapter.title
  }

  return chapter.outlineSection ? `${chapter.outlineSection}. ${chapter.title}` : chapter.title
}

function chapterNumberLabel(chapter: BookStudioChapter) {
  if (chapter.volumeModuleCode) {
    const outline = compactOutlineLabel(chapter.outlineSection)

    return outline ? `${chapter.volumeModuleCode} ${outline}` : chapter.volumeModuleCode
  }

  return chapter.outlineSection || "Libro"
}

function compactOutlineLabel(outlineSection: string) {
  const normalized = outlineSection.trim()

  if (/^[A-Z]$/i.test(normalized)) return `App. ${normalized.toUpperCase()}`

  return normalized
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

function BookPagePreview({ bookId, page }: { bookId: string; page: PreviewPage }) {
  const { chapter } = page

  if (chapter.sectionType === "front_matter") {
    return <FrontMatterPagePreview bookId={bookId} page={page} />
  }

  return (
    <article className="bookPage" lang="it">
      {page.isFirstPage ? (
        <header className="chapterPreviewHeader">
          <span className="chapterNumber">{chapterNumberLabel(chapter)}</span>
          <div>
            <h2>{chapter.title}</h2>
            <BandoPhaseBar chapter={chapter} />
          </div>
        </header>
      ) : (
        <div className="runningHeader">
          <span>{sectionLabel(chapter)}</span>
          <span>continua</span>
        </div>
      )}

      <div className="previewBlocks">
        {page.blocks.map((block, index) => (
          <PreviewBlock block={block} bookId={bookId} key={`${chapter.path}-${page.chapterPageNumber}-${index}`} />
        ))}
      </div>

      <footer className="pageFooter">
        <span>Il Metodo BANDO</span>
        <span>{page.pageNumber}</span>
      </footer>
    </article>
  )
}

function FrontMatterPagePreview({ bookId, page }: { bookId: string; page: PreviewPage }) {
  const { chapter } = page
  const layoutClass = frontMatterLayoutClass(chapter.frontMatterLayout)

  if (chapter.frontMatterLayout === "digital-services") {
    return <DigitalServicesPagePreview bookId={bookId} page={page} layoutClass={layoutClass} />
  }

  return (
    <article className={`bookPage frontMatterPage ${layoutClass}`} lang="it">
      {page.chapterPageNumber > 1 ? (
        <div className="runningHeader">
          <span>{chapter.title}</span>
          <span>continua</span>
        </div>
      ) : null}

      <div className="frontMatterBrand">Capitale Personale</div>
      <div className="previewBlocks frontMatterBlocks">
        {page.blocks.map((block, index) => (
          <PreviewBlock block={block} bookId={bookId} key={`${chapter.path}-${page.chapterPageNumber}-${index}`} />
        ))}
      </div>

      {chapter.frontMatterLayout === "title-page" ? (
        <div className="titlePageWordmark">Capitale Personale</div>
      ) : (
        <footer className="pageFooter frontMatterFooter">
          <span>www.capitalepersonale.it</span>
          <span>{page.pageNumber}</span>
        </footer>
      )}
    </article>
  )
}

function DigitalServicesPagePreview({ bookId, page, layoutClass }: { bookId: string; page: PreviewPage; layoutClass: string }) {
  const imageIndex = page.blocks.findIndex((block) => block.type === "image")
  const heroBlocks = imageIndex >= 0 ? page.blocks.slice(0, imageIndex) : page.blocks.slice(0, 2)
  const imageBlock = imageIndex >= 0 ? page.blocks[imageIndex] : undefined
  const bodyBlocks = imageIndex >= 0 ? page.blocks.slice(imageIndex + 1) : page.blocks.slice(2)

  return (
    <article className={`bookPage frontMatterPage ${layoutClass}`} lang="it">
      <div className="digitalServicesHero">
        <div className="digitalHeroCopy">
          {heroBlocks.map((block, index) => (
            <PreviewBlock block={block} bookId={bookId} key={`${page.chapter.path}-hero-${index}`} />
          ))}
        </div>
        {imageBlock ? (
          <div className="digitalQrBox">
            <PreviewBlock block={imageBlock} bookId={bookId} />
          </div>
        ) : null}
      </div>

      <div className="previewBlocks digitalServicesContent">
        {bodyBlocks.map((block, index) => (
          <PreviewBlock block={block} bookId={bookId} key={`${page.chapter.path}-${page.chapterPageNumber}-${index}`} />
        ))}
      </div>

      <footer className="pageFooter frontMatterFooter">
        <span>www.capitalepersonale.it</span>
        <span>{page.pageNumber}</span>
      </footer>
    </article>
  )
}

function frontMatterLayoutClass(value: string) {
  const normalized = value.replace(/[^a-z0-9-]/gi, "").toLowerCase()

  return normalized ? `frontMatter-${normalized}` : "frontMatter-standard"
}

function PreviewBlock({ block, bookId }: { block: MarkdownBlock; bookId?: string }) {
  if (block.type === "heading") {
    if ((block.level || 2) <= 2) return <h3>{block.text}</h3>
    if (block.level === 3) return <h4>{block.text}</h4>

    return <h5>{block.text}</h5>
  }

  if (block.type === "index-part") {
    return (
      <div className="indexPart">
        {block.number ? <span>{block.number}</span> : null}
        <strong>{block.text}</strong>
      </div>
    )
  }

  if (block.type === "index-chapter") {
    const content = (
      <>
        <span className="indexChapterLabel">{block.number}</span>
        <span className="indexLineTitle">{block.text}</span>
        <span className="indexLeader" aria-hidden />
        <span className="indexPageNumber">{block.pageNumber}</span>
      </>
    )

    if (bookId && block.path) {
      return (
        <a className="indexLine indexChapterLine" href={chapterStudioHref(bookId, block.path)}>
          {content}
        </a>
      )
    }

    return (
      <div className="indexLine indexChapterLine">
        {content}
      </div>
    )
  }

  if (block.type === "index-row") {
    return (
      <div className="indexLine indexSubLine">
        <span className="indexSubNumber">{block.number}</span>
        <span className="indexLineTitle">{block.text}</span>
        <span className="indexLeader" aria-hidden />
        <span className="indexPageNumber">{block.pageNumber}</span>
      </div>
    )
  }

  if (block.type === "index-entry") {
    const items = block.items || []

    return (
      <section className="indexEntry">
        <h4>{block.text}</h4>
        {items.length > 0 ? (
          <div className="indexEntryTopics">
            {items.map((item, index) => (
              <span key={`${item}-${index}`}>{item}</span>
            ))}
          </div>
        ) : null}
      </section>
    )
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
    const showHeader = !block.continued

    return (
      <div className={`previewTableWrap${block.continued ? " continuedTable" : ""}`}>
        <table className="previewTable">
          {showHeader ? (
            <thead>
              <tr>
                {(block.headers || []).map((header, index) => (
                  <th key={`${header}-${index}`}>{header}</th>
                ))}
              </tr>
            </thead>
          ) : null}
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
  if (chapter.bookScope === "ricettario") {
    const moduleLabel = ricettarioModuleLabel(chapter.outlineSection)

    return (
      <div className="bandoPhaseBar ricettarioScopeBar" aria-label="Modulo ricettario digitale">
        <span className="active">
          <strong>{moduleLabel || "R"}</strong>
          <small>Ricettario digitale</small>
        </span>
      </div>
    )
  }

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

function bookIdFromChapterPath(chapterPath: string) {
  const normalized = chapterPath.replace(/\\/g, "/")
  const match = normalized.match(/^books\/(.+)\/chapters\/[^/]+\.md$/)

  return match?.[1] || ""
}

function isRenderableAssetPath(value: string) {
  return value.startsWith("raw/assets/") || /^books\/(?:[a-z0-9-]+\/)*[a-z0-9-]+\/assets\//.test(value)
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

  const renderedPage = root.ownerDocument.querySelector<HTMLElement>(".bookPages > .bookPage")
  const renderedPageRect = renderedPage?.getBoundingClientRect()
  if (renderedPageRect && renderedPageRect.width > 0 && renderedPageRect.height > 0) {
    measurePage.style.width = `${Math.round(renderedPageRect.width)}px`
    measurePage.style.height = `${Math.round(renderedPageRect.height)}px`
  } else {
    measurePage.style.removeProperty("width")
    measurePage.style.removeProperty("height")
  }

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
    if (chapter.sectionType === "front_matter") {
      for (const page of paginateBlocks(chapter)) {
        pages.push({ ...page, pageNumber: pageNumber++ })
      }

      return
    }

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
    const blockBounds = blockElements.map(measureBlockBounds)
    const blockHeights = chapter.blocks.map((block, index) => {
      const current = blockBounds[index]
      const next = blockBounds[index + 1]
      const measuredHeight = current
        ? Math.max(0, (next?.top ?? current.bottom) - current.top)
        : 0

      return Math.ceil(measuredHeight || estimateBlockCost(block)) + measuredLayoutSafetyCost(block)
    })
    const chapterPages = paginateBlocksByHeight(chapter, blockHeights, pageBudget, firstHeaderHeight, runningHeaderHeight)

    for (const page of chapterPages) {
      pages.push({ ...page, pageNumber: pageNumber++ })
    }
  })

  return pages
}

function refineRenderedPageOverflows(pages: PreviewPage[], root: HTMLDivElement | null): PreviewPage[] {
  if (!root) return pages

  const pageElements = Array.from(root.querySelectorAll<HTMLElement>(".bookPage"))
  const nextPages = pages.map((page) => ({
    ...page,
    blocks: [...page.blocks]
  }))

  for (let index = 0; index < Math.min(pageElements.length, nextPages.length); index += 1) {
    const pageElement = pageElements[index]
    const previewBlocks = pageElement.querySelector<HTMLElement>(".previewBlocks")
    const footer = pageElement.querySelector<HTMLElement>(".pageFooter")
    const blockElements = Array.from(previewBlocks?.children || []) as HTMLElement[]

    if (!footer || blockElements.length === 0) continue

    const safeBottom = footer.getBoundingClientRect().top - PAGE_RENDER_GUARD_SPACE
    const firstOverflowIndex = blockElements.findIndex(
      (blockElement) => blockElement.getBoundingClientRect().bottom > safeBottom
    )

    if (firstOverflowIndex <= 0) continue

    const movedBlocks = nextPages[index].blocks.splice(firstOverflowIndex)

    if (movedBlocks.length === 0) continue

    const targetIndex = index + 1

    if (nextPages[targetIndex]?.chapter.path === nextPages[index].chapter.path) {
      nextPages[targetIndex].blocks.unshift(...movedBlocks)
    } else {
      nextPages.splice(targetIndex, 0, {
        chapter: nextPages[index].chapter,
        blocks: movedBlocks,
        pageNumber: 0,
        chapterPageNumber: 0,
        isFirstPage: false
      })
    }

    return renumberPreviewPages(nextPages)
  }

  return pages
}

function renumberPreviewPages(pages: PreviewPage[]): PreviewPage[] {
  const chapterPageCounts = new Map<string, number>()

  return pages.map((page, index) => {
    const chapterPageNumber = (chapterPageCounts.get(page.chapter.path) || 0) + 1
    chapterPageCounts.set(page.chapter.path, chapterPageNumber)

    return {
      ...page,
      pageNumber: index + 1,
      chapterPageNumber,
      isFirstPage: chapterPageNumber === 1
    }
  })
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
  if (chapter.sectionType === "front_matter" && isSinglePageFrontMatter(chapter.frontMatterLayout)) {
    return [{
      chapter,
      blocks: chapter.blocks,
      chapterPageNumber: 1,
      isFirstPage: true
    }]
  }

  const pages: Array<Omit<PreviewPage, "pageNumber">> = []
  let blocks: MarkdownBlock[] = []
  let usedBlockCosts: number[] = []
  let chapterPageNumber = 1
  let used = chapter.sectionType === "front_matter" ? FRONT_MATTER_FIRST_PAGE_COST : FIRST_PAGE_HEADER_COST

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
    used = chapter.sectionType === "front_matter" ? FRONT_MATTER_RUNNING_PAGE_COST : RUNNING_HEADER_COST
  }

  for (let index = 0; index < chapter.blocks.length; index += 1) {
    const block = chapter.blocks[index]
    const nextBlock = chapter.blocks[index + 1]
    const cost = estimateBlockCost(block) + layoutSafetyCost(block)
    const keepWithNextCost = shouldKeepWithNext(block, nextBlock)
      ? estimateBlockCost(nextBlock) + layoutSafetyCost(nextBlock)
      : 0
    const budget = chapter.sectionType === "front_matter" ? FRONT_MATTER_PAGE_BUDGET : MAIN_PAGE_FALLBACK_BUDGET

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

function isSinglePageFrontMatter(layout: string) {
  return layout === "digital-services" || layout === "title-page" || layout === "module-opening"
}

function shouldKeepWithNext(block: MarkdownBlock, nextBlock?: MarkdownBlock) {
  if (!nextBlock) return false

  if (block.type === "index-part") return nextBlock.type === "index-chapter"
  if (block.type === "index-chapter") return nextBlock.type === "index-row"

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

    if (level <= 2) return 42
    if (level === 3) return 32

    return 26
  }

  if (block.type === "paragraph") {
    const words = wordCount(block.text || "")
    return Math.ceil(words / 17) * 18 + 5
  }

  if (block.type === "list") {
    return (block.items || []).reduce((total, item) => total + Math.ceil(wordCount(item) / 16) * 17 + 4, 12)
  }

  if (block.type === "index-entry") {
    const items = block.items || []
    return 36 + Math.ceil(wordCount(block.text || "") / 7) * 9 + Math.ceil(items.length / 2) * 18
  }

  if (block.type === "index-part") {
    return 28
  }

  if (block.type === "index-chapter") {
    return 17 + Math.max(0, Math.ceil(wordCount(block.text || "") / 10) - 1) * 9
  }

  if (block.type === "index-row") {
    return 11 + Math.max(0, Math.ceil(wordCount(block.text || "") / 12) - 1) * 8
  }

  if (block.type === "table") {
    const headerCost = block.continued ? 0 : 24

    return headerCost + (block.rows?.length || 0) * 22 + 8
  }

  if (block.type === "image") {
    return 315
  }

  if (block.type === "callout") {
    return Math.ceil(wordCount(`${block.title || ""} ${block.text || ""}`) / 16) * 18 + 28
  }

  if (block.type === "code") {
    return (block.text || "").split("\n").length * 18 + 24
  }

  return 36
}

function layoutSafetyCost(block?: MarkdownBlock) {
  if (!block) return 0

  if (
    block.type === "index-entry" ||
    block.type === "index-part" ||
    block.type === "index-chapter" ||
    block.type === "index-row"
  ) return 0
  if (block.type === "image") return 64
  if (block.type === "table") return 56
  if (block.type === "paragraph") return 12
  if (block.type === "list") return 16
  if (block.type === "callout" || block.type === "code") return 18

  return 8
}

function measuredLayoutSafetyCost(block?: MarkdownBlock) {
  if (!block) return 0

  if (block.type === "image") return 4
  if (block.type === "table") return 2
  if (block.type === "list") return 1
  if (block.type === "callout" || block.type === "code") return 2
  if (block.type === "paragraph") return 0

  return 1
}

function measureBlockBounds(element?: HTMLElement | null) {
  if (!element) return null

  const children = Array.from(element.children) as HTMLElement[]
  const visibleRects = children
    .map((child) => child.getBoundingClientRect())
    .filter((rect) => rect.width > 0 && rect.height > 0)

  if (visibleRects.length === 0) return null

  return {
    top: Math.min(...visibleRects.map((rect) => rect.top)),
    bottom: Math.max(...visibleRects.map((rect) => rect.bottom))
  }
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
