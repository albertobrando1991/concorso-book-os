---
id: review-vol-07-pipeline-02-consolidamento-contributi
type: review
title: "VOL-07 - Consolidamento dei contributi dello staff"
status: complete
domain: "concorsi pubblici italiani"
topics: ["pipeline editoriale", "consolidamento contributi"]
entities: ["ConcorsoBook OS"]
source_refs: ["sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md"]
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.96
updated_at: 2026-07-28T15:00:00+02:00
created_at: 2026-07-28T15:00:00+02:00
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-07", "consolidation"]
issue_type: staff_contribution_consolidation
severity: low
affected_pages: []
---

# VOL-07 - Consolidamento dei contributi dello staff

## Esito

Il censimento dello step 01 non ha rilevato contributi approvati esterni al branch `vol-07-pipeline-start`, versioni concorrenti o file sanitari presenti in altri worktree. Non è quindi necessaria alcuna fusione editoriale.

Il pacchetto VOL-07 già presente nel branch viene preservato integralmente:

- raw immutabile e source note del dossier;
- inventario delle 74 fonti/famiglie;
- matrice iniziale delle 48 materie specialistiche;
- volume aggregator e scheda pipeline;
- scaffold dei quattro moduli;
- topic, entity page, memoria, indice e log;
- test e correzioni dell'orchestratore.

## Registro delle integrazioni

| Origine del contributo | Integrazione applicata | Contenuto preservato | Conflitti rimasti |
| --- | --- | --- | --- |
| Nessun contributo esterno approvato | Nessuna integrazione necessaria | Intero pacchetto VOL-07 del branch | Nessuno |

## Esclusioni intenzionali

- `.claude/settings.local.json` resta locale, non tracciato e non modificato.
- Le incoerenze storiche di M-FL01, M-FL02 e M-FC04 restano soltanto segnalate nel report 01.
- Non sono stati duplicati capitoli, tabelle, fonti o immagini.
- Non sono stati creati capitoli sanitari prima del consolidamento delle fonti.

## Verifica

Il riepilogo Git contiene soltanto i due report di pipeline e l'aggiornamento del run-state prodotto dal CLI. `git diff --check` non segnala errori. Non sono stati eseguiti commit o push durante lo step.
