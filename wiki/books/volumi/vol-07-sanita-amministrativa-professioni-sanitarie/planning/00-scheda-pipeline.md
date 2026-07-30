---
type: pipeline_spec
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [A, B]
status: draft
updated_at: 2026-07-28
review_required: true
---

# Scheda di pipeline — VOL-07

Input eseguibile della pipeline editoriale per il volume VOL-07. Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`.

La prima inizializzazione abilita soltanto le fasi A e B: inquadramento, fonti, indice e architettura. Le fasi C, D e F saranno aggiunte con `sync` dopo il consolidamento del corpus ufficiale; la fase E seguirà il congelamento del testo.

## Moduli

| Codice | Module id | Priorita | Fasi |
| --- | --- | --- | --- |
| M-SA02 | moduli/m-sa02-professioni-sanitarie | 1 | A,B |
| M-SA01 | moduli/m-sa01-sanita-amministrativa | 2 | A,B,C |
| M-SA03 | moduli/m-sa03-dirigenza-medica-sanitaria | 3 | A,B |
| M-SA04 | moduli/m-sa04-tecnici-sanitari-prevenzione | 4 | A,B |

## Capitoli M-SA01

| # | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- |
| 04 | chapters/04-atti-procedimenti-flussi-informativi.md | planning/02-matrice-copertura-didattica.md | completo | Atti e procedimenti aziendali; flussi informativi sanitari |
| 05 | chapters/05-documentazione-accesso-conservazione.md | planning/02-matrice-copertura-didattica.md | completo | Documentazione sanitaria, accesso, privacy, FSE, dossier e conservazione |
| 06 | chapters/06-front-office-comunicazione-utenza.md | planning/02-matrice-copertura-didattica.md | completo | Front-office, comunicazione, reclami, accessibilità e riservatezza |
| 09 | chapters/09-contabilita-budget-controllo-gestione.md | planning/02-matrice-copertura-didattica.md | completo | Contabilità economico-patrimoniale, budget e controllo di gestione |
| 10 | chapters/10-procurement-farmaci-dispositivi-magazzino.md | planning/02-matrice-copertura-didattica.md | completo | Procurement sanitario, farmaci, dispositivi, magazzino e ciclo passivo |

La fase C di M-SA01 procede progressivamente dal capitolo 04; le review dello step 15 restano obbligatorie. Nessun capitolo M-SA01 è dichiarato già scritto.

I capitoli sono derivati dagli scaffold presenti in `<module id>/chapters/`. In questa fase la pipeline incontra soltanto `00-piano-editoriale.md`: non autorizza la generazione di capitoli specialistici senza fonti consolidate.

## Input canonici

- Source note: `[[sources/vol-07-dossier-fonti-materie-sanita-2026-07-28]]`.
- Dossier source-ready: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/01-dossier-source-ready]]`.
- Matrice di copertura: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/02-matrice-copertura-didattica]]`.
- Inventario fonti: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/03-mappa-fonti-specialistiche]]`.

## Gate iniziali

- Il dossier raw non è una fonte diretta per i capitoli.
- I tre URL espliciti sono localizzatori `da_verificare`.
- Ogni fonte specialistica richiede una source note ufficiale autonoma.
- Contenuti normativi, clinici e professionali richiedono review umana.
- Le frequenze dei bandi restano `ND` finché il campione non è adeguato.

## Comandi

```text
npm run pipeline -- init VOL-07
npm run pipeline -- status VOL-07
npm run pipeline -- next VOL-07
```
