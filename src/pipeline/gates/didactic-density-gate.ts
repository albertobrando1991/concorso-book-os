import { parseFrontmatter } from "../../server/wiki/frontmatter"
import type { GateIssue, GateResult } from "../state/types"
import { headingsOf, type MarkdownHeading } from "./chapter-lint-gate"

export interface DidacticThresholds {
  minNuclei: number
  minWordsPerNucleus: number
  minChapterWords: number
  minQuizzes: number
  minCases: number
  maxNucleiBetweenVerifications: number
  longNucleusWords: number
}

export const DEFAULT_DIDACTIC_THRESHOLDS: DidacticThresholds = {
  minNuclei: 5,
  minWordsPerNucleus: 600,
  minChapterWords: 3000,
  minQuizzes: 6,
  minCases: 1,
  maxNucleiBetweenVerifications: 7,
  longNucleusWords: 1800
}

export interface DidacticDensityGateInput {
  content: string
  chapterPath: string
  formatVersion?: number
  thresholds?: Partial<DidacticThresholds>
}

export interface NucleusMetrics {
  id: string
  heading: string
  words: number
  line: number
}

export interface DidacticDensityMetrics {
  formatVersion: number
  chapterWords: number
  nuclei: NucleusMetrics[]
  malformedNucleusHeadings: MarkdownHeading[]
  verificationBlocks: number
  maxConsecutiveNuclei: number
  quizzes: number
  cases: number
}

const VALID_NUCLEUS = /^(N-[A-Z]{2}\d{2}-\d{2}-\d{2})\s+·\s+.+$/
const NUCLEUS_PREFIX = /^N-/
const VERIFICATION = /^▣\s*Verifica\b/i

export function analyzeDidacticDensity(content: string, explicitFormatVersion?: number): DidacticDensityMetrics {
  const parsed = parseFrontmatter(content.replace(/\r\n/g, "\n"))
  const frontmatter = parsed.data as Record<string, unknown>
  const body = parsed.body
  const lines = body.split("\n")
  const headings = headingsOf(body)
  const validHeadings = headings.flatMap((heading) => {
    const match = VALID_NUCLEUS.exec(heading.text)
    return match ? [{ heading, id: match[1] }] : []
  })
  const malformedNucleusHeadings = headings.filter((heading) => NUCLEUS_PREFIX.test(heading.text) && !VALID_NUCLEUS.test(heading.text))
  const nuclei = validHeadings.map(({ heading, id }) => {
    const next = headings.find((candidate) => candidate.line > heading.line && candidate.level <= heading.level)
    const section = lines.slice(heading.line + 1, next?.line ?? lines.length).join("\n")
    return { id, heading: heading.text, words: wordCount(section), line: heading.line }
  })

  return {
    formatVersion: explicitFormatVersion ?? numeric(frontmatter.format_version) ?? 1,
    chapterWords: wordCount(body),
    nuclei,
    malformedNucleusHeadings,
    verificationBlocks: headings.filter((heading) => VERIFICATION.test(heading.text)).length,
    maxConsecutiveNuclei: maximumConsecutiveNuclei(headings),
    quizzes: body.match(/Risposta corretta\s*:/gi)?.length ?? 0,
    cases: body.match(/Caso (?:ragionato|guidato)\b/gi)?.length ?? 0
  }
}

export function runDidacticDensityGate(input: DidacticDensityGateInput): GateResult {
  const thresholds = { ...DEFAULT_DIDACTIC_THRESHOLDS, ...input.thresholds }
  const metrics = analyzeDidacticDensity(input.content, input.formatVersion)
  const warnings: GateIssue[] = []
  const blockers: GateIssue[] = []
  const at = (code: string, message: string): GateIssue => ({ code, message, location: input.chapterPath })

  const longNuclei = metrics.nuclei.filter((nucleus) => nucleus.words > thresholds.longNucleusWords)
  if (longNuclei.length) {
    warnings.push(at("nucleo-molto-lungo", `Nuclei oltre ${thresholds.longNucleusWords} parole: ${longNuclei.map((nucleus) => nucleus.id).join(", ")}.`))
  }

  if (metrics.nuclei.length > 1) {
    const lengths = metrics.nuclei.map((nucleus) => nucleus.words).filter((words) => words > 0)
    const shortest = Math.min(...lengths)
    const longest = Math.max(...lengths)
    if (shortest > 0 && longest > shortest * 3) {
      warnings.push(at("squilibrio-nuclei", `Il nucleo più lungo (${longest} parole) supera tre volte il più breve (${shortest}).`))
    }
  }

  if (metrics.formatVersion < 2) {
    const deficits = [
      `nuclei ${metrics.nuclei.length}/${thresholds.minNuclei}`,
      `parole ${metrics.chapterWords}/${thresholds.minChapterWords}`,
      `quiz ${metrics.quizzes}/${thresholds.minQuizzes}`,
      `casi ${metrics.cases}/${thresholds.minCases}`,
      `verifiche ${metrics.verificationBlocks}/1`
    ]
    warnings.unshift(at("retrofit-dovuto", `Capitolo legacy (format_version ${metrics.formatVersion}): ${deficits.join(", ")}. Nessun deficit blocca finché non passa al formato 2.`))
    return { passed: true, blockers: [], warnings }
  }

  if (metrics.nuclei.length < thresholds.minNuclei) {
    blockers.push(at("nuclei-insufficienti", `Servono almeno ${thresholds.minNuclei} nuclei validi: trovati ${metrics.nuclei.length}.`))
  }

  if (metrics.malformedNucleusHeadings.length) {
    blockers.push(
      at(
        "nucleo-id-malformato",
        `Heading nucleo non conformi a N-XX00-00-00 · Titolo: ${metrics.malformedNucleusHeadings.map((heading) => heading.text).join("; ")}.`
      )
    )
  }

  const shortNuclei = metrics.nuclei.filter((nucleus) => nucleus.words < thresholds.minWordsPerNucleus)
  if (shortNuclei.length) {
    blockers.push(
      at(
        "nucleo-troppo-breve",
        `Nuclei sotto ${thresholds.minWordsPerNucleus} parole: ${shortNuclei.map((nucleus) => `${nucleus.id} (${nucleus.words})`).join(", ")}.`
      )
    )
  }

  if (metrics.verificationBlocks === 0) {
    blockers.push(at("verifica-assente", "Manca un heading ▣ Verifica nel capitolo."))
  }
  if (metrics.maxConsecutiveNuclei > thresholds.maxNucleiBetweenVerifications) {
    blockers.push(
      at(
        "verifica-troppo-distante",
        `Trovati ${metrics.maxConsecutiveNuclei} nuclei consecutivi senza verifica; il massimo è ${thresholds.maxNucleiBetweenVerifications}.`
      )
    )
  }
  if (metrics.quizzes < thresholds.minQuizzes) {
    blockers.push(at("quiz-insufficienti", `Servono almeno ${thresholds.minQuizzes} risposte commentate: trovate ${metrics.quizzes}.`))
  }
  if (metrics.cases < thresholds.minCases) {
    blockers.push(at("caso-assente", "Manca almeno un Caso ragionato o Caso guidato."))
  }
  if (metrics.chapterWords < thresholds.minChapterWords) {
    blockers.push(at("capitolo-troppo-breve", `Il corpo ha ${metrics.chapterWords} parole; minimo ${thresholds.minChapterWords}.`))
  }

  return { passed: blockers.length === 0, blockers, warnings }
}

function maximumConsecutiveNuclei(headings: MarkdownHeading[]) {
  let current = 0
  let maximum = 0
  for (const heading of headings) {
    if (NUCLEUS_PREFIX.test(heading.text)) {
      current += 1
      maximum = Math.max(maximum, current)
    } else if (VERIFICATION.test(heading.text)) {
      current = 0
    }
  }
  return maximum
}

function wordCount(value: string) {
  return value.match(/[\p{L}\p{N}]+(?:['’][\p{L}\p{N}]+)*/gu)?.length ?? 0
}

function numeric(value: unknown) {
  if (value === undefined || value === null || value === "") return undefined
  const parsed = Number(value)
  return Number.isFinite(parsed) ? parsed : undefined
}
