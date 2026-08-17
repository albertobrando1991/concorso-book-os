---
id: pipeline-vol-12-01-censimento-lavoro-staff
type: pipeline_review
title: "VOL-12 — Step 01: censimento del lavoro dello staff"
volume_code: VOL-12
step: "01"
phase: A
scope: catalog
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-01", "censimento"]
---

# VOL-12 — Step 01: censimento del lavoro dello staff

Censimento eseguito il 2026-08-11 sul branch `main`, commit `a61d5fc`. Nessun file è stato sovrascritto o integrato in questo step.

## Stato del repository

- Branch: `main`. Nessun altro branch locale con lavoro editoriale in corso.
- Ultimo commit: `a61d5fc docs: plan complete VOL-12 pipeline`.
- File modificati e non committati: **550**.
- File non tracciati: **473**, in larghissima parte artefatti PNG di contact sheet VOL-02 in `artifacts/`.
- Nessun conflitto di merge aperto. Nessuna versione concorrente dello stesso file editoriale rilevata.

Il worktree è quindi pesantemente caricato di lavoro non committato **estraneo a VOL-12**: revisione VOL-01/Book Studio e capitoli M-FL01/M-FL02. È la principale sorgente di rischio di collisione per gli step successivi.

## Censimento dei moduli

Conteggio dei capitoli effettivamente presenti in `chapters/` e delle parole di testo.

| Volume | Modulo | Capitoli | Parole | Planning | Stato contenuto | Stato fonti | Stato immagini | Collisione | Azione proposta |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| VOL-12 | M-SP01 forze di polizia | 0 | 0 | 1 | scaffold | da completare | assenti | no | audit bandi 05 |
| VOL-12 | M-SP02 vigili del fuoco | 0 | 0 | 1 | scaffold | da completare | assenti | no | audit bandi 05 |
| VOL-12 | M-SP03 magistratura e affini | 0 | 0 | 1 | scaffold | da completare | assenti | no | audit bandi 05 |
| VOL-12 | M-SP04 prefettizia e diplomatica | 0 | 0 | 1 | scaffold | da completare | assenti | no | audit bandi 05 |
| VOL-07 | M-SA02 professioni sanitarie | 9 | 46.670 | 9 | utilizzabile | consolidate | presenti | no | nessuna, fuori perimetro |
| VOL-07 | M-SA01 sanità amministrativa | 5 | 31.588 | 3 | utilizzabile | consolidate | presenti | no | nessuna, fuori perimetro |
| VOL-07 | M-SA03 dirigenza sanitaria | 7 | 17.854 | 3 | utilizzabile | consolidate | presenti | no | nessuna, fuori perimetro |
| VOL-07 | M-SA04 tecnici sanitari | 4 | 19.008 | 3 | utilizzabile | consolidate | presenti | no | nessuna, fuori perimetro |
| VOL-02 | M-FL01 comuni e unioni | 14 | 80.581 | 4 | utilizzabile | da verificare | presenti | **sì** | 14 capitoli modificati non committati |
| VOL-02 | M-FL04 polizia locale | 15 | 67.269 | 4 | utilizzabile | da verificare | presenti | **sì** | worktree sporco |
| VOL-02 | M-FL02 regioni e province | 12 | 72.645 | 4 | utilizzabile | da verificare | presenti | **sì** | worktree sporco |
| VOL-03 | M-FC02 agenzie fiscali | 16 | 81.857 | 3 | utilizzabile | da verificare | presenti | no | fuori perimetro |
| VOL-04 | M-FC04 giustizia | 14 | 72.140 | 1 | utilizzabile | da verificare | presenti | no | fuori perimetro |
| VOL-05 | M-FC05 authority | 15 | 44.852 | 1 | da consolidare | da verificare | da verificare | no | media 2.990 parole/capitolo |
| — | M-FL03 camere di commercio | 5 | 24.661 | 3 | da completare | da verificare | da verificare | no | modulo parziale |
| — | **M-FC01 ministeri** | 15 | **8.855** | 1 | **da verificare** | da verificare | da verificare | no | **vedi rilievo sotto** |
| — | M-FC03 enti non economici | 0 | 0 | 2 | scaffold | da completare | assenti | no | fuori perimetro |
| — | M-IR01 · M-IR02 · M-IR03 · M-IR04 | 0 | 0 | 1 cad. | scaffold | da completare | assenti | no | fuori perimetro |
| — | M-TR01 · M-TR02 · M-TR03 · M-TR04 | 0 | 0 | 1 cad. | scaffold | da completare | assenti | no | fuori perimetro |

## Rilievo fuori perimetro da segnalare allo staff

**M-FC01 ministeri — 13 capitoli su 15 sono stub presentati come capitoli.**

Il modulo dichiara 15 file in `chapters/`, ma la distribuzione delle parole è questa:

| Capitolo | Parole |
| --- | ---: |
| `01-lavorare-ministeri-funzioni-centrali.md` | 4.182 |
| `02-anatomia-bando-ministeriale-ripam.md` | 2.910 |
| gli altri 13 file | **126 – 152 ciascuno** |

Totale del modulo: 8.855 parole su 15 capitoli. Un modulo comparabile della stessa collana ne conta 67.000-80.000. I 13 file sotto le 152 parole non sono capitoli brevi: sono scaffold con il nome di un capitolo. Un conteggio automatico che si limiti a contare i file restituisce «15 capitoli» e classifica il modulo come sviluppato.

**Classificazione: da verificare / scaffold mascherato.** È fuori dal perimetro di VOL-12 e non viene toccato in questa pipeline, ma va segnalato perché falsa qualsiasi metrica di copertura globale che conti i file invece delle parole.

## Contenuti non presenti nel branch principale

Nessun contenuto editoriale di VOL-12 esiste in forma non committata: i quattro moduli non hanno capitoli né in `main` né nel worktree.

Non risultano branch, stash o directory alternative contenenti bozze dei moduli M-SP. **Non esiste lavoro pregresso da recuperare per questo volume.**

## Fonti già presenti riutilizzabili per VOL-12

Su 321 source notes schedate, nessuna è stata prodotta per la famiglia Carriere Speciali. Sono però presenti fonti tangenzialmente pertinenti, prodotte per altri moduli, da rivalutare nell'audit dello step 06:

| Fonte | Pertinenza potenziale | Classificazione |
| --- | --- | --- |
| `corte-costituzionale-requisiti-concorsuali-polizia-di-stato-g-u-27-gennaio-2021.md` | M-SP01, requisiti di accesso | da verificare |
| `codice-procedura-penale-polizia-giudiziaria.md` | M-SP01, materie specialistiche | da verificare |
| `regio-decreto-18-giugno-1931-n-773-tulps-polizia-amministrativa.md` | M-SP01, pubblica sicurezza | da verificare |
| `avvocatura-stato-organizzazione-funzioni.md` | M-SP03 binario B | da verificare |
| `rd-30-ottobre-1933-n-1611-avvocatura-stato.md` | M-SP03 binario B | da verificare |
| `ministero-interno-dait-anpr-finanza-locale.md` | M-SP04 binario A, marginale | da verificare |

Nessuna fonte esiste per M-SP02 (Corpo nazionale dei vigili del fuoco), per la magistratura ordinaria, per il notariato e per la carriera diplomatica. **Sono quattro vuoti da colmare integralmente allo step 06.**

Tutte le fonti sopra elencate sono state prodotte con un cut-off e per un perimetro diversi: nessuna è utilizzabile senza rischedatura per il perimetro VOL-12.

## Collisioni e cautele per gli step successivi

1. Il worktree contiene 550 file modificati non committati. Ogni step VOL-12 deve limitare le scritture al proprio perimetro e non eseguire operazioni git distruttive.
2. `src/catalog/text-volumes.ts` è già modificato da lavoro preesistente: le modifiche VOL-12 su quel file restano circoscritte a due stringhe.
3. Gli artefatti PNG non tracciati in `artifacts/` non vanno rimossi: appartengono alla revisione VOL-02 in corso.

## Esito

Il censimento non ha trovato **alcun contenuto editoriale VOL-12 da consolidare**. Lo step 02, che consolida i contributi dello staff, opererà quindi su un insieme vuoto: è l'esito atteso e va registrato come tale, non come anomalia.
