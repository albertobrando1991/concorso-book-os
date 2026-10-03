# Audit specialistico conclusivo M-FC02 — 3 ottobre 2026

## 1. Sintesi editoriale

Riesaminati i claim specialistici del candidato fiscale dopo le 23 correzioni dell’audit integrale. Il controllo parte dalla lettura integrale dei 16 capitoli e di quiz/casi del 2 ottobre, confronta le modifiche attuali e ricontrolla norme, soglie e applicazioni interessate. Individuati e corretti anche due residui nel passaggio dal TU futuro al processo vigente. Nessun rinvio a una successiva revisione umana del testo; la verifica del PDF resta un distinto gate di produzione.

## 2. Perimetro e metodo

Controllati: qualificazioni degli enti; principi tributari e UE; accertamento/garanzie; TUIR e dichiarazioni; sanzioni e processo; riscossione; dogane/accise; estimo/pubblicità; bilancio e civile. Estrazione dei claim numerici e dei riferimenti articolo per articolo conservata negli artefatti; rilettura in contesto dei passaggi corretti. I quiz preesistenti restano quelli risolti nell’audit integrale; le correzioni non cambiano chiavi o ordine delle opzioni. Nuovi casi numerici e calendario ricalcolati separatamente. Nessun box Dato operativo di formato 2 è presente nel modulo, come attesta il prompt generato dalla pipeline.

## 3. Rilievi ed esiti conclusivi

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| FC02-S01 | 05b, mappa normativa e prova | Norma | Grave | Restavano numerazione del TU e due occorrenze «546/1992 175». | Mappa 545/546, articoli 1–70 secondo il decreto processuale; onere della prova art. 7, comma 5-bis. Fonte ufficiale integrale 546 acquisita e nota rettifica processo. | Corretto e verificato |
| FC02-S02 | 05b, notificazione e deposito | Coerenza | Media | Una frase dichiarava assenti i termini già inseriti. | Richiamo coerente 60/30/60; calendario 2 marzo–4 maggio e 20 aprile–20 maggio ricalcolato. | Corretto e verificato |
| FC02-S03 | 07, sospensione legale | Procedura | Media | Formula generica sull’atto notificato. | Precisati agente notificante, domanda non ripetibile, esclusioni per avviso impositivo e sollecito ordinario. Fonte AdER Sospensione, riletta il 3 ottobre. | Corretto e verificato |
| FC02-S04 | 03, nota sugli organigrammi | Testo lettore | Media | Residuo «prima della pubblicazione definitiva». | Istruzione di studio collegata a statuto/organigramma alla data del bando; regolamento ADM 541/2026 riscontrato sul portale ufficiale. | Corretto e verificato |
| FC02-S05 | 01–14 e 05a/05b | Ortografia e rimandi | Media | Grafie residue perciò/infedeltà/né e ancore da verificare dopo pulizia. | Correzioni contestuali; zero file o titoli di destinazione mancanti. Test retrofit FC02 2/2 superati. | Corretto e verificato |
| FC02-S06 | Delta dei 23 ID V03 | Specialistica | Grave | Verifica delle integrazioni normative e didattiche prima del freeze. | Fonti primarie e casi verificati come indicato sotto; mantenuti presupposti e distinzioni, senza sopprimere materia. | Corretto e verificato |

## 4. Riscontri per area

- **Processo:** D.Lgs. 545 e 546 nel 2026, TU 175 dal 2027; territorio art. 4, difesa fino a 3.000, ricorso/costituzione 60/30/60, feriale, appelli 60 giorni/sei mesi; art. 7, comma 5-bis e cautela con danno grave e irreparabile. Evidenze nella nuova source note e PDF ufficiale acquisito.
- **Accertamento e sanzioni:** artt. 38–41 D.P.R. 600/1973; 6-bis e 10-quater/quinquies Statuto; TCF 500 milioni dal 2026; D.Lgs. 472/1997, art. 2, comma 2-bis; D.Lgs. 74/2000 e modifiche 87/2024. Distinti soglia ordinaria/residua e regime futuro. Fonti Gazzetta/MEF e circolare AE 6/E 2026 nelle note.
- **Redditi:** AKN TUIR già acquisito, letti gli artt. 45, 49, 51, 54, 66 e 109; confronto con art. 51 corrente MEF. Cassa, competenza, pensioni e deroghe non ridotte a un'unica regola. D.P.R. 322/1998: 90 giorni e diverso effetto oltre termine.
- **Riscossione:** istruzioni AdER correnti su 84 rate, 120.000 per istanza, 60 giorni sospensione, 30 giorni preavviso fermo, strumentalità e circolazione; separati ente creditore e agente.
- **Dogane/accise:** CDU artt. 134 e 173, D.Lgs. 141/2024, A.TR e libera pratica, direttiva 2020/262/EMCS; regimi sospensivi e a imposta assolta distinti. Il caso Turchia non deduce l’origine dal documento A.TR.
- **Estimo/contabilità/civile:** art. 2808 c.c.; OIC 13/16/24 e art. 2426; calcoli estimativi e margini con convenzioni dichiarate; modificazioni soggettive, patologie e responsabilità dei sei tipi societari confrontate con le note codicistiche. La regola dei terreni ammette l'utilità esauribile e non include le immobilizzazioni finanziarie nell'ammortamento.

## 5. Coerenza globale

Nessun TU anticipato nel regime 2026; riferimenti staff sostituiti con bibliografia pubblica; corretto D = Diario. La parte legittima del Decoder è integralmente conservata dopo controllo differenziale. Fonti e topic alimentano gli stessi concetti dei capitoli. I limiti dei casi sono dichiarati senza demandare la spiegazione necessaria a documenti interni.

## 6. Verifiche eseguite

Controllo normativo e tecnico delle aree sopra elencate; ricalcolo dei nuovi esempi; controllo di tutti i wikilink del corpo (zero irrisolti); test di copertura e densità del pilota FC02/04 (2/2). Gli hash dei 16 file sono nel ledger conclusivo specialistico. Non è stato prodotto un nuovo PDF in questo step.

## 7. Suggerimenti facoltativi

Nessuna ulteriore integrazione è necessaria per correggere i 23 rilievi assegnati al modulo. La frequenza dei richiami istituzionali va mantenuta nelle future edizioni in funzione della data del bando.

## 8. Priorità di produzione

Text freeze tramite CLI, successivamente export e controllo visivo del candidato. I rilievi sulle figure sono gestiti nel registro iconografico coordinato e non sono dichiarati chiusi da questo audit testuale.

## 9. Giudizio sul testo

Testo specialistico corretto per il passaggio al text freeze; zero errori gravi o medi aperti nel perimetro riesaminato. Il giudizio non attesta la pubblicabilità del PDF o la chiusura degli altri moduli del volume.

## 10. Limiti

Questo è un riesame specialistico del candidato rispetto alla baseline integralmente letta, non una dichiarazione di nuova lettura pagina per pagina del PDF. Non si attesta aggiornamento automatico dopo il 3 ottobre 2026. Nomi dei titolari degli uffici, aliquote annuali non necessarie ai casi e calendari di bandi aperti non sono inventati per ampliare il perimetro.


### Riesame specialistico del delta grafico, 3 ottobre 2026

Riesaminati i 70 schemi rispetto ai 70 originali, al contesto dei capitoli e alla nuova nota ol-03-schemi-fiscali-verifica-2026-10-03. P03-05/06/07 sono corretti semanticamente: BANDO e appendici coerenti, alternative esplicite, liquidazione periodica distinta dalla dichiarazione annuale, riscossione ordinaria distinta dall’accertamento esecutivo, EORI distinto da AEO e AEO dal singolo controllo, AE/ADM/AdER distinti per funzione. Qualificati il bilancio ordinario e i rapporti contabili senza cronologie obbligatorie. Il solo capoverso aggiuntivo IVA elimina il medesimo automatismo nel testo.

Verifica di preservazione: 14 hash iniziali corrispondono al freeze; invertendo i 70 schemi e il capoverso dichiarato il corpo coincide integralmente con lo snapshot. Casi, quiz, risposte, soglie e termini restano invariati. Zero wikilink irrisolti. Nessun nuovo dato mobile non verificato; nessun errore specialistico grave o medio aperto nel delta. La leggibilità della nuova impaginazione resta controllo PDF separato, non un riesame normativo rinviato. Evidenza: VOL-03-native-checkpoint.json.
