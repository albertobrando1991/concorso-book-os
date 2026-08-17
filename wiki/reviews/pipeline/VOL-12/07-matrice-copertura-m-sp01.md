---
id: pipeline-vol-12-07-matrice-copertura-m-sp01
type: pipeline_review
title: "VOL-12 — Step 07: matrice di copertura didattica M-SP01 ed esito del gate"
volume_code: VOL-12
step: "07"
phase: B
scope: module
module_code: M-SP01
domain: "concorsi pubblici italiani"
source_refs: ["sources/bandi-rappresentativi-m-sp01-forze-polizia-2026", "sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01"]
book_refs: ["m-sp01-forze-ordine", "vol-12-carriere-speciali-premium"]
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-07", "m-sp01", "gate-coverage"]
---

# VOL-12 — Step 07: matrice di copertura didattica M-SP01 ed esito del gate

Matrice prodotta: [[books/moduli/m-sp01-forze-ordine/planning/02-matrice-copertura-didattica]].

## Esito del gate `coverage`

```
npm run pipeline -- gate VOL-12 --step 07 --module M-SP01 --json
```

```
passed: false
blockers: 26 { 'blocking-status': 26 }
```

**Il gate non passa, ed è l'esito corretto.** Ventisei nuclei su ventisei sono in stato `mancante` perché il modulo non ha capitoli. Il gate sta facendo esattamente ciò per cui esiste: impedire l'ingresso in fase C a un modulo privo di contenuto.

Lo step 07 **non viene chiuso**. Non è un caso di `gate-not-implemented`: il gate è implementato, è stato eseguito e ha dato esito negativo su base reale. Chiuderlo con `--accept` sarebbe una forzatura, non una verifica manuale.

## Correzione applicata durante l'esecuzione

La prima esecuzione del gate ha restituito **32 blocker** invece di 26, con codici anomali: `incomplete-complete-row`, `missing-referral-destination` e due `invalid-status`.

Causa: `parseCoverageMatrix` in `src/server/editorial/didactic-coverage.ts:95` considera riga di matrice qualunque riga di **qualunque tabella** del file la cui intestazione contenga una colonna «Stato». La tabella riepilogativa dei totali, che usava proprio quell'intestazione, veniva letta come se contenesse sei nuclei aggiuntivi.

Correzione: i totali sono stati riscritti come elenco puntato. Il gate riporta ora 26 blocker, uno per nucleo reale.

**Rilievo per lo staff della piattaforma:** è una trappola che si ripresenterà. Chiunque scriva una matrice con una tabella riepilogativa intitolata «Stato» ottiene conteggi falsati, in eccesso e con codici fuorvianti. Vale la pena o documentarlo nel template `wiki/templates/didactic-coverage-matrix-template.md`, o restringere il parser alla prima tabella primaria del file. Fuori perimetro VOL-12: **segnalato, non risolto**.

## Blocker in sintesi

Elenco completo e ordinato per priorità nella matrice. In sintesi:

**Alta priorità, 7 gruppi.** Due nuclei senza alcuna fonte (efficienza fisica e preparazione atletica); requisiti e cause di esclusione con rapporto irrisolto fra d.m. 198/2003 e giurisprudenza successiva; vigenza del d.lgs. 95/2017 dopo i correttivi; formati della prova scritta al livello ispettivo su bandi non riscontrati; testo vigente degli atti di ordinamento non ancora letto; prova orale; verifica della destinazione del rinvio al VOL-01.

**Media priorità, 5 gruppi.** Contingenti e riserve; titoli e lingua facoltativa; preselezione; accertamento attitudinale; rilettura di TULPS e c.p.p. nel perimetro.

**Bassa priorità, 7 nuclei metodologici**, scrivibili appena i nuclei normativi a monte sono chiusi.

## Condizione di sblocco

Lo step 07 si chiude quando la matrice non contiene più stati `mancante`, `parziale` o `solo-nominato`. Poiché lo stato dipende dall'esistenza dei capitoli, la sequenza reale è:

1. colmare le due fonti assenti e riscontrare i quattro bandi DA VERIFICARE;
2. leggere il testo vigente degli atti individuati;
3. chiudere la review umana sul rapporto d.m. 198/2003 – giurisprudenza;
4. dichiarare i capitoli nella scheda di pipeline ed estendere a `phases: [A, B, C, D, E, F]`;
5. eseguire `sync`;
6. scrivere i capitoli in fase C;
7. rieseguire il gate `coverage`.

## Stato di M-SP01 alla consegna

| Step | Esito |
| --- | --- |
| 05 audit bandi | ✅ chiuso — corpus di 6 bandi su 3 cluster, 2 verificati su fonte ufficiale |
| 06 audit fonti | ✅ chiuso con riserve — 5 nuclei pronti, 8 parziali, 2 senza fonte |
| 07 matrice di copertura | 🔴 **gate non superato** — 26 nuclei `mancante` |

Il modulo ha ora una base documentale reale, un'architettura corretta dall'evidenza e un piano di lavoro per la fase C. Non ha contenuto.
