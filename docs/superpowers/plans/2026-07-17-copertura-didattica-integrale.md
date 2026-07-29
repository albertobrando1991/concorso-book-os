# Integral Didactic Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rendere globale, verificabile e retroattiva la copertura didattica integrale di tutti i volumi e moduli ConcorsoBook OS, quindi pubblicare il lavoro organizzato su GitHub.

**Architecture:** La governance definisce il contratto editoriale; template e matrici rendono misurabile la copertura; un inventario globale censisce 12 volumi e 25 moduli; audit semantici per volume identificano gap; integrazioni teoriche e review normative chiudono i gap prima del gate editoriale. L'esecuzione è progressiva: nessun censimento viene presentato come completamento editoriale.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian wikilinks, PowerShell, TypeScript/Vitest, Git e GitHub.

## Global Constraints

- Il Metodo BANDO organizza e rende operativa la teoria, ma non la sostituisce.
- Ogni materia assegnata a un volume o modulo deve essere realmente insegnata con profondità proporzionata a profilo, frequenza e peso nei bandi.
- Le fonti raw non alimentano direttamente il testo finale: raw -> source note -> topic/entity -> capitolo.
- Gli stati `solo-nominato` e `mancante` sono bloccanti; `parziale` richiede integrazione; `rinviato` richiede destinazione precisa e completa.
- Nessuna modifica preesistente dell'utente deve essere eliminata o sovrascritta.
- I commit devono essere separati per governance, strumenti, inventari, audit, integrazioni e pubblicazione.
- Il repository locale include già integralmente `origin/main` ed è avanti rispetto al remoto.

---

### Task 1: Rendere vincolante la governance didattica

**Files:**
- Create: `wiki/sources/principio-copertura-didattica-integrale-2026-07-17.md`
- Create: `wiki/topics/copertura-didattica-integrale.md`
- Modify: `wiki/AGENTS.md`
- Modify: `.agents/skills/concorso-book-professional-writer/SKILL.md`
- Modify: `.agents/skills/revisore-editoriale-totale/SKILL.md`
- Modify: `.agents/skills/revisore-editoriale-totale/references/checklist-30-punti.md`
- Modify: `wiki/books/moduli/architettura-moduli-specialistici.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-07-17-copertura-didattica-integrale-design.md` e `[[sources/logica-volumi-copertura-concorsobook-v4]]`.
- Produces: regola globale richiamabile da agenti, writer, revisore e architettura.

- [ ] **Step 1: Creare la source note canonica della decisione**

Usare frontmatter `type: source`, `status: canonical`, `authority_level: progetto-editoriale`, `confidence: 1.0`, `review_required: false` e sezioni: Decisione, Unità minima, Matrice, Rinvii, Gate, Impatti.

- [ ] **Step 2: Creare il topic cumulativo**

Collegare la nuova source note, la logica v4, architettura moduli, writer e revisore. Il topic deve distinguere copertura di catalogo, copertura teorica e copertura operativa.

- [ ] **Step 3: Aggiornare `wiki/AGENTS.md`**

Inserire tra le regole non negoziabili:

```text
Metodo BANDO organizza la teoria richiesta e la trasforma in performance concorsuale, ma non la sostituisce. Ogni concetto promesso deve essere spiegato oppure rinviato con destinazione precisa e verificata.
```

Aggiungere matrice, stati bloccanti e gate sia al Manual Writer Agent sia al Revisore Editoriale Totale.

- [ ] **Step 4: Aggiornare la skill del writer**

Aggiungere una sezione `## Integral Didactic Coverage Gate` con unità minima: definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio, modalità d'esame, errore, verifica e fonti.

- [ ] **Step 5: Aggiornare revisore e checklist**

Rendere grave e bloccante la promessa formativa non mantenuta; aggiungere controllo su concetti nominati, rinvii, autonomia didattica e corrispondenza matrice/capitolo.

- [ ] **Step 6: Aggiornare l'architettura moduli**

Integrare la regola v4: non duplicazione e copertura integrale devono operare insieme; il rinvio sostituisce la duplicazione solo quando conduce a contenuto completo.

- [ ] **Step 7: Verificare e committare la governance**

Run:

```powershell
rg -n "copertura didattica integrale|solo-nominato|promessa formativa|Metodo BANDO.*non.*sostituisce" wiki/AGENTS.md .agents/skills wiki/books/moduli/architettura-moduli-specialistici.md wiki/sources wiki/topics
git diff --check
npm test
```

Expected: regola presente in tutti i punti, nessun errore whitespace, 32 o più test superati.

Commit:

```powershell
git add -- wiki/AGENTS.md .agents/skills/concorso-book-professional-writer/SKILL.md .agents/skills/revisore-editoriale-totale/SKILL.md .agents/skills/revisore-editoriale-totale/references/checklist-30-punti.md wiki/books/moduli/architettura-moduli-specialistici.md wiki/sources/principio-copertura-didattica-integrale-2026-07-17.md wiki/topics/copertura-didattica-integrale.md
git commit -m "docs: enforce integral didactic coverage"
```

### Task 2: Creare template e validatore della matrice

**Files:**
- Create: `wiki/templates/didactic-coverage-matrix-template.md`
- Create: `src/server/editorial/didactic-coverage.ts`
- Create: `scripts/audit-didactic-coverage.mjs`
- Create: `tests/didactic-coverage.test.ts`
- Modify: `package.json`

**Interfaces:**
- Produces: `parseCoverageMatrix(markdown: string)`, `auditCoverageRows(rows)`, CLI `npm run audit:coverage`.
- Status validi: `completo | parziale | solo-nominato | rinviato | mancante`.

- [ ] **Step 1: Scrivere test fallenti**

Testare: riga completa accettata; `solo-nominato` bloccante; rinvio senza destinazione bloccante; concetto senza fonte segnalato; stato non valido rifiutato.

- [ ] **Step 2: Eseguire i test e verificare il fallimento**

Run: `npx vitest run tests/didactic-coverage.test.ts`

Expected: FAIL perché il modulo non esiste.

- [ ] **Step 3: Implementare parser e audit**

La funzione di audit deve restituire `{ blockers, warnings, complete }` senza modificare file.

- [ ] **Step 4: Creare template e CLI**

Il template deve contenere tutte le colonne della specifica. La CLI deve scansionare file `*-matrice-copertura-didattica.md`, stampare riepilogo e terminare con codice 1 in presenza di blocker.

- [ ] **Step 5: Aggiungere script npm**

```json
"audit:coverage": "node scripts/audit-didactic-coverage.mjs"
```

- [ ] **Step 6: Verificare e committare**

Run:

```powershell
npx vitest run tests/didactic-coverage.test.ts
npm test
npm run audit:coverage
```

Expected: test verdi; audit eseguibile; eventuali blocker editoriali riportati come dati, non come crash.

### Task 3: Generare inventario globale di volumi e moduli

**Files:**
- Create: `wiki/reviews/audit-copertura-didattica-inventario-globale-2026-07-17.md`
- Create: `wiki/dashboards/copertura-didattica-globale.md`

**Interfaces:**
- Consumes: cartelle `wiki/books/volumi/`, `wiki/books/moduli/`, indici canonici e frontmatter.
- Produces: censimento di 12 volumi, 25 moduli, capitoli, stati, parole, fonti e matrici disponibili.

- [ ] **Step 1: Censire gli artefatti**

Registrare per ogni volume/modulo: id, famiglia, volume commerciale, index, capitoli, stati, placeholder, source refs e presenza matrice.

- [ ] **Step 2: Separare assenza editoriale e assenza filesystem**

Un modulo scaffold esistente non è “coperto”; un volume commerciale aggregatore senza capitoli propri non è “mancante” se rinvia correttamente ai moduli.

- [ ] **Step 3: Produrre dashboard e report**

La dashboard deve mostrare totali e stati; il report deve elencare blocker e priorità senza dichiarare completato l'audit semantico.

- [ ] **Step 4: Verificare catalogo**

Run:

```powershell
rg -n "VOL-01|VOL-12|M-FC01|M-SP04" wiki/reviews/audit-copertura-didattica-inventario-globale-2026-07-17.md
```

Expected: estremi e catalogo canonico rappresentati.

### Task 4: Eseguire audit pilota M-FC02 e VOL-03

**Files:**
- Create: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- Create: `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/02-matrice-copertura-didattica.md`
- Create: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
- Create: `wiki/reviews/review-vol-03-copertura-didattica-integrale-2026-07-17.md`

**Interfaces:**
- Consumes: bandi consolidati, indice, capitoli, source/topic/entity pages.
- Produces: classificazione semantica e backlog di integrazione prioritario.

- [ ] **Step 1: Estrarre promesse formative e materie**

Cercare formulazioni `deve sapere`, `deve riconoscere`, `occorre conoscere`, obiettivi, nuclei, checklist e indice.

- [ ] **Step 2: Verificare ogni promessa nel testo**

Classificare `completo`, `parziale`, `solo-nominato`, `rinviato`, `mancante` sulla base di spiegazione, esempio, output e verifica realmente presenti.

- [ ] **Step 3: Verificare le fonti**

Ogni riga deve collegare source note consolidate. La sola presenza in raw non rende il concetto scrivibile.

- [ ] **Step 4: Produrre report con priorità**

Ordinare: lacune gravi su materie pesate; capitoli source-ready; concetti solo nominati; rinvii incompleti; miglioramenti di esempi e verifiche.

- [ ] **Step 5: Eseguire il validatore**

Run: `npm run audit:coverage`

Expected: blocker rilevati e descritti finché l'integrazione non li chiude.

### Task 5: Integrare M-FC02 e VOL-03

**Files:**
- Modify: capitoli indicati come bloccanti dai due report.
- Create/Modify: source, topic ed entity pages richieste dai gap.

**Interfaces:**
- Consumes: backlog Task 4 e fonti ufficiali già scaricate.
- Produces: spiegazioni teoriche complete, casi, output concorsuali e matrici aggiornate.

- [ ] **Step 1: Chiudere prima i capitoli non scritti**

Trasformare `source_ready` e placeholder in capitoli effettivi solo dopo consolidamento delle fonti.

- [ ] **Step 2: Integrare i concetti solo nominati**

Per ogni nucleo aggiungere definizione, funzione, inquadramento, distinzioni, conseguenze, esempio, modalità d'esame, errore e verifica.

- [ ] **Step 3: Correggere i rinvii**

Sostituire rinvii generici con wikilink a capitolo/paragrafo completo; se la destinazione non esiste, scrivere il contenuto nel punto responsabile.

- [ ] **Step 4: Eseguire review normativa**

Consolidare fonti ufficiali vive per norme mobili, aggiornare note e mantenere `review_required: true` finché il controllo umano non è concluso.

- [ ] **Step 5: Aggiornare matrici e rieseguire gate**

Run: `npm run audit:coverage`

Expected: nessun `solo-nominato` o `mancante` per M-FC02/VOL-03; eventuali `parziale` mantengono stato non pubblicabile.

### Task 6: Estendere audit e integrazione agli altri volumi

**Files:**
- Create: una matrice e un report per ogni volume/modulo canonico.
- Modify: capitoli e knowledge base secondo i backlog approvati.

**Interfaces:**
- Consumes: metodo validato su M-FC02/VOL-03.
- Produces: catalogo completo classificato e progressivamente integrato.

- [ ] **Step 1: Audit VOL-01 e ricettario**
- [ ] **Step 2: Audit VOL-02 e moduli M-FL01/M-FL04, poi M-FL02/M-FL03**
- [ ] **Step 3: Completare VOL-03 con M-FC01/M-FC03**
- [ ] **Step 4: Audit VOL-04/VOL-05**
- [ ] **Step 5: Audit VOL-06 e M-IR01/M-IR04**
- [ ] **Step 6: Audit VOL-07 e M-SA01/M-SA04**
- [ ] **Step 7: Audit VOL-08/VOL-11 e moduli M-TR01/M-TR04**
- [ ] **Step 8: Audit VOL-12 e moduli M-SP01/M-SP04**
- [ ] **Step 9: Integrare per priorità e rieseguire gate dopo ogni volume**

Expected per ciascun blocco: matrice completa, report, fonti consolidate, capitoli integrati, nessun blocker prima di stato pubblicabile.

### Task 7: Gate finale, memoria e GitHub

**Files:**
- Modify: `wiki/index.md`, `wiki/log.md`, memoria locale e dashboard.
- Create: `wiki/reviews/review-copertura-didattica-integrale-finale.md`

**Interfaces:**
- Consumes: tutti gli audit e le integrazioni.
- Produces: evidenza finale, commit ordinati, push GitHub e istruzioni staff.

- [ ] **Step 1: Eseguire verifiche complete**

```powershell
npm test
npm run typecheck
npm run audit:coverage
git diff --check
```

- [ ] **Step 2: Eseguire Revisore Editoriale Totale**

Applicare checklist a 30 punti più gate di copertura a ogni volume candidabile alla pubblicazione.

- [ ] **Step 3: Aggiornare index, log e memoria**

Registrare decisione, artefatti, esiti, limiti e stato reale; non usare “completo” per volumi con blocker.

- [ ] **Step 4: Organizzare i commit**

Separare governance, tool, inventari, audit e integrazioni; escludere artefatti temporanei e log di processo non destinati al repository.

- [ ] **Step 5: Sincronizzare e pubblicare**

Rieseguire `git fetch origin --prune`, verificare divergenze, integrare non distruttivamente eventuali nuovi commit remoti, eseguire di nuovo i test e poi push.

- [ ] **Step 6: Consegnare istruzioni allo staff**

Indicare commit/branch pubblicati, comandi di fetch/pull e eventuali migrazioni o rigenerazioni della dashboard.
