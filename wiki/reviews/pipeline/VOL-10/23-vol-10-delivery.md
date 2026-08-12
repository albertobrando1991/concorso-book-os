---
id: review-vol-10-step-23-delivery
type: review
title: "Preparazione del pacchetto di pubblicazione - VOL-10"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "reviews/pipeline/VOL-10/21-vol-10"
  - "reviews/pipeline/VOL-10/22-vol-10-preflight"
book_refs: ["vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"]
updated_at: 2026-08-12
created_at: 2026-08-12
review_required: false
canonical: true
tags: ["vol-10", "pipeline-step-23", "delivery", "publication-candidate"]
---

# Preparazione del pacchetto di pubblicazione — VOL-10

## Esito

Il pacchetto `delivery/VOL-10/candidate/` è completo, autoconsistente e pronto per la conferma finale dello step 24. Non è stato pubblicato e non viene dichiarato approvato.

## Identità

- Versione editoriale: `VOL-10-candidate-2026.08.12.1`
- Data: 12 agosto 2026
- Cut-off normativo/editoriale: 12 agosto 2026
- Commit sorgente: `067e5eb1633f9941a846f3d6c3a3b03d9f9021a9`
- Stato: `publication-candidate`
- Conferma umana: `pending-step-24`

## Contenuto del pacchetto

| File | Funzione |
| --- | --- |
| `vol-10-interior-kdp.pdf` | Interno finale no-bleed, 196 pagine. |
| `REPORT-PUBBLICABILITA.md` | Giudizio editoriale e stato dei rilievi dello step 21. |
| `PREFLIGHT.md` | Sintesi verificabile del preflight dello step 22. |
| `README.md` | Identità, contenuto, esito e uso previsto. |
| `VERSION.json` | Versione strutturata, commit, cut-off e stato. |
| `CHANGELOG.md` | Modifiche consolidate nel candidato. |
| `LIMITS.md` | Limiti, dati mobili e controlli esterni non eseguiti. |
| `MAINTENANCE.md` | Ciclo ordinario, trigger immediati e gate da riaprire. |
| `MANIFEST.sha256` | Hash SHA-256 degli altri otto file. |

- File totali: 9.
- Dimensione totale: 1.301.899 byte.
- SHA-256 del manifest: `7B631AF6FE0DE738FED1AFC5A9E5DC6C7EF59104C6E7F473D60DE851945B7B44`.
- Verifica manifest: 8/8 file presenti, 8/8 hash corrispondenti, nessun file non censito.

## Stato remoto e modifiche dello staff

- Branch locale: `codex/vol10-format2-retrofit`.
- Remote: `origin` su GitHub.
- `git fetch origin` eseguito il 12 agosto 2026.
- Ultimo commit remoto osservato: `3ccdf0a Revisione editoriale completa VOL-01: correzioni, ricettario, conclusione`.
- Divergenza rispetto al merge-base `a25b808`: il remoto contiene 45 commit esclusivi e il branch VOL-10 186 commit esclusivi.
- La scansione dei 45 commit remoti non rileva modifiche nel perimetro VOL-10, nei suoi report, nel PDF o negli script di export usati dal candidato.
- Nessun file remoto o modifica di staff estranea è stato incorporato nel pacchetto.

## Esclusioni intenzionali

- `.next`, cache, dipendenze e output di build;
- log del server e file temporanei;
- tavole-contatto, screenshot e JSON diagnostici degli step 19-22;
- artefatti di altri volumi;
- run-state condiviso e memoria locale dell'agente;
- sorgenti wiki, script e test, che restano nel repository ma non nel candidato KDP;
- copertina, ISBN e metadati commerciali;
- qualunque file non elencato nel manifest.

## Gate tecnici finali

- Audit di copertura: 94 righe accettate, 0 blocker e 0 warning; 78/78 nuclei completi nella vista di volume.
- Audit pagina per pagina: 196/196 pagine, 0 blocker e 0 significativi.
- PDF finale: MediaBox 481,68 × 691,92 pt, font incorporati, no bleed.
- SHA-256 PDF: `FC5546DD591222D96DEED9666476219C7A30BFB171792B26F68F88EB535031C0`.
- Test completi: 48 file, 437 test passati.
- Typecheck: verde.
- Build di produzione: verde, 20/20 pagine statiche.
- `git diff --check`: verde.
- KDP Previewer: non eseguito, limite dichiarato nel pacchetto; nessun esito inventato.

## Decisione

Il candidato supera la preparazione di consegna. Lo step 24 resta aperto e deve confermare il pacchetto prima di qualunque pubblicazione. Un errore rilevato durante upload, Previewer o conferma finale riapre il gate automatico pertinente.
