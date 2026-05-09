import { parseFrontmatter, withFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import { baseFrontmatter } from "../wiki/templates"

export class QuizAgent {
  constructor(private readonly store: FileWikiStore) {}

  async generateBaseQuiz() {
    const topics = await this.store.listMarkdown("topics")
    const topicTitles: string[] = []
    const sourceRefs: string[] = []

    for (const topicPath of topics) {
      const parsed = parseFrontmatter(await this.store.readText(topicPath))
      topicTitles.push(String(parsed.data.title || topicPath))

      if (Array.isArray(parsed.data.source_refs)) {
        sourceRefs.push(...parsed.data.source_refs.map(String))
      }
    }

    const path = "quizzes/quiz-base-concorsi-pubblici.md"

    await this.store.writeText(
      path,
      withFrontmatter(
        baseFrontmatter({
          id: "quiz-base-concorsi-pubblici",
          type: "quiz",
          title: "Quiz base concorsi pubblici",
          status: "draft",
          topics: topicTitles,
          sourceRefs: Array.from(new Set(sourceRefs)),
          confidence: 0.7,
          reviewRequired: true,
          tags: ["quiz", "recall"]
        }),
        `# Quiz base concorsi pubblici

## Domande a risposta multipla
1. Quale principio guida l'uso della knowledge base per generare capitoli?
   - A. Usare direttamente le raw sources.
   - B. Usare solo topic pages e source summaries consolidate.
   - C. Generare capitoli senza fonti.
   - D. Ignorare i log.
   - Risposta corretta: B.

2. Quale sezione segnala contenuti da verificare?
   - A. Stato revisione.
   - B. Titolo.
   - C. Assets.
   - D. Raw.
   - Risposta corretta: A.

## Flash recap
- Ogni claim importante deve puntare a source notes.
- I capitoli sono aggiornati incrementalmente.
- Il lint individua orfani, conflitti e gap.

## Errori tipici
- Studiare solo la fonte senza collegarla al topic.
- Non distinguere note canoniche da note di lavoro.
`
      )
    )

    await this.store.appendText(
      "log.md",
      `\n- ${new Date().toISOString()} | quiz_generate | ${path} | topics=${topicTitles.length}`
    )

    return path
  }
}

