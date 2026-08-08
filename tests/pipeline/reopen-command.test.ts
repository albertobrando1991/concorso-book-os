import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { afterEach, beforeEach, describe, expect, it } from "vitest"
import { parseArgs } from "../../src/pipeline/cli/args"
import { runCommand } from "../../src/pipeline/cli/commands"
import { createRunState, stepKey } from "../../src/pipeline/state/run-state"
import { saveRunState } from "../../src/pipeline/state/run-state-store"
import type { RunState, StepRecord } from "../../src/pipeline/state/types"

const moduleId = "moduli/m-tr01-ict-trasformazione-digitale"
const chapterOne = `${moduleId}/chapters/01-ruoli-ict.md`
const chapterTwo = `${moduleId}/chapters/02-cybersecurity.md`
const now = "2026-08-05T12:00:00.000Z"

let fixtureRoot = ""
let originalCwd = ""

beforeEach(async () => {
  fixtureRoot = await mkdtemp(path.join(os.tmpdir(), "pipeline-reopen-command-"))
  originalCwd = process.cwd()
  process.chdir(fixtureRoot)
  await writeFixture(fixtureRoot)
})

afterEach(async () => {
  process.chdir(originalCwd)
  await rm(fixtureRoot, { recursive: true, force: true })
})

describe.sequential("pipeline reopen command", () => {
  it("reopens every step-08 chapter of a declared module and persists only that volume state", async () => {
    const result = await runCommand(
      parseArgs(["reopen", "VOL-08", "--step", "08", "--module", "M-TR01", "--cascade", "--note", "Retrofit formato 2 autorizzato"])
    )

    const expectedStartKeys = [stepKey("08", chapterOne), stepKey("08", chapterTwo)]
    const updated = await readState("VOL-08")

    expect(result).toMatchObject({
      exitCode: 0,
      payload: {
        ok: true,
        command: "reopen",
        volumeCode: "VOL-08",
        startKeys: expectedStartKeys,
        reopened: [stepKey("08", chapterOne), stepKey("09", chapterOne), stepKey("08", chapterTwo), stepKey("09", chapterTwo), stepKey("13", moduleId)]
      }
    })
    expect(updated.steps.map((step) => step.status)).toEqual(["pending", "pending", "pending", "pending", "pending", "pending"])
    expect(updated.steps[0].evidence).toContain("reopen: Retrofit formato 2 autorizzato")
    expect(updated.steps[2].evidence).toContain("reopen: Retrofit formato 2 autorizzato")
    expect(await readFile(path.join(fixtureRoot, "pipeline", "VOL-99", "run-state.json"), "utf8")).toBe('{"sentinel":true}\n')
  })

  it("narrows declared module targets with --chapter", async () => {
    const result = await runCommand(
      parseArgs(["reopen", "VOL-08", "--step", "08", "--module", "M-TR01", "--chapter", "01", "--cascade", "--note", "Capitolo 01 da adeguare"])
    )

    expect(result.payload).toMatchObject({ startKeys: [stepKey("08", chapterOne)] })
  })

  it("resolves a declared chapter without requiring --module", async () => {
    const result = await runCommand(
      parseArgs(["reopen", "VOL-08", "--step", "08", "--chapter", "02", "--cascade", "--note", "Capitolo 02 da adeguare"])
    )

    expect(result.payload).toMatchObject({ startKeys: [stepKey("08", chapterTwo)] })
  })

  it.each([
    [["reopen", "VOL-08", "--module", "M-TR01", "--cascade", "--note", "Motivo"], /--step/i],
    [["reopen", "VOL-08", "--step", "08", "--module", "M-TR01", "--cascade"], /--note/i],
    [["reopen", "VOL-08", "--step", "08", "--module", "M-UNKNOWN", "--cascade", "--note", "Motivo"], /M-UNKNOWN|modulo/i],
    [["reopen", "VOL-08", "--step", "08", "--cascade", "--note", "Motivo"], /--module o --chapter/i],
    [["reopen", "VOL-08", "--step", "08", "--chapter", "99", "--cascade", "--note", "Motivo"], /Capitolo 99/i],
    [["reopen", "VOL-08", "--step", "24", "--module", "M-TR01", "--cascade", "--note", "Motivo"], /24|conferma/i]
  ])("rejects an invalid audited reopen request", async (argv, message) => {
    await expect(runCommand(parseArgs(argv))).rejects.toThrow(message)
  })
})

async function writeFixture(root: string) {
  const planning = path.join(root, "wiki", "books", "vol-08-fixture", "planning")
  await mkdir(planning, { recursive: true })
  await writeFile(
    path.join(planning, "00-scheda-pipeline.md"),
    `---\nvolume_code: VOL-08\nvolume_title: Fixture reopen\ncut_off_date: 2026-08-05\nwriter_provider: codex\nphases: [C, D, F]\n---\n\n# Scheda\n\n## Moduli\n\n| Codice | Module id | PrioritÃ  | Fasi |\n| --- | --- | --- | --- |\n| M-TR01 | ${moduleId} | 1 | C,D,F |\n\n## Capitoli M-TR01\n\n| # | File | Matrice | Stato atteso | Note |\n| --- | --- | --- | --- | --- |\n| 01 | chapters/01-ruoli-ict.md | planning/matrice.md | completo | fixture |\n| 02 | chapters/02-cybersecurity.md | planning/matrice.md | completo | fixture |\n`,
    "utf8"
  )

  const state = completedState()
  await saveRunState(root, state)
  await mkdir(path.join(root, "pipeline", "VOL-99"), { recursive: true })
  await writeFile(path.join(root, "pipeline", "VOL-99", "run-state.json"), '{"sentinel":true}\n', "utf8")
}

async function readState(volumeCode: string) {
  return JSON.parse(await readFile(path.join(fixtureRoot, "pipeline", volumeCode, "run-state.json"), "utf8")) as RunState
}

function completedState() {
  const drafts: Array<Omit<StepRecord, "status" | "attempts" | "evidence">> = [
    draft("08", "C", "chapter", chapterOne),
    draft("09", "C", "chapter", chapterOne),
    draft("08", "C", "chapter", chapterTwo),
    draft("09", "C", "chapter", chapterTwo),
    draft("13", "D", "module", moduleId),
    draft("24", "F", "volume", "VOL-08")
  ]
  const initial = createRunState({ volumeCode: "VOL-08", specPath: "fixture", specHash: "sha256:fixture", steps: drafts, now })

  return {
    ...initial,
    steps: initial.steps.map((step) =>
      step.id === "24"
        ? step
        : { ...step, status: "done" as const, attempts: 1, evidence: ["complete.json"], owner: "tester", agent: "vitest", finishedAt: now }
    )
  }
}

function draft(id: string, phase: string, scope: StepRecord["scope"], target: string): Omit<StepRecord, "status" | "attempts" | "evidence"> {
  return { key: stepKey(id, target), id, phase, scope, target }
}
