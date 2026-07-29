---
type: pipeline_spec
volume_code: VOL-02
volume_title: Enti locali, Camere di commercio e Polizia locale
cut_off_date: 2026-07-24
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [C, D, F]
status: draft
updated_at: 2026-07-29
review_required: true
---

# Scheda di pipeline — VOL-02

Input della pipeline editoriale per VOL-02. Il protocollo dei 25 prompt resta in `wiki/templates/prompt-staff-revisione-completa-volumi.md`.

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | ---: | --- |
| M-FL01 | moduli/m-fl01-comuni-unioni | 1 | C,D |
| M-FL02 | moduli/m-fl02-regioni-province-citta-metropolitane | 2 | C,D |
| M-FL04 | moduli/m-fl04-polizia-locale | 3 | C,D |
| M-FL03 | moduli/m-fl03-camere-commercio | 4 | C,D |

I capitoli sono derivati dai file presenti nelle cartelle `chapters/`; la pipeline registrerà `chaptersSource: derived` nel run-state. Il capitolo finale VOL-02 e i capitoli di orientamento restano nella fase F del volume.

## Stato di partenza

- indice dettagliato: `wiki/books/vol-02-enti-locali-polizia-locale/planning/01-indice-dettagliato-volume-moduli-v4.md`
- matrice di copertura: `wiki/books/vol-02-enti-locali-polizia-locale/planning/02-matrice-copertura-didattica.md`
- review editoriale: `wiki/reviews/review-vol-02-editorial-revision-2026-07-24.md`
- review normativa umana ancora necessaria; i nuclei `parziale` restano bloccanti.

## Comandi

```text
npm run pipeline -- doctor
npm run pipeline -- init VOL-02
npm run pipeline -- status VOL-02 --json
npm run pipeline -- next VOL-02
```
