import { execFileSync } from "node:child_process"
import fs from "node:fs"
import path from "node:path"
import { describe, expect, it } from "vitest"

interface PipelineStep {
  key: string
  id: string
  target: string
  status: string
}

interface PipelineState {
  steps: PipelineStep[]
}

const repoRoot = process.cwd()
const runStatePath = path.join(repoRoot, "pipeline", "VOL-07", "run-state.json")

const volumeOutputs: Record<string, string> = {
  "01": "wiki/reviews/pipeline/VOL-07/01-censimento-lavoro-staff.md",
  "02": "wiki/reviews/pipeline/VOL-07/02-consolidamento-contributi.md",
  "03": "wiki/reviews/pipeline/VOL-07/03-riconciliazione-catalogo.md",
  "04": "wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/04-bibbia-del-volume.md"
}

describe("VOL-07 completed pipeline artifacts", () => {
  it("keeps every expected output for completed steps 01-07 present and tracked", () => {
    const state = JSON.parse(fs.readFileSync(runStatePath, "utf8")) as PipelineState
    const completedSteps = state.steps.filter(
      (step) => step.status === "done" && Number(step.id) >= 1 && Number(step.id) <= 7
    )
    const artifactPaths = completedSteps.map(expectedArtifactPath)
    const trackedPaths = new Set(
      execFileSync("git", ["ls-files", "-z"], {
        cwd: repoRoot,
        encoding: "utf8"
      })
        .split("\0")
        .filter(Boolean)
    )

    expect(completedSteps.length).toBeGreaterThan(0)
    expect(artifactPaths).toHaveLength(completedSteps.length)
    expect(
      artifactPaths.filter((artifactPath) => !fs.existsSync(path.join(repoRoot, artifactPath)))
    ).toEqual([])
    expect(artifactPaths.filter((artifactPath) => !trackedPaths.has(artifactPath))).toEqual([])
  })
})

function expectedArtifactPath(step: PipelineStep) {
  const volumeOutput = volumeOutputs[step.id]

  if (volumeOutput) return volumeOutput

  const moduleCode = step.target.match(/(?:^|\/)(m-sa\d+)(?:-|$)/i)?.[1]?.toLowerCase()

  if (!moduleCode) {
    throw new Error(`Nessun modulo risolvibile per lo step completato ${step.key}`)
  }

  if (step.id === "05") {
    return `wiki/reviews/pipeline/VOL-07/05-audit-bandi-${moduleCode}.md`
  }

  if (step.id === "06") {
    return `wiki/reviews/pipeline/VOL-07/06-audit-fonti-${moduleCode}.md`
  }

  if (step.id === "07") {
    return `wiki/books/${step.target}/planning/02-matrice-copertura-didattica.md`
  }

  throw new Error(`Nessun output atteso per lo step completato ${step.key}`)
}
