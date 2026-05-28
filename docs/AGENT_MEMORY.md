# Local Agent Memory

ConcorsoBook OS include un layer di memoria locale ispirato a TencentDB Agent Memory, adattato al runtime del progetto senza dipendere da OpenClaw.

La memoria deve restare sempre attiva nel contesto operativo del progetto. Serve a ricordare preferenze, istruzioni, workflow e risultati ricorrenti, cosi gli output migliorano progressivamente invece di ripartire da zero.

La regola vale per tutti i provider usati dal progetto: Codex/GPT, Claude, Kimi, OpenAI API, Hermes e writer locale. Ogni nuovo agente deve usare lo stesso store `wiki/memory/agent/` invece di creare una memoria separata.

## Cosa fa

- Salva le conversazioni operative in `wiki/memory/agent/l0/`.
- Estrae memorie atomiche in `wiki/memory/agent/l1/atoms.jsonl`.
- Mantiene blocchi scenario ispezionabili in `wiki/memory/agent/l2/scenarios.md`.
- Genera una persona operativa in `wiki/memory/agent/l3/persona.md`.
- Richiama automaticamente solo le memorie pertinenti prima di chiamare Hermes o Manual Writer.

La memoria serve per continuita operativa, preferenze e workflow. Per norme, date, fonti e claim editoriali resta vincolante la knowledge consolidata in `wiki/sources`, `wiki/topics` e `wiki/entities`.

## Punti integrati

- `POST /api/hermes/chat`: richiama memoria prima della risposta e cattura la conversazione dopo la risposta.
- `importSourceForHermes`: registra gli import di fonti, source note create e capitoli collegati.
- `ManualWriterAgent`: richiama memoria prima del prompt per `codex`, `claude`, `kimi`, `openai`, `hermes` e `local`, poi registra il risultato senza salvare l'intera bozza come memoria.
- Dashboard: mostra il conteggio delle memorie locali L1.

## Configurazione

Variabili opzionali:

```text
AGENT_MEMORY_ENABLED=true
AGENT_MEMORY_ROOT=wiki/memory/agent
AGENT_MEMORY_RECALL_MAX_RESULTS=5
AGENT_MEMORY_RECALL_MAX_CHARS=3500
AGENT_MEMORY_MAX_CHARS_PER_MESSAGE=6000
AGENT_MEMORY_MAX_MESSAGES_PER_CONVERSATION=24
AGENT_MEMORY_MAX_ATOMS_PER_CONVERSATION=8
```

La disattivazione va usata solo per debug tecnico:

```text
AGENT_MEMORY_ENABLED=false
```

Il launcher `AVVIA_CONCORSOBOOK.bat` forza `AGENT_MEMORY_ENABLED=true`, quindi nell'uso normale la memoria e' sempre attiva.

## Debug

Apri direttamente:

```text
wiki/memory/agent/l1/atoms.jsonl
wiki/memory/agent/l2/scenarios.md
wiki/memory/agent/l3/persona.md
```

Ogni memoria L1 contiene `sourceRef`, che punta alla conversazione L0 usata come evidenza.
