---
id: pipeline-vol-12-07-chiusura-fase-b
type: pipeline_review
title: "VOL-12 — Chiusura della fase B ed esito dei quattro gate di copertura"
volume_code: VOL-12
step: "07"
phase: B
scope: volume
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-07", "fase-b", "gate-coverage"]
---

# VOL-12 — Chiusura della fase B ed esito dei quattro gate

Data di controllo delle fonti: **2026-08-10**.

## Stato della pipeline

`13 done · 1 in-progress · 3 pending` su 17 step delle fasi A-B.

Completati: 00-04 di volume e **05-06 su tutti e quattro i moduli**. I quattro step 07 restano aperti perché il gate `coverage` non passa, ed è l'esito corretto.

## Esito dei quattro gate

| Modulo | Nuclei | Blocker | Esito |
| --- | ---: | ---: | --- |
| M-SP01 | 26 | 26 `blocking-status` | 🔴 non superato |
| M-SP02 | 21 | 21 `blocking-status` | 🔴 non superato |
| M-SP03 | 23 | 23 `blocking-status` | 🔴 non superato |
| M-SP04 | 24 | 24 `blocking-status` | 🔴 non superato |
| **Totale** | **94** | **94** | — |

Il numero dei blocker coincide esattamente con quello dei nuclei in ogni modulo: nessun falso positivo, nessuna riga spuria. Tutti i nuclei sono `mancante` perché **nessun capitolo esiste**.

Nessuno dei quattro step è stato chiuso con `--accept`. Il gate è implementato, è stato eseguito e ha dato esito negativo su base reale: forzarlo scriverebbe una falsità nel run-state.

## Corpus documentale acquisito

**16 PDF ufficiali, circa 36 MB**, in `wiki/raw/m-sp0*/`.

| Modulo | Documenti | Livello |
| --- | --- | --- |
| M-SP01 | 12 — bandi PS 4.400, CC 3.081, CC 898 con decreto di modifica, GdF 983, CC ufficiali 208°; procedure PS su prove fisiche, accertamenti psico-fisici e attitudinali; norme tecniche CC | corpus più ampio |
| M-SP02 | 2 — bandi VVF 400 e VVF 8 vice direttori informatici | entrambi letti sull'articolato |
| M-SP03 | 0 | **contorno verificato, articolato ignoto** |
| M-SP04 | 2 — bandi carriera prefettizia 158 e MAECI 35 | entrambi letti sull'articolato |

Sette source note consolidate prodotte per il volume.

## Cosa hanno cambiato gli audit

Nessuno dei quattro moduli è uscito dalla fase B con la struttura con cui vi era entrato.

| Modulo | Assunto iniziale | Evidenza dei bandi |
| --- | --- | --- |
| M-SP01 | binario unico, tre corpi a confronto | due binari **base** e **ispettivo**, che attraversano i tre corpi; prova scritta con tre formati incompatibili allo stesso livello. Da 11 a 15 sezioni |
| M-SP02 | doppio binario con materie tecniche | confermato il doppio binario, **smentite le materie**: nel concorso base non esiste una prova scritta d'esame, e il 95% dei posti è riservato. Da 13 a 14 sezioni, con contenuti diversi |
| M-SP03 | tre binari | confermato, con l'aggiunta di tre vincoli decisivi: proporzioni 450/400/**7**, compiuta pratica notarile come prerequisito, calendari mutuamente esclusivi |
| M-SP04 | due binari, orizzonte 6-12 mesi | confermati i binari; **cinque prove scritte** per la prefettizia e **limite di quattro tentativi** per la diplomatica impongono di rivedere l'orizzonte |

Cinque pattern trasversali sono stati consolidati nella Bibbia del Volume anziché lasciati a ricostruzioni parallele nei moduli.

## Blocker residui, per natura

**Di reperimento** — documenti che non esistono ancora nel repository:

- 🔴 i tre bandi di M-SP03 in PDF: d.m. 22 ottobre 2025, D.A.G. 30 maggio 2025, d.m. 16 dicembre 2025;
- 🔴 ordinamento del notariato; ordinamento della carriera prefettizia e di quella diplomatica; organizzazione del soccorso pubblico;
- 🔴 allegati A e B del bando VVF 400, che determinano la prova d'esame che vale 90 punti su 95;
- 🔴 d.m. Interno 166/2019 e d.m. 29 luglio 1999 n. 357;
- 🟠 norme tecniche delle prove fisiche GdF; bando GdF 69 allievi ufficiali; bando VVF per vice direttore del ruolo ordinario.

**Di verifica** — atti individuati ma non letti nel testo vigente:

- d.lgs. 95/2017 dopo i correttivi; d.lgs. 217/2005; d.lgs. 199/1995; d.lgs. 160/2006; r.d. 1860/1925.

**Riservati a review umana** — non risolvibili per deduzione:

- il rapporto fra d.m. 198/2003 e la giurisprudenza successiva sui requisiti di accesso alle forze di polizia;
- la questione dei titoli di accesso alla magistratura, se sia davvero venuto meno l'obbligo di SSPL e abilitazione forense.

## Decisioni di perimetro aperte

1. **Livello ufficiali in M-SP01** — l'acquisizione del bando per il 208° corso dell'Accademia Militare ha rivelato un terzo livello di ruolo. Va incluso come terzo binario o escluso con motivazione esplicita.
2. **Prevenzione incendi e protezione civile in M-SP02** — non risultano materie d'esame nel concorso base. Le sezioni corrispondenti vanno ridimensionate o soppresse.
3. **Confine con le Forze armate** — la decisione 1 interseca l'esclusione dichiarata delle Forze armate dal perimetro di volume.

## Condizione per aprire la fase C

1. chiudere i blocker di reperimento e di verifica sopra elencati;
2. chiudere le due questioni riservate a review umana;
3. sciogliere le tre decisioni di perimetro;
4. dichiarare i capitoli approvati nella scheda di pipeline ed estendere a `phases: [A, B, C, D, E, F]`;
5. eseguire `npm run pipeline -- sync VOL-12 --json`;
6. scrivere i capitoli;
7. rieseguire i quattro gate `coverage`.

## Esito

Fase B **sostanzialmente conclusa** sul piano dell'istruttoria: quattro moduli mappati, 94 nuclei definiti, 16 documenti ufficiali acquisiti, quattro architetture corrette sull'evidenza anziché su assunti.

Fase B **non chiusa formalmente**: i quattro gate di copertura restano aperti e resteranno tali finché i capitoli non saranno scritti. È il comportamento previsto.

**VOL-12 non è un candidato alla pubblicazione e non deve comparire in alcun materiale commerciale.**
