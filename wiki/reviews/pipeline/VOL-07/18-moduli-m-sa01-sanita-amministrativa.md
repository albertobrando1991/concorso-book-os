---
id: review-vol-07-step-18-m-sa01-image-audit
type: review
title: Audit immagini e layout M-SA01 — integrazioni nazionali
status: in_progress
updated_at: 2026-10-02
review_required: true
canonical: false
book_refs: [m-sa01-sanita-amministrativa, vol-07-sanita-amministrativa-professioni-sanitarie]
tags: [pipeline-step-18, image-audit, layout]
---

# Audit immagini e layout — M-SA01

## Stato reale

Ricontrollati i cinque file di capitolo: nessun riferimento Markdown/HTML a immagini e nessun asset raster/vettoriale nella cartella modulo. Non serve grafica decorativa. La nuova filosofia Precisione Vitale conserva formato KDP e gerarchia della collana.

Nei capitoli04/09 interessati dalle integrazioni sono state suddivise sette tabelle da4–8colonne in blocchi collegati a2–3colonne, conservando tutte le114tuple chiave/intestazione/cella. Lint e rinvii ricontrollati con esito positivo. Evidenza: [[reviews/integrazione-layout-tabelle-sanita-2026-10-02]].

| Asset/blocco | Problema | Correzione | Verifica | Esito |
| --- | --- | --- | --- | --- |
| Immagini dei cinque capitoli | Nessun asset o riferimento rilevato | Nessuna nuova grafica | Inventario sorgenti | Non applicabile |
| Tabelle cap04/09 | Griglie fino a8colonne nel paperback | Divisione in tabelle2–3colonne collegate dalla stessa chiave | Conservazione celle, lint e preview DOM mirata | Correzione applicata; PDF da verificare |
| Tabelle cap05/06/10 | Quattro tabelle comparative preesistenti a4colonne | Valutare resa reale prima di decidere eventuale divisione | Ricognizione sorgenti, non nuova revisione visiva completa | Controllo residuo |
| Pagine del modulo | La sola anteprima non prova il PDF | Rigenerare PDF e controllare pagine, salti, margini, spazi e leggibilità | Non eseguito in questo turno | Pendente |

Lo step18 resta in-progress: non si usa il report storico come prova di una nuova revisione visiva completa. Le precedenti evidenze sono conservate in [[reviews/pipeline/VOL-07/archive/18-m-sa01-pre-integrazione-2026-10-02]]. Gli step19–23 restano aperti e lo step24 richiede la conferma umana del pacchetto finale.


## Riesame di produzione del 3 ottobre 2026

Prova `vol-07-release-20261003-proof.pdf`. Capitoli osservati nelle pagine 9–141; tabelle contabili e procurement già ingranditi nella prova precedente.

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
| Tabelle native, nessuna immagine raster | Leggibilità e continuazioni dopo ripaginazione | Conservata la tipografia 9,5 pt degli apparati | Panoramica completa della proiezione Book Studio esportata, controlli geometrici senza overflow | Verificato nel perimetro visivo dichiarato |

Seconda passata su precisione e uniformità conclusa. La panoramica non equivale a lettura a piena risoluzione di ogni pagina. Evidenze nel registro VOL-07-production-visual-checkpoint.json.
