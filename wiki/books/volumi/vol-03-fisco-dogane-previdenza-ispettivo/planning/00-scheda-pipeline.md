---
type: pipeline_spec
volume_code: VOL-03
volume_title: Funzioni centrali, Fisco, Previdenza e Ispettivo
cut_off_date: 2026-07-27
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [C, D, F]
status: draft
updated_at: 2026-07-27
review_required: true
---

# Scheda di pipeline — VOL-03

Input della pipeline editoriale per il volume VOL-03. Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`.

Da confermare prima di aprire la fase C: `cut_off_date` e i responsabili umani sono valori operativi, non dedotti dal repository. Il gate 15 li usa per il nulla osta specialistico.

## Moduli

Ordine di lavorazione secondo la sequenza raccomandata dal protocollo: M-FC02 per primo, poi M-FC01, infine M-FC03.

| Codice | Module id | Priorità | Fasi |
| --- | --- | --- | --- |
| M-FC02 | moduli/m-fc02-agenzie-fiscali | 1 | C,D |
| M-FC01 | moduli/m-fc01-ministeri | 2 | C,D |
| M-FC03 | moduli/m-fc03-enti-non-economici | 3 | C,D |

I capitoli di M-FC01 e M-FC02 restano derivati dalle rispettive directory. M-FC03 è dichiarato esplicitamente per attribuire una numerazione stabile anche alle sei appendici e consentire la tracciabilità dei Nucleo ID Formato 2.

## Capitoli M-FC03

| # | Titolo | File | Matrice | Stato atteso | Note |
|---|---|---|---|---|---|
| 01 | Lavorare negli enti pubblici non economici | chapters/01-lavorare-enti-pubblici-non-economici.md | planning/02-matrice-copertura-didattica.md | final | Perimetro e metodo |
| 02 | Ordinamento e governance EPNE | chapters/02-ordinamento-governance-epne.md | planning/02-matrice-copertura-didattica.md | final | Ordinamento |
| 03 | INPS: previdenza, servizi e prestazioni | chapters/03-inps-previdenza-servizi-prestazioni.md | planning/02-matrice-copertura-didattica.md | final | INPS |
| 04 | INAIL: assicurazione, prevenzione e prestazioni | chapters/04-inail-assicurazione-prevenzione-prestazioni.md | planning/02-matrice-copertura-didattica.md | final | INAIL |
| 05 | Procedimenti EPNE | chapters/05-procedimenti-epne-cittadini-imprese.md | planning/02-matrice-copertura-didattica.md | final | Procedimento e servizi |
| 06 | Bilancio, patrimonio e controlli | chapters/06-bilancio-patrimonio-controlli-epne.md | planning/02-matrice-copertura-didattica.md | final | Contabilità EPNE |
| 07 | Performance, PIAO e valore pubblico | chapters/07-performance-piao-valore-pubblico-epne.md | planning/02-matrice-copertura-didattica.md | final | Programmazione |
| 08 | Personale EPNE e CCNL | chapters/08-personale-epne-ccnl-funzioni-centrali.md | planning/02-matrice-copertura-didattica.md | final | Pubblico impiego |
| 09 | Contratti e acquisti | chapters/09-contratti-acquisti-forniture-epne.md | planning/02-matrice-copertura-didattica.md | final | Procurement |
| 10 | Bando Decoder EPNE | chapters/10-bando-decoder-epne.md | planning/02-matrice-copertura-didattica.md | final | Bandi e piano |
| 11 | Casi pratici EPNE | chapters/11-casi-pratici-epne.md | planning/02-matrice-copertura-didattica.md | final | Applicazione |
| 12 | Quesiti situazionali EPNE | chapters/12-quesiti-situazionali-epne.md | planning/02-matrice-copertura-didattica.md | final | Situazionali |
| 13 | Piano 30/60/90 | chapters/13-piano-30-60-90-inps-inail-epne.md | planning/02-matrice-copertura-didattica.md | final | Piano e simulazione |
| 14 | Vigilanza ispettiva INPS/INAIL | chapters/appendice-a-vigilanza-ispettiva-inps-inail.md | planning/02-matrice-copertura-didattica.md | final | Appendice A |
| 15 | Glossario previdenza e assicurazione | chapters/appendice-b-glossario-previdenza-assicurazione-prestazioni.md | planning/02-matrice-copertura-didattica.md | final | Appendice B |
| 16 | Schede rapide altri enti | chapters/appendice-c-schede-rapide-aci-enac-istat-enea-asi-cri.md | planning/02-matrice-copertura-didattica.md | final | Appendice C |
| 17 | Errori tipici nei bandi EPNE | chapters/appendice-d-errori-tipici-bandi-epne.md | planning/02-matrice-copertura-didattica.md | final | Appendice D |
| 18 | Rinvii ragionati ad altri moduli | chapters/appendice-e-rinvii-ragionati-altri-moduli.md | planning/02-matrice-copertura-didattica.md | final | Appendice E |
| 19 | Materie integrative INAIL/RIPAM | chapters/appendice-f-materie-integrative-inail-ripam.md | planning/02-matrice-copertura-didattica.md | final | Appendice F |

## Stato di partenza

- matrice di copertura del volume: `[[books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/02-matrice-copertura-didattica]]`
- matrice del modulo M-FC02: `[[books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica]]`
- matrici dedicate di M-FC01 e M-FC03: `planning/02-matrice-copertura-didattica.md` nei rispettivi moduli.

## Comandi

```
npm run pipeline -- init VOL-03
npm run pipeline -- status VOL-03
npm run pipeline -- next VOL-03
```
