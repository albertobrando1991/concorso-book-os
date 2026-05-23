import fs from "node:fs/promises"
import path from "node:path"
import process from "node:process"

const projectRoot = process.cwd()
const source = path.join(projectRoot, "hermes", "skills", "concorso-book-os")
const hermesHome = process.env.HERMES_HOME || path.join(process.env.USERPROFILE || process.env.HOME || "", ".hermes")
const target = path.join(hermesHome, "skills", "concorso-book-os")

if (!hermesHome || hermesHome === ".hermes") {
  throw new Error("Cannot determine HERMES_HOME. Set HERMES_HOME explicitly.")
}

await fs.mkdir(path.dirname(target), { recursive: true })
await fs.rm(target, { recursive: true, force: true })
await copyDirectory(source, target)

console.log(`Installed Hermes skill: ${target}`)

async function copyDirectory(from, to) {
  const entries = await fs.readdir(from, { withFileTypes: true })
  await fs.mkdir(to, { recursive: true })

  for (const entry of entries) {
    const sourcePath = path.join(from, entry.name)
    const targetPath = path.join(to, entry.name)

    if (entry.isDirectory()) {
      await copyDirectory(sourcePath, targetPath)
      continue
    }

    if (entry.isFile()) {
      await fs.copyFile(sourcePath, targetPath)
    }
  }
}
