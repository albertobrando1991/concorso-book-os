# conv-20260703232436-mfc02-cap06-editorial-images

created_at: 2026-07-03T23:24:36+02:00
scope: editorial-design
route: codex/editorial-images/mfc02-chapter06

## Sintesi

Integrate immagini editoriali nel capitolo 6 M-FC02, "Adempimenti fiscali: redditi, IVA, dichiarazioni", seguendo lo stile dei capitoli M-FC02 gia illustrati e del libro base.

## Analisi stile

Lo stile confermato usa master SVG modificabili, PNG 1600 x 900 per preview/PDF, fondo Off-White, palette Navy/Bordeaux/Muted Gold/Green/Teal, card a raggio contenuto, testi brevi, frecce leggere e funzione didattica esplicita: mappa BANDO, confronto, sequenza operativa, schema anti-confusione e sintesi di rapporto amministrazione-contribuente.

## Asset creati

- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-06/01-mappa-bando-adempimenti-fiscali.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-06/02-redditi-iva-due-logiche.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-06/03-flusso-dichiarazione-versamento-controllo.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-06/04-credito-rimborso-compensazione.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-06/05-servizi-compliance-controllo.png

Ogni PNG ha il relativo master SVG e la cartella contiene README con funzione didattica.

## Inserimento

Il capitolo e' stato aggiornato con asset_refs, tag `illustrated` e cinque figure inserite subito dopo le sezioni che sintetizzano: mappa BANDO, IVA/redditi, versamenti, crediti/compensazioni e servizi fiscali.

## Verifiche

- `node scripts/run-mfc02-chapter06-preview-verification.cjs`: 15 pagine, 5 immagini caricate, PNG 1600 x 900, immagini dentro pagina, nessuna sovrapposizione footer, SVG text audit 0 issues.
- `rg` caratteri non ASCII: ok.
- `git diff --check`: ok.
- `npm.cmd test`: 25 test superati.
- `npm.cmd run typecheck`: ok.
- `npm.cmd run build`: ok.
