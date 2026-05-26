import { spawn } from "node:child_process"
import { getProjectRoot, getWriterConfig } from "../config"

export interface ClaudeCodeCompletionResult {
  text: string
  stderr: string
}

export async function completeWithClaudeCode(prompt: string): Promise<ClaudeCodeCompletionResult> {
  const config = getWriterConfig()
  const projectRoot = getProjectRoot()
  const args = [
    "--print",
    "--input-format",
    "text",
    "--output-format",
    "text",
    "--no-session-persistence",
    "--permission-mode",
    "dontAsk",
    "--tools="
  ]

  if (config.claudeModel) {
    args.push("--model", config.claudeModel)
  }

  if (config.claudeReasoningEffort) {
    args.push("--effort", config.claudeReasoningEffort)
  }

  const result = await runClaudeProcess({
    command: config.claudeCommand,
    args,
    cwd: projectRoot,
    prompt,
    timeoutMs: config.claudeTimeoutMs
  })

  return {
    text: stripClaudeNoise(result.stdout),
    stderr: result.stderr
  }
}

function runClaudeProcess(input: {
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
      reject(new Error(`Claude Code timeout after ${input.timeoutMs}ms`))
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
        reject(new Error(`Claude Code exited with code ${code}: ${trim(stderr || stdout, 1200)}`))
        return
      }

      resolve({ stdout, stderr })
    })

    child.stdin.write(input.prompt)
    child.stdin.end()
  })
}

function stripClaudeNoise(value: string) {
  return value
    .replace(/^```markdown\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/```\s*$/i, "")
    .trim()
}

function trim(value: string, limit: number) {
  return value.length > limit ? `${value.slice(0, limit)}...` : value
}
