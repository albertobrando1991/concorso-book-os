import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"

const readProjectFile = (relativePath: string) =>
  readFile(path.join(process.cwd(), relativePath), "utf8")

describe("canonical editorial typography", () => {
  it("keeps the shared book renderer on the Arial and Garamond scale", async () => {
    const css = await readProjectFile("app/globals.css")

    expect(css).toContain('--manual-serif: Garamond, "Adobe Garamond Pro", "EB Garamond"')
    expect(css).toContain("--manual-sans: Arial, Helvetica, sans-serif")
    expect(css).toMatch(/\.chapterPreviewHeader h2\s*\{[^}]*font-size:\s*20pt;[^}]*font-weight:\s*700;/)
    expect(css).toMatch(/\.previewBlocks\s*\{[^}]*font-family:\s*var\(--book-body\);[^}]*font-size:\s*11pt;[^}]*line-height:\s*1\.18;/)
    expect(css).toMatch(/\.previewBlocks h3\s*\{[^}]*font-size:\s*14pt;[^}]*font-weight:\s*700;/)
    expect(css).toMatch(/\.previewBlocks h4\s*\{[^}]*font-size:\s*12pt;[^}]*font-weight:\s*700;/)
    expect(css).toMatch(/\.previewTable\s*\{[^}]*font-family:\s*var\(--manual-sans\);[^}]*font-size:\s*9\.5pt;/)
    expect(css).toMatch(/\.previewCallout\s*\{[^}]*font-family:\s*var\(--manual-sans\);/)
    expect(css).toMatch(/\.digitalServicesContent h3\s*\{[^}]*font-size:\s*14pt;/)
    expect(css).toMatch(/\.digitalServicesContent \.previewCallout p\s*\{[^}]*font-size:\s*9\.5pt;/)
  })

  it("keeps writers and reviewers aligned with the same canonical rule", async () => {
    const [designSystem, writerSkill, agentInstructions, writerAgent, reviewerAgent] =
      await Promise.all([
        readProjectFile("wiki/books/il-metodo-bando/design-system-editoriale.md"),
        readProjectFile(".agents/skills/concorso-book-professional-writer/SKILL.md"),
        readProjectFile("wiki/AGENTS.md"),
        readProjectFile("src/server/agents/manual-writer-agent.ts"),
        readProjectFile("src/server/agents/editorial-reviewer-agent.ts")
      ])

    for (const source of [designSystem, writerSkill, agentInstructions, writerAgent]) {
      expect(source).toContain("Garamond")
      expect(source).toContain("Arial")
      expect(source).toContain("11 pt")
      expect(source).toContain("14 pt")
      expect(source).toContain("12 pt")
    }

    expect(designSystem).toContain("9,5-10 pt")
    expect(designSystem).toContain("Le immagini raster gia prodotte restano integre")
    expect(reviewerAgent).toContain("loadDesignSystemGuide")
    expect(reviewerAgent).toContain("Garamond Regular 11 pt")
    expect(reviewerAgent).toContain("Arial 9,5-10 pt")
  })
})
