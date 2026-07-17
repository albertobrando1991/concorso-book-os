import fs from "node:fs"
import path from "node:path"
const valid = new Set(["completo", "parziale", "solo-nominato", "rinviato", "mancante"])
const files = find(process.cwd())
if (!files.length) { console.log("Audit copertura didattica: nessuna matrice *-matrice-copertura-didattica.md trovata."); process.exit(0) }
let blockers = 0, warnings = 0, complete = 0
for (const file of files) {
  const rows = parse(fs.readFileSync(file, "utf8")); const result = audit(rows)
  blockers += result.blockers.length; warnings += result.warnings.length; complete += result.complete
  console.log(`${path.relative(process.cwd(), file)}: ${rows.length} righe, ${result.complete} complete, ${result.blockers.length} blocker, ${result.warnings.length} warning`)
  for (const item of [...result.blockers, ...result.warnings]) console.log(`  riga ${item.row}: ${item.message}`)
}
console.log(`Totale: ${files.length} matrici, ${complete} righe complete, ${blockers} blocker, ${warnings} warning.`)
process.exitCode = blockers ? 1 : 0
function find(root) { const found = []; for (const entry of fs.readdirSync(root, { withFileTypes: true })) { if ([".git", "node_modules"].includes(entry.name)) continue; const target = path.join(root, entry.name); if (entry.isDirectory()) found.push(...find(target)); else if (entry.name.endsWith("-matrice-copertura-didattica.md")) found.push(target) } return found.sort() }
function parse(markdown) {
  const lines = markdown.split(/\r?\n/), rows = []
  for (let i = 0; i < lines.length - 1; i += 1) {
    const headers = line(lines[i]); if (!headers || !separator(lines[i + 1])) continue
    const normalized = headers.map((value) => value.toLowerCase().replace(/\s+/g, " ")), index = (names) => normalized.findIndex((value) => names.includes(value))
    const indexes = { status: index(["stato"]), sources: index(["fonti", "fonti consolidate"]), theory: index(["copertura teorica"]), application: index(["applicazione"]), verification: index(["verifica", "verifica apprendimento"]), referral: index(["destinazione rinvio"]) }
    if (indexes.status < 0) continue
    for (let j = i + 2; j < lines.length; j += 1) { const cells = line(lines[j]); if (!cells) break; const value = (key) => indexes[key] < 0 ? "" : cells[indexes[key]] || ""; rows.push({ status: value("status"), sources: value("sources"), theory: value("theory"), application: value("application"), verification: value("verification"), referral: value("referral") }) }
  }
  return rows
}
function audit(rows) {
  const blockers = [], warnings = []; let complete = 0
  rows.forEach((row, i) => { const number = i + 1, status = row.status.trim().toLowerCase(); if (!valid.has(status)) blockers.push({ row: number, message: `stato non valido: ${row.status || "(vuoto)"}` }); else if (["parziale", "solo-nominato", "mancante"].includes(status)) blockers.push({ row: number, message: `stato bloccante: ${status}` }); if (status === "rinviato" && !row.referral.trim()) blockers.push({ row: number, message: "rinvio senza destinazione precisa" }); if (!row.sources.trim()) warnings.push({ row: number, message: "fonte consolidata mancante" }); if (status === "completo") { if (!row.theory.trim() || !row.application.trim() || !row.verification.trim()) blockers.push({ row: number, message: "riga completa priva di teoria, applicazione o verifica" }); else complete += 1 } })
  return { blockers, warnings, complete }
}
function line(text) { const value = text.trim(); return value.startsWith("|") && value.endsWith("|") ? value.slice(1, -1).split("|").map((cell) => cell.trim()) : null }
function separator(text) { const cells = line(text); return Boolean(cells?.length && cells.every((cell) => /^:?-{3,}:?$/.test(cell))) }
