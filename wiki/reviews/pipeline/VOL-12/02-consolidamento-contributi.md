---
id: pipeline-vol-12-02-consolidamento-contributi
type: pipeline_review
title: "VOL-12 — Step 02: consolidamento dei contributi"
volume_code: VOL-12
step: "02"
phase: A
scope: catalog
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-02", "consolidamento"]
---

# VOL-12 — Step 02: consolidamento dei contributi

## Esito complessivo

**Nessun contributo editoriale di staff da integrare.** Il censimento dello step 01 ha accertato che i quattro moduli M-SP non hanno capitoli né in `main`, né nel worktree, né in branch o stash alternativi. Non esistono versioni concorrenti, duplicati o conflitti da risolvere per questo volume.

Lo step si chiude quindi senza integrazioni di contenuto d'autore. Le modifiche registrate sotto non sono consolidamenti di contributi altrui: sono correzioni di impianto applicate allo scaffold in esito alla revisione editoriale pre-pipeline, riportate qui per tracciabilità.

## File modificati

| File | Origine del contributo | Integrazione applicata | Contenuto preservato | Conflitti rimasti |
| --- | --- | --- | --- | --- |
| `m-sp01-forze-ordine/index.md` | revisione editoriale 2026-08-11 | perimetro riallineato a «forze di polizia»; aggiunta sezione «Fuori perimetro»; accenti corretti | ruolo, confine editoriale, fonti, prossimo passo | nessuno |
| `m-sp01-forze-ordine/planning/00-piano-editoriale.md` | revisione editoriale 2026-08-11 | struttura differenziata a 11 sezioni con marcatura `[nucleo]`; aggiunta sezione «Ritmo e taglio» | obiettivo, lettore, collegamenti obbligatori, fonti | nessuno |
| `m-sp02-vigili-fuoco/index.md` | revisione editoriale 2026-08-11 | perimetro esplicitato su Corpo nazionale; aggiunta «Fuori perimetro»; accenti corretti | impianto originale | nessuno |
| `m-sp02-vigili-fuoco/planning/00-piano-editoriale.md` | revisione editoriale 2026-08-11 | struttura a 13 sezioni con doppio binario operativo/direttivo | impianto originale | nessuno |
| `m-sp03-.../index.md` | revisione editoriale 2026-08-11 | architettura a tre binari; avvertenza sul notariato; «Fuori perimetro»; accenti | impianto originale | nessuno |
| `m-sp03-.../planning/00-piano-editoriale.md` | revisione editoriale 2026-08-11 | struttura a 15 sezioni su tre binari; piano pluriennale al posto del 30/60/90 | impianto originale | nessuno |
| `m-sp04-.../index.md` | revisione editoriale 2026-08-11 | architettura a due binari; «Fuori perimetro»; accenti | impianto originale | nessuno |
| `m-sp04-.../planning/00-piano-editoriale.md` | revisione editoriale 2026-08-11 | struttura a 13 sezioni su due binari; piano a 6-12 mesi | impianto originale | nessuno |
| `architettura-moduli-specialistici.md` | revisione editoriale 2026-08-11 | 1 riga: titolo M-SP01 allineato al nuovo perimetro | tutto il resto del documento | nessuno |
| `src/catalog/text-volumes.ts` | revisione editoriale 2026-08-11 | 2 stringhe: `audience` VOL-12 e `description` del pacchetto premium | **vedi collisione sotto** | nessuno |

**File creati:**

- `wiki/books/volumi/vol-12-carriere-speciali-premium/index.md`
- `wiki/books/volumi/vol-12-carriere-speciali-premium/planning/00-scheda-pipeline.md`
- `wiki/reviews/pipeline/VOL-12/00-presa-in-carico.md`
- `wiki/reviews/pipeline/VOL-12/01-censimento-lavoro-staff.md`
- `pipeline/VOL-12/run-state.json` (generato dal CLI)

Nessun file è stato cancellato. Nessun capitolo, sezione, tabella o immagine è stato duplicato. Nessun piano interno è stato collocato in un capitolo destinato al lettore: tutti i piani restano in `planning/` e tutti i verbali in `wiki/reviews/pipeline/VOL-12/`.

## Collisione rilevata e gestita

`src/catalog/text-volumes.ts` conteneva **lavoro preesistente non committato di un altro flusso**, riconoscibile nel diff:

- introduzione del campo opzionale `orientationBookId` con relativo commento JSDoc;
- assegnazione di `orientationBookId: "vol-02-enti-locali-polizia-locale"` alla voce VOL-02;
- correzione sistematica di accenti su più voci di catalogo (`piu` → `più`, `autorita` → `autorità`, `universita` → `università`, `interoperabilita` → `interoperabilità`).

Questo lavoro è stato **integralmente preservato**. Le due modifiche VOL-12 sono state applicate come patch chirurgiche su righe distinte e non toccano né il campo `orientationBookId` né le correzioni di accento altrui. Il diff complessivo del file (25 righe) è quindi in larga parte contributo preesistente: **le righe attribuibili a VOL-12 sono due.**

## Riepilogo `git diff --stat` sul perimetro VOL-12

```
 src/catalog/text-volumes.ts                        | 25 +++++++-----   (di cui 2 righe VOL-12)
 wiki/books/moduli/architettura-moduli-specialistici.md |  2 +-
 wiki/books/moduli/m-sp01-forze-ordine/index.md     | 13 +++---
 m-sp01-forze-ordine/planning/00-piano-editoriale.md | 42 +++++++++++--------
 wiki/books/moduli/m-sp02-vigili-fuoco/index.md     |  9 +++--
 m-sp02-vigili-fuoco/planning/00-piano-editoriale.md | 40 +++++++++++-------
 m-sp03-.../index.md                                | 18 ++++++---
 m-sp03-.../planning/00-piano-editoriale.md         | 47 +++++++++++++++-------
 m-sp04-.../index.md                                | 16 +++++---
 m-sp04-.../planning/00-piano-editoriale.md         | 43 +++++++++++-------
 10 files changed, 165 insertions(+), 90 deletions(-)
```

## Esito di `git diff --check`

Il comando esce con codice 2 e segnala **trailing whitespace su file estranei a VOL-12**: capitoli di M-FL02 (10 file), M-FL04 (2 file) e un avviso CRLF su `vol-02-enti-locali-polizia-locale/front-matter/06-indice.md`.

Le occorrenze si concentrano nelle righe di risposta dei quiz e derivano dall'uso del doppio spazio di fine riga come interruzione Markdown. **Nessuna segnalazione riguarda file del perimetro VOL-12.**

Trattandosi di lavoro di un altro flusso, non è stato corretto in questo step: correggerlo significherebbe modificare 12 capitoli non committati appartenenti a una revisione in corso. **Rilievo trasmesso allo staff VOL-02, non azionato qui.**

## Nessun commit eseguito

Come prescritto, non sono stati eseguiti `commit` né `push`.
