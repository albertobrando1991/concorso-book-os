import { parseFrontmatter } from "../wiki/frontmatter"
import { FileWikiStore } from "../wiki/file-store"
import { extractWikiLinks } from "../wiki/markdown"
import type { QualityIssue } from "../wiki/types"

export class LintAgent {
  constructor(private readonly store: FileWikiStore) {}

  async analyze() {
    const files = await this.store.listMarkdown("")
    const markdownFiles = files.filter((file) => !file.startsWith("raw/"))
    const contentByFile = new Map<string, string>()
    const pathKeys = new Set(markdownFiles.map((file) => file.replace(".md", "")))
    const inbound = new Map<string, number>()
    const issues: QualityIssue[] = []

    for (const file of markdownFiles) {
      const content = await this.store.readText(file)
      contentByFile.set(file, content)

      for (const link of extractWikiLinks(content)) {
        inbound.set(link, (inbound.get(link) || 0) + 1)
      }
    }

    for (const file of markdownFiles) {
      if (["AGENTS.md", "index.md", "log.md"].includes(file)) continue

      const key = file.replace(".md", "")
      const content = contentByFile.get(file) || ""
      const parsed = parseFrontmatter(content)
      const type = String(parsed.data.type || "")
      const confidence = Number(parsed.data.confidence || 1)

      if (!inbound.has(key) && !file.includes("/index.md")) {
        issues.push({
          id: `orphan-${key}`,
          title: `Pagina senza inbound link: ${file}`,
          severity: "medium",
          issueType: "orphan_page",
          affectedPages: [file],
          recommendation: "Collegare la pagina da index, topic correlati o capitoli."
        })
      }

      if (confidence < 0.72) {
        issues.push({
          id: `low-confidence-${key}`,
          title: `Bassa confidenza: ${file}`,
          severity: "medium",
          issueType: "low_confidence",
          affectedPages: [file],
          recommendation: "Aggiungere fonti autorevoli o richiedere review umana."
        })
      }

      if (type === "chapter") {
        const sources = Array.isArray(parsed.data.source_refs) ? parsed.data.source_refs : []

        if (sources.length < 2) {
          issues.push({
            id: `thin-chapter-${key}`,
            title: `Capitolo con fonti insufficienti: ${file}`,
            severity: "high",
            issueType: "chapter_low_coverage",
            affectedPages: [file],
            recommendation: "Espandere il capitolo dopo avere consolidato almeno due source notes."
          })
        }
      }

      const topics = Array.isArray(parsed.data.topics) ? parsed.data.topics.map(String) : []

      for (const topic of topics) {
        const topicKey = `topics/${topic.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "")}`

        if (topic && !pathKeys.has(topicKey) && type !== "topic") {
          issues.push({
            id: `missing-topic-${key}-${topicKey}`,
            title: `Topic citato ma mancante: ${topic}`,
            severity: "medium",
            issueType: "missing_topic",
            affectedPages: [file],
            recommendation: `Creare o collegare la topic page ${topicKey}.`
          })
        }
      }
    }

    return issues
  }

  async run() {
    const issues = await this.analyze()

    const reportPath = `reviews/lint-${new Date().toISOString().slice(0, 10)}.md`
    await this.store.writeText(
      reportPath,
      `# Lint report

Generato: ${new Date().toISOString()}

## Issues
${issues.map((issue) => `- ${issue.severity.toUpperCase()} | ${issue.issueType} | ${issue.title} | ${issue.recommendation}`).join("\n") || "- Nessuna issue rilevata."}
`
    )
    await this.store.appendText(
      "log.md",
      `\n- ${new Date().toISOString()} | lint | issues=${issues.length} | report=${reportPath}`
    )

    return { issues, reportPath }
  }
}
