import {
  findTextVolumeForBookId,
  isSpecialistTextVolume,
  normalizeTextBookId
} from "../../catalog/text-volumes"
import { loadVolumeSpec, type LoadedVolumeSpec } from "../../pipeline/spec/load-volume-spec"
import { loadRunState } from "../../pipeline/state/run-state-store"
import { isTerminal, type StepRecord } from "../../pipeline/state/types"
import { findStepDefinition } from "../../pipeline/steps/registry"
import { FileWikiStore } from "../wiki/file-store"
import { parseFrontmatter } from "../wiki/frontmatter"

export type EditorialTargetState =
  | "to-plan"
  | "to-write"
  | "in-progress"
  | "written"
  | "in-review"
  | "complete"
  | "blocked"

export interface BookStudioEditorialTarget {
  number: string
  title: string
  path: string
  exists: boolean
  state: EditorialTargetState
  nextStep: string
  gate: string
}

export interface BookStudioEditorialModule {
  code: string
  title: string
  moduleId: string
  priority: number
  chaptersSource: "declared" | "derived"
  targets: BookStudioEditorialTarget[]
}

export interface BookStudioEditorialPlan {
  volumeCode: string
  updatedAt: string
  modules: BookStudioEditorialModule[]
}

export async function buildEditorialPlan(input: {
  store: FileWikiStore
  projectRoot: string
  bookId: string
}): Promise<BookStudioEditorialPlan | null> {
  const normalizedBookId = normalizeTextBookId(input.bookId)
  const volume = findTextVolumeForBookId(normalizedBookId)

  if (!volume || !isSpecialistTextVolume(volume)) return null

  const loaded = await loadSpecOrNull(input.store.getRoot(), volume.code)

  if (!loaded) return null

  const runState = await loadRunState(input.projectRoot, volume.code)
  const selectedModuleId = normalizedBookId.startsWith("moduli/") ? normalizedBookId : ""
  const modules = await Promise.all(
    loaded.spec.modules
      .filter((module) => !selectedModuleId || normalizeTextBookId(module.moduleId) === selectedModuleId)
      .sort((left, right) => left.priority - right.priority)
      .map(async (module): Promise<BookStudioEditorialModule> => {
        const indexPath = `books/${module.moduleId}/index.md`
        const moduleTitle = await readTitle(input.store, indexPath)
        const targets = await Promise.all(
          module.chapters.map(async (chapter): Promise<BookStudioEditorialTarget> => {
            const publicPath = `books/${module.moduleId}/${chapter.file}`
            const pipelineTarget = `${module.moduleId}/${chapter.file}`
            const exists = await input.store.exists(publicPath)
            const fileData = exists ? await readFrontmatter(input.store, publicPath) : {}
            const steps = runState?.steps.filter(
              (step) => step.scope === "chapter" && step.target === pipelineTarget
            ) ?? []
            const next = steps.find((step) => !isTerminal(step.status))

            return {
              number: chapter.number,
              title: String(fileData.title || chapter.title).trim(),
              path: publicPath,
              exists,
              state: targetState(steps, exists, String(fileData.status || "")),
              nextStep: next?.id || "",
              gate: next ? findStepDefinition(next.id)?.gate || "" : ""
            }
          })
        )

        targets.sort((left, right) => chapterRank(left.number) - chapterRank(right.number) || left.title.localeCompare(right.title, "it"))

        return {
          code: module.code,
          title: stripModuleCode(moduleTitle || module.code),
          moduleId: module.moduleId,
          priority: module.priority,
          chaptersSource: module.chaptersSource,
          targets
        }
      })
  )

  return {
    volumeCode: volume.code,
    updatedAt: runState?.updatedAt || new Date().toISOString(),
    modules
  }
}

async function loadSpecOrNull(wikiRoot: string, volumeCode: string): Promise<LoadedVolumeSpec | null> {
  try {
    return await loadVolumeSpec({ wikiRoot, volumeCode })
  } catch (error) {
    if ((error as Error).message.startsWith("Nessuna scheda di pipeline")) return null

    throw error
  }
}

async function readTitle(store: FileWikiStore, file: string) {
  const data = await readFrontmatter(store, file)

  return String(data.title || "")
}

async function readFrontmatter(store: FileWikiStore, file: string) {
  if (!(await store.exists(file))) return {} as Record<string, unknown>

  return parseFrontmatter(await store.readText(file)).data as Record<string, unknown>
}

function targetState(steps: StepRecord[], exists: boolean, fileStatus: string): EditorialTargetState {
  if (steps.some((step) => step.status === "blocked")) return "blocked"
  if (steps.length > 0 && steps.every((step) => isTerminal(step.status))) return "complete"
  if (steps.some((step) => step.id === "09" && step.status === "done")) return "in-review"
  if (steps.some((step) => ["in-progress", "awaiting-agent", "awaiting-human"].includes(step.status))) {
    return "in-progress"
  }
  if (steps.some((step) => step.id === "08" && step.status === "done")) return "to-write"
  if (exists && fileStatus !== "structure") return "written"

  return "to-plan"
}

function stripModuleCode(value: string) {
  return value.replace(/^M-[A-Z]{2}\d{2}\s*[-–—]\s*/i, "").trim()
}

function chapterRank(value: string) {
  const parsed = Number.parseInt(value, 10)

  return Number.isFinite(parsed) ? parsed : 999
}
