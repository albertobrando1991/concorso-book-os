import { spawn } from "node:child_process"
import { mkdtemp, readdir, readFile, rm, stat } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { getGlmOcrConfig, getProjectRoot } from "../config"

export interface GlmOcrResult {
  markdown: string
  outputFiles: string[]
  warnings: string[]
}

export async function extractPdfMarkdownWithGlmOcr(pdfPath: string): Promise<GlmOcrResult> {
  const config = getGlmOcrConfig()

  if (!config.enabled) {
    return {
      markdown: "",
      outputFiles: [],
      warnings: ["GLM-OCR disabilitato. Imposta GLM_OCR_ENABLED=true per estrarre automaticamente i PDF."]
    }
  }

  const tempDir = await mkdtemp(path.join(os.tmpdir(), "concorso-book-glm-ocr-"))
  const args = ["parse", pdfPath, "--output", tempDir]

  if (config.configPath) {
    args.push("--config", config.configPath)
  }

  if (config.layoutDevice) {
    args.push("--layout-device", config.layoutDevice)
  }

  try {
    await runProcess({
      command: config.command,
      args,
      cwd: getProjectRoot(),
      timeoutMs: config.timeoutMs
    })

    const outputFiles = await listFiles(tempDir)
    const markdownFiles = outputFiles.filter((file) => file.toLowerCase().endsWith(".md"))
    const markdownParts = []

    for (const file of markdownFiles) {
      const content = await readFile(file, "utf8")
      if (content.trim()) {
        markdownParts.push(`<!-- GLM-OCR output: ${path.basename(file)} -->\n\n${content.trim()}`)
      }
    }

    if (markdownParts.length === 0) {
      return {
        markdown: "",
        outputFiles,
        warnings: ["GLM-OCR completato, ma non ha prodotto file Markdown leggibili."]
      }
    }

    return {
      markdown: markdownParts.join("\n\n---\n\n"),
      outputFiles,
      warnings: []
    }
  } catch (error) {
    return {
      markdown: "",
      outputFiles: [],
      warnings: [`GLM-OCR non disponibile o fallito: ${error instanceof Error ? error.message : "errore sconosciuto"}`]
    }
  } finally {
    await rm(tempDir, { recursive: true, force: true }).catch(() => undefined)
  }
}

function runProcess(input: {
  command: string
  args: string[]
  cwd: string
  timeoutMs: number
}) {
  return new Promise<void>((resolve, reject) => {
    const child = spawn(input.command, input.args, {
      cwd: input.cwd,
      env: process.env,
      shell: false,
      windowsHide: true
    })
    let stdout = ""
    let stderr = ""
    const timer = setTimeout(() => {
      child.kill()
      reject(new Error(`GLM-OCR timeout after ${input.timeoutMs}ms`))
    }, input.timeoutMs)

    child.stdout.on("data", (chunk: Buffer) => {
      stdout += chunk.toString("utf8")
    })
    child.stderr.on("data", (chunk: Buffer) => {
      stderr += chunk.toString("utf8")
    })
    child.on("error", (error) => {
      clearTimeout(timer)
      reject(error)
    })
    child.on("close", (code) => {
      clearTimeout(timer)

      if (code !== 0) {
        reject(new Error(`GLM-OCR exited with code ${code}: ${trim(stderr || stdout, 1200)}`))
        return
      }

      resolve()
    })
  })
}

async function listFiles(directory: string) {
  const files: string[] = []

  async function walk(current: string) {
    const entries = await readdir(current, { withFileTypes: true })

    for (const entry of entries) {
      const absolutePath = path.join(current, entry.name)

      if (entry.isDirectory()) {
        await walk(absolutePath)
        continue
      }

      if (entry.isFile()) {
        const fileStat = await stat(absolutePath)
        if (fileStat.size > 0) files.push(absolutePath)
      }
    }
  }

  await walk(directory)

  return files.sort()
}

function trim(value: string, limit: number) {
  return value.length > limit ? `${value.slice(0, limit)}...` : value
}
