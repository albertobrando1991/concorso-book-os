#!/usr/bin/env node
import { readFileSync, writeFileSync } from "node:fs"
import { runMergeDriver } from "../../src/pipeline/state/merge-driver"

function main() {
  const [, , basePath, oursPath, theirsPath] = process.argv

  if (!oursPath || !theirsPath) {
    process.stderr.write("Uso: merge-run-state.ts <base> <ours> <theirs> (invocato da Git come merge driver, non a mano)\n")
    process.exitCode = 2
    return
  }

  const baseContent = basePath ? readFileSync(basePath, "utf8") : ""
  const oursContent = readFileSync(oursPath, "utf8")
  const theirsContent = readFileSync(theirsPath, "utf8")
  const result = runMergeDriver({ baseContent, oursContent, theirsContent })

  writeFileSync(oursPath, result.output, "utf8")

  if (!result.ok) {
    process.stderr.write(`${result.diagnostic}\n`)
    process.exitCode = 1
    return
  }

  process.stdout.write(`run-state unito senza conflitti: ${oursPath}\n`)
}

main()
