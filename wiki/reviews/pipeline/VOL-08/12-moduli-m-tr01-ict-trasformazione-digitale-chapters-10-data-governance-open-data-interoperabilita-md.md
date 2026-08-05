# Report editoriale — Data governance, open data, interoperabilità e qualità

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale specialistico/workbook per concorsi pubblici.
- Pubblico target: candidati a profili ICT e Data/AI della pubblica amministrazione.
- Perimetro di questa revisione: capitolo 10 di M-TR01, con confronto con matrice di copertura, indice del modulo, capitoli 4, 6 e 9, nucleo comune del VOL-01 e fonti consolidate.
- Stato generale in una frase: capitolo didatticamente autonomo e ben strutturato; una promessa su trasparenza e accesso era incompleta ed è stata risolta, mentre restano interventi trasversali e verifiche specialistiche non bloccanti.

## 2. Punti applicati della checklist
1. Indice: applicato; l'indice del modulo è ancora allo stato di scaffold (E04).
2. Struttura del libro: applicato al raccordo tra capitoli 4, 6, 9 e 10 e con il VOL-01.
3. Progressione logica: applicato; sequenza governance-ruoli-ciclo di vita-metadati-qualità-apertura-interoperabilità coerente.
4. Gerarchia dei titoli: applicato; un solo H1, H2 e H3 coerenti.
5. Idoneità alla pubblicazione: applicato; esito al § 9.
6. Coerenza interna: applicato; corretta la promessa non mantenuta in E01.
7. Coerenza tra capitoli: applicato; i rinvii tecnici evitano la duplicazione dei capitoli 4, 6 e 9.
8. Coerenza terminologica: applicato; corretti E02-E03.
9. Completezza delle spiegazioni: applicato; nuclei completi dopo E01.
10. Accuratezza delle definizioni: applicato; distinzioni centrali corrette nei limiti delle fonti consolidate.
11. Errori concettuali: applicato; nessun errore certo residuo.
12. Errori normativi/contenutistici: applicato; verifiche V01-V03.
13. Esempi: applicato; caso comunale coerente con teoria e strumenti.
14. Tabelle, box e schemi: applicato; inventario, RACI, qualità e albero decisionale pertinenti.
15. Apparato bibliografico/normativo: applicato; source note specialistica presente e collegata.
16. Sintassi: applicato; chiara dopo Humanizer.
17. Chiarezza espositiva: applicato; corretta la formula ellittica di E03.
18. Tono editoriale: applicato; sobrio e professionale.
19. Stile didattico: applicato; teoria, caso, strumenti e verifiche sono distinti.
20. Ripetizioni inutili: applicato; nessuna ripetizione rilevante.
21. Contraddizioni: applicato; nessuna contraddizione interna residua.
22. Grammatica: applicato; nessun errore rilevante.
23. Ortografia: applicato; nessun errore rilevante.
24. Punteggiatura: applicato; corretta e leggibile.
25. Refusi: applicato; corretti E02-E03.
26. Uniformità grafica: applicato; corsivi e grassetti hanno funzione coerente.
27. Impaginazione: non applicabile; non è disponibile un PDF impaginato.
28. Layout: applicato nei limiti del Markdown; tabelle da verificare nel formato KDP.
29. Leggibilità complessiva: applicato; paragrafi brevi e progressione chiara.
30. Qualità editoriale complessiva: applicato.

Gate aggiuntivo di copertura didattica integrale: applicato. Governance, ruoli, ciclo di vita, inventario, catalogo, glossario, lineage, metadati, qualità, open data, riuso e interoperabilità sono completi. L'integrazione E01 distingue ora anche pubblicazione web, trasparenza, accesso e open data. La matrice resta correttamente classificata `completo`.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | «Open data e riuso» | Copertura didattica integrale | Grave | L'obiettivo prometteva di distinguere pubblicazione web, trasparenza e accesso dagli open data, ma il corpo non spiegava le prime tre nozioni. | Inserire una distinzione teorica esplicita prima di applicarla al caso e alle domande-trappola. L'integrazione è stata applicata usando le fonti consolidate. | Risolto |
| E04 | `index.md`, «Capitoli di lavoro» | Struttura/indice | Media | L'indice del modulo elenca soltanto il piano editoriale e mantiene lo stato `scaffold`, mentre dieci capitoli sono già in sviluppo o revisione. | Rigenerare l'indice nella fase trasversale, elencare i capitoli reali e aggiornare stato e `draft_stage`. | Aperto |
| E05 | «Open data e riuso» | Rinvio cross-volume | Media | La distinzione tra trasparenza e accesso è ora autonoma, ma manca un rinvio diretto al nucleo comune che sviluppa disciplina e tipologie di accesso. | Aggiungere un rinvio preciso a VOL-01, capitolo 7 «Trasparenza, anticorruzione e privacy», §§ 1-6 e § 19, senza duplicarne la teoria. | Aperto |
| E06 | Tabelle e strumenti | Layout | Media | Le tabelle sono leggibili in Markdown, ma quella di inventario e gli strumenti compilabili non sono stati provati nella gabbia paperback KDP. | Eseguire il test nel Book Studio; dividere le tabelle se il corpo scende sotto lo standard editoriale. | Da verificare |
| E02 | Titolo «Formato, macchina, licenza e accessibilità» | Terminologia | Lieve | «Macchina» era un'abbreviazione impropria rispetto al termine tecnico usato nel corpo. | Sostituire con «leggibilità meccanica». | Risolto |
| E03 | «Domande-trappola», PDF online | Chiarezza/refuso | Lieve | La risposta «consultabilità, macchina, licenza» era ellittica e poco naturale. | Sostituire «macchina» con «leggibilità meccanica». | Risolto |

## 4. Osservazioni per capitolo
### Capitolo 10 — Data governance, open data, interoperabilità e qualità
- Punti di forza: progressione logica solida; distinzione netta tra decisione organizzativa e attuazione tecnica; ruoli presentati come modelli e non come qualifiche normative; qualità tradotta in regole e metriche; caso comunale realistico; esercizi con soluzioni; fonti AgID e UE consolidate.
- Criticità: indice generale del modulo obsoleto; rinvio al nucleo comune su trasparenza e accesso da rendere cliccabile e preciso; layout degli strumenti non ancora verificato; fonti mobili da ricontrollare al text freeze.
- Copertura v4: collocazione corretta nella famiglia ICT/Data; nessuna duplicazione sostanziale del B-PA. Il rinvio al capitolo 6 mantiene qui il presidio organizzativo e lascia API, ModI, PDND ed e-service alla sede tecnica. Stato complessivo: `completo`.

## 5. Coerenza globale
- Terminologia: coerente per governance, gestione, architettura, owner, steward, custodian, inventario, catalogo, glossario, lineage, dataset, distribuzione e interoperabilità. Le correzioni E02-E03 uniformano «leggibilità meccanica».
- Struttura vs indice: la struttura del capitolo corrisponde al piano e alla matrice; l'indice del modulo è obsoleto (E04).
- Promesse dell'introduzione mantenute: sì, dopo E01. Ogni promessa ha spiegazione, applicazione o rinvio preciso; E05 migliora il raccordo, ma non sostituisce teoria mancante.
- Rinvii: corretti quelli ai capitoli 4, 6 e 9; da aggiungere il rinvio editoriale al VOL-01 indicato in E05.

## 6. Contenuto da verificare
- V01 — Ricontrollare al text freeze versione vigente delle Linee guida AgID sugli open data, profilo DCAT-AP_IT, cataloghi e licenze richiamati.
- V02 — Verificare sull'allegato del regolamento di esecuzione (UE) 2023/138 l'appartenenza di eventuali dataset concreti alle serie di elevato valore e le relative modalità di pubblicazione.
- V03 — Verificare il campo applicativo del regolamento (UE) 2024/903 prima di attribuire valutazioni o adempimenti a uno specifico progetto o ente.
- V04 — Far validare ruoli, regole di qualità, lineage e catalogazione da uno specialista data governance/data quality.
- V05 — Far validare pubblicazione, anonimizzazione, comunicazione e diffusione da giurista del dato pubblico e DPO; accessi e classificazione da security architect.

## 7. Suggerimenti facoltativi (non errori)
- Valutare una pagina staccabile che unisca inventario, scheda dataset e registro delle anomalie.
- Valutare un esempio compilato di glossario con tre termini dello stesso dominio.
- Nell'impaginato, usare una legenda grafica stabile per distinguere uso interno, condivisione, interoperabilità e open data.

## 8. Priorità degli interventi
1. E01 è stato risolto: mantenere la distinzione teorica introdotta.
2. Aggiungere il rinvio preciso al VOL-01 (E05).
3. Aggiornare l'indice del modulo nella revisione trasversale (E04).
4. Eseguire preflight degli strumenti nel formato KDP (E06).
5. Chiudere le verifiche V01-V05 prima del text freeze.

## 9. Giudizio di pubblicabilità
**Pubblicabile dopo intervento medio.**
Motivazione: il blocker di copertura E01 è stato risolto e la matrice può restare `completo`. Restano due interventi editoriali medi, un controllo di layout e verifiche normative/specialistiche che non richiedono una riscrittura strutturale, ma devono essere chiusi prima della pubblicazione.

## 10. Limiti di questa revisione
La revisione riguarda il capitolo Markdown, la matrice, l'indice e i raccordi disponibili. Non è stato ispezionato un PDF impaginato né eseguito il preflight KDP. La verifica normativa si è basata sulle source note consolidate e sulle fonti ufficiali già acquisite nello step 09; non sostituisce il controllo giuridico finale sulle versioni vigenti. Gli altri capitoli sono stati consultati soltanto per i rinvii necessari, non sottoposti nuovamente a revisione integrale.
