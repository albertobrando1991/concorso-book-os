import { parseFrontmatter } from "../../server/wiki/frontmatter"
import { findTableAfterHeading, parseMarkdownTables, type MarkdownTable } from "../../server/wiki/markdown-table"

export const PHASE_IDS = ["A", "B", "C", "D", "E", "F", "G"] as const
export type PhaseId = (typeof PHASE_IDS)[number]

export interface VolumeSpecChapter {
  number: string
  title: string
  file: string
  matrix: string
  expectedStatus: string
  notes: string
}

export interface VolumeSpecModule {
  code: string
  moduleId: string
  priority: number
  phases: string[]
  chapters: VolumeSpecChapter[]
  chaptersSource: "declared" | "derived"
  line: number
  chapterLines: number[]
}

export interface VolumeSpec {
  specPath: string
  volumeCode: string
  volumeTitle: string
  cutOffDate: string
  responsabileNormativo: string
  responsabileEditoriale: string
  writerProvider: string
  phases: string[]
  modules: VolumeSpecModule[]
}

const CHAPTER_TABLE_HEADING = /^capitoli\s+(.+)$/i

export function parseVolumeSpec(markdown: string, specPath: string): VolumeSpec {
  const normalized = markdown.replace(/^﻿/, "").replace(/\r\n/g, "\n")
  const data = parseFrontmatter(normalized).data as Record<string, unknown>
  const phases = toList(data.phases)

  return {
    specPath,
    volumeCode: text(data.volume_code),
    volumeTitle: text(data.volume_title),
    cutOffDate: text(data.cut_off_date),
    responsabileNormativo: text(data.responsabile_normativo),
    responsabileEditoriale: text(data.responsabile_editoriale),
    writerProvider: text(data.writer_provider),
    phases,
    modules: parseModules(normalized, phases)
  }
}

function parseModules(markdown: string, volumePhases: string[]): VolumeSpecModule[] {
  const table = findTableAfterHeading(markdown, "Moduli")

  if (!table) return []

  const chapterTables = collectChapterTables(markdown)

  return table.rows.map((row, index) => {
    const code = row.codice ?? ""
    const chapters = chapterTables.get(code.trim().toUpperCase())
    const declaredPhases = toList(row.fasi)

    return {
      code,
      moduleId: row["module id"] ?? "",
      priority: toPriority(row["priorità"] ?? row.priorita),
      phases: declaredPhases.length ? declaredPhases : volumePhases,
      chapters: chapters ? chapters.rows.map(toChapter) : [],
      chaptersSource: chapters ? ("declared" as const) : ("derived" as const),
      line: table.lines[index],
      chapterLines: chapters ? chapters.lines : []
    }
  })
}

function collectChapterTables(markdown: string) {
  return parseMarkdownTables(markdown).reduce((tables, table) => {
    const match = CHAPTER_TABLE_HEADING.exec(table.heading.trim())
    return match ? tables.set(match[1].trim().toUpperCase(), table) : tables
  }, new Map<string, MarkdownTable>())
}

function toChapter(row: Record<string, string>): VolumeSpecChapter {
  return {
    number: row["#"] ?? row.numero ?? "",
    title: row.titolo ?? row.title ?? "",
    file: row.file ?? "",
    matrix: row.matrice ?? "",
    expectedStatus: row["stato atteso"] ?? "",
    notes: row.note ?? ""
  }
}

function toPriority(value: string | undefined) {
  const parsed = Number.parseInt((value ?? "").trim(), 10)
  return Number.isFinite(parsed) ? parsed : 0
}

function toList(value: unknown): string[] {
  if (Array.isArray(value)) return value.map((item) => String(item).trim()).filter(Boolean)

  return String(value ?? "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean)
}

function text(value: unknown) {
  if (value === undefined || value === null) return ""

  return String(value).trim()
}
