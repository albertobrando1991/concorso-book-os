---
type: pipeline_spec
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
writer_provider: codex
phases: [A, B, C, D, E, F]
status: draft
updated_at: 2026-07-31
review_required: true
---

# Scheda di pipeline — VOL-07

Input eseguibile della pipeline editoriale per il volume VOL-07. Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`.

Le fasi A e B sono concluse. La scheda dichiara ora l'intero perimetro editoriale di 25 capitoli e le fasi A-F. La fase C deve essere completata per tutti i target prima della revisione trasversale; lo step 15 esegue l'audit specialistico automatico e la sola conferma umana resta allo step 24.

## Moduli

| Codice | Module id | Priorita | Fasi |
| --- | --- | --- | --- |
| M-SA02 | moduli/m-sa02-professioni-sanitarie | 1 | A,B,C,D,E,F |
| M-SA01 | moduli/m-sa01-sanita-amministrativa | 2 | A,B,C,D,E,F |
| M-SA03 | moduli/m-sa03-dirigenza-medica-sanitaria | 3 | A,B,C,D,E,F |
| M-SA04 | moduli/m-sa04-tecnici-sanitari-prevenzione | 4 | A,B,C,D,E,F |

## Capitoli M-SA02

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Professioni sanitarie: profili, requisiti e prove | chapters/01-mappa-profili-e-prove.md | planning/02-matrice-copertura-didattica.md | completo | Primo ciclo progressivo della fase C |
| 03 | Discipline professionali: autonomia, responsabilità e deontologia | chapters/03-discipline-professionali-autonomia-responsabilita.md | planning/02-matrice-copertura-didattica.md | completo | Secondo ciclo progressivo della fase C; nucleo Discipline professionali specifiche |
| 04 | Assistenza infermieristica, tecniche assistenziali e supporto OSS | chapters/04-assistenza-infermieristica-tecniche-assistenziali-oss.md | planning/02-matrice-copertura-didattica.md | completo | Processo assistenziale, sicurezza, assistenza di base e attribuzione infermiere-OSS |
| 05 | Valutazione clinica, triage, urgenza ed emergenza | chapters/05-valutazione-clinica-triage-urgenza-emergenza.md | planning/02-matrice-copertura-didattica.md | completo | Riconoscimento, priorità, escalation e casi non esecutivi |
| 06 | Prevenzione, continuità assistenziale e presa in carico | chapters/06-prevenzione-continuita-presa-in-carico.md | planning/02-matrice-copertura-didattica.md | completo | Educazione, cronicità, territorio, COT e PDTA |
| 07 | Evidenze scientifiche, PICO, GRADE e applicabilità | chapters/07-evidenze-pico-grade-applicabilita.md | planning/02-matrice-copertura-didattica.md | completo | Ricerca, appraisal, raccomandazioni ed esercizi |
| 08 | Igiene pubblica, epidemiologia, sorveglianza e screening | chapters/08-igiene-pubblica-epidemiologia-screening.md | planning/02-matrice-copertura-didattica.md | completo | Misure, screening, PASSI, PREMAL e ICA |
| 09 | Controlli TPALL, verbalizzazione, campionamento e sanzioni | chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md | planning/02-matrice-copertura-didattica.md | completo | Sopralluogo, atti, campionamento e non conformità |
| 10 | Prova pratica e casi professionali | chapters/10-prova-pratica-casi-professionali.md | planning/02-matrice-copertura-didattica.md | completo | Metodo di soluzione e laboratori distinti per profilo |

Il capitolo tecnico 02 non viene dichiarato perché il nucleo comune del Metodo BANDO resta nel VOL-01 e non deve essere duplicato. L'indice del volume applica una numerazione editoriale continua senza rinominare i target storici 01 e 03.

## Capitoli M-SA01

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 04 | Atti, procedimenti e flussi informativi nelle aziende sanitarie | chapters/04-atti-procedimenti-flussi-informativi.md | planning/02-matrice-copertura-didattica.md | completo | Atti e procedimenti aziendali; flussi informativi sanitari |
| 05 | Documentazione sanitaria, accesso, privacy e conservazione | chapters/05-documentazione-accesso-conservazione.md | planning/02-matrice-copertura-didattica.md | completo | Documentazione sanitaria, accesso, privacy, FSE, dossier e conservazione |
| 06 | Front office e comunicazione con l'utenza | chapters/06-front-office-comunicazione-utenza.md | planning/02-matrice-copertura-didattica.md | completo | Front office, comunicazione, reclami, accessibilità e riservatezza |
| 09 | Contabilità, budget e controllo di gestione | chapters/09-contabilita-budget-controllo-gestione.md | planning/02-matrice-copertura-didattica.md | completo | Contabilità economico-patrimoniale, budget e controllo di gestione |
| 10 | Procurement sanitario, farmaci, dispositivi e magazzino | chapters/10-procurement-farmaci-dispositivi-magazzino.md | planning/02-matrice-copertura-didattica.md | completo | Procurement sanitario, farmaci, dispositivi, magazzino e ciclo passivo |

I cinque capitoli M-SA01 hanno già completato gli step 08-12; resta obbligatorio l'audit specialistico automatico dello step 15.

## Capitoli M-SA03

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Profili, requisiti e prove della dirigenza sanitaria | chapters/01-profili-requisiti-prove-dirigenza-sanitaria.md | planning/02-matrice-copertura-didattica.md | completo | Famiglie dirigenziali, requisiti e forme di prova |
| 02 | Programmazione sanitaria e organizzazione dei servizi | chapters/02-programmazione-sanitaria-organizzazione-servizi.md | planning/02-matrice-copertura-didattica.md | completo | Bisogni, livelli, obiettivi, risorse e indicatori |
| 03 | Linee guida, appropriatezza e decisioni cliniche | chapters/03-linee-guida-appropriatezza-decisioni-cliniche.md | planning/02-matrice-copertura-didattica.md | completo | Evidenze, raccomandazioni, adattamento e applicabilità |
| 04 | Governo clinico, HTA, qualità, accreditamento e rischio | chapters/04-governo-clinico-hta-qualita-accreditamento-rischio.md | planning/02-matrice-copertura-didattica.md | completo | Governance, audit, tecnologie, qualità e sicurezza |
| 05 | Epidemiologia e sanità pubblica per la dirigenza | chapters/05-epidemiologia-sanita-pubblica-dirigenza.md | planning/02-matrice-copertura-didattica.md | completo | Misure, sorveglianza, screening e decisioni |
| 06 | Dirigenza medica: discipline e casi | chapters/06-dirigenza-medica-discipline-casi.md | planning/02-matrice-copertura-didattica.md | completo | Verticale medico non sostitutivo dei manuali di specialità |
| 07 | Dirigenza sanitaria non medica: discipline e casi | chapters/07-dirigenza-sanitaria-non-medica-discipline-casi.md | planning/02-matrice-copertura-didattica.md | completo | Verticali distinti secondo il profilo del bando |

## Capitoli M-SA04

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Profili TSLB e TSRM: requisiti, prove e responsabilità | chapters/01-profili-tslb-tsrm-requisiti-prove-responsabilita.md | planning/02-matrice-copertura-didattica.md | completo | Profili distinti, titoli, responsabilità e prove |
| 02 | TSLB: processo di laboratorio, qualità e biosicurezza | chapters/02-tslb-processo-laboratorio-qualita-biosicurezza.md | planning/02-matrice-copertura-didattica.md | completo | Ciclo di laboratorio, discipline applicate e sicurezza |
| 03 | TSRM: imaging, dosimetria e radioprotezione | chapters/03-tsrm-imaging-dosimetria-radioprotezione.md | planning/02-matrice-copertura-didattica.md | completo | Tecniche, qualità dell'immagine, dose e protezione |
| 04 | Tecnologie, dispositivi, apparecchiature e rischio | chapters/04-tecnologie-dispositivi-apparecchiature-rischio.md | planning/02-matrice-copertura-didattica.md | completo | Ciclo di vita, vigilanza e miglioramento |

I 25 target autorizzano i cicli 08-12. Le fasi D-F sono configurate per rendere visibile l'intero percorso: lo step 15 deve chiudere automaticamente ogni criticità specialistica, mentre il gate umano compare soltanto allo step 24.

## Input canonici

- Source note: `[[sources/vol-07-dossier-fonti-materie-sanita-2026-07-28]]`.
- Dossier source-ready: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/01-dossier-source-ready]]`.
- Matrice di copertura: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/02-matrice-copertura-didattica]]`.
- Inventario fonti: `[[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/03-mappa-fonti-specialistiche]]`.

## Gate iniziali

- Il dossier raw non è una fonte diretta per i capitoli.
- I tre URL espliciti sono localizzatori `da_verificare`.
- Ogni fonte specialistica richiede una source note ufficiale autonoma.
- Contenuti normativi, clinici e professionali richiedono fonti consolidate e audit specialistico automatico prima del text freeze.
- Le frequenze dei bandi restano `ND` finché il campione non è adeguato.

## Comandi

```text
npm run pipeline -- init VOL-07
npm run pipeline -- status VOL-07
npm run pipeline -- next VOL-07
```
