import { readFile } from "node:fs/promises"
import path from "node:path"
import type { VolumeSpec, VolumeSpecModule } from "../spec/parse-volume-spec"
import type { GateResult, StepRecord } from "../state/types"
import { runChapterLintGate } from "./chapter-lint-gate"
import { runCitationGuard } from "./citation-guard"
import { runCoverageGate } from "./coverage-gate"
import { analyzeDidacticDensity, runDidacticDensityGate } from "./didactic-density-gate"
import { chapterFileOf, reportPathOf, reportRelativePathOf, snapshotPathOf } from "./paths"
import { runReviewReportGate } from "./review-report-gate"
import { runVerifiedReferralGate } from "./verified-referral-gate"

export const DEFAULT_MATRIX_PATH = "planning/02-matrice-copertura-didattica.md"

export interface GateContext {
  wikiRoot: string
  projectRoot: string
  spec: VolumeSpec
  step: StepRecord
  module?: VolumeSpecModule
  chapterNumber?: string
}

export async function runGate(gateId: string | undefined, context: GateContext): Promise<GateResult> {
  if (!gateId) {
    return {
      passed: true,
      blockers: [],
      warnings: [{ code: "no-gate", message: `Lo step ${context.step.id} non prevede un gate automatico.` }]
    }
  }

  if (gateId === "coverage") return coverage(context)
  if (gateId === "didactic-density") return didacticDensity(context)
  if (gateId === "chapter-lint") return chapterLint(context)
  if (gateId === "citation-guard") return citationGuard(context)
  if (gateId === "review-report") return reviewReport(context)
  return notImplemented(gateId, context)
}

async function chapterLint(context: GateContext): Promise<GateResult> {
  const relative = `wiki/books/${context.step.target}`
  const content = await readOptional(chapterFileOf(context.wikiRoot, context.step.target))

  if (content === null) {
    return blocker("missing-chapter", `Capitolo assente: atteso ${relative}. Lo step 09 deve produrre il file.`, relative)
  }

  return runChapterLintGate({ content, chapterPath: relative, requireFormatVersion2: context.step.id === "09" })
}

async function citationGuard(context: GateContext): Promise<GateResult> {
  const relative = `wiki/books/${context.step.target}`
  const after = await readOptional(chapterFileOf(context.wikiRoot, context.step.target))

  if (after === null) {
    return blocker("missing-chapter", `Capitolo assente: atteso ${relative}.`, relative)
  }

  const before = await readOptional(snapshotPathOf(context.projectRoot, context.spec.volumeCode, context.step))

  return runCitationGuard({ before: before ?? "", after, chapterPath: relative })
}

async function reviewReport(context: GateContext): Promise<GateResult> {
  const relative = `wiki/${reportRelativePathOf(context.spec.volumeCode, context.step)}`
  const report = await readOptional(reportPathOf(context.wikiRoot, context.spec.volumeCode, context.step))

  if (report === null) {
    return blocker(
      "missing-report",
      `Report di revisione assente: attesa la nota ${relative} nel template fisso del Revisore Editoriale Totale.`,
      relative
    )
  }

  return runReviewReportGate({ report, reportPath: relative, requireJudgment: context.step.id === "21" })
}

async function coverage(context: GateContext): Promise<GateResult> {
  if (!context.module) {
    return blocker(
      "missing-module",
      `Lo step ${context.step.id} non è associato a un modulo: impossibile individuare la matrice di copertura.`
    )
  }

  const relative = matrixPathFor(context.module, context.chapterNumber)
  const absolute = path.join(context.wikiRoot, "books", ...relative.split("/"))
  const matrix = await readFile(absolute, "utf8").catch(() => "")

  if (!matrix) {
    return blocker(
      "missing-matrix",
      `Matrice di copertura assente: attesa in wiki/books/${relative}. Esegui il prompt 07 prima dei gate di capitolo.`,
      relative
    )
  }

  return runCoverageGate({ matrix, matrixPath: `wiki/books/${relative}`, chapterNumber: context.chapterNumber })
}

async function didacticDensity(context: GateContext): Promise<GateResult> {
  const relative = `wiki/books/${context.step.target}`
  const content = await readOptional(chapterFileOf(context.wikiRoot, context.step.target))
  const coverageResult = await coverage(context)

  if (content === null) {
    return combineGateResults(
      coverageResult,
      blocker("missing-chapter", `Capitolo assente: atteso ${relative}. Lo step 09 deve produrre il file.`, relative)
    )
  }

  const chapter = context.chapterNumber
    ? context.module?.chapters.find((candidate) => candidate.number === context.chapterNumber)
    : undefined
  const densityResult = runDidacticDensityGate({
    content,
    chapterPath: relative,
    thresholds: {
      ...(chapter?.minWords ? { minChapterWords: chapter.minWords } : {}),
      ...(chapter?.minQuizzes ? { minQuizzes: chapter.minQuizzes } : {})
    }
  })
  const referralResult = analyzeDidacticDensity(content).formatVersion >= 2
    ? await runVerifiedReferralGate({ content, wikiRoot: context.wikiRoot, chapterPath: relative })
    : { passed: true, blockers: [], warnings: [] }

  return combineGateResults(coverageResult, densityResult, referralResult)
}

function matrixPathFor(module: VolumeSpecModule, chapterNumber: string | undefined) {
  const declared = chapterNumber ? module.chapters.find((chapter) => chapter.number === chapterNumber)?.matrix : ""

  return `${module.moduleId}/${declared?.trim() || DEFAULT_MATRIX_PATH}`
}

function notImplemented(gateId: string, context: GateContext): GateResult {
  return {
    passed: false,
    blockers: [
      {
        code: "gate-not-implemented",
        message: `Il gate "${gateId}" dello step ${context.step.id} non è ancora implementato: esegui la verifica a mano e chiudi lo step con --accept motivando l'esito.`,
        location: context.step.target
      }
    ],
    warnings: [],
    notImplemented: [gateId]
  }
}

function blocker(code: string, message: string, location?: string): GateResult {
  return { passed: false, blockers: [{ code, message, location }], warnings: [] }
}

function combineGateResults(...results: GateResult[]): GateResult {
  const blockers = results.flatMap((result) => result.blockers)
  const warnings = results.flatMap((result) => result.warnings)
  const notImplemented = results.flatMap((result) => result.notImplemented ?? [])

  return {
    passed: blockers.length === 0,
    blockers,
    warnings,
    ...(notImplemented.length ? { notImplemented } : {})
  }
}

async function readOptional(file: string) {
  return readFile(file, "utf8").catch((error: NodeJS.ErrnoException) => {
    if (error.code === "ENOENT") return null

    throw error
  })
}
