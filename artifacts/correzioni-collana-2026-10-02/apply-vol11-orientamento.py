from pathlib import Path
import re,json
p=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile/chapters/01-quattro-profili-mappa-sistema.md');t=p.read_text(encoding='utf8')
start=t.index('Un ultimo controllo');end=t.index('\n\n',t.index('Queste micro-sequenze',start));block=t[start:end];assert t.count(block)==5
first=True
def remove(m):
 global first
 if first:first=False;return m[0]
 return ''
t=re.sub(re.escape(block),remove,t)
adds={2:'''### Quattro consegne sullo stesso territorio

Immagina quattro bandi didattici riferiti allo stesso territorio. Il primo richiede al funzionario ambiente di istruire pratiche e interpretare risultati di monitoraggio. Il secondo seleziona uno specialista per aggiornare il piano di protezione civile. Il terzo cerca competenze per ridurre i consumi degli edifici pubblici. Il quarto riguarda la gestione dei procedimenti ambientali comunali. I luoghi coincidono; le prestazioni richieste cambiano.

Per **AMB**, una consegna utile è: «Individua il regime autorizzativo di un impianto e i dati necessari a controllarlo». Lo studio mette in relazione capacità, matrici, titolo, prescrizioni e accertamenti. Un elaborato ben riuscito non presume che l'autorizzazione elimini tutti i rischi; precisa che cosa viene consentito, a quali condizioni e come se ne verifica il rispetto. Nel ripasso privilegia i capitoli 02–09 e usa il laboratorio per trasformare le distinzioni in note motivate.

Per **PC**, la consegna può chiedere di organizzare uno scenario di esondazione sulla base di un bollettino e di osservazioni locali. Il candidato deve separare probabilità dell'evento, conseguenze possibili, vulnerabilità delle persone e disponibilità delle strutture. La risposta indica chi riceve l'informazione, quale fase viene valutata secondo il piano e quale messaggio raggiunge la popolazione. Non inventa una previsione certa e non tratta il colore dell'allerta come ordine automatico di evacuazione. I capitoli 10–11 costituiscono il percorso centrale.

Per **EN**, la consegna può riguardare due alternative di efficientamento di una scuola. La risposta parte dalla situazione iniziale e confronta energia, costi, emissioni e durata del progetto, esplicitando le ipotesi. Un risparmio percentuale senza consumo iniziale non basta; un incentivo non coincide con il beneficio fisico dell'intervento. I capitoli 12–13 conducono al confronto tra prestazioni, autorizzazioni, comunità energetiche ed evidenze di sostenibilità.

Per **LOC**, una segnalazione di rumore richiede una nota che distingua ricezione, verifica della competenza, accertamento tecnico e decisione. Il Comune può essere il punto di ingresso, mentre altri soggetti svolgono parti dell'istruttoria. Il percorso centrale comprende 02, 04–09 e il raccordo con 10–11 per i compiti locali di protezione civile. Se il bando comprende procedure di acquisto, il capitolo 13 serve per gli aspetti ambientali, insieme al volume dedicato agli appalti.

**Autovalutazione:** copri i nomi dei quattro profili e ricostruiscili dalla consegna. Assegna un punto per il profilo prevalente, uno per l'output e uno per la coppia di capitoli più pertinente: massimo 12. Una risposta diversa è accettabile se motivata da attività esplicitamente presenti nel bando; non lo è se deriva soltanto dal nome dell'ente.''',3:'''### Dalla misura alla conclusione: una scheda compilata

Un rapporto consegnato in prova indica un valore di 240 mg/L di solidi sospesi. Questa sola informazione non consente ancora di decidere. La scheda deve precisare oggetto della misura, recapito, punto, periodo, metodo, limite applicabile e prescrizioni del titolo. Nel caso didattico del capitolo 05 lo scarico è industriale, il recapito è una fognatura e il titolo pone il limite di 200 mg/L. Solo dopo questa qualificazione lo scostamento assume un significato verificabile.

La prima riga della scheda è il **fatto**: il laboratorio ha riportato un risultato, riferito a un campione identificato. La seconda è la **regola**: il limite appartiene al titolo e va confrontato con un dato raccolto nelle condizioni prescritte. La terza è la **valutazione**: il risultato supera il limite assunto nel caso, ma metodo e rappresentatività devono essere coerenti. La quarta è l'**azione amministrativa**: trasmissione e valutazione presso il soggetto competente, con qualificazione delle conseguenze secondo la norma. La quinta è la **verifica successiva**: documentare eventuali misure e controllarne l'esito.

Se la stessa cifra proviene invece da un rilevamento non identificabile, manca il collegamento al fatto. Se il valore riguarda un corpo idrico e non uno scarico, cambia il parametro di confronto. Se il campione è istantaneo mentre la prescrizione richiede una media, manca la necessaria comparabilità. Queste tre varianti spiegano perché conoscere una soglia non basta e, nello stesso tempo, perché non si può rinunciare a studiare la soglia pertinente.

**Seconda applicazione:** il progetto energetico dichiara un risparmio di 20.000 kWh annui. Per interpretarlo occorrono consumo iniziale, confine del sistema e metodo di stima o misura. Su 100.000 kWh iniziali il risparmio è il 20%; su 400.000 è il 5%. Il dato assoluto è uguale, ma cambia la lettura relativa. Se il clima dell'anno o l'orario di apertura differiscono, il confronto richiede una normalizzazione adeguata. Nel capitolo 12 il calcolo viene collegato a costi e emissioni.

**Consegna in cinque minuti:** riscrivi i due casi in cinque righe ciascuno, usando fatto, regola, valutazione, decisione e controllo. Correggi separatamente l'errore matematico e quello di qualificazione: rifare la divisione non risolve l'uso del parametro sbagliato. Una risposta completa rende visibili sia ciò che è già dimostrato sia il dato che impedisce di concludere.''',4:'''### Gerarchia e aggiornamento: come leggere tre documenti

La traccia presenta una disposizione normativa, una linea guida tecnica e una FAQ amministrativa. Prima di cercare una risposta, identifica la funzione di ciascuna. La disposizione può stabilire competenza, obblighi e termini; la linea guida può specificare un metodo nei limiti del proprio valore giuridico; la FAQ può chiarire il funzionamento di un servizio. Se sembrano contraddirsi, non vince automaticamente il documento più recente o più facile da leggere: occorre verificare rango, ambito e contenuto.

**Esempio A:** una norma distingue autorità ambientale e sportello unico. Una pagina informativa descrive lo sportello come «unico interlocutore». La formula organizzativa non trasferisce allo sportello ogni valutazione tecnica. Nel capitolo 04 la distinzione diventa concreta: autorità competente che adotta l'AUA e SUAP che rilascia il titolo. Il candidato può spiegare la semplificazione per l'utente mantenendo separate le responsabilità.

**Esempio B:** un rapporto ISPRA confronta dati nazionali e regionali. Il rapporto è adatto a descrivere un fenomeno e la metodologia usata; non assegna di per sé a un Comune il potere di imporre una nuova soglia. La risposta utilizza il dato per motivare l'istruttoria e ricerca la base normativa dell'eventuale intervento. Il SNPA è il sistema che comprende ISPRA e agenzie; le funzioni di indirizzo e coordinamento tecnico appartengono a ISPRA secondo la L. 132/2016.

**Esempio C:** il Parlamento esamina uno schema di decreto attuativo di una direttiva. Lo schema illustra un possibile futuro assetto, ma non va sostituito al testo nazionale vigente. Per studiare correttamente annota tre date distinte: pubblicazione della fonte europea, termine di recepimento e pubblicazione/entrata in vigore dell'atto nazionale. Se il testo definitivo non è ancora identificato, indica la distinzione senza attribuire allo schema efficacia già acquisita.

Per ogni fonte costruisci una piccola carta: titolo e autore istituzionale; oggetto; versione e data; regola o metodo ricavato; limite d'uso. Questa carta è utile soprattutto quando due documenti usano la stessa parola con funzioni diverse, come «controllo», «validazione» o «autorizzazione». Conservare soltanto un indirizzo internet non sostituisce la comprensione del contenuto.

**Prova orale:** spiega perché una FAQ sull'invio telematico di una domanda non può prolungare da sola la durata di un'autorizzazione. La risposta modello distingue il canale di presentazione, disciplinato dalle istruzioni operative, dalla durata del titolo, che richiede una base normativa. La data recente della FAQ non basta a modificare quest'ultima.''',5:'''### Decoder compilato: una selezione didattica

Il seguente avviso è inventato per esercitarsi: un ente cerca un funzionario per autorizzazioni e controlli ambientali; la prova scritta prevede due risposte aperte e un caso di istruttoria in 90 minuti; l'orale comprende le stesse materie, informatica e lingua indicate nel programma. I requisiti di ammissione e la scadenza della domanda sono campi da verificare nel bando reale, prima di iniziare il piano di studio.

**Profilo:** AMB, con raccordo LOC perché il caso riguarda pratiche territoriali. **Materie centrali:** sistema delle competenze, valutazioni, autorizzazioni, acque, rifiuti, bonifiche e controlli. **Prove:** due risposte sintetiche e una nota istruttoria, seguite da orale. **Prodotti da allenare:** confronto tra istituti, sequenza procedimentale motivata, richiesta di integrazione documentale. **Percorso:** capitoli 02–09, laboratorio 14; ripasso mirato dei capitoli 01 e 13 secondo il programma. Gli aspetti amministrativi comuni si recuperano nel volume base, senza duplicarli nello schema specialistico.

Per i 90 minuti della prova, un'ipotesi di allenamento è 5 minuti per leggere tutte le consegne, 20 per ciascuna risposta, 35 per il caso e 10 per il controllo. La somma è 90. Questa ripartizione non è un vincolo di concorso: si modifica in base a lunghezza, punteggi e indicazioni della commissione. Se il caso vale metà del punteggio, va protetto da una gestione del tempo che lo lasci incompleto.

Il decoder personale usa otto campi compilabili: ente e profilo; requisiti e titoli; scadenza e canale della domanda; materie e pesi dichiarati; prove e tempi; criteri di valutazione; documenti da produrre; calendario di studio. Se il bando non assegna pesi alle materie, scrivi «non dichiarati» e separa la tua scelta didattica dai dati ufficiali. Se la prova pratica viene rinviata a un avviso successivo, registra dove e quando controllarlo, senza inventarne la forma.

**Variante risolta:** sostituisci nell'avviso «autorizzazioni e controlli» con «piano comunale di protezione civile, esercitazioni e informazione alla popolazione». Il profilo prevalente diventa PC; il percorso centrale passa ai capitoli 10–11; l'output diventa scenario, matrice e messaggio pubblico. Il tempo totale rimane uguale, ma l'allenamento deve cambiare. Questa modifica controllata permette di capire se il piano segue davvero il lavoro richiesto.

**Controllo finale del decoder:** un compagno deve poter ricostruire ciò che studierai, quando lo verificherai e quale elaborato produrrai. Se trova soltanto sigle e titoli di capitoli, completa le consegne. Se trova scadenze inventate, correggi i dati prima di usare il calendario.'''}
for n,x in adds.items():
 t=re.sub(rf'(^## N-TR04-01-{n:02d}[^\n]*\n)',lambda m:m[0]+'\n'+x+'\n\n',t,count=1,flags=re.M)
t=t.replace('ISPRA produce dati, metodologie e supporto tecnico-scientifico; SNPA coordina il sistema nazionale a rete e rende omogenee molte attività di controllo e monitoraggio;','ISPRA produce dati, metodologie e supporto tecnico-scientifico ed esercita indirizzo e coordinamento tecnico; il SNPA è il sistema nazionale a rete formato da ISPRA, ARPA e APPA;')
a=t.index('Nei primi 30 giorni');b=t.index('\n\nIl capitolo 02',a)
t=t[:a]+'''I tre calendari sono **alternative**, non tre tappe obbligatorie dello stesso piano. Le durate indicano giorni disponibili; le ore sono ipotesi didattiche da adattare agli impegni personali. Il bando prevale sempre sulle priorità proposte.

| Durata | Carico indicativo | Ripartizione dei giorni |
|---|---|---|
| 30 giorni | 2 ore al giorno, 60 ore totali | 1–3 diagnosi; 4–18 teoria e richiamo; 19–26 casi; 27–30 prove e recupero |
| 60 giorni | 90 minuti al giorno, 90 ore totali | 1–5 diagnosi; 6–35 teoria e richiamo; 36–50 casi; 51–60 prove e recupero |
| 90 giorni | 1 ora al giorno, 90 ore totali | 1–7 diagnosi; 8–52 teoria e richiamo; 53–75 casi; 76–90 prove e recupero |

**AMB:** assegna circa il 60% del tempo disciplinare a 02–09, il 25% ai casi del 14 e il 15% ai raccordi indicati nel bando. Alterna una procedura autorizzativa e un tema di controllo, evitando di studiare tutte le autorizzazioni senza mai applicarle.

**PC:** dedica il 55% a 10–11, il 25% alle simulazioni di rischio e comunicazione del 14, il 20% al quadro 02 e ai temi ambientali richiesti. Ogni settimana produci uno scenario e un messaggio comprensibile a un destinatario non tecnico.

**EN:** dedica il 55% a 12–13, il 25% a calcoli e dossier del 14, il 20% a 02–04 e agli altri raccordi espressamente richiesti. Alterna sempre il calcolo di una prestazione alla verifica del procedimento e delle evidenze.

**LOC:** dedica il 55% a 02 e 04–09, il 25% alle note istruttorie del 14, il 20% a valutazioni, protezione civile o sostenibilità secondo il bando. Allena la distinzione tra segnalazione, competenza, accertamento e atto.

Le percentuali riguardano il tempo disciplinare, dopo la diagnosi; non sono pesi ufficiali delle materie. Usa un richiamo a libro chiuso dopo ogni sessione e una verifica ogni sette giorni: sei domande e un caso breve. Una regola didattica utile è almeno cinque risposte corrette e un caso senza errori su competenza o procedimento. Se non raggiungi il risultato, destina la prima sessione successiva al recupero e ripeti una variante del caso dopo due giorni. Registra separatamente errori di regola, calcolo, lettura e tempo.

**Esempio di recupero:** riconosci l'AUA ma attribuisci al SUAP tutte le decisioni tecniche. Non serve rileggere l'intero volume: riprendi il capitolo 04, ricostruisci la sequenza autorità–SUAP e risolvi un caso con un diverso titolo sostituito. Nel calendario di 30 giorni proteggi almeno gli ultimi quattro giorni dalle nuove materie non essenziali, mantenendo prove complete e correzione degli errori ricorrenti.''' +t[b:]
for key,val in [('source_refs','sources/vol-11-ambiente-rettifiche-2026-10-03'),('last_compiled_from','wiki/sources/vol-11-ambiente-rettifiche-2026-10-03.md'),('topics','topics/ambiente-rettifiche-2026')]:
 m=re.search(r'^'+key+r': (\[.*\])$',t,re.M);arr=json.loads(m[1]);arr.append(val);t=t[:m.start(1)]+json.dumps(arr,ensure_ascii=False)+t[m.end(1):]
t=re.sub(r'^updated_at: .*$', 'updated_at: 2026-10-03',t,flags=re.M);t=re.sub(r'^draft_stage: .*$', 'draft_stage: revision-in-progress',t,flags=re.M);t=re.sub(r'^review_required: .*$', 'review_required: true',t,flags=re.M)
p.write_text(t,encoding='utf8');print('Capitolo 01: quattro copie rimosse, esempi distinti e tre calendari alternativi.')
