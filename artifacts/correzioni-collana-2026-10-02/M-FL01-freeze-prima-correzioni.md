---
id: m-fl01-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-FL01 Comuni e Unioni"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-fl01-comuni-unioni
module_code: M-FL01
freeze_date: 2026-08-05
reference_commit: f7e5ad8275aaab37d8d9a8cea7e3016b4eea00d2
updated_at: 2026-08-05T00:00:00+02:00
created_at: 2026-08-05T00:00:00+02:00
review_required: false
canonical: true
tags: ["text-freeze", "m-fl01", "pipeline-step-16"]
---

# Text freeze — M-FL01 Comuni e Unioni

## Esito

Il modulo entra in congelamento testuale il 5 agosto 2026. I capitoli 01-14 sono presenti; la matrice non contiene stati `parziale`, `solo-nominato` o `mancante`; gli errori obbligatori degli step 13-14 sono chiusi; l'audit specialistico dello step 15 è completato senza esiti aperti; indice e fonti sono coerenti.

Da questo manifest sono ammesse soltanto correzioni controllate. Una modifica sostanziale a teoria, casi, quiz, riferimenti o struttura riapre i gate 10-15.

## Riferimento di versione

- Commit precedente al pacchetto di freeze: `f7e5ad8275aaab37d8d9a8cea7e3016b4eea00d2`.
- Stato editoriale da congelare: modifiche correnti degli step 13-16, da includere nel successivo commit di pipeline.
- Algoritmo hash: SHA-256 sul contenuto UTF-8 dei file capitolo.
- Cut-off normativo dell'audit: 5 agosto 2026; testi vigenti e source notes consolidate disponibili a tale data.

## Manifest dei capitoli

| File | Stato | SHA-256 |
| --- | --- | --- |
| `01-tuel-operativo-autonomia-organi-funzioni-comune.md` | frozen | `eedd4afccaff88d61b8d7ca7799893178688626606dd1a28b6082364c1d4cf8b` |
| `02-statuto-regolamenti-autonomia-normativa-locale.md` | frozen | `021fcce551bcba27457eef7fd574c310720aae61fc22c7e2ae3b6e2b696b378b` |
| `03-organizzazione-comunale-uffici-servizi-gestioni-associate.md` | frozen | `9b277cf3bbc3d68942393840b34ac0df218cb02cff67c403fbd3fdbfe7411f03` |
| `04-deliberazioni-determinazioni-decreti-ordinanze-pareri.md` | frozen | `b539f916e4bcc2e018b91d45eca049ad3488fce2a2d2c58896d6f1998bae14fa` |
| `05-procedimento-locale-protocollo-albo-urp-accesso.md` | frozen | `c8c939eec8463a72bb2e1f8a165377492b0a93247a3acc6bdd82e99dffa2d1fc` |
| `06-servizi-digitali-comunali-cad-anpr-gestione-documentale.md` | frozen | `80408d6d170d81da8fec90b679a0f291d0676c63ff4dd26e52616f4e67d89f14` |
| `07-servizi-demografici-elettorali.md` | frozen | `925a662f81f6959986834a5b2115235caeee3c6a04b6b4ce096f624af0edd8fb` |
| `08-welfare-locale-servizi-sociali-isee-minori-servizi-educativi.md` | frozen | `c616388d1444f419ef3fddcd232b54183f00e7be95849491afcd7276d5baad81` |
| `09-programmazione-integrata-comunale-dup-bilancio-peg-piao-performance.md` | frozen | `79d573bc6b43fe763ff7d366ba55e4ae04a8fa8314dbeb3a3e5f9bdc53945f20` |
| `10-gestione-finanziaria-rendiconto-tesoreria-controlli.md` | frozen | `f039568d3875d1edeb4c1bf1d35e61b73560791bfdf569fa3690624649c7acac` |
| `11-entrate-tributi-locali-patrimonio-economato-riscossione.md` | frozen | `3de74ac2ab561cb0db876bfaf9804bdc4ae8ae87862e6ccf9f7bc2a485c7c2dc` |
| `12-procurement-operativo-ufficio-comunale.md` | frozen | `d482586b728f957570ff5ba58103ef30f218b2dc2df174285416a312d222be93` |
| `13-territorio-patrimonio-edilizia-lavori-interfaccia-amministrativa.md` | frozen | `98c82446fc0f1ade2ee255b3a3f957b93525627da49f2845f7019bc007fa49a9` |
| `14-laboratorio-teorico-pratico-profili-comunali.md` | frozen | `4fbd2d98e05051e35f28bf1d59959e8a55a7642d937d3fb9aa8eb2ebd9c3f966` |

## Evidenze di gate

- Step 13: revisione trasversale superata senza blocker.
- Step 14: E01-E04 chiusi e report di correzione superato.
- Step 15: audit specialistico A01-A05 chiuso senza errori aperti.
- Nessun box `Dato operativo` nel modulo.
- Tutti i rinvii e gli apparati restano soggetti al preflight tecnico successivo.
