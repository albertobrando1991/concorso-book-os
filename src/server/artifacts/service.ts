import fs from "node:fs/promises"
import path from "node:path"
import { getArtifactsRoot } from "../config"
import type { AgentArtifact } from "../wiki/types"

export async function listArtifacts(): Promise<AgentArtifact[]> {
  const root = getArtifactsRoot()
  const files: string[] = []

  await walk(root)

  return files
    .filter((file) => file.endsWith(".md"))
    .sort()
    .map((file) => ({
      title: titleFromFile(file),
      path: path.relative(process.cwd(), file).replace(/\\/g, "/"),
      kind: kindFromFile(file)
    }))

  async function walk(directory: string) {
    try {
      const entries = await fs.readdir(directory, { withFileTypes: true, encoding: "utf8" })

      for (const entry of entries) {
        const absolutePath = path.join(directory, entry.name)

        if (entry.isDirectory()) {
          await walk(absolutePath)
          continue
        }

        files.push(absolutePath)
      }
    } catch {
      return
    }
  }
}

function titleFromFile(file: string) {
  return path
    .basename(file, ".md")
    .replace(/-/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
}

function kindFromFile(file: string): AgentArtifact["kind"] {
  const lower = file.toLowerCase()

  if (lower.includes("wireframe")) return "wireframe"
  if (lower.includes("task")) return "task-list"
  if (lower.includes("plan")) return "plan"
  if (lower.includes("screenshot")) return "screenshot"
  if (lower.includes("summary")) return "summary"

  return "report"
}
