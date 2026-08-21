---
id: review-pipeline-vol-11-step-23
type: editorial_review
volume: VOL-11
step: 23
status: passed
review_required: false
updated_at: 2026-08-20
---

# VOL-11 — Step 23: pacchetto candidato e consegna tecnica

## Esito

**PASS TECNICO.** Il pacchetto è predisposto per la sola revisione e approvazione umana dello step 24. Non costituisce approvazione alla pubblicazione né autorizza il caricamento su KDP.

## Identificazione riproducibile

| Voce | Valore |
|---|---|
| Candidato | `VOL-11-candidate-2026.08.20.1` |
| Cut-off editoriale | 18 agosto 2026 |
| Ramo | `agent/sync-volumi-04-05-06-09-20260817` |
| Base commit | `1014415c4a681c8eea0663319c8fb68e3ac4e5a7` |
| Stato remoto al controllo | sincronizzato (`ahead 0`, `behind 0`) |
| Interno consegnato | `delivery/VOL-11/candidate/vol-11-interior-kdp.pdf` |
| SHA-256 dell'interno | `0864ac2267d76713b02f21a64be21685c45121e8dd6b2f490f1ba65faa0dafca` |
| Struttura verificata | 223 pagine, 14 capitoli, 90 nuclei |

## Contenuto del pacchetto

La directory `delivery/VOL-11/candidate/` contiene l'interno PDF, identificazione di versione, preflight, rapporto di pubblicabilità, changelog, limiti noti, manutenzione, checklist KDP e `MANIFEST.sha256`. Il manifest elenca le impronte SHA-256 di ogni file consegnato, escluso il manifest stesso.

## Verifiche finali previste nello step

- ripetizione dei gate tecnici e dei test di regressione rilevanti;
- controllo dell'integrità del PDF consegnato rispetto al PDF preflight;
- staging limitato a Volume 11, correzione di anteprima collegata e file di consegna;
- esclusione esplicita di cache, log, file temporanei, artefatti diagnostici e lavoro parallelo su VOL-04.

Le eventuali modifiche già in staging per VOL-04 sono preesistenti e restano fuori dall'ambito del candidato VOL-11; il controllo dello staging VOL-11 è quindi eseguito su un set di percorsi esplicito.

## Condizioni residue

Restano obbligatori, nello step 24, la lettura umana dell'interno, la conferma dei metadati e della copertina, l'anteprima KDP e la prova di stampa. I limiti e le azioni di manutenzione sono riportati nei rispettivi file del pacchetto.

## Risultati registrati il 20 agosto 2026

- Gate `delivery` interrogato tramite CLI: `gate-not-implemented`; chiusura ammessa esclusivamente con verifica manuale e nota esplicita.
- Gate automatici precedenti confermati nel preflight dello step 22; l'interno candidato conserva l'hash SHA-256 atteso.
- Suite di anteprima: **3 file, 18 test superati** (`book-preview`, regressione nuclei indice, segmentazione paragrafi).
- `npm run typecheck`: superato.
- `npm run build`: superato (Next.js 15.5.22).
- `git diff --cached --check`: superato dopo la normalizzazione delle due righe vuote finali segnalate.
- Il ramo era sincronizzato con `origin` al controllo (`ahead 0`, `behind 0`).