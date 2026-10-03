---
id: review-piano-integrazioni-vol-01-vol-07-2026-10-02
type: editorial_plan
title: Integrazioni nazionali VOL-01 e VOL-07 dal piano Angela
status: in_progress
domain: pianificazione-editoriale
topics: []
entities: []
source_refs: []
book_refs: [il-metodo-bando, m-sa01-sanita-amministrativa]
confidence: medium
updated_at: 2026-10-02
created_at: 2026-10-02
review_required: true
canonical: false
tags: [integrazioni, esclusioni-concordate, piano-staff]
---

# Perimetro autorizzato

Integrare le lacune nazionali emerse dal piano di studio Angela nei libri esistenti, preservando il testo precedente e l'autonomia didattica. Nessun nuovo capitolo è necessario per il perimetro individuato.

Esclusioni esplicite dell'utente: normativa e organizzazione specifica Campania/ASL Caserta; cultura generale. Quest'ultima resta sospesa: in un lavoro successivo sarà affrontata mediante banca dati quiz, senza teoria. Non creare adesso né teoria né banca dati di cultura generale.

## Stato delle evidenze

- Analizzato il workbook `Piano_personale_Angela_ASL_Caserta_Assistenti_Amministrativi_2026-10-02_v10.xlsx`, incluso il foglio SQ3R e il registro fonti.
- Il PDF richiesto `Piano_personale_Angela_ASL_Caserta_Assistenti_Amministrativi_2026-10-01_v2.pdf` non è stato reperito: confronto integrale fra i due piani NON concluso. Non è stato sostituito con un PDF precedente.
- Letta la pagina sulle prove del bando locale `BANDO-40-ASS-AMM.pdf-5931-KB.pdf`.
- Ricognizioni di lavoro: `tmp/integrazione-20261002-base.md` e `tmp/integrazione-20261002-sanita.md`. Sono memo di audit, NON source notes consolidate né attestazioni di verifica integrale delle norme.

## Integrazioni scritte e revisionate

| ID | Destinazione già esistente | Delta didattico | Stato |
| --- | --- | --- | --- |
| INT-01 | VOL-01, cap.05 | DPR445: certificati, dichiarazioni, firme, copie, acquisizione d'ufficio, limiti, controlli e conseguenze; esempi e quiz commentati | Testo integrato; revisione indipendente conclusa |
| INT-02 | VOL-01, cap.05 | Rimedi amministrativi e giurisdizionali: presupposti, differenze, termini verificati, silenzio e autotutela | Testo integrato; revisione indipendente conclusa |
| INT-03 | VOL-01, cap.06 | Incompatibilità, inconferibilità, incarichi esterni e conflitto di interessi: ambiti e conseguenze distinti | Testo integrato; revisione indipendente conclusa |
| INT-04 | VOL-01, cap.12 | Operazioni, decimali, frazioni, equivalenze e conversioni; progressione di esercizi numerici e logici con soluzioni ragionate | Testo integrato; 43 chiavi verificate |
| INT-05 | VOL-07, M-SA01 cap.04 | Principi SSN, riordino e aziendalizzazione, Stato-Regioni, attori nazionali, aziende e organi | Testo integrato; revisione indipendente conclusa |
| INT-06 | VOL-07, M-SA01 cap.04 | LEA, distretto, prevenzione, ospedale, rete territoriale, programmazione e integrazione sociosanitaria | Testo integrato; revisione indipendente conclusa |
| INT-07 | VOL-07, M-SA01 cap.04 | Autorizzazione, accreditamento e accordi contrattuali: condizioni e differenze, senza specificità regionali | Testo integrato; revisione indipendente conclusa |
| INT-08 | VOL-07, M-SA01 cap.09 | Finanziamento SSN, riparto e assegnazione, mobilità e remunerazione; raccordo con budget e contabilità già trattati | Testo integrato; revisione indipendente conclusa |

Le risposte brevi applicative possono stare accanto ai nuclei integrati. Il cap.15 del base resta un'eventuale destinazione complementare, non un pretesto per duplicare la teoria. Conservare i 25 quesiti già presenti nel cap.12 e distinguere chiaramente i nuovi esercizi graduati.

## Controlli prima della scrittura e della chiusura

1. Consolidare le fonti primarie correnti e collegare source/topic/entity pages prima della prosa finale. Il mero indice di Normattiva non dimostra la verifica di ogni articolo.
2. Risolvere le criticità segnalate nei memo: ambito dei privati nel DPR445, disciplina aggiornata degli incarichi, composizione degli organi sanitari, decorrenza delle novità LEA e disposizioni transitorie sull'accreditamento. Non usare FAQ storiche per affermare una regola vigente.
3. Aggiornare le matrici aggregate che oggi marcano come completi nuclei solo nominati. Non promuovere uno stato a completo prima di teoria, esempio, errore tipico e verifica effettivamente presenti.
4. Integrare soltanto i capitoli dichiarati nelle schede; M-SA01 ha target 04,05,06,09,10. I rinvii residui a inesistenti cap.02/03 non autorizzano nuovi target.
5. Ripetere copertura, Humanizer e micro-revisione sui passaggi sostanzialmente modificati; eseguire poi audit specialistico, nuovo freeze e controlli di impaginazione/consegna. I PDF precedenti non rappresenteranno automaticamente le integrazioni.

## Pipeline e vincolo operativo

Applicata la skill `pipeline-volume`: riapertura tramite CLI dello step14 con cascata per VOL-01/M-PA01 e VOL-07/M-SA01. Entrambi hanno superato nuovamente 14/15; i freeze16 sono stati chiusi con verifiche manuali documentate, perché il gate non è implementato. VOL-01 è al successivo step17; VOL-07 ha aggiornato la filosofia visiva17 e mantiene18 in-progress. I controlli di impaginazione e consegna restano riaperti, non automaticamente superati. Nessuna modifica manuale ai run-state e nessuna chiusura forzata di gate.

Per riprendere il target M-SA01 usare `next VOL-07 --step 14 --module M-SA01 --json`: la combinazione `--from 14 --module M-SA01` seleziona un target precedente di capitolo e non trova lo step richiesto. Nessuna modifica al codice del CLI effettuata.

La regola locale impone GPT-5.5/xhigh per la scrittura; il Codex CLI risulta non autenticato. L'utente ha autorizzato esplicitamente l'uso del modello della sessione («si continua con questo modello»). La deroga vale per questo incarico e non modifica la regola persistente. Completate scrittura e revisioni dei delta sui cinque capitoli indicati; le evidenze e i limiti restano nei report, non sono sostituiti da questo piano.

## Risultato testuale del 2 ottobre

Integrati cinque capitoli esistenti: VOL-01 cap.05,06,12 e VOL-07/M-SA01 cap.04,09. Aggiunti 43 quiz a scelta multipla commentati (6 documentazione,4 incarichi,18 numerici,10 organizzazione sanitaria,5 finanziamento), oltre a casi, esercizi e tre verifiche sui rimedi. Ricontrollati anche i 25 quesiti logici preesistenti, con correzioni delle ambiguità e delle chiavi errate individuate.

- [[reviews/integrazione-base-verifica-indipendente-2026-10-02]].
- [[reviews/integrazione-cap12-verifica-indipendente-2026-10-02]].
- [[reviews/integrazione-sanita-verifica-indipendente-2026-10-02]].
- [[reviews/pipeline/VOL-07/16-moduli-m-sa01-sanita-amministrativa]].

Le verifiche riguardano i delta dichiarati, non una certificazione di aggiornamento di tutti i capitoli della collana.

Matrici correnti: VOL-01 21 nuclei completi; M-SA01 12. Per il layout sono state suddivise nove tabelle preesistenti: due nel base e sette nella sanità. Nessuna tabella oltre tre colonne rimane nei cinque capitoli integrati. Contenuti e dati conservati, senza riduzione dei caratteri. Verifica del PDF ancora pendente.

Verifica preview conclusa: [[reviews/integrazione-layout-verifica-preview-2026-10-02]]. Conteggi DOM assestati 615 e 414 pagine; controlli geometrici su 160 pagine dei cinque capitoli senza anomalie rilevate e ispezione visiva di un campione dichiarato. Corretta e ricontrollata un'etichetta orfana. Restano audit visivo completo, doppia didascalia preesistente Figura 5.5 nel base, valutazione di alcuni spazi e tabelle degli altri capitoli, nuovo PDF e preflight. Il campione non certifica l'intero impaginato.

## Layout: requisito permanente, non facoltativo

L'utente ha ribadito di ottimizzare sempre anche il layout delle pagine. Preferenza salvata tramite LocalAgentMemory e aggiunta a wiki/AGENTS.md. A ogni integrazione: rigenerare l'impaginato e controllare spazi bianchi, leggibilità di tabelle/quiz, titoli orfani, interruzioni, margini, coerenza tipografica e separazione delle soluzioni. Dividere i blocchi densi senza ridurre arbitrariamente i caratteri. I PDF precedenti non comprendono automaticamente le aggiunte e non possono essere dichiarati aggiornati sulla sola base del text freeze.
