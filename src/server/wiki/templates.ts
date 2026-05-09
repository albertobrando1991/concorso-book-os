import { DEFAULT_DOMAIN } from "../config"
import type { BaseFrontmatter, ClassifiedSource } from "./types"
import { createId, slugify } from "./slug"
import { withFrontmatter } from "./frontmatter"

export function baseFrontmatter(input: {
  id: string
  type: string
  title: string
  status?: string
  topics?: string[]
  entities?: string[]
  sourceRefs?: string[]
  bookRefs?: string[]
  confidence?: number
  reviewRequired?: boolean
  canonical?: boolean
  tags?: string[]
  extra?: Record<string, unknown>
}): BaseFrontmatter {
  const now = new Date().toISOString()

  return {
    id: input.id,
    type: input.type,
    title: input.title,
    status: input.status || "draft",
    domain: DEFAULT_DOMAIN,
    topics: input.topics || [],
    entities: input.entities || [],
    source_refs: input.sourceRefs || [],
    book_refs: input.bookRefs || [],
    confidence: input.confidence ?? 0.7,
    updated_at: now,
    created_at: now,
    review_required: input.reviewRequired ?? false,
    canonical: input.canonical ?? true,
    tags: input.tags || [],
    ...(input.extra || {})
  }
}

export function sourceNotePath(source: ClassifiedSource) {
  return `sources/${source.slug}.md`
}

export function topicNotePath(topic: string) {
  return `topics/${slugify(topic)}.md`
}

export function entityNotePath(entity: string) {
  return `entities/${slugify(entity)}.md`
}

export function bookNotePath(bookId: string) {
  return `books/${bookId}/index.md`
}

export function chapterNotePath(bookId: string, chapterSlug: string) {
  return `books/${bookId}/chapters/${chapterSlug}.md`
}

export function renderSourceNote(source: ClassifiedSource, input: { sourceUrl?: string; sourceDate?: string }) {
  return withFrontmatter(
    baseFrontmatter({
      id: source.id,
      type: "source",
      title: source.title,
      status: "processed",
      topics: source.topics,
      entities: source.entities,
      sourceRefs: [],
      confidence: source.authorityLevel === "alta" ? 0.9 : 0.72,
      tags: ["source", source.sourceType],
      extra: {
        source_type: source.sourceType,
        source_url: input.sourceUrl || "",
        source_date: input.sourceDate || "",
        authority_level: source.authorityLevel
      }
    }),
    `# ${source.title}

## Sintesi
${source.summary}

## Fonti
- Raw source collegata: \`wiki/raw/${source.sourceType}s/${source.slug}.md\`
${input.sourceUrl ? `- URL: ${input.sourceUrl}` : "- URL: non fornito"}

## Topic rilevati
${source.topics.map((topic) => `- [[${slugify(topic)}|${topic}]]`).join("\n")}

## Entita rilevate
${source.entities.map((entity) => `- [[${slugify(entity)}|${entity}]]`).join("\n")}

## Capitoli collegati
- Da determinare durante la manutenzione del libro.

## Stato revisione
Fonte processata automaticamente. Verifica umana richiesta solo per claim normativi di dettaglio.
`
  )
}

export function renderTopicNote(input: {
  topic: string
  sourceRefs: string[]
  entities: string[]
  chapterRefs?: string[]
  summary: string
}) {
  const id = createId("topic", input.topic)

  return withFrontmatter(
    baseFrontmatter({
      id,
      type: "topic",
      title: input.topic,
      status: "draft",
      topics: [input.topic],
      entities: input.entities,
      sourceRefs: input.sourceRefs,
      confidence: 0.76,
      tags: ["topic"],
      extra: {
        parent_topics: [],
        child_topics: [],
        chapter_refs: input.chapterRefs || []
      }
    }),
    `# ${input.topic}

## Sintesi
${input.summary}

## Fonti
${input.sourceRefs.map((ref) => `- [[${ref.replace(".md", "")}]]`).join("\n")}

## Entita collegate
${input.entities.map((entity) => `- [[${slugify(entity)}|${entity}]]`).join("\n")}

## Capitoli collegati
${(input.chapterRefs || []).map((chapter) => `- [[${chapter.replace(".md", "")}]]`).join("\n") || "- Nessun capitolo collegato."}

## Stato revisione
Da consolidare dopo almeno due fonti autorevoli o revisione umana.

## Note editoriali
Usare questa pagina come fonte consolidata per capitoli e quiz.
`
  )
}

export function renderEntityNote(input: { entity: string; sourceRefs: string[]; topics: string[] }) {
  const id = createId("entity", input.entity)

  return withFrontmatter(
    baseFrontmatter({
      id,
      type: "entity",
      title: input.entity,
      status: "draft",
      topics: input.topics,
      entities: [input.entity],
      sourceRefs: input.sourceRefs,
      confidence: 0.74,
      tags: ["entity"]
    }),
    `# ${input.entity}

## Sintesi
Entita o istituto rilevante per ${input.topics.join(", ")}.

## Fonti
${input.sourceRefs.map((ref) => `- [[${ref.replace(".md", "")}]]`).join("\n")}

## Topic collegati
${input.topics.map((topic) => `- [[${slugify(topic)}|${topic}]]`).join("\n")}

## Stato revisione
Da verificare e arricchire con definizioni normative.
`
  )
}

