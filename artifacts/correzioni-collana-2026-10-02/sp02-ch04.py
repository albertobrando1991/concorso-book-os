from pathlib import Path
import re
p=Path('wiki/books/moduli/m-sp02-vigili-fuoco/chapters/04-tre-prove-motorio-attitudinali.md');t=p.read_text(encoding='utf8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp02-04.md')
if not a.exists():a.write_text(t,encoding='utf8')
def rep(a,b):
 global t
 assert a in t,a[:70]
 t=t.replace(a,b)
def span(a,b,v):
 global t
 i=t.index(a);j=t.index(b,i);t=t[:i]+v+'\n\n'+t[j:]
rep('ammette dieci candidati per ogni posto disponibile.','ammette un numero di candidati pari a dieci volte i posti, oltre ai pari merito dell’ultimo ammesso.')
rep('Detto altrimenti: dopo la preselezione, **il novantacinque per cento del tuo punteggio dipende dal corpo**. Se hai impostato la preparazione come se fosse un concorso da studiare, l\'hai impostata al contrario.','Le prove motorio-attitudinali rappresentano **90 dei 95 punti massimi**, circa il 94,7%. Occorre prepararle per tempo, insieme allo studio necessario a superare la preselezione: il peso in graduatoria e la funzione di accesso sono due cose diverse.')
rep('individuare il tuo **modulo peggiore**, perché è quello che determina l\'esito della Prova 1 e quindi il punto di partenza del piano.','distinguere **soglia di ogni modulo e media della Prova 1**: una insufficienza impedisce il superamento, mentre il voto dei moduli tutti sufficienti si calcola con la media.')
rep('Il certificato agonistico richiede una visita con elettrocardiogramma sotto sforzo, e nei periodi di punta gli appuntamenti si trovano a settimane di distanza.','Gli accertamenti per il certificato sono individuati dal professionista secondo la disciplina applicabile; il bando non prescrive qui un identico esame sotto sforzo per ogni candidato. Considera i tempi di prenotazione e rilascio.')
rep('Chi stringe i denti, finisce la prova e reclama il giorno dopo, ha perso il diritto di reclamare.','Questa regola riguarda l’istanza di riesame per l’infortunio non tempestivamente rappresentato; non va trasformata nell’abolizione di ogni rimedio o tutela giuridica.')
rep('Un candidato che porta 30 alle trazioni e 18 alla trave non ha una media di 26: ha una prova non superata.','Un candidato con 30 alle trazioni e un modulo C non superato resta insufficiente, anche se la trave è conclusa correttamente. Se invece ottiene 30, 21 e 21, supera tutti i moduli e la media è 24: il voto non coincide con il minimo di 21.')
rep('Dieci centimetri di larghezza, quattro metri di altezza. Fermati su questi due numeri: è la parte del concorso che più somiglia al mestiere, e la ragione per cui non si allena in palestra.','L’esecuzione ufficiale avviene con i dispositivi di sicurezza e l’assistenza previsti dall’allegato, fra cui imbragatura e casco. La descrizione serve a comprendere la prova, non a riprodurla autonomamente su attrezzature improvvisate.')
rep('Non conta quanto vai veloce sulla trave, conta se cadi.','Il punteggio dipende dal tentativo utile, fermo il tempo massimo complessivo.')
rep('La commissione regola l\'altezza di una sbarra in modo da farne coincidere la parte bassa con la punta delle tue dita, da stazione eretta con le braccia lungo i fianchi. Poi dà il «via».','Per **regolare l’altezza** della sbarra il candidato è in stazione eretta, con piedi uniti, **braccia in alto e dita distese e unite**: la parte inferiore della sbarra coincide con l’estremità delle dita. Terminata la regolazione, la **posizione di partenza** è a braccia lungo i fianchi, con i piedi in linea, prima del «via». Le due posizioni hanno funzioni differenti e non vanno invertite.')
rep('Qui la forbice è tutta un\'altra cosa: dal minimo al massimo passano nove progressioni per gli uomini, ma su una base di diciotto. In proporzione, è l\'esercizio in cui il salto dal sufficiente all\'eccellente costa meno.','Fra minimo e massimo maschili ci sono nove progressioni. Il rapporto numerico non misura quanto sia facile guadagnarle: tecnica, condizione individuale e stabilità dell’esecuzione vanno valutate separatamente.')
rep('Le altre due prove sono monomodulo, e sono molto diverse fra loro: una si migliora allenandola, l\'altra va prima imparata.','Le altre due prove sono monomodulo: entrambe richiedono capacità fisiche e tecnica specifica. Le soglie descrivono la valutazione, non i tempi personali necessari per prepararsi.')
rep('Non è un dettaglio burocratico: il rilevamento è ridondante e non lascia margini di contestazione.','Il doppio rilevamento serve anche a gestire il malfunzionamento dell’automatismo; non rende il risultato sottratto a controlli o ai rimedi previsti.')
span('Quattro minuti e cinquantacinque','Due dettagli di rilevazione','''Tra le soglie maschili di 21 e 30 punti ci sono quaranta secondi; lo stesso scarto separa i due estremi femminili. Non è una valutazione della difficoltà personale della prova. La commissione può variare l’ordine: la corsa non si svolge necessariamente dopo trave e trazioni. Una rilevazione da riposati è un dato iniziale; l’effetto di sequenze e recuperi va considerato nella preparazione con personale competente, senza presupporre un ordine fisso.''')
rep('### Prova 3: quella che elimina','### Prova 3: acquaticità e validità del percorso')
rep('È l\'unica tolleranza a costo zero dell\'intera giornata.','La ripetizione segue questa specifica condizione; non è un permesso generale di ricominciare qualsiasi esecuzione.')
span('Sono i numeri più duri','## N-SP02-05-04','''Le soglie vanno associate al sesso previsto dal protocollo e a un’esecuzione valida. Un tempo basso ottenuto omettendo un ostacolo non vale come superamento: prima si verifica la correttezza del percorso, poi il tempo.

> **Preparazione in sicurezza.** Non svolgere prove di apnea da solo e non ricostruire autonomamente ostacoli o percorsi sommersi. La conoscenza del protocollo concorsuale non sostituisce l’assistenza e la valutazione professionale necessarie alla preparazione in acqua.

Il calendario delle prove viene pubblicato sul sito istituzionale e su inPA dopo la preselezione. Avvia per tempo la valutazione della preparazione necessaria, senza attendere la convocazione per scoprire una capacità non ancora acquisita. Non esistono dati, in questo capitolo, per affermare che il nuoto elimini più candidati delle altre prove o che tutti richiedano lo stesso numero di mesi.''')
span('Adesso che hai tutte le tabelle davanti','## N-SP02-06-01','''Le tabelle permettono di calcolare **soglie, scarti e peso dei punteggi**. Non permettono di calcolare automaticamente il rendimento di un’ora di allenamento. Un rapporto 27/18 nelle progressioni e un rapporto 13/4 nelle trazioni confrontano prestazioni diverse: non dimostrano che il primo miglioramento sia più facile.

### Validità, margine e punteggio

**Primo controllo: validità.** Ogni modulo deve rispettare il protocollo e raggiungere almeno 21. Una prestazione non valida non si recupera con i punti di un altro esercizio. Questo giustifica l’attenzione prioritaria alle insufficienze, senza trasformare il libro in una prescrizione di allenamento.

**Secondo controllo: margine.** Un uomo che compie 19 progressioni supera di una sola ripetizione il minimo di 18. Se ne compie 12 alla sbarra, supera di otto il minimo di quattro. Sono distanze nominali: per scegliere le priorità occorrono anche ripetibilità, qualità tecnica e condizioni personali. Non si confrontano direttamente otto trazioni e una progressione come se fossero la stessa unità di fatica.

**Terzo controllo: peso.** Se tutti i moduli sono sufficienti, un aumento di nove punti in un modulo della Prova 1 aumenta la sua media di tre punti. Un aumento di nove punti nella corsa aumenta di nove il totale delle prove. Questa è aritmetica della graduatoria, non una raccomandazione a trascurare i moduli: senza tutte le sufficienze il totale non è utilizzabile.

Esempio: A = 30, B = 21, C = 21. La media è (30 + 21 + 21)/3 = 24. Se B sale a 30, la nuova media è 27, con guadagno di tre punti. Aggiungendo corsa 21 e nuoto 21, il totale passa da 66 a 69. Se il nuoto non è superato, nessuno dei due totali consente di proseguire alla valutazione dei titoli. Il valore minimo individua una condizione di validità, non sostituisce la media.

### Caso guidato: Luca dopo la chiusura delle domande

Luca ha già presentato domanda dichiarando la patente B e dispone, nell’ipotesi del caso, di sei mesi prima delle prove. Alla rilevazione iniziale conclude la trave al primo tentativo, esegue 11 trazioni e 20 progressioni, corre in 4'48\"; non completa il percorso acquatico. Il dato sulla piscina descrive una prova non superata, non una diagnosi della sua capacità futura.

Il primo output è una tabella di criticità: acquaticità da valutare e preparare in sicurezza; margine nominale di due progressioni nel modulo C; sette secondi rispetto al limite maschile di corsa. Non è necessario inventare i punteggi intermedi per riconoscere queste distanze. L’ordine delle prove non è predeterminato: la preparazione deve considerare il possibile affaticamento senza affermare che Luca correrà sicuramente dopo le trazioni.

Luca valuta anche la patente C. Nell’allegato B vale quattro punti contro uno della B: differenza nominale di tre. Ma conseguirla nei sei mesi successivi alla **scadenza già trascorsa** non la rende valutabile in questo concorso. Il primo controllo economico e organizzativo è dunque il termine, prima di qualsiasi confronto con il guadagno fisico. Per una procedura futura il percorso di guida può avere senso, ma dovrà rispettare i requisiti e i termini di quel bando; superare gli esami non è garantito.

Il piano risultante riguarda decisioni, non carichi atletici. Luca discute la situazione sanitaria e tecnica con i professionisti competenti, definisce verifiche della validità del percorso acquatico, registra i margini e la loro stabilità, mantiene le capacità già sufficienti e colloca il certificato nella finestra richiesta. A ogni controllo annota protocollo usato, esecuzione valida o invalida, misura e condizioni della rilevazione. Un numero senza contesto non prova un miglioramento stabile.

### Mini-esercizio sul rendimento

Due candidati guadagnano entrambi nove punti nominali: uno in un modulo della Prova 1, l’altro nella corsa. Tutti i moduli erano e restano sufficienti. Il primo guadagna tre punti nel totale, il secondo nove. Puoi concludere che per chiunque convenga allenare la corsa? **No:** mancano probabilità e tempi del miglioramento, stato di partenza e sicurezza. Puoi soltanto descrivere il diverso peso aritmetico dei punteggi. Separare queste due conclusioni impedisce di trasformare una tabella d’esame in un programma atletico universale.

> **Avvertenza necessaria.** Questo capitolo descrive prove e criteri; non prescrive allenamenti. Per preparazione fisica, attività in acqua e in quota servono valutazione sanitaria e assistenza professionale appropriate.''')
rep('più di quanto separi, su una singola prova motorio-attitudinale, un candidato che passa a fatica da uno che va bene.','un incremento aritmetico da valutare insieme alle condizioni per ottenere e far valutare il titolo.')
span('> **È l\'unica leva interamente sotto il tuo controllo.**','Le patenti superiori hanno inoltre','''> **Titoli e calendario.** Una patente è una possibile scelta di preparazione, subordinata a requisiti, tempi, costi e superamento degli esami. Non è un esito certo. Se la scadenza del titolo è già trascorsa, conseguirla prima della prova fisica non attribuisce punti nella tornata in corso.

Confronta due casi. Anna ha la C alla scadenza, la dichiara e supera tutte le prove: il titolo vale quattro punti. Bruno ha la B alla scadenza e consegue la C dopo: il nuovo titolo non diventa valutabile per il solo fatto che la commissione esamina i titoli più tardi. La data della valutazione non sposta quella del possesso.

Se un candidato possiede C e CQC Merci, entrambe tempestivamente dichiarate, dopo aver superato le prove riceve cinque punti, non nove. Il principio di non cumulabilità impone di considerare il titolo più favorevole. Non equivale a una preferenza a parità di merito: il titolo valutabile concorre al punteggio; una preferenza opera sul confronto fra candidati a parità secondo le regole specifiche.

Per programmare un percorso futuro annota il titolo già posseduto, quello eventuale, il guadagno nominale, i prerequisiti e la data entro cui deve maturare. Solo dopo questi controlli valuta il costo e la compatibilità con gli altri impegni. Nessuna scelta relativa ai titoli precede automaticamente la sicurezza, l’ammissibilità o la preparazione delle prove eliminatorie.''')
rep('hai vinto la parte che non conta.','hai superato un filtro necessario senza essere pronto per la fase successiva.')
span('**«Punto tutto sulle trazioni','**«Il certificato medico','''**«Il rapporto fra minimo e massimo dice dove guadagno più facilmente».** Non misura il rendimento dell’allenamento. Confronta validità, margini, stabilità e peso dei punteggi, con una valutazione personale della preparazione.

**«I tempi li recupero il mese prima».** Il protocollo non consente di prevedere i tuoi tempi di miglioramento. Le capacità mancanti e i margini instabili vanno individuati per tempo.''')
span('## ▣ Verifica 04.A','## ▣ Verifica 04.B','''## ▣ Verifica 04.A · Quiz ragionati

**1. In Prova 1 il candidato ottiene A = 25, B = 30, ma non supera il modulo C. Qual è l’esito?**

A. Supera grazie ai primi due voti.
B. Non supera: ciascun modulo deve raggiungere almeno 21.
C. Ottiene il minimo dei primi due voti, cioè 25.
D. Ripete automaticamente il solo modulo C.

**Risposta corretta: B.** La media è utilizzabile solo se tutti i moduli sono sufficienti. A e C inventano compensazioni; D un diritto automatico alla ripetizione. Il 25 alla trave è un esito previsto, a differenza di un ipotetico 28.

**2. Alla trave la traslocazione è completata alla seconda esecuzione entro il tempo complessivo. Qual è il punteggio?**

A. 30.
B. 21.
C. 25.
D. Zero, perché ogni caduta esclude.

**Risposta corretta: C.** Gli esiti utili sono 30, 25 e 21 secondo il tentativo. A ignora la ripetizione, B la confonde con la terza esecuzione e D elimina i tentativi consentiti.

**3. Quale documento è richiesto prima delle prove motorio-attitudinali?**

A. Certificato agonistico dei soggetti abilitati indicati, emesso non prima di 45 giorni dalla prova.
B. Un generico certificato del medico di base.
C. Nessun documento prima della prova.
D. Qualsiasi certificato agonistico, indipendentemente dalla data.

**Risposta corretta: A.** Tipo, soggetto emittente e finestra temporale sono condizioni cumulative. B sbaglia il documento, C elimina l’adempimento e D ignora la data.

**4. Il candidato già riconvocato è nuovamente impossibilitato a presentarsi. Che cosa prevede il bando campione?**

A. Una terza data automatica.
B. Il punteggio minimo d’ufficio.
C. La valutazione dei soli titoli.
D. La considerazione come rinunciatario e l’esclusione.

**Risposta corretta: D.** Il bando limita il differimento a una volta anche per le ulteriori cause indicate. A, B e C sostituiscono alla regola benefici non previsti.

**5. Un uomo esegue 12 trazioni e 19 progressioni. Quale affermazione riguarda correttamente i margini nominali?**

A. La trave vale il doppio.
B. Sono otto trazioni e una progressione sopra i rispettivi minimi; da ciò solo non si deduce il rendimento dell’allenamento.
C. Le progressioni rendono certamente di più a parità di ore.
D. Essere sopra soglia rende inutile ogni controllo di stabilità.

**Risposta corretta: B.** Le sottrazioni sono 12 − 4 e 19 − 18. C trasforma numeri non omogenei in una previsione fisica; A altera il peso dei moduli e D ignora la ripetibilità della prestazione.

**6. Dopo aver superato tutte le prove, un candidato ha C e CQC Merci possedute e dichiarate entro il termine. Quanti punti spettano per questi titoli?**

A. Nove.
B. Quattro.
C. Cinque.
D. Uno.

**Risposta corretta: C.** Vale il titolo più favorevole e i punteggi non si cumulano. A somma indebitamente; B trascura la CQC e D applica il valore della sola B. La premessa soddisfa espressamente le condizioni di possesso, dichiarazione e superamento.''')
span('## ▣ Verifica 04.B','## In sintesi','''## ▣ Verifica 04.B · Domande aperte e riscontri

**1.** A = 25, B = 30, C = 21: calcola la media. **Riscontro:** 76/3 = 25,333…; tutti sufficienti. Se C non è superato, non basta la media degli altri a salvare la prova.

**2.** Alla trave concludi alla seconda ripetizione: quanti punti perdi? **Riscontro:** ottieni 21 e perdi nove rispetto a 30; un ulteriore tentativo ordinario non è previsto.

**3.** Un uomo corre in 5'10\" e non completa il percorso acquatico, mentre i tre moduli sono sufficienti. Che cosa emerge? **Riscontro:** corsa oltre 4'55\" e acquaticità non superata, entrambe da affrontare nella preparazione competente. Per una donna il confronto con 5'40\" darebbe un diverso esito della corsa.

**4.** Dodici trazioni e diciannove progressioni bastano a scegliere l’investimento più redditizio? **Riscontro:** no; descrivono margini nominali, non tempi, possibilità individuali o stabilità del miglioramento.

**5.** La corsa si svolge sempre dopo le trazioni? **Riscontro:** no, decide la commissione e l’ordine può cambiare. Considerare l’affaticamento non significa inventare una sequenza obbligatoria.

**6.** La preselezione non dà punti: può essere trascurata? **Riscontro:** no, è il filtro per accedere alle prove; punteggio finale e condizione di accesso sono funzioni differenti.

**7.** Qual è il guadagno da B a C e quello di venti secondi in corsa? **Riscontro:** tre punti nominali per il titolo, se posseduto e dichiarato entro termine e dopo superamento delle prove. Per i venti secondi mancano tempo iniziale e corrispondente tabella di conversione: non si deve inventare un punteggio intermedio.

**8.** Convocazione con 35 giorni di anticipo: che cosa controlli sul certificato? **Riscontro:** prenotazione, rilascio da soggetto abilitato, tipo richiesto e data nella finestra dei 45 giorni prima della prova. La prenotazione non equivale al rilascio.

**9.** Infortunio durante un modulo: qual è l’adempimento immediato? **Riscontro:** comunicarlo alla commissione. La specifica regola sulle istanze di riesame non tempestivamente rappresentate non elimina ogni tutela giuridica.

**10.** Quali documenti consentono di verificare esercizi e titoli? **Riscontro:** articolo 8 e allegati A e B del bando della propria tornata, insieme agli avvisi pertinenti. Un esempio datato non sostituisce eventuali regole diverse.''')
span('## In sintesi','*Fonti:','''## In sintesi

La graduatoria somma le tre prove, fino a novanta punti, e i titoli valutabili, fino a cinque. La Prova 1 usa la media dei moduli tutti sufficienti; il modulo minimo non è il voto finale. Protocollo, soglie, certificati e termini si controllano separatamente. I numeri descrivono il punteggio, senza prevedere la facilità dell’allenamento o garantire l’acquisizione di una patente.''')
t=t.replace('Dati verificati al 10 agosto 2026.','Dati del bando campione ricontrollati il 3 ottobre 2026.')
for old,new in [('N-SP02-05-01','N-SP02-04-01'),('N-SP02-05-02','N-SP02-04-02'),('N-SP02-05-03','N-SP02-04-03'),('N-SP02-05-04','N-SP02-04-04'),('N-SP02-06-01','N-SP02-04-05')]:t=t.replace(old,new)
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);t=t.replace('review_required: false','review_required: true');p.write_text(t,encoding='utf8');print('SP02/04 corretto')
