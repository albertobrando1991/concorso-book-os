import type { VolumeSpec, VolumeSpecModule } from "../spec/parse-volume-spec"
import { stepKey, type StepDraft } from "../state/run-state"
import { STEP_REGISTRY, type StepDefinition } from "./registry"

export function buildStepDrafts(spec: VolumeSpec, phases: string[]): StepDraft[] {
  const wanted = new Set(phases.map((phase) => phase.trim().toUpperCase()).filter(Boolean))

  if (!wanted.size) return []

  const selected = STEP_REGISTRY.filter((step) => wanted.has(step.phase))
  const modules = [...spec.modules].sort((left, right) => left.priority - right.priority)
  return groupByScope(selected).flatMap((steps) =>
    isGlobal(steps[0]) ? volumeSteps(steps, spec) : modules.flatMap((module) => moduleSteps(steps, module, wanted))
  )
}

function groupByScope(steps: StepDefinition[]) {
  return steps.reduce<StepDefinition[][]>((groups, step) => {
    const last = groups.at(-1)

    if (!last || isGlobal(last[0]) !== isGlobal(step)) groups.push([step])
    else last.push(step)

    return groups
  }, [])
}

function isGlobal(step: StepDefinition) {
  return step.scope === "volume" || step.scope === "catalog"
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

  const scopeGroups = steps.reduce<StepDefinition[][]>((groups, step) => {
    const last = groups.at(-1)

    if (!last || last[0].scope !== step.scope) groups.push([step])
    else last.push(step)

    return groups
  }, [])

  return scopeGroups.flatMap((group) =>
    group[0].scope === "chapter"
      ? module.chapters.flatMap((chapter) =>
          group.map((step) => draft(step, `${module.moduleId}/${chapter.file}`))
        )
      : group.map((step) => draft(step, module.moduleId))
  )
}

function volumeSteps(selected: StepDefinition[], spec: VolumeSpec): StepDraft[] {
  return selected
    .filter((step) => step.scope === "volume" || step.scope === "catalog")
    .map((step) => draft(step, spec.volumeCode))
}

function draft(step: StepDefinition, target: string): StepDraft {
  return { key: stepKey(step.id, target), id: step.id, phase: step.phase, scope: step.scope, target }
}
