#!/usr/bin/env node
import { parseArgs } from "../../src/pipeline/cli/args"
import { runCommand } from "../../src/pipeline/cli/commands"

async function main() {
  const argv = process.argv.slice(2)
  const json = argv.includes("--json")

  try {
    const args = parseArgs(argv)
    const result = await runCommand(args)

    process.stdout.write(args.json ? `${JSON.stringify(result.payload, null, 2)}\n` : `${result.lines.join("\n")}\n`)
    process.exitCode = result.exitCode
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error)

    if (json) process.stdout.write(`${JSON.stringify({ ok: false, error: message }, null, 2)}\n`)
    else process.stderr.write(`${message}\n`)

    process.exitCode = 1
  }
}

void main()
