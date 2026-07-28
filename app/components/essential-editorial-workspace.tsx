"use client"

import { useCallback, useEffect, useState } from "react"
import { Loader2, RefreshCw } from "lucide-react"
import type { ChapterOption } from "@/src/server/agents/manual-writer-agent"
import type { BookStudioData } from "@/src/server/book/book-preview"
import type { WriterProvider } from "@/src/server/config"
import { BookStudioPanel } from "./book-studio-panel"
import { EditorialReviewerPanel } from "./editorial-reviewer-panel"
import { ManualWriterPanel } from "./manual-writer-panel"

interface EssentialEditorialWorkspaceProps {
  bookId: string
  initialChapterPath?: string
  writerProvider: WriterProvider
  writerModel: string
  writerReasoningEffort: string
}

export function EssentialEditorialWorkspace({
  bookId,
  initialChapterPath,
  writerProvider,
  writerModel,
  writerReasoningEffort
}: EssentialEditorialWorkspaceProps) {
  const [data, setData] = useState<BookStudioData | null>(null)
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(true)

  const loadWorkspace = useCallback(async (signal?: AbortSignal) => {
    setIsLoading(true)
    setError("")

    try {
      const response = await fetch(`/api/book-studio?bookId=${encodeURIComponent(bookId)}`, {
        signal,
        cache: "no-store"
      })
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Impossibile caricare lo spazio editoriale")
      }

      setData(payload)
    } catch (currentError) {
      if (currentError instanceof Error && currentError.name === "AbortError") return
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      if (!signal?.aborted) setIsLoading(false)
    }
  }, [bookId])

  useEffect(() => {
    const controller = new AbortController()
    setData(null)
    void loadWorkspace(controller.signal)

    return () => controller.abort()
  }, [loadWorkspace])

  if (isLoading && !data) {
    return (
      <section className="essentialWorkspaceState" id="studio" aria-live="polite">
        <Loader2 className="spin" size={22} aria-hidden />
        <div>
          <strong>Apro lo spazio editoriale</strong>
          <span>La dashboard è già utilizzabile; capitoli e anteprime vengono caricati in background.</span>
        </div>
      </section>
    )
  }

  if (error && !data) {
    return (
      <section className="essentialWorkspaceState error" id="studio" role="alert">
        <div>
          <strong>Spazio editoriale non disponibile</strong>
          <span>{error}</span>
        </div>
        <button type="button" onClick={() => void loadWorkspace()}>
          <RefreshCw size={16} aria-hidden />
          Riprova
        </button>
      </section>
    )
  }

  if (!data) return null

  const chapters: ChapterOption[] = data.chapters
    .filter((chapter) => !chapter.isGenerated)
    .map((chapter) => ({
      path: chapter.path,
      title: chapter.title,
      bookId,
      outlineSection: chapter.outlineSection,
      status: chapter.status,
      reviewRequired: chapter.reviewRequired
    }))

  return (
    <>
      <BookStudioPanel
        initialData={data}
        initialChapterPath={initialChapterPath}
        writerProvider={writerProvider}
        writerModel={writerModel}
        writerReasoningEffort={writerReasoningEffort}
      />

      <ManualWriterPanel
        initialChapters={chapters}
        activeBookId={bookId}
        writerProvider={writerProvider}
        writerModel={writerModel}
        writerReasoningEffort={writerReasoningEffort}
      />

      <EditorialReviewerPanel
        bookId={bookId}
        chapters={data.chapters.map((chapter) => ({ path: chapter.path, title: chapter.title }))}
      />
    </>
  )
}
