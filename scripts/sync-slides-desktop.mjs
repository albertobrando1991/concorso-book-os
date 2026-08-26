#!/usr/bin/env node
/**
 * Copia slides/ (canone in repo, GitHub staff) sul Desktop.
 */
import fs from "node:fs"
import os from "node:os"
import path from "node:path"
import { fileURLToPath } from "node:url"

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const SRC = path.join(ROOT, "slides")

function resolveDesktop() {
  const home = os.homedir()
  const parent = path.dirname(ROOT)
  if (path.basename(parent).toLowerCase() === "desktop") return parent
  const candidates = [path.join(home, "OneDrive", "Desktop"), path.join(home, "Desktop")]
  return candidates.find((dir) => fs.existsSync(dir)) || path.join(home, "Desktop")
}

const DEST = path.join(resolveDesktop(), "slide-capitale-personale")

function copyDir(from, to) {
  fs.mkdirSync(to, { recursive: true })
  for (const entry of fs.readdirSync(from, { withFileTypes: true })) {
    if (entry.name === "qa" || entry.name === ".git") continue
    const src = path.join(from, entry.name)
    const dst = path.join(to, entry.name)
    if (entry.isDirectory()) copyDir(src, dst)
    else fs.copyFileSync(src, dst)
  }
}

if (!fs.existsSync(SRC)) {
  console.error("Manca slides/ nel repo")
  process.exit(1)
}

if (fs.existsSync(DEST)) fs.rmSync(DEST, { recursive: true, force: true })
copyDir(SRC, DEST)
console.log(`Sincronizzato ${SRC} → ${DEST}`)
