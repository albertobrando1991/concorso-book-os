"use client"

import { useEffect, useMemo, useState } from "react"
import { BookOpenCheck, Loader2, PenLine } from "lucide-react"
import type { ChapterOption, ManualWriterMode } from "@/src/server/agents/manual-writer-agent"

interface ManualWriterPanelProps {
  initialChapters: ChapterOption[]
  writerProvider: "codex" | "openai" | "local"
  writerModel: string
  writerReasoningEffort: string
}

interface WriterResult {
  chapterPath: string
  changedFiles: string[]
  knowledgeUsed: string[]
  draft: string
  writerProvider: "codex" | "openai" | "local"
  warnings: string[]
}

const modeOptions: Array<{ value: ManualWriterMode; label: string }> = [
  { value: "integrate", label: "Integra nel capitolo" },
  { value: "format", label: "Sistema formattazione" },
  { value: "improve", label: "Migliora testo" },
  { value: "expand", label: "Espandi sezione" },
  { value: "draft", label: "Solo bozza" }
]

export function ManualWriterPanel({
  initialChapters,
  writerProvider,
  writerModel,
  writerReasoningEffort
}: ManualWriterPanelProps) {
  const [chapters, setChapters] = useState(initialChapters)
  const [chapterPath, setChapterPath] = useState(initialChapters[0]?.path || "")
  const [mode, setMode] = useState<ManualWriterMode>("integrate")
  const [instruction, setInstruction] = useState(
    "Riscrivi questo capitolo come manuale operativo Metodo BANDO, integrando la conoscenza nuova e aggiungendo caso guidato, domanda-trappola, errori frequenti e mini-esercizio."
  )
  const [isLoading, setIsLoading] = useState(false)
  const [result, setResult] = useState<WriterResult | null>(null)
  const [error, setError] = useState("")

  useEffect(() => {
    if (initialChapters.length > 0) return

    fetch("/api/manual-writer/chapters")
      .then((response) => response.json())
      .then((data: { chapters: ChapterOption[] }) => {
        setChapters(data.chapters)
        setChapterPath(data.chapters[0]?.path || "")
      })
      .catch(() => setError("Impossibile caricare i capitoli."))
  }, [initialChapters.length])

  const selectedChapter = useMemo(
    () => chapters.find((chapter) => chapter.path === chapterPath),
    [chapters, chapterPath]
  )

  async function runWriter() {
    setIsLoading(true)
    setError("")
    setResult(null)

    try {
      const response = await fetch("/api/manual-writer/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          chapterPath,
          instruction,
          mode
        })
      })

      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Manual Writer Agent failed")
      }

      setResult(payload)
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore sconosciuto")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <section className="writerPanel" id="writer">
      <header>
        <div>
          <span className="panelKicker">Manual Writer Agent</span>
          <h2>Scrittura automatica capitoli</h2>
        </div>
        <div className={`writerLlmStatus ${writerProvider === "local" ? "disabled" : "enabled"}`}>
          <BookOpenCheck size={18} aria-hidden />
          <span>{writerProvider === "codex" ? "Codex attivo" : writerProvider === "openai" ? "OpenAI attivo" : "Writer locale"}</span>
        </div>
      </header>

      <div className="writerGrid">
        <label>
          Capitolo
          <select value={chapterPath} onChange={(event) => setChapterPath(event.target.value)}>
            {chapters.map((chapter) => (
              <option value={chapter.path} key={chapter.path}>
                {chapter.title}
              </option>
            ))}
          </select>
        </label>

        <label>
          Modalità
          <select value={mode} onChange={(event) => setMode(event.target.value as ManualWriterMode)}>
            {modeOptions.map((option) => (
              <option value={option.value} key={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </label>
      </div>

      {selectedChapter ? (
        <p className="writerMeta">
          File: <code>{selectedChapter.path}</code> | Stato: {selectedChapter.status} | Modello:{" "}
          <code>{writerModel}</code> | Reasoning: <code>{writerReasoningEffort}</code>
        </p>
      ) : null}

      <label className="writerInstruction">
        Richiesta al writer
        <textarea value={instruction} onChange={(event) => setInstruction(event.target.value)} rows={5} />
      </label>

      <button className="writerButton" onClick={runWriter} disabled={isLoading || !chapterPath}>
        {isLoading ? <Loader2 size={17} className="spin" aria-hidden /> : <PenLine size={17} aria-hidden />}
        {isLoading ? "Scrittura in corso" : "Scrivi e integra capitolo"}
      </button>

      {error ? <div className="writerError">{error}</div> : null}

      {result ? (
        <div className="writerResult">
          <strong>Capitolo aggiornato</strong>
          <span>Provider: {result.writerProvider}</span>
          <span>{result.chapterPath}</span>
          {result.warnings.length > 0 ? (
            <details>
              <summary>Avvisi</summary>
              <ul>
                {result.warnings.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </details>
          ) : null}
          <details>
            <summary>Anteprima testo generato</summary>
            <pre>{result.draft}</pre>
          </details>
          <details>
            <summary>Knowledge usata</summary>
            <ul>
              {result.knowledgeUsed.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </details>
        </div>
      ) : null}
    </section>
  )
}
