# Report editoriale — Catasto, cartografia, estimo e pubblicità immobiliare

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili tecnici e amministrativi dell'Agenzia delle Entrate — Territorio e Servizi di pubblicità immobiliare.
- Perimetro di questa revisione: capitolo 10, matrice M-FC02, raccordo con la matrice VOL-03, source note consolidate, apparati didattici e cinque asset visuali.
- Stato generale in una frase: capitolo completo, coerente e didatticamente autonomo, pubblicabile dopo normalizzazione ortografica e review tecnica, estimativa, civilistica e operativa al cut-off.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, poiché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero capitolo, frontmatter e corpo | Ortografia e qualità editoriale | Media | Il testo alterna grafie ASCII (`e'`, `unita`, `pubblicita`, `proprieta`, `puo`, `continuita`) e forme correttamente accentate introdotte nelle revisioni recenti. L'alternanza è diffusa e non è adatta alla pubblicazione. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| E02 | Frontmatter | Uniformità editoriale e metadati | Lieve | `updated_at` è fermo al 18 luglio 2026, mentre il capitolo incorpora interventi successivi; `review_required: true` è coerente con le verifiche ancora aperte, ma data e stato dovranno essere riallineati al termine della review umana. | Aggiornare `updated_at` e lo stato di review soltanto quando le verifiche V01-V05 saranno chiuse e registrate. | Proposto |
| V01 | §§ 1-8 e note di review | Accuratezza tecnica e catastale | Media | Natura del catasto, classamento, rendita, DOCFA, PREGEO, voltura, Docte e cartografia sono coerenti con le source note, ma versioni, specifiche, canali e poteri di controllo non sono stati verificati sulle istruzioni ufficiali vigenti al cut-off. | Verificare D.M. 701/1994, istruzioni e specifiche correnti di DOCFA, PREGEO, Voltura Web, Docte e Sister; registrare data ed esito. | Da verificare |
| V02 | §§ 8-10 ed esempio numerico | Accuratezza estimativa e OMI | Media | Principi estimativi, calcolo didattico e distinzione fra rendita, OMI e stima sono internamente coerenti; cadenza, classificazioni, unità di misura e modalità di consultazione OMI restano dati operativi mobili. | Sottoporre procedimenti e terminologia a revisore estimativo e confrontare la sezione OMI con le istruzioni ufficiali vigenti. | Da verificare |
| V03 | §§ 11-13 | Accuratezza civilistica | Media | Trascrizione, iscrizione, annotazione, continuità ed effetti della pubblicità sono presentati correttamente a livello generale, ma le singole fattispecie e formule sugli effetti richiedono controllo puntuale sul codice civile e sulla disciplina vigente. | Verificare le categorie e gli effetti delle formalità sulle fonti civilistiche vigenti, mantenendo distinto il livello introduttivo dalle eccezioni. | Da verificare |
| V04 | §§ 13-14 | Accuratezza operativa e istituzionale | Media | Modalità di ispezione, copertura dei periodi pre-automazione, competenza territoriale, certificazioni e attività degli uffici possono variare in base a servizi, canali e organizzazione corrente. | Confrontare il testo con i servizi ufficiali dell'Agenzia e con il bando/profilo assunto per l'edizione. | Da verificare |
| V05 | Caso guidato e domanda-trappola | Accuratezza edilizio-urbanistica | Media | Il limite della conformità catastale rispetto alla regolarità edilizia è formulato prudentemente, ma i requisiti da verificare in sede di atto e le discipline applicabili non sono sviluppati perché esterni al nucleo del capitolo. | Confermare il raccordo con la disciplina edilizio-urbanistica vigente e mantenere esplicito il limite di perimetro. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 10 — Catasto, cartografia, estimo e pubblicità immobiliare
- Punti di forza: la progressione separa con chiarezza dato catastale, rappresentazione cartografica, giudizio estimativo e pubblicità immobiliare. DOCFA, PREGEO, voltura e Docte sono confrontati per oggetto, presupposto, output e limite; l'esempio estimativo svolge un calcolo verificabile senza trasformare OMI in perizia. Il caso guidato, le differenze da non confondere, le domande, il mini-esercizio, il quiz, il glossario, il diario e la checklist applicano teoria già esposta. I sette nuclei assegnati dalla matrice risultano completi.
- Criticità: non emergono errori concettuali certi o lacune didattiche bloccanti. E01 richiede una normalizzazione diffusa prima della pubblicazione; E02 va chiuso insieme alla review umana. V01-V05 richiedono verifica specialistica. Le cinque figure esistono, sono numerate in ordine e collocate accanto ai passaggi pertinenti.

## 5. Coerenza globale
- Terminologia: coerente nelle distinzioni fondamentali: catasto e registri immobiliari; rendita, quotazione OMI e stima; mappa e planimetria; voltura e trasferimento; trascrizione, iscrizione e annotazione. Resta soltanto l'alternanza grafica indicata in E01.
- Struttura vs indice: coerente. Il capitolo mantiene un solo corpo editoriale, un solo H1 e una gerarchia H2/H3 leggibile. Le Figure 10.1-10.5 seguono l'ordine di lettura.
- Promesse dell'introduzione mantenute: sì. I nove obiettivi trovano spiegazione, applicazione e verifica; nessun nucleo risulta solo nominato, parziale o mancante.
- Copertura v4 e rinvii: le righe 74-80 della matrice M-FC02 sono `completo` e corrispondono al contenuto reale. La matrice di volume non assegna a questo capitolo rinvii autonomi da correggere; il modulo resta correttamente specialistico e non duplica il nucleo comune del VOL-01. Non occorre declassificare le matrici.

## 6. Contenuto da verificare
- D.M. 701/1994, classamento e poteri/termini di controllo.
- Versioni, specifiche e canali correnti di DOCFA, PREGEO, Voltura Web, Docte e Sister.
- Cartografia catastale, sistemi di riferimento e limiti tecnici delle trasformazioni.
- Procedimenti estimativi, terminologia e correttezza specialistica dell'esempio.
- Banca dati OMI: cadenza, zone, tipologie, stati, unità di superficie e modalità di consultazione.
- Disciplina civilistica di trascrizione, iscrizione, annotazione e continuità.
- Servizi di ispezione, registri pre-automazione, competenza territoriale e certificazioni.
- Raccordo tra conformità catastale e disciplina edilizio-urbanistica vigente.
- Bando, profilo, organizzazione e mansioni degli uffici assunti per l'edizione.
- Resa delle cinque figure, delle tabelle e della checklist nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare, dopo la review tecnica, una scheda digitale separata per versioni software, canali e specifiche operative mobili.
- Nel render KDP, evitare che la tabella delle procedure e quella sulle formalità si spezzino tra pagine.
- Valutare un richiamo grafico comune per la sequenza `domanda → banca dati o procedura → output → limite`.

## 8. Priorità degli interventi
1. Chiudere V01-V05 sulle fonti ufficiali e con i revisori specialistici al cut-off editoriale.
2. Normalizzare accenti e grafie italiane nell'intero capitolo (E01).
3. Riallineare data e stato di review nel frontmatter dopo la chiusura delle verifiche (E02).
4. Eseguire il preflight del PDF KDP, con particolare attenzione a cinque figure e tabelle.
5. Valutare soltanto dopo i controlli obbligatori i suggerimenti facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, apparati, figure e coerenza terminologica non presentano errori gravi o blocker. Prima della pubblicazione occorrono tuttavia la review specialistica V01-V05, la normalizzazione ortografica E01 e il riallineamento finale dei metadati E02.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, le matrici, le source note presenti nel repository, i riferimenti incrociati e l'esistenza dei cinque asset. Non ha svolto una nuova verifica web articolo per articolo delle fonti ufficiali al 30 luglio 2026, non ha sostituito la review tecnica, estimativa, civilistica o edilizio-urbanistica e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana specialistica e produttiva prevista dal progetto.
