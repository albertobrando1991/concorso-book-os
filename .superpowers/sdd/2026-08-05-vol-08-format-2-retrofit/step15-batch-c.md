# Step 15 — audit atomico, batch C (capitoli 10–13)

Data del controllo: 2026-08-12. Cutoff normativo: 2026-08-12. Revisore tecnico: `codex-step15-batch-c`; gate: `step-15`.

## Metodo ed esito

Questo dossier registra 28 nuclei (7 per capitolo), senza aggiornare manifest, matrice o testo editoriale. `Q/C/E` resta **chapter-level**: i capitoli non offrono un collegamento esplicito e affidabile tra una singola citazione e una quota numerica. Ogni record è `FAIL — non promuovere`: l'attuale manifest non contiene un'attestazione atomica e quindi non è consentito trasformare questi riscontri in `verified`.

Le quote sono letterali e complete come periodo/paragrafo probatorio nel nucleo indicato; `sourceLocation` è il relativo anchor Markdown. “Fonte primaria” identifica il riferimento verificato, non una pretesa che la fonte normativa dimostri da sola le parti metodologiche/editoriali. Per il capitolo 13 le fonti di metodo sono mantenute distinte e non sostituiscono il bando o gli atti della procedura.

### Fonti primarie verificate

- DGA — Regolamento (UE) 2022/868, CELEX 32022R0868, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2022/868/oj>.
- Open data — Direttiva (UE) 2019/1024, CELEX 32019L1024, EUR-Lex: <https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32019L1024>.
- Interoperabilità — Regolamento (UE) 2024/903, CELEX 32024R0903, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2024/903/oj>.
- Privacy — Regolamento (UE) 2016/679, CELEX 32016R0679, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2016/679/oj>.
- AI Act — Regolamento (UE) 2024/1689, CELEX 32024R1689, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>.
- Modifica AI Act — Regolamento (UE) 2026/1744, CELEX 32026R1744, GU L del 24-07-2026, in vigore dal 27-07-2026, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>.
- Contratti pubblici — d.lgs. 31 marzo 2023, n. 36, Normattiva: <https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=23G00044&atto.dataPubblicazioneGazzetta=2023-03-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=be987210-bd7c-41b1-994e-ffeaa414f240&tabID=0.5832057097543953&tipoDettaglio=vigente&title=lbl.dettaglioAtto>.
- Concorsi — d.P.R. 9 maggio 1994, n. 487, Normattiva: <https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Apresidente.repubblica%3Adecreto%3A1994%3B487~art2=>.

## Capitolo 10 — Data governance, open data e interoperabilità

| ID | Quote letterale completa | sourceLocation | T/A/O | Fonte primaria | Esito / correzione |
| --- | --- | --- | --- | --- | --- |
| N-TR01-10-01 | “Un asset informativo va letto anche per le sue conseguenze: se una definizione cambia, possono cambiare calcoli, comunicazioni, indicatori, controlli e servizi collegati.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-01` | T: governance; A: conflitto di definizioni; O: fonte autorevole/versione | DGA 2022/868 | FAIL — attribuzione primaria da collegare nel manifest. |
| N-TR01-10-02 | “Una mappa di ruoli parte dalle decisioni ricorrenti: chi approva una definizione, chi autorizza un nuovo fruitore, chi valuta un difetto di qualità, chi cambia la frequenza di aggiornamento, chi sospende una distribuzione.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-02` | T: ruoli; A: RACI; O: mappa decisionale | DGA 2022/868 | FAIL — attesta solo presenza testuale, non verifica atomica. |
| N-TR01-10-03 | “Ogni fase del ciclo deve avere un punto di ingresso e uno di uscita riconoscibile.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-03` | T: ciclo; A: classificazione; O: tracciato lifecycle | DGA 2022/868 | FAIL — fonte/posizione da registrare nel contratto. |
| N-TR01-10-04 | “Un metadato utile risponde a una domanda concreta.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-04` | T: metadati; A: catalogo; O: scheda metadato | Dir. 2019/1024 | FAIL — nessuna promozione senza attestation. |
| N-TR01-10-05 | “Una regola di qualità deve indicare anche il punto in cui viene applicata.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-05` | T: qualità; A: controlli; O: regola/metrica | Reg. 2016/679, art. 5(1)(d) | FAIL — requisito editoriale non ancora attestato. |
| N-TR01-10-06 | “Un dataset aperto è utile quando una persona diversa dall'ente può capirlo, ottenerlo e riutilizzarlo senza ricostruirne ogni volta il significato.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-06` | T: riuso; A: distribuzione; O: dataset documentato | Dir. 2019/1024 | FAIL — fonte da associare atomicamente. |
| N-TR01-10-07 | “Prima di attivare uno scambio automatico, l'ente descrive evento che lo attiva, finalità, attributi necessari, erogatore, fruitore, risposta attesa, errori possibili e responsabilità di correzione.” | `chapters/10-data-governance-open-data-interoperabilita.md#n-tr01-10-07` | T: interoperabilità; A: scambio; O: requisito organizzativo | Reg. 2024/903; Reg. 2016/679 | FAIL — non iscrivere come verificato. |

## Capitolo 11 — AI/ML, rischi e compliance

| ID | Quote letterale completa | sourceLocation | T/A/O | Fonte primaria | Esito / correzione |
| --- | --- | --- | --- | --- | --- |
| N-TR01-11-01 | “Un algoritmo è una procedura finita che trasforma input in output.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-01` | T: algoritmo; A: distinzione; O: definizione motivata | Reg. 2024/1689, art. 3 (solo quadro legale) | FAIL — no fonte primaria per la tassonomia didattica completa. |
| N-TR01-11-02 | “Nell'apprendimento supervisionato gli esempi contengono input e risultato atteso.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-02` | T: paradigmi; A: classificazione; O: distinzione | Reg. 2024/1689 (contesto, non prova didattica) | FAIL — richiede fonte tecnica consolidata separata. |
| N-TR01-11-03 | “Il dato per l'AI non è una materia prima neutra.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-03` | T: provenienza; A: dataset; O: scheda dati | Reg. 2024/1689, artt. 10 e 13 | FAIL — collegare la fonte al record. |
| N-TR01-11-04 | “Prima di misurare un modello occorre fissare una baseline: può essere una regola semplice, il procedimento attuale o una prestazione minima.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-04` | T: metriche; A: confronto; O: baseline | Reg. 2024/1689, artt. 9 e 15 | FAIL — fonte non sufficiente per l'intera didattica. |
| N-TR01-11-05 | “Il bias può nascere nel campionamento, nelle etichette, nelle feature, nell'obiettivo ottimizzato o nel modo in cui il risultato entra nel lavoro quotidiano.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-05` | T: bias; A: analisi; O: azione correttiva | Reg. 2024/1689, artt. 9, 10, 14 | FAIL — record non attestato. |
| N-TR01-11-06 | “Un sistema AI va governato lungo il suo ciclo di vita: definizione del problema, raccolta e preparazione dei dati, sviluppo, validazione, rilascio, uso, monitoraggio, modifica e dismissione.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-06` | T: lifecycle; A: MLOps; O: versioni/evidenze | Reg. 2024/1689, artt. 9, 17, 72 | FAIL — nessuna attestazione nel manifest. |
| N-TR01-11-07 | “Il regolamento (UE) 2024/1689, noto come AI Act, adotta un approccio basato sul rischio.” | `chapters/11-ai-ml-pa-rischi-compliance.md#n-tr01-11-07` | T: quadro UE; A: classificazione; O: verifica di ruolo/uso | Reg. 2024/1689, modificato da Reg. 2026/1744 (CELEX 32026R1744; cutoff 2026-08-12) | FAIL — aggiornare dossier sorgenti e record atomico; non dichiarare il testo consolidato verificato oltre il cutoff. |

## Capitolo 12 — Procurement ICT e gestione fornitori

| ID | Quote letterale completa | sourceLocation | T/A/O | Fonte primaria | Esito / correzione |
| --- | --- | --- | --- | --- | --- |
| N-TR01-12-01 | “Il fabbisogno parte dal problema pubblico da risolvere, non dal prodotto desiderato.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-01` | T: fabbisogno; A: baseline; O: strategia | d.lgs. 36/2023, art. 1 e allegati progettazione | FAIL — fonte atomica assente dal manifest. |
| N-TR01-12-02 | “Un requisito funzionale descrive ciò che il sistema deve fare.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-02` | T: requisito; A: capitolato; O: requisito testabile | d.lgs. 36/2023 | FAIL — nessuna verifica atomica. |
| N-TR01-12-03 | “Lo SLA è l'impegno contrattuale sul livello di servizio. Lo SLI è l'indicatore osservato.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-03` | T: SLA/SLI; A: misura; O: report servizio | d.lgs. 36/2023 | FAIL — terminologia operativa da fonte contrattuale/editoriale, non promossa. |
| N-TR01-12-04 | “Il RUP, responsabile unico del progetto, presidia il progetto secondo la disciplina applicabile.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-04` | T: ruoli; A: esecuzione; O: evidenze | d.lgs. 36/2023, art. 15 | FAIL — verificare formulazione e ruolo DEC nel testo vigente prima della promozione. |
| N-TR01-12-05 | “La formula «il fornitore garantisce la sicurezza» non definisce una prestazione verificabile.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-05` | T: sicurezza; A: supply chain; O: controllo verificabile | d.lgs. 36/2023; Reg. 2016/679, art. 28 | FAIL — fonte da assegnare per singola evidenza. |
| N-TR01-12-06 | “Correzione di un difetto, manutenzione ordinaria, evoluzione funzionale, variazione del perimetro e modifica contrattuale non sono sinonimi.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-06` | T: modifiche; A: rilascio; O: classificazione | d.lgs. 36/2023, art. 120 | FAIL — mantenere distinzione ma senza attestation. |
| N-TR01-12-07 | “La portabilità consente di trasferire dati, applicazioni o carichi in un altro ambiente.” | `chapters/12-procurement-ict-gestione-fornitori.md#n-tr01-12-07` | T: portabilità; A: exit; O: exit plan/test | d.lgs. 36/2023; Reg. 2016/679, art. 20 (solo dati personali) | FAIL — non estendere l'art. 20 a ogni rapporto ICT. |

## Capitolo 13 — Laboratorio prove ICT

Le fonti qui sono per natura doppie: **primaria** = bando, avvisi, istruzioni e criteri della procedura concreta (oltre al d.P.R. 487/1994 per il quadro generale); **editoriale** = `sources/campione-bandi-ict-pa-vol-08-2024-2026`, `sources/simulazioni-concorsuali-metodo-bando`, `sources/risposta-sintetica-domande-aperte-metodo-bando`, `sources/strategia-punteggio-prova-concorsuale-metodo-bando`, `sources/revisione-finale-risposta-concorsuale-metodo-bando`, `sources/schema-universale-risposta-orale-metodo-bando`. Nessuna fonte editoriale è una fonte primaria per regole, punteggi o criteri della singola selezione.

| ID | Quote letterale completa | sourceLocation | T/A/O | Fonte primaria / editoriale | Esito / correzione |
| --- | --- | --- | --- | --- | --- |
| N-TR01-13-01 | “Formato, durata, punteggio, soglia, penalità e strumenti ammessi devono essere ricavati dal bando e dalle comunicazioni ufficiali.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-01` | T: regole; A: decoder; O: piano prova | d.P.R. 487/1994 + bando; editoriale: campione bandi | FAIL — serve atto della procedura, non solo campione. |
| N-TR01-13-02 | “La decisione se rispondere a un quesito incerto dipende dalle regole effettive, non da formule universali.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-02` | T: quiz; A: distrattori; O: regola decisione | Bando/istruzioni; editoriale: simulazioni | FAIL — fonte primaria individuale assente. |
| N-TR01-13-03 | “La qualità di una risposta breve dipende dalla selezione. Il nucleo richiesto deve emergere attraverso un ordine riconoscibile.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-03` | T: risposta; A: scaletta; O: testo breve | Bando/criteri; editoriale: risposta sintetica | FAIL — metodo editoriale, non criterio ufficiale. |
| N-TR01-13-04 | “Un elaborato tecnico collega bisogno, vincoli, soluzione, rischi ed evidenze.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-04` | T: elaborato; A: progetto; O: elaborato verificabile | Bando/traccia; editoriale: strategia punteggio | FAIL — non attribuire valore valutativo ufficiale senza criteri pubblicati. |
| N-TR01-13-05 | “All'orale devi rendere udibile la struttura. Apri delimitando il concetto, sviluppa due o tre passaggi e chiudi sulla conseguenza.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-05` | T: orale; A: esposizione; O: risposta | d.P.R. 487/1994 + atti; editoriale: schema orale | FAIL — struttura editoriale non fonte primaria. |
| N-TR01-13-06 | “Per una diagnosi usa sintomo → ipotesi → evidenza → test → esito → azione.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-06` | T: caso; A: diagnosi; O: sequenza decisionale | Traccia; editoriale: simulazioni | FAIL — traccia concreta richiesta per attestation. |
| N-TR01-13-07 | “Il totale permette di confrontare le tue simulazioni. Non può prevedere il voto della commissione.” | `chapters/13-laboratorio-prove-ict.md#n-tr01-13-07` | T: autocorrezione; A: rubrica; O: diario errori | Criteri pubblicati; editoriale: revisione finale | FAIL — rubrica esplicitamente non equiparabile alla commissione. |

## Riepilogo fail-closed

- Record esaminati: **28**; record promossi: **0**; FAIL aperti: **28**.
- Ogni record ha `reviewer: codex-step15-batch-c`, `gateId: step-15`, `cutoff: 2026-08-12`; tali campi sono qui documentali e **non** sostituiscono le attestazioni del manifest.
- Correzione necessaria prima di qualsiasi passaggio a `verified`: inserire nel manifest un record per nucleo con la stessa quote, stessa `sourceLocation`, fonte specifica e reviewer, dopo verifica umana/editoriale delle affermazioni normative; per cap. 13 allegare l'atto della procedura concreta quando si afferma una regola di prova.
