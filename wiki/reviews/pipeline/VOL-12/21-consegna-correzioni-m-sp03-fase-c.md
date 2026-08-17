---
id: pipeline-vol-12-21-consegna-correzioni-m-sp03
type: pipeline_handover
title: 'VOL-12 — M-SP03: consegna correzioni fase C'
volume_code: VOL-12
phase: C
scope: module
target: moduli/m-sp03-magistratura-avvocatura-notariato
executor: codex
reviewer: claude-code
domain: 'concorsi pubblici italiani'
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ['pipeline', 'vol-12', 'm-sp03', 'handover', 'correzioni']
---

# Consegna correzioni M-SP03 — fase C

Data: 2026-08-13.

## Correzione eseguita

Rimosse da tutti e sette i capitoli le sezioni finali identiche `Spiegazione teorica`, `Applicazione e caso` ed `Errori e trappole`, insieme alle tre frasi di metatesto che le accompagnavano.

Nel capitolo 01 è stato rimosso anche l'heading isolato `Inquadramento`. La sua idea reale — scegliere in sequenza professione, requisiti, prove e piano — è confluita nel nucleo `N-SP03-01-01`, senza perdita di contenuto.

Per evitare che il lint dipenda di nuovo da sezioni vuote, contenuti già presenti dentro i nuclei hanno ricevuto heading di terzo livello: un caso ragionato, l'errore tipico pertinente e, dove necessario, i principi teorici o di metodo. Il testo sostanziale non è stato riscritto.

## Esito dei gate

Esecuzione diretta degli analizzatori del repository:

- `runDidacticDensityGate({ content, chapterPath })`;
- `runChapterLintGate({ content, chapterPath, requireFormatVersion2: true })`.

| Capitolo | Parole | Nuclei (min–max) | Quiz | Casi | Verifiche | didactic-density | chapter-lint |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 01 — Mappa e scelta | 3951 | 5 (681–776) | 15 | 5 | 5 | PASS | PASS |
| 02 — Magistratura | 3427 | 5 (601–687) | 10 | 5 | 5 | PASS | PASS |
| 03 — Avvocatura dello Stato | 3342 | 5 (607–646) | 10 | 5 | 5 | PASS | PASS |
| 04 — Notariato | 3300 | 5 (605–645) | 10 | 5 | 5 | PASS | PASS |
| 05 — Metodo delle prove scritte | 3514 | 5 (668–686) | 10 | 5 | 5 | PASS | PASS |
| 06 — Piano pluriennale | 3722 | 5 (709–730) | 10 | 5 | 5 | PASS | PASS |
| 07 — Errori, casi e checklist | 3236 | 5 (614–626) | 10 | 5 | 5 | PASS | PASS |

Esito complessivo: **14/14 gate PASS**, senza blocker e senza warning.

## Contenuto preservato

- Conservati i blocchi `▣ Verifica` distribuiti per nucleo.
- Conservati i casi ragionati dentro i nuclei; soltanto il primo caso di ogni capitolo è stato promosso a sottosezione riconoscibile dal lint.
- Conservato il trattamento dell'art. 5 della L. 89/1913, compresa la dichiarazione sul limite del PDF locale storico e la verifica del dato tramite fonte ulteriore.
- Conservato il contenuto normativo già verificato.
- Nessun intervento sul formato dei quiz, indicato dalla review come nota non bloccante.

## Controlli di perimetro

Le frasi duplicate e i quattro heading da rimuovere non risultano più nel corpus M-SP03. `pipeline/VOL-12/run-state.json` non è stato modificato. Non sono stati eseguiti commit o push.
