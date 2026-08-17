# Task 1 — Rendere vincolante la governance didattica

Leggi prima:

- `docs/superpowers/specs/2026-07-17-copertura-didattica-integrale-design.md`
- `docs/superpowers/plans/2026-07-17-copertura-didattica-integrale.md`, Task 1
- `wiki/AGENTS.md`
- `.agents/skills/concorso-book-professional-writer/SKILL.md`
- `.agents/skills/revisore-editoriale-totale/SKILL.md`
- `.agents/skills/revisore-editoriale-totale/references/checklist-30-punti.md`
- `wiki/books/moduli/architettura-moduli-specialistici.md`
- `wiki/sources/logica-volumi-copertura-concorsobook-v4.md`

## Deliverable

Creare:

- `wiki/sources/principio-copertura-didattica-integrale-2026-07-17.md`
- `wiki/topics/copertura-didattica-integrale.md`

Modificare esclusivamente:

- `wiki/AGENTS.md`
- `.agents/skills/concorso-book-professional-writer/SKILL.md`
- `.agents/skills/revisore-editoriale-totale/SKILL.md`
- `.agents/skills/revisore-editoriale-totale/references/checklist-30-punti.md`
- `wiki/books/moduli/architettura-moduli-specialistici.md`

## Requisiti vincolanti

- Metodo BANDO organizza la teoria richiesta e la trasforma in performance concorsuale, ma non la sostituisce.
- Ogni concetto promesso deve essere spiegato oppure rinviato con destinazione precisa e verificata.
- Unità minima: definizione, funzione, inquadramento teorico/normativo, elementi, distinzioni, conseguenze, esempio/caso, modalità d'esame, errore tipico, verifica, fonti.
- Stati: `completo`, `parziale`, `solo-nominato`, `rinviato`, `mancante`.
- `solo-nominato` e `mancante` sono bloccanti; `parziale` non è pubblicabile; `rinviato` è valido solo con destinazione precisa, completa e aggiornata.
- La promessa formativa non mantenuta è errore grave.
- Non duplicazione e completezza devono convivere: rinviare solo se la destinazione insegna davvero il concetto.
- Raw non è fonte finale: raw -> source note -> topic/entity -> capitolo.
- Non modificare o includere nel commit file estranei, anche se già sporchi.

## Verifica

Eseguire:

```powershell
rg -n "copertura didattica integrale|solo-nominato|promessa formativa|non la sostituisce" wiki/AGENTS.md .agents/skills wiki/books/moduli/architettura-moduli-specialistici.md wiki/sources wiki/topics
git diff --check -- wiki/AGENTS.md .agents/skills/concorso-book-professional-writer/SKILL.md .agents/skills/revisore-editoriale-totale/SKILL.md .agents/skills/revisore-editoriale-totale/references/checklist-30-punti.md wiki/books/moduli/architettura-moduli-specialistici.md wiki/sources/principio-copertura-didattica-integrale-2026-07-17.md wiki/topics/copertura-didattica-integrale.md
npm test
```

Committare soltanto i file elencati con messaggio `docs: enforce integral didactic coverage`.

## Report

Scrivere `.superpowers/sdd/task-1-report.md` con file modificati, decisioni, verifiche, commit e preoccupazioni. Restituire uno stato tra `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, `BLOCKED`.
