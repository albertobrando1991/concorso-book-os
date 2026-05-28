# ConcorsoBook OS Agent Instructions

Questa repo usa `wiki/AGENTS.md` come schema operativo canonico.

Regole persistenti per gli agenti che lavorano qui:
- Leggi e rispetta `wiki/AGENTS.md` prima di modificare workflow editoriali o agentici.
- Mantieni attiva la memoria locale in `wiki/memory/agent/`.
- Usa `LocalAgentMemory` per richiamare preferenze e decisioni operative pertinenti prima di generare output AI, qualunque sia il provider usato: Codex/GPT, Claude, Kimi, OpenAI API, Hermes o locale.
- Dopo flussi agentici importanti, registra una traccia sintetica in memoria.
- La memoria aiuta continuita e qualita degli output, ma non sostituisce source notes, topic pages ed entity pages per contenuti normativi.
