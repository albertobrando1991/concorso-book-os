from pathlib import Path
import re
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters')
def patch(n,fn):
 p=next(B.glob(f'{n:02}-*.md')); p.write_text(fn(p.read_text(encoding='utf8')),encoding='utf8')
def before(s,m,t):
 assert m in s,m
 return s.replace(m,t.strip()+'\n\n'+m,1)
def ai(s):
 s=before(s,'## N-TR01-11-03','''### Due algoritmi svolti su piccoli dati

Un **albero decisionale** divide i dati mediante condizioni e associa una previsione alle foglie. Considera quattro ticket didattici: giorni di attesa 1, 2, 8, 9; etichette storiche «da riesaminare» 0, 0, 1, 1. Una divisione a 5 separa perfettamente i due gruppi. L'impurità di Gini iniziale è 1−(2/4)²−(2/4)²=0,5; nelle due foglie è zero. Il piccolo albero restituisce 1 per un ticket con attesa 6. La soglia è appresa confrontando separazioni sui dati etichettati: non coincide con una regola normativa scritta da un programmatore. Quattro osservazioni non provano generalizzazione; un albero molto profondo può memorizzare il training. Si limitano complessità e profondità e si misura su dati separati. L'esempio non autorizza a decidere diritti o priorità amministrative in base alla sola attesa.

Nel **k-means**, invece, mancano etichette da predire. Su dati monodimensionali 1, 2, 8, 9, scegli k=2 e centroidi iniziali 1 e 9. Assegna ciascun punto al centro più vicino: gruppi {1,2} e {8,9}. Ricalcola le medie: 1,5 e 8,5. La successiva assegnazione non cambia; la somma dei quadrati delle distanze è quattro volte 0,5², cioè 1. Il metodo alterna assegnazione e aggiornamento per ridurre tale obiettivo, ma l'esito dipende dall'inizializzazione e non garantisce il minimo globale. Scale diverse delle variabili richiedono attenzione e spesso standardizzazione; un gruppo numerico non è una categoria giuridica o una classe vera. Il numero k e l'utilità dei gruppi vanno motivati rispetto allo scopo.''')
 s=before(s,'## N-TR01-11-05','''### Matrice di confusione e calcolo completo

Su 1.000 segnalazioni, la verifica umana ne classifica 100 come urgenti. Il modello segnala 120 urgenze, 90 delle quali corrette.

| Previsione | Urgente reale | Non urgente reale |
| --- | --- | --- |
| Urgente | TP = 90 | FP = 30 |
| Non urgente | FN = 10 | TN = 870 |

La **precision** è TP/(TP+FP)=90/120=75%: tra gli allarmi, quanti sono corretti. Il **recall** è TP/(TP+FN)=90/100=90%: quante urgenze intercetto. F1=2TP/(2TP+FP+FN)=180/220≈81,82%; accuracy=(TP+TN)/1.000=96%. Un modello che risponde sempre «non urgente» raggiunge il 90% di accuracy ma recall zero sulle urgenze. Abbassare una soglia può aumentare il recall al costo di più falsi positivi: si sceglie su validation considerando carico di revisione e danno delle omissioni, poi si misura sul test senza riaggiustarla. Precision e recall dipendono dalla classe positiva dichiarata; denominatori nulli vanno gestiti esplicitamente.''')
 start=s.index('## N-TR01-11-07');end=s.index('## ▣ Verifica',start)
 s=s[:start]+'''## N-TR01-11-07 · Quadro UE e italiano: ruoli, rischio e confini

Il regolamento (UE) 2024/1689, **AI Act**, distingue pratiche vietate, sistemi ad alto rischio, obblighi specifici di trasparenza e modelli di IA per finalità generali. Il rischio dipende da uso previsto, contesto e ruolo; non basta il nome commerciale del prodotto. Il **provider** sviluppa o fa sviluppare un sistema e lo immette sul mercato o mette in servizio sotto il proprio nome; il **deployer** lo usa sotto la propria autorità nell'attività professionale. Una PA può essere deployer acquistando un servizio, ma anche assumere responsabilità da provider nei casi previsti, per esempio cambiandone la destinazione in modo da renderlo ad alto rischio. Il contratto deve rendere leggibili ruoli, documenti, assistenza e modifiche, senza trasferire artificialmente obblighi fissati dalla legge.

### Classificare un caso della PA

1. Verifica prima le pratiche vietate dell'articolo 5, tra cui forme di manipolazione dannosa e social scoring alle condizioni previste. Non si compensa un divieto con una firma umana finale.
2. Esamina l'articolo 6: prodotti/componenti di sicurezza dell'allegato I soggetti alla valutazione prevista e usi dell'allegato III, tra cui selezione del personale, accesso a determinati servizi essenziali, istruzione e giustizia.
3. L'articolo 6(3) consente, alle condizioni indicate, di non classificare come alto rischio alcuni usi dell'allegato III che non presentano un rischio significativo, per esempio compiti preparatori o procedurali ristretti. Non è un'esenzione generica per qualunque assistente. Un sistema dell'allegato III che effettua profilazione di persone rimane ad alto rischio; la valutazione del provider deve essere documentata.
4. Considera gli obblighi di trasparenza dell'articolo 50 e gli altri regimi applicabili. Un chatbot informativo non diventa automaticamente ad alto rischio, ma l'interazione con AI deve essere resa riconoscibile nei casi previsti; l'uso per selezionare candidati cambia la valutazione.

Per un sistema ad alto rischio, il deployer segue le istruzioni, assegna sorveglianza a persone competenti e dotate di autorità, controlla i dati di input sotto il proprio controllo, monitora e conserva i log automaticamente generati sotto il proprio controllo per il periodo pertinente, almeno sei mesi salvo diversa disciplina applicabile. Gestisce rischi, incidenti e sospensione secondo l'articolo 26. La PA verifica inoltre registrazione e valutazione d'impatto sui diritti fondamentali dell'articolo 27, quando richieste: quest'ultima ha un ambito proprio e si coordina con la DPIA privacy, senza sostituirla automaticamente. La semplice presenza di un operatore non basta: deve poter capire i limiti, contestare il risultato e fermare o modificare l'uso.

### Calendario aggiornato al 3 ottobre 2026

Il regolamento (UE) **2026/1744**, in vigore dal 27 luglio 2026, ha modificato il calendario. La tabella distingue regole generali e transitori: il rinvio di una categoria non sospende ogni obbligo AI.

| Disposizione o categoria | Applicazione pertinente |
| --- | --- |
| Capi I e II, inclusi alfabetizzazione e pratiche vietate | Dal 2 febbraio 2025, con le modifiche successive |
| Governance, modelli per finalità generali e altre parti anticipate dall'articolo 113 | Dal 2 agosto 2025 secondo il rispettivo ambito |
| Regola generale, incluse disposizioni di trasparenza non differite | Dal 2 agosto 2026 |
| Alto rischio, allegato III: capo III sezioni 1–3, salvo articolo 6(5) | Dal 2 dicembre 2027 |
| Articolo 6(1), prodotti dell'allegato I e obblighi collegati | Dal 2 agosto 2028 |

Per i sistemi generativi già immessi prima del 2 agosto 2026, il nuovo articolo 111(4) differisce al 2 dicembre 2026 il solo obbligo di marcatura dell'articolo 50(2): non rinvia indistintamente tutta la trasparenza. L'articolo 111(2) disciplina separatamente sistemi ad alto rischio già immessi/in servizio prima delle rispettive date, le modifiche significative successive e il termine del 2 agosto 2030 per provider e deployer di sistemi destinati a essere usati dalle autorità pubbliche. Quest'ultimo non è una proroga generale per ogni nuovo sistema acquistato dalla PA.

Il nuovo articolo 4 richiede misure che sostengano lo sviluppo dell'alfabetizzazione AI, considerando conoscenze, esperienza, formazione e contesto; non impone di garantire un identico livello individuale per tutti. Per l'esame collega quindi formazione, istruzioni e limiti agli usi effettivi del personale.

### La regola italiana per la PA e un esempio

L'articolo 14 della **legge 132/2025** richiede conoscibilità del funzionamento e tracciabilità dell'impiego. L'AI supporta l'attività provvedimentale: autonomia e responsabilità della persona che decide restano ferme. Le amministrazioni adottano misure tecniche, organizzative e formative per un utilizzo responsabile. La legge è distinta dalle strategie e dalle bozze di linee guida; un documento in consultazione non si presenta come obbligo già definitivo.

**Caso.** Un ufficio sperimenta un sistema che ordina curriculum per convocare candidati. Non lo classifica come semplice chatbot perché genera spiegazioni testuali: la finalità è selezione del personale, quindi verifica l'allegato III, il ruolo dell'ente e il calendario pertinente. Chiede documentazione, dati e limiti delle prestazioni, individua responsabili della sorveglianza, registra motivi delle decisioni e valuta impatti e disciplina privacy. Una firma che conferma sempre il punteggio non è un controllo effettivo. Se invece il sistema prepara solo bozze informative sui bandi, si rivaluta il diverso uso senza importare automaticamente la medesima classe.

Il NIST AI RMF, articolato in Govern, Map, Measure e Manage, offre un riferimento tecnico volontario per il ciclo di vita; non è una norma europea obbligatoria. Prima di una nuova decisione operativa, il calendario e gli atti attuativi vanno controllati sulla fonte ufficiale, conservando versione e data del riscontro.

'''+s[end:]
 return s
patch(11,ai)
def procure(s):
 s=before(s,'## N-TR01-12-02','''### CAD 68–69: confronto e riuso prima dell'acquisto

L'articolo 68 CAD richiede una valutazione comparativa tecnico-economica: sviluppo per conto dell'ente, riuso di software della PA, software libero/a codice aperto, cloud, software proprietario mediante licenza e combinazioni. Considera costo complessivo, formati e interfacce aperti, interoperabilità, sicurezza, protezione dei dati e livelli di servizio. Prima del software proprietario o dello sviluppo ad hoc deve essere verificata, con motivazione secondo le linee guida AgID, l'impossibilità di ricorrere alle soluzioni in riuso o a codice aperto adeguate alle esigenze. La disponibilità del sorgente non elimina costi di migrazione e gestione.

**Confronto didattico su cinque anni.** Una soluzione in riuso costa 20 mila euro di adattamento, 5 di migrazione, 30 di manutenzione e 5 di uscita: TCO 60 mila. Un prodotto proprietario costa 25 di licenze, 5 di migrazione, 30 di gestione e 10 di uscita: TCO 70 mila. Se entrambe soddisfano requisiti, sicurezza e servizio, il confronto motiva la scelta del riuso. Se una non soddisfa un requisito necessario, si documenta la verifica e si confrontano alternative: il solo totale non decide. Le cifre sono ipotetiche e non prezzi di mercato.

L'articolo 69 riguarda il riuso delle soluzioni di cui la PA è titolare: codice sorgente e documentazione devono essere resi disponibili con licenza aperta in repertorio pubblico secondo le regole AgID, salvo le eccezioni previste, tra cui sicurezza e difesa. Per software sviluppato su specifica indicazione dell'ente, la titolarità dei diritti necessari al riuso deve essere assicurata contrattualmente, salvo comprovate ragioni tecnico-economiche. Richiedere solo un eseguibile alla consegna può quindi compromettere un obbligo e la capacità di subentro.

### Vincoli specifici per l'approvvigionamento ICT

La legge 208/2015, articolo 1, commi 512 e seguenti, aggiunge una disciplina specifica per beni e servizi informatici e connettività. I soggetti individuati dal comma 512 ricorrono agli strumenti Consip o dei soggetti aggregatori, comprese le centrali regionali, per i beni e servizi disponibili presso tali soggetti. Il comma 516 consente l'approvvigionamento fuori dalle modalità prescritte solo previa autorizzazione motivata dell'organo di vertice amministrativo, se il bene/servizio non è disponibile o idoneo al fabbisogno, oppure in caso di necessità e urgenza funzionale alla continuità amministrativa; prevede comunicazione ad ANAC e AgID. Vanno controllati ambito soggettivo, norme speciali e deroghe applicabili al caso: non si trasforma questa sintesi in un obbligo identico per qualsiasi ente o attività di ricerca.

Il percorso è quindi duplice: documentare la scelta della soluzione secondo CAD e linee guida, poi individuare canale e procedura consentiti. Un confronto tecnico favorevole a un prodotto non autorizza da solo a saltare gli strumenti obbligatori.''')
 s=before(s,'## N-TR01-12-04','''### Calcolo svolto della disponibilità

Il contratto ipotetico misura il servizio end-to-end per 30 giorni, 24 ore su 24, senza esclusioni: 30×24×60=43.200 minuti. Le indisponibilità registrate e riconciliate durano 90 minuti. Disponibilità=(43.200−90)/43.200×100≈99,7917%. Con obiettivo 99,9%, l'indisponibilità ammessa è 43,2 minuti: il limite è superato di 46,8 minuti. Il verbale riporta intervalli, fonte di misura e confronto, non soltanto la percentuale del fornitore. Penali o altri rimedi dipendono dalle clausole: lo scostamento numerico non autorizza a inventarne l'importo.

Se il contratto escludesse manutenzioni programmate, occorrerebbe definirne preventivamente autorizzazione, finestra e trattamento del denominatore. Non si cancellano ex post i minuti sfavorevoli. Anche con disponibilità rispettata, latenza o errori applicativi potrebbero violare altri indicatori: uno SLA non rappresenta da solo tutta la qualità.''')
 s=s.replace("Il **direttore dell'esecuzione**, quando previsto, controlla l'esecuzione.","La funzione di **direzione dell'esecuzione** deve essere assicurata: per servizi e forniture è normalmente svolta dal RUP; nei casi di particolare importanza previsti dall'articolo 114, comma 8, e dall'allegato II.14, articoli 31–32, del d.lgs. 36/2023 si nomina un DEC distinto. Non confondere la presenza della funzione con l'obbligo di una persona separata, né presumere che qualsiasi acquisto ICT lo richieda automaticamente.")
 s=s.replace("il direttore dell'esecuzione quando previsto", "il soggetto che svolge la direzione dell'esecuzione")
 s=s.replace('Ruoli privacy, istruzioni, trasferimenti e misure richiedono validazione di giurista e DPO.', 'Il titolare decide su ruoli privacy, istruzioni, trasferimenti e misure, acquisendo le competenze legali necessarie e il parere/consulenza del DPO nei suoi compiti. Il DPO informa, consiglia e sorveglia: non è un organo che approva i trattamenti al posto del titolare e non assume funzioni operative incompatibili con la propria indipendenza.')
 return s
patch(12,procure)
def lab(s):
 s=before(s,'### Orale','''#### Elaborato modello: portale per consultare pratiche

Assumo un ente con 100 operatori e accesso esterno dei soli interessati, un archivio di un milione di pratiche e un servizio di sola consultazione nella prima fase. Prima della gara confermo volumi, categorie di dati, integrazioni e competenze interne. Il risultato atteso è consultare stato e documenti autorizzati senza recarsi allo sportello, mantenendo un canale assistito per chi ne ha bisogno.

Separerei interfaccia, API applicativa e database, con ambienti di sviluppo, collaudo e produzione distinti. L'accesso esterno passa dal meccanismo di identificazione previsto; l'applicazione verifica poi l'autorizzazione sulla singola pratica. Un token valido non autorizza a leggere quella di un altro cittadino. Gli operatori ricevono privilegi coerenti con funzione e ufficio; le attività amministrative privilegiate sono tracciate. Nel modello dati, chiavi e vincoli impediscono riferimenti incoerenti, mentre minimizzazione e tempi di conservazione sono definiti con i responsabili competenti.

Per la consultazione propongo un obiettivo didattico: 95° percentile entro 800 ms a 100 utenti concorrenti nell'ambiente e nel carico definiti, con errori sotto lo 0,5%. Il collaudo comprende accesso consentito e negato, input errati, pratiche assenti, indisponibilità di una dipendenza e verifica di accessibilità. Testo anche ripristino di backup e coerenza dei dati: la presenza di un file di backup non dimostra che il servizio riparta. Disponibilità, RTO e RPO sono concordati dopo l'analisi d'impatto; non li ricavo da un'etichetta commerciale.

Confronterei riuso, codice aperto e altre opzioni secondo CAD 68–69, includendo adattamento, migrazione, formazione, gestione e uscita. Per il cloud verifico classificazione di dati/servizi e qualificazione pertinente del servizio concreto. Contratto e piano operativo attribuiscono gestione degli accessi, patch, log, incidenti, supporto e comunicazioni; conservano all'ente evidenze e capacità di verifica.

Il rilascio avviene dopo migrazione di prova, riconciliazione dei record, test accettati e decisione autorizzata. Un piano indica finestra, responsabili, soglie di stop e rollback compatibile con eventuali nuove scritture. In esercizio misuro successo delle consultazioni, errori, tempi, incidenti e richieste allo sportello: se il canale digitale sposta soltanto il lavoro sugli operatori, il risultato va riesaminato. Preparo fin dall'inizio esportazione documentata, prova di subentro e gestione delle credenziali alla fine del contratto.

Questo elaborato rende esplicite assunzioni, architettura, controlli, test e governo. Una soluzione diversa è valutabile se collega altre scelte agli stessi bisogni e produce evidenze verificabili.''')
 s=before(s,'### Foglio di esito','''#### Soluzione commentata del caso autonomo

La correlazione con il rilascio è un indizio, non una causa dimostrata. Delimito orari, versioni, percentuale di errori e differenza fra canale interno ed esterno usando identificativi di correlazione, senza esportare dati personali non necessari.

| Ipotesi | Evidenza da cercare | Esito che cambia la decisione |
| --- | --- | --- |
| Configurazione del proxy o timeout diverso all'esterno | Confronto configurazioni/versioni, tempi a ogni tratto e codici gateway | Errore nasce al proxy prima della risposta applicativa |
| Nuova verifica del token incompatibile con alcuni accessi | Log di validazione, scadenza/audience e prova con account di test autorizzati | Fallisce una classe definita di token, non tutte le richieste |
| Dipendenza esterna lenta o limite di richieste | Latenza e stato del fornitore, correlazione con timeout e carico | Errori seguono saturazione o limiti della dipendenza |

Contengo il problema limitando la funzione coinvolta o attivando il canale alternativo previsto; non disabilito l'autorizzazione per far sparire gli errori. Coinvolgo responsabile del servizio e fornitore con orari, versioni e richieste riproducibili. Decido il rollback solo se versione precedente e dati sono compatibili, gli effetti sono reversibili e la procedura autorizzata è pronta. Se vi è sospetto di incidente di sicurezza, attivo il percorso dedicato preservando evidenze e valutando notifiche secondo il regime applicabile.

Dopo il ripristino confronto errori e latenza su entrambi i canali, provo permessi positivi e negativi, riconcilio operazioni rimaste pendenti e osservo una finestra significativa. Registro causa accertata o ancora da confermare, correzione, responsabile e prevenzione. La rubrica premia la sequenza ipotesi–evidenza–decisione: non richiede di indovinare una delle tre cause con i soli dati della traccia.

#### Prova pratica aggiuntiva: dati, algoritmo e metrica

Tempo didattico: 25 minuti. Tabella `Ticket(id, ufficio, minuti, chiuso)` con righe (1,A,20,true), (2,A,40,true), (3,B,30,true), (4,B,90,false). Scrivi una query con numero e tempo medio dei soli ticket chiusi per ufficio; indica output. Poi descrivi un algoritmo per il massimo tempo dei ticket chiusi e la sua complessità. Infine interpreta un monitor che segnala 8 anomalie vere, 2 false e ne perde 4.

**Soluzione SQL:** `SELECT ufficio, COUNT(*) AS numero, AVG(minuti) AS media FROM Ticket WHERE chiuso = TRUE GROUP BY ufficio ORDER BY ufficio;`. Output: A, 2, 30; B, 1, 30. La riga 4 è esclusa prima dell'aggregazione. Un ufficio senza chiusure non compare: se la traccia li richiedesse tutti, servirebbe l'anagrafica degli uffici con join e gestione esplicita dei null, senza spostare impropriamente il filtro in WHERE.

**Algoritmo:** inizializza `trovato=false`; scorri le righe; per ogni ticket chiuso, se è il primo o supera il massimo, aggiorna massimo e trovato. Restituisci «nessun ticket chiuso» se trovato rimane falso. Il risultato è 40. Per n righe il tempo è Theta(n), spazio ausiliario Theta(1); non ordinare tutto per ottenere un solo massimo. **Metriche:** precision=8/(8+2)=80%; recall=8/(8+4)≈66,67%; F1=16/(16+2+4)≈72,73%. Senza il numero di veri negativi non è calcolabile l'accuracy.

Assegna 2 punti a filtro/gruppi corretti, 2 all'output, 2 all'algoritmo e caso vuoto, 2 alla complessità dichiarata e 2 alle metriche con limite sull'accuracy. Ripeti correggendo l'errore specifico, senza memorizzare solo i numeri.''')
 return s
patch(13,lab)
def alg(s):
 s=s.replace('- Materiali didattici universitari e riferimenti tecnici su algoritmi, strutture dati e analisi asintotica.', '- Pat Morin, *Open Data Structures*, versione Python, § 1.3 e capitoli sulle strutture: https://opendatastructures.org/ods-python/.')
 start=s.index('### Quiz 5');end=s.index('### Quiz 6',start)
 q=s[start:end].replace('O(1)','Theta(1)').replace('O(log n)','Theta(log n)').replace('O(n)','Theta(n)').replace('O(n²)','Theta(n²)')
 q=q.replace('quale crescita tende', 'quale termine dominante a·f(n), con a positivo, tende')
 return s[:start]+q+s[end:]
patch(3,alg)
print('AI, ML, procurement, SLA, DEC, DPO, laboratorio e bibliografia corretti.')
