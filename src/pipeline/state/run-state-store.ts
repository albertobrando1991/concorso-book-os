import { createHash } from "node:crypto"
import { mkdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"
import type { RunState } from "./types"

export const PIPELINE_DIRECTORY = "pipeline"

export function runStateDirectory(projectRoot: string, volumeCode: string) {
  return path.join(projectRoot, PIPELINE_DIRECTORY, volumeCode)
}

export function runStatePath(projectRoot: string, volumeCode: string) {
  return path.join(runStateDirectory(projectRoot, volumeCode), "run-state.json")
}

export function hashContent(content: string) {
  return `sha256:${createHash("sha256").update(content.replace(/\r\n/g, "\n"), "utf8").digest("hex")}`
}

export async function loadRunState(projectRoot: string, volumeCode: string): Promise<RunState | null> {
  const file = runStatePath(projectRoot, volumeCode)

  try {
    return parseRunState(await readFile(file, "utf8"), file)
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return null

    throw error
  }
}

export async function saveRunState(projectRoot: string, state: RunState) {
  const file = runStatePath(projectRoot, state.volumeCode)
  await mkdir(path.dirname(file), { recursive: true })
  await writeFile(file, `${JSON.stringify(state, null, 2)}\n`, "utf8")

  return file
}

export function parseRunState(content: string, file: string): RunState {
  const parsed = safeParse(content, file)

  if (!parsed || typeof parsed !== "object" || !Array.isArray((parsed as RunState).steps)) {
    throw new Error(`Run-state non valido in ${file}: manca l'elenco degli step. Rigenera lo stato con "pipeline init".`)
  }

  return parsed as RunState
}

function safeParse(content: string, file: string): unknown {
  try {
    return JSON.parse(content)
  } catch (error) {
    throw new Error(
      `Run-state illeggibile in ${file}: ${(error as Error).message}. Recupera la versione dal repository o rigenera con "pipeline init".`
    )
  }
}
