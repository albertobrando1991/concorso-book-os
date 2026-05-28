"use client"

import { useEffect, useMemo, useState } from "react"
import { BookOpenCheck, Loader2, PenLine } from "lucide-react"
import type { ChapterOption, ManualWriterMode } from "@/src/server/agents/manual-writer-agent"
import type { WriterProvider } from "@/src/server/config"

interface ManualWriterPanelProps {
  initialChapters: ChapterOption[]
  writerProvider: WriterProvider
  writerModel: string
  writerReasoningEffort: string
}

interface WriterResult {
  chapterPath: string
  changedFiles: string[]
  knowledgeUsed: string[]
  memoryUsed?: string[]
  draft: string
  writerProvider: WriterProvider
  warnings: string[]
}

const modeOptions: Array<{ value: ManualWriterMode; label: string }> = [
  { value: "integrate", label: "Integra nel capitolo" },
  { value: "format", label: "Sistema formattazione" },
  { value: "improve", label: "Migliora testo" },
  { value: "expand", label: "Espandi sezione" },
  { value: "draft", label: "Solo bozza" }
]

const providerOptions: Array<{ value: WriterProvider; label: string }> = [
  { value: "codex", label: "Codex / GPT" },
  { value: "claude", label: "Claude" },
  { value: "kimi", label: "Kimi" },
  { value: "openai", label: "OpenAI API" },
  { value: "hermes", label: "Hermes" },
  { value: "local", label: "Locale" }
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
  const [selectedProvider, setSelectedProvider] = useState<WriterProvider>(writerProvider)
  const [instruction, setInstruction] = useState(
    "Scrivi il capitolo effettivo come testo da manuale Metodo BANDO, non un riepilogo tecnico. Usa prima il cervello wiki: struttura madre, nota capitolo, source notes, topic pages, entity pages e design system; aggiungi caso guidato, domanda-trappola, errori frequenti, mini-esercizio e note di ricerca web ufficiale se servono aggiornamenti."
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
          mode,
          provider: selectedProvider
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
        <div className={`writerLlmStatus ${selectedProvider === "local" ? "disabled" : "enabled"}`}>
          <BookOpenCheck size={18} aria-hidden />
          <span>{providerStatusLabel(selectedProvider)}</span>
        </div>
      </header>

      <div className="writerGrid">
        <label>
          Capitolo
          <select value={chapterPath} onChange={(event) => setChapterPath(event.target.value)}>
            {chapters.map((chapter) => (
              <option value={chapter.path} key={chapter.path}>
                {chapter.outlineSection ? `${chapter.outlineSection} - ` : ""}
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
      </div>

      {selectedChapter ? (
        <p className="writerMeta">
          File: <code>{selectedChapter.path}</code> | Stato: {selectedChapter.status} | Modello:{" "}
          <code>{providerModelLabel(selectedProvider, writerModel)}</code> | Reasoning:{" "}
          <code>{providerReasoningLabel(selectedProvider, writerReasoningEffort)}</code>
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
                {result.warnings.map((item, index) => (
                  <li key={`${item}-${index}`}>{item}</li>
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
              {result.knowledgeUsed.map((item, index) => (
                <li key={`${item}-${index}`}>{item}</li>
              ))}
            </ul>
          </details>
          {result.memoryUsed && result.memoryUsed.length > 0 ? (
            <details>
              <summary>Memoria locale richiamata</summary>
              <ul>
                {result.memoryUsed.map((item, index) => (
                  <li key={`${item}-${index}`}>{item}</li>
                ))}
              </ul>
            </details>
          ) : null}
        </div>
      ) : null}
    </section>
  )
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
