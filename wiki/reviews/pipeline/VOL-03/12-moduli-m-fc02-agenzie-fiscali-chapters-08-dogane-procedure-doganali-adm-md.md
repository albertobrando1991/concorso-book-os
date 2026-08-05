# Report editoriale — Dogane e procedure doganali: il lavoro ADM

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili dell'Agenzia delle dogane e dei monopoli e ai profili che richiedono conoscenze di diritto doganale.
- Perimetro di questa revisione: capitolo 08, matrice M-FC02, rinvii della matrice VOL-03, source note consolidate, apparati didattici e cinque asset visuali.
- Stato generale in una frase: capitolo completo, coerente e didatticamente efficace, pubblicabile dopo la normalizzazione editoriale, il riordino delle figure e la review normativa al cut-off.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, poiché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero capitolo, in particolare parr. 38-362 | Ortografia e qualità editoriale | Media | Il corpo usa diffusamente grafie ASCII al posto degli accenti (`e'`, `puo`, `gia`, `piu`, `perche`, `modalita`), mentre alcune integrazioni recenti impiegano gli accenti corretti. L'alternanza è visibile e non è adatta alla pubblicazione. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| E02 | Figure 8.3-8.5, parr. 134-232 | Impaginazione e richiami visuali | Media | La Figura 8.5 compare prima delle Figure 8.3 e 8.4. Gli asset sono pertinenti e incorporati, ma la sequenza numerica non coincide con l'ordine di lettura. | Spostare la checklist 8.5 dopo la Figura 8.4 oppure rinumerare in modo coordinato asset, didascalie e richiami; verificare poi la resa KDP. | Aperto |
| V01 | Parr. 68-76 e note di review | Accuratezza normativa | Media | Versione consolidata del CDU, regolamenti delegato ed esecutivo e disciplina nazionale complementare sono correttamente individuati, ma non verificati articolo per articolo al cut-off editoriale. | Verificare Reg. (UE) 952/2013, Reg. delegato 2015/2446, Reg. di esecuzione 2015/2447, D.Lgs. 141/2024 ed eventuali correttivi vigenti; registrare data ed esito. | Da verificare |
| V02 | Parr. 164-226 | Accuratezza normativa | Media | Regimi speciali, autorizzazioni, garanzie, appuramento, insorgenza del debito, debitore, estinzione, sgravio e rimborso sono esposti correttamente a livello didattico, ma richiedono riscontro puntuale sulle fattispecie vigenti. | Eseguire una review giuridica sul CDU e sugli atti integrativi, mantenendo nel testo solo formulazioni confermate. | Da verificare |
| V03 | Parr. 136-162 e caso guidato | Accuratezza normativa e operativa | Media | Classificazione TARIC, informazione tariffaria vincolante, origine preferenziale e non preferenziale, prove di origine, rettifiche del valore e metodi secondari dipendono da regole e misure aggiornabili. | Verificare nomenclatura e misure TARIC, regole di origine applicabili, accordi preferenziali e artt. CDU sul valore; datare gli esempi operativi. | Da verificare |
| V04 | Parr. 87-120 e 228-246 | Accuratezza operativa e istituzionale | Media | EORI, AEO, dichiarazioni elettroniche, analisi del rischio, controllo successivo e sistemi ADM sono descritti senza dati mobili specifici, ma procedure e tracciati possono cambiare. | Confrontare il testo con portali e manuali ufficiali UE/ADM vigenti alla data del bando; verificare anche diritto al contraddittorio e conservazione documentale. | Da verificare |
| V05 | Par. 242 e fonti sul lavoro ADM | Accuratezza istituzionale e lavoro | Media | Le attività del personale ADM sono formulate in modo prudente, ma profilo, mansioni, requisiti e disciplina del rapporto dipendono dal bando e dai documenti assunti per l'edizione. | Confermare regolamento di selezione, bando, profilo, CCNL e mansioni sulle fonti ufficiali selezionate. | Da verificare |
| E03 | Riferimenti consolidati e note di review | Coerenza delle fonti | Lieve | Il capitolo conserva sia la source note aggiornata del 17 luglio 2026 sia la precedente source note di supporto. La compresenza è utile per tracciabilità, ma non è esplicitata la gerarchia tra fonte principale aggiornata e supporto storico. | Indicare la source note del 17 luglio 2026 come riferimento operativo principale e qualificare la nota precedente come supporto; verificare che la copia raw ufficiale richiesta sia archiviata. | Aperto |

## 4. Osservazioni per capitolo
### Capitolo 08 — Dogane e procedure doganali: il lavoro ADM
- Punti di forza: la progressione va dalle fonti e dallo status delle merci al flusso dichiarativo, quindi separa con chiarezza classificazione, origine e valore; regimi, debito, garanzia e controlli sono collegati senza confonderli. Il caso principale riutilizza la sequenza teorica, mentre tabelle, domande orali, trappole, esercizio, quiz, glossario, diario e checklist verificano competenze diverse. I sette nuclei assegnati dalla matrice M-FC02 risultano completi.
- Criticità: non emergono errori concettuali certi o lacune didattiche bloccanti. E01 ed E02 richiedono un intervento editoriale prima della pubblicazione; V01-V05 richiedono review normativa, operativa e istituzionale; E03 è una rifinitura di tracciabilità delle fonti.

## 5. Coerenza globale
- Terminologia: coerente. Introduzione, presentazione, dichiarazione, accettazione e svincolo sono distinti; provenienza e origine non coincidono; regime, debito e garanzia restano su piani diversi. L'unica incoerenza editoriale è l'alternanza grafica rilevata in E01.
- Struttura vs indice: coerente. Il capitolo mantiene un solo corpo editoriale e una gerarchia H1/H2/H3 leggibile. L'ordine logico è stabile; va corretta soltanto la sequenza numerica delle figure indicata in E02.
- Promesse dell'introduzione mantenute: sì. Gli obiettivi dichiarati sono spiegati, applicati nel caso e verificati dagli apparati finali.
- Copertura v4 e rinvii: i sette nuclei doganali della matrice M-FC02 sono `completo`. Le righe 28-33 della matrice VOL-03 sono `rinviato` verso sezioni precise del capitolo 08, comprese le sezioni 9 e 10 per regimi e debito/garanzia. I rinvii al VOL-01 per procedimento, pubblico impiego, privacy e metodo dei casi evitano duplicazioni. Non occorre aggiornare le matrici.

## 6. Contenuto da verificare
- Testi consolidati del Reg. (UE) 952/2013, del Reg. delegato (UE) 2015/2446 e del Reg. di esecuzione (UE) 2015/2447.
- D.Lgs. 141/2024, correttivi e disciplina nazionale doganale vigente al cut-off.
- TARIC, informazioni tariffarie vincolanti, misure commerciali, origine preferenziale e prove applicabili agli esempi.
- Regole sul valore di transazione, rettifiche e successione dei metodi secondari.
- Regimi speciali, autorizzazioni, garanzie, appuramento, debito, debitore, sgravio e rimborso.
- EORI, AEO, sistemi dichiarativi, analisi del rischio, controllo successivo e procedure ADM.
- Regolamento di selezione, bando, CCNL, profilo e mansioni ADM assunti come riferimento editoriale.
- Resa e ordine delle cinque figure, delle tabelle e delle checklist nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare una piccola etichetta grafica ricorrente per la triade `classificazione-origine-valore`, così da renderla immediatamente riconoscibile nel caso e nel ripasso.
- Nel render KDP, mantenere la checklist della dichiarazione sulla stessa apertura della sezione 5, purché la numerazione delle figure sia resa progressiva.
- Valutare una scheda di aggiornamento datata per TARIC, sistemi telematici e misure preferenziali, separata dal nucleo stabile del capitolo.

## 8. Priorità degli interventi
1. Chiudere V01-V05 sulle fonti ufficiali vigenti al cut-off editoriale.
2. Normalizzare accenti e grafie italiane in tutto il capitolo (E01).
3. Correggere l'ordine o la numerazione delle Figure 8.3-8.5 e verificarne la resa KDP (E02).
4. Esplicitare la gerarchia tra source note aggiornata e supporto precedente, controllando l'archivio raw (E03).
5. Eseguire il preflight del PDF e valutare soltanto dopo i suggerimenti facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, casi, verifiche e rinvii non presentano errori gravi o bloccanti. La pubblicazione richiede tuttavia la review delle fonti mobili, la normalizzazione ortografica e il riordino delle figure indicati in E01-E02 e V01-V05.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, le matrici, le source note presenti nel repository, i riferimenti incrociati e l'esistenza dei cinque asset. Non ha svolto una nuova verifica web articolo per articolo delle fonti ufficiali al 30 luglio 2026, non ha confrontato un bando/CCNL definitivo e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana doganale e produttiva prevista dal progetto.
