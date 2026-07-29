# conv-20260703235332-mfc02-cap07-editorial-images

created_at: 2026-07-03T23:53:32+02:00
scope: editorial-design
route: codex/editorial-images/mfc02-chapter07

## Sintesi

Integrate immagini editoriali nel capitolo 7 M-FC02, "Riscossione nazionale e lavoro in AdER", seguendo lo stile dei capitoli M-FC02 gia illustrati e del libro base.

## Analisi stile

Lo stile confermato usa master SVG modificabili, PNG 1600 x 900 per preview/PDF, fondo Off-White, palette Navy/Bordeaux/Muted Gold/Green/Teal, card a raggio contenuto, testi brevi, frecce leggere e funzione didattica esplicita: mappa BANDO, confronto concettuale, sequenza operativa, schema anti-confusione e checklist applicativa.

## Asset creati

- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-07/01-mappa-bando-riscossione-ader.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-07/02-accertamento-riscossione-distinti.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-07/03-flusso-riscossione-nazionale.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-07/04-cartella-rateizzazione-sospensione.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-07/05-front-office-ader-checklist.png

Ogni PNG ha il relativo master SVG e la cartella contiene README con funzione didattica.

## Inserimento

Il capitolo e' stato aggiornato con asset_refs, tag `illustrated` e cinque figure inserite subito dopo le sezioni che sintetizzano: mappa BANDO, distinzione accertamento/riscossione, flusso riscossione, cartella-rateizzazione-sospensione e checklist front-office.

## Verifiche

- `node scripts/run-mfc02-chapter07-preview-verification.cjs`: 14 pagine, 5 immagini caricate, PNG 1600 x 900, immagini dentro pagina, nessuna sovrapposizione footer, SVG text audit 0 issues.
- `node --check` sui tre script del capitolo 7: ok.
- `rg` caratteri non ASCII: ok.
- `git diff --check` sul capitolo 7: ok.
- `npm.cmd test`: 25 test superati.
- `npm.cmd run typecheck`: ok.
- `npm.cmd run build`: ok.
