#!/usr/bin/env node
/**
 * Copia le figure PNG dei capitoli wiki dentro slides/<VOL>/<folder>/images/
 * Preferisce i file *-v3.png.
 */
import fs from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const WIKI = path.join(ROOT, "wiki", "books")
const SLIDES = path.join(ROOT, "slides")

function copyPngs(fromDir, toDir) {
  if (!fs.existsSync(fromDir)) return 0
  const files = fs.readdirSync(fromDir).filter((name) => name.toLowerCase().endsWith(".png"))
  const chosen = new Map()
  for (const name of files) {
    const key = name.replace(/-v\d+(?=\.png$)/i, "")
    const prev = chosen.get(key)
    const isV3 = /-v3\.png$/i.test(name)
    const isV = /-v\d+\.png$/i.test(name)
    if (!prev) chosen.set(key, name)
    else if (isV3) chosen.set(key, name)
    else if (isV && !/-v\d+\.png$/i.test(prev)) chosen.set(key, name)
  }
  fs.mkdirSync(toDir, { recursive: true })
  let n = 0
  for (const name of chosen.values()) {
    fs.copyFileSync(path.join(fromDir, name), path.join(toDir, name))
    n += 1
  }
  return n
}

function chapterAssetsFromSource(source) {
  if (!source) return null
  const modulo = source.match(/wiki\/books\/moduli\/([^/]+)\/chapters\/(\d+)-/)
  if (modulo) {
    return path.join(WIKI, "moduli", modulo[1], "assets", `chapter-${modulo[2]}`)
  }
  const metodo = source.match(/wiki\/books\/il-metodo-bando\/chapters\//)
  if (metodo) return null
  return null
}

function syncVolumeManifest(vol, extraFromChapter) {
  const manifestPath = path.join(SLIDES, vol, "manifest.json")
  if (!fs.existsSync(manifestPath)) return 0
  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"))
  let total = 0
  for (const ch of manifest.chapters) {
    const candidates = []
    const fromSource = chapterAssetsFromSource(ch.source)
    if (fromSource) candidates.push(fromSource)
    if (typeof extraFromChapter === "function") {
      const extra = extraFromChapter(ch)
      if (extra) candidates.push(extra)
    }
    const to = path.join(SLIDES, vol, ch.folder, "images")
    let n = 0
    for (const from of candidates) n += copyPngs(from, to)
    if (n) console.log(`${vol} ${ch.n}  ${n} figure → ${ch.folder}/images`)
    total += n
  }
  return total
}

function syncVolume01() {
  return syncVolumeManifest("VOL-01", (ch) => {
    const num = Number.parseInt(ch.n, 10)
    if (!Number.isFinite(num) || num < 1) return null
    return path.join(WIKI, "il-metodo-bando", "assets", `chapter-${String(num).padStart(2, "0")}`)
  })
}

function syncVolume02() {
  return syncVolumeManifest("VOL-02")
}

function syncVolume03() {
  return syncVolumeManifest("VOL-03")
}

function syncVolume04() {
  return syncVolumeManifest("VOL-04")
}

function syncVolume05() {
  return syncVolumeManifest("VOL-05")
}

function syncVolume06() {
  return syncVolumeManifest("VOL-06")
}

function syncVolume07() {
  return syncVolumeManifest("VOL-07")
}

function syncVolume08() {
  return syncVolumeManifest("VOL-08")
}

function syncVolume09() {
  return syncVolumeManifest("VOL-09")
}

function syncVolume10() {
  return syncVolumeManifest("VOL-10")
}

function syncVolume11() {
  return syncVolumeManifest("VOL-11")
}

function syncVolume12() {
  return syncVolumeManifest("VOL-12")
}

function syncModules() {
  const moduli = path.join(WIKI, "moduli")
  if (!fs.existsSync(moduli)) return 0
  let total = 0
  for (const entry of fs.readdirSync(moduli, { withFileTypes: true })) {
    if (!entry.isDirectory() || !entry.name.startsWith("m-")) continue
    const assets = path.join(moduli, entry.name, "assets")
    if (!fs.existsSync(assets)) continue
    const to = path.join(SLIDES, "assets", "moduli", entry.name)
    const n = copyPngs(assets, to)
    if (n) console.log(`modulo ${entry.name}  ${n} figure`)
    total += n
  }
  return total
}

const a = syncVolume01()
const vol02 = syncVolume02()
const vol03 = syncVolume03()
const vol04 = syncVolume04()
const vol05 = syncVolume05()
const vol06 = syncVolume06()
const vol07 = syncVolume07()
const vol08 = syncVolume08()
const vol09 = syncVolume09()
const vol10 = syncVolume10()
const vol11 = syncVolume11()
const vol12 = syncVolume12()
const b = syncModules()
console.log(`Copiate ${a + vol02 + vol03 + vol04 + vol05 + vol06 + vol07 + vol08 + vol09 + vol10 + vol11 + vol12 + b} figure nelle cartelle slide`)
