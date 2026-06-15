---
id: conv-20260609162753-ch24-checklist-operative-images
created_at: 2026-06-09T16:27:53.3228734+02:00
scope: il-metodo-bando
route: codex/chapter24-editorial-images
chapter: 24
figures: 7
assets: books/il-metodo-bando/assets/chapter-24
verification: chapter24-images,book-preview-test,git-diff-check
preview: http://localhost:3024
canonical: false
---

# Capitolo 24 - Immagini editoriali

## Richiesta utente

prossimo capitolo

## Esito

Completato il flusso immagini del Capitolo 24, `Checklist operative`.

Sono state generate e inserite 7 figure professionali SVG+PNG:

- mappa BANDO delle checklist;
- tre regole per usare le checklist;
- percorso domanda e comunicazioni;
- preparazione delle prove;
- ultimi 7 giorni e ultime 24 ore;
- logistica, ansia e tenuta;
- checklist unica BANDO applicata al caso Giulia.

Asset principali:

- `books/il-metodo-bando/assets/chapter-24`
- `scripts/generate-chapter24-assets.cjs`
- `scripts/verify-chapter24-images.cjs`

## Verifiche

- `node scripts/verify-chapter24-images.cjs` su Book Studio locale: 19 pagine, 7 immagini `chapter-24`, tutte 1600x900, nessun problema layout, nessun testo SVG fuori margine, nessuna sovrapposizione al footer.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: nessun errore; restano solo avvisi CRLF su file preesistenti non toccati nel flusso.

## Decisione operativa

Per il prossimo capitolo proseguire con il flusso immagini professionale o passare al primo capitolo extra non illustrato, rispettando l'ordine effettivo del libro e la memoria locale.
