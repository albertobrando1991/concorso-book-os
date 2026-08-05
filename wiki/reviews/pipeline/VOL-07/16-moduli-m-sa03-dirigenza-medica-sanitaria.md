---
id: review-vol-07-step-16-m-sa03-text-freeze
type: review
title: Manifest di text freeze - M-SA03 Dirigenza medica e sanitaria
status: complete
domain: concorsi pubblici italiani
source_refs:
  - sources/vol-07-dossier-fonti-materie-sanita-2026-07-28
book_refs:
  - m-sa03-dirigenza-medica-sanitaria
  - vol-07-sanita-amministrativa-professioni-sanitarie
confidence: 0.98
updated_at: 2026-08-04T12:30:00+02:00
created_at: 2026-08-04T12:30:00+02:00
review_required: false
canonical: false
tags:
  - pipeline-step-16
  - text-freeze
  - m-sa03
issue_type: text_freeze
severity: none
affected_pages:
  - books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md
  - books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters
---

# Manifest di text freeze - M-SA03 Dirigenza medica e sanitaria

## Esito

**Text freeze approvato il 4 agosto 2026.** Tutte le condizioni del contratto dello step 16 sono verificate. Il manifest registra il pacchetto congelato e costituisce l'evidenza richiesta dal gate `text-freeze`.

Riferimento Git di base: `5fbe444c18d466be0ab6e133cdfe1027f9ff5936`. Gli apparati aggiornati allo stato di freeze e tutti i file del pacchetto sono identificati dai SHA-256 riportati sotto; tali hash prevalgono sul solo commit di base per ricostruire il pacchetto congelato.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
| --- | --- | --- |
| Tutti i capitoli presenti | Sette target dichiarati e presenti: 01-07; indice e cartella `chapters/` coincidono | superata |
| Copertura integrale | Matrice: 9 righe, 9 `completo`; nessun `parziale`, `solo-nominato`, `rinviato` o `mancante` | superata |
| Rinvii precisi | 28 wikilink unici nel pacchetto, tutti risolti; nessun collegamento a source note, topic, entity, raw, planning o review nel corpo destinato al lettore | superata |
| Humanizer | Tutti i sette step 11 risultano `done`, con gate passato | superata |
| Errori gravi e medi | Step 13-14 `done`; step 15: A01-A08 corretti e nessuna voce aperta | superata |
| Audit specialistico | Step 15 `done`, gate passato, zero blocker e zero warning; audit giuridico-concorsuale, contrattuale, organizzativo, clinico non esecutivo, epidemiologico e professionale concluso | superata |
| Indice coerente | Sette link di capitolo, sette file presenti; perimetro limitato alla dirigenza medica e sanitaria non medica; stato aggiornato a `text_frozen` | superata |
| Fonti e cut-off | 60 `source_refs` nei sette capitoli, 36 unici e zero destinazioni mancanti; cut-off `2026-07-28` dichiarato nella scheda, nel dossier e nella source note VOL-07; i capitoli con dati mobili dichiarano inoltre il limite temporale applicabile | superata |

## Correzioni controllate prima del freeze

- Indice e piano editoriale sono stati aggiornati a `status: text_frozen` e `draft_stage: text-frozen`.
- Bibbia del Modulo e matrice sono state allineate allo stato effettivo successivo agli step 13-15.
- Le correzioni riguardano esclusivamente stato e regola post-freeze; non modificano teoria, casi, esercizi, fonti o perimetro specialistico.

## File congelati

| File | Stato al 2026-08-04 | SHA-256 |
| --- | --- | --- |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md` | text-frozen | `e532d20362cb0e391094f98883b1165834b4c49587bd10f457a91db2c70baceb` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/00-piano-editoriale.md` | text-frozen | `fd82267ceeeb5de93f42c7c75c7351dd70e74f1b0605d514efae707f612e2a27` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/02-matrice-copertura-didattica.md` | complete | `5f902849231360ac3500ce62d78242cb616b943e88c54e4fcb21601742129f93` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/09-bibbia-del-modulo.md` | review-ready, text-frozen | `7d6accaa668c9e365afa23fdbf162564214158e48ffc65654956a2c03e5a5a74` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/01-profili-requisiti-prove-dirigenza-sanitaria.md` | frozen | `9f7b6e296806a0b855277c512c596a8039ea93ccda23a9b6e6e2efe85f5db615` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/02-programmazione-sanitaria-organizzazione-servizi.md` | frozen | `73f1a2384ab18941f84856461298d6b619209ed725d0e8d8cf484ad16ec7afc4` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/03-linee-guida-appropriatezza-decisioni-cliniche.md` | frozen | `341725b981036070c976f23811a84d00f0d211ee0281dfc8b7792bed434621e0` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/04-governo-clinico-hta-qualita-accreditamento-rischio.md` | frozen | `448dc90f2cec977539af61662f4425e47dfea3398e09d30c32af085c66ccec12` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/05-epidemiologia-sanita-pubblica-dirigenza.md` | frozen | `59481597cbd2c90eaa1fb8ca1354fb2fe8b620e74c3d1043788802dbaf903ff6` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/06-dirigenza-medica-discipline-casi.md` | frozen | `c3a77a451d9cc6009c133bde11a1d737ff255193b94e1486f38996233a33eba6` |
| `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/07-dirigenza-sanitaria-non-medica-discipline-casi.md` | frozen | `1ed29804bbaabc0f3cd5e0b8a5a75c27366664b57d1509786d68cb23a3e14fef` |
| `wiki/reviews/pipeline/VOL-07/13-moduli-m-sa03-dirigenza-medica-sanitaria.md` | evidenza chiusa | `e43e6db72de1b7085db4eab9256c0dbf17365aee33e9e807bad9946353569424` |
| `wiki/reviews/pipeline/VOL-07/14-moduli-m-sa03-dirigenza-medica-sanitaria.md` | evidenza chiusa | `f361ba0e66a7ee7f90df8864e4ab8a84ce62dfd0124420660ac571bfaf20be68` |
| `wiki/reviews/pipeline/VOL-07/15-moduli-m-sa03-dirigenza-medica-sanitaria.md` | evidenza chiusa | `414fcb7483e9d11f3bc6e2dc1024d1ad80893052e720792dfa52e128d761424d` |

## Regola successiva al freeze

Da questo manifest in avanti sono ammesse soltanto correzioni controllate e tracciate. Ogni modifica sostanziale a teoria, fonti, casi, dati operativi, quiz, struttura o perimetro riapre i gate 10-15 prima di un nuovo text freeze.
