---
id: m-tr04-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-TR04 Ambiente, protezione civile e sostenibilità"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-tr04-ambiente-protezione-civile
volume_code: VOL-11
module_code: M-TR04
freeze_date: 2026-08-21
reference_commit: fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a
updated_at: 2026-08-21T12:00:00+02:00
created_at: 2026-08-19T00:58:22+02:00
review_required: false
canonical: true
tags: ["text-freeze", "vol-11", "m-tr04", "pipeline-step-16"]
---

# Text freeze — M-TR04 Ambiente, protezione civile e sostenibilità

## Esito

Il modulo entra in congelamento testuale il 19 agosto 2026. I quattordici capitoli e i 90 nuclei sono presenti; la matrice non contiene stati parziale, solo-nominato o mancante; gli errori obbligatori degli step 13-15 sono chiusi; indice, Bibbia, fonti e apparati risultano coerenti. Il gate text-freeze non è ancora implementato e viene chiuso con accettazione manuale motivata dopo questa verifica.

Da questo manifest sono ammesse soltanto correzioni controllate. Ogni modifica sostanziale a teoria, fonti, casi, quiz, riferimenti o struttura riapre i gate 10-15.

## Riferimento di versione

- Commit di base: fedfb0fe49cef4c111f18ac014c77d7eb1e1cd4a.
- Stato da congelare: modifiche correnti degli step 13-16, identificate dagli hash seguenti e destinate al successivo commit di pipeline.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cut-off dell'audit specialistico: 18 agosto 2026, secondo le fonti ufficiali e le source note consolidate nel progetto.
- Ricontrollo indipendente: 21 agosto 2026 su Gazzetta Ufficiale, RENTRI, Dipartimento della Protezione civile, EUR-Lex, ARERA e GSE.

## Verifica delle condizioni

| Condizione | Evidenza | Esito |
| --- | --- | --- |
| Capitoli presenti | Quattordici target, quattordici file e un solo H1 per capitolo | superata |
| Copertura integrale | 90 nuclei; nessuno stato parziale, solo-nominato o mancante nella matrice | superata |
| Rinvii | Rinvii editoriali precisati; slug, ID e source_refs preservati | superata |
| Humanizer | Tutti i quattordici step 11 risultano chiusi; passaggi sostanziali dello step 15 micro-revisionati | superata |
| Errori obbligatori | Step 13 e 14 chiusi; gate step 15 verde senza blocker né warning | superata |
| Audit specialistico | VIA, FIR/RENTRI, IT-alert, aria, CER/TIAD e DNSH/CAM consolidati nel report step 15 | superata |
| Indice | Quattordici voci e quattordici capitoli; matrice e Bibbia allineate | superata |
| Fonti e cut-off | Source refs presenti in tutti i capitoli; cut-off specialistico 21-08-2026 dichiarato | superata |
| Dati mobili | Nessun box Dato operativo rilevato dal contratto; dati 2026 individuati nei metadati e auditati nello step 15 | superata |

## File congelati

| File | Stato | SHA-256 |
| --- | --- | --- |
| index.md | frozen | 09149c2db711249312e05b773e7dba5cc6728530cbd7d952a2c9cecae9462900 |
| planning/01-indice-analitico-vol-11.md | frozen | 86458d70ded013e355b972f6f727dc44c5fb774272f31776ba5c4922a5a1365d |
| planning/02-matrice-copertura-didattica.md | frozen | 5423bcc1583a5fbb2372e693633c7a23dcfa66aa376089a4db0368b11dc99069 |
| planning/17-bibbia-del-modulo.md | frozen | 07b75a61dd3021891d5398ae6cf763f6ad0195ee4ac1e21f547dbd6542650ade |
| chapters/01-quattro-profili-mappa-sistema.md | frozen | fe727db84e5811000259c3ac5bd7494cdb3bf06eb288509cb352843cf9e3a569 |
| chapters/02-dlgs-152-mase-ispra-snpa.md | frozen | 7a4ff4fab5ff89eec01012028c4a27fad5c26b80835590dba427dd125e1bbd1f |
| chapters/03-via-vas-valutazioni-ambientali.md | frozen | 007d86b372cf52a6d7ceb1d5271deae63f6dfc8bcc3fc1634d866d2f84ee9cec |
| chapters/04-aia-aua-emissioni-autorizzazioni.md | frozen | 92ed87e06cb293f7994f7e1da7b1446531b5eb4acc8201bdda85778396e3ec5c |
| chapters/05-acque-scarichi-servizio-idrico.md | frozen | ec304e0d8bffb1cf7ccf58cc74f8b3328db73c77d3da1dcf5552824da6e802bd |
| chapters/06-rifiuti-economia-circolare-rentri.md | frozen | d1e8c0bd3d4c4723b6b16d57024e86b228b6693230e9e16c4fd32f680802301c |
| chapters/07-bonifiche-siti-contaminati-danno.md | frozen | 0654c4ae0a8c7c6765a666e40d2b1f72d3ed7775031f24c56868d0660f3b3762 |
| chapters/08-aria-rumore-monitoraggio-dati.md | frozen | 790ef3e8d9e592dbee8c3e243303e9e97cf687d5a6425133c9f090fe6e9a3d56 |
| chapters/09-controlli-sanzioni-reati-ambientali.md | frozen | 012fc1659be9dfce7653ddec509cef9a1ec9278ddc5799d48586392c3ecee011 |
| chapters/10-sistema-protezione-civile-pianificazione.md | frozen | c5b12ef36d68c451fe16a30c2125abed20b51e84a1f95379ee109fd73f352b9f |
| chapters/11-rischi-allertamento-it-alert-emergenze.md | frozen | 235f875e7dabaec1ad38f3a9b7bc2db7906d0bc3f8d3a73fbbb09c7b81290cda |
| chapters/12-clima-energia-rinnovabili-cer.md | frozen | 0b0f3172028d4db7771d80bd73d7be59738292fe4687e9fea66a2b1da4b6fd3b |
| chapters/13-dnsh-cam-sostenibilita-pa.md | frozen | 1653d60448669c03a974dc8f5171917973006117d2f42122d1afabb8f85ee3c1 |
| chapters/14-laboratorio-casi-quesiti-sintetici.md | frozen | f973e39064bf1fe77782e938c4ad705cba9c681dd76fe4d9f02883af50a06570 |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.
