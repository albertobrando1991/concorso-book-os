# VOL-07 — Avvio progressivo della scrittura

## Obiettivo

Portare VOL-07 dalla fase preparatoria A-B alla scrittura effettiva del primo capitolo, mantenendo il CLI come unico proprietario dell'ordine, dello stato e dei gate.

## Decisione

La fase C viene aperta in modo progressivo, iniziando da M-SA02, primo modulo previsto dalla Bibbia del Volume. Non vengono generati in anticipo tutti gli scaffold dei quattro moduli.

Il primo target editoriale è:

- modulo: `M-SA02`;
- capitolo: `chapters/01-mappa-profili-e-prove.md`;
- matrice: `planning/02-matrice-copertura-didattica.md`;
- stato atteso della copertura: `completo`.

## Modifiche previste

1. Aggiornare la scheda `00-scheda-pipeline.md`:
   - aggiungere la fase C alle fasi globali;
   - abilitare C soltanto per M-SA02;
   - dichiarare esplicitamente il primo capitolo nella tabella `## Capitoli M-SA02`.
2. Eseguire `npm run pipeline -- sync VOL-07 --json`.
3. Verificare che il CLI aggiunga gli step 08-12 per il solo capitolo dichiarato, senza perdere i 17 step già conclusi.
4. Aprire lo step 08 con `pipeline next` e produrre il piano operativo del capitolo.
5. Chiudere il gate manuale `chapter-plan` solo dopo verifica puntuale e nota motivata.
6. Aprire lo step 09 e scrivere il capitolo completo secondo:
   - Bibbia del Volume;
   - matrice M-SA02;
   - source note consolidate;
   - skill `concorso-book-professional-writer`;
   - struttura ricorrente dei capitoli sanitari.

## Confini

- `pipeline/VOL-07/run-state.json` non viene modificato manualmente.
- Non si abilitano ancora le fasi D-F.
- Non si dichiarano capitoli successivi finché il primo ciclo non dimostra che target, matrice e gate sono coerenti.
- Il capitolo resta non esecutivo nelle procedure cliniche o professionali che richiedono setting, protocollo locale o review specialistica.
- Lo step 09 produce una bozza editoriale completa, non un testo congelato o pubblicabile.

## Flusso e gate

```text
scheda aggiornata
      ↓
pipeline sync
      ↓
08 piano capitolo ── gate manuale chapter-plan
      ↓
09 scrittura ─────── gate automatico chapter-lint
      ↓
10 copertura ─────── gate automatico coverage
      ↓
11 humanizer ─────── gate automatico citation-guard
      ↓
12 revisione ─────── gate automatico review-report
```

## Gestione degli errori

- Se `sync` non aggiunge esattamente gli step attesi, si interrompe l'avanzamento e si confrontano specifica caricata, capitoli risolti e differenza del run-state.
- Se il gate 08 non è automatizzato, la chiusura usa `--accept --note` con evidenze verificabili; non viene dichiarato verde automaticamente.
- Se il gate 09 o 10 fallisce, si corregge il capitolo o la matrice e si ripete lo stesso step.
- Nessuno step successivo parte con blocker aperti.

## Verifica

Prima di dichiarare completato il ciclo:

- `pipeline status VOL-07 --json`;
- test mirati della pipeline e dei gate interessati;
- typecheck;
- `git diff --check`;
- controllo che non siano stati introdotti segnaposto, riferimenti normativi non tracciati o perdite di source refs;
- registrazione sintetica del flusso in `LocalAgentMemory`.

## Criterio di successo

Il design è riuscito quando:

1. i 17 step A-B restano conclusi;
2. lo step 08 compare per il solo primo capitolo M-SA02;
3. il piano operativo supera la verifica manuale;
4. lo step 09 produce il primo capitolo completo e supera `chapter-lint`;
5. il run-state è stato aggiornato esclusivamente dal CLI.
