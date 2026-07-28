import { describe, expect, it } from "vitest"
import { runMergeDriver } from "../../src/pipeline/state/merge-driver"
import { completeStep, createRunState, startStep, stepKey } from "../../src/pipeline/state/run-state"
import type { RunState } from "../../src/pipeline/state/types"

const now = "2026-07-27T15:08:27.185Z"
const later = "2026-07-27T15:31:04.902Z"
const chapterA = "moduli/m-fc02-agenzie-fiscali/chapters/01-perimetro.md"
const chapterB = "moduli/m-fc02-agenzie-fiscali/chapters/02-tributi.md"

const base = () =>
  createRunState({
    volumeCode: "VOL-03",
    specPath: "wiki/books/volumi/vol-03/planning/00-scheda-pipeline.md",
    specHash: "sha256:abc",
    steps: [
      { key: stepKey("08", chapterA), id: "08", phase: "C", scope: "chapter", target: chapterA },
      { key: stepKey("08", chapterB), id: "08", phase: "C", scope: "chapter", target: chapterB }
    ],
    now
  })

const serialize = (state: RunState) => `${JSON.stringify(state, null, 2)}\n`
const baseContent = () => serialize(base())

describe("runMergeDriver", () => {
  it("merges cleanly when two people work different chapters of the same volume", () => {
    const ours = startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now })
    const theirs = startStep(base(), stepKey("08", chapterB), { owner: "bruno", agent: "claude-code", now })

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.ok).toBe(true)
    expect(result.conflicts).toEqual([])
    const merged = JSON.parse(result.output) as RunState
    expect(merged.steps.find((s) => s.target === chapterA)?.owner).toBe("alice")
    expect(merged.steps.find((s) => s.target === chapterB)?.owner).toBe("bruno")
  })

  it("does not lose either person's progress on a clean merge", () => {
    const ours = completeStep(startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now }), stepKey("08", chapterA), {
      gate: { passed: true, blockers: [], warnings: [] },
      now: later
    })
    const theirs = completeStep(startStep(base(), stepKey("08", chapterB), { owner: "bruno", agent: "claude-code", now }), stepKey("08", chapterB), {
      gate: { passed: true, blockers: [], warnings: [] },
      now: later
    })

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })
    const merged = JSON.parse(result.output) as RunState

    expect(merged.steps.every((s) => s.status === "done")).toBe(true)
  })

  it("does NOT flag a conflict when the other side simply carried the common ancestor forward untouched", () => {
    const claimed = startStep(base(), stepKey("08", chapterA), { owner: "alber", agent: "codex-cli", now })
    const ours = startStep(claimed, stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now: later, force: true })
    const theirs = claimed // bruno's branch never touched this step again after the shared ancestor

    const result = runMergeDriver({ baseContent: serialize(claimed), oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.ok).toBe(true)
    expect(result.conflicts).toEqual([])
    const merged = JSON.parse(result.output) as RunState
    expect(merged.steps.find((s) => s.target === chapterA)?.owner).toBe("alice")
  })

  it("fails with visible git-style conflict markers when two people claim the same chapter", () => {
    const ours = startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now })
    const theirs = startStep(base(), stepKey("08", chapterA), { owner: "bruno", agent: "claude-code", now })

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.ok).toBe(false)
    expect(result.output).toContain("<<<<<<< HEAD")
    expect(result.output).toContain("=======")
    expect(result.output).toContain(">>>>>>> incoming")
    expect(result.conflicts).toHaveLength(1)
  })

  it("names the conflicting step and both owners in the diagnostic, not just in the raw JSON", () => {
    const ours = startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now })
    const theirs = startStep(base(), stepKey("08", chapterA), { owner: "bruno", agent: "claude-code", now })

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.diagnostic).toContain("alice")
    expect(result.diagnostic).toContain("bruno")
    expect(result.diagnostic).toContain(chapterA)
  })

  it("still produces valid JSON on each side of the conflict markers, for manual resolution", () => {
    const ours = startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now })
    const theirs = completeStep(startStep(base(), stepKey("08", chapterA), { owner: "bruno", agent: "claude-code", now }), stepKey("08", chapterA), {
      gate: { passed: false, blockers: [{ code: "x", message: "y" }], warnings: [] },
      now: later
    })

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })
    const [oursBlock, theirsBlock] = result.output.split("=======").map((part) => part.replace(/^<<<<<<< HEAD\n|\n>>>>>>> incoming\n?$/g, ""))

    expect(() => JSON.parse(oursBlock)).not.toThrow()
    expect(() => JSON.parse(theirsBlock)).not.toThrow()
  })

  it("refuses to merge run-states from two different volumes instead of guessing", () => {
    const ours = base()
    const theirs = { ...base(), volumeCode: "VOL-09" }

    const result = runMergeDriver({ baseContent: baseContent(), oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.ok).toBe(false)
    expect(result.diagnostic).toContain("VOL-09")
  })

  it("reports an unreadable side as a hard failure rather than silently keeping one version", () => {
    const result = runMergeDriver({ baseContent: baseContent(), oursContent: "{ not json", theirsContent: serialize(base()) })

    expect(result.ok).toBe(false)
    expect(result.diagnostic).toMatch(/illeggibile|non valido/i)
  })

  it("treats a missing base as no prior history, instead of failing, when the file is new on both sides", () => {
    const ours = startStep(base(), stepKey("08", chapterA), { owner: "alice", agent: "codex-cli", now })
    const theirs = startStep(base(), stepKey("08", chapterB), { owner: "bruno", agent: "claude-code", now })

    const result = runMergeDriver({ baseContent: "", oursContent: serialize(ours), theirsContent: serialize(theirs) })

    expect(result.ok).toBe(true)
    expect(result.conflicts).toEqual([])
  })
})
