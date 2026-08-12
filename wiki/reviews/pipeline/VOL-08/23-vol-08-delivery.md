---
id: review-vol-08-step-23-delivery
type: review
title: "Preparazione del pacchetto di pubblicazione - VOL-08"
status: complete
domain: "concorsi pubblici italiani"
source_refs: ["reviews/pipeline/VOL-08/21-vol-08", "reviews/pipeline/VOL-08/22-vol-08"]
book_refs: ["vol-08-ict-digitale-cybersecurity-dati"]
updated_at: 2026-08-12
review_required: false
canonical: true
tags: ["vol-08", "pipeline-step-23", "delivery", "publication-candidate"]
---

# Preparazione del pacchetto di pubblicazione — VOL-08

## Esito

Il pacchetto `delivery/VOL-08/candidate/` è completo e pronto per la conferma finale dello step 24. Non è stato pubblicato e non viene dichiarato approvato.

## Identità

- Versione: `VOL-08-candidate-2026.08.12.1`
- Cut-off normativo/editoriale: 12 agosto 2026
- Commit sorgente del PDF e del preflight: `701d0bb`
- Stato: `publication-candidate`
- Conferma umana: `pending-step-24`

## Stato remoto e modifiche staff

- `git fetch origin --prune` eseguito il 12 agosto 2026.
- Ultimo remoto osservato: `origin/main` a `3ccdf0a`.
- Il confronto mirato mostra che `origin/main` non contiene ancora il corpus VOL-08 di questo ramo; un merge cieco ne rappresenterebbe i file come cancellati.
- Nessun contenuto remoto è stato sovrascritto e nessuna modifica locale VOL-08 è stata rimossa. Il pacchetto resta isolato sul ramo `codex/vol08-step15-qce`.

## Esclusioni intenzionali

- helper non versionati in `.superpowers/`;
- cache `.next`, log dei server e file temporanei;
- tavole-contatto e screenshot diagnostici;
- artefatti di altri volumi e memoria agentica;
- copertina, ISBN e metadati commerciali;
- qualunque file non elencato in `MANIFEST.sha256`.

## Gate finali

- copertura: 82/82 nuclei, nessuna failure;
- audit pagina per pagina: 231/231, zero blocker;
- test pertinenti: 95/95;
- typecheck e build: verdi;
- PDF: 231 pagine, 6,69 × 9,61 pollici, no-bleed;
- `git diff --cached --check`: da eseguire sullo staging selettivo prima della chiusura;
- KDP Previewer: non disponibile, limite dichiarato senza esito inventato.

## Decisione

Il candidato può passare allo step 24. Qualunque errore rilevato nel sign-off o nel Previewer deve riaprire il gate pertinente.
