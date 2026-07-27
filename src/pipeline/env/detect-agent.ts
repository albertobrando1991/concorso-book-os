export const AGENT_IDS = ["codex-cli", "claude-code", "hermes", "human", "unknown"] as const
export type AgentId = (typeof AGENT_IDS)[number]

export interface AgentEnvironment {
  [key: string]: string | undefined
}

export function detectAgent(env: AgentEnvironment = process.env): AgentId {
  if (env.PIPELINE_AGENT && AGENT_IDS.includes(env.PIPELINE_AGENT as AgentId)) return env.PIPELINE_AGENT as AgentId
  if (env.CLAUDECODE || env.CLAUDE_CODE_ENTRYPOINT || env.CLAUDE_CODE_SESSION_ID) return "claude-code"
  if (env.CODEX_SANDBOX || env.CODEX_HOME || env.CODEX_CLI_VERSION) return "codex-cli"
  if (env.HERMES_HOME || env.HERMES_SESSION) return "hermes"

  return "unknown"
}

export function detectOwner(env: AgentEnvironment = process.env) {
  const candidate = env.PIPELINE_OWNER || env.GIT_AUTHOR_NAME || env.GIT_COMMITTER_NAME || env.USERNAME || env.USER || env.LOGNAME

  return candidate?.trim() || "sconosciuto"
}
