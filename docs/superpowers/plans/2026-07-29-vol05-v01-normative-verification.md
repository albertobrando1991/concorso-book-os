# VOL-05 V01 Normative Verification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verificare con fonti primarie vigenti le voci V01 dei quindici capitoli M-FC05 e registrare esclusivamente correzioni dimostrate.

**Architecture:** Le fonti istituzionali vengono confrontate con le source note consolidate e con le voci V01 dei report del 28 luglio 2026. Gli esiti aggiornano le source note necessarie, i report per capitolo e un report trasversale, senza riscritture editoriali non richieste.

**Tech Stack:** Markdown, fonti ufficiali delle autorità italiane, EUR-Lex, Normattiva, `vitest` per i controlli disponibili.

## Global Constraints

- Data di cut-off: 29 luglio 2026.
- Usare fonti primarie o istituzionali; non usare `wiki/raw/` come testo editoriale.
- Distinguere fatto verificato, dato non riscontrato e aggiornamento ancora necessario.
- Applicare al testo solo correzioni fattuali inequivoche e tracciarle nel report.

---

### Task 1: Inventario V01 e fonti

**Files:**
- Read: `wiki/reviews/m-fc05-capitolo-01-…15-revisione-editoriale-2026-07-28.md`
- Read: `wiki/sources/*-2026-07-24.md`
- Create: `wiki/reviews/m-fc05-verifica-v01-normativa-2026-07-29.md`

- [x] Estrarre V01 e claim associati dei quindici capitoli.
- [x] Associare ciascun claim a una fonte primaria ufficiale e alla data di verifica.

### Task 2: Verifica normativa dei nuclei comuni e regolatori

**Files:**
- Read/modify when justified: source note e report dei Capitoli 1–7.

- [x] Verificare basi legali, procedimenti, AIR/VIR, poteri istruttori e rimedi con fonti UE, Normattiva e autorità competenti.
- [x] Registrare esito e difformità dimostrate.

### Task 3: Verifica delle authority e del laboratorio

**Files:**
- Read/modify when justified: source note e report dei Capitoli 8–15.

- [x] Verificare competenze e atti delle authority, GDPR/EDPB, PNA e whistleblowing.
- [x] Verificare che le tracce del laboratorio restino dichiarate originali e subordinate al bando target.

### Task 4: Consolidamento e gate

**Files:**
- Modify: `wiki/reviews/m-fc05-*.md`, solo per esiti effettivi.
- Modify: `wiki/log.md`, `wiki/memory/agent/`.

- [x] Aggiornare gli stati V01 con esito, fonte e data.
- [x] Applicare eventuali correzioni inequivoche e registrarle.
- [x] Eseguire `git diff --check` e i test M-FC05 disponibili.
