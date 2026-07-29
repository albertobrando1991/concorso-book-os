# conv-20260704004506-mfc02-cap09-editorial-images

created_at: 2026-07-04T00:45:06+02:00
scope: editorial-design
route: codex/editorial-images/mfc02-chapter09

## Sintesi

Integrate immagini editoriali nel capitolo 9 M-FC02, "Accise, giochi e monopoli", seguendo lo stile dei capitoli M-FC02 gia illustrati e del libro base.

## Analisi stile

Lo stile confermato usa master SVG modificabili, PNG 1600 x 900 per preview/PDF, fondo Off-White, palette Navy/Bordeaux/Muted Gold/Green/Teal, card leggere, testi brevi, frecce leggibili e funzione didattica esplicita: mappa BANDO, sequenza operativa, schema aree, schema di controllo e checklist applicativa.

## Asset creati

- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-09/01-mappa-bando-accise-giochi-monopoli.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-09/02-filiera-accise-regime-sospensivo.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-09/03-prodotti-giochi-monopoli-adm.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-09/04-controlli-adm-filiere-regolate.png
- wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-09/05-checklist-accise-giochi-monopoli.png

Ogni PNG ha il relativo master SVG e la cartella contiene README con funzione didattica.

## Inserimento

Il capitolo e' stato aggiornato con asset_refs, tag `illustrated` e cinque figure inserite subito dopo le sezioni che sintetizzano: mappa BANDO, accise come logica di filiera, prodotti e filiere da riconoscere, controlli ADM nelle filiere regolate e checklist operativa finale.

## Verifiche

- `node scripts/run-mfc02-chapter09-preview-verification.cjs`: 15 pagine, 5 immagini caricate, PNG 1600 x 900, immagini dentro pagina, nessuna sovrapposizione footer, SVG text audit 0 issues.
- `node --check` sui tre script del capitolo 9: ok.
- `rg` caratteri non ASCII: ok.
- `git diff --check` sul capitolo 9 e sugli asset: ok.
- `npm.cmd test`: 25 test superati.
- `npm.cmd run typecheck`: ok.
- `npm.cmd run build`: ok.
