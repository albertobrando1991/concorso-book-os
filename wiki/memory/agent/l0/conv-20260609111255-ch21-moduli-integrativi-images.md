---
id: conv-20260609111255-ch21-moduli-integrativi-images
created_at: 2026-06-09T11:12:55.6026857+02:00
scope: il-metodo-bando
route: codex/chapter21-editorial-images
chapter: 21
figures: 7
assets: books/il-metodo-bando/assets/chapter-21
verification: chapter21-images,book-preview-test,git-diff-check
preview: http://127.0.0.1:3021
canonical: false
---

# Capitolo 21 - Immagini editoriali

## Richiesta utente

prossimo capitolo procedi

## Esito

Completato il flusso immagini del Capitolo 21, `Come scegliere i moduli integrativi`.

Sono state generate e inserite 7 figure professionali SVG+PNG:

- mappa BANDO dei moduli integrativi;
- distinzione tra core, modulo e approfondimento;
- quattro requisiti del modulo;
- cinque filtri di scelta;
- matrice di decisione dei moduli;
- atlante operativo dei moduli integrativi;
- scheda modulo e caso Sara.

Asset principali:

- `books/il-metodo-bando/assets/chapter-21`
- `scripts/generate-chapter21-assets.cjs`
- `scripts/verify-chapter21-images.cjs`

## Verifiche

- `node scripts/verify-chapter21-images.cjs` su Book Studio locale: 21 pagine, 7 immagini `chapter-21`, tutte 1600x900, nessun problema layout, nessun testo SVG fuori margine, nessuna sovrapposizione al footer.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: nessun errore; restano solo avvisi CRLF su file preesistenti non toccati nel flusso.

## Decisione operativa

Per il prossimo capitolo proseguire con il flusso immagini professionale: generatore dedicato, inserimento chirurgico in markdown, verifica Playwright su preview e memoria locale.
