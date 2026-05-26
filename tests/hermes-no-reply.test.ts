import { describe, expect, it } from "vitest"
import {
  HERMES_NO_REPLY_TOKEN,
  parseHermesReply,
  withHermesNoReplyCapability
} from "@/src/server/hermes/no-reply"
import type { LlmMessage } from "@/src/server/llm/openai-adapter"

describe("Hermes no-reply support", () => {
  it("marks blank responses and no-reply tokens as silent", () => {
    expect(parseHermesReply("")).toEqual({ shouldReply: false, message: "" })
    expect(parseHermesReply(` ${HERMES_NO_REPLY_TOKEN} `)).toEqual({ shouldReply: false, message: "" })
    expect(parseHermesReply("`NO_REPLY`")).toEqual({ shouldReply: false, message: "" })
    expect(parseHermesReply("```text\n__HERMES_NO_REPLY__\n```")).toEqual({ shouldReply: false, message: "" })
  })

  it("preserves real replies", () => {
    expect(parseHermesReply(" Fonte importata. ")).toEqual({
      shouldReply: true,
      message: "Fonte importata."
    })
  })

  it("prepends the no-reply instruction only when enabled", () => {
    const messages: LlmMessage[] = [{ role: "user", content: "ok" }]

    expect(withHermesNoReplyCapability(messages, false)).toBe(messages)

    const enabled = withHermesNoReplyCapability(messages, true)
    expect(enabled).toHaveLength(2)
    expect(enabled[0].role).toBe("system")
    expect(enabled[0].content).toContain(HERMES_NO_REPLY_TOKEN)
    expect(enabled[1]).toBe(messages[0])
  })
})
