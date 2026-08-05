---
id: review-vol-07-step-23-delivery
type: review
title: "Preparazione del pacchetto di pubblicazione - VOL-07"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "reviews/pipeline/VOL-07/21-vol-07"
  - "reviews/pipeline/VOL-07/22-vol-07-preflight"
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-08-05T00:00:00+02:00
review_required: false
canonical: true
tags: ["vol-07", "pipeline-step-23", "delivery", "publication-candidate"]
---

# Preparazione del pacchetto di pubblicazione — VOL-07

## Esito

Il pacchetto `delivery/VOL-07/candidate/` è completo, autoconsistente e pronto per la conferma finale dello step 24. Non è stato pubblicato e non viene dichiarato approvato.

## Identità

- Versione editoriale: `VOL-07-candidate-2026.08.05.1`
- Data: 5 agosto 2026
- Cut-off normativo iniziale: 28 luglio 2026
- Commit sorgente: `a1da022`
- Stato: `publication-candidate`
- Conferma umana: `pending-step-24`

## Contenuto del pacchetto

| File | Funzione |
| --- | --- |
| `vol-07-interior-kdp.pdf` | Interno finale no-bleed, 394 pagine. |
| `REPORT-PUBBLICABILITA.md` | Copia byte-identica del report dello step 21. |
| `PREFLIGHT.md` | Copia byte-identica del report dello step 22, aggiornata all'hash finale. |
| `README.md` | Identità, contenuto, esito e uso previsto. |
| `VERSION.json` | Versione strutturata, commit, cut-off e stato. |
| `CHANGELOG.md` | Modifiche consolidate nel candidato. |
| `LIMITS.md` | Limiti, dati mobili e controlli esterni non eseguiti. |
| `MAINTENANCE.md` | Ciclo ordinario, trigger immediati e gate da riaprire. |
| `MANIFEST.sha256` | Hash SHA-256 degli altri otto file. |

- File totali: 9.
- Dimensione totale: 24.327.440 byte.
- SHA-256 del manifest: `5A749F37A6E2BE3E08F1B3662A9A54CA82F844FD9684E2756FECB5D5A600A3DD`.
- Verifica manifest: 8/8 file presenti, 8/8 hash corrispondenti, nessun file non censito.

## Stato remoto e modifiche dello staff

- Branch: `main`.
- Remote: `origin` su GitHub.
- `git fetch origin` eseguito il 5 agosto 2026.
- Divergenza dopo il fetch: `main` 137 commit avanti e 0 indietro rispetto a `origin/main`.
- Ultimo commit remoto osservato: `a6e5bea feat: sync modifiche locali utente per allineamento staff`.
- Le modifiche locali a VOL-02/M-FL01, memoria agentica e run-state condivisi sono state riconosciute come lavoro dello staff e non incluse nel pacchetto.

## Esclusioni intenzionali

- `.next`, cache e dipendenze;
- log del server e file temporanei;
- tavole-contatto e screenshot diagnostici degli step 19, 20, 22 e 23;
- artefatti di altri volumi;
- run-state condivisi;
- memoria locale dell'agente;
- copertina, ISBN e metadati commerciali;
- qualunque file non elencato nel manifest.

## Gate tecnici finali

- Audit di copertura: 45/45 righe verdi fra volume e moduli.
- Audit pagina per pagina dopo l'ultima correzione visibile: 394/394 pagine, 0 blocker, 0 significativi.
- PDF finale: MediaBox/CropBox 481,68 × 691,92 pt, font incorporati, no bleed.
- SHA-256 PDF: `2BA9C6C130CB52A17767815213A4F90ED7C876E6078E68AD71515A67AEB940A6`.
- Test completi: 47 file, 429 test passati.
- Typecheck: verde.
- Build di produzione: verde.
- `git diff --check`: verde.
- KDP Previewer: non eseguito, limite dichiarato nel pacchetto; nessun esito inventato.

## Decisione

Il candidato supera la preparazione di consegna. Lo step 24 resta aperto e deve confermare il pacchetto prima di qualunque pubblicazione. Un errore rilevato durante upload, Previewer o conferma finale riapre il gate automatico pertinente.
