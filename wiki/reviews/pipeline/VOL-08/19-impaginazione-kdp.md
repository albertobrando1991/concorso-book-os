---
id: review-vol-08-pipeline-19-impaginazione-kdp
type: review
title: "VOL-08 - Impaginazione KDP"
status: complete
domain: "concorsi pubblici italiani"
topics: ["impaginazione KDP", "Book Studio", "nuclei didattici"]
entities: ["ConcorsoBook OS", "Metodo BANDO"]
source_refs: []
book_refs: ["vol-08-ict-digitale-cybersecurity-dati", "m-tr01-ict-trasformazione-digitale"]
confidence: 1
updated_at: 2026-08-12
created_at: 2026-08-05
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-08", "kdp-layout", "complete"]
issue_type: kdp_layout
severity: none
affected_pages: ["wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters/"]
---

# VOL-08 - Impaginazione KDP

## Esito sintetico

Il master editoriale canonico è applicato correttamente al Volume 08. Il retrofit Format 2 ha risolto i precedenti blocker: i Nucleo ID sono presenti e riconciliati con l'indice analitico, mentre gli apparati `▣ Verifica` ricevono il trattamento grafico dedicato. Non sono stati eliminati testo o immagini e non è stato generato anticipatamente il PDF.

## Evidenza Book Studio

| Controllo | Esito |
| --- | --- |
| Formato | 6,69 × 9,61 in, pagina singola, bianco e nero, senza bleed |
| Pagine | 231, numerazione progressiva 1-231 |
| Front matter | 6 sezioni |
| Aperture modulo | 1 |
| Capitoli | 13 |
| Nuclei nel testo | 82 |
| Nuclei nell'indice analitico | 82 |
| Blocchi `▣ Verifica` | 13 |
| Tipografia | H1/H2/H3 Arial 20/14/12 pt; corpo Garamond 11 pt; tabelle e callout Arial 9,5 pt |
| Interlinea corpo | 1,18 |
| Colonne | 1 |
| Margini | speculari, con gutter proporzionato al master paperback |
| Overflow | 0 su 231 pagine |
| Collisioni | 0 su 231 pagine |
| Asset strip / preview | nessuna sovrapposizione |

Comando di verifica:

```text
BOOK_STUDIO_URL=http://127.0.0.1:3027
BOOK_STUDIO_BOOK_IDS=volumi/vol-08
BOOK_STUDIO_ARTIFACT_PREFIX=vol-08-step-19
BOOK_STUDIO_EXPECTED_COUNTS={"frontMatter":6,"moduleOpenings":1,"chapters":13,"nuclei":82}
node scripts/verify-book-studio-layout.mjs
```

Esito: `Book Studio layout OK for vol-08`.

## Requisiti soddisfatti

- master paperback KDP 6,69 × 9,61 in, colonna singola e senza bleed;
- Garamond e Arial alle dimensioni canoniche, testo giustificato e interlinea 1,18;
- pagine singole numerate progressivamente;
- front matter canonico e apertura del modulo;
- indice analitico con 82 nuclei derivati dai Nucleo ID;
- 13 apparati `▣ Verifica` riconoscibili dal renderer;
- zero overflow e collisioni strutturali;
- nessun contenuto eliminato o asset ridotto per forzare il layout.

## Blocker

Nessuno. I due blocker del report del 5 agosto 2026 — assenza dei Nucleo ID e degli apparati `▣ Verifica` — sono risolti dal retrofit Format 2.

## Evidenze tecniche

- `artifacts/vol-08-step-19-layout-report.json`;
- `artifacts/vol-08-step-19-vol-08.png`.

## Confine con lo step 20

Questo step certifica struttura, conteggi, master tipografico, numerazione e contenimento del rendering completo. Lo step 20 eseguirà l'audit qualitativo di ogni pagina, comprese vedove, orfani, spazi bianchi, spezzature di tabelle e apparati di verifica. Il suo esito non è anticipato qui.
