---
id: review-vol-10-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-10"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/book-layout-typography-standards"
  - "reviews/pipeline/VOL-10/21-vol-10"
  - "reviews/pipeline/VOL-10/20-audit-pagina-per-pagina"
book_refs: ["vol-10-tecnico-ingegneristico-territorio-lavori-pubblici"]
confidence: 1
updated_at: 2026-08-12
created_at: 2026-08-12
review_required: false
canonical: true
tags: ["vol-10", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale — VOL-10

## Esito

Il preflight locale è superato. Il candidato PDF contiene 196 pagine, usa il trim KDP esatto 6,69 × 9,61 pollici senza bleed, incorpora tutte le risorse font e corrisponde al corpus verificato pagina per pagina. Non risultano errori bloccanti o significativi aperti.

Il KDP Previewer esterno non è installato e non è stato simulato: eventuali messaggi prodotti dal servizio di upload dovranno essere registrati nel passaggio di pubblicazione. Questo limite non viene dichiarato verde e non sostituisce un esito inesistente.

## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | PASS | `parseCoverageMatrix` + `auditCoverageRows` sulla matrice canonica M-TR03: 94 righe accettate, 93 complete e una con rinvio preciso; 0 blocker, 0 warning. La vista aggregata di volume attesta 78/78 nuclei completi. |
| Link wiki | PASS | Scansione dei 13 corpi capitolo: 0 dipendenze wiki esposte al lettore e 0 target mancanti. |
| `source_refs` | PASS | `parseFrontmatter` sui 13 capitoli: 82 riferimenti dichiarati, 0 target mancanti. |
| Frontmatter | PASS | 13/13 capitoli con i campi editoriali obbligatori, `format_version: 2`, `review_required: false` e stadio specialistico consolidato. |
| Asset path | PASS | 0 riferimenti immagine Markdown o HTML nei capitoli; Book Studio carica il volume senza `.missingAsset`. |
| File mancanti | PASS | Presenti indice volume, indice modulo, 13 capitoli, matrici e report obbligatori fino allo step 21. |
| Immagini duplicate | PASS | Nessuna immagine editoriale referenziata; controllo non applicabile agli elementi tipografici generati dal layout. |
| Tabelle anomale | PASS | 478 righe Markdown di tabella nel corpus; verifica Book Studio step 22: 196 pagine, 0 overflow, 0 collisioni. L'audit step 18 aveva già validato 161 blocchi e i 23 blocchi a quattro colonne. |
| Caratteri corrotti | PASS | Scansione UTF-8 dei 13 capitoli sui marker `�`, `Ãƒ`, `Ã‚`, `Ã¢â‚¬`, `ï¿½`: 0 occorrenze. |
| `git diff --check` | PASS | Eseguito sull'intero worktree: nessun errore di whitespace. |
| Test pertinenti | PASS | Suite mirata post-correzione: 4 file e 58 test passati; include export PDF, layout, page audit e copertura. Suite completa finale: 48 file e 437 test passati. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0 dopo aggiornamento della dichiarazione `.d.mts`. |
| Build | PASS | `npm run build`: Next.js 15.5.18 compilato e 20/20 pagine statiche generate. Cache `.next` rigenerata dopo aver isolato un vecchio dev server concorrente. |
| Export PDF | PASS | `npm run export:volume-pdf` con `BOOK_STUDIO_BOOK_ID=volumi/vol-10` e conteggio atteso 196; output `delivery/VOL-10/candidate/vol-10-interior-kdp.pdf`, 1.293.214 byte. |
| Normalizzazione trim | PASS | Il contratto normalizza in-place i 196 MediaBox generati da Chromium da 481,91998 pt a 481,68000 pt e l'altezza a 691,92000 pt, preservando lunghezza e offset del PDF. Test red/green dedicato presente. |
| Font incorporati | PASS | Ispezione delle risorse PDF: Arial Bold, Garamond, Arial Black e Arial sono subset Type0 con `FontFile2`; Cambria Math è una risorsa Type3 con `CharProcs` incorporati. Nessuna risorsa font esterna richiesta. |
| Dimensione pagina | PASS | 196/196 pagine con MediaBox 481,68 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici; CropBox assente e quindi coincidente per default con MediaBox. |
| Bleed | PASS | Nessun bleed previsto; nessun elemento al vivo e area visibile coincidente con MediaBox. |
| Margini | PASS | CSS canonico verificato: interno 23 mm, esterno 13 mm, superiore e inferiore 18 mm; margini speculari recto/verso e profilo no-bleed. |
| Conteggio pagine | PASS | 196 pagine nel DOM stabile, 196 pagine nel PDF, numerazione progressiva 1-196. |
| Audit pagina per pagina | PASS | Report step 20: 196/196 pagine e 10/10 tavole-contatto, 0 bloccanti e 0 significativi. Verifica DOM step 22: `Book Studio layout OK for vol-10`. |
| Hash del candidato | PASS | SHA-256 `FC5546DD591222D96DEED9666476219C7A30BFB171792B26F68F88EB535031C0`; dimensione 1.293.214 byte. |
| KDP Previewer | NON ESEGUITO | Applicazione locale non disponibile (`KDP_PREVIEWER_NOT_INSTALLED`); nessun warning osservato o inventato. Controllo da ripetere nel servizio KDP al momento dell'upload. |

## Note operative

- Il primo avvio sulla porta 3010 ha intercettato un vecchio `next dev`; il server di produzione è stato isolato sulla porta 3012.
- Il processo concorrente aveva contaminato la cache `.next`. Sono stati arrestati esclusivamente i processi Next del worktree, la cache derivata è stata rigenerata e la build è stata ripetuta con esito verde.
- Chromium quantizza la larghezza 6,69″ a 481,91998 pt. L'export applica ora una normalizzazione deterministica dei box, senza rimuovere contenuto e senza modificare gli offset del PDF.
- Gli artefatti diagnostici in `artifacts/` non fanno parte del candidato di consegna.

## Candidato verificato

- File: `delivery/VOL-10/candidate/vol-10-interior-kdp.pdf`
- Pagine: 196
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- Colore: bianco e nero
- SHA-256: `FC5546DD591222D96DEED9666476219C7A30BFB171792B26F68F88EB535031C0`
- Stato: pronto per la preparazione selettiva del pacchetto di consegna dello step 23; non approvato e non pubblicato.
