# M-FC02 capitolo 1 - integrazione immagini editoriali

Data: 2026-07-02T18:53:00+02:00
Scope: editorial-design

Richiesta: analizzare lo stile delle immagini del libro base e creare immagini coerenti da inserire nel capitolo attuale del modulo M-FC02.

Esito:
- analizzato lo stile del libro base: diagrammi vettoriali 1600px, palette chiara, card con bordi sottili, colori funzionali BANDO, titoli sintetici, funzione didattica e decisionale;
- generate cinque figure SVG+PNG per il capitolo 1 di M-FC02;
- inserite le figure nel capitolo `books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md`;
- aggiornati `asset_refs` e tag `illustrated`;
- aggiornata la whitelist asset del Book Studio per supportare percorsi annidati `books/moduli/.../assets`;
- rimossa la duplicazione delle didascalie markdown, lasciando la didascalia del blocco immagine come nel libro base.

Asset:
- `books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/01-mappa-bando-agenzie-fiscali.png`
- `books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/02-perimetro-mfc02-dentro-fuori.png`
- `books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/03-tre-porte-ae-adm-ader.png`
- `books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/04-nucleo-comune-delta-fiscale.png`
- `books/moduli/m-fc02-agenzie-fiscali/assets/chapter-01/05-bando-decoder-fiscale.png`

Verifica:
- `npm.cmd test`: 23/23 passed;
- `npm.cmd run typecheck`: passed;
- `npm.cmd run build`: passed;
- `git diff --check`: passed;
- Playwright dashboard: 5 figure uniche, tutte caricate con `naturalWidth=1600`, `naturalHeight=1000`, `complete=true`, `figureInsidePage=true`;
- screenshot: `artifacts/mfc02-chapter01-images-dashboard-after-caption-fix.png`.
