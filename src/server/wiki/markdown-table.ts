export interface MarkdownTable {
  heading: string
  headers: string[]
  rows: Record<string, string>[]
  lines: number[]
}

export function parseMarkdownTables(markdown: string): MarkdownTable[] {
  const lines = markdown.replace(/^﻿/, "").replace(/\r\n/g, "\n").split("\n")
  const tables: MarkdownTable[] = []
  let heading = ""

  for (let index = 0; index < lines.length; index += 1) {
    const headingMatch = /^#{1,6}\s+(.+?)\s*$/.exec(lines[index])

    if (headingMatch) {
      heading = headingMatch[1]
      continue
    }

    const headers = tableCells(lines[index])

    if (!headers || !isSeparator(lines[index + 1])) continue

    const rows: Record<string, string>[] = []
    const rowLines: number[] = []
    let cursor = index + 2

    while (cursor < lines.length) {
      const cells = tableCells(lines[cursor])

      if (!cells) break

      rows.push(toRow(headers, cells))
      rowLines.push(cursor + 1)
      cursor += 1
    }

    tables.push({ heading, headers, rows, lines: rowLines })
    index = cursor - 1
  }

  return tables
}

export function findTableAfterHeading(markdown: string, heading: string | RegExp): MarkdownTable | undefined {
  const matches = (value: string) =>
    typeof heading === "string" ? value.trim().toLowerCase() === heading.trim().toLowerCase() : heading.test(value.trim())

  return parseMarkdownTables(markdown).find((table) => matches(table.heading))
}

function toRow(headers: string[], cells: string[]) {
  return headers.reduce<Record<string, string>>(
    (row, header, index) => ({ ...row, [normalizeHeader(header)]: cells[index] ?? "" }),
    {}
  )
}

function normalizeHeader(header: string) {
  return header.trim().toLowerCase().replace(/\s+/g, " ")
}

function tableCells(line: string | undefined) {
  const value = (line ?? "").trim()
  return value.startsWith("|") && value.endsWith("|") && value.length > 1 ? tokenize(value.slice(1, -1)) : null
}

function isSeparator(line: string | undefined) {
  const cells = tableCells(line)
  return Boolean(cells?.length && cells.every((cell) => /^:?-{3,}:?$/.test(cell)))
}

function tokenize(value: string) {
  const cells: string[] = []
  let cell = ""
  let codeDelimiterLength = 0
  let inWikilink = false

  for (let index = 0; index < value.length; index += 1) {
    const char = value[index]
    const next = value[index + 1]

    if (char === "\\" && next === "|") {
      cell += "|"
      index += 1
      continue
    }

    if (!codeDelimiterLength && char === "[" && next === "[") {
      inWikilink = true
      cell += "[["
      index += 1
      continue
    }

    if (!codeDelimiterLength && inWikilink && char === "]" && next === "]") {
      inWikilink = false
      cell += "]]"
      index += 1
      continue
    }

    if (!inWikilink && char === "`") {
      let run = 1
      while (value[index + run] === "`") run += 1
      if (!codeDelimiterLength) codeDelimiterLength = run
      else if (run === codeDelimiterLength) codeDelimiterLength = 0
      cell += "`".repeat(run)
      index += run - 1
      continue
    }

    if (char === "|" && !codeDelimiterLength && !inWikilink) {
      cells.push(cell.trim())
      cell = ""
      continue
    }

    cell += char
  }

  cells.push(cell.trim())
  return cells
}
