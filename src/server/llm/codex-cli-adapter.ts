import { spawn } from "node:child_process"
import { mkdtemp, readFile, rm } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import { getProjectRoot, getWriterConfig } from "../config"

export interface CodexCliCompletionResult {
  text: string
  stderr: string
}

export async function completeWithCodexCli(prompt: string): Promise<CodexCliCompletionResult> {
  const config = getWriterConfig()
  const projectRoot = getProjectRoot()
  const tempDir = await mkdtemp(path.join(os.tmpdir(), "concorso-book-codex-"))
  const outputPath = path.join(tempDir, "last-message.md")
  const args = [
    "exec",
    "--ephemeral",
    "--sandbox",
    "read-only",
    "--cd",
    projectRoot,
    "--color",
    "never",
    "--output-last-message",
    outputPath
  ]

  if (config.codexModel) {
    args.push("-m", config.codexModel)
  }

  if (config.codexReasoningEffort) {
    args.push("-c", `model_reasoning_effort="${config.codexReasoningEffort}"`)
  }

  args.push("-")

  try {
    const result = await runCodexProcess({
      command: config.codexCommand,
      args,
      cwd: projectRoot,
      prompt,
      timeoutMs: config.codexTimeoutMs
    })
    const finalMessage = await readFile(outputPath, "utf8").catch(() => result.stdout)

    return {
      text: stripCodexNoise(finalMessage),
      stderr: result.stderr
    }
  } finally {
    await rm(tempDir, { recursive: true, force: true }).catch(() => undefined)
  }
}

function runCodexProcess(input: {
  command: string
  args: string[]
  cwd: string
  prompt: string
  timeoutMs: number
}) {
  return new Promise<{ stdout: string; stderr: string }>((resolve, reject) => {
    const child = spawn(input.command, input.args, {
      cwd: input.cwd,
      env: { ...process.env, NO_COLOR: "1" },
      shell: false,
      windowsHide: true
    })
    let stdout = ""
    let stderr = ""
    const timer = setTimeout(() => {
      child.kill()
      reject(new Error(`Codex CLI timeout after ${input.timeoutMs}ms`))
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
        reject(new Error(`Codex CLI exited with code ${code}: ${trim(stderr || stdout, 1200)}`))
        return
      }

      resolve({ stdout, stderr })
    })

    child.stdin.write(input.prompt)
    child.stdin.end()
  })
}

function stripCodexNoise(value: string) {
  return value
    .replace(/^```markdown\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/```\s*$/i, "")
    .trim()
}

function trim(value: string, limit: number) {
  return value.length > limit ? `${value.slice(0, limit)}...` : value
}
