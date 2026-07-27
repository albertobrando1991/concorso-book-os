# ConcorsoBook OS Agent Instructions

Questa repo usa `wiki/AGENTS.md` come schema operativo canonico.

Regole persistenti per gli agenti che lavorano qui:
- Leggi e rispetta `wiki/AGENTS.md` prima di modificare workflow editoriali o agentici.
- Mantieni attiva la memoria locale in `wiki/memory/agent/`.
- Usa `LocalAgentMemory` per richiamare preferenze e decisioni operative pertinenti prima di generare output AI, qualunque sia il provider usato: Codex/GPT, Claude, Kimi, OpenAI API, Hermes o locale.
- Dopo flussi agentici importanti, registra una traccia sintetica in memoria.
- La memoria aiuta continuita e qualita degli output, ma non sostituisce source notes, topic pages ed entity pages per contenuti normativi.

## Pipeline editoriale di volume

Il protocollo dei 25 prompt si esegue attraverso il CLI, non incollando i prompt a mano:

```
npm run pipeline -- doctor
npm run pipeline -- status VOL-03
npm run pipeline -- next VOL-03
npm run pipeline -- complete VOL-03 --step 09 --module M-FC02 --chapter 01
```

- Il CLI possiede stato, ordine e gate; l'agente esegue il lavoro editoriale. Vale per qualunque agente: Codex CLI, Claude Code, Hermes o una persona.
- Istruzioni operative: `.agents/skills/pipeline-volume/SKILL.md` (corpo canonico). Guida per lo staff: `docs/PIPELINE.md`.
- I prompt restano in `wiki/templates/prompt-staff-revisione-completa-volumi.md`: il CLI li legge da lì e non ne conserva copie.
- Ogni comando accetta `--json`: non dedurre l'esito di un gate leggendo il testo formattato.
- Nessuno step a valle parte se un gate non passa. Un gate non ancora automatizzato risponde `gate-not-implemented` e blocca: va verificato a mano e chiuso con `--accept --note`, mai dichiarato verde.
- Il run-state in `pipeline/<VOL>/run-state.json` è condiviso e versionato: non modificarlo a mano.
