import { readdir, readFile } from "node:fs/promises"
import path from "node:path"
import { hashContent } from "../state/run-state-store"
import { parseVolumeSpec, type VolumeSpec, type VolumeSpecModule } from "./parse-volume-spec"
import { validateVolumeSpec, type SpecIssue } from "./validate-volume-spec"

export const SPEC_FILE_NAME = "00-scheda-pipeline.md"

export interface LoadedVolumeSpec {
  spec: VolumeSpec
  specFile: string
  specHash: string
  issues: SpecIssue[]
}

export async function loadVolumeSpec(input: { wikiRoot: string; volumeCode: string }): Promise<LoadedVolumeSpec> {
  const candidates = await findSpecFiles(path.join(input.wikiRoot, "books"))
  const wanted = input.volumeCode.trim().toUpperCase()

  for (const specFile of candidates) {
    const content = await readFile(specFile, "utf8")
    const relativePath = toPosix(path.relative(input.wikiRoot, specFile))
    const parsed = parseVolumeSpec(content, relativePath)

    if (parsed.volumeCode.trim().toUpperCase() !== wanted) continue

    const spec = await withResolvedChapters(parsed, input.wikiRoot)

    return { spec, specFile, specHash: hashContent(content), issues: validateVolumeSpec(spec) }
  }

  throw new Error(
    `Nessuna scheda di pipeline per ${input.volumeCode}: attesa una nota con "volume_code: ${input.volumeCode}" in wiki/books/**/planning/${SPEC_FILE_NAME}. Copia wiki/templates/scheda-pipeline-volume-template.md e compilala.`
  )
}

async function withResolvedChapters(spec: VolumeSpec, wikiRoot: string): Promise<VolumeSpec> {
  const modules = await Promise.all(
    spec.modules.map(async (module) => (module.chaptersSource === "declared" ? module : deriveChapters(module, wikiRoot)))
  )

  return { ...spec, modules }
}

async function deriveChapters(module: VolumeSpecModule, wikiRoot: string): Promise<VolumeSpecModule> {
  const directory = path.join(wikiRoot, "books", ...module.moduleId.split("/"), "chapters")
  const files = await listMarkdown(directory)

  return {
    ...module,
    chapters: files.map((file) => ({
      number: /^(\d+[a-z]?)/i.exec(file)?.[1] ?? file.replace(/\.md$/i, ""),
      title: "",
      file: `chapters/${file}`,
      matrix: "",
      expectedStatus: "",
      notes: ""
    }))
  }
}

async function listMarkdown(directory: string) {
  try {
    const entries = await readdir(directory, { withFileTypes: true })

    return entries
      .filter((entry) => entry.isFile() && entry.name.endsWith(".md") && !entry.name.startsWith("_"))
      .map((entry) => entry.name)
      .sort((left, right) => left.localeCompare(right, "it"))
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return []

    throw error
  }
}

async function findSpecFiles(root: string): Promise<string[]> {
  const entries = await readdir(root, { withFileTypes: true }).catch((error: NodeJS.ErrnoException) => {
    if (error.code === "ENOENT") return []

    throw error
  })

  const nested = await Promise.all(
    entries.filter((entry) => entry.isDirectory()).map((entry) => findSpecFiles(path.join(root, entry.name)))
  )
  const here = entries
    .filter((entry) => entry.isFile() && entry.name === SPEC_FILE_NAME)
    .map((entry) => path.join(root, entry.name))

  return [...here, ...nested.flat()].sort()
}

function toPosix(value: string) {
  return value.split(path.sep).join("/")
}
