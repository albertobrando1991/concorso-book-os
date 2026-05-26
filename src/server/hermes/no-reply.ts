import type { LlmMessage } from "../llm/openai-adapter"

export const HERMES_NO_REPLY_TOKEN = "__HERMES_NO_REPLY__"

const HERMES_NO_REPLY_INSTRUCTION = [
  "Hermes puo scegliere di non inviare alcuna risposta.",
  `Quando non serve rispondere, restituisci esattamente ${HERMES_NO_REPLY_TOKEN} e nient'altro.`,
  "Usa questa opzione solo per semplici conferme, duplicati, rumore o messaggi chiaramente rivolti ad altri in chat di gruppo/canale.",
  "In una chat privata con Hermes, considera il messaggio come indirizzato a Hermes anche se non contiene il nome del bot.",
  "Non restare mai silenzioso se il messaggio contiene verbi come scarica, importa, aggiungi, cerca, integra oppure una lista di leggi, decreti, PDF o fonti normative.",
  "Se invece la richiesta e' pertinente ma manca un dato necessario, fai una sola domanda breve di chiarimento."
].join(" ")

export interface HermesParsedReply {
  shouldReply: boolean
  message: string
}

export function withHermesNoReplyCapability(messages: LlmMessage[], enabled: boolean): LlmMessage[] {
  if (!enabled) return messages

  return [
    {
      role: "system",
      content: HERMES_NO_REPLY_INSTRUCTION
    },
    ...messages
  ]
}

export function parseHermesReply(value: string): HermesParsedReply {
  const message = value.trim()

  if (!message || isNoReplyToken(message)) {
    return { shouldReply: false, message: "" }
  }

  return { shouldReply: true, message }
}

function isNoReplyToken(value: string) {
  const normalized = value
    .trim()
    .replace(/^```(?:text)?\s*/i, "")
    .replace(/\s*```$/i, "")
    .replace(/^["'`]+|["'`]+$/g, "")
    .trim()
    .toUpperCase()

  return normalized === HERMES_NO_REPLY_TOKEN || normalized === "HERMES_NO_REPLY" || normalized === "NO_REPLY"
}
