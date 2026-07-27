import { mkdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"
import { getProjectRoot, getWikiRoot } from "../../server/config"
import { detectAgent, detectOwner } from "../env/detect-agent"
import { runDoctor } from "../env/doctor"
import { runGate } from "../gates"
import { chapterFileOf, reportRelativePathOf, snapshotPathOf } from "../gates/paths"
import { loadVolumeSpec } from "../spec/load-volume-spec"
import type { VolumeSpec } from "../spec/parse-volume-spec"
import { completeStep, createRunState, nextStep, startStep } from "../state/run-state"
import { loadRunState, saveRunState } from "../state/run-state-store"
import type { GateResult, RunState, StepRecord } from "../state/types"
import { buildStepDrafts } from "../steps/build-steps"
import { loadPromptCatalog, PROMPT_TEMPLATE_PATH, renderPrompt, type PromptCatalog } from "../steps/prompt-renderer"
import { requireStepDefinition } from "../steps/registry"
import type { ParsedArgs } from "./args"

export interface CommandResult {
  exitCode: number
  payload: Record<string, unknown>
  lines: string[]
}

interface Context {
  projectRoot: string
  wikiRoot: string
  args: ParsedArgs
  now: string
}

export async function runCommand(args: ParsedArgs): Promise<CommandResult> {
  const context: Context = { projectRoot: getProjectRoot(), wikiRoot: getWikiRoot(), args, now: new Date().toISOString() }

  if (args.command === "help") return help()
  if (args.command === "doctor") return doctor(context)

  if (!args.volumeCode) {
    throw new Error(
      `Il comando "${args.command}" richiede il codice del volume, per esempio: npm run pipeline -- ${args.command} VOL-03.`
    )
  }

  if (args.command === "init") return init(context)
  if (args.command === "status") return status(context)
  if (args.command === "next") return next(context)
  if (args.command === "gate") return gate(context)
  if (args.command === "complete") return complete(context)
  if (args.command === "sync") return sync(context)

  throw new Error(`Comando "${args.command}" non ancora implementato in questa versione della pipeline.`)
}

async function doctor(context: Context): Promise<CommandResult> {
  const checks = await runDoctor({ projectRoot: context.projectRoot })
  const failed = checks.filter((check) => !check.ok)

  return {
    exitCode: failed.length ? 1 : 0,
    payload: { ok: !failed.length, command: "doctor", checks },
    lines: [
      "Diagnosi ambiente pipeline",
      ...checks.flatMap((check) => [`  [${check.ok ? "ok" : "KO"}] ${check.id}: ${check.message}`, ...(check.remedy ? [`        rimedio: ${check.remedy}`] : [])]),
      failed.length
        ? `${failed.length} ${failed.length === 1 ? "controllo da sistemare" : "controlli da sistemare"} prima di eseguire la pipeline.`
        : "Ambiente pronto."
    ]
  }
}

async function init(context: Context): Promise<CommandResult> {
  const loaded = await loadVolumeSpec({ wikiRoot: context.wikiRoot, volumeCode: context.args.volumeCode })

  if (loaded.issues.length) {
    return {
      exitCode: 1,
      payload: { ok: false, command: "init", specFile: loaded.specFile, issues: loaded.issues },
      lines: [
        `Scheda non valida: ${loaded.specFile}`,
        ...loaded.issues.map((issue) => `  ${issue.field}${issue.line ? ` (riga ${issue.line})` : ""}: ${issue.message}`)
      ]
    }
  }

  const phases = context.args.phase ? context.args.phase.split(",") : loaded.spec.phases
  const existing = await loadRunState(context.projectRoot, loaded.spec.volumeCode)
  const fresh = createRunState({
    volumeCode: loaded.spec.volumeCode,
    specPath: loaded.spec.specPath,
    specHash: loaded.specHash,
    steps: buildStepDrafts(loaded.spec, phases),
    now: context.now
  })
  const state = existing ? reproject(fresh, existing) : fresh
  const file = await saveRunState(context.projectRoot, state)
  const dropped = existing ? existing.steps.filter((step) => !state.steps.some((current) => current.key === step.key)).length : 0

  return {
    exitCode: 0,
    payload: { ok: true, command: "init", specFile: loaded.specFile, runState: file, steps: state.steps.length, phases, dropped },
    lines: [
      `Volume ${state.volumeCode} — scheda ${loaded.spec.specPath}`,
      `Fasi: ${phases.join(", ")} — step pianificati: ${state.steps.length}`,
      existing ? `Stato precedente conservato; step non più previsti rimossi: ${dropped}` : "Run-state creato da zero",
      `Run-state: ${path.relative(context.projectRoot, file)}`
    ]
  }
}

async function status(context: Context): Promise<CommandResult> {
  const state = await requireRunState(context)
  const counts = state.steps.reduce<Record<string, number>>(
    (totals, step) => ({ ...totals, [step.status]: (totals[step.status] ?? 0) + 1 }),
    {}
  )
  const blocked = state.steps.filter((step) => step.status === "blocked")
  const held = state.steps.filter((step) => step.status === "in-progress")
  const upcoming = nextStep(state, { phase: context.args.phase })

  return {
    exitCode: blocked.length ? 1 : 0,
    payload: {
      ok: !blocked.length,
      command: "status",
      volumeCode: state.volumeCode,
      counts,
      blocked,
      inProgress: held,
      next: upcoming ?? null
    },
    lines: [
      `Volume ${state.volumeCode} — ${state.steps.length} step`,
      ...Object.entries(counts).map(([key, value]) => `  ${key}: ${value}`),
      ...held.map((step) => `In carico a ${step.owner ?? "?"} (${step.agent ?? "?"}): step ${step.id} su ${step.target}`),
      ...blocked.flatMap((step) => [
        `Bloccato: step ${step.id} su ${step.target}`,
        ...(step.gate?.blockers ?? []).map((issue) => `    ${issue.message}`)
      ]),
      upcoming ? `Prossimo: step ${upcoming.id} su ${upcoming.target}` : "Nessuno step residuo nel perimetro richiesto"
    ]
  }
}

async function next(context: Context): Promise<CommandResult> {
  const { state, spec } = await load(context)
  const step = selectStep(state, context)

  if (!step) {
    return {
      exitCode: 0,
      payload: { ok: true, command: "next", step: null },
      lines: ["Nessuno step residuo nel perimetro richiesto."]
    }
  }

  const definition = requireStepDefinition(step.id)
  const catalog = await promptCatalog(context)
  const rendered = renderPrompt(catalog, step.id, promptValues(spec, step))
  const contract = deliveryContract(context, spec, step, definition.gate)
  const prompt = `${contract}\n\n---\n\n${rendered}`
  const promptFile = await writePrompt(context, step, prompt)
  const snapshot = await writeSnapshot(context, spec, step, definition.gate)
  const claimed = startStep(state, step.key, {
    owner: context.args.owner || detectOwner(),
    agent: detectAgent(),
    provider: context.args.provider || spec.writerProvider,
    now: context.now,
    force: context.args.force
  })
  await saveRunState(context.projectRoot, claimed)
  const chapterNumber = chapterNumberOf(spec, step)

  return {
    exitCode: 0,
    payload: {
      ok: true,
      command: "next",
      step: { ...step, status: "in-progress" },
      definition,
      promptFile: path.relative(context.projectRoot, promptFile),
      gate: definition.gate ?? null,
      prompt
    },
    lines: [
      `Step ${step.id} — ${definition.title}`,
      `Target: ${step.target}`,
      `Tipo: ${definition.kind} (${definition.automation}) — gate: ${definition.gate ?? "nessuno"}`,
      `Prompt: ${path.relative(context.projectRoot, promptFile)}`,
      ...(snapshot ? [`Snapshot pre-Humanizer: ${path.relative(context.projectRoot, snapshot)}`] : []),
      `Al termine: npm run pipeline -- complete ${state.volumeCode} --step ${step.id}${chapterNumber ? ` --chapter ${chapterNumber}` : ""}`
    ]
  }
}

async function gate(context: Context): Promise<CommandResult> {
  const { state, spec } = await load(context)
  const step = requireTargetStep(state, context)
  const definition = requireStepDefinition(step.id)
  const result = await runGate(definition.gate, gateContext(spec, step, context))

  return {
    exitCode: result.passed ? 0 : 1,
    payload: { ok: result.passed, command: "gate", step: step.key, gate: definition.gate ?? null, result },
    lines: gateLines(step, result)
  }
}

async function complete(context: Context): Promise<CommandResult> {
  const { state, spec } = await load(context)
  const step = requireTargetStep(state, context)
  const definition = requireStepDefinition(step.id)
  const evaluated = await runGate(definition.gate, gateContext(spec, step, context))
  const result = context.args.accept ? accepted(evaluated, context) : evaluated
  const updated = completeStep(state, step.key, { gate: result, now: context.now })
  await saveRunState(context.projectRoot, updated)
  const following = nextStep(updated, { phase: context.args.phase })

  return {
    exitCode: result.passed ? 0 : 1,
    payload: { ok: result.passed, command: "complete", step: step.key, result, next: result.passed ? (following ?? null) : null },
    lines: [
      ...gateLines(step, result),
      result.passed
        ? following
          ? `Prossimo: step ${following.id} su ${following.target}`
          : "Perimetro completato."
        : "Pipeline ferma: risolvi i blocker e ripeti lo step."
    ]
  }
}

async function sync(context: Context): Promise<CommandResult> {
  const loaded = await loadVolumeSpec({ wikiRoot: context.wikiRoot, volumeCode: context.args.volumeCode })
  const existing = await requireRunState(context)
  const phases = context.args.phase ? context.args.phase.split(",") : loaded.spec.phases
  const fresh = createRunState({
    volumeCode: loaded.spec.volumeCode,
    specPath: loaded.spec.specPath,
    specHash: loaded.specHash,
    steps: buildStepDrafts(loaded.spec, phases),
    now: context.now
  })
  const state = reproject(fresh, existing)
  const added = state.steps.filter((step) => !existing.steps.some((current) => current.key === step.key))
  const dropped = existing.steps.filter((step) => !state.steps.some((current) => current.key === step.key))
  const specChanged = existing.specHash !== loaded.specHash
  await saveRunState(context.projectRoot, state)

  return {
    exitCode: 0,
    payload: { ok: true, command: "sync", added: added.map((step) => step.key), dropped: dropped.map((step) => step.key), specChanged },
    lines: [
      specChanged ? "La scheda è cambiata rispetto all'ultimo run-state." : "Scheda invariata.",
      `Step aggiunti: ${added.length}`,
      `Step non più previsti e rimossi: ${dropped.length}`,
      ...dropped
        .filter((step) => step.status !== "pending")
        .map((step) => `  attenzione: lo step ${step.id} su ${step.target} era in stato ${step.status}`)
    ]
  }
}

function help(): CommandResult {
  return {
    exitCode: 0,
    payload: { ok: true, command: "help" },
    lines: [
      "Pipeline editoriale ConcorsoBook OS",
      "",
      "  pipeline doctor                          diagnosi dell'ambiente dopo il clone",
      "  pipeline init VOL-03 [--phase C,D,F]     valida la scheda e crea il run-state",
      "  pipeline status VOL-03                   avanzamento, blocchi e proprietari",
      "  pipeline next VOL-03 [--chapter 01]      step successivo e prompt renderizzato",
      "  pipeline gate VOL-03 --step 10           esegue il gate senza chiudere lo step",
      "  pipeline complete VOL-03 --step 09       chiude lo step se il gate passa",
      "  pipeline sync VOL-03                     riallinea il run-state alla scheda",
      "",
      "  --json      output strutturato per gli agenti",
      "  --force     subentra a uno step in carico ad altri",
      "  --accept    chiude uno step il cui gate non è automatizzato (richiede --note)",
      "",
      `Prompt canonici: ${PROMPT_TEMPLATE_PATH}`
    ]
  }
}

async function load(context: Context) {
  const loaded = await loadVolumeSpec({ wikiRoot: context.wikiRoot, volumeCode: context.args.volumeCode })

  return { spec: loaded.spec, state: await requireRunState(context), specHash: loaded.specHash }
}

async function requireRunState(context: Context): Promise<RunState> {
  const state = await loadRunState(context.projectRoot, context.args.volumeCode.toUpperCase())

  if (!state) {
    throw new Error(`Nessun run-state per ${context.args.volumeCode}: esegui prima "npm run pipeline -- init ${context.args.volumeCode}".`)
  }

  return state
}

function reproject(fresh: RunState, existing: RunState): RunState {
  const previous = new Map(existing.steps.map((step) => [step.key, step]))

  return { ...fresh, createdAt: existing.createdAt, steps: fresh.steps.map((step) => previous.get(step.key) ?? step) }
}

function selectStep(state: RunState, context: Context) {
  if (context.args.step) return requireTargetStep(state, context)

  return nextStep(state, { phase: context.args.phase, from: context.args.from, target: targetFilter(state, context) })
}

function requireTargetStep(state: RunState, context: Context): StepRecord {
  if (!context.args.step) {
    const upcoming = nextStep(state, { phase: context.args.phase, target: targetFilter(state, context) })

    if (!upcoming) throw new Error('Nessuno step da valutare: indica --step oppure verifica lo stato con "pipeline status".')

    return upcoming
  }

  const filtered = state.steps.filter((step) => step.id === context.args.step && matchesFilters(step, context))

  if (!filtered.length) {
    throw new Error(
      `Step ${context.args.step}${describeFilters(context)} non presente nel run-state di ${state.volumeCode}.`
    )
  }

  if (filtered.length > 1) {
    throw new Error(
      `Lo step ${context.args.step} esiste per più target: precisa --module (o --chapter) fra ${filtered.map((step) => step.target).join(", ")}.`
    )
  }

  return filtered[0]
}

function matchesFilters(step: StepRecord, context: Context) {
  const { chapter, module } = context.args

  if (chapter && !matchesChapter(step, chapter)) return false
  if (module && !matchesModule(step, module)) return false

  return true
}

function describeFilters(context: Context) {
  const parts = [context.args.module ? `del modulo ${context.args.module}` : "", context.args.chapter ? `per il capitolo ${context.args.chapter}` : ""]

  return parts.filter(Boolean).length ? ` ${parts.filter(Boolean).join(" ")}` : ""
}

function matchesChapter(step: StepRecord, chapter: string) {
  return step.target.includes(`/chapters/${chapter}-`) || step.target.endsWith(`/chapters/${chapter}.md`)
}

function matchesModule(step: StepRecord, module: string) {
  return step.target.toLowerCase().includes(module.trim().toLowerCase())
}

function targetFilter(state: RunState, context: Context) {
  if (!context.args.chapter && !context.args.module) return undefined

  return state.steps.find((step) => matchesFilters(step, context))?.target
}

function moduleOf(spec: VolumeSpec, step: StepRecord) {
  return spec.modules.find((module) => step.target === module.moduleId || step.target.startsWith(`${module.moduleId}/`))
}

function chapterNumberOf(spec: VolumeSpec, step: StepRecord) {
  const module = moduleOf(spec, step)

  if (!module || step.scope !== "chapter") return undefined

  const file = step.target.slice(module.moduleId.length + 1)

  return module.chapters.find((chapter) => chapter.file === file)?.number
}

function gateContext(spec: VolumeSpec, step: StepRecord, context: Context) {
  return {
    wikiRoot: context.wikiRoot,
    projectRoot: context.projectRoot,
    spec,
    step,
    module: moduleOf(spec, step),
    chapterNumber: chapterNumberOf(spec, step)
  }
}

function promptValues(spec: VolumeSpec, step: StepRecord) {
  const module = moduleOf(spec, step)

  return {
    VOLUME_CODE: spec.volumeCode,
    VOLUME_TITLE: spec.volumeTitle,
    CUT_OFF_DATE: spec.cutOffDate,
    RESPONSABILE: spec.responsabileNormativo,
    MODULE_CODE: module?.code ?? "",
    MODULE_ID: module?.moduleId ?? "",
    CHAPTER_FILE: step.scope === "chapter" ? `wiki/books/${step.target}` : "",
    CHAPTER_NUMBER: chapterNumberOf(spec, step) ?? ""
  }
}

async function promptCatalog(context: Context): Promise<PromptCatalog> {
  const file = path.join(context.projectRoot, ...PROMPT_TEMPLATE_PATH.split("/"))

  return loadPromptCatalog(await readFile(file, "utf8"))
}

async function writePrompt(context: Context, step: StepRecord, prompt: string) {
  const directory = path.join(
    context.projectRoot,
    "artifacts",
    "pipeline",
    context.args.volumeCode.toUpperCase(),
    step.id,
    slug(step.target)
  )
  await mkdir(directory, { recursive: true })
  const file = path.join(directory, "prompt.md")
  await writeFile(file, `${prompt}\n`, "utf8")

  return file
}

function deliveryContract(context: Context, spec: VolumeSpec, step: StepRecord, gate: string | undefined) {
  const chapterNumber = chapterNumberOf(spec, step)
  const closing = `npm run pipeline -- complete ${spec.volumeCode} --step ${step.id}${moduleOf(spec, step) ? ` --module ${moduleOf(spec, step)?.code}` : ""}${chapterNumber ? ` --chapter ${chapterNumber}` : ""}`

  return [
    "<!-- Contratto di esecuzione aggiunto dalla pipeline. Non fa parte del prompt canonico. -->",
    `> **Step ${step.id}** su \`${step.target}\` — gate: \`${gate ?? "nessuno"}\``,
    ...(gate === "review-report"
      ? [`> Scrivi il report nel template fisso del Revisore Editoriale Totale in \`wiki/${reportRelativePathOf(spec.volumeCode, step)}\`.`]
      : []),
    ...(gate === "chapter-lint" ? ["> Il capitolo deve avere un solo H1, frontmatter veritiero con `source_refs` e `draft_stage`, nessun segnaposto e nessun meta-commento."] : []),
    ...(gate === "citation-guard"
      ? ["> Wikilink, `source_refs` e riferimenti normativi devono restare identici a prima dell'Humanizer: la pipeline ne ha salvato lo snapshot."]
      : []),
    ...(gate === "coverage" ? ["> Il gate valuta le righe della matrice collocate in questo capitolo: nessuno stato `parziale`, `solo-nominato` o `mancante`."] : []),
    `> Al termine: \`${closing}\``
  ].join("\n")
}

async function writeSnapshot(context: Context, spec: VolumeSpec, step: StepRecord, gate: string | undefined) {
  if (gate !== "citation-guard") return null

  const source = chapterFileOf(context.wikiRoot, step.target)
  const content = await readFile(source, "utf8").catch(() => null)

  if (content === null) return null

  const file = snapshotPathOf(context.projectRoot, spec.volumeCode, step)
  await mkdir(path.dirname(file), { recursive: true })
  await writeFile(file, content, "utf8")

  return file
}

function accepted(result: GateResult, context: Context): GateResult {
  if (!context.args.note?.trim()) {
    throw new Error("--accept richiede --note con la motivazione della chiusura manuale: un gate non automatizzato va giustificato.")
  }

  return {
    passed: true,
    blockers: [],
    warnings: [
      ...result.warnings,
      ...result.blockers.map((issue) => ({ ...issue, code: `accepted:${issue.code}` })),
      { code: "manual-acceptance", message: `Chiusura manuale di ${detectOwner()}: ${context.args.note.trim()}` }
    ],
    notImplemented: result.notImplemented
  }
}

function gateLines(step: StepRecord, result: GateResult) {
  return [
    `Step ${step.id} su ${step.target}: gate ${result.passed ? "superato" : "non superato"}`,
    ...result.blockers.map((issue) => `  blocker [${issue.code}] ${issue.message}`),
    ...result.warnings.map((issue) => `  warning [${issue.code}] ${issue.message}`)
  ]
}

function slug(value: string) {
  return (
    value
      .replace(/[^a-z0-9]+/gi, "-")
      .replace(/^-+|-+$/g, "")
      .toLowerCase() || "volume"
  )
}
