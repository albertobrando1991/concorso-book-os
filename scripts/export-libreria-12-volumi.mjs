#!/usr/bin/env node
/**
 * Esporta una libreria navigabile dei 12 volumi:
 *
 *   Desktop/libreria-12-volumi/
 *     VOL-01-.../
 *       M-PA01-il-metodo-bando/*.md
 *       ricettario-digitale/*.md
 *       00-apertura-volume/*.md   (se presente)
 *       fonti/                    PDF e altri originali scaricati
 *
 * Destinazione: solo Desktop, fuori dal repo.
 * I file canonici restano in wiki/. I file della libreria sono hardlink
 * (o copie se il collegamento non è possibile).
 *
 * Uso: node scripts/export-libreria-12-volumi.mjs
 */

import fs from "node:fs"
import os from "node:os"
import path from "node:path"
import { fileURLToPath } from "node:url"

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const ROOT = path.resolve(__dirname, "..")
const WIKI = path.join(ROOT, "wiki")
const BOOKS = path.join(WIKI, "books")
const RAW = path.join(WIKI, "raw")
const SOURCES = path.join(WIKI, "sources")

function resolveDesktop() {
  const home = os.homedir()
  const repoParent = path.dirname(ROOT)
  if (path.basename(repoParent).toLowerCase() === "desktop") return repoParent

  const candidates = [path.join(home, "OneDrive", "Desktop"), path.join(home, "Desktop")]
  return candidates.find((dir) => fs.existsSync(dir)) || path.join(home, "Desktop")
}

const OUT_ROOT = path.join(resolveDesktop(), "libreria-12-volumi")

const SOURCE_FILE_EXT = new Set([".pdf", ".html", ".htm", ".xml", ".txt", ".md", ".docx"])
const SKIP_RAW_NAMES = new Set([
  "download-log.csv",
  "download-manifest.csv",
  "download-manifest.tsv",
  "download-manifest-extra.csv"
])

const VOLUMES = [
  {
    code: "VOL-01",
    title: "Manuale base PA",
    modules: [{ code: "M-PA01", bookId: "il-metodo-bando" }],
    rawFolders: [
      "chapter-7-trasparenza-anticorruzione-privacy",
      "chapter-8-contabilita-pubblica",
      "chapter-9-contratti-pubblici",
      "chapter-10-informatica",
      "chapter-11-inglese",
      "chapter-12-logica-comprensione-ragionamento",
      "chapter-17-18-casi-situazionali",
      "chapter-19-20-profili-concorsuali",
      "chapter-21-23-moduli-piano-diario",
      "chapter-25-aggiornare-metodo",
      "constitutional-law",
      "decrees",
      "laws",
      "manuals",
      "websites"
    ]
  },
  {
    code: "VOL-02",
    title: "Enti locali, Camere di commercio e Polizia locale",
    modules: [
      { code: "M-FL01", bookId: "moduli/m-fl01-comuni-unioni" },
      { code: "M-FL02", bookId: "moduli/m-fl02-regioni-province-citta-metropolitane" },
      { code: "M-FL03", bookId: "moduli/m-fl03-camere-commercio" },
      { code: "M-FL04", bookId: "moduli/m-fl04-polizia-locale" }
    ],
    orientationBookIds: ["vol-02-enti-locali-polizia-locale"],
    rawFolders: ["vol-02-enti-locali-polizia-locale", "vol-12-comuni"]
  },
  {
    code: "VOL-03",
    title: "Funzioni centrali, Fisco, Previdenza e Ispettivo",
    modules: [
      { code: "M-FC01", bookId: "moduli/m-fc01-ministeri" },
      { code: "M-FC02", bookId: "moduli/m-fc02-agenzie-fiscali" },
      { code: "M-FC03", bookId: "moduli/m-fc03-enti-non-economici" }
    ],
    orientationBookIds: ["volumi/vol-03-fisco-dogane-previdenza-ispettivo"],
    rawFolders: [
      "m-fc01-ministeri",
      "m-fc02-agenzie-fiscali",
      "m-fc03-enti-non-economici",
      "vol-03-fisco-dogane-previdenza-ispettivo"
    ]
  },
  {
    code: "VOL-04",
    title: "Giustizia e UPP",
    modules: [{ code: "M-FC04", bookId: "moduli/m-fc04-giustizia" }],
    orientationBookIds: ["vol-04-giustizia-upp"],
    rawFolders: ["m-fc04-giustizia"]
  },
  {
    code: "VOL-05",
    title: "Authority e regolazione",
    modules: [{ code: "M-FC05", bookId: "moduli/m-fc05-authority-indipendenti" }],
    orientationBookIds: ["vol-05-authority-regolazione"],
    rawFolders: ["vol-05-authority-regolazione"]
  },
  {
    code: "VOL-06",
    title: "Scuola, Universita, Ricerca, Cultura",
    modules: [
      { code: "M-IR01", bookId: "moduli/m-ir01-scuola" },
      { code: "M-IR02", bookId: "moduli/m-ir02-universita-afam" },
      { code: "M-IR03", bookId: "moduli/m-ir03-enti-ricerca" },
      { code: "M-IR04", bookId: "moduli/m-ir04-cultura-beni-culturali" }
    ],
    orientationBookIds: ["volumi/vol-06-scuola-universita-ricerca-cultura"],
    rawFolders: ["vol-06-scuola-universita-ricerca-cultura"]
  },
  {
    code: "VOL-07",
    title: "Sanita amministrativa e professioni sanitarie",
    modules: [
      { code: "M-SA01", bookId: "moduli/m-sa01-sanita-amministrativa" },
      { code: "M-SA02", bookId: "moduli/m-sa02-professioni-sanitarie" },
      { code: "M-SA03", bookId: "moduli/m-sa03-dirigenza-medica-sanitaria" },
      { code: "M-SA04", bookId: "moduli/m-sa04-tecnici-sanitari-prevenzione" }
    ],
    orientationBookIds: ["volumi/vol-07-sanita-amministrativa-professioni-sanitarie"],
    rawFolders: [
      "m-sa01-sanita-amministrativa",
      "m-sa02-professioni-sanitarie",
      "m-sa03-dirigenza-medica-sanitaria",
      "m-sa04-tecnici-sanitari-prevenzione"
    ]
  },
  {
    code: "VOL-08",
    title: "ICT, digitale, cybersecurity e dati",
    modules: [{ code: "M-TR01", bookId: "moduli/m-tr01-ict-trasformazione-digitale" }],
    orientationBookIds: ["volumi/vol-08-ict-digitale-cybersecurity-dati"],
    rawFolders: []
  },
  {
    code: "VOL-09",
    title: "Appalti, PNRR e procurement",
    modules: [{ code: "M-TR02", bookId: "moduli/m-tr02-appalti-pnrr-fondi-ue" }],
    orientationBookIds: ["volumi/vol-09-appalti-pnrr-procurement"],
    rawFolders: ["vol-09-appalti-pnrr-procurement"]
  },
  {
    code: "VOL-10",
    title: "Tecnico-ingegneristico, territorio, lavori pubblici",
    modules: [{ code: "M-TR03", bookId: "moduli/m-tr03-tecnico-ingegneristico" }],
    orientationBookIds: ["volumi/vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"],
    rawFolders: []
  },
  {
    code: "VOL-11",
    title: "Ambiente, protezione civile e sostenibilita",
    modules: [{ code: "M-TR04", bookId: "moduli/m-tr04-ambiente-protezione-civile" }],
    orientationBookIds: ["volumi/vol-11-ambiente-protezione-civile-sostenibilita"],
    rawFolders: ["vol-11-ambiente-protezione-civile-sostenibilita"]
  },
  {
    code: "VOL-12",
    title: "Carriere speciali premium",
    modules: [
      { code: "M-SP01", bookId: "moduli/m-sp01-forze-ordine" },
      { code: "M-SP02", bookId: "moduli/m-sp02-vigili-fuoco" },
      { code: "M-SP03", bookId: "moduli/m-sp03-magistratura-avvocatura-notariato" },
      { code: "M-SP04", bookId: "moduli/m-sp04-prefettizia-diplomatica" }
    ],
    orientationBookIds: ["volumi/vol-12-carriere-speciali-premium"],
    rawFolders: [
      "m-sp01-forze-ordine",
      "m-sp02-vigili-fuoco",
      "m-sp03-magistratura-avvocatura-notariato",
      "m-sp04-prefettizia-diplomatica"
    ]
  }
]

function slugify(value) {
  return String(value)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^A-Za-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
}

function volumeFolderName(volume) {
  return `${volume.code}-${slugify(volume.title)}`
}

function moduleFolderName(mod) {
  const slug = path.basename(mod.bookId)
  const rest = slug.replace(/^m-[a-z]{2}\d{2}-/i, "")
  return rest && rest !== slug ? `${mod.code}-${rest}` : `${mod.code}-${slug}`
}

function parseFrontmatter(text) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (!match) return { data: {}, body: text }
  const raw = match[1]
  const data = {}
  const outline = raw.match(/^outline_section:\s*["']?([^"'\n]+?)["']?\s*$/m)
  if (outline) data.outline_section = outline[1].trim()
  const title = raw.match(/^title:\s*["']?(.+?)["']?\s*$/m)
  if (title) data.title = title[1].trim()
  data.source_refs = extractSourceRefs(raw)
  return { data, body: text.slice(match[0].length) }
}

function extractSourceRefs(frontmatter) {
  const refs = []
  const inline = frontmatter.match(/^source_refs:\s*\[([\s\S]*?)\]/m)
  if (inline) {
    for (const item of inline[1].matchAll(/["']([^"']+)["']/g)) refs.push(item[1])
    return refs
  }
  const block = frontmatter.match(/^source_refs:\s*\n((?:[ \t]*-[ \t].+\n?)+)/m)
  if (block) {
    for (const item of block[1].matchAll(/-\s+["']?([^"'\n]+)["']?/g)) refs.push(item[1].trim())
  }
  return refs
}

function outlineNumber(value) {
  const parsed = Number.parseInt(String(value ?? "").trim(), 10)
  return Number.isFinite(parsed) ? parsed : null
}

function chapterDestName(filename, outline) {
  if (/^\d{2}[a-z]?-/.test(filename)) return filename
  const number = outlineNumber(outline)
  if (number !== null) return `${String(number).padStart(2, "0")}-${filename}`
  if (filename === "introduzione.md") return "00-introduzione.md"
  return filename
}

function listMarkdown(dir) {
  if (!fs.existsSync(dir)) return []
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.toLowerCase().endsWith(".md"))
    .map((entry) => path.join(dir, entry.name))
    .sort((a, b) => a.localeCompare(b, "it"))
}

function walkFiles(dir, files = []) {
  if (!fs.existsSync(dir)) return files
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) walkFiles(full, files)
    else files.push(full)
  }
  return files
}

function isSourceFile(filePath) {
  const name = path.basename(filePath)
  if (SKIP_RAW_NAMES.has(name)) return false
  if (name.toLowerCase().includes("z-library") || name.toLowerCase().includes("z-lib")) return false
  return SOURCE_FILE_EXT.has(path.extname(filePath).toLowerCase())
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true })
}

async function placeFile(src, dest) {
  ensureDir(path.dirname(dest))
  if (fs.existsSync(dest)) fs.unlinkSync(dest)
  try {
    fs.linkSync(src, dest)
    return "link"
  } catch {
    fs.copyFileSync(src, dest)
    return "copy"
  }
}

function resolveSourceNote(ref) {
  const cleaned = String(ref)
    .replace(/^\[\[/, "")
    .replace(/\]\]$/, "")
    .replace(/^sources\//, "")
    .replace(/\.md$/, "")
  const candidates = [
    path.join(SOURCES, `${cleaned}.md`),
    path.join(SOURCES, cleaned),
    path.join(WIKI, "sources", `${cleaned}.md`)
  ]
  return candidates.find((candidate) => fs.existsSync(candidate)) || null
}

function extractRawPathsFromText(text) {
  const found = new Set()
  const patterns = [
    /(?:local:)?wiki\/raw\/[^\s\)\]`'"]+/g,
    /(?:^|\s)raw\/[^\s\)\]`'"]+/gm
  ]
  for (const pattern of patterns) {
    for (const match of text.matchAll(pattern)) {
      let value = match[0].replace(/^local:/, "").trim()
      value = value.replace(/[.,;:]+$/, "")
      if (value.startsWith("raw/")) value = `wiki/${value}`
      found.add(value.replace(/\\/g, "/"))
    }
  }
  const rawPath = text.match(/^raw_path:\s*["']?([^"'\n]+)["']?/m)
  if (rawPath) found.add(rawPath[1].replace(/\\/g, "/"))
  const sourceUrl = text.match(/^source_url:\s*["']?(local:wiki\/raw\/[^"'\n]+)["']?/m)
  if (sourceUrl) found.add(sourceUrl[1].replace(/^local:/, "").replace(/\\/g, "/"))
  return [...found]
}

function toAbsoluteRaw(rawRef) {
  const relative = rawRef.replace(/^wiki\//, "")
  return path.join(WIKI, relative)
}

function collectChapterSources(chapterPath, bucket) {
  const text = fs.readFileSync(chapterPath, "utf8")
  const { data } = parseFrontmatter(text)
  for (const ref of data.source_refs || []) {
    const notePath = resolveSourceNote(ref)
    if (!notePath) {
      bucket.missingNotes.add(ref)
      continue
    }
    const note = fs.readFileSync(notePath, "utf8")
    const rawPaths = extractRawPathsFromText(note)
    if (rawPaths.length === 0) {
      const url = note.match(/^source_url:\s*["']?([^"'\n]+)["']?/m)
      if (url && /^https?:/i.test(url[1])) bucket.urlOnly.add(`${ref} → ${url[1]}`)
    }
    for (const rawRef of rawPaths) {
      const abs = toAbsoluteRaw(rawRef)
      if (fs.existsSync(abs) && fs.statSync(abs).isFile()) bucket.files.add(abs)
      else bucket.missingRaw.add(rawRef)
    }
  }
  return data
}

function isInside(parent, child) {
  const relative = path.relative(parent, child)
  return Boolean(relative) && !relative.startsWith("..") && !path.isAbsolute(relative)
}

function relativeToRaw(absPath) {
  return path.relative(RAW, absPath)
}

async function exportVolume(volume) {
  const volumeDir = path.join(OUT_ROOT, volumeFolderName(volume))
  ensureDir(volumeDir)

  const stats = {
    chapters: 0,
    fonti: 0,
    pdf: 0,
    linked: 0,
    copied: 0,
    modules: []
  }

  const sourceBucket = {
    files: new Set(),
    missingNotes: new Set(),
    missingRaw: new Set(),
    urlOnly: new Set()
  }

  for (const mod of volume.modules) {
    const chaptersDir = path.join(BOOKS, mod.bookId, "chapters")
    const files = listMarkdown(chaptersDir)
    const isVol01 = volume.code === "VOL-01"
    const groups = isVol01
      ? { libro: [], ricettario: [] }
      : { modulo: files }

    if (isVol01) {
      for (const file of files) {
        const text = fs.readFileSync(file, "utf8")
        const { data } = parseFrontmatter(text)
        const number = outlineNumber(data.outline_section)
        if (number !== null && number >= 25) groups.ricettario.push({ file, data })
        else groups.libro.push({ file, data })
      }
    }

    if (isVol01) {
      const libroFolder = path.join(volumeDir, "M-PA01-il-metodo-bando")
      const ricettarioFolder = path.join(volumeDir, "ricettario-digitale")
      ensureDir(libroFolder)
      ensureDir(ricettarioFolder)
      for (const item of groups.libro) {
        collectChapterSources(item.file, sourceBucket)
        const dest = path.join(libroFolder, chapterDestName(path.basename(item.file), item.data.outline_section))
        const mode = await placeFile(item.file, dest)
        stats.chapters += 1
        stats[mode === "link" ? "linked" : "copied"] += 1
      }
      for (const item of groups.ricettario) {
        collectChapterSources(item.file, sourceBucket)
        const dest = path.join(ricettarioFolder, chapterDestName(path.basename(item.file), item.data.outline_section))
        const mode = await placeFile(item.file, dest)
        stats.chapters += 1
        stats[mode === "link" ? "linked" : "copied"] += 1
      }
      stats.modules.push({
        folder: "M-PA01-il-metodo-bando",
        count: groups.libro.length,
        source: chaptersDir
      })
      stats.modules.push({
        folder: "ricettario-digitale",
        count: groups.ricettario.length,
        source: chaptersDir
      })
      continue
    }

    const folder = path.join(volumeDir, moduleFolderName(mod))
    ensureDir(folder)
    let count = 0
    for (const file of files) {
      const data = collectChapterSources(file, sourceBucket)
      const dest = path.join(folder, chapterDestName(path.basename(file), data.outline_section))
      const mode = await placeFile(file, dest)
      count += 1
      stats.chapters += 1
      stats[mode === "link" ? "linked" : "copied"] += 1
    }
    if (count === 0) {
      fs.writeFileSync(
        path.join(folder, "NESSUN-CAPITOLO.md"),
        `# ${mod.code}\n\nNessun file capitolo trovato in \`wiki/books/${mod.bookId}/chapters/\`.\n`,
        "utf8"
      )
    }
    stats.modules.push({ folder: moduleFolderName(mod), count, source: chaptersDir })
  }

  for (const bookId of volume.orientationBookIds || []) {
    const chaptersDir = path.join(BOOKS, bookId, "chapters")
    const files = listMarkdown(chaptersDir)
    if (files.length === 0) continue
    const folder = path.join(volumeDir, "00-apertura-volume")
    ensureDir(folder)
    for (const file of files) {
      const data = collectChapterSources(file, sourceBucket)
      const dest = path.join(folder, chapterDestName(path.basename(file), data.outline_section))
      const mode = await placeFile(file, dest)
      stats.chapters += 1
      stats[mode === "link" ? "linked" : "copied"] += 1
    }
    stats.modules.push({ folder: "00-apertura-volume", count: files.length, source: chaptersDir })
  }

  const fontiDir = path.join(volumeDir, "fonti")
  ensureDir(fontiDir)

  const placed = new Set()
  const pdfNames = []

  for (const folderName of volume.rawFolders || []) {
    const absFolder = path.join(RAW, folderName)
    for (const file of walkFiles(absFolder).filter(isSourceFile)) {
      sourceBucket.files.add(file)
    }
  }

  for (const mod of volume.modules) {
    const slug = path.basename(mod.bookId)
    const absFolder = path.join(RAW, slug)
    if (fs.existsSync(absFolder)) {
      for (const file of walkFiles(absFolder).filter(isSourceFile)) sourceBucket.files.add(file)
    }
  }

  for (const abs of [...sourceBucket.files].sort()) {
    if (placed.has(abs)) continue
    placed.add(abs)
    const rel = isInside(RAW, abs) ? relativeToRaw(abs) : path.basename(abs)
    const dest = path.join(fontiDir, rel)
    const mode = await placeFile(abs, dest)
    stats.fonti += 1
    stats[mode === "link" ? "linked" : "copied"] += 1
    if (path.extname(abs).toLowerCase() === ".pdf") {
      stats.pdf += 1
      pdfNames.push(rel.replace(/\\/g, "/"))
    }
  }

  const pdfDirListing = pdfNames.length
    ? pdfNames.map((name) => `- ${name}`).join("\n")
    : "_Nessun PDF locale trovato per questo volume._"

  const missingNotes = [...sourceBucket.missingNotes]
  const missingRaw = [...sourceBucket.missingRaw]
  const urlOnly = [...sourceBucket.urlOnly]

  const volumeReadme = `# ${volume.code} — ${volume.title}

Cartella di lavoro del volume. I capitoli \`.md\` sono la vista dei file canonici in \`wiki/books/\`.
Le fonti scaricate stanno in \`fonti/\` (PDF e, se presenti, HTML/XML/TXT originali).

## Moduli e capitoli

${stats.modules.map((item) => `- \`${item.folder}/\` — ${item.count} file`).join("\n") || "- nessun modulo"}

## Fonti

- File originali totali: **${stats.fonti}**
- Di cui PDF: **${stats.pdf}**

${missingNotes.length ? `### Source notes citate ma non trovate\n\n${missingNotes.map((item) => `- ${item}`).join("\n")}\n` : ""}
${missingRaw.length ? `### Percorsi raw citati ma assenti\n\n${missingRaw.map((item) => `- \`${item}\``).join("\n")}\n` : ""}
${urlOnly.length ? `### Fonti citate solo via URL (non scaricate in locale)\n\n${urlOnly.map((item) => `- ${item}`).join("\n")}\n` : ""}
## Elenco PDF

${pdfDirListing}
`

  fs.writeFileSync(path.join(volumeDir, "LEGGIMI.md"), volumeReadme, "utf8")
  fs.writeFileSync(path.join(fontiDir, "ELENCO-PDF.md"), `# PDF di ${volume.code}\n\n${pdfDirListing}\n`, "utf8")

  return stats
}

function rootReadme(summaries) {
  const rows = summaries
    .map(
      (item) =>
        `| ${item.code} | ${item.title} | ${item.chapters} | ${item.pdf} | ${item.fonti} |`
    )
    .join("\n")

  return `# Libreria 12 volumi

Vista di lavoro dei 12 volumi ConcorsoBook / Metodo BANDO.

Struttura:

\`\`\`
libreria-12-volumi/
  VOL-01-Manuale-base-PA/
    M-PA01-il-metodo-bando/     capitoli del libro base
    ricettario-digitale/        capitoli 25-47
    fonti/                      PDF e originali scaricati
  VOL-02-.../
    M-FL01-.../
    M-FL02-.../
    fonti/
  ...
\`\`\`

- Un file \`.md\` per ogni capitolo, dentro il modulo (e quindi il volume) di appartenenza.
- \`fonti/\` raccoglie gli originali scaricati usati o citati per quel volume, con i PDF in evidenza.
- Questa cartella sta sul Desktop, fuori dal repository.
- I file canonici restano in \`wiki/books/\` e \`wiki/raw/\`. Qui sono hardlink (o copie se il collegamento non è possibile).
- Per rigenerare: \`npm run export:libreria\` oppure \`node scripts/export-libreria-12-volumi.mjs\`.

## Riepilogo

| Volume | Titolo | Capitoli | PDF | Fonti totali |
| --- | --- | ---: | ---: | ---: |
${rows}
`
}

async function main() {
  const leftoverInRepo = path.join(ROOT, "libreria-12-volumi")
  if (fs.existsSync(leftoverInRepo)) {
    fs.rmSync(leftoverInRepo, { recursive: true, force: true })
    console.log(`Rimossa copia nel repo: ${leftoverInRepo}`)
  }

  if (fs.existsSync(OUT_ROOT)) fs.rmSync(OUT_ROOT, { recursive: true, force: true })
  ensureDir(OUT_ROOT)

  const summaries = []
  for (const volume of VOLUMES) {
    const stats = await exportVolume(volume)
    summaries.push({ ...volume, ...stats })
    console.log(
      `${volume.code}  capitoli=${stats.chapters}  pdf=${stats.pdf}  fonti=${stats.fonti}  link=${stats.linked}  copy=${stats.copied}`
    )
  }

  fs.writeFileSync(path.join(OUT_ROOT, "README.md"), rootReadme(summaries), "utf8")
  console.log(`\nLibreria scritta in ${OUT_ROOT}`)
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
