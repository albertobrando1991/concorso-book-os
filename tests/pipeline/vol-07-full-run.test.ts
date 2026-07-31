import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { parseVolumeSpec } from "../../src/pipeline/spec/parse-volume-spec"
import { buildStepDrafts } from "../../src/pipeline/steps/build-steps"

const specRelativePath =
  "books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md"
const specFile = path.resolve(process.cwd(), "wiki", specRelativePath)

async function loadSpec() {
  return parseVolumeSpec(await readFile(specFile, "utf8"), specRelativePath)
}

describe("VOL-07 full editorial run", () => {
  it("declares the approved 25-chapter manifest across all four modules", async () => {
    const spec = await loadSpec()

    expect(spec.phases).toEqual(["A", "B", "C", "D", "E", "F"])
    expect(spec.modules.map((module) => [module.code, module.chapters.length])).toEqual([
      ["M-SA02", 9],
      ["M-SA01", 5],
      ["M-SA03", 7],
      ["M-SA04", 4]
    ])
    expect(spec.modules.flatMap((module) => module.chapters)).toHaveLength(25)
  })

  it("builds every protocol phase without duplicate chapter targets", async () => {
    const spec = await loadSpec()
    const chapterSteps = buildStepDrafts(spec, ["C"])
    const writingTargets = chapterSteps
      .filter((step) => step.id === "09")
      .map((step) => step.target)

    expect(chapterSteps).toHaveLength(125)
    expect(writingTargets).toHaveLength(25)
    expect(new Set(writingTargets).size).toBe(25)
    expect(buildStepDrafts(spec, ["D"])).toHaveLength(16)
    expect(buildStepDrafts(spec, ["E"])).toHaveLength(7)
    expect(buildStepDrafts(spec, ["F"])).toHaveLength(3)
  })
})
