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

I capitoli non sono dichiarati: la pipeline li deriva da `<module id>/chapters/` e lo registra nel run-state come `chaptersSource: derived`. Dichiararli esplicitamente quando l'ordine di lavorazione dovrà divergere da quello dei file.

## Stato di partenza

- matrice di copertura del volume: `[[books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/02-matrice-copertura-didattica]]`
- matrice del modulo M-FC02: `[[books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica]]`
- M-FC01 e M-FC03 non hanno ancora una matrice dedicata: il gate di copertura li blocca finché il prompt 07 non la produce.

## Comandi

```
npm run pipeline -- init VOL-03
npm run pipeline -- status VOL-03
npm run pipeline -- next VOL-03
```
