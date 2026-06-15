---
id: conv-20260609143014-ch23-diario-errori-images
created_at: 2026-06-09T14:30:14.3644559+02:00
scope: il-metodo-bando
route: codex/chapter23-editorial-images
chapter: 23
figures: 7
assets: books/il-metodo-bando/assets/chapter-23
verification: chapter23-images,book-preview-test,git-diff-check
preview: http://localhost:3023
canonical: false
---

# Capitolo 23 - Immagini editoriali

## Richiesta utente

procedi con prossimo capitolo

## Esito

Completato il flusso immagini del Capitolo 23, `Il diario degli errori`.

Sono state generate e inserite 7 figure professionali SVG+PNG:

- mappa BANDO del diario degli errori;
- sei categorie di errore;
- protocollo in sei passaggi;
- scheda professionale del diario;
- uso del diario nelle diverse prove;
- ciclo errore, flashcard, ripasso e materia che peggiora;
- caso Marta e lettura dei pattern.

Asset principali:

- `books/il-metodo-bando/assets/chapter-23`
- `scripts/generate-chapter23-assets.cjs`
- `scripts/verify-chapter23-images.cjs`

## Verifiche

- `node scripts/verify-chapter23-images.cjs` su Book Studio locale: 14 pagine, 7 immagini `chapter-23`, tutte 1600x900, nessun problema layout, nessun testo SVG fuori margine, nessuna sovrapposizione al footer.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: nessun errore; restano solo avvisi CRLF su file preesistenti non toccati nel flusso.

## Decisione operativa

Per il prossimo capitolo proseguire con il flusso immagini professionale: analisi del capitolo, generatore dedicato, inserimento chirurgico in markdown, verifica Playwright su preview e memoria locale.
