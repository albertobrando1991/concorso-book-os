---
id: review-pipeline-vol-08-step-22
type: editorial_review
volume: VOL-08
step: 22
status: passed
review_required: false
updated_at: 2026-08-12
---

# VOL-08 — Step 22: preflight finale

## Esito

**PASS.** Il pacchetto editoriale e il PDF candidato superano il preflight locale. Non risultano blocker tecnici o editoriali. KDP Previewer non è installato nell'ambiente: il suo controllo proprietario resta distinto dai controlli equivalenti locali e non viene dichiarato come eseguito.

## Checklist pass/fail

| Controllo | Esito | Evidenza / verifica |
| --- | --- | --- |
| Copertura didattica | PASS | `node scripts/audit-vol08-format2-nuclei.mjs`: 13 capitoli, 82 nuclei nel testo, 82 nella matrice e 82 nell'indice; nessun duplicato, mancante o failure. |
| Link wiki | PASS | Indice analitico risolto dal medesimo audit: 82 destinazioni su 82, con capitolo, heading e anchor esistenti. |
| `source_refs` | PASS | Verifica del frontmatter dei 13 capitoli: chiave presente e valorizzata in tutti i file. |
| Frontmatter | PASS | 13/13 capitoli con delimitatori YAML e metadati editoriali; audit e build li elaborano senza errori. |
| Asset path e file mancanti | PASS | Export Book Studio completato con `missingImages: 0`; lo step 18 ha inoltre attestato zero asset reader-visible richiesti. |
| Immagini duplicate | PASS | Nessuna immagine reader-visible nel volume; insieme vuoto, nessun duplicato. |
| Tabelle anomale | PASS | Audit pagina-per-pagina dello step 20: 231/231 pagine, zero blocker di tabella, overflow o collisione. |
| Caratteri corrotti | PASS | `rg -n 'Ã|Â|�'` sulle directory canoniche del volume e del modulo: nessuna corrispondenza. |
| Diff Git | PASS | `git diff --check`: nessun errore di whitespace. |
| Test pertinenti | PASS | Vitest: 7 file, 95 test superati, inclusi nuclei Format 2, paginazione, indice, layout, anteprima ed export PDF. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0. |
| Build produzione | PASS | `npm run build`: Next.js 15.5.18 compilato, type/lint validi e 20/20 pagine statiche generate. |
| Export PDF | PASS | `npm run export:volume-pdf` con `BOOK_STUDIO_BOOK_ID=volumi/vol-08`: file generato in `delivery/VOL-08/candidate/vol-08-interior-kdp.pdf`, 1.567.744 byte. |
| Font | PASS | L'export attende `document.fonts.ready`, verifica `document.fonts.status === "loaded"` e interrompe l'operazione se i font non sono pronti; contratto e test export verdi. |
| Dimensione pagina | PASS | Contratto PDF: `6.69in × 9.61in`, sia in `@page` sia nelle opzioni Chromium. |
| Bleed | PASS | Interno senza elementi al vivo; `@page` e PDF hanno margine esterno zero, mentre il contenuto rispetta l'area sicura verificata nello step 20. |
| Margini | PASS | Layout Book Studio verificato a 23 mm interno, 13 mm esterno e 18 mm verticale, senza overflow o collisioni sulle 231 pagine. |
| Conteggio pagine | PASS | Export bloccante su conteggio atteso: 231 pagine rilevate e 231 attese. |
| Warning KDP Previewer | N/D | Applicazione proprietaria non disponibile nell'ambiente. Nessun warning nei controlli locali equivalenti di formato, paginazione, font pronti, immagini mancanti, margini, overflow e build. |

## Comandi principali

```text
node scripts/audit-vol08-format2-nuclei.mjs
npx vitest run tests/audit-vol08-format2-nuclei.test.ts tests/book-studio-page-boundaries.test.ts tests/book-studio-page-audit-core.test.ts tests/book-studio-index-pages.test.ts tests/book-studio-layout-options.test.ts tests/book-studio-pdf-export-core.test.ts tests/book-preview.test.ts
npm run typecheck
npm run build
npm run export:volume-pdf
git diff --check
```

## Decisione

Il pacchetto è idoneo al passaggio successivo della pipeline. Il mancato avvio di KDP Previewer è registrato esplicitamente e non viene trasformato in una falsa attestazione; i controlli locali riproducibili non hanno rilevato difetti bloccanti.
