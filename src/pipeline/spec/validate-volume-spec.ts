import { WRITER_PROVIDERS } from "../../server/config"
import { PHASE_IDS, type VolumeSpec, type VolumeSpecChapter, type VolumeSpecModule } from "./parse-volume-spec"

export interface SpecIssue {
  field: string
  message: string
  line?: number
}

const VOLUME_CODE = /^VOL-\d{2}$/
const MODULE_CODE = /^M-[A-Z]{2}\d{2}$/
const BOOK_ID = /^[a-z0-9-]+(?:\/[a-z0-9-]+)*$/
const CHAPTER_FILE = /^chapters\/[^/\\]+\.md$/
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/

export function validateVolumeSpec(spec: VolumeSpec): SpecIssue[] {
  return [...validateScalars(spec), ...validateModules(spec)]
}

function validateScalars(spec: VolumeSpec): SpecIssue[] {
  const issues: SpecIssue[] = []

  if (!spec.volumeCode) issues.push(missing("volumeCode", "volume_code"))
  else if (!VOLUME_CODE.test(spec.volumeCode)) issues.push(invalid("volumeCode", "volume_code", spec.volumeCode, "atteso il formato VOL-03"))

  if (!spec.volumeTitle) issues.push(missing("volumeTitle", "volume_title"))

  if (!spec.cutOffDate) issues.push(missing("cutOffDate", "cut_off_date"))
  else if (!isCalendarDate(spec.cutOffDate)) issues.push(invalid("cutOffDate", "cut_off_date", spec.cutOffDate, "attesa una data reale in formato AAAA-MM-GG"))

  if (spec.writerProvider && !WRITER_PROVIDERS.includes(spec.writerProvider as (typeof WRITER_PROVIDERS)[number])) {
    issues.push(invalid("writerProvider", "writer_provider", spec.writerProvider, `valori ammessi: ${WRITER_PROVIDERS.join(", ")}`))
  }

  if (!spec.phases.length) issues.push(missing("phases", "phases"))

  const unknownPhases = spec.phases.filter((phase) => !PHASE_IDS.includes(phase.toUpperCase() as (typeof PHASE_IDS)[number]))

  if (unknownPhases.length) {
    issues.push(invalid("phases", "phases", unknownPhases.join(", "), `fasi ammesse: ${PHASE_IDS.join(", ")}`))
  }

  return issues
}

function validateModules(spec: VolumeSpec): SpecIssue[] {
  if (!spec.modules.length) {
    return [{ field: "modules", message: `La scheda ${spec.specPath} non elenca moduli: serve una tabella sotto l'intestazione "## Moduli".` }]
  }

  const seen = new Map<string, number>()

  return spec.modules.flatMap((module, index) => {
    const prefix = `modules[${index}]`
    const issues = validateModule(module, prefix, spec.phases)
    const code = module.code.trim().toUpperCase()
    const firstIndex = seen.get(code)

    if (code && firstIndex !== undefined) {
      return [
        ...issues,
        {
          field: `${prefix}.code`,
          message: `Il modulo ${module.code} è già dichiarato alla riga ${spec.modules[firstIndex].line}: ogni modulo va elencato una volta sola.`,
          line: module.line
        }
      ]
    }

    if (code) seen.set(code, index)

    return issues
  })
}

function validateModule(module: VolumeSpecModule, prefix: string, volumePhases: string[]): SpecIssue[] {
  const issues: SpecIssue[] = []

  if (!MODULE_CODE.test(module.code)) {
    issues.push({ field: `${prefix}.code`, message: `Codice modulo non valido: "${module.code}" (atteso il formato M-FC02).`, line: module.line })
  }

  if (!BOOK_ID.test(module.moduleId)) {
    issues.push({
      field: `${prefix}.moduleId`,
      message: `Module id non valido: "${module.moduleId}" (atteso un percorso wiki come moduli/m-fc02-agenzie-fiscali).`,
      line: module.line
    })
  }

  if (!Number.isInteger(module.priority) || module.priority <= 0) {
    issues.push({
      field: `${prefix}.priority`,
      message: `Priorità non valida per ${module.code || "il modulo"}: atteso un intero maggiore di zero.`,
      line: module.line
    })
  }

  const unknownPhases = module.phases.filter((phase) => !PHASE_IDS.includes(phase.toUpperCase() as (typeof PHASE_IDS)[number]))

  if (unknownPhases.length) {
    issues.push({ field: `${prefix}.phases`, message: `Fasi non valide per ${module.code}: ${unknownPhases.join(", ")}.`, line: module.line })
  }

  const outsideVolume = module.phases.filter(
    (phase) => !unknownPhases.includes(phase) && !volumePhases.some((declared) => declared.toUpperCase() === phase.toUpperCase())
  )

  if (outsideVolume.length) {
    issues.push({
      field: `${prefix}.phases`,
      message: `Il modulo ${module.code} dichiara fasi non previste dal volume: ${outsideVolume.join(", ")}.`,
      line: module.line
    })
  }

  const chapterIssues = module.chapters.flatMap((chapter, index) =>
    validateChapter(chapter, module.chaptersSource, `${prefix}.chapters[${index}]`, module.chapterLines[index])
  )

  return [...issues, ...chapterIssues]
}

function validateChapter(
  chapter: VolumeSpecChapter,
  chaptersSource: VolumeSpecModule["chaptersSource"],
  prefix: string,
  line: number | undefined
): SpecIssue[] {
  const issues: SpecIssue[] = []
  const { file, number, title } = chapter

  if (!number.trim()) issues.push({ field: `${prefix}.number`, message: "Numero capitolo mancante nella colonna #.", line })
  if (chaptersSource === "declared" && !title.trim()) {
    issues.push({ field: `${prefix}.title`, message: "Titolo capitolo mancante nella colonna Titolo.", line })
  }

  if (!CHAPTER_FILE.test(chapter.file)) {
    issues.push({ field: `${prefix}.file`, message: `Percorso capitolo non valido: "${chapter.file}" (atteso chapters/<nome>.md, relativo al modulo).`, line })
  }

  for (const [field, value, label] of [
    ["minWords", chapter.minWords, "Min parole"],
    ["minQuizzes", chapter.minQuizzes, "Min quiz"]
  ] as const) {
    if (value !== undefined && (!Number.isInteger(value) || value <= 0)) {
      issues.push({ field: `${prefix}.${field}`, message: `${label} deve essere un intero maggiore di zero.`, line })
    }
  }

  return issues
}

function isCalendarDate(value: string) {
  if (!ISO_DATE.test(value)) return false

  const [year, month, day] = value.split("-").map(Number)
  const date = new Date(Date.UTC(year, month - 1, day))

  return date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day
}

function missing(field: string, sheetField: string): SpecIssue {
  return { field, message: `Campo obbligatorio mancante nel frontmatter della scheda: ${sheetField}.` }
}

function invalid(field: string, sheetField: string, value: string, hint: string): SpecIssue {
  return { field, message: `Valore non valido per ${sheetField}: "${value}" — ${hint}.` }
}
