import type { VolumeSpec, VolumeSpecModule } from "../spec/parse-volume-spec"
import { stepKey, type StepDraft } from "../state/run-state"
import { STEP_REGISTRY, type StepDefinition } from "./registry"

export function buildStepDrafts(spec: VolumeSpec, phases: string[]): StepDraft[] {
  const wanted = new Set(phases.map((phase) => phase.trim().toUpperCase()).filter(Boolean))

  if (!wanted.size) return []

  const selected = STEP_REGISTRY.filter((step) => wanted.has(step.phase))
  const modules = [...spec.modules].sort((left, right) => left.priority - right.priority)

  return [...modules.flatMap((module) => moduleSteps(selected, module, wanted)), ...volumeSteps(selected, spec)]
}

function moduleSteps(selected: StepDefinition[], module: VolumeSpecModule, wanted: Set<string>): StepDraft[] {
  const declared = new Set(module.phases.map((phase) => phase.trim().toUpperCase()))
  const phases = [...wanted].filter((phase) => declared.has(phase))
  const steps = selected.filter((step) => phases.includes(step.phase))
  const chapterSteps = steps.filter((step) => step.scope === "chapter")

  if (chapterSteps.length && !module.chapters.length) {
    throw new Error(
      `Il modulo ${module.code} non dichiara capitoli: aggiungi la tabella "## Capitoli ${module.code}" alla scheda oppure lascia che "pipeline init" li derivi da ${module.moduleId}/chapters.`
    )
  }

  const perChapter = module.chapters.flatMap((chapter) =>
    chapterSteps.map((step) => draft(step, `${module.moduleId}/${chapter.file}`))
  )
  const perModule = steps.filter((step) => step.scope === "module").map((step) => draft(step, module.moduleId))

  return [...perChapter, ...perModule]
}

function volumeSteps(selected: StepDefinition[], spec: VolumeSpec): StepDraft[] {
  return selected
    .filter((step) => step.scope === "volume" || step.scope === "catalog")
    .map((step) => draft(step, spec.volumeCode))
}

function draft(step: StepDefinition, target: string): StepDraft {
  return { key: stepKey(step.id, target), id: step.id, phase: step.phase, scope: step.scope, target }
}
