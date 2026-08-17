# Task 1: Perimetro ACFI e corpus ufficiale

## Contesto

Il modulo M-FC02 presenta la fiscalità internazionale ACFI come unico nucleo ancora `solo-nominato`. Questo task deve produrre la base normativa consolidata; nessun testo editoriale del capitolo può essere scritto prima dell'approvazione di questa fonte.

## Vincoli globali

- Perimetro selettivo ACFI: residenza, stabile organizzazione, convenzioni, doppia imposizione, transfer pricing, operazioni infragruppo, rischio e tax control framework.
- Nessun claim editoriale deriva direttamente da `wiki/raw/`.
- Nessuna aliquota, soglia, termine o lista mobile priva di verifica ufficiale puntuale.
- Preservare tutte le modifiche preesistenti nel worktree.
- Il nucleo diventa `completo` soltanto dopo review normativa ed editoriale indipendente.

## File

- Leggere `wiki/raw/m-fc02-agenzie-fiscali/ae-avviso-350-funzionari-acfi-2025.html`.
- Leggere `wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md`.
- Creare raw ufficiali pertinenti in `wiki/raw/m-fc02-agenzie-fiscali/`.
- Creare `wiki/sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18.md`.

## Requisiti

1. Estrarre dal bando ufficiale materie e attività effettive del profilo ACFI.
2. Verificare su fonti primarie ufficiali aggiornate al 18 luglio 2026: artt. 2, 73, 110 e 162 TUIR; funzione e struttura delle convenzioni contro le doppie imposizioni e del modello OCSE; disciplina ufficiale del transfer pricing; documentazione infragruppo e analisi del rischio pertinenti.
3. Salvare i documenti ufficiali mancanti nei raw con slug descrittivi, URL, versione e data di audit; non modificare raw esistenti.
4. Scrivere la source note con frontmatter canonico e sezioni: esito audit; perimetro ACFI; gerarchia fonti; residenza; stabile organizzazione; convenzioni/doppia imposizione; transfer pricing; documentazione e rischio; raccordo TCF; metodo del caso; limiti/review; raw refs e link consolidati.
5. Controllare frontmatter, raw refs, wikilink, UTF-8 e `git diff --check`.
6. Non modificare capitoli, matrici, report, `wiki/index.md`, `wiki/log.md` o memoria.
7. Non eseguire commit: il controller committerà dopo la review indipendente.

## Report

Scrivere il rapporto completo in `.superpowers/sdd/acfi-task-1-report.md` includendo: file creati, URL ufficiali, perimetro estratto dal bando, controlli eseguiti con risultati, self-review, limiti o dubbi. Restituire in chat solo `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT` o `BLOCKED`, una riga di verifica e le eventuali preoccupazioni.
