# VOL-05 Authority e regolazione — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consegnare un dossier wiki source-ready e un indice professionale completo per VOL-05/M-FC05.

**Architecture:** Le fonti ufficiali vengono archiviate come raw immutabili e trasformate in source note. Le note alimentano pagine tema/entità e il volume unico VOL-05, articolato in moduli interni con front matter solamente iniziale.

**Tech Stack:** Markdown, Obsidian links, PowerShell per download riproducibili, fonti istituzionali e EUR-Lex.

## Global Constraints

- Non modificare VOL-01 né file estranei al perimetro VOL-05.
- Usare fonti primarie ufficiali e dichiarare la data di verifica.
- Non duplicare le aree B-PA: inserire rinvii precisi e contenuto delta.
- Conservare in ogni modulo interno solo frontespizio e sommario.

---

### Task 1: Consolidare le fonti istituzionali

**Files:**
- Create: `wiki/raw/vol-05-authority-regolazione/`
- Create: `wiki/sources/vol-05-fonti-ufficiali-scaricate-2026-07-24.md`
- Create: source note M-FC05 per normativa, bandi e autorità.

- [ ] Acquisire i testi normativi, UE e concorsuali da fonti istituzionali.
- [ ] Registrare URL, data di verifica, autorità, uso editoriale e limiti.
- [ ] Collegare ogni fonte ai nuclei e ai capitoli interessati.

### Task 2: Consolidare pagine tema ed entità

**Files:**
- Create: `wiki/topics/authority-indipendenti-regolazione.md`
- Create: topic settoriali per concorrenza, energia, comunicazioni, finanza-vigilanza, privacy e anticorruzione.
- Create: entity page per le authority non già presenti.

- [ ] Sintetizzare la conoscenza consolidata senza usare i raw come testo editoriale.
- [ ] Inserire source link, chapter link e review necessarie.

### Task 3: Creare il volume e l'indice analitico

**Files:**
- Create: `wiki/books/vol-05-authority-regolazione/index.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/index.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/00-piano-editoriale.md`

- [ ] Redigere front matter iniziale e indice dettagliato del volume.
- [ ] Organizzare i moduli interni e i relativi sommari.
- [ ] Mappare ogni capitolo a fonti, materie, output e stato di copertura.

### Task 4: Verificare e registrare l'esito

**Files:**
- Create: `wiki/reviews/vol-05-source-ready-audit-2026-07-24.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] Verificare link, metadati, perimetro e copertura dei nuclei.
- [ ] Registrare fonti mancanti e review normative residui.
- [ ] Catturare una traccia sintetica in LocalAgentMemory.
