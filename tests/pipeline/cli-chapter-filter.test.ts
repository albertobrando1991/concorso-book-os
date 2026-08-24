import { describe, expect, it } from "vitest"
import { matchesChapter } from "../../src/pipeline/cli/commands"
import type { VolumeSpec } from "../../src/pipeline/spec/parse-volume-spec"
import type { StepRecord } from "../../src/pipeline/state/types"

const target = "moduli/m-fc03-enti-non-economici/chapters/appendice-a-vigilanza-ispettiva-inps-inail.md"

const spec: VolumeSpec = {
  specPath: "wiki/books/volumi/vol-03/planning/00-scheda-pipeline.md",
  volumeCode: "VOL-03",
  volumeTitle: "Volume 3",
  cutOffDate: "2026-08-22",
  writerProvider: "codex",
  phases: ["C"],
  modules: [
    {
      code: "M-FC03",
      moduleId: "moduli/m-fc03-enti-non-economici",
      priority: 1,
      phases: ["C"],
      chaptersSource: "declared",
      line: 1,
      chapterLines: [2],
      chapters: [
        {
          number: "14",
          title: "Vigilanza ispettiva",
          file: "chapters/appendice-a-vigilanza-ispettiva-inps-inail.md",
          matrix: "planning/02-matrice-copertura-didattica.md",
          expectedStatus: "final",
          notes: ""
        }
      ]
    }
  ]
}

const step = { target } as StepRecord

describe("filtro capitolo del CLI", () => {
  it("risolve il numero dichiarato anche quando il file è un'appendice", () => {
    expect(matchesChapter(step, "14", spec)).toBe(true)
  })

  it("non associa un numero dichiarato diverso", () => {
    expect(matchesChapter(step, "15", spec)).toBe(false)
  })

  it("mantiene il filtro legacy sui file con prefisso numerico", () => {
    const numbered = { target: "moduli/m-fc03/chapters/04-inail.md" } as StepRecord
    expect(matchesChapter(numbered, "04", spec)).toBe(true)
  })
})
