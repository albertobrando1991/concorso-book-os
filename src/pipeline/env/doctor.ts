import { execFile } from "node:child_process"
import { access, readFile } from "node:fs/promises"
import path from "node:path"
import { promisify } from "node:util"
import { PROMPT_TEMPLATE_PATH } from "../steps/prompt-renderer"
import { detectAgent, detectOwner, type AgentEnvironment } from "./detect-agent"

const run = promisify(execFile)

export interface DoctorCheck {
  id: string
  ok: boolean
  message: string
  remedy?: string
}

export interface DoctorInput {
  projectRoot: string
  env?: AgentEnvironment
}

export async function runDoctor(input: DoctorInput): Promise<DoctorCheck[]> {
  const env = input.env ?? process.env

  return [
    await checkNode(input.projectRoot),
    await checkDependencies(input.projectRoot),
    await checkPlaywright(input.projectRoot),
    await checkEnvFile(input.projectRoot),
    checkProvider(env),
    await checkGit(input.projectRoot),
    await checkPromptTemplate(input.projectRoot),
    await checkMergeDriver(input.projectRoot),
    checkAgent(env)
  ]
}

const MERGE_DRIVER_NAME = "pipeline-run-state"
const MERGE_DRIVER_COMMAND = "npx tsx scripts/pipeline/merge-run-state.ts %O %A %B"

async function checkMergeDriver(projectRoot: string): Promise<DoctorCheck> {
  const key = `merge.${MERGE_DRIVER_NAME}.driver`

  try {
    const { stdout } = await run("git", ["config", "--get", key], { cwd: projectRoot })

    if (stdout.trim() === MERGE_DRIVER_COMMAND) {
      return { id: "merge-driver", ok: true, message: "Merge driver del run-state di pipeline già registrato." }
    }
  } catch {
    // non ancora configurato: si registra sotto
  }

  try {
    await run("git", ["config", key, MERGE_DRIVER_COMMAND], { cwd: projectRoot })

    return {
      id: "merge-driver",
      ok: true,
      message: "Merge driver del run-state di pipeline registrato ora (config locale del repository, non globale)."
    }
  } catch (error) {
    return {
      id: "merge-driver",
      ok: false,
      message: `Impossibile registrare il merge driver: ${(error as Error).message}`,
      remedy: `git config ${key} "${MERGE_DRIVER_COMMAND}"`
    }
  }
}

async function checkNode(projectRoot: string): Promise<DoctorCheck> {
  const manifest = JSON.parse(await readFile(path.join(projectRoot, "package.json"), "utf8")) as {
    engines?: { node?: string }
  }
  const required = manifest.engines?.node ?? ">=20.11.0"
  const current = process.versions.node
  const ok = compareVersions(current, required.replace(/[^\d.]/g, "")) >= 0

  return {
    id: "node",
    ok,
    message: `Node ${current} (richiesto ${required})`,
    remedy: ok ? undefined : "Installa la versione indicata in .nvmrc, per esempio con: nvm install 20.11.0"
  }
}

async function checkDependencies(projectRoot: string): Promise<DoctorCheck> {
  const ok = await exists(path.join(projectRoot, "node_modules", "tsx"))

  return {
    id: "dependencies",
    ok,
    message: ok ? "Dipendenze installate (tsx presente)" : "Dipendenze mancanti",
    remedy: ok ? undefined : "npm ci"
  }
}

async function checkPlaywright(projectRoot: string): Promise<DoctorCheck> {
  const installed = await exists(path.join(projectRoot, "node_modules", "@playwright", "test"))

  if (!installed) {
    return { id: "playwright", ok: false, message: "Playwright non installato", remedy: "npm ci" }
  }

  const browsers = await hasChromium()

  return {
    id: "playwright",
    ok: browsers,
    message: browsers
      ? "Browser Chromium disponibile per i gate di impaginazione"
      : "Browser Chromium non installato: i gate 20 e 22 non possono girare",
    remedy: browsers ? undefined : "npx playwright install chromium"
  }
}

async function checkEnvFile(projectRoot: string): Promise<DoctorCheck> {
  const example = await readFile(path.join(projectRoot, ".env.example"), "utf8").catch(() => "")
  const local = await readFile(path.join(projectRoot, ".env.local"), "utf8").catch(() => "")

  if (!local) {
    return {
      id: "env",
      ok: false,
      message: "File .env.local assente",
      remedy: "Copia .env.example in .env.local e compila i valori necessari"
    }
  }

  const declared = keysOf(local)
  const missing = keysOf(example).filter((key) => !declared.includes(key))

  return {
    id: "env",
    ok: true,
    message: missing.length
      ? `File .env.local presente. Non impostate (facoltative, valgono i default di src/server/config.ts): ${missing.join(", ")}`
      : "File .env.local allineato a .env.example",
    remedy: missing.length ? "Impostale solo se usi i servizi corrispondenti; i nomi sono in .env.example" : undefined
  }
}

function checkProvider(env: AgentEnvironment): DoctorCheck {
  const provider = env.WRITER_PROVIDER?.trim() || "codex"
  const requiresKey: Record<string, string> = { openai: "OPENAI_API_KEY", kimi: "KIMI_API_KEY", hermes: "HERMES_HOME" }
  const key = requiresKey[provider]

  if (key && !env[key]) {
    return {
      id: "provider",
      ok: false,
      message: `Provider ${provider} configurato ma ${key} non è impostata`,
      remedy: `Imposta ${key} in .env.local`
    }
  }

  return {
    id: "provider",
    ok: true,
    message: `Provider di scrittura: ${provider}. Se la sua CLI non è disponibile, gli step LLM restano in awaiting-agent con il prompt su file.`
  }
}

async function checkGit(projectRoot: string): Promise<DoctorCheck> {
  try {
    const { stdout } = await run("git", ["rev-parse", "--abbrev-ref", "HEAD"], { cwd: projectRoot })

    return { id: "git", ok: true, message: `Repository git sul branch ${stdout.trim()}` }
  } catch {
    return {
      id: "git",
      ok: false,
      message: "Directory non riconosciuta come repository git",
      remedy: "Clona il progetto da GitHub invece di copiarne i file"
    }
  }
}

async function checkPromptTemplate(projectRoot: string): Promise<DoctorCheck> {
  const ok = await exists(path.join(projectRoot, ...PROMPT_TEMPLATE_PATH.split("/")))

  return {
    id: "prompts",
    ok,
    message: ok
      ? `Protocollo dei 25 prompt disponibile in ${PROMPT_TEMPLATE_PATH}`
      : `Template dei prompt assente: ${PROMPT_TEMPLATE_PATH}`,
    remedy: ok ? undefined : "Aggiorna il repository: la pipeline legge i prompt dal wiki, non ne conserva una copia"
  }
}

function checkAgent(env: AgentEnvironment): DoctorCheck {
  return {
    id: "agent",
    ok: true,
    message: `Agente rilevato: ${detectAgent(env)}; owner degli step: ${detectOwner(env)}. Forzabili con PIPELINE_AGENT e PIPELINE_OWNER.`
  }
}

async function hasChromium() {
  try {
    const { chromium } = await import("@playwright/test")
    const executable = chromium.executablePath()

    return Boolean(executable) && (await exists(executable))
  } catch {
    return false
  }
}

function keysOf(content: string) {
  return content
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#"))
    .map((line) => line.split("=")[0].trim())
    .filter(Boolean)
}

async function exists(target: string) {
  return access(target).then(
    () => true,
    () => false
  )
}

function compareVersions(left: string, right: string) {
  const parse = (value: string) => value.split(".").map((part) => Number.parseInt(part, 10) || 0)
  const current = parse(left)
  const minimum = parse(right)

  for (let index = 0; index < Math.max(current.length, minimum.length); index += 1) {
    const difference = (current[index] ?? 0) - (minimum[index] ?? 0)

    if (difference !== 0) return difference
  }

  return 0
}
