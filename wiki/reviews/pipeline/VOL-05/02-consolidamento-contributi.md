---
id: review-pipeline-vol-05-step-02
type: editorial_review
volume: VOL-05
step: 02
status: completed
review_required: false
updated_at: 2026-08-22
---

# VOL-05 — Consolidamento dei contributi

| File | Origine del contributo | Integrazione applicata | Contenuto preservato | Conflitti rimasti |
| --- | --- | --- | --- | --- |
| `vol-05-authority-regolazione/index.md` | indice storico staff + audit 18 agosto | eliminata la promessa di servizi/appendici assenti; aggiunta conclusione reale al percorso | titolo, pubblico, premessa, sequenza dei 15 capitoli | nessuno |
| `m-fc05-authority-indipendenti/index.md` | indice modulo staff | stato reso veritiero; precedente via libera qualificato come storico | perimetro, collegamenti, fonti, bando di riferimento | nessuno |
| `planning/00-piano-editoriale.md` | piano staff | rimosso il segnaposto “Da sviluppare”; registrato il corpus esistente e il ciclo di ricertificazione | struttura, lettore, sommario, fonti e collegamenti | nessuno |
| `planning/00-scheda-pipeline.md` | catalogo + corpus esistente | dichiarati i 15 target canonici e i confini editoriali | ordine e titoli pubblici già approvati | nessuno |

## Regole applicate

- nessun capitolo o asset duplicato;
- nessuna versione storica cancellata;
- nessun contenuto di `raw/` usato come testo finale;
- nessuna scelta arbitraria tra versioni concorrenti, perché non ne sono state rilevate;
- piani e report restano fuori da `chapters/`;
- la correzione dei contenuti avviene negli step dedicati e non viene anticipata in questo consolidamento.

## Controllo

`git diff --check` viene eseguito sul worktree condiviso. Eventuali avvisi CRLF/LF relativi a manifest di altri volumi sono informativi; non risultano errori di whitespace introdotti nel perimetro VOL-05.
