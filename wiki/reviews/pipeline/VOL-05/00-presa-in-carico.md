---
id: review-pipeline-vol-05-step-00
type: editorial_review
volume: VOL-05
step: 00
status: completed
review_required: false
updated_at: 2026-08-22
---

# VOL-05 — Presa in carico

## Target e perimetro

- volume: VOL-05 — *Authority e regolazione*;
- modulo: M-FC05 — `books/moduli/m-fc05-authority-indipendenti`;
- corpus: indice, piano, 15 capitoli, 75 coppie PNG/SVG, source note consolidate, report pregressi e output Book Studio;
- esclusi: `raw/`, VOL-06, file temporanei e contenuti di altre famiglie.

## Memoria locale richiamata

`LocalAgentMemory` ha restituito dieci elementi pertinenti. Sono stati applicati: preservazione del lavoro esistente; rinvii ammessi solo verso contenuti completi; ciclo Formato 2 → matrice → densità → Humanizer → revisione; continuità con la precedente scrittura professionale del capitolo 3. Le memorie non sono usate come fonti normative.

## Stato Git e collisioni

- branch: `codex/publish-volumes-01-03-05-10-11`;
- `origin/main` non contiene commit non acquisiti (`HEAD...origin/main`: 30/0);
- worktree condiviso e già modificato per altri volumi;
- nessun reset, checkout distruttivo o sovrascrittura globale;
- VOL-05 viene lavorato con patch e percorsi espliciti; lo staging preesistente resta intatto.

## Rischi accertati

- run-state prima assente, ora creato esclusivamente tramite CLI;
- matrice Formato 2 assente;
- apparato editoriale interno visibile nel corpo;
- lacune specialistiche e promessa di appendici/servizi non materializzati;
- struttura ripetitiva e capitoli sotto il contratto didattico;
- controllo normativo necessario su REMIT, SSM, DORA, MiCAR, ADR assicurativo e whistleblowing.

## Piano operativo

1. riconciliare catalogo, indice e fonti;
2. correggere le lacune specialistiche con fonti primarie;
3. trasformare i 15 capitoli in Formato 2 senza perdere la voce valida;
4. costruire matrice e report capitolo/modulo;
5. completare Humanizer, text freeze, immagini, impaginazione e PDF;
6. preparare il candidato, lasciando allo step 24 la sola conferma umana finale.

## Skill applicate

`pipeline-volume` → `revisore-editoriale-totale` → `concorso-book-professional-writer` → `humanizer` → `canvas-design` → `pdf` → verifica finale.
