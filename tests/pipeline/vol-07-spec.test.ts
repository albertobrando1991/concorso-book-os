import path from "node:path"
import { describe, expect, it } from "vitest"
import { loadVolumeSpec } from "../../src/pipeline/spec/load-volume-spec"
import { buildStepDrafts } from "../../src/pipeline/steps/build-steps"

describe("VOL-07 pipeline spec", () => {
  it("loads the real sheet with the approved roles, phases and module order", async () => {
    const loaded = await loadVolumeSpec({
      wikiRoot: path.resolve(process.cwd(), "wiki"),
      volumeCode: "VOL-07"
    })

    expect(loaded.issues).toEqual([])
    expect(loaded.spec).toMatchObject({
      volumeCode: "VOL-07",
      volumeTitle: "Sanità amministrativa e professioni sanitarie",
      cutOffDate: "2026-07-28",
      responsabileNormativo: "Alberto Brando",
      responsabileEditoriale: "Alberto Brando",
      writerProvider: "codex",
      phases: ["A", "B"]
    })
    expect(loaded.spec.modules.map((module) => [module.code, module.priority, module.phases])).toEqual([
      ["M-SA02", 1, ["A", "B"]],
      ["M-SA01", 2, ["A", "B", "C"]],
      ["M-SA03", 3, ["A", "B"]],
      ["M-SA04", 4, ["A", "B"]]
    ])
    const msa01 = loaded.spec.modules.find((module) => module.code === "M-SA01")

    expect(msa01).toBeDefined()
    expect(msa01).toMatchObject({
      chaptersSource: "declared",
      chapters: [
        {
          number: "04",
          file: "chapters/04-atti-procedimenti-flussi-informativi.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "05",
          file: "chapters/05-documentazione-accesso-conservazione.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "06",
          file: "chapters/06-front-office-comunicazione-utenza.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "09",
          file: "chapters/09-contabilita-budget-controllo-gestione.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "10",
          file: "chapters/10-procurement-farmaci-dispositivi-magazzino.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        }
      ]
    })
    expect(loaded.spec.modules.slice(2).every((module) => module.chaptersSource === "derived")).toBe(true)

    const msa01Steps = buildStepDrafts(loaded.spec, ["C"]).filter((step) =>
      step.target.startsWith("moduli/m-sa01-sanita-amministrativa/chapters/")
    )

    expect(msa01Steps).toHaveLength(25)
    expect(msa01Steps[0]?.key).toBe(
      "08:moduli/m-sa01-sanita-amministrativa/chapters/04-atti-procedimenti-flussi-informativi.md"
    )
    expect(msa01Steps.at(-1)?.key).toBe(
      "12:moduli/m-sa01-sanita-amministrativa/chapters/10-procurement-farmaci-dispositivi-magazzino.md"
    )
  })
})
