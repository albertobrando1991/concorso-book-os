---
id: conv-20260609105201-ch20-mappe-profilo-images
created_at: 2026-06-09T10:52:01.4580719+02:00
scope: il-metodo-bando
route: codex/chapter20-editorial-images
chapter: 20
figures: 7
assets: books/il-metodo-bando/assets/chapter-20
verification: chapter20-images,book-preview-test,git-diff-check
preview: http://127.0.0.1:3020
canonical: false
---

# Capitolo 20 - Immagini editoriali

## Richiesta utente

procedi ocn il prossimo capitolo

## Esito

Completato il flusso immagini del Capitolo 20, `Mappe profilo: cosa resta comune e cosa cambia`.

Sono state generate e inserite 7 figure professionali SVG+PNG:

- mappa BANDO delle mappe profilo;
- formula core + modulo profilo + prova reale;
- scheda unica di mappa profilo;
- profili amministrativi e centrali;
- profili specialistici e servizi;
- semaforo e pesatura del tempo;
- caso guidato di conversione da preparazione amministrativa a profilo tecnico.

Asset principali:

- `books/il-metodo-bando/assets/chapter-20`
- `scripts/generate-chapter20-assets.cjs`
- `scripts/verify-chapter20-images.cjs`

## Verifiche

- `node scripts/verify-chapter20-images.cjs` su Book Studio locale: 21 pagine, 7 immagini `chapter-20`, tutte 1600x900, nessun problema layout, nessun testo SVG fuori margine, nessuna sovrapposizione al footer.
- `npm test -- tests\book-preview.test.ts`: 3 test passati.
- `git diff --check`: nessun errore; restano solo avvisi CRLF su file preesistenti non toccati nel flusso.

## Decisione operativa

Per i prossimi capitoli della Parte IV continuare con figure didattiche a funzione esplicita, non decorative: mappe, formule, schede, griglie, sequenze e casi guidati. Mantenere il controllo Playwright su safe-box SVG e preview A4.
