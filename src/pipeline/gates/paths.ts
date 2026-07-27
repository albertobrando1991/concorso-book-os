import path from "node:path"
import type { StepRecord } from "../state/types"

export function slugOf(target: string) {
  return (
    target
      .replace(/[^a-z0-9]+/gi, "-")
      .replace(/^-+|-+$/g, "")
      .toLowerCase() || "volume"
  )
}

export function chapterFileOf(wikiRoot: string, target: string) {
  return path.join(wikiRoot, "books", ...target.split("/"))
}

export function artifactDirectoryOf(projectRoot: string, volumeCode: string, step: StepRecord) {
  return path.join(projectRoot, "artifacts", "pipeline", volumeCode.toUpperCase(), step.id, slugOf(step.target))
}

export function snapshotPathOf(projectRoot: string, volumeCode: string, step: StepRecord) {
  return path.join(artifactDirectoryOf(projectRoot, volumeCode, step), "before.md")
}

export function reportRelativePathOf(volumeCode: string, step: StepRecord) {
  return `reviews/pipeline/${volumeCode.toUpperCase()}/${step.id}-${slugOf(step.target)}.md`
}

export function reportPathOf(wikiRoot: string, volumeCode: string, step: StepRecord) {
  return path.join(wikiRoot, ...reportRelativePathOf(volumeCode, step).split("/"))
}
