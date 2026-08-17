---
id: review-vol-12-step-23-delivery
type: review
title: "Preparazione del pacchetto di pubblicazione - VOL-12"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "reviews/pipeline/VOL-12/21-vol-12"
  - "reviews/pipeline/VOL-12/22-vol-12-preflight"
book_refs: ["vol-12-carriere-speciali-premium"]
updated_at: 2026-08-14T19:20:00+02:00
review_required: false
canonical: true
tags: ["vol-12", "pipeline-step-23", "delivery", "publication-candidate"]
---

# Preparazione del pacchetto di pubblicazione - VOL-12

## Esito

Il pacchetto `delivery/VOL-12/candidate/` è completo, autoconsistente e pronto per la conferma finale dello step 24. Non è stato pubblicato e non viene dichiarato approvato.

## Identità

- Versione editoriale: `VOL-12-candidate-2026.08.14.1`
- Data: 14 agosto 2026
- Cut-off editoriale: 14 agosto 2026
- Cut-off delle fonti dichiarato dai capitoli: M-SP01 e M-SP04 10 agosto; M-SP02 e M-SP03 13 agosto 2026
- Commit sorgente locale: `a61d5fc`
- Stato: `publication-candidate`
- Conferma umana: `pending-step-24`

## Contenuto del pacchetto

| File | Funzione |
| --- | --- |
| `vol-12-interior-kdp.pdf` | Interno finale no-bleed, 459 pagine. |
| `REPORT-PUBBLICABILITA.md` | Copia byte-identica del report dello step 21. |
| `PREFLIGHT.md` | Copia byte-identica del report dello step 22. |
| `README.md` | Identità, contenuto, esito e uso previsto. |
| `VERSION.json` | Versione strutturata, commit, cut-off e stato. |
| `CHANGELOG.md` | Modifiche consolidate nel candidato. |
| `LIMITS.md` | Limiti, dati mobili e controlli esterni non eseguiti. |
| `MAINTENANCE.md` | Ciclo ordinario, trigger immediati e gate da riaprire. |
| `MANIFEST.sha256` | Hash SHA-256 degli altri otto file. |

- File totali: 9.
- Dimensione totale: 30.895.348 byte.
- SHA-256 del manifest: `C74A1DA20F285742514657C746D597C6291B7B6E09F5AFE1CA6EB24FC0757AA8`.
- Verifica manifest: 8/8 file presenti, 8/8 hash corrispondenti, nessun file non censito.

## Stato remoto e modifiche dello staff

- Branch locale: `main`.
- Remote: `origin` su GitHub.
- `git fetch origin` eseguito il 14 agosto 2026; nessun push.
- Ultimo commit remoto osservato: `be864b6a` (`Merge pull request #3 from albertobrando1991/codex/vol08-kdp-kit`).
- Divergenza dopo il fetch: branch locale 139 commit indietro e 2 avanti rispetto a `origin/main`.
- Il working tree contiene un ampio insieme di modifiche dello staff su altri volumi, artefatti e memoria agentica; non sono state incluse nel pacchetto.
- L'area di staging conteneva già otto file dello staff, inclusi file con modifiche miste staged/unstaged. Per non alterare o combinare lavoro altrui, non è stato eseguito nuovo staging. La selezione della consegna è realizzata dal pacchetto isolato e verificata dal manifest 8/8.
- Non sono stati eseguiti commit, merge, rebase o push.

## Esclusioni intenzionali

- `.next`, cache, dipendenze, `__pycache__` e directory temporanee;
- log del server e helper temporanei della lavorazione;
- tavole-contatto, screenshot e testo estratto degli step 19, 20 e 22;
- artefatti di VOL-02 o di altri volumi;
- run-state condiviso e memoria locale dell'agente;
- modifiche staged o unstaged dello staff non contenute nella directory di consegna;
- copertina, dorso, ISBN, prezzo e metadati commerciali;
- qualunque file non elencato nel manifest.

## Gate tecnici finali

- Audit di copertura: 162/162 nuclei completi.
- Link e fonti: 90/90 link risolti; 57 `source_refs`, 16 unici, 0 mancanti.
- Audit pagina per pagina dopo l'ultima correzione visibile: 459/459 pagine, 23 tavole-contatto, 0 bloccanti, 0 significativi.
- PDF finale: MediaBox/CropBox/TrimBox/BleedBox 481,68 × 691,92 pt, font incorporati, no bleed.
- SHA-256 PDF: `F8ECF8499C19BF7727F4BB72314CAA84DF828C911DD16D0918DAA278079609F9`.
- Test completi: 59 file, 452 test passati.
- Typecheck: verde.
- Build di produzione: verde, 20/20 pagine statiche.
- `git diff --check` sul perimetro VOL-12: verde; le sole anomalie globali sono esterne e dichiarate nel preflight.
- Manifest del pacchetto: 8/8 hash verdi, 0 file extra.
- KDP Previewer: non eseguito, limite dichiarato nel pacchetto; nessun esito inventato.

## Decisione

Il candidato supera la preparazione di consegna. Lo step 24 resta aperto e deve confermare il pacchetto prima di qualunque pubblicazione. Un errore rilevato durante upload, Previewer o conferma finale riapre il gate pertinente.
