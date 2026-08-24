---
id: review-pipeline-vol-10-step-23
type: editorial_delivery
volume: VOL-10
step: 23
status: passed
review_required: false
updated_at: 2026-08-21
---

# VOL-10 — Step 23: pacchetto candidato

## Esito

**PASS.** Preparato `delivery/VOL-10/candidate` come candidato tecnico `VOL-10-candidate-2026.08.21.1`, non approvato e non pubblicato. Lo step 24 resta obbligatoriamente riservato alla conferma umana.

## Stato remoto e tutela del lavoro staff

- `origin/main` osservato dopo `git fetch origin --prune`: `c5f3ac01cc896b22563216eede96367235cd8fbe`;
- branch locale: `codex/publish-volumes-01-03-05-10-11`, HEAD `fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a`;
- nessuna differenza remota nel perimetro editoriale M-TR03/VOL-10;
- due file condivisi (`src/server/book/book-preview.ts` e `tests/book-preview.test.ts`) risultano modificati anche su `origin/main`, ma in hunk distinti: il pacchetto locale non elimina né sostituisce le modifiche dello staff;
- VOL-06, cache, log, output intermedi e tavole di contatto sono esclusi dallo staging selettivo.

## Contenuto e integrità

| Voce | Esito |
| --- | --- |
| Versione editoriale | `1.0.0-candidate` |
| Cut-off normativo/editoriale | 21 agosto 2026 |
| PDF interno | `vol-10-interior-kdp.pdf`, 100 pagine, 670.852 byte |
| SHA-256 PDF | `03f3445d0a6f5ba821bc7d304a68839d0c9aa48ae00e4b8d12e0c25dde703117` |
| File nel pacchetto | 10 |
| Voci nel manifest | 9, escluso il manifest stesso |
| Errori di integrità | 0 |
| Report di pubblicabilità | presente |
| Preflight | presente |
| Changelog | presente |
| Limiti dichiarati | presenti |
| Manutenzione futura | presente |
| Checklist KDP | presente |

## Controlli finali ripetuti

- gate specialistico step 15: PASS, zero blocker e zero warning;
- sei suite pertinenti: 52/52 test superati;
- `npm run typecheck`: PASS;
- `git diff --cached --check`: PASS;
- controllo dei path staged: nessun file VOL-06, cache, log, `output/pdf` o artifact temporaneo;
- manifest SHA-256: nove verifiche, zero mismatch.

## Limiti e manutenzione

Il pacchetto dichiara esplicitamente l’assenza di copertina commerciale, ISBN e metadati di canale, nonché la mancata esecuzione di KDP Previewer. Gli aggiornamenti successivi al cut-off seguono il ciclo fonte → mappatura impatti → revisione mirata → gate → text freeze → preflight → nuova candidata.

## Decisione

Il gate `delivery`, se non implementato nel CLI, può essere chiuso con accettazione manuale motivata sulla base delle evidenze sopra. Il risultato è un candidato integro e consegnabile allo staff per lo step 24, non un volume già approvato o pubblicato.
