# conv-20260704001830-mfc02-cap08-editorial-images

created_at: 2026-07-04T00:18:30+02:00
scope: editorial-design
route: codex/editorial-images/mfc02-chapter08

## Sintesi

Integrate immagini editoriali nel capitolo 8 M-FC02, "Dogane e procedure doganali ADM", seguendo lo stile dei capitoli M-FC02 gia illustrati e del libro base.

## Analisi stile

Lo stile confermato usa master SVG modificabili, PNG 1600 x 900 per preview/PDF, fondo Off-White, palette Navy/Bordeaux/Muted Gold/Green/Teal, card leggere, testi brevi, frecce leggibili e funzione didattica esplicita: mappa BANDO, sequenza operativa, schema concettuale, controllo del rischio e checklist applicativa.

## Asset creati

- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-08/01-mappa-bando-dogane-adm.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-08/02-flusso-procedura-doganale.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-08/03-triade-classificazione-origine-valore.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-08/04-controlli-doganali-rischio-aeo.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-08/05-checklist-dichiarazione-doganale.png

Ogni PNG ha il relativo master SVG e la cartella contiene README con funzione didattica.

## Inserimento

Il capitolo e' stato aggiornato con asset_refs, tag `illustrated` e cinque figure inserite subito dopo le sezioni che sintetizzano: mappa BANDO, procedura doganale come sequenza, triade classificazione-origine-valore, controlli doganali e checklist dichiarazione doganale.

## Verifiche

- `node scripts/run-mfc02-chapter08-preview-verification.cjs`: 17 pagine, 5 immagini caricate, PNG 1600 x 900, immagini dentro pagina, nessuna sovrapposizione footer, SVG text audit 0 issues.
- `node --check` sui tre script del capitolo 8: ok.
- `rg` caratteri non ASCII: ok.
- `git diff --check` sul capitolo 8 e sugli asset: ok.
- `npm.cmd test`: 25 test superati.
- `npm.cmd run typecheck`: ok.
- `npm.cmd run build`: ok.
