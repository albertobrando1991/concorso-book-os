import { parseFrontmatter } from "../../server/wiki/frontmatter"

export interface OperationalDataReviewRow {
  id: string
  title: string
  file: string
  line: number
  reviewer: string
  source: string
  version: string
  verifiedAt: string
}

const BOX_HEADING = /^>\s*\*\*Dato operativo\s+—\s+(.+?)\*\*\s*$/i

export function extractOperationalDataReviewRows(content: string, file: string): OperationalDataReviewRow[] {
  const normalized = content.replace(/\r\n/g, "\n")
  const parsed = parseFrontmatter(normalized)
  const declared = strings(parsed.data.dati_operativi)
  const lines = normalized.split("\n")
  const rows: OperationalDataReviewRow[] = []

  for (let index = 0; index < lines.length; index += 1) {
    const heading = BOX_HEADING.exec(lines[index])
    if (!heading) continue

    const boxLines: string[] = []
    let cursor = index + 1
    while (cursor < lines.length && /^>/.test(lines[cursor])) {
      boxLines.push(lines[cursor].replace(/^>\s?/, "").trim())
      cursor += 1
    }
    const box = boxLines.join("\n")
    const sourceLine = /^Fonte:\s*(.*?)(?:\s*·\s*Versione:|$)/mi.exec(box)

    rows.push({
      id: declared[rows.length] || slug(heading[1]),
      title: heading[1].trim(),
      file,
      line: index + 1,
      reviewer: /^Review:\s*(REV-[A-Z0-9-]+)/mi.exec(box)?.[1] || "NON ASSEGNATO",
      source: sourceLine?.[1]?.trim() || "NON INDICATA",
      version: /(?:^|·\s*)Versione:\s*([^·\n]+)/mi.exec(box)?.[1]?.trim() || "NON INDICATA",
      verifiedAt: /(?:^|·\s*)Verificata al:\s*([^·\n]+)/mi.exec(box)?.[1]?.trim() || "NON INDICATA"
    })
  }

  return rows
}

export function renderOperationalDataReviewAppendix(rows: OperationalDataReviewRow[]) {
  if (!rows.length) {
    return "## Dati operativi — righe obbligatorie generate dalla pipeline\n\nNessun box `Dato operativo` rilevato nei capitoli del modulo."
  }

  return [
    "## Dati operativi — righe obbligatorie generate dalla pipeline",
    "",
    "Queste righe sono obbligatorie: l'audit specialistico automatico deve verificare la competenza indicata e chiudere ogni esito prima del text freeze.",
    "",
    "| ID | Dato operativo | File e posizione | Competenza specialistica | Fonte · versione · verifica | Esito |",
    "|---|---|---|---|---|---|",
    ...rows.map((row) =>
      `| ${cell(row.id)} | ${cell(row.title)} | ${cell(`${row.file}:${row.line}`)} | ${cell(row.reviewer)} | ${cell(`${row.source} · v. ${row.version} · ${row.verifiedAt}`)} | da compilare |`
    )
  ].join("\n")
}

function strings(value: unknown) {
  if (Array.isArray(value)) return value.map(String).map((item) => item.trim()).filter(Boolean)
  if (typeof value === "string") return value.split(",").map((item) => item.trim()).filter(Boolean)
  return []
}

function slug(value: string) {
  return `DO-${value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase().replace(/[^A-Z0-9]+/g, "-").replace(/^-+|-+$/g, "")}`
}

function cell(value: string) {
  return value.replace(/\|/g, "/").replace(/\s+/g, " ").trim()
}
