import { DEFAULT_BOOK_ID } from "../config"
import { parseFrontmatter } from "../wiki/frontmatter"
import type { ClassifiedSource } from "../wiki/types"
import { FileWikiStore } from "../wiki/file-store"
import {
  entityNotePath,
  renderEntityNote,
  renderTopicNote,
  sourceNotePath,
  topicNotePath
} from "../wiki/templates"

export class KnowledgeMaintainer {
  constructor(private readonly store: FileWikiStore) {}

  async applySource(source: ClassifiedSource) {
    const changedFiles: string[] = []
    const sourcePath = sourceNotePath(source)

    for (const topic of source.topics) {
      const path = topicNotePath(topic)
      const sourceRefs = [sourcePath]

      if (await this.store.exists(path)) {
        const current = await this.store.readText(path)
        const parsed = parseFrontmatter(current)
        const nextSourceRefs = union(asStringArray(parsed.data.source_refs), sourceRefs)
        const nextEntities = union(asStringArray(parsed.data.entities), source.entities)
        await this.store.updateFrontmatter(path, {
          source_refs: nextSourceRefs,
          entities: nextEntities,
          updated_at: new Date().toISOString(),
          review_required: nextSourceRefs.length < 2
        })
        await this.store.appendHeading(
          path,
          "Sintesi",
          `- Aggiornamento da [[${sourcePath.replace(".md", "")}]]: ${source.summary}`
        )
      } else {
        await this.store.writeText(
          path,
          renderTopicNote({
            topic,
            sourceRefs,
            entities: source.entities,
            chapterRefs: [`books/${DEFAULT_BOOK_ID}/chapters/${chapterForTopic(topic)}.md`],
            summary: source.summary
          })
        )
      }

      changedFiles.push(path)
    }

    for (const entity of source.entities) {
      const path = entityNotePath(entity)

      if (await this.store.exists(path)) {
        const current = await this.store.readText(path)
        const parsed = parseFrontmatter(current)
        await this.store.updateFrontmatter(path, {
          source_refs: union(asStringArray(parsed.data.source_refs), [sourcePath]),
          topics: union(asStringArray(parsed.data.topics), source.topics),
          updated_at: new Date().toISOString()
        })
        await this.store.appendHeading(
          path,
          "Fonti",
          `- [[${sourcePath.replace(".md", "")}]]`
        )
      } else {
        await this.store.writeText(
          path,
          renderEntityNote({
            entity,
            sourceRefs: [sourcePath],
            topics: source.topics
          })
        )
      }

      changedFiles.push(path)
    }

    await this.updateIndex()

    return changedFiles
  }

  async updateIndex() {
    const sources = await this.store.listMarkdown("sources")
    const topics = await this.store.listMarkdown("topics")
    const entities = await this.store.listMarkdown("entities")
    const books = await this.store.listMarkdown("books")
    const now = new Date().toISOString()

    await this.store.writeText(
      "index.md",
      `# ConcorsoBook OS Index

Aggiornato: ${now}

## Sources
${sources.map((file) => `- [[${file.replace(".md", "")}]]`).join("\n") || "- Nessuna source note."}

## Topics
${topics.map((file) => `- [[${file.replace(".md", "")}]]`).join("\n") || "- Nessun topic."}

## Entities
${entities.map((file) => `- [[${file.replace(".md", "")}]]`).join("\n") || "- Nessuna entity."}

## Books
${books.map((file) => `- [[${file.replace(".md", "")}]]`).join("\n") || "- Nessun libro."}

## Operational Notes
- Raw sources restano immutabili in \`raw/\`.
- I capitoli devono essere generati da source summaries, topic pages ed entity pages.
- Ogni ingest deve appenderne traccia in \`log.md\`.
`
    )
  }
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function union(left: string[], right: string[]) {
  return Array.from(new Set([...left, ...right]))
}

function chapterForTopic(topic: string) {
  const normalized = topic.toLowerCase()

  if (normalized.includes("anatomia") || normalized.includes("decoder")) {
    return "anatomia-del-bando"
  }

  if (normalized.includes("moduli") || normalized.includes("piano") || normalized.includes("diario")) {
    return "sistema-adattabile"
  }

  if (normalized.includes("procedimento") || normalized.includes("amministrativo")) {
    return "diritto-amministrativo-per-candidati"
  }

  return "il-metodo-bando"
}
