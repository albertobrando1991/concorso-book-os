import {
  AlertTriangle,
  BookOpen,
  Bot,
  Database,
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

export const dynamic = "force-dynamic"

const navigation = [
  ["Overview", Database],
  ["Sources", FileSearch],
  ["Topics", Layers3],
  ["Books", BookOpen],
  ["Agents", Bot],
  ["Quality", ShieldCheck],
  ["Logs", ScrollText],
  ["Settings", Settings]
] as const

export default async function Home() {
  const data = await getDashboardData()
  const topSources = data.sources.slice(0, 5)
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
          <div className="topActions">
            <span>Active book</span>
            <strong>Il Metodo BANDO</strong>
          </div>
        </header>

        <section className="metrics" aria-label="Metriche operative">
          <Metric label="Fonti totali" value={data.metrics.totalSources} accent="blue" />
          <Metric label="Fonti non processate" value={data.metrics.unprocessedSources} accent="amber" />
          <Metric label="Topic recenti" value={data.metrics.recentTopics} accent="green" />
          <Metric label="Capitoli in bozza" value={data.metrics.draftChapters} accent="blue" />
          <Metric label="Capitoli consolidati" value={data.metrics.consolidatedChapters} accent="green" />
          <Metric label="Conflitti aperti" value={data.metrics.openConflicts} accent="red" />
        </section>

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
              {["Ingest Agent", "Knowledge Maintainer", "Book Writer", "Quiz Agent", "Lint Agent", "Review Agent"].map(
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

        <section className="grid three">
          <Panel title="Sources" icon={<FileSearch size={19} aria-hidden />} id="sources">
            <Table
              headers={["Fonte", "Tipo", "Affidabilita", "Stato"]}
              rows={topSources.map((source) => [
                source.title,
                source.sourceType,
                source.authorityLevel,
                source.status
              ])}
            />
          </Panel>

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
            {data.books.map((book) => (
              <div className="bookBlock" key={book.path}>
                <strong>{book.title}</strong>
                <span>{book.chapters} capitoli | {book.status}</span>
                <small>{book.reviewRequired ? "review_required" : "stable"}</small>
              </div>
            ))}
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
              {data.logEntries.slice(0, 6).map((entry) => (
                <code key={entry}>{entry}</code>
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

function Metric({ label, value, accent }: { label: string; value: number; accent: string }) {
  return (
    <div className={`metric ${accent}`}>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
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

function Table({ headers, rows }: { headers: string[]; rows: string[][] }) {
  return (
    <div className="tableWrap">
      <table>
        <thead>
          <tr>
            {headers.map((header) => (
              <th key={header}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.join("-")}>
              {row.map((cell) => (
                <td key={cell}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
