---
type: pipeline_spec
volume_code: VOL-04
volume_title: Giustizia e Ufficio per il processo
cut_off_date: 2026-10-03
writer_provider: codex
phases: [D, F]
status: active
updated_at: 2026-10-03
review_required: true
---

# Scheda di pipeline — VOL-04

Input della fase finale della pipeline editoriale per `VOL-04`.
Il protocollo dei 25 prompt resta in
`[[templates/prompt-staff-revisione-completa-volumi]]`.

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | ---: | --- |
| M-FC04 | moduli/m-fc04-giustizia | 1 | D,F |

I capitoli non sono dichiarati: la pipeline li deriva da
`moduli/m-fc04-giustizia/chapters/` e registra nel run-state
`chaptersSource: derived`.

## Perimetro della fase finale

- revisione editoriale totale dei diciassette file di M-FC04: quattordici capitoli, appendici, conclusione e fonti;
- controllo incrociato con front matter, indice, matrice didattica e promesse
  del volume commerciale;
- fact-check dei claim normativi e tecnici mobili alla data di chiusura;
- preflight e preparazione del pacchetto soltanto dopo il superamento del gate
  editoriale;
- conferma umana esclusivamente allo step 24.

## Stato di partenza

Il 3 ottobre 2026 si riaprono correzioni, audit specialistico e freeze dopo la revisione integrale del 2 ottobre: 29 rilievi testuali da risolvere, oltre ai rilievi PDF. Le precedenti chiusure della fase F documentano soltanto il candidato storico, non il nuovo testo. Il perimetro resta legacy, senza promozione automatica al formato 2.

- volume commerciale: `[[books/vol-04-giustizia-upp/index]]`;
- modulo: `[[books/moduli/m-fc04-giustizia/index]]`;
- matrice: `[[books/vol-04-giustizia-upp/planning/02-matrice-copertura-didattica]]`;
- audit precedente: `[[reviews/review-vol-04-copertura-didattica-integrale-2026-07-22]]`.

## Comandi

```text
npm run pipeline -- init VOL-04
npm run pipeline -- status VOL-04 --json
npm run pipeline -- next VOL-04 --json
```
