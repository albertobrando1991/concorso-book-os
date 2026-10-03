from pathlib import Path
import re,shutil
B=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters');A=Path('wiki/reviews/correzioni-collana-2026-10-02/archive')
def get(n):
 p=next(B.glob(n+'-*.md')); a=A/('pre-correzioni-sp01-'+n+'.md');assert not a.exists();shutil.copyfile(p,a);return p,p.read_text(encoding='utf-8')
p,t=get('01'); t=t.replace('## Spiegazione\n\n','',1)
pos=t.index('Il quadro delle prove va letto in modo dinamico.')
t=t[:pos]+'''### Ruoli concreti e prove dei bandi 2026

«Base» e «ispettivo» sono categorie di orientamento di questo modulo; nel bando devi cercare la denominazione giuridica del ruolo. Per la Polizia di Stato il confronto è fra allievo agente e allievo vice ispettore; per l’Arma e la Guardia di finanza il percorso ispettivo considerato è quello degli allievi marescialli. Non equivale all’accesso all’Accademia per ufficiali.

| Esempio datato | Prove che distinguono la preparazione |
| --- | --- |
| PS 4.400 allievi agenti, decreto 29 aprile 2026 | Scritto, efficienza fisica, accertamenti psicofisici e attitudinali, titoli |
| PS 1.000 vice ispettori, decreto 19 gennaio 2026 | Scritto giuridico a quiz; accertamenti e orale, anche inglese e informatica |
| Carabinieri 3.081 allievi, 146° corso | Scritto di selezione, efficienza fisica, accertamenti psicofisici e attitudinali, titoli; non un orale autonomo |
| Carabinieri 898 marescialli, decreto 16 febbraio 2026 | Preliminare, scritto d’italiano a 60 quiz, efficienza fisica, accertamenti, orale e facoltative |
| GdF 983 marescialli, bando 20 febbraio 2026 | Preselezione, composizione italiana di sei ore, prove fisiche, accertamenti, orale, lingua facoltativa e titoli |

Il diploma è il titolo di riferimento negli esempi, ma ciascun bando disciplina quando conseguirlo ed eventuali categorie particolari: il capitolo 02 distingue queste condizioni. Per i bandi PS citati esiste la possibilità di conseguimento entro la prima prova; gli esempi marescialli indicano l’anno scolastico 2025/2026. Non è corretto scrivere «diploma sempre già posseduto all’invio» né applicare l’eccezione a una diversa selezione.

Il confronto cambia il lavoro settimanale. Il candidato CC 898 esercita italiano a risposta multipla, non un tema attribuito per analogia al ruolo marescialli. Il candidato GdF 983 deve invece produrre elaborati completi. Il candidato PS vice ispettore allena quesiti di penale, procedura penale e costituzionale e prepara anche l’orale con le ulteriori materie dell’articolo 8. Il nome del livello non sostituisce il programma.

La Polizia locale segue una distinta famiglia: per identificare agente, istruttore o ufficiale e ricostruire il programma territoriale usa [[books/moduli/m-fl04-polizia-locale/chapters/01-diventare-agente-ufficiale-polizia-locale#N-FL04-01-01 · Dal bando al profilo di Polizia locale|VOL-02, Polizia locale: dal bando al profilo]]. Le qualifiche e i requisiti non si trasferiscono automaticamente fra quel percorso e quelli di questo modulo.

''' +t[pos:]
t=t.replace('La graduatoria finale non è la somma emotiva degli sforzi compiuti, ma il risultato della catena selettiva.','La graduatoria finale richiede il superamento di tutte le condizioni previste e l’applicazione dei criteri del bando.')
p.write_text(t,encoding='utf-8')
p,t=get('03')
start=t.index('La prova scritta nelle carriere speciali');end=t.index('Il punto decisivo è il doppio binario',start)
t=t[:start]+'''Per riconoscere una prova devi separare tre informazioni. La **funzione** indica se seleziona l’accesso alla fase successiva o contribuisce alla graduatoria; il **formato** indica che cosa consegni, per esempio risposte a scelta multipla o un elaborato; la **provenienza dei quesiti** indica se esiste una banca ufficiale, completa o soltanto parziale. Una preselezione può essere a quiz tratti da banca dati: le tre etichette descrivono contemporaneamente la stessa prova, non tre alternative incompatibili.

''' +t[end:]
t=t.replace('capire perché sono incompatibili tra loro','distinguere funzione, formato e materiale disponibile')
t=t.replace('Devi capire la logica del componimento di italiano nei concorsi dell’Arma dei Carabinieri, quando il bando prevede una prova scritta discorsiva centrata sulla qualità della lingua, dell’ordine espositivo e dell’aderenza alla traccia.','Devi riconoscere la prova scritta di italiano a 60 quesiti del bando Carabinieri 898 marescialli 2026, senza trasformarla in un componimento per analogia con altre procedure.')
t=t.replace('componimento di italiano CC','italiano a quesiti CC').replace('un componimento richiede scrittura ordinata','un test d’italiano richiede analisi linguistica').replace('scalette di componimento','esercizi linguistici corretti')
start=t.index('## N-SP01-05-03');end=t.index('## N-SP01-05-04',start)
t=t[:start]+'''## N-SP01-05-03 · Italiano a quesiti: l’esempio Carabinieri 898 marescialli

### Leggere l’allegato prima di scegliere gli esercizi

Nel bando 2026 per 898 allievi marescialli dell’Arma, l’articolo 9 denomina la fase «prova scritta di conoscenza della lingua italiana». Il nome non basta per identificarne il formato. L’allegato C, punto 2, specifica **60 quesiti a risposta multipla**: si verificano strutture della lingua, ragionamento verbale e comprensione del testo. Non si tratta di un componimento. Chi prepara soltanto temi svolti allena una capacità utile in generale, ma trascura il prodotto richiesto dalla prova concreta.

La soglia indicata dall’articolo 9 è 18/30. Non va confusa con il numero di quesiti né convertita autonomamente in un numero di risposte: per questa operazione occorre conoscere criteri di correzione, eventuali penalizzazioni e trattamento delle omissioni. La prova preliminare che precede lo scritto è una fase diversa: non basta superarla per considerare già verificata tutta la competenza linguistica richiesta.

### Le competenze che entrano nel test

L’ortografia riguarda la corretta scrittura: accenti, apostrofi, grafie. La morfologia riguarda le forme e le categorie delle parole, come tempi e modi verbali o accordi. La sintassi riguarda i rapporti nella frase e nel periodo. Lessico e semantica riguardano scelta dei termini e significato nel contesto. Il ragionamento verbale richiede di ricavare relazioni coerenti; la comprensione richiede di distinguere ciò che il testo afferma da ciò che il lettore aggiunge.

Queste aree si sovrappongono in alcuni quesiti, ma separarle nel diario consente una correzione mirata. Se sbagli una concordanza, non serve soltanto rileggere il brano più velocemente. Se interpreti male una negazione, non basta studiare una lista di sinonimi. Dopo ogni errore scrivi la regola o il passaggio che decide l’alternativa, e costruisci una frase nuova che ne controlli l’applicazione.

### Tre esercizi originali risolti

**Accordo.** Completa: «La serie di controlli ___ conclusa». A: sono; B: è; C: hanno; D: vengono. La risposta è B: il soggetto è «la serie», singolare; «di controlli» non diventa il soggetto perché è la parola più vicina al verbo. Il distrattore A sfrutta precisamente questa attrazione. C e D non costruiscono correttamente la frase proposta.

**Comprensione.** Leggi: «L’accesso è consentito solo dopo la registrazione. La registrazione non assicura la disponibilità di un posto». Quale conclusione segue? A: ogni registrato entra; B: si può entrare senza registrarsi; C: chi entra si è registrato, ma un registrato può non trovare posto; D: nessuno entra. La risposta è C. La registrazione è necessaria, ma il testo esclude che basti da sola. A cancella la seconda frase, B contraddice la prima, D aggiunge un fatto non detto.

**Lessico nel contesto.** In «la commissione differisce la prova», il verbo significa rinvia, non distingue. Il significato va ricavato dalla costruzione: «differire da» esprime diversità, mentre differire un’attività significa spostarla nel tempo. Memorizzare un solo sinonimo per una parola senza contesto produce errori proprio nelle alternative plausibili.

### Un ciclo di preparazione verificabile

Usa una sessione iniziale per diagnosticare il tipo di errore, senza inventare la durata ufficiale del test. Dedica poi un blocco a una sola debolezza: per esempio dieci periodi con subordinate e individuazione del soggetto. Nel blocco successivo mescola tipologie differenti, così non rispondi grazie all’etichetta dell’esercizio. Infine ripeti a distanza gli errori cambiando ordine delle opzioni e frase di contesto. Il risultato da registrare è la regola applicata, insieme al tempo e all’esito.

La banca della prova preliminare prevista dall’allegato C è un ausilio allo studio con esclusioni: non comprende tutti i quesiti linguistici e di comprensione indicati dalla procedura. Non puoi dedurre che ogni domanda successiva sia già disponibile né chiamare automaticamente «chiusa» ogni raccolta ufficiale. Controlla separatamente quale materiale riguarda la preliminare e quale lo scritto d’italiano.

### Caso e controllo finale

Laura trova una guida che associa «marescialli» a «tema». Dopo una settimana di elaborati legge il bando 898 e scopre i 60 quesiti. Corregge il piano: mantiene una breve attività di scrittura per chiarire le regole, ma sposta le esercitazioni principali su ortografia, morfologia, sintassi, lessico e comprensione. Non afferma che tutti i concorsi dell’Arma abbiano questo formato: registra anno, numero di posti e allegato.

**Verifica.** Spiega perché il titolo «prova d’italiano» non identifica da solo il formato; risolvi i tre esercizi senza guardare le soluzioni; indica quale documento ti serve prima di calcolare il punteggio. Se rispondi «un tema è sempre richiesto ai marescialli», stai ancora usando il nome del ruolo al posto del bando.

''' +t[end:]
start=t.index('Il tema o la prova di cultura generale,');end=t.index('La teoria di questo formato',start)
t=t[:start]+'''Nel bando GdF 983 allievi marescialli del 2026 la «prova scritta di cultura generale» è definita dall’articolo 12, comma 3: composizione italiana unica per tutti i candidati, durata sei ore, adeguata ai programmi della scuola secondaria di secondo grado. Il minimo di idoneità dell’articolo 13 è 10/20. Qui «cultura generale» è la denominazione della prova e «composizione italiana» ne descrive il formato: non sono due generi da separare artificialmente.

Il confronto con i Carabinieri 898 è netto: in quel bando lo scritto d’italiano è a quiz, in questo si consegna un testo. Per GdF sono consentiti vocabolario italiano e dizionario dei sinonimi e contrari, non commentati né annotati né in fotocopia, secondo l’articolo 12. Non estendere questa ammissione di materiali al test Carabinieri o allo scritto PS, che seguono regole proprie.

''' +t[end:]
pos=t.index('In prova, il tema richiede equilibrio.')
t=t[:pos]+'''### Laboratorio di composizione: traccia, scaletta e revisione

**Traccia originale di allenamento, non tema ufficiale:** «Spiega come l’uso di servizi pubblici digitali possa favorire l’accesso e quali condizioni occorrano per non escludere le persone con minori competenze». La richiesta contiene un beneficio e un problema: svilupparne soltanto uno lascerebbe incompleta la risposta.

**Scaletta:** definire accesso; mostrare il vantaggio della disponibilità a distanza; introdurre difficoltà di competenze, strumenti e comprensione; discutere assistenza e canali accessibili; concludere con un criterio di valutazione del servizio. Non occorrono statistiche inventate per rendere concreto l’argomento.

**Passaggio debole:** «Oggi tutto è digitale e chi non sa usare internet resta sempre escluso; basta fare più corsi e il problema scompare». Le due generalizzazioni assolute non sono dimostrate; il rimedio unico ignora barriere differenti.

**Passaggio revisionato:** «Un servizio accessibile a distanza può ridurre spostamenti e attese, ma il vantaggio dipende dalla possibilità di comprendere e completare la procedura. Una persona priva di dispositivo o di competenze può incontrare un nuovo ostacolo. Istruzioni chiare e assistenza permettono di affrontare difficoltà diverse; dove necessario, un canale alternativo evita che l’accesso dipenda soltanto dall’autonomia digitale».

La revisione mantiene una tesi verificabile, distingue le condizioni e collega ogni soluzione al problema. Per completare l’elaborato sviluppa un esempio di domanda con allegati e ricevuta e valuta se l’utente riesca a concluderla. Rileggi infine il testo cercando affermazioni assolute, nessi mancanti e ripetizioni: la correzione deve migliorare il ragionamento oltre alla grammatica.

''' +t[pos:]
t=t.replace('Una banca dati chiusa, una prova ispettiva compressa, un componimento, un tema e una preselezione richiedono abilità diverse.','Funzione selettiva, formato e provenienza dei quesiti richiedono controlli distinti e possono coesistere nella stessa prova.')
t=t.replace('“Perché un candidato non dovrebbe preparare nello stesso modo una banca dati ufficiale, un componimento di italiano e una preselezione?”','“Come distingui funzione, formato e provenienza dei quesiti?”')
t=t.replace('1. La prova scritta è: banca dati, quiz, componimento, tema, cultura generale, preselezione o altro formato indicato.','1. La funzione è: filtro o prova con voto finale; il formato è: quiz o elaborato; la banca ufficiale è: prevista completa, parziale, non prevista oppure ancora da verificare.')
t=t.replace('Indica tre differenze tra componimento di italiano e tema o prova di cultura generale.','Confronta lo scritto a 60 quesiti dei Carabinieri 898 con la composizione italiana GdF 983: formato, esercitazione e criterio di superamento.')
t=t.replace('Per il componimento di italiano nell’Arma dei Carabinieri e per il tema o prova di cultura generale nella Guardia di Finanza,','Per la prova d’italiano a quesiti CC 898 e la composizione italiana GdF 983 del 2026,')
t=t.replace('Se la prova è una banca dati, l’output deve includere quesiti, errori e simulazioni.','Se la prova è a quiz e attinge a una banca dati, l’output deve includere quesiti, errori e simulazioni.')
p.write_text(t,encoding='utf-8');print('SP01/01 e03: mappa concreta, classificazione e italianoCC/GdF')
