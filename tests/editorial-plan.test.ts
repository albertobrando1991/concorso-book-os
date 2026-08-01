import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { buildEditorialPlan } from "@/src/server/book/editorial-plan"
import { buildBookStudioData } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

const moduleId = "moduli/m-sa01-sanita-amministrativa"
const chapter04 = "chapters/04-atti-procedimenti-flussi-informativi.md"
const chapter05 = "chapters/05-documentazione-accesso-conservazione.md"

describe("buildEditorialPlan", () => {
  it("combines declared chapters, existing files and run-state progress", async () => {
    const fixture = await createFixture(true)

    try {
      const plan = await buildEditorialPlan({
        store: new FileWikiStore(fixture.wikiRoot),
        projectRoot: fixture.projectRoot,
        bookId: "volumi/vol-07"
      })

      expect(plan).toMatchObject({
        volumeCode: "VOL-07",
        updatedAt: "2026-07-30T18:00:00.000Z",
        modules: [
          {
            code: "M-SA01",
            title: "Sanità amministrativa",
            chaptersSource: "declared",
            targets: [
              {
                number: "04",
                title: "Atti, procedimenti e flussi informativi nelle aziende sanitarie",
                exists: true,
                state: "in-review",
                nextStep: "10",
                gate: "didactic-density"
              },
              {
                number: "05",
                title: "Documentazione sanitaria, accesso, privacy e conservazione",
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
            chaptersSource: "derived",
            targets: []
          }
        ]
      })
    } finally {
      await fixture.cleanup()
    }
  })

  it("uses declared targets and file state when the run-state does not exist", async () => {
    const fixture = await createFixture(false)

    try {
      const plan = await buildEditorialPlan({
        store: new FileWikiStore(fixture.wikiRoot),
        projectRoot: fixture.projectRoot,
        bookId: "volumi/vol-07"
      })

      expect(plan?.modules[0].targets).toEqual([
        expect.objectContaining({ number: "04", state: "written", exists: true, nextStep: "" }),
        expect.objectContaining({ number: "05", state: "to-plan", exists: false, nextStep: "" })
      ])
    } finally {
      await fixture.cleanup()
    }
  })

  it("filters the staff plan when a specialist module is opened directly", async () => {
    const fixture = await createFixture(true)

    try {
      const plan = await buildEditorialPlan({
        store: new FileWikiStore(fixture.wikiRoot),
        projectRoot: fixture.projectRoot,
        bookId: moduleId
      })

      expect(plan?.modules.map((module) => module.code)).toEqual(["M-SA01"])
    } finally {
      await fixture.cleanup()
    }
  })

  it("returns null when the catalog volume has no pipeline sheet", async () => {
    const fixture = await createFixture(false)

    try {
      expect(await buildEditorialPlan({
        store: new FileWikiStore(fixture.wikiRoot),
        projectRoot: fixture.projectRoot,
        bookId: "volumi/vol-08"
      })).toBeNull()
    } finally {
      await fixture.cleanup()
    }
  })

  it("attaches the staff plan to Book Studio only when a project root is supplied", async () => {
    const fixture = await createFixture(true)
    const store = new FileWikiStore(fixture.wikiRoot)

    try {
      const withoutPipelineContext = await buildBookStudioData(store, "volumi/vol-07")
      const withPipelineContext = await buildBookStudioData(
        store,
        "volumi/vol-07",
        { projectRoot: fixture.projectRoot }
      )

      expect(withoutPipelineContext.editorialPlan).toBeNull()
      expect(withPipelineContext.editorialPlan?.volumeCode).toBe("VOL-07")
      expect(withPipelineContext.editorialPlan?.modules[0].targets).toHaveLength(2)
    } finally {
      await fixture.cleanup()
    }
  })
})

async function createFixture(withRunState: boolean) {
  const projectRoot = await mkdtemp(path.join(os.tmpdir(), "editorial-plan-"))
  const wikiRoot = path.join(projectRoot, "wiki")
  const volumePlanning = path.join(
    wikiRoot,
    "books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning"
  )
  const msa01Root = path.join(wikiRoot, "books", moduleId)
  const msa03Root = path.join(wikiRoot, "books/moduli/m-sa03-dirigenza-medica-sanitaria")

  await mkdir(volumePlanning, { recursive: true })
  await mkdir(path.join(msa01Root, "chapters"), { recursive: true })
  await mkdir(path.join(msa03Root, "chapters"), { recursive: true })
  await writeFile(path.join(volumePlanning, "00-scheda-pipeline.md"), pipelineSheet(), "utf8")
  await writeFile(
    path.join(msa01Root, "index.md"),
    "---\ntitle: M-SA01 — Sanità amministrativa\n---\n# M-SA01 — Sanità amministrativa",
    "utf8"
  )
  await writeFile(
    path.join(msa03Root, "index.md"),
    "---\ntitle: M-SA03 — Dirigenza medica e sanitaria\n---\n# M-SA03 — Dirigenza medica e sanitaria",
    "utf8"
  )
  await writeFile(
    path.join(msa01Root, chapter04),
    [
      "---",
      "type: book_chapter",
      "title: Atti, procedimenti e flussi informativi nelle aziende sanitarie",
      "status: draft",
      "outline_section: 4",
      "---",
      "# Atti, procedimenti e flussi informativi nelle aziende sanitarie"
    ].join("\n"),
    "utf8"
  )

  if (withRunState) {
    await mkdir(path.join(projectRoot, "pipeline/VOL-07"), { recursive: true })
    await writeFile(
      path.join(projectRoot, "pipeline/VOL-07/run-state.json"),
      `${JSON.stringify(runState(), null, 2)}\n`,
      "utf8"
    )
  }

  return {
    projectRoot,
    wikiRoot,
    cleanup: () => rm(projectRoot, { recursive: true, force: true })
  }
}

function pipelineSheet() {
  return `---
type: pipeline_spec
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
phases: [B, C]
---

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | --- | --- |
| M-SA01 | ${moduleId} | 1 | C |
| M-SA03 | moduli/m-sa03-dirigenza-medica-sanitaria | 2 | B |

## Capitoli M-SA01

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 04 | Atti, procedimenti e flussi informativi nelle aziende sanitarie | ${chapter04} | planning/02-matrice-copertura-didattica.md | completo | |
| 05 | Documentazione sanitaria, accesso, privacy e conservazione | ${chapter05} | planning/02-matrice-copertura-didattica.md | completo | |
`
}

function runState() {
  const steps = [
    step("08", chapter04, "done"),
    step("09", chapter04, "done"),
    step("10", chapter04, "in-progress"),
    step("11", chapter04, "pending"),
    step("12", chapter04, "pending"),
    step("08", chapter05, "pending"),
    step("09", chapter05, "pending"),
    step("10", chapter05, "pending"),
    step("11", chapter05, "pending"),
    step("12", chapter05, "pending")
  ]

  return {
    volumeCode: "VOL-07",
    specPath: "books/volumi/vol-07/planning/00-scheda-pipeline.md",
    specHash: "sha256:test",
    createdAt: "2026-07-30T17:00:00.000Z",
    updatedAt: "2026-07-30T18:00:00.000Z",
    steps
  }
}

function step(id: string, chapter: string, status: string) {
  const target = `${moduleId}/${chapter}`

  return {
    key: `${id}:${target}`,
    id,
    phase: "C",
    scope: "chapter",
    target,
    status,
    attempts: status === "pending" ? 0 : 1,
    evidence: []
  }
}
