---
id: review-vol-08-pipeline-19-impaginazione-kdp
type: review
title: "VOL-08 - Impaginazione KDP"
status: blocked
domain: "concorsi pubblici italiani"
topics: ["impaginazione KDP", "Book Studio", "nuclei didattici"]
entities: ["ConcorsoBook OS", "Metodo BANDO"]
source_refs: []
book_refs: ["vol-08-ict-digitale-cybersecurity-dati", "m-tr01-ict-trasformazione-digitale"]
confidence: 1
updated_at: 2026-08-05
created_at: 2026-08-05
review_required: true
canonical: false
tags: ["review", "pipeline", "vol-08", "kdp-layout", "blocked"]
issue_type: kdp_layout
severity: high
affected_pages: ["wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/"]
---

# VOL-08 - Impaginazione KDP

## Esito sintetico

Il master condiviso è applicato correttamente a VOL-08 per formato pagina, margini, tipografia, riflusso, numerazione e contenimento. Lo step 19 non può ancora essere chiuso perché i capitoli non espongono Nucleo ID e blocchi `▣ Verifica`, entrambi richiesti dal contratto corrente.

## Evidenza Book Studio

| Controllo | Esito |
| --- | --- |
| Formato | 6,69 × 9,61 in, pagina singola |
| Pagine | 139, numerazione progressiva 1-139 |
| Front matter | 6 layout |
| Aperture modulo | 1 |
| Capitoli | 13 |
| Tipografia | H1/H2/H3 Arial 20/14/12 pt; corpo Garamond 11 pt; tabelle e callout Arial 9,5 pt |
| Overflow | 0 su 139 pagine |
| Collisioni | 0 su 139 pagine |
| Asset strip / preview | nessuna sovrapposizione |
| Nuclei nel testo | 0 |
| Nuclei nell'indice analitico | 0 |
| Blocchi `▣ Verifica` | 0 |

Comando eseguito:

```text
BOOK_STUDIO_BOOK_IDS=volumi/vol-08 node scripts/verify-book-studio-layout.mjs
```

Esito: `Book Studio layout OK for vol-08`.

Artefatti tecnici:

- `artifacts/vol-08-step-19-layout-report.json`;
- `artifacts/vol-08-step-19-vol-08.png`.

## Requisiti soddisfatti

- master paperback KDP 6,69 × 9,61 in;
- colonna singola, margini speculari e gutter;
- Garamond/Arial alle dimensioni canoniche;
- testo giustificato e controllo vedove/orfani nel renderer;
- tabelle a larghezza controllata e righe non spezzate;
- immagini contenute nei margini;
- pagine numerate;
- zero overflow e collisioni.

## Blocker

1. **Indice analitico incompleto:** il renderer può derivare i numeri decimali soltanto da heading con Nucleo ID; i 13 capitoli correnti ne espongono zero.
2. **Verifiche non riconoscibili dal master:** non risultano heading `▣ Verifica`, quindi il renderer non può applicare il trattamento grafico dedicato né verificarne le spezzature.

## Correzione necessaria

Il retrofit non è una modifica di solo layout: richiede di convertire i 13 capitoli al formato 2, assegnare Nucleo ID stabili, riallineare la matrice, inserire o riconciliare i blocchi `▣ Verifica` e rieseguire i gate editoriali impattati prima del nuovo text freeze.

In alternativa serve una deroga editoriale esplicita e tracciata al contratto dello step 19 per mantenere VOL-08 come volume legacy. In assenza di una delle due decisioni lo step resta aperto.

## Modifiche al testo

Nessun capitolo, immagine o contenuto editoriale è stato eliminato o modificato per forzare il layout.
