# Report editoriale — Riscossione nazionale e lavoro in AdER

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili di Agenzia delle entrate-Riscossione e, più in generale, ai profili che richiedono conoscenze sulla riscossione nazionale.
- Perimetro di questa revisione: capitolo 07, matrice M-FC02, rinvio della matrice VOL-03, source note consolidate, capitoli adiacenti e apparati didattici e visuali dichiarati.
- Stato generale in una frase: capitolo strutturalmente completo e didatticamente solido, pubblicabile dopo il ripristino delle figure, la normalizzazione ortografica e la review normativa al cut-off.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, perché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Frontmatter `asset_refs` e intero corpo | Note, richiami, impaginazione e layout | Media | I cinque PNG esistono e sono dichiarati nel frontmatter, ma nessuna figura è richiamata nel corpo dopo il consolidamento. Il lettore perde mappe già progettate per cinque passaggi didattici. | Reinserire ogni figura accanto alla sezione pertinente: Mappa BANDO; accertamento/riscossione; flusso ruolo-cartella; rateizzazione/sospensione; checklist front-office. Verificare didascalie e resa KDP. | Aperto |
| E02 | Intero capitolo, in particolare parr. 34-242 | Ortografia e qualità editoriale | Media | Il testo usa sistematicamente grafie ASCII al posto degli accenti (`e'`, `puo`, `gia`, `piu`, `legalita`, `modalita`, `perche`, `ne` per `né`). La comprensione resta integra, ma la forma non è adatta alla pubblicazione. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| V01 | Parr. 104-113, `Dato mobile 2026` | Accuratezza normativa e fattuale | Media | La soglia di 120.000 euro e il massimo di 84 rate per le richieste 2025-2026 sono dati mobili, correttamente segnalati ma non verificati in questa revisione sul testo ufficiale al cut-off. | Verificare art. 19 D.P.R. 602/1973, D.Lgs. 110/2024 e provvedimenti/istruzioni AdER vigenti; registrare data ed esito. | Da verificare |
| V02 | Parr. 115-123 e caso guidato | Accuratezza normativa e fattuale | Media | Termine di sessanta giorni, cause tassative, flusso AdER-ente creditore ed effetti della sospensione legale richiedono controllo puntuale sulla disciplina vigente. | Verificare legge 228/2012, testo vigente, modulistica e istruzioni ufficiali AdER; controllare anche la formulazione dell'effetto sospensivo nel caso. | Da verificare |
| V03 | Parr. 63-69 e 163-180 | Accuratezza istituzionale e lavoro | Media | Natura, controllo, organi di AdER e quadro del rapporto di lavoro sono coerenti con le source note, ma regolamento di selezione, avviso e CCNL dipendono dall'edizione e dal bando assunto a riferimento. | Confermare assetto istituzionale, regolamento, CCNL, profilo e mansioni sul bando e sui documenti ufficiali selezionati per l'edizione. | Da verificare |
| V04 | Parr. 125-161 | Accuratezza normativa e fattuale | Media | Fermo, ipoteca e pignoramento sono distinti correttamente a livello funzionale, ma presupposti quantitativi, comunicazioni preventive, esclusioni e limiti non sono verificati articolo per articolo. | Eseguire review sul D.P.R. 602/1973 vigente e sulle istruzioni ufficiali; mantenere nel corpo soltanto dati confermati e datati. | Da verificare |
| E03 | Par. 195-196 | Layout Markdown | Lieve | Manca una riga vuota tra il paragrafo conclusivo e l'H3 `Mappa anti-confusione`; alcuni renderer possono gestire il passaggio in modo meno stabile. | Inserire una riga vuota prima dell'H3 e verificare il render. | Aperto |

## 4. Osservazioni per capitolo
### Capitolo 07 — Riscossione nazionale e lavoro in AdER
- Punti di forza: la progressione separa ente creditore e agente della riscossione, quindi distingue percorso a ruolo e accertamento esecutivo; rateizzazione, sospensione, sgravio e ricorso hanno funzioni e competenze riconoscibili; misure cautelari ed esecuzione sono spiegate prima del caso; front-office e back-office sono collegati a identificazione, documenti, riservatezza e tracciabilità. Mappa BANDO, tabelle, casi, esercizio, quiz, diario e checklist applicano teoria già esposta. I sei nuclei assegnati dalla matrice risultano completi.
- Criticità: non emergono errori concettuali certi o promesse didattiche scoperte. E01 ed E02 richiedono un intervento editoriale prima della pubblicazione; V01-V04 richiedono review normativa e istituzionale; E03 è una rifinitura di layout.

## 5. Coerenza globale
- Terminologia: coerente. Accertamento, riscossione, ruolo, carico, cartella, presa in carico, rateizzazione, sospensione, sgravio e ricorso non sono usati come sinonimi.
- Struttura vs indice: coerente. Il capitolo segue la sequenza istituzione-fasi-atti-strumenti-recupero-lavoro e mantiene un solo corpo editoriale. La gerarchia H1/H2/H3 è leggibile; il rilievo E03 è locale.
- Promesse dell'introduzione mantenute: sì. Tutti i sei obiettivi hanno spiegazione, applicazione e verifica.
- Copertura v4 e rinvii: i nuclei assegnati nella matrice M-FC02 sono `completo`. La riga AdER della matrice VOL-03 resta `rinviato` verso il paragrafo 3 del capitolo 07, con destinazione precisa. I rinvii al VOL-01 per procedimento amministrativo, pubblico impiego, privacy e metodo dei casi evitano di duplicare il nucleo comune. Non occorre aggiornare le matrici.

## 6. Contenuto da verificare
- Art. 1 D.L. 193/2016, legge di conversione 225/2016 e assetto istituzionale vigente di AdER.
- Art. 19 D.P.R. 602/1973, D.Lgs. 110/2024, soglia di 120.000 euro, 84 rate e regime 2025-2026.
- Legge 228/2012: termine di sessanta giorni, cause ammesse, flusso di verifica ed effetti della sospensione legale.
- D.P.R. 602/1973 e D.Lgs. 112/1999 per ruolo, cartella, accertamento esecutivo, presa in carico, fermo, ipoteca e pignoramento.
- Regolamento di selezione, CCNL, profilo, mansioni e avviso AdER assunto come riferimento editoriale.
- Resa delle cinque figure, delle tabelle e delle checklist nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare, dopo la verifica normativa, se trasformare il box `Dato mobile 2026` in una scheda di aggiornamento con data di controllo ben visibile.
- Nel render KDP, evitare che le cinque figure formino una sequenza decorativa: ciascuna deve seguire il passaggio teorico che sintetizza.
- Valutare una numerazione grafica distinta per il caso sulle misure cautelari e per il caso principale sulla somma già pagata.

## 8. Priorità degli interventi
1. Chiudere V01-V04 sulle fonti ufficiali vigenti al cut-off editoriale.
2. Ripristinare nel corpo i cinque asset e controllarne didascalie, posizione e leggibilità KDP (E01).
3. Normalizzare accenti e grafie italiane in tutto il capitolo (E02).
4. Correggere la spaziatura Markdown e svolgere il preflight del PDF (E03).
5. Valutare solo dopo i controlli obbligatori i suggerimenti grafici facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, esempi, verifiche, fonti e rinvii non presentano errori gravi o bloccanti. La pubblicazione richiede tuttavia la review normativa dei dati mobili, il ripristino delle figure e la normalizzazione ortografica indicati in E01-E02 e V01-V04.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, le matrici, le source note presenti nel repository, i riferimenti incrociati e l'esistenza fisica dei cinque asset. Non ha svolto una nuova verifica web articolo per articolo delle fonti ufficiali al 30 luglio 2026, non ha confrontato un bando/CCNL definitivo e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana tributaria e produttiva prevista dal progetto.