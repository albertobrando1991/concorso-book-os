---
name: pipeline-volume
description: Use when running the ConcorsoBook OS editorial pipeline on a volume — executing the 25-prompt protocol chapter by chapter without pasting prompts by hand. Drives the loop next → work → gate → complete through the npm CLI, which owns state, order and gates. Agent-agnostic: works from Codex CLI, Claude Code, Hermes or a human terminal.
---

# Pipeline di volume

Il CLI possiede stato, ordine e gate. Tu esegui il lavoro editoriale. Non tenere lo stato in testa: chiedilo al CLI a ogni passo.

## Ciclo

```
npm run pipeline -- status VOL-03            cosa è fatto, cosa blocca, chi ha in mano cosa
npm run pipeline -- next VOL-03              step successivo, prompt renderizzato su file
# esegui il lavoro descritto dal prompt
npm run pipeline -- complete VOL-03 --step 09 --module M-FC02 --chapter 01
```

`next` scrive il prompt in `artifacts/pipeline/<VOL>/<step>/<target>/prompt.md` e prende in carico lo step a tuo nome. Leggi quel file ed esegui **esattamente** ciò che dice: sotto la riga `---` c'è il prompt canonico del protocollo, non una parafrasi.

Sopra il `---` la pipeline aggiunge il contratto di esecuzione: target, gate, dove scrivere il report, comando di chiusura. Rispettalo, altrimenti il gate non troverà ciò che cerca. I report di revisione vanno in `wiki/reviews/pipeline/<VOL>/<step>-<slug>.md`, nel template fisso del Revisore Editoriale Totale.

Sullo step 11 la pipeline salva lo snapshot del capitolo *prima* del tuo intervento. Non modificare il capitolo prima di aver eseguito `next`: senza snapshot il gate blocca.

`complete` esegue il gate. Se il gate non passa lo step resta `blocked` e **nessuno step a valle può partire**: correggi e ripeti lo stesso step.

Aggiungi `--json` a qualunque comando per ottenere l'esito strutturato invece del testo. Non dedurre l'esito di un gate leggendo il testo formattato.

## Regole non negoziabili

- Non saltare un gate. Non chiudere uno step il cui gate non è passato.
- Ogni capitolo deve superare il contratto dello studente: testo autosufficiente, teoria completa nel perimetro assegnato e nessuna dipendenza nel corpo da wiki, source note, corpus o report interni. La tracciabilità resta nel frontmatter.
- Non modificare a mano `pipeline/<VOL>/run-state.json`: è stato condiviso e versionato.
- Se uno step è in carico a un'altra persona, `next` lo rifiuta. Subentra con `--force` solo dopo esserti accordato.
- `--accept` chiude uno step il cui gate non è ancora automatizzato e richiede `--note` con la motivazione. Usalo solo dopo aver eseguito la verifica a mano.
- Vale tutto ciò che impone `AGENTS.md` e `wiki/AGENTS.md`: niente testo finale da `raw/`, nessuna norma o data inventata, nessun contenuto dichiarato completo con nuclei parziali.

## Memoria

Prima di ogni step LLM richiama `LocalAgentMemory` con lo scope del volume; al termine registra la traccia. Lo store è `wiki/memory/agent/`: non crearne di paralleli. La memoria è suggerimento operativo, mai fonte normativa.

## Skill da usare per step

| Step | Skill |
| --- | --- |
| 09 scrittura | `concorso-book-professional-writer` |
| 11 Humanizer | `humanizer` |
| 12, 13, 21 revisione | `revisore-editoriale-totale` |
| 17, 18 immagini | `canvas-design` |

## Fasi

- **C** (08-12) capitolo: piano, scrittura, copertura, Humanizer, revisione.
- **D** (13-16) modulo: revisione trasversale, correzioni, review umana, text freeze.
- **F** (21-23) volume: revisione finale, preflight, consegna.
- **A**, **B**, **E**, **G** restano manuali: `next` presenta il prompt, il gate automatico non esiste ancora e va dichiarato tale, non simulato.

## Se qualcosa non parte

`npm run pipeline -- doctor` elenca cosa manca sulla macchina e il comando esatto per rimediare. La scheda del volume sta in `wiki/books/**/planning/00-scheda-pipeline.md`; il modello è `wiki/templates/scheda-pipeline-volume-template.md`.
