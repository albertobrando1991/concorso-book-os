export const COMMANDS = ["doctor", "init", "status", "next", "gate", "complete", "run", "sync", "reopen", "help"] as const
export type Command = (typeof COMMANDS)[number]

export interface ParsedArgs {
  command: Command
  volumeCode: string
  json: boolean
  force: boolean
  accept: boolean
  step?: string
  chapter?: string
  module?: string
  phase?: string
  from?: string
  fromStep?: string
  owner?: string
  provider?: string
  note?: string
}

const VALUE_FLAGS = ["step", "chapter", "module", "phase", "from", "from-step", "owner", "provider", "note"] as const
const BOOLEAN_FLAGS = ["json", "force", "accept"] as const

export function parseArgs(argv: string[]): ParsedArgs {
  const [rawCommand = "help", ...rest] = argv
  const command = normalizeCommand(rawCommand)
  const positional: string[] = []
  const values = new Map<string, string>()
  const flags = new Set<string>()

  for (let index = 0; index < rest.length; index += 1) {
    const token = rest[index]

    if (!token.startsWith("--")) {
      positional.push(token)
      continue
    }

    const [name, inlineValue] = splitFlag(token.slice(2))

    if ((BOOLEAN_FLAGS as readonly string[]).includes(name) && inlineValue === undefined) {
      flags.add(name)
      continue
    }

    if (!(VALUE_FLAGS as readonly string[]).includes(name)) {
      throw new Error(`Opzione sconosciuta: --${name}. Esegui "pipeline help" per l'elenco dei comandi.`)
    }

    const value = inlineValue ?? rest[++index]

    if (value === undefined || value.startsWith("--")) {
      throw new Error(`L'opzione --${name} richiede un valore.`)
    }

    values.set(name, value)
  }

  return {
    command,
    volumeCode: positional[0] ?? "",
    json: flags.has("json"),
    force: flags.has("force"),
    accept: flags.has("accept"),
    step: values.get("step"),
    chapter: values.get("chapter"),
    module: values.get("module"),
    phase: values.get("phase"),
    from: values.get("from"),
    fromStep: values.get("from-step"),
    owner: values.get("owner"),
    provider: values.get("provider"),
    note: values.get("note")
  }
}

function normalizeCommand(value: string): Command {
  const command = value.trim().toLowerCase()

  if (!(COMMANDS as readonly string[]).includes(command)) {
    throw new Error(`Comando sconosciuto: ${value}. Comandi disponibili: ${COMMANDS.join(", ")}.`)
  }

  return command as Command
}

function splitFlag(token: string): [string, string | undefined] {
  const separator = token.indexOf("=")

  return separator === -1 ? [token, undefined] : [token.slice(0, separator), token.slice(separator + 1)]
}
