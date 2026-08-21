---
id: m-tr04-text-freeze-manifest
type: text_freeze_manifest
title: "Text freeze — M-TR04 Ambiente, protezione civile e sostenibilità"
status: frozen
domain: "concorsi pubblici italiani"
book_id: m-tr04-ambiente-protezione-civile
volume_code: VOL-11
module_code: M-TR04
freeze_date: 2026-08-19
reference_commit: 1014415c4a681c8eea0663319c8fb68e3ac4e5a7
updated_at: 2026-08-19T00:58:22+02:00
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

- Commit di base: 1014415c4a681c8eea0663319c8fb68e3ac4e5a7.
- Stato da congelare: modifiche correnti degli step 13-16, identificate dagli hash seguenti e destinate al successivo commit di pipeline.
- Algoritmo: SHA-256 sul contenuto dei file.
- Cut-off dell'audit specialistico: 18 agosto 2026, secondo le fonti ufficiali e le source note consolidate nel progetto.

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
| Fonti e cut-off | Source refs presenti in tutti i capitoli; cut-off specialistico 18-08-2026 dichiarato | superata |
| Dati mobili | Nessun box Dato operativo rilevato dal contratto; dati 2026 individuati nei metadati e auditati nello step 15 | superata |

## File congelati

| File | Stato | SHA-256 |
| --- | --- | --- |
| index.md | frozen | 9e7137d8216e45ebbc935a0f67d2dd7f84cefff46e01c1912b6b7df6ac91946f |
| planning/01-indice-analitico-vol-11.md | frozen | e0539f7afbb124b282868a427a70cbc31a34d8ed198607f7f458e0f638867dcc |
| planning/02-matrice-copertura-didattica.md | frozen | e4f55e54283996f97fef66775a3b8f170f656ce23cad6072b1391fb672070568 |
| planning/17-bibbia-del-modulo.md | frozen | 07b75a61dd3021891d5398ae6cf763f6ad0195ee4ac1e21f547dbd6542650ade |
| chapters/01-quattro-profili-mappa-sistema.md | frozen | 289767352133ba9a06015060e31d0b884edeaabd05d1fe60036a815a3b6c41bf |
| chapters/02-dlgs-152-mase-ispra-snpa.md | frozen | 20586529df75dd7c70fbff7887c1e634ea17bff3fd79d1a2024eb674704792ed |
| chapters/03-via-vas-valutazioni-ambientali.md | frozen | bf164efa9f8f61c74cb872f6b3ddec2d3558f9f3297ff48b8505ba11b79ea21d |
| chapters/04-aia-aua-emissioni-autorizzazioni.md | frozen | f7f2ddf971e0d74231937ecfe34ee038959ee41ec69f3c0b9651df2da7158036 |
| chapters/05-acque-scarichi-servizio-idrico.md | frozen | af4433bcda8f3e684dc2c46ea0d6195e4cba9ef5175658d02ba1b847ba27949a |
| chapters/06-rifiuti-economia-circolare-rentri.md | frozen | 916bb8a60f4d62c95cfd56f6c7889c212fcca213be5cab422a020be7222cfb02 |
| chapters/07-bonifiche-siti-contaminati-danno.md | frozen | 70c851e5dd13ecf329ff281510b2c3b6bee59a2193875709df6b6e5e6b5918c0 |
| chapters/08-aria-rumore-monitoraggio-dati.md | frozen | e5607015cfb541507726f902ded75525d95138015d56a4ec1c25e60031753646 |
| chapters/09-controlli-sanzioni-reati-ambientali.md | frozen | 6d9d82f63aa9ae5ed9032d85dffc2c1ef33ddd586acc02b8fbae9a63eca7dbc7 |
| chapters/10-sistema-protezione-civile-pianificazione.md | frozen | 506fae640171d25f1748ac7edf53e1f831dfdec3b3e2930b64f6d3f3020d77ec |
| chapters/11-rischi-allertamento-it-alert-emergenze.md | frozen | 37cdf04407960d8944837bf60fc027c1426fc487176091f7ec4fd5a9db5256f3 |
| chapters/12-clima-energia-rinnovabili-cer.md | frozen | bed838e4ecdb44f50c36fd707ef30275fbf4631c69dda60f6c977a13b4d2c4b2 |
| chapters/13-dnsh-cam-sostenibilita-pa.md | frozen | 14711ad41ade2a4c34326313dac3a3a49038cb3baabb5d841d917b521ee03347 |
| chapters/14-laboratorio-casi-quesiti-sintetici.md | frozen | fb2beda33a31af3c8c251d4a4bf1a996eef4fbac35131b1a2c423d3004a50596 |

## Regola successiva al freeze

Ogni modifica sostanziale successiva deve essere tracciata e sottoposta nuovamente a copertura, Humanizer, revisione trasversale e audit specialistico prima di un nuovo freeze.