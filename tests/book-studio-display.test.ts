import { renderToStaticMarkup } from "react-dom/server"
import { createElement } from "react"
import { describe, expect, it } from "vitest"
import {
  EditorialPlanPanel,
  editorialTargetStateLabel,
  formatChapterLabel,
  formatCodedTitle
} from "@/app/components/editorial-plan-panel"
import type { BookStudioEditorialPlan } from "@/src/server/book/editorial-plan"

describe("Book Studio display labels", () => {
  it("formats staff chapter numbers with a leading zero and a long dash", () => {
    expect(formatChapterLabel("3", "Discipline professionali")).toBe(
      "Capitolo 03 — Discipline professionali"
    )
  })

  it("formats module codes once", () => {
    expect(formatCodedTitle("M-SA01", "M-SA01 - Sanità amministrativa")).toBe(
      "M-SA01 — Sanità amministrativa"
    )
  })

  it.each([
    ["to-plan", "Da pianificare"],
    ["to-write", "Da scrivere"],
    ["in-progress", "In lavorazione"],
    ["written", "Scritto"],
    ["in-review", "In revisione"],
    ["complete", "Completato"],
    ["blocked", "Bloccato"]
  ] as const)("maps %s to %s", (state, label) => {
    expect(editorialTargetStateLabel(state)).toBe(label)
  })

  it("renders planned targets as staff information, not reader navigation", () => {
    const html = renderToStaticMarkup(createElement(EditorialPlanPanel, { plan: planFixture() }))

    expect(html).toContain("Piano editoriale staff")
    expect(html).toContain("Non incluso nell&#x27;anteprima del libro")
    expect(html).toContain("Capitolo 05 — Documentazione sanitaria")
    expect(html).toContain("Capitoli non ancora dichiarati nella pipeline")
    expect(html).not.toContain("<a")
    expect(html).not.toContain("<button")
  })
})

function planFixture(): BookStudioEditorialPlan {
  return {
    volumeCode: "VOL-07",
    updatedAt: "2026-07-30T18:00:00.000Z",
    modules: [
      {
        code: "M-SA01",
        title: "Sanità amministrativa",
        moduleId: "moduli/m-sa01-sanita-amministrativa",
        priority: 1,
        chaptersSource: "declared",
        targets: [
          {
            number: "05",
            title: "Documentazione sanitaria",
            path: "books/moduli/m-sa01-sanita-amministrativa/chapters/05-documentazione.md",
            exists: false,
            state: "to-plan",
            nextStep: "08",
            gate: "chapter-plan"
          }
        ]
      },
      {
        code: "M-SA03",
        title: "Dirigenza medica e sanitaria",
        moduleId: "moduli/m-sa03-dirigenza-medica-sanitaria",
        priority: 2,
        chaptersSource: "derived",
        targets: []
      }
    ]
  }
}
