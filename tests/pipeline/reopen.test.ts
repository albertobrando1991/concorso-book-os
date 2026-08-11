import { describe, expect, it } from "vitest"
import { parseArgs } from "../../src/pipeline/cli/args"
import { runCommand } from "../../src/pipeline/cli/commands"
import { reopenSteps } from "../../src/pipeline/state/run-state"
import type { RunState, StepRecord } from "../../src/pipeline/state/types"

describe("pipeline reopen arguments", () => {
  it("parses the volume, starting step, module, chapter and mandatory audit note", () => {
    expect(parseArgs([
      "reopen",
      "VOL-10",
      "--from-step",
      "08",
      "--module",
      "M-TR03",
      "--chapter",
      "01",
      "--note",
      "Retrofit formato 2"
    ])).toMatchObject({
      command: "reopen",
      volumeCode: "VOL-10",
      fromStep: "08",
      module: "M-TR03",
      chapter: "01",
      note: "Retrofit formato 2"
    })
  })

  it("rejects the command before loading state when the audit note is missing", async () => {
    await expect(runCommand(parseArgs([
      "reopen",
      "VOL-10",
      "--from-step",
      "08",
      "--module",
      "M-TR03"
    ]))).rejects.toThrow(/--note/)
  })
})

const done = (id: string, scope: StepRecord["scope"], target: string): StepRecord => ({
  key: `${id}:${target}`,
  id,
  phase: scope === "chapter" ? "C" : scope === "module" ? "D" : "F",
  scope,
  target,
  status: "done",
  attempts: 1,
  evidence: [`report-${id}.md`],
  owner: "editor",
  agent: "codex",
  startedAt: "2026-08-01T09:00:00.000Z",
  finishedAt: "2026-08-01T10:00:00.000Z",
  gate: { passed: true, blockers: [], warnings: [] }
})

describe("reopenSteps", () => {
  it("reopens one chapter and every dependent module and volume step without touching sibling chapters", () => {
    const moduleTarget = "moduli/m-tr03-tecnico-ingegneristico"
    const chapter01 = `${moduleTarget}/chapters/01-profilo.md`
    const chapter02 = `${moduleTarget}/chapters/02-ufficio.md`
    const state: RunState = {
      volumeCode: "VOL-10",
      specPath: "spec.md",
      specHash: "hash",
      createdAt: "2026-08-01T08:00:00.000Z",
      updatedAt: "2026-08-01T10:00:00.000Z",
      steps: [
        done("08", "chapter", chapter01),
        done("09", "chapter", chapter01),
        done("12", "chapter", chapter01),
        done("08", "chapter", chapter02),
        done("12", "chapter", chapter02),
        done("13", "module", moduleTarget),
        done("18", "module", moduleTarget),
        done("19", "volume", "VOL-10"),
        done("24", "volume", "VOL-10")
      ]
    }

    const reopened = reopenSteps(state, {
      fromStep: "08",
      moduleTarget,
      chapterTarget: chapter01,
      note: "Retrofit formato 2 capitolo 01",
      actor: "aless",
      now: "2026-08-11T10:30:00.000Z"
    })

    expect(reopened.steps.map(({ key, status }) => [key, status])).toEqual([
      [`08:${chapter01}`, "pending"],
      [`09:${chapter01}`, "pending"],
      [`12:${chapter01}`, "pending"],
      [`08:${chapter02}`, "done"],
      [`12:${chapter02}`, "done"],
      [`13:${moduleTarget}`, "pending"],
      [`18:${moduleTarget}`, "pending"],
      ["19:VOL-10", "pending"],
      ["24:VOL-10", "pending"]
    ])
    expect(reopened.steps[0]).not.toHaveProperty("owner")
    expect(reopened.steps[0].evidence).toEqual([])
    expect(reopened.reopenHistory).toEqual([{
      at: "2026-08-11T10:30:00.000Z",
      actor: "aless",
      note: "Retrofit formato 2 capitolo 01",
      fromStep: "08",
      moduleTarget,
      chapterTarget: chapter01,
      reopenedKeys: [
        `08:${chapter01}`,
        `09:${chapter01}`,
        `12:${chapter01}`,
        `13:${moduleTarget}`,
        `18:${moduleTarget}`,
        "19:VOL-10",
        "24:VOL-10"
      ]
    }])
  })

  it("rejects reopening without an audit note", () => {
    const state: RunState = {
      volumeCode: "VOL-10",
      specPath: "spec.md",
      specHash: "hash",
      createdAt: "2026-08-01T08:00:00.000Z",
      updatedAt: "2026-08-01T10:00:00.000Z",
      steps: []
    }

    expect(() => reopenSteps(state, {
      fromStep: "08",
      moduleTarget: "moduli/m-tr03-tecnico-ingegneristico",
      note: "",
      actor: "aless",
      now: "2026-08-11T10:30:00.000Z"
    })).toThrow(/note/i)
  })
})
