# Task 2 report

Status: DONE

## Commit

- `de8f562 feat: add didactic coverage audit`
- Commit isolato ai cinque file autorizzati.

## RED evidence

- Comando: `npx vitest run tests/didactic-coverage.test.ts`
- Prima esecuzione sandbox: startup bloccato da `esbuild` con `spawn EPERM`.
- Riesecuzione autorizzata fuori sandbox: exit 1, suite non raccolta perché `../src/server/editorial/didactic-coverage` non esisteva. Il fallimento era quello atteso per la nuova API.

## GREEN evidence

- `npx vitest run tests/didactic-coverage.test.ts`: 1 file, 6 test superati.
- `npm test`: 12 file, 38 test superati.
- `npm run typecheck`: exit 0.
- `npm run audit:coverage`: exit 0 con messaggio esplicito `nessuna matrice *-matrice-copertura-didattica.md trovata`.
- `git diff --check -- wiki/templates/didactic-coverage-matrix-template.md src/server/editorial/didactic-coverage.ts scripts/audit-didactic-coverage.mjs tests/didactic-coverage.test.ts package.json`: exit 0.

## Implementazione

- Parser TypeScript della tabella Markdown e audit puro con blocker, warning e conteggio delle righe complete.
- Test per riga completa, `solo-nominato`, rinvio senza destinazione, fonte mancante, stato invalido e riga `completo` priva di teoria/applicazione/verifica.
- Template Markdown con tutte le colonne richieste, inclusa la destinazione del rinvio.
- CLI ricorsiva per `*-matrice-copertura-didattica.md`, riepilogo per file e exit 1 in presenza di blocker.
- Script npm `audit:coverage` senza nuove dipendenze.

## Concerns

- Vitest emette l'avviso preesistente sulla deprecazione della CJS build della Node API di Vite; non incide sull'esito.
- Su Windows il wrapper sandbox ha impedito in modo intermittente gli update via `apply_patch`; i nuovi file sono stati creati singolarmente e la patch minima a `package.json` è stata applicata dal coordinatore. Nessun file utente estraneo è stato incluso nel commit.
- Il richiamo iniziale di `LocalAgentMemory` non è stato completato perché l'esecuzione diretta del modulo TypeScript non risolve gli import ESM extensionless; non è stata usata la memoria come fonte normativa né modificato il relativo store.

## Review fixes

- RED: 16 test eseguiti, 4 fallimenti attesi (tre rinvii generici e tokenizer Markdown).
- GREEN: 16/16 test mirati e 48/48 suite completa.
- Gate: typecheck, audit senza matrici e diff-check con exit 0.
- Implementata una regola di precisione dei rinvii che blocca destinazioni generiche e accetta percorsi/wikilink con sezione o riferimenti espliciti a capitolo/paragrafo.
- Implementato tokenizer per pipe escaped, alias nei wikilink Obsidian e inline code.
- Aggiunti test E2E della CLI per scansione ricorsiva, nessuna matrice, blocker, exit code e riepilogo.
## Residual review fixes

- RED: 4 fallimenti attesi su 20 test (tre rinvii umani precisi e code span con backtick multipli).
- GREEN: 20/20 test mirati e 52/52 suite completa.
- Gate: typecheck, audit e diff-check con exit 0.
- Riconosciuti riferimenti VOL/M/volume con capitolo e paragrafo espliciti.
- Tokenizer TS/CLI aggiornato per delimiter run di backtick multipli.