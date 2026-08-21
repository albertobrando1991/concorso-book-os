---
id: review-pipeline-vol-04-step-22
type: editorial_review
volume: VOL-04
step: 22
status: passed
review_required: false
updated_at: 2026-08-18
---

# VOL-04 — Step 22: preflight finale

## Esito

**PASS.** Il manoscritto revisionato e il PDF candidato superano il preflight editoriale e tecnico locale. Non risultano criticità bloccanti nella copertura, nei collegamenti interni, nei metadati, nella composizione delle pagine o nell'esportazione. KDP Previewer non è installato nell'ambiente e il controllo proprietario non viene quindi dichiarato come eseguito.

## Checklist pass/fail

| Controllo | Esito | Evidenza / verifica |
| --- | --- | --- |
| Copertura didattica | PASS | Audit diretto della matrice: 14 righe, 14 capitoli completi, zero blocker e zero warning. |
| Link wiki | PASS | Audit su 30 file del perimetro: 113 collegamenti verificati, zero destinazioni mancanti. |
| `source_refs` | PASS | Audit dei 26 file reader-facing: nessun riferimento a fonte mancante. |
| Frontmatter | PASS | Audit dei 26 file reader-facing: nessun delimitatore o metadato obbligatorio anomalo. |
| Asset path e file mancanti | PASS | Nessun riferimento immagine nel manoscritto; preflight Book Studio con `missingImages: 0`. |
| Immagini duplicate | N/D | Nessuna immagine reader-facing nel volume. |
| Tabelle anomale | PASS | 240 tabelle Markdown nei 26 file reader-facing; audit di tutte le 303 pagine con zero overflow, zero sovrapposizioni e zero collisioni con gli asset di anteprima. |
| Caratteri corrotti | PASS | Controllo dei pattern di mojibake sul perimetro editoriale: nessuna occorrenza. |
| Refusi strutturali | PASS | Secondo controllo dedicato a doppie parole, titoli, numerazioni, riferimenti, accenti e marcatori interni: nessun blocker residuo. |
| Diff Git | PASS sul perimetro | `git diff --check` sui file VOL-04: nessun errore di whitespace. Il controllo globale segnala spazi finali in un file VOL-11 estraneo a questo intervento, già modificato nel worktree condiviso. |
| Test pertinenti | PASS | Vitest: 7 file e 55 test superati su anteprima, export PDF, audit pagina, tipografia, layout, confini e indice. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0. |
| Build produzione | PASS | `npm run build`: Next.js 15.5.22 compilato e 20 pagine statiche generate. |
| Export PDF | PASS | Generato `output/pdf/vol-04-giustizia-upp-interior-kdp.pdf`: 1.694.085 byte; SHA-256 `60889c610d3014a09cb6e83e5e577b21194e872e879c88a5de36460960110cdd`. |
| Font | PASS | Analisi strutturale del PDF: Arial Bold, Garamond, Arial Black e Arial presenti; documento non cifrato. |
| Dimensione pagina | PASS | MediaBox 481,92 × 691,92 punti, corrispondente al formato KDP 6,69 × 9,61 pollici. |
| Bleed | PASS | Interno senza elementi al vivo; nessuna fuoriuscita rilevata nell'audit DOM dell'intero volume. |
| Margini | PASS | Layout Book Studio impostato a 23 mm interno, 13 mm esterno e 18 mm verticale; zero overflow sulle 303 pagine. |
| Conteggio pagine | PASS | 303 pagine; nessuna pagina bianca o a densità testuale anomala nel controllo strutturale. |
| Ispezione visiva | PASS | Verificate la prima pagina, la conclusione (pagina 299) e l'ultima pagina bibliografica (pagina 303). |
| Warning KDP Previewer | N/D | Applicazione proprietaria non disponibile nell'ambiente. I controlli locali equivalenti non hanno rilevato difetti. |
| EPUB | N/D | Pandoc e un esportatore EPUB non sono disponibili; il deliverable verificato è l'interno cartaceo PDF. |

## Comandi principali

```text
npx tsx scripts/.tmp-audit-vol04-matrix.ts
npx vitest run <sette suite Book Studio pertinenti>
npm run typecheck
npm run build
npm run pipeline -- status VOL-04 --json
git diff --check -- <perimetro VOL-04>
```

## Decisione

Il Volume 4 è idoneo al passaggio successivo della pipeline. Il giudizio editoriale complessivo resta **B — pronto dopo revisione leggera**, nella formulazione richiesta dal gate: **Pubblicabile con correzioni minori.** Le attività residue sono esterne al manoscritto: attribuzione dell'ISBN, verifica proprietaria in KDP Previewer ed eventuale produzione EPUB se si decide di pubblicare anche in formato ebook.
