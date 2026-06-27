import { DEFAULT_BOOK_ID } from "../config"
import { FileWikiStore } from "../wiki/file-store"
import { sourceNotePath, renderSourceNote } from "../wiki/templates"
import type { AgentRunResult, SourceInput } from "../wiki/types"
import { classifySource } from "./classifier"
import { KnowledgeMaintainer } from "./knowledge-maintainer"

const RAW_FOLDERS: Record<SourceInput["sourceType"], string> = {
  article: "articles",
  law: "laws",
  decree: "decrees",
  manual: "manuals",
  website: "websites",
  transcript: "transcripts"
}

export class IngestAgent {
  constructor(private readonly store: FileWikiStore) {}

  async ingest(input: SourceInput): Promise<AgentRunResult> {
    const runId = `ingest-${Date.now()}`
    const source = classifySource(input)
    const rawPath = `raw/${RAW_FOLDERS[input.sourceType]}/${source.slug}.md`
    const sourcePath = sourceNotePath(source)
    const changedFiles = [rawPath, sourcePath]

    await this.store.writeText(rawPath, input.content)
    await this.store.writeText(
      sourcePath,
      renderSourceNote(source, {
        sourceUrl: input.sourceUrl,
        sourceDate: input.sourceDate
      })
    )

    const maintainer = new KnowledgeMaintainer(this.store)
    const maintained = await maintainer.applySource(source)
    changedFiles.push(...maintained)

    const impactedBooks = await this.markImpactedChapters(source.topics, sourcePath)
    await this.store.appendText(
      "log.md",
      `\n- ${new Date().toISOString()} | ingest | ${source.title} | source=${sourcePath} | topics=${source.topics.join(", ")} | impacted=${impactedBooks.join(", ") || "none"}`
    )

    return {
      runId,
      status: "completed",
      changedFiles: Array.from(new Set(changedFiles)),
      impactedBooks,
      artifacts: [
        {
          title: "Ingest Change Summary",
          path: "artifacts/code-diff-summary.md",
          kind: "summary"
        }
      ],
      messages: [
        `Created immutable raw source ${rawPath}`,
        `Created source note ${sourcePath}`,
        `Updated ${maintained.length} topic/entity pages`
      ]
    }
  }

  private async markImpactedChapters(topics: string[], sourcePath: string) {
    const files = await this.store.listMarkdown("books")
    const chapters = files.filter((item) => item.includes("/chapters/"))
    const impactedBooks = new Set<string>()

    for (const chapterPath of chapters) {
      const content = await this.store.readText(chapterPath)
      const isImpacted = topics.some((topic) => content.toLowerCase().includes(topic.toLowerCase()))

      if (!isImpacted) continue

      const bookId = chapterPath.split("/")[1] || DEFAULT_BOOK_ID

      await this.store.updateFrontmatter(chapterPath, {
        status: "to_expand",
        review_required: true,
        updated_at: new Date().toISOString()
      })
      await this.store.appendHeading(
        chapterPath,
        "Note editoriali",
        `- Da rivedere per nuova fonte [[${sourcePath.replace(".md", "")}]].`
      )
      impactedBooks.add(bookId)
    }

    return Array.from(impactedBooks)
  }
}

