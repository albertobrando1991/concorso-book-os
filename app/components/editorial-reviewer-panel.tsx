"use client"

import { useState } from "react"
import {
  BookOpenCheck,
  CheckCircle2,
  ClipboardCheck,
  AlertTriangle,
  XCircle,
  Loader2,
  ShieldCheck
} from "lucide-react"
import type { WriterProvider } from "@/src/server/config"
import type {
  ReviewScope,
  PublishabilityJudgment,
  ReviewErrorRow,
  ChapterObservation,
  EditorialReviewResult
} from "@/src/server/agents/editorial-reviewer-agent"

interface EditorialReviewerPanelProps {
  bookId: string
  chapters: Array<{ path: string; title: string }>
}

const providerOptions: Array<{ value: WriterProvider; label: string }> = [
  { value: "codex", label: "Codex / GPT" },
  { value: "claude", label: "Claude" },
  { value: "kimi", label: "Kimi" },
  { value: "openai", label: "OpenAI API" },
  { value: "hermes", label: "Hermes" },
  { value: "local", label: "Locale" }
]

const scopeOptions: Array<{ value: ReviewScope; label: string }> = [
  { value: "full", label: "Libro intero" },
  { value: "chapter", label: "Singolo capitolo" },
  { value: "aspect", label: "Aspetto specifico" }
]

export function EditorialReviewerPanel({ bookId, chapters }: EditorialReviewerPanelProps) {
  const [provider, setProvider] = useState<WriterProvider>("codex")
  const [scope, setScope] = useState<ReviewScope>("full")
  const [selectedChapter, setSelectedChapter] = useState(chapters[0]?.path || "")
  const [aspect, setAspect] = useState("")
  const [isRunning, setIsRunning] = useState(false)
  const [progressMessage, setProgressMessage] = useState("")
  const [error, setError] = useState("")
  const [result, setResult] = useState<EditorialReviewResult | null>(null)

  async function runReview() {
    setIsRunning(true)
    setError("")
    setResult(null)

    const steps = [
      "Caricamento capitoli dal vault e costruzione Bibbia del Libro...",
      "Lettura checklist a 30 punti e template di report...",
      "Analisi strutturale: indice, progressione, gerarchia...",
      "Controllo contenutistico: definizioni, norme, coerenza tra capitoli...",
      "Controllo linguistico: grammatica, sintassi, stile, refusi...",
      "Costruzione tabella errori ordinata per gravita...",
      "Valutazione finale di pubblicabilita in corso..."
    ]
    let stepIndex = 0
    setProgressMessage(steps[0])
    const timer = window.setInterval(() => {
      stepIndex = Math.min(stepIndex + 1, steps.length - 1)
      setProgressMessage(steps[stepIndex])
    }, 3200)

    try {
      const body: Record<string, string> = { bookId, scope, provider }
      if (scope === "chapter") body.chapterPath = selectedChapter
      if (scope === "aspect") body.aspect = aspect

      const response = await fetch("/api/editorial-reviewer/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      })
      const payload = await response.json()

      if (!response.ok) {
        throw new Error(payload.error || "Revisione editoriale fallita")
      }

      setResult(payload as EditorialReviewResult)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Errore sconosciuto")
    } finally {
      window.clearInterval(timer)
      setIsRunning(false)
      setProgressMessage("")
    }
  }

  return (
    <section className="editorialReviewerPanel" id="editorial-review">
      <header>
        <div>
          <span className="panelKicker">Revisione Editoriale</span>
          <h2>Revisore Editoriale Totale</h2>
        </div>
        <div className="studioHeaderActions">
          <span className={`writerLlmStatus ${provider === "local" ? "disabled" : "enabled"}`}>
            <ShieldCheck size={18} aria-hidden />
            <span>{providerLabel(provider)}</span>
          </span>
        </div>
      </header>

      <p className="reviewerDescription">
        Revisione editoriale professionale e completa prima della pubblicazione. Copre tutti i 30 punti: struttura, coerenza, terminologia, grammatica, contenuto, layout e giudizio di pubblicabilita.
      </p>

      <div className="reviewerControls">
        <label>
          Perimetro
          <select value={scope} onChange={(e) => setScope(e.target.value as ReviewScope)}>
            {scopeOptions.map((opt) => (
              <option value={opt.value} key={opt.value}>{opt.label}</option>
            ))}
          </select>
        </label>

        {scope === "chapter" ? (
          <label>
            Capitolo
            <select value={selectedChapter} onChange={(e) => setSelectedChapter(e.target.value)}>
              {chapters.map((ch) => (
                <option value={ch.path} key={ch.path}>{ch.title}</option>
              ))}
            </select>
          </label>
        ) : null}

        {scope === "aspect" ? (
          <label>
            Aspetto specifico
            <input
              type="text"
              value={aspect}
              onChange={(e) => setAspect(e.target.value)}
              placeholder="Es. coerenza terminologica, accuratezza normativa..."
            />
          </label>
        ) : null}

        <label>
          Modello AI
          <select value={provider} onChange={(e) => setProvider(e.target.value as WriterProvider)}>
            {providerOptions.map((opt) => (
              <option value={opt.value} key={opt.value}>{opt.label}</option>
            ))}
          </select>
        </label>

        <button
          className="reviewerRunButton"
          onClick={runReview}
          disabled={isRunning || (scope === "aspect" && !aspect.trim())}
        >
          {isRunning
            ? <Loader2 size={17} className="spin" aria-hidden />
            : <ClipboardCheck size={17} aria-hidden />
          }
          {isRunning ? "Revisione in corso..." : "Avvia revisione editoriale"}
        </button>
      </div>

      {isRunning ? (
        <div className="reviewerProgressBar" role="status" aria-live="polite">
          <Loader2 size={17} className="spin" aria-hidden />
          <span>{progressMessage}</span>
        </div>
      ) : null}

      {error ? <div className="reviewerError">{error}</div> : null}

      {result ? <ReviewResult result={result} /> : null}
    </section>
  )
}

// ── Result display ─────────────────────────────────────────────────────────────

function ReviewResult({ result }: { result: EditorialReviewResult }) {
  return (
    <div className="reviewerResultContainer">
      {/* Publishability judgment */}
      <div className={`publishabilityCard ${judgmentClass(result.publishabilityJudgment)}`}>
        <div className="publishabilityIcon">
          {judgmentIcon(result.publishabilityJudgment)}
        </div>
        <div className="publishabilityContent">
          <strong>{judgmentLabel(result.publishabilityJudgment)}</strong>
          <span>Provider: {result.provider} | Errori: {result.errorTable.length} | Scope: {result.scope}</span>
        </div>
      </div>

      {/* Editorial summary */}
      <div className="reviewSummaryBox">
        <h3>Sintesi editoriale</h3>
        <p>{result.editorialSummary}</p>
      </div>

      {/* Error table */}
      {result.errorTable.length > 0 ? (
        <div className="reviewErrorTableWrap">
          <h3>Tabella errori ({result.errorTable.length})</h3>
          <div className="reviewErrorTableScroll">
            <table className="reviewErrorTable">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Posizione</th>
                  <th>Categoria</th>
                  <th>Gravità</th>
                  <th>Descrizione</th>
                  <th>Correzione proposta</th>
                  <th>Stato</th>
                </tr>
              </thead>
              <tbody>
                {result.errorTable.map((row) => (
                  <tr className={`severity-${row.severity}`} key={row.id}>
                    <td><strong>{row.id}</strong></td>
                    <td>{row.position}</td>
                    <td>{row.category}</td>
                    <td><span className={`severityBadge ${row.severity}`}>{row.severity}</span></td>
                    <td>{row.description}</td>
                    <td>{row.proposedFix}</td>
                    <td>{row.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ) : null}

      {/* Chapter observations */}
      {result.chapterObservations.length > 0 ? (
        <details className="reviewSection" open>
          <summary><h3>Osservazioni per capitolo ({result.chapterObservations.length})</h3></summary>
          <div className="chapterObservationsList">
            {result.chapterObservations.map((obs, i) => (
              <div className="chapterObservation" key={`obs-${i}`}>
                <strong>{obs.chapter}</strong>
                <div className="observationGrid">
                  <div className="observationStrength">
                    <CheckCircle2 size={14} aria-hidden />
                    <span>{obs.strengths}</span>
                  </div>
                  <div className="observationIssue">
                    <AlertTriangle size={14} aria-hidden />
                    <span>{obs.issues}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </details>
      ) : null}

      {/* Priority order */}
      {result.priorityOrder.length > 0 ? (
        <details className="reviewSection">
          <summary><h3>Priorita degli interventi</h3></summary>
          <ol className="reviewPriorityList">
            {result.priorityOrder.map((item, i) => (
              <li key={`prio-${i}`}>{item}</li>
            ))}
          </ol>
        </details>
      ) : null}

      {/* Verification items */}
      {result.verificationItems.length > 0 ? (
        <details className="reviewSection">
          <summary><h3>Contenuto da verificare con fonti esterne</h3></summary>
          <ul className="reviewBulletList verification">
            {result.verificationItems.map((item, i) => (
              <li key={`ver-${i}`}>{item}</li>
            ))}
          </ul>
        </details>
      ) : null}

      {/* Optional suggestions */}
      {result.optionalSuggestions.length > 0 ? (
        <details className="reviewSection">
          <summary><h3>Suggerimenti facoltativi (non errori)</h3></summary>
          <ul className="reviewBulletList suggestions">
            {result.optionalSuggestions.map((item, i) => (
              <li key={`sug-${i}`}>{item}</li>
            ))}
          </ul>
        </details>
      ) : null}

      {/* Publishability reason */}
      {result.publishabilityReason ? (
        <details className="reviewSection">
          <summary><h3>Motivazione giudizio di pubblicabilita</h3></summary>
          <p className="reviewReasonText">{result.publishabilityReason}</p>
        </details>
      ) : null}

      {/* Limitations */}
      {result.limitations.length > 0 ? (
        <div className="reviewLimitations">
          <strong>Limiti di questa revisione:</strong>
          <ul>
            {result.limitations.map((item, i) => (
              <li key={`lim-${i}`}>{item}</li>
            ))}
          </ul>
        </div>
      ) : null}

      {/* Warnings */}
      {result.warnings.length > 0 ? (
        <div className="reviewerWarnings">
          {result.warnings.map((w, i) => (
            <span key={`warn-${i}`}>{w}</span>
          ))}
        </div>
      ) : null}

      {/* Raw report */}
      <details className="reviewSection">
        <summary><h3>Report completo (raw)</h3></summary>
        <pre className="reviewRawReport">{result.rawReport}</pre>
      </details>
    </div>
  )
}

// ── Helpers ────────────────────────────────────────────────────────────────────

function providerLabel(provider: WriterProvider) {
  const labels: Record<string, string> = {
    codex: "Codex / GPT attivo",
    claude: "Claude attivo",
    kimi: "Kimi attivo",
    openai: "OpenAI API attiva",
    hermes: "Hermes attivo",
    local: "Writer locale"
  }
  return labels[provider] || provider
}

function judgmentClass(judgment: PublishabilityJudgment) {
  if (judgment === "publishable_minor") return "judgment-minor"
  if (judgment === "not_publishable") return "judgment-not"
  return "judgment-medium"
}

function judgmentLabel(judgment: PublishabilityJudgment) {
  if (judgment === "publishable_minor") return "Pubblicabile con correzioni minori"
  if (judgment === "not_publishable") return "Non pubblicabile allo stato attuale"
  return "Pubblicabile dopo intervento medio"
}

function judgmentIcon(judgment: PublishabilityJudgment) {
  if (judgment === "publishable_minor") return <BookOpenCheck size={28} aria-hidden />
  if (judgment === "not_publishable") return <XCircle size={28} aria-hidden />
  return <AlertTriangle size={28} aria-hidden />
}
