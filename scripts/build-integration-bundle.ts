import path from "node:path"
import {
  IntegrationReleaseBlockedError,
  buildBookIntegrationBundle,
  writeBookIntegrationBundle,
  type IntegrationBundleChannel
} from "../src/server/book/book-integration-bundle"

interface CliOptions {
  volumeCode: string
  channel: IntegrationBundleChannel
  sourceSha: string
  outputDirectory: string
}

async function main() {
  const projectRoot = process.cwd()
  const options = parseArgs(process.argv.slice(2), projectRoot)
  const bundle = await buildBookIntegrationBundle({
    projectRoot,
    volumeCode: options.volumeCode,
    channel: options.channel,
    sourceSha: options.sourceSha
  })
  const written = await writeBookIntegrationBundle(projectRoot, options.outputDirectory, bundle)

  process.stdout.write(`${JSON.stringify({
    ok: true,
    schemaVersion: bundle.schemaVersion,
    bundleId: bundle.bundleId,
    bundleDigest: bundle.bundleDigest,
    contentDigest: bundle.contentDigest,
    channel: bundle.channel,
    releaseEligible: bundle.gate.releaseEligible,
    blockers: bundle.gate.blockers,
    counts: bundle.volume.counts,
    assets: bundle.assets.length,
    media: {
      video: bundle.media.video.length,
      audio: bundle.media.audio.length,
      slides: bundle.media.slides.length,
      renders: bundle.media.renders.length
    },
    outputDirectory: written.outputDirectory
  }, null, 2)}\n`)
}

function parseArgs(args: string[], projectRoot: string): CliOptions {
  const values = new Map<string, string>()

  for (let index = 0; index < args.length; index += 1) {
    const key = args[index]

    if (!key?.startsWith("--")) throw usage(`Argomento inatteso: ${key || ""}.`)
    const value = args[index + 1]
    if (!value || value.startsWith("--")) throw usage(`Valore mancante per ${key}.`)
    values.set(key, value)
    index += 1
  }

  const volumeCode = required(values, "--volume").toUpperCase()
  const channel = required(values, "--channel")
  const sourceSha = required(values, "--source-sha").toLowerCase()

  if (channel !== "candidate" && channel !== "release") {
    throw usage("--channel deve essere candidate oppure release.")
  }

  return {
    volumeCode,
    channel,
    sourceSha,
    outputDirectory: path.resolve(
      projectRoot,
      values.get("--out") || path.join("output", "integration", volumeCode, `${channel}-${sourceSha}`)
    )
  }
}

function required(values: Map<string, string>, key: string) {
  const value = values.get(key)?.trim()
  if (!value) throw usage(`Parametro obbligatorio mancante: ${key}.`)
  return value
}

function usage(message: string) {
  return new Error(
    `${message}\nUso: npm run bundle:integration -- --volume VOL-01 --channel candidate --source-sha <sha40> [--out <directory>]`
  )
}

main().catch((error: unknown) => {
  if (error instanceof IntegrationReleaseBlockedError) {
    process.stderr.write(`${JSON.stringify({
      ok: false,
      error: error.message,
      bundleId: error.bundle.bundleId,
      contentDigest: error.bundle.contentDigest,
      blockers: error.bundle.gate.blockers
    }, null, 2)}\n`)
    process.exitCode = 1
    return
  }

  process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`)
  process.exitCode = 1
})
