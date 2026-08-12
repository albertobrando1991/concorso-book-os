---
id: review-vol-10-pipeline-19-impaginazione-kdp
type: review
title: "VOL-10 - Impaginazione KDP"
status: approved
domain: "concorsi pubblici italiani"
topics: ["impaginazione KDP", "Book Studio", "indice analitico", "nuclei didattici"]
entities: ["ConcorsoBook OS", "Metodo BANDO"]
source_refs: []
book_refs: ["vol-10-tecnico-ingegneristico-territorio-lavori-pubblici", "m-tr03-tecnico-ingegneristico"]
confidence: 1
updated_at: 2026-08-12
created_at: 2026-08-12
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-10", "kdp-layout", "approved"]
issue_type: kdp_layout
severity: none
affected_pages: []
---

# VOL-10 - Impaginazione KDP

## Esito sintetico

VOL-10 è interamente renderizzato nel Book Studio con il master paperback KDP canonico. Tutti i 13 capitoli e i 78 nuclei compaiono nel testo e nell'indice analitico; la numerazione delle 195 pagine è progressiva e non risultano overflow o sovrapposizioni strutturali.

## Evidenza Book Studio

| Controllo | Esito |
| --- | --- |
| Formato | 6,69 x 9,61 in, bianco e nero, senza bleed, pagina singola |
| Pagine | 195, numerazione progressiva 1-195 |
| Front matter | 6 layout |
| Aperture modulo | 1 |
| Capitoli | 13 |
| Nuclei nel testo | 78 |
| Nuclei nell'indice analitico | 78 |
| Blocchi `▣ Verifica` | 33 |
| Tipografia | H1/H2/H3 Arial 20/14/12 pt; corpo Garamond 11 pt; tabelle e callout Arial 9,5 pt |
| Overflow | 0 su 195 pagine |
| Collisioni | 0 su 195 pagine |
| Asset strip / preview | nessuna sovrapposizione |

Comando eseguito:

```powershell
$env:BOOK_STUDIO_BOOK_IDS='volumi/vol-10'
$env:BOOK_STUDIO_ARTIFACT_PREFIX='vol-10-step19'
$env:BOOK_STUDIO_EXPECTED_COUNTS='{"frontMatter":6,"moduleOpenings":1,"chapters":13,"nuclei":78}'
node scripts/verify-book-studio-layout.mjs
```

Esito: `Book Studio layout OK for vol-10`.

Artefatti tecnici:

- `artifacts/vol-10-step19-layout-report.json`;
- `artifacts/vol-10-step19-vol-10.png`.

## Anomalie corrette

1. Il riconoscimento dei placeholder considerava vuoto un capitolo completo quando la prosa conteneva incidentalmente le parole "da sviluppare". Il marcatore ora vale solo a inizio contenuto; il capitolo 7 viene renderizzato con tutti i suoi sei nuclei.
2. Il filtro delle sezioni accessorie escludeva dall'indice due nuclei canonici il cui titolo iniziava con "Caso guidato". La presenza del `Nucleo ID` ora prevale sul filtro editoriale; `N-TR03-10-06` e `N-TR03-11-06` compaiono correttamente nell'indice.
3. Entrambe le correzioni sono protette da test di regressione in `tests/book-preview.test.ts`.

## Requisiti soddisfatti

- master KDP a colonna singola con margini speculari e gutter;
- Garamond/Arial alle dimensioni canoniche e testo giustificato;
- indice completo di capitoli e numeri decimali derivati dai Nucleo ID;
- tabelle, box e verifiche contenuti nei margini;
- nessun testo, tabella, quiz o immagine eliminato per ottenere il riflusso;
- zero overflow, collisioni con il footer o pagine mancanti.

## Handoff allo step 20

Lo step 20 riceve un impaginato completo di 195 pagine e gli artefatti diagnostici. L'audit visivo pagina per pagina resta di sua competenza e dovrà controllare in dettaglio spazi bianchi, vedove, orfani, spezzature, tabelle, box e coerenza recto/verso.
