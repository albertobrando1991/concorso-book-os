import { getWikiRoot } from "../config"
import { listArtifacts } from "../artifacts/service"
import { LintAgent } from "../agents/lint-agent"
import { LocalAgentMemory } from "../memory/local-agent-memory"
import { FileWikiStore } from "../wiki/file-store"
import { parseFrontmatter } from "../wiki/frontmatter"
import type {
  DashboardBook,
  DashboardData,
  DashboardSource,
  DashboardTopic
} from "../wiki/types"

export async function getDashboardData(): Promise<DashboardData> {
  const store = new FileWikiStore(getWikiRoot())
  const [sources, topics, books, logEntries, artifacts] = await Promise.all([
    loadSources(store),
    loadTopics(store),
    loadBooks(store),
    loadLogs(store),
    listArtifacts()
  ])
  const lint = new LintAgent(store)
  const qualityIssues = await lint.analyze()
  const draftChapters = books.reduce((count, book) => count + book.chapters, 0)
  const memoryStats = await LocalAgentMemory.fromConfig().stats()

  return {
    metrics: {
      totalSources: sources.length,
      unprocessedSources: sources.filter((source) => source.status !== "processed").length,
      recentTopics: topics.filter((topic) => isRecent(topic.updatedAt)).length,
      draftChapters,
      consolidatedChapters: books.filter((book) => book.status === "consolidated").length,
      openConflicts: qualityIssues.filter((issue) => issue.issueType.includes("conflict")).length,
      memoryConversations: memoryStats.conversations,
      memoryAtoms: memoryStats.atoms
    },
    sources,
    topics,
    books,
    qualityIssues,
    logEntries,
    agentRuns: logEntries.slice(0, 8),
    artifacts
  }
}

async function loadSources(store: FileWikiStore): Promise<DashboardSource[]> {
  const files = await store.listMarkdown("sources")
  const sources: DashboardSource[] = []

  for (const file of files) {
    const parsed = parseFrontmatter(await store.readText(file))
    sources.push({
      title: String(parsed.data.title || file),
      path: file,
      status: String(parsed.data.status || "unknown"),
      sourceType: String(parsed.data.source_type || "unknown"),
      authorityLevel: String(parsed.data.authority_level || "unknown"),
      topics: asStringArray(parsed.data.topics),
      updatedAt: String(parsed.data.updated_at || "")
    })
  }

  return sources
}

async function loadTopics(store: FileWikiStore): Promise<DashboardTopic[]> {
  const files = await store.listMarkdown("topics")
  const topics: DashboardTopic[] = []

  for (const file of files) {
    const parsed = parseFrontmatter(await store.readText(file))
    topics.push({
      title: String(parsed.data.title || file),
      path: file,
      status: String(parsed.data.status || "unknown"),
      sourceRefs: asStringArray(parsed.data.source_refs),
      chapterRefs: asStringArray(parsed.data.chapter_refs),
      confidence: Number(parsed.data.confidence || 0),
      updatedAt: String(parsed.data.updated_at || "")
    })
  }

  return topics
}

async function loadBooks(store: FileWikiStore): Promise<DashboardBook[]> {
  const files = await store.listMarkdown("books")
  const bookIndexes = files.filter((file) => file.endsWith("/index.md"))
  const books: DashboardBook[] = []

  for (const file of bookIndexes) {
    const parsed = parseFrontmatter(await store.readText(file))
    const bookFolder = file.replace("/index.md", "")
    const chapters = (await store.listMarkdown(`${bookFolder}/chapters`)).length

    books.push({
      title: String(parsed.data.title || file),
      path: file,
      status: String(parsed.data.status || "unknown"),
      chapters,
      reviewRequired: Boolean(parsed.data.review_required),
      updatedAt: String(parsed.data.updated_at || "")
    })
  }

  return books
}

async function loadLogs(store: FileWikiStore) {
  try {
    const content = await store.readText("log.md")
    return content
      .split("\n")
      .filter((line) => line.trim().startsWith("- "))
      .reverse()
      .slice(0, 20)
  } catch {
    return []
  }
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function isRecent(value: string) {
  const time = Date.parse(value)

  if (Number.isNaN(time)) return false

  return Date.now() - time < 1000 * 60 * 60 * 24 * 14
}
