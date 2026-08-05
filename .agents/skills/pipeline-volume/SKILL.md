---
name: pipeline-volume
description: Use when executing or resuming the ConcorsoBook OS 25-step editorial pipeline for a volume, module, or chapter, especially when CLI state, gates, staff planning, or reader-visible chapter files are involved.
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

La conferma umana non è un prerequisito di apertura, scrittura, audit specialistico o text freeze. Lo step 15 è un audit specialistico automatico che deve chiudere ogni criticità nel testo; l'unico step umano è il 24, ultimo del protocollo, che conferma o respinge la validità del pacchetto già completo. Non assegnare preventivamente nomi di revisori nella scheda volume.

## Formato 2 e gate del capitolo

Il contratto prodotto da `next` espone le soglie effettive del capitolo: usa quelle, comprese le eventuali personalizzazioni `Min parole` e `Min quiz` della scheda volume. Non sostituirle con valori ricordati o stimati.

Per lo step 09, un capitolo nuovo deve dichiarare `format_version: 2` nel frontmatter ed essere organizzato in almeno cinque nuclei numerati (`1.1`, `1.2`, ...). Ogni nucleo deve raggiungere almeno 600 parole e avere una verifica vicina; il capitolo deve contenere almeno sei quiz e un caso applicativo. Le soglie dichiarate dal contratto prevalgono su questi default.

Lo step 10 è un gate composito: verifica copertura, dimensioni didattiche, densità dei nuclei e risoluzione dei rinvii al volume `il-metodo-bando`. Un capitolo legacy può ricevere il warning `retrofit-dovuto`, che da solo non blocca; qualunque blocker resta invece vincolante e impedisce la chiusura. Non promuovere un capitolo legacy al formato 2 finché matrice, checklist qualitativa, verifiche e rinvii non sono completi.

## Regole non negoziabili

- Non saltare un gate. Non chiudere uno step il cui gate non è passato.
- Ogni capitolo deve superare il contratto dello studente: testo autosufficiente, teoria completa nel perimetro assegnato e nessuna dipendenza nel corpo da wiki, source note, corpus o report interni. La tracciabilità resta nel frontmatter.
- Non modificare a mano `pipeline/<VOL>/run-state.json`: è stato condiviso e versionato. Un merge driver dedicato lo unisce per-step a ogni `git pull`; se compaiono marcatori `<<<<<<< HEAD / ======= / >>>>>>> incoming`, è un vero conflitto (due persone sullo stesso step) — risolvilo leggendo entrambi i blocchi, non sceglierne uno alla cieca.
- Se uno step è in carico a un'altra persona, `next` lo rifiuta. Subentra con `--force` solo dopo esserti accordato.
- `--accept` chiude uno step il cui gate non è ancora automatizzato e richiede `--note` con la motivazione. Usalo solo dopo aver eseguito la verifica a mano.
- Vale tutto ciò che impone `AGENTS.md` e `wiki/AGENTS.md`: niente testo finale da `raw/`, nessuna norma o data inventata, nessun contenuto dichiarato completo con nuclei parziali.

## Contratto indice studente e piano staff

- `chapters/` contiene esclusivamente testo destinato al lettore. Non salvare qui piani, matrici, prompt, review o checklist interne.
- `planning/` contiene gli artefatti editoriali interni. Il piano di modulo canonico è `planning/00-piano-editoriale.md`, con `type: editorial_plan` e tag `specialist-module-plan`.
- Un capitolo entra nel piano staff quando è dichiarato nella scheda della pipeline. Non inventare target da note, prompt o nomi plausibili.
- Un capitolo entra nell'indice studente soltanto quando il file editoriale dichiarato esiste in `chapters/`.
- La sezione `Piano editoriale staff` della dashboard mostra specifica e run-state; l'anteprima commerciale mostra soltanto il libro destinato allo studente.
- Codice e titolo visibili usano il trattino lungo: `M-SA01 — Sanità amministrativa`; la UI staff mostra `Capitolo 03 — Titolo`.
- Non modificare manualmente `pipeline/<VOL>/run-state.json`: usa `next`, `gate`, `complete` e `sync`.

## Memoria

Prima di ogni step LLM richiama `LocalAgentMemory` con lo scope del volume; al termine registra la traccia. Lo store è `wiki/memory/agent/`: non crearne di paralleli. La memoria è suggerimento operativo, mai fonte normativa.

## Skill da usare per step

| Step | Skill |
| --- | --- |
| 09 scrittura | `concorso-book-professional-writer` |
| 11 Humanizer | `humanizer` |
| 12, 13, 15, 21 revisione | `revisore-editoriale-totale` |
| 17, 18 immagini | `canvas-design` |

## Fasi

- **C** (08-12) capitolo: piano, scrittura, copertura, Humanizer, revisione.
- **D** (13-16) modulo: revisione trasversale, correzioni, audit specialistico automatico, text freeze.
- **F** (21-24) volume: revisione finale, preflight, preparazione della consegna, conferma umana conclusiva.
- **A**, **B** ed **E** restano manuali: `next` presenta il prompt, il gate automatico non esiste ancora e va dichiarato tale, non simulato.

## Se qualcosa non parte

`npm run pipeline -- doctor` elenca cosa manca sulla macchina e il comando esatto per rimediare. La scheda del volume sta in `wiki/books/**/planning/00-scheda-pipeline.md`; il modello è `wiki/templates/scheda-pipeline-volume-template.md`.
