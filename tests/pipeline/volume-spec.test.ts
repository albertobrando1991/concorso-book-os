import { describe, expect, it } from "vitest"
import { parseVolumeSpec } from "../../src/pipeline/spec/parse-volume-spec"
import { validateVolumeSpec } from "../../src/pipeline/spec/validate-volume-spec"

const specPath = "wiki/books/volumi/vol-03/planning/00-scheda-pipeline.md"
const complete = `---
type: pipeline_spec
volume_code: VOL-03
volume_title: Funzioni centrali, Fisco, Previdenza e Ispettivo
cut_off_date: 2026-07-27
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [C, D, F]
---

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | --- | --- |
| M-FC02 | moduli/m-fc02-agenzie-fiscali | 1 | C,D |
| M-FC01 | moduli/m-fc01-ministeri | 2 | C |

## Capitoli M-FC02

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Perimetro delle Agenzie fiscali | chapters/01-perimetro.md | planning/02-matrice-copertura-didattica.md | completo | |
| 02 | Tributi e procedimenti | chapters/02-tributi.md | planning/02-matrice-copertura-didattica.md | completo | rivedere soglie |
`

const parse = (markdown: string) => parseVolumeSpec(markdown, specPath)
const issueFields = (markdown: string) => validateVolumeSpec(parse(markdown)).map((issue) => issue.field)

describe("parseVolumeSpec", () => {
  it("reads the scalar fields the staff must supply", () => {
    expect(parse(complete)).toMatchObject({
      volumeCode: "VOL-03",
      volumeTitle: "Funzioni centrali, Fisco, Previdenza e Ispettivo",
      cutOffDate: "2026-07-27",
      responsabileNormativo: "Alberto Brando",
      responsabileEditoriale: "Alberto Brando",
      writerProvider: "codex",
      phases: ["C", "D", "F"],
      specPath
    })
  })
  it("reads modules in declaration order with their own phases", () => {
    expect(parse(complete).modules.map((module) => [module.code, module.moduleId, module.priority, module.phases])).toEqual([
      ["M-FC02", "moduli/m-fc02-agenzie-fiscali", 1, ["C", "D"]],
      ["M-FC01", "moduli/m-fc01-ministeri", 2, ["C"]]
    ])
  })
  it("attaches the chapters declared for a module and marks them as declared", () => {
    const [module] = parse(complete).modules
    expect(module.chaptersSource).toBe("declared")
    expect(module.chapters).toEqual([
      { number: "01", title: "Perimetro delle Agenzie fiscali", file: "chapters/01-perimetro.md", matrix: "planning/02-matrice-copertura-didattica.md", expectedStatus: "completo", notes: "" },
      { number: "02", title: "Tributi e procedimenti", file: "chapters/02-tributi.md", matrix: "planning/02-matrice-copertura-didattica.md", expectedStatus: "completo", notes: "rivedere soglie" }
    ])
  })
  it("marks chapters as derived when the module has no chapter table", () => {
    const module = parse(complete).modules[1]
    expect(module).toMatchObject({ code: "M-FC01", chapters: [], chaptersSource: "derived" })
  })
  it("falls back to the volume phases when a module declares none", () => {
    const markdown = complete.replace("| M-FC01 | moduli/m-fc01-ministeri | 2 | C |", "| M-FC01 | moduli/m-fc01-ministeri | 2 | |")
    expect(parse(markdown).modules[1].phases).toEqual(["C", "D", "F"])
  })
  it("returns empty values instead of throwing when the sheet is unusable", () => {
    expect(parse("prosa senza frontmatter")).toMatchObject({ volumeCode: "", modules: [], phases: [] })
  })
})

describe("validateVolumeSpec", () => {
  it("accepts a complete sheet", () => {
    expect(validateVolumeSpec(parse(complete))).toEqual([])
  })
  it.each([
    ["volume_code", "volumeCode"],
    ["volume_title", "volumeTitle"],
    ["cut_off_date", "cutOffDate"],
    ["responsabile_normativo", "responsabileNormativo"]
  ])("reports the missing mandatory field %s", (frontmatterKey, field) => {
    const markdown = complete.replace(new RegExp(`^${frontmatterKey}:.*$`, "m"), `${frontmatterKey}:`)
    expect(issueFields(markdown)).toContain(field)
  })
  it("names the sheet field, not the internal one, in the message", () => {
    const markdown = complete.replace(/^cut_off_date:.*$/m, "cut_off_date:")
    expect(validateVolumeSpec(parse(markdown))[0].message).toContain("cut_off_date")
  })
  it.each(["27-07-2026", "2026-13-01", "2026-02-31", "domani"])("rejects the invalid cut-off date %s", (value) => {
    expect(issueFields(complete.replace(/^cut_off_date:.*$/m, `cut_off_date: ${value}`))).toContain("cutOffDate")
  })
  it("rejects a volume code outside the VOL-NN shape", () => {
    expect(issueFields(complete.replace(/^volume_code:.*$/m, "volume_code: VOLUME 3"))).toContain("volumeCode")
  })
  it("rejects an unknown writer provider", () => {
    expect(issueFields(complete.replace(/^writer_provider:.*$/m, "writer_provider: gemini"))).toContain("writerProvider")
  })
  it("accepts a sheet without a writer provider, since the environment can supply it", () => {
    expect(issueFields(complete.replace(/^writer_provider:.*$/m, "writer_provider:"))).not.toContain("writerProvider")
  })
  it("rejects an unknown phase", () => {
    expect(issueFields(complete.replace(/^phases:.*$/m, "phases: [C, Z]"))).toContain("phases")
  })
  it("requires at least one module", () => {
    expect(issueFields(complete.replace(/## Moduli[\s\S]*?## Capitoli/, "## Capitoli"))).toContain("modules")
  })
  it("rejects a module code outside the M-XXNN shape", () => {
    expect(issueFields(complete.replace("| M-FC02 |", "| FC02 |"))).toContain("modules[0].code")
  })
  it("rejects a module id that is not a wiki book path", () => {
    expect(issueFields(complete.replace("moduli/m-fc02-agenzie-fiscali", "C:\\moduli\\m-fc02"))).toContain("modules[0].moduleId")
  })
  it("rejects a duplicated module code", () => {
    expect(issueFields(complete.replace("| M-FC01 | moduli/m-fc01-ministeri", "| M-FC02 | moduli/m-fc01-ministeri"))).toContain("modules[1].code")
  })
  it("rejects a chapter file outside the module chapters directory", () => {
    expect(issueFields(complete.replace("chapters/01-perimetro.md", "../altrove/01-perimetro.md"))).toContain("modules[0].chapters[0].file")
  })
  it("rejects a chapter file that is not markdown", () => {
    expect(issueFields(complete.replace("chapters/01-perimetro.md", "chapters/01-perimetro.docx"))).toContain("modules[0].chapters[0].file")
  })
  it("requires a public title for every explicitly declared chapter", () => {
    const markdown = complete.replace("Perimetro delle Agenzie fiscali", "")
    expect(issueFields(markdown)).toContain("modules[0].chapters[0].title")
  })
  it("points at the sheet line of the offending row", () => {
    const issue = validateVolumeSpec(parse(complete.replace("| M-FC02 |", "| FC02 |"))).find((item) => item.field === "modules[0].code")
    expect(issue?.line).toBe(16)
  })
})
