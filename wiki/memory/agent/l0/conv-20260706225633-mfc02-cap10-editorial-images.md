---
id: conv-20260706225633-mfc02-cap10-editorial-images
createdAt: 2026-07-06T22:56:33+02:00
scope: editorial-design
route: codex/editorial-images/mfc02-chapter10
messageCount: 1
replyChars: 1035
---

# M-FC02 capitolo 10 immagini editoriali

## Richiesta
Analizzare stile e funzione delle immagini esistenti nel libro, creare immagini coerenti e inserirle nel capitolo attuale senza sovrapposizioni o problemi di layout.

## Contesto usato
- Skill `imagegen`, con decisione di non usare generazione raster AI perche' il repo usa diagrammi vettoriali SVG/PNG nativi.
- Skill `playwright` per verifica Book Studio.
- Capitolo 10 M-FC02 `Catasto, cartografia, estimo e pubblicita immobiliare`.
- Stile asset gia usato nei capitoli M-FC02 8 e 9: SVG master, PNG 1600 x 900, palette istituzionale, card leggere, testi brevi, mappa BANDO, sequenze e checklist.

## Esito
Creati e inseriti 5 asset SVG+PNG in `wiki/books/moduli/m-fc02-agenzie-fiscali/assets/chapter-10`: mappa BANDO Territorio/SPI, sistema Territorio AE, identificativo-classamento-rendita, servizi/procedure del Territorio e checklist Catasto/pubblicita immobiliare. Aggiornato il frontmatter del capitolo con `asset_refs` e tag `illustrated`; immagini inserite alle sezioni pertinenti.

## Verifiche
Book Studio: 16 pagine, 5 immagini caricate, nessun overlap, SVG audit 0 issue. Test: `node --check`, `rg` ASCII, placeholder, `git diff --check`, `npm test` 25/25, `npm run build` e `npm run typecheck` ok.
