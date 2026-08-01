import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"

const repoRoot = process.cwd()

describe("staff editorial contract", () => {
  it.each([
    "docs/PIPELINE.md",
    "wiki/AGENTS.md",
    ".agents/skills/pipeline-volume/SKILL.md"
  ])("keeps reader chapters and staff planning separate in %s", async (relativePath) => {
    const content = await readFile(path.join(repoRoot, relativePath), "utf8")

    expect(content).toMatch(/`chapters\/` contiene esclusivamente testo destinato al lettore/i)
    expect(content).toMatch(/`planning\/` contiene (?:gli )?artefatti editoriali interni/i)
    expect(content).toMatch(/piano staff[\s\S]*dichiarat[oa] nella scheda[\s\S]*pipeline/i)
    expect(content).toMatch(/indice studente[\s\S]*file editoriale[\s\S]*esiste/i)
    expect(content).toMatch(/non modificare[\s\S]*`pipeline\/<VOL>\/run-state\.json`/i)
  })

  it("makes the dashboard boundary explicit for staff", async () => {
    const guide = await readFile(path.join(repoRoot, "docs/PIPELINE.md"), "utf8")

    expect(guide).toMatch(/Piano editoriale staff/)
    expect(guide).toMatch(/anteprima commerciale[\s\S]*non[\s\S]*ispezione[\s\S]*artefatti interni/i)
  })
})
