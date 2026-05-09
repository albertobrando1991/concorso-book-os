import { DEFAULT_BOOK_ID } from "../config"
import { parseFrontmatter, withFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import { slugify } from "../wiki/slug"
import { baseFrontmatter, bookNotePath, chapterNotePath } from "../wiki/templates"
import type { AgentRunResult } from "../wiki/types"

interface TopicKnowledge {
  title: string
  path: string
  summary: string
  sourceRefs: string[]
  entities: string[]
}

export class BookWriterAgent {
  constructor(private readonly store: FileWikiStore) {}

  async compileDemoBook(bookId = DEFAULT_BOOK_ID): Promise<AgentRunResult> {
    const topics = await this.loadTopics()
    const now = new Date().toISOString()
    const chapterOneTopics = topics.filter((topic) =>
      ["anatomia del bando", "bando decoder"].includes(topic.title)
    )
    const chapterTwoTopics = topics.filter((topic) =>
      ["metodo bando", "piano 30 60 90 giorni", "diario errori"].includes(topic.title)
    )
    const changedFiles: string[] = []

    const masterPath = bookNotePath(bookId)
    await this.store.writeText(
      masterPath,
      withFrontmatter(
        baseFrontmatter({
          id: bookId,
          type: "book",
          title: "Il Metodo BANDO",
          status: "draft",
          topics: topics.map((topic) => topic.title),
          sourceRefs: union(topics.flatMap((topic) => topic.sourceRefs)),
          bookRefs: [bookId],
          confidence: 0.78,
          reviewRequired: true,
          tags: ["book", "demo"],
          extra: {
            last_compiled_from: topics.map((topic) => topic.path)
          }
        }),
        `# Il Metodo BANDO

## Obiettivo editoriale
Libro-workbook operativo per preparare concorsi pubblici diversi senza ricominciare da zero ogni volta. Il prodotto parte dal Metodo BANDO e usa le materie come moduli applicativi, non come trattato enciclopedico.

## Outline
1. [[books/${bookId}/chapters/anatomia-del-bando|Anatomia del bando e Bando Decoder]]
2. [[books/${bookId}/chapters/il-metodo-bando|Il Metodo BANDO]]
3. [[books/${bookId}/chapters/diritto-amministrativo-per-candidati|Diritto amministrativo per candidati]]
4. [[books/${bookId}/chapters/sistema-adattabile|Moduli profilo e piano 30/60/90]]

## Stato revisione
- Bozza demo generata dal wiki consolidato e dal riferimento prodotto canonico.
- Review umana richiesta sui riferimenti normativi puntuali.

## Revisioni
- ${now} | compilazione iniziale da topic pages.
`
      )
    )
    changedFiles.push(masterPath)

    const chapterOne = chapterNotePath(bookId, "anatomia-del-bando")
    await this.store.writeText(
      chapterOne,
      renderChapter({
        bookId,
        title: "Anatomia del bando e Bando Decoder",
        outlineSection: "1",
        topics: chapterOneTopics.length > 0 ? chapterOneTopics : topics.slice(0, 2)
      })
    )
    changedFiles.push(chapterOne)

    const chapterTwo = chapterNotePath(bookId, "il-metodo-bando")
    await this.store.writeText(
      chapterTwo,
      renderChapter({
        bookId,
        title: "Il Metodo BANDO",
        outlineSection: "2",
        topics: chapterTwoTopics.length > 0 ? chapterTwoTopics : topics.slice(2, 5)
      })
    )
    changedFiles.push(chapterTwo)

    await this.store.appendText(
      "log.md",
      `\n- ${now} | book_compile | ${bookId} | chapters=${changedFiles.filter((file) => file.includes("/chapters/")).length}`
    )

    return {
      runId: `book-${Date.now()}`,
      status: "completed",
      changedFiles,
      impactedBooks: [bookId],
      artifacts: [
        {
          title: "Book Demo Summary",
          path: "artifacts/final-readiness-report.md",
          kind: "report"
        }
      ],
      messages: ["Compiled demo book from consolidated topic pages"]
    }
  }

  private async loadTopics(): Promise<TopicKnowledge[]> {
    const topicPaths = await this.store.listMarkdown("topics")
    const topics: TopicKnowledge[] = []

    for (const topicPath of topicPaths) {
      const content = await this.store.readText(topicPath)
      const parsed = parseFrontmatter(content)
      topics.push({
        title: String(parsed.data.title || topicPath),
        path: topicPath,
        summary: extractSection(content, "Sintesi"),
        sourceRefs: asStringArray(parsed.data.source_refs),
        entities: asStringArray(parsed.data.entities)
      })
    }

    return topics
  }
}

function renderChapter(input: {
  bookId: string
  title: string
  outlineSection: string
  topics: TopicKnowledge[]
}) {
  const sourceRefs = union(input.topics.flatMap((topic) => topic.sourceRefs))
  const topicTitles = input.topics.map((topic) => topic.title)
  const chapterSlug = slugify(input.title)

  return withFrontmatter(
    baseFrontmatter({
      id: `chapter-${chapterSlug}`,
      type: "chapter",
      title: input.title,
      status: "draft",
      topics: topicTitles,
      entities: union(input.topics.flatMap((topic) => topic.entities)),
      sourceRefs,
      bookRefs: [input.bookId],
      confidence: sourceRefs.length >= 2 ? 0.82 : 0.68,
      reviewRequired: sourceRefs.length < 2,
      tags: ["book-chapter"],
      extra: {
        book_id: input.bookId,
        outline_section: input.outlineSection,
        draft_stage: "demo-draft",
        last_compiled_from: input.topics.map((topic) => topic.path)
      }
    }),
    `# ${input.title}

## Obiettivo didattico
Guidare il candidato nell'uso operativo dei seguenti blocchi del prodotto: ${topicTitles.join(", ")}.

## Spiegazione
${input.topics.map((topic) => `### ${topic.title}\n${topic.summary}`).join("\n\n")}

## Punti chiave
${input.topics.map((topic) => `- ${topic.title}: trasformare teoria, bando e allenamento in uno strumento compilabile.`).join("\n")}

## Norme o riferimenti
${sourceRefs.map((ref) => `- [[${ref.replace(".md", "")}]]`).join("\n") || "- Fonti consolidate non ancora sufficienti."}

## Esempi
- Applicare il metodo a un bando reale: estrarre requisiti, prove, materie core, rischi e calendario.
- Trasformare una materia giuridica in una risposta da concorso con definizione, funzione, caso e domanda-trappola.

## Errori frequenti
- Confondere fonte raw e conoscenza consolidata.
- Citare una norma senza collegarla alla sua source note.
- Trasformare il libro in un manuale enciclopedico, perdendo il focus workbook del Metodo BANDO.

## Quiz collegati
- [[quizzes/quiz-base-concorsi-pubblici]]

## Note editoriali
- Capitolo generato solo da topic pages e source summaries.
- Integrare esempi e riferimenti dopo review umana.
`
  )
}

function extractSection(content: string, heading: string) {
  const lines = content.replace(/\r\n/g, "\n").split("\n")
  const start = lines.findIndex((line) => line.trim().toLowerCase() === `## ${heading.toLowerCase()}`)

  if (start === -1) return ""

  let end = lines.length

  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^#{1,2}\s+/.test(lines[index])) {
      end = index
      break
    }
  }

  return lines.slice(start + 1, end).join("\n").trim()
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}

function union(values: string[]) {
  return Array.from(new Set(values.filter(Boolean)))
}
