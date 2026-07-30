---
type: pipeline_spec
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [A, B, C]
status: draft
updated_at: 2026-07-28
review_required: true
---

# Scheda di pipeline — VOL-07

Input eseguibile della pipeline editoriale per il volume VOL-07. Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`.

Le fasi A e B sono concluse. La fase C è stata aperta in modo progressivo sui capitoli 01 e 03 di M-SA02. Le fasi D-F non sono attivate; ogni eventuale avanzamento resta affidato al CLI dopo le review obbligatorie.

## Moduli

| Codice | Module id | Priorita | Fasi |
| --- | --- | --- | --- |
| M-SA02 | moduli/m-sa02-professioni-sanitarie | 1 | A,B,C |
| M-SA01 | moduli/m-sa01-sanita-amministrativa | 2 | A,B,C |
| M-SA03 | moduli/m-sa03-dirigenza-medica-sanitaria | 3 | A,B |
| M-SA04 | moduli/m-sa04-tecnici-sanitari-prevenzione | 4 | A,B |

## Capitoli M-SA02

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Professioni sanitarie: profili, requisiti e prove | chapters/01-mappa-profili-e-prove.md | planning/02-matrice-copertura-didattica.md | completo | Primo ciclo progressivo della fase C |
| 03 | Discipline professionali: autonomia, responsabilità e deontologia | chapters/03-discipline-professionali-autonomia-responsabilita.md | planning/02-matrice-copertura-didattica.md | completo | Secondo ciclo progressivo della fase C; nucleo Discipline professionali specifiche |

La fase C procede in modo progressivo sui capitoli 01 e 03 di M-SA02. Il capitolo 02 non viene dichiarato perché il nucleo comune del Metodo BANDO resta nel VOL-01 e non deve essere duplicato.

## Capitoli M-SA01

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 04 | Atti, procedimenti e flussi informativi nelle aziende sanitarie | chapters/04-atti-procedimenti-flussi-informativi.md | planning/02-matrice-copertura-didattica.md | completo | Atti e procedimenti aziendali; flussi informativi sanitari |
| 05 | Documentazione sanitaria, accesso, privacy e conservazione | chapters/05-documentazione-accesso-conservazione.md | planning/02-matrice-copertura-didattica.md | completo | Documentazione sanitaria, accesso, privacy, FSE, dossier e conservazione |
| 06 | Front office e comunicazione con l'utenza | chapters/06-front-office-comunicazione-utenza.md | planning/02-matrice-copertura-didattica.md | completo | Front office, comunicazione, reclami, accessibilità e riservatezza |
| 09 | Contabilità, budget e controllo di gestione | chapters/09-contabilita-budget-controllo-gestione.md | planning/02-matrice-copertura-didattica.md | completo | Contabilità economico-patrimoniale, budget e controllo di gestione |
| 10 | Procurement sanitario, farmaci, dispositivi e magazzino | chapters/10-procurement-farmaci-dispositivi-magazzino.md | planning/02-matrice-copertura-didattica.md | completo | Procurement sanitario, farmaci, dispositivi, magazzino e ciclo passivo |

La fase C di M-SA01 procede progressivamente dal capitolo 04; le review dello step 15 restano obbligatorie. Nessun capitolo M-SA01 è dichiarato già scritto.

I capitoli 01 e 03 di M-SA02 sono dichiarati esplicitamente; gli altri moduli continuano a derivare gli eventuali capitoli dagli scaffold presenti in `<module id>/chapters/`. La dichiarazione autorizza il ciclo 08-12 soltanto sui target indicati e non abilita ancora i capitoli successivi o le fasi D-F.

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
