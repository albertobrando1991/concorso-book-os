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
      writerProvider: "codex",
      phases: ["A", "B", "C", "D", "E", "F"]
    })
    expect(loaded.spec.modules.map((module) => [module.code, module.priority, module.phases])).toEqual([
      ["M-SA02", 1, ["A", "B", "C", "D", "E", "F"]],
      ["M-SA01", 2, ["A", "B", "C", "D", "E", "F"]],
      ["M-SA03", 3, ["A", "B", "C", "D", "E", "F"]],
      ["M-SA04", 4, ["A", "B", "C", "D", "E", "F"]]
    ])
    expect(loaded.spec.modules[0]?.chaptersSource).toBe("declared")
    expect(
      loaded.spec.modules[0]?.chapters.map((chapter) => [
        chapter.number,
        chapter.file,
        chapter.expectedStatus
      ])
    ).toEqual([
      ["01", "chapters/01-mappa-profili-e-prove.md", "completo"],
      ["03", "chapters/03-discipline-professionali-autonomia-responsabilita.md", "completo"],
      ["04", "chapters/04-assistenza-infermieristica-tecniche-assistenziali-oss.md", "completo"],
      ["05", "chapters/05-valutazione-clinica-triage-urgenza-emergenza.md", "completo"],
      ["06", "chapters/06-prevenzione-continuita-presa-in-carico.md", "completo"],
      ["07", "chapters/07-evidenze-pico-grade-applicabilita.md", "completo"],
      ["08", "chapters/08-igiene-pubblica-epidemiologia-screening.md", "completo"],
      ["09", "chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md", "completo"],
      ["10", "chapters/10-prova-pratica-casi-professionali.md", "completo"]
    ])
    const msa01 = loaded.spec.modules.find((module) => module.code === "M-SA01")

    expect(msa01).toBeDefined()
    expect(msa01).toMatchObject({
      chaptersSource: "declared",
      chapters: [
        {
          number: "04",
          title: "Atti, procedimenti e flussi informativi nelle aziende sanitarie",
          file: "chapters/04-atti-procedimenti-flussi-informativi.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "05",
          title: "Documentazione sanitaria, accesso, privacy e conservazione",
          file: "chapters/05-documentazione-accesso-conservazione.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "06",
          title: "Front office e comunicazione con l'utenza",
          file: "chapters/06-front-office-comunicazione-utenza.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "09",
          title: "Contabilità, budget e controllo di gestione",
          file: "chapters/09-contabilita-budget-controllo-gestione.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        },
        {
          number: "10",
          title: "Procurement sanitario, farmaci, dispositivi e magazzino",
          file: "chapters/10-procurement-farmaci-dispositivi-magazzino.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "completo"
        }
      ]
    })
    expect(loaded.spec.modules.every((module) => module.chaptersSource === "declared")).toBe(true)

    const chapter03Target =
      "moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md"
    const chapter03Steps = buildStepDrafts(loaded.spec, ["C"]).filter(
      (step) => step.target === chapter03Target
    )

    expect(chapter03Steps.map((step) => step.key)).toEqual([
      `08:${chapter03Target}`,
      `09:${chapter03Target}`,
      `10:${chapter03Target}`,
      `11:${chapter03Target}`,
      `12:${chapter03Target}`
    ])

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
