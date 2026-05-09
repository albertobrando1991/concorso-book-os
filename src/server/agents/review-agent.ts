import { FileWikiStore } from "../wiki/file-store"
import { LintAgent } from "./lint-agent"

export class ReviewAgent {
  constructor(private readonly store: FileWikiStore) {}

  async runQualityReview() {
    const lint = new LintAgent(this.store)
    const result = await lint.run()
    const highSeverity = result.issues.filter((issue) => issue.severity === "high")
    const lowCoverage = result.issues.filter((issue) => issue.issueType === "chapter_low_coverage")
    const path = `reviews/quality-review-${new Date().toISOString().slice(0, 10)}.md`

    await this.store.writeText(
      path,
      `# Quality review

Generato: ${new Date().toISOString()}

## Sintesi
- Issues totali: ${result.issues.length}
- Issues high severity: ${highSeverity.length}
- Capitoli con copertura bassa: ${lowCoverage.length}

## Azioni raccomandate
${highSeverity.map((issue) => `- ${issue.title}: ${issue.recommendation}`).join("\n") || "- Nessuna azione critica immediata."}

## Report collegato
- [[${result.reportPath.replace(".md", "")}]]
`
    )

    await this.store.appendText(
      "log.md",
      `\n- ${new Date().toISOString()} | review | issues=${result.issues.length} | report=${path}`
    )

    return { ...result, reviewPath: path }
  }
}

