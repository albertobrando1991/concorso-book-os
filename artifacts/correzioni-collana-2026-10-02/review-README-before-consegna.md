---
id: review-correzioni-collana-2026-10-02
type: review
title: "Applicazione delle correzioni e integrazioni della collana"
status: in_progress
domain: concorsi-pubblici
topics: []
entities: []
source_refs: [sources/logica-volumi-copertura-concorsobook-v4]
book_refs: [VOL-01, VOL-02, VOL-03, VOL-04, VOL-05, VOL-06, VOL-07, VOL-08, VOL-09, VOL-10, VOL-11, VOL-12]
confidence: medium
created_at: 2026-10-02
updated_at: 2026-10-02
review_required: true
canonical: false
tags: [correzioni, integrazioni, pubblicabilita]
issue_type: corrections_execution
severity: high
affected_pages: []
---

# Correzioni e integrazioni della collana

Mandato autorizzato: applicare le modifiche e integrazioni necessarie a portare i dodici volumi cartacei alla pubblicabilità. Riferimento: [audit integrale](../audit-integrale-2026-10-02/README.md), 582 voci operative. Il registro storico resta invariato.

## Ordine e responsabilità

1. Correzioni sostanziali e integrazione del nucleo comune VOL-01; ripristino della conservazione del contenuto in export.
2. Interventi sui volumi specialistici, fonti consolidate, esempi risolti, quiz, apparati e rinvii verificati.
3. Riallineamento di matrici, figure e produzione cartacea; divisione in tomi quando necessaria, senza riduzione dei corpi tipografici.
4. Controlli indipendenti, audit specialistici e freeze attraverso il CLI; rigenerazione e verifica dei PDF.
5. Preflight e pacchetti completi; conferma umana conclusiva prevista dallo step 24 soltanto dopo i controlli.

Le lavorazioni parallele hanno file distinti: VOL-02; VOL-06/07/12; VOL-03/08/10/11/05; coordinatore per VOL-01/04/09 e codice comune di esportazione, figure scientifiche e consolidamento finale. Modifiche preesistenti preservate. Nessuna pubblicazione commerciale o invio a terzi incluso in questa lavorazione.

## Tracciabilità

`artifacts/correzioni-collana-2026-10-02/registro-applicazione.json` mantiene gli ID dell'audit e separa applicazione e verifica. I rapporti per volume documentano file modificati ed evidenza. Un intervento applicato non è automaticamente verificato; un file modificato non è automaticamente pubblicabile.

Snapshot iniziale dei 326 manoscritti e hash nella stessa cartella. I run-state della pipeline si aggiornano soltanto tramite CLI; i gate non implementati si chiudono soltanto dopo verifica documentata. Restano ferme le esclusioni editoriali concordate, incluse quelle delle precedenti integrazioni.
