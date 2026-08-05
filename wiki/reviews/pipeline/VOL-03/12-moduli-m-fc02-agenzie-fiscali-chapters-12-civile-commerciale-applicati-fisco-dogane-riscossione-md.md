# Report editoriale — Civile e commerciale applicati a fisco, dogane e riscossione

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili AE, ADM e AdER che devono applicare istituti civilistici e commerciali a casi fiscali, doganali e di riscossione.
- Perimetro di questa revisione: capitolo 12, matrice M-FC02, copertura v4, source note consolidate, rinvii ai capitoli 7, 8, 10 e 11, apparati didattici e cinque asset visuali.
- Stato generale in una frase: capitolo strutturalmente completo e didatticamente autonomo nel perimetro assegnato, pubblicabile dopo normalizzazione ortografica, revisione giuridica e preflight KDP.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, poiché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero capitolo, frontmatter e corpo | Ortografia e qualità editoriale | Media | Il testo usa sistematicamente grafie ASCII (`e'`, `responsabilita`, `societa`, `attivita`, `pubblicita`, `puo`) non adatte all'edizione tipografica finale. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| E02 | Frontmatter | Uniformità editoriale e metadati | Lieve | `updated_at` è fermo al 17 luglio 2026, benché il capitolo incorpori revisioni successive; `review_required: true` resta corretto finché le verifiche specialistiche sono aperte. | Aggiornare `updated_at` e lo stato di review soltanto dopo la chiusura documentata delle verifiche V01-V04. | Proposto |
| V01 | §§ 1-9 | Accuratezza civilistica | Media | Obbligazioni, mora, modificazioni soggettive, responsabilità, contratto, invalidità, garanzie e mezzi di conservazione sono coerenti con le source note, ma regimi, presupposti ed eccezioni richiedono controllo sul Codice civile vigente. | Far verificare da un revisore giuridico terminologia, coordinamenti ed eccezioni al cut-off editoriale, senza introdurre citazioni puntuali non consolidate. | Da verificare |
| V02 | §§ 10-11 | Accuratezza commerciale e societaria | Media | Categorie d'imprenditore, trasferimento d'azienda, rappresentanza commerciale, tipi societari, conferimenti, governance e responsabilità sono esposti correttamente nel livello richiesto, ma leggi speciali e regimi puntuali possono modificare la risposta. | Verificare Codice civile vigente, discipline speciali, pubblicità, responsabilità e poteri rappresentativi con revisore di diritto commerciale. | Da verificare |
| V03 | § 12 | Accuratezza sulla crisi d'impresa | Media | Il nucleo essenziale distingue crisi e insolvenza e collega gli assetti alla rilevazione tempestiva. Procedure, misure protettive ed effetti sui creditori sono correttamente esclusi, ma definizioni e coordinamento con il Codice della crisi richiedono fonte ufficiale dedicata se il bando amplia il perimetro. | Confermare il box essenziale al cut-off; prima di ogni ampliamento consolidare una source note ufficiale dedicata e sottoporla a review giuridica. | Da verificare |
| V04 | § 13 e caso guidato | Accuratezza settoriale | Media | I raccordi con AE, ADM e AdER separano correttamente piano civilistico e discipline pubblicistiche, ma poteri, responsabilità e regole settoriali dipendono dalle fonti vigenti e dal bando. | Confrontare i raccordi con le fonti ufficiali e con i capitoli 7 e 8 nell'edizione definitiva. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 12 — Civile e commerciale applicati a fisco, dogane e riscossione
- Punti di forza: la progressione parte dal rapporto giuridico, sviluppa obbligazioni, responsabilità, contratto e garanzie, quindi passa a impresa, azienda, società e crisi. Le distinzioni fra firma e imputazione, impresa e azienda, capitale e patrimonio, garanzia personale e reale sono chiare e utili in sede d'esame. Caso guidato, domanda orale, trappola, esercizio, quiz, glossario, diario e checklist applicano teoria già spiegata. I quattro nuclei assegnati dalla matrice risultano completi nel rispettivo perimetro.
- Criticità: non emergono errori concettuali certi o lacune didattiche bloccanti. E01 richiede una normalizzazione diffusa prima della pubblicazione; E02 va chiuso con la review finale. V01-V04 richiedono verifica specialistica. Le cinque figure esistono, sono numerate in ordine e collocate presso i blocchi pertinenti.

## 5. Coerenza globale
- Terminologia: coerente nelle distinzioni fra soggetto e rappresentante, credito e pagamento, responsabilità contrattuale ed extracontrattuale, nullità e annullabilità, impresa e azienda, società di persone e di capitali, crisi e insolvenza. Resta la grafia ASCII indicata in E01.
- Struttura vs indice: coerente. Il capitolo mantiene un solo H1 e una gerarchia H2/H3 leggibile. Le Figure 12.1-12.5 seguono l'ordine didattico.
- Promesse dell'introduzione mantenute: sì. I dieci obiettivi trovano spiegazione, applicazione o verifica; nessun nucleo assegnato risulta `parziale`, `solo-nominato` o `mancante`.
- Copertura v4 e rinvii: le quattro righe assegnate al capitolo 12 nella matrice M-FC02 sono `completo`. Il capitolo non duplica un corso generale di diritto privato del VOL-01 e rinvia con destinazioni precise ai capitoli 7, 8, 10 e 11 per riscossione, dogane, pubblicità immobiliare, contabilità e bilancio. Il nucleo sulla crisi copre soltanto definizioni essenziali, assetti e allerta; non promette procedure concorsuali. Non occorre declassificare la matrice.

## 6. Contenuto da verificare
- Codice civile vigente per obbligazioni, mora, responsabilità, garanzie, contratto, patologie e rimedi.
- Solidarietà, cessione, delegazione, espromissione e accollo, con relativi effetti ed eccezioni.
- Categorie d'imprenditore, trasferimento d'azienda e rappresentanza commerciale.
- Tipi societari, conferimenti, governance, autonomia patrimoniale e responsabilità personali.
- Definizioni di crisi e insolvenza e coordinamento degli assetti adeguati con il Codice della crisi.
- Raccordi con obbligazione doganale, riscossione pubblica e responsabilità per crediti pubblici.
- Resa delle cinque figure, della tabella societaria, del glossario e della checklist nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare, dopo la review giuridica, una scheda digitale separata con ulteriori casi su cessione d'azienda, rappresentanza e responsabilità societaria, senza appesantire il cartaceo.
- Nel render KDP, evitare che la tabella sulle società e il mini-esercizio si spezzino tra due pagine.
- Mantenere il nucleo sulla crisi in forma di box essenziale finché il programma del concorso non richiede espressamente procedure e strumenti.

## 8. Priorità degli interventi
1. Chiudere V01-V04 sulle fonti vigenti e con revisore giuridico al cut-off editoriale.
2. Normalizzare accenti e grafie italiane nell'intero capitolo (E01).
3. Riallineare data e stato di review nel frontmatter dopo la chiusura delle verifiche (E02).
4. Eseguire il preflight del PDF KDP, con particolare attenzione alle cinque figure, alla tabella societaria e agli apparati finali.
5. Valutare soltanto dopo i controlli obbligatori i suggerimenti facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, apparati, figure e rinvii non presentano errori gravi o blocker. Prima della pubblicazione occorrono tuttavia la review specialistica V01-V04, la normalizzazione ortografica E01 e il riallineamento finale dei metadati E02.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, la matrice M-FC02, le source note consolidate presenti nel repository, i riferimenti incrociati e l'esistenza dei cinque asset. Non ha svolto una nuova verifica web articolo per articolo delle fonti ufficiali al 30 luglio 2026, non sostituisce una review legale civilistica, commerciale, societaria, doganale o sulla crisi e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana specialistica e produttiva prevista dal progetto.
