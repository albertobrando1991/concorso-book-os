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
import {
  TEXT_CATALOG_MODULE_COUNT,
  TEXT_CATALOG_PACKAGE_RULES,
  TEXT_VOLUME_CATALOG,
  type TextVolume,
  findTextVolumeForBookId,
  isSpecialistTextVolume,
  isTextVolumeBookId,
  normalizeTextBookId,
  textBookIdFromPath,
  textCatalogSortRank,
  textLaunchWaveLabel,
  textVolumeBookId,
  textVolumeTierLabel
} from "@/src/catalog/text-volumes"

export const dynamic = "force-dynamic"

type HomeProps = {
  searchParams?: Promise<{
    source?: string | string[]
    bookId?: string | string[]
    chapterPath?: string | string[]
  }>
}

const navigation = [
  { label: "Strategia", id: "overview", Icon: Database },
  { label: "Catalogo", id: "catalogo", Icon: Library },
  { label: "Studio", id: "studio", Icon: BookOpen },
  { label: "Writer", id: "writer", Icon: PenIcon },
  { label: "Testi", id: "testi", Icon: BookOpen },
  { label: "Fonti", id: "sources", Icon: FileSearch },
  { label: "Topic", id: "topics", Icon: Layers3 },
  { label: "Graph", id: "graph", Icon: GitBranch },
  { label: "Agents", id: "agents", Icon: Bot },
  { label: "Quality", id: "quality", Icon: ShieldCheck },
  { label: "Logs", id: "logs", Icon: ScrollText },
  { label: "Settings", id: "settings", Icon: Settings }
] as const

export default async function Home({ searchParams }: HomeProps) {
  const data = await getDashboardData()
  const store = new FileWikiStore(getWikiRoot())
  const params = searchParams ? await searchParams : {}
  const requestedBookId = normalizeDashboardBookId(firstParam(params.bookId) || DEFAULT_BOOK_ID)
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
  const catalogVolumes = buildCatalogVolumes(data.books)
  const activeCatalogVolume = findTextVolumeForBookId(requestedBookId)
  const availableCatalogTexts = catalogVolumes.filter((volume) => volume.availableBooks.length > 0).length
  const reviewRequiredTexts = data.books.filter((book) => book.reviewRequired).length

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
          {navigation.map(({ label, id, Icon }) => (
            <a href={`#${id}`} key={id}>
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
            <p className="eyebrow">Libro base + ricettario digitale + 12 volumi specialistici</p>
            <h1>Dashboard catalogo testi e produzione editoriale</h1>
          </div>
          <div className="topActions" style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
            <span>Testo attivo</span>
            <BookSelector books={data.books} currentBookId={requestedBookId} />
            {activeCatalogVolume ? (
              <small className="activeVolumeNote">
                {activeCatalogVolume.code} | {textVolumeTierLabel(activeCatalogVolume.tier)} | {textLaunchWaveLabel(activeCatalogVolume.launchWave)}
              </small>
            ) : (
              <small className="activeVolumeNote">Testo fuori catalogo commerciale</small>
            )}
          </div>
        </header>

        <section className="metrics" aria-label="Metriche operative">
          <Metric label="Volumi catalogo" value={TEXT_VOLUME_CATALOG.length} accent="blue" />
          <Metric label="Moduli specialistici" value={TEXT_CATALOG_MODULE_COUNT} accent="green" />
          <Metric label="Testi in dashboard" value={availableCatalogTexts} accent="blue" />
          <Metric label="Fonti totali" value={data.metrics.totalSources} accent="green" />
          <Metric label="Review richieste" value={reviewRequiredTexts} accent="amber" />
          <Metric label="Conflitti aperti" value={data.metrics.openConflicts} accent="red" />
          <Metric label="Memorie locali" value={data.metrics.memoryAtoms} accent="amber" />
        </section>

        <CatalogStrategyPanel volumes={catalogVolumes} activeVolume={activeCatalogVolume} />

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
                <strong>Fondazione</strong>
                <span>Libro base, 11 nuclei comuni e ricettario digitale restano il centro del sistema.</span>
              </li>
              <li>
                <strong>Catalogo</strong>
                <span>{TEXT_VOLUME_CATALOG.length} volumi commerciali coprono {TEXT_CATALOG_MODULE_COUNT} moduli specialistici.</span>
              </li>
              <li>
                <strong>Produzione</strong>
                <span>{availableCatalogTexts} testi sono selezionabili in dashboard e lavorabili nello Studio.</span>
              </li>
              <li>
                <strong>Controllo</strong>
                <span>{data.qualityIssues.length} issue aperte da lint/review prima della pubblicazione.</span>
              </li>
            </ol>
          </Panel>

          <Panel title="Agent queue" icon={<Bot size={19} aria-hidden />} id="agents">
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

          <Panel title="Lista testi" icon={<BookOpen size={19} aria-hidden />} id="testi">
            <TextCatalogList volumes={catalogVolumes} currentBookId={requestedBookId} />
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

type DashboardBookItem = Awaited<ReturnType<typeof getDashboardData>>["books"][number]

type CatalogBookItem = {
  book: DashboardBookItem
  bookId: string
  moduleCode: string
}

type CatalogVolumeView = TextVolume & {
  volumeBookId: string
  isSpecialistVolume: boolean
  availableBooks: CatalogBookItem[]
  missingBookIds: string[]
}

function buildCatalogVolumes(books: DashboardBookItem[]): CatalogVolumeView[] {
  const booksById = new Map(
    books.map((book) => [normalizeTextBookId(textBookIdFromPath(book.path)), book])
  )

  return TEXT_VOLUME_CATALOG.map((volume) => {
    const isSpecialistVolume = isSpecialistTextVolume(volume)
    const availableBooks = volume.bookIds
      .map((bookId, index) => {
        const normalized = normalizeTextBookId(bookId)
        const book = booksById.get(normalized)

        if (!book) return null

        return {
          book,
          bookId: textBookIdFromPath(book.path),
          moduleCode: volume.modules[index] || "BASE"
        }
      })
      .filter((book): book is CatalogBookItem => Boolean(book))
      .sort((left, right) => textCatalogSortRank(left.bookId) - textCatalogSortRank(right.bookId))

    return {
      ...volume,
      volumeBookId: textVolumeBookId(volume),
      isSpecialistVolume,
      availableBooks,
      missingBookIds: volume.bookIds.filter((bookId) => !booksById.has(normalizeTextBookId(bookId)))
    }
  })
}

function CatalogStrategyPanel({
  volumes,
  activeVolume
}: {
  volumes: CatalogVolumeView[]
  activeVolume?: TextVolume
}) {
  const firstWaveModules = volumes
    .filter((volume) => volume.launchWave === "first")
    .flatMap((volume) => volume.modules)
  const secondWaveModules = volumes
    .filter((volume) => volume.launchWave === "second")
    .flatMap((volume) => volume.modules)
  const premiumModules = volumes
    .filter((volume) => volume.tier === "premium")
    .flatMap((volume) => volume.modules)

  return (
    <section className="grid two catalogStrategy" id="catalogo">
      <Panel title="Architettura commerciale" icon={<Library size={19} aria-hidden />}>
        <div className="catalogLevelGrid">
          <div>
            <span>Livello 1</span>
            <strong>Libro base</strong>
            <p>Manuale universale con Metodo BANDO, nucleo comune e prove.</p>
          </div>
          <div>
            <span>Livello 2</span>
            <strong>Ricettario digitale</strong>
            <p>Allenamento, schede, casi, planner, quiz e dashboard su capitalepersonale.it.</p>
          </div>
          <div>
            <span>Livello 3</span>
            <strong>Moduli specialistici</strong>
            <p>{TEXT_CATALOG_MODULE_COUNT} moduli raccolti in {TEXT_VOLUME_CATALOG.length} volumi commerciali.</p>
          </div>
        </div>

        <div className="packageGrid" aria-label="Pacchetti commerciali">
          {TEXT_CATALOG_PACKAGE_RULES.map((rule) => (
            <div className="packageCard" key={rule.key}>
              <strong>{rule.label}</strong>
              <span>{rule.formula}</span>
              <p>{rule.description}</p>
            </div>
          ))}
        </div>
      </Panel>

      <Panel title="Priorita produzione" icon={<ListChecks size={19} aria-hidden />}>
        <div className="launchStack">
          <LaunchRow label="Prima ondata" modules={firstWaveModules} note="Moduli a domanda alta e bando ricorrente." />
          <LaunchRow label="Seconda ondata" modules={secondWaveModules} note="Espansione ampia: centrali, fiscale, ICT, tecnico." />
          <LaunchRow label="Premium" modules={premiumModules} note="Target ristretto, prezzo alto, review settoriale obbligatoria." />
        </div>

        <div className="activeVolumeCard">
          <span>Testo attivo</span>
          <strong>{activeVolume ? `${activeVolume.code} - ${activeVolume.title}` : "Fuori catalogo"}</strong>
          <p>{activeVolume?.promise || "Il testo selezionato non appartiene ancora alla mappa commerciale a 12 volumi."}</p>
        </div>
      </Panel>
    </section>
  )
}

function LaunchRow({ label, modules, note }: { label: string; modules: string[]; note: string }) {
  return (
    <div className="launchRow">
      <div>
        <strong>{label}</strong>
        <span>{note}</span>
      </div>
      <p>{modules.join(" | ") || "Da definire"}</p>
    </div>
  )
}

function TextCatalogList({
  volumes,
  currentBookId
}: {
  volumes: CatalogVolumeView[]
  currentBookId: string
}) {
  const normalizedCurrent = normalizeTextBookId(currentBookId)

  return (
    <div className="textCatalogList">
      {volumes.map((volume) => (
        <article className="textVolumeCard" key={volume.code}>
          <header>
            <div>
              <span className={`volumeTier ${volume.tier}`}>{textVolumeTierLabel(volume.tier)}</span>
              <h3>{volume.code} - {volume.title}</h3>
            </div>
            <small>{textLaunchWaveLabel(volume.launchWave)}</small>
          </header>

          <p>{volume.promise}</p>

          {volume.isSpecialistVolume ? (
            <a
              href={`/?bookId=${encodeURIComponent(volume.volumeBookId)}#studio`}
              className={`catalogVolumeLink${normalizedCurrent === volume.volumeBookId ? " active" : ""}`}
            >
              Apri volume completo
            </a>
          ) : null}

          <div className="moduleChips" aria-label={`Moduli ${volume.code}`}>
            {(volume.modules.length > 0 ? volume.modules : ["B-PA01/B-PA11"]).map((module) => (
              <span key={module}>{module}</span>
            ))}
          </div>

          <div className="volumeVerticals">
            {volume.verticals.map((vertical) => (
              <span key={vertical}>{vertical}</span>
            ))}
          </div>

          <div className="volumeBooks">
            {volume.availableBooks.map(({ book, bookId, moduleCode }) => {
              const active = volume.isSpecialistVolume
                ? normalizedCurrent === volume.volumeBookId || normalizeTextBookId(bookId) === normalizedCurrent
                : normalizeTextBookId(bookId) === normalizedCurrent
              const details = (
                <>
                  <span>{moduleCode}</span>
                  <strong>{book.title}</strong>
                  <small>
                    {book.chapters} capitoli | {book.status} | {book.reviewRequired ? "review_required" : "stable"}
                  </small>
                </>
              )

              return volume.isSpecialistVolume ? (
                <div
                  className={`catalogBookLink moduleBookStatus${active ? " active" : ""}`}
                  key={book.path}
                >
                  {details}
                </div>
              ) : (
                <a
                  href={`/?bookId=${encodeURIComponent(bookId)}#studio`}
                  className={`catalogBookLink${active ? " active" : ""}`}
                  key={book.path}
                >
                  {details}
                </a>
              )
            })}

            {volume.missingBookIds.length > 0 ? (
              <div className="missingBooks">
                Da inizializzare: {volume.missingBookIds.map((bookId) => bookId.replace("moduli/", "")).join(", ")}
              </div>
            ) : null}
          </div>
        </article>
      ))}
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

function normalizeDashboardBookId(bookId: string) {
  const normalized = normalizeTextBookId(bookId)
  const volume = findTextVolumeForBookId(normalized)

  if (!volume || !isSpecialistTextVolume(volume)) return normalized
  if (isTextVolumeBookId(normalized)) return normalized

  return textVolumeBookId(volume)
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
