import {
  AlertTriangle,
  BookOpen,
  Bot,
  Database,
  ExternalLink,
  FileSearch,
  GitBranch,
  Layers3,
  Library,
  ListChecks,
  ScrollText,
  Settings,
  ShieldCheck
} from "lucide-react"
import { getDashboardData } from "@/src/server/dashboard/data"
import { ManualWriterPanel } from "./components/manual-writer-panel"
import { KnowledgeGraphPanel } from "./components/knowledge-graph-panel"
import { BookStudioPanel } from "./components/book-studio-panel"
import { ManualWriterAgent } from "@/src/server/agents/manual-writer-agent"
import { DEFAULT_BOOK_ID, getWikiRoot, getWriterConfig } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import { parseFrontmatter } from "@/src/server/wiki/frontmatter"
import { buildKnowledgeGraph } from "@/src/server/wiki/graph"
import type { DashboardSource } from "@/src/server/wiki/types"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { BookSelector } from "./components/book-selector"
import { BookCreatorPanel } from "./components/book-creator-panel"
import { EditorialReviewerPanel } from "./components/editorial-reviewer-panel"

export const dynamic = "force-dynamic"

type HomeProps = {
  searchParams?: Promise<{
    source?: string | string[]
    bookId?: string | string[]
    chapterPath?: string | string[]
  }>
}

const navigation = [
  ["Overview", Database],
  ["Sources", FileSearch],
  ["Topics", Layers3],
  ["Books", BookOpen],
  ["Studio", BookOpen],
  ["Writer", PenIcon],
  ["Graph", GitBranch],
  ["Agents", Bot],
  ["Quality", ShieldCheck],
  ["Logs", ScrollText],
  ["Settings", Settings]
] as const

export default async function Home({ searchParams }: HomeProps) {
  const data = await getDashboardData()
  const store = new FileWikiStore(getWikiRoot())
  const params = searchParams ? await searchParams : {}
  const requestedBookId = firstParam(params.bookId) || DEFAULT_BOOK_ID
  const requestedChapterPath = firstParam(params.chapterPath)
  const chapters = await new ManualWriterAgent(store).listChapters(requestedBookId)
  const graph = await buildKnowledgeGraph(store)
  const bookStudio = await buildBookStudioData(store, requestedBookId)
  const writerConfig = getWriterConfig()
  const allSources = [...data.sources].sort(compareSources)
  const requestedSourcePath = firstParam(params.source)
  const selectedSource = allSources.find((source) => source.path === requestedSourcePath) || allSources[0]
  const sourceReader = selectedSource ? await loadSourceReader(store, selectedSource) : null
  const topTopics = data.topics.slice(0, 6)
  const topIssues = data.qualityIssues.slice(0, 6)

  return (
    <main className="shell">
      <aside className="sidebar" aria-label="Navigazione principale">
        <div className="brand">
          <Library size={24} aria-hidden />
          <div>
            <strong>ConcorsoBook OS</strong>
            <span>LLM Wiki Control Center</span>
          </div>
        </div>
        <nav className="navList">
          {navigation.map(([label, Icon]) => (
            <a href={`#${label.toLowerCase()}`} key={label}>
              <Icon size={18} aria-hidden />
              {label}
            </a>
          ))}
        </nav>
        <div className="vaultStatus">
          <GitBranch size={18} aria-hidden />
          <div>
            <span>Vault</span>
            <strong>wiki/ connected</strong>
          </div>
        </div>
      </aside>

      <section className="workspace">
        <header className="topbar" id="overview">
          <div>
            <p className="eyebrow">Dominio iniziale: concorsi pubblici italiani</p>
            <h1>Knowledge base agentica per libri incrementali</h1>
          </div>
          <div className="topActions" style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
            <span>Active book</span>
            <BookSelector books={data.books} currentBookId={requestedBookId} />
          </div>
        </header>

        <section className="metrics" aria-label="Metriche operative">
          <Metric label="Fonti totali" value={data.metrics.totalSources} accent="blue" />
          <Metric label="Fonti non processate" value={data.metrics.unprocessedSources} accent="amber" />
          <Metric label="Topic recenti" value={data.metrics.recentTopics} accent="green" />
          <Metric label="Capitoli in bozza" value={data.metrics.draftChapters} accent="blue" />
          <Metric label="Capitoli consolidati" value={data.metrics.consolidatedChapters} accent="green" />
          <Metric label="Conflitti aperti" value={data.metrics.openConflicts} accent="red" />
          <Metric label="Memorie locali" value={data.metrics.memoryAtoms} accent="amber" />
        </section>

        <BookStudioPanel
          initialData={bookStudio}
          initialChapterPath={requestedChapterPath}
          writerProvider={writerConfig.provider}
          writerModel={writerConfig.writerModel}
          writerReasoningEffort={writerConfig.writerReasoningEffort}
        />

        <EditorialReviewerPanel
          bookId={requestedBookId}
          chapters={bookStudio.chapters.map((ch) => ({ path: ch.path, title: ch.title }))}
        />

        <BookCreatorPanel />

        <section className="grid two">
          <Panel title="Pipeline stato" icon={<ListChecks size={19} aria-hidden />}>
            <ol className="timeline">
              <li>
                <strong>Entrato</strong>
                <span>{data.sources.length} source notes tracciate nel vault.</span>
              </li>
              <li>
                <strong>Capito</strong>
                <span>{data.topics.length} topic pages e knowledge link disponibili.</span>
              </li>
              <li>
                <strong>Aggiornato</strong>
                <span>{data.books.length} libro demo con capitoli modulari.</span>
              </li>
              <li>
                <strong>Da fare</strong>
                <span>{data.qualityIssues.length} issue aperte da lint/review.</span>
              </li>
            </ol>
          </Panel>

          <Panel title="Agent queue" icon={<Bot size={19} aria-hidden />}>
            <div className="agentGrid">
              {["Ingest Agent", "Knowledge Maintainer", "Manual Writer Agent", "Book Writer", "Quiz Agent", "Lint Agent", "Review Agent"].map(
                (agent, index) => (
                  <div className="agentRow" key={agent}>
                    <span>{agent}</span>
                    <strong>{index < 3 ? "ready" : "idle"}</strong>
                  </div>
                )
              )}
            </div>
          </Panel>
        </section>

        <ManualWriterPanel
          initialChapters={chapters}
          activeBookId={requestedBookId}
          writerProvider={writerConfig.provider}
          writerModel={writerConfig.writerModel}
          writerReasoningEffort={writerConfig.writerReasoningEffort}
        />

        <KnowledgeGraphPanel graph={graph} />

        <section className="grid">
          <Panel title={`Sources (${allSources.length})`} icon={<FileSearch size={19} aria-hidden />} id="sources">
            <SourceLibrary sources={allSources} selectedPath={selectedSource?.path || ""} reader={sourceReader} />
          </Panel>
        </section>

        <section className="grid two">
          <Panel title="Topics" icon={<Layers3 size={19} aria-hidden />} id="topics">
            <div className="topicList">
              {topTopics.map((topic) => (
                <div className="topicRow" key={topic.path}>
                  <div>
                    <strong>{topic.title}</strong>
                    <span>{topic.sourceRefs.length} fonti | {topic.chapterRefs.length} capitoli</span>
                  </div>
                  <meter min="0" max="1" value={topic.confidence} aria-label={`Copertura ${topic.title}`} />
                </div>
              ))}
            </div>
          </Panel>

          <Panel title="Books" icon={<BookOpen size={19} aria-hidden />} id="books">
            <div className="booksGridList" style={{ display: "grid", gap: "10px" }}>
              {data.books.map((book) => {
                const bookId = book.path.replace("books/", "").replace("/index.md", "")
                const active = bookId === requestedBookId
                return (
                  <a
                    href={`/?bookId=${encodeURIComponent(bookId)}`}
                    className={`bookBlock${active ? " active" : ""}`}
                    key={book.path}
                    style={{
                      display: "block",
                      border: active ? "1px solid #9ebbe0" : "1px solid var(--line)",
                      background: active ? "#edf5ff" : "var(--panel)",
                      borderRadius: "6px",
                      padding: "12px",
                      transition: "all 0.15s ease"
                    }}
                  >
                    <strong style={{ display: "block" }}>{book.title}</strong>
                    <span style={{ display: "block", fontSize: "13px", color: "var(--muted)", marginTop: "4px" }}>
                      {book.chapters} capitoli | {book.status}
                    </span>
                    <small style={{ display: "block", fontSize: "11px", color: book.reviewRequired ? "var(--red)" : "var(--green)", marginTop: "4px", fontWeight: 600 }}>
                      {book.reviewRequired ? "review_required" : "stable"}
                    </small>
                  </a>
                )
              })}
            </div>
          </Panel>
        </section>

        <section className="grid two">
          <Panel title="Quality" icon={<AlertTriangle size={19} aria-hidden />} id="quality">
            <div className="issueList">
              {topIssues.length === 0 ? (
                <p className="muted">Nessuna issue aperta.</p>
              ) : (
                topIssues.map((issue) => (
                  <div className={`issue ${issue.severity}`} key={issue.id}>
                    <strong>{issue.title}</strong>
                    <span>{issue.recommendation}</span>
                  </div>
                ))
              )}
            </div>
          </Panel>

          <Panel title="Logs e Artifacts" icon={<ScrollText size={19} aria-hidden />} id="logs">
            <div className="logList">
              {data.logEntries.slice(0, 6).map((entry, index) => (
                <code key={`${entry}-${index}`}>{entry}</code>
              ))}
            </div>
            <div className="artifactList">
              {data.artifacts.slice(0, 6).map((artifact) => (
                <span key={artifact.path}>{artifact.title}</span>
              ))}
            </div>
          </Panel>
        </section>
      </section>
    </main>
  )
}

function PenIcon({ size }: { size?: number }) {
  return <Bot size={size} aria-hidden />
}

function Metric({ label, value, accent }: { label: string; value: number; accent: string }) {
  return (
    <div className={`metric ${accent}`}>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
}

interface SourceReaderData {
  source: DashboardSource
  body: string
  rawMarkdown?: {
    path: string
    body: string
  }
  metadata: {
    sourceUrl: string
    createdAt: string
    updatedAt: string
  }
}

async function loadSourceReader(store: FileWikiStore, source: DashboardSource): Promise<SourceReaderData> {
  const parsed = parseFrontmatter(await store.readText(source.path))
  const rawMarkdownPath = findRawMarkdownPath(parsed.body)
  const rawMarkdown = rawMarkdownPath && (await store.exists(rawMarkdownPath))
    ? {
        path: rawMarkdownPath,
        body: parseFrontmatter(await store.readText(rawMarkdownPath)).body.trim()
      }
    : undefined

  return {
    source,
    body: parsed.body.trim(),
    rawMarkdown,
    metadata: {
      sourceUrl: String(parsed.data.source_url || ""),
      createdAt: String(parsed.data.created_at || ""),
      updatedAt: String(parsed.data.updated_at || source.updatedAt || "")
    }
  }
}

function SourceLibrary({
  sources,
  selectedPath,
  reader
}: {
  sources: DashboardSource[]
  selectedPath: string
  reader: SourceReaderData | null
}) {
  if (sources.length === 0) {
    return <p className="muted">Nessuna fonte presente nel vault.</p>
  }

  return (
    <div className="sourceLibrary">
      <nav className="sourceList" aria-label="Fonti disponibili">
        {sources.map((source) => {
          const active = source.path === selectedPath

          return (
            <a
              className={`sourceListItem${active ? " active" : ""}`}
              href={`/?source=${encodeURIComponent(source.path)}#sources`}
              key={source.path}
            >
              <strong>{source.title}</strong>
              <span>{source.sourceType} | {source.status} | {source.authorityLevel}</span>
              <code>{source.path}</code>
            </a>
          )
        })}
      </nav>

      {reader ? (
        <article className="sourceReader">
          <header>
            <div>
              <span className="panelKicker">Fonte selezionata</span>
              <h3>{reader.source.title}</h3>
            </div>
            {reader.metadata.sourceUrl ? (
              <a className="sourceExternal" href={reader.metadata.sourceUrl} target="_blank" rel="noreferrer">
                URL ufficiale
                <ExternalLink size={14} aria-hidden />
              </a>
            ) : null}
          </header>

          <div className="sourceMetaGrid" aria-label="Metadati fonte">
            <span>Tipo <strong>{reader.source.sourceType}</strong></span>
            <span>Stato <strong>{reader.source.status}</strong></span>
            <span>Affidabilita <strong>{reader.source.authorityLevel}</strong></span>
            <span>Aggiornata <strong>{formatDateTime(reader.metadata.updatedAt)}</strong></span>
          </div>

          <details className="sourceDocument" open>
            <summary>Source note consolidata</summary>
            <MarkdownReader content={reader.body} />
          </details>

          {reader.rawMarkdown ? (
            <details className="sourceDocument" open>
              <summary>Documento convertito in Markdown</summary>
              <code className="sourcePath">{reader.rawMarkdown.path}</code>
              <MarkdownReader content={reader.rawMarkdown.body} />
            </details>
          ) : null}
        </article>
      ) : null}
    </div>
  )
}

function MarkdownReader({ content }: { content: string }) {
  const blocks = content
    .replace(/\r\n/g, "\n")
    .split(/\n{2,}/)
    .map((block) => block.trim())
    .filter(Boolean)

  return (
    <div className="markdownReader">
      {blocks.map((block, index) => renderMarkdownBlock(block, index))}
    </div>
  )
}

function renderMarkdownBlock(block: string, index: number) {
  if (block.startsWith("```")) {
    return <pre key={index}>{block.replace(/^```[a-z]*\n?/i, "").replace(/\n?```$/, "")}</pre>
  }

  const headingMatch = block.match(/^(#{1,4})\s+(.+)$/)
  if (headingMatch) {
    const level = Math.min(headingMatch[1].length + 2, 6)
    if (level === 3) return <h3 key={index}>{headingMatch[2]}</h3>
    if (level === 4) return <h4 key={index}>{headingMatch[2]}</h4>
    if (level === 5) return <h5 key={index}>{headingMatch[2]}</h5>
    return <h6 key={index}>{headingMatch[2]}</h6>
  }

  const lines = block.split("\n")
  if (lines.every((line) => line.startsWith("- "))) {
    return (
      <ul key={index}>
        {lines.map((line) => (
          <li key={line}>{line.slice(2)}</li>
        ))}
      </ul>
    )
  }

  if (lines.some((line) => line.includes("|")) && lines.length > 1) {
    return <pre key={index}>{block}</pre>
  }

  return <p key={index}>{block}</p>
}

function findRawMarkdownPath(body: string) {
  const match = body.match(/`wiki\/(raw\/[^`]+\.md)`/)
  return match?.[1] || ""
}

function firstParam(value: string | string[] | undefined) {
  return Array.isArray(value) ? value[0] : value
}

function formatDateTime(value: string) {
  const time = Date.parse(value)

  if (Number.isNaN(time)) return "-"

  return new Intl.DateTimeFormat("it-IT", {
    dateStyle: "short",
    timeStyle: "short"
  }).format(new Date(time))
}

function compareSources(a: { title: string; updatedAt: string }, b: { title: string; updatedAt: string }) {
  const bTime = toSortableTime(b.updatedAt)
  const aTime = toSortableTime(a.updatedAt)

  if (bTime !== aTime) return bTime - aTime

  return a.title.localeCompare(b.title, "it")
}

function toSortableTime(value: string) {
  const time = Date.parse(value)
  return Number.isNaN(time) ? 0 : time
}

function Panel({
  title,
  icon,
  children,
  id
}: {
  title: string
  icon: React.ReactNode
  children: React.ReactNode
  id?: string
}) {
  return (
    <section className="panel" id={id}>
      <header>
        {icon}
        <h2>{title}</h2>
      </header>
      {children}
    </section>
  )
}
