from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02');p=next(base.glob('04-*.md'));backup=art/'before-fl04'/p.name
if backup.exists():raise RuntimeError('Capitolo 04 già modificato')
t=p.read_text(encoding='utf-8');backup.write_text(t,encoding='utf-8')
def add(anchor,body):
 global t
 assert t.count(anchor)==1,anchor
 t=t.replace(anchor,body.strip()+'\n\n'+anchor)
t=t.replace('- L. 177/2024 come fonte di aggiornamento obbligatorio.', '- Comportamenti, documenti, revisione, assicurazione, alcol e stupefacenti nel testo vigente.')
t=t.replace('- usare la L. 177/2024 come avviso di aggiornamento e non come lista di sanzioni da ripetere a memoria.', '- applicare le principali regole di comportamento, distinguere controlli documentali e violazioni sostanziali e riconoscere le conseguenze della guida con alcol o dopo assunzione di stupefacenti.')
add('## N-FL04-04-04', '''### La gerarchia dei segnali in un incrocio

Gli artt. 38 e 43 stabiliscono quale indicazione seguire quando segnali diversi convivono. Le indicazioni dell'agente che regola il traffico prevalgono su ogni altra segnalazione. I semafori, escluso il giallo lampeggiante, prevalgono sui segnali verticali e orizzontali di precedenza; i segnali verticali prevalgono su quelli orizzontali. Vanno rispettati anche i segnali temporanei, benché contrastanti con quelli permanenti.

Il braccio alzato verticalmente indica arresto per tutti, salvo chi non possa fermarsi in sicurezza o abbia già impegnato l'intersezione. Le braccia distese orizzontalmente arrestano le direzioni che le intersecano e consentono quelle parallele, secondo la configurazione dell'art. 43.

**Caso.** Il semaforo è verde, ma l'agente ordina l'arresto per far passare un mezzo di soccorso: il conducente si ferma. Non può invocare il verde. Se invece l'agente non sta regolando il traffico, il semplice fatto che sia presente non disattiva i segnali.

### Comportamenti: dalla regola alla conseguenza

| Condotta | Regola essenziale | Cosa dimostrare nell'accertamento |
|---|---|---|
| Velocità, artt. 141–142 | Rispettare il limite e adattare l'andatura a visibilità, traffico, fondo e utenti | Velocità o comportamento, condizioni, limite applicabile e fonte della prova |
| Precedenza, art. 145 | Massima prudenza; precedenza a destra salvo diversa disciplina; regole specifiche per rotaia e uscita da area privata | Provenienza, segnali, manovra e possibilità di liberare l'incrocio |
| Rosso, art. 146 | Arresto secondo la segnalazione luminosa | Fase semaforica, posizione e condotta osservata |
| Sorpasso, art. 148 | Visibilità e spazio sufficienti, nessun pericolo o intralcio, rispetto di divieti ed eccezioni | Manovre dei veicoli, visuale, segnalazioni e spazio disponibile |
| Cinture e bambini, art. 172 | Dispositivi usati durante la marcia; ritenuta omologata per bambini sotto 1,50 m, salvo eccezioni previste | Occupanti, dispositivo, uso effettivo ed eventuale esenzione documentata |
| Telefono e dispositivi, art. 173 | Vietato uso che comporta allontanamento delle mani; ammessi i sistemi consentiti senza uso delle mani | Uso concreto del dispositivo, non sola presenza nell'abitacolo |

La velocità massima generale è 50 km/h nei centri abitati, 90 sulle extraurbane secondarie e locali, 110 sulle extraurbane principali e 130 sulle autostrade. Restano i limiti propri delle categorie di veicoli e quelli legittimamente segnalati; con precipitazioni i massimi sono 90 sulle extraurbane principali e 110 sulle autostrade. L'art. 141 impone comunque una velocità adeguata: viaggiare a 45 km/h in un tratto con limite 50 può essere imprudente se la visuale è ridotta e vi sono pedoni.

L'art. 142 distingue l'eccesso non superiore a 10 km/h, quello oltre 10 e fino a 40, oltre 40 e fino a 60, e oltre 60. Nelle ultime due fasce si aggiunge la sospensione, rispettivamente da uno a tre e da sei a dodici mesi, ferme le altre condizioni della norma. Se l'eccesso oltre 10 e fino a 40 avviene in centro abitato almeno due volte nell'anno, la disciplina vigente prevede 220–880 euro e sospensione da quindici a trenta giorni. Occorre distinguere questa reiterazione dal regime degli accertamenti ravvicinati nell'ora previsto dal comma 6-ter.

Nel sorpasso di un velocipede il veicolo a motore mantiene una distanza laterale adeguata e, ove le condizioni della strada lo consentano, almeno 1,5 metri. La clausola non autorizza a passare comunque troppo vicino: se non c'è spazio per una manovra sicura, la manovra non si esegue.

Le cinture riguardano anche i passeggeri posteriori dei veicoli cui si applica l'obbligo. Per il minore risponde il conducente oppure il soggetto tenuto alla sorveglianza, se presente. Il dispositivo antiabbandono è richiesto per bambini sotto quattro anni nelle categorie e condizioni dell'art. 172, comma 1-bis. L'appartenenza alla Polizia locale non crea un'esenzione generale dalle cinture: la previsione riguarda il servizio di emergenza.

L'uso vietato del telefono comporta, alla prima violazione, 250–1.000 euro e sospensione da quindici giorni a due mesi; nella reiterazione biennale gli importi diventano 350–1.400 euro e la sospensione da uno a tre mesi. È distinta la sospensione breve dell'art. 218-ter: per violazioni tassativamente elencate e conducente identificato al momento del fatto, richiede meno di venti punti sulla patente. Dura sette giorni con almeno dieci punti, quindici sotto dieci; raddoppia se il conducente provoca un incidente. Non richiede un provvedimento prefettizio, ma va coordinata con le sospensioni già previste. Non basta quindi dire «violazione con perdita di punti uguale sospensione breve».
''')
add('## N-FL04-04-05', '''### Patente, documenti, revisione e assicurazione

Il controllo documentale distingue quattro domande: il soggetto è abilitato? Il titolo è valido e corrisponde al veicolo? I documenti sono disponibili? Il veicolo può circolare?

L'art. 116 disciplina categorie e abilitazioni. Per esempio, la patente B ordinaria abilita agli autoveicoli entro 3.500 kg e non più di otto passeggeri oltre al conducente; traino, codici ed estensioni richiedono le condizioni specifiche previste dal Codice. Non si deduce l'abilitazione dal solo possesso di una patente qualsiasi.

L'art. 180 richiede i documenti pertinenti, fra cui documento di circolazione, patente valida e corrispondente e certificato assicurativo, oltre ai titoli professionali ove prescritti. Avere dimenticato un documento e non possedere affatto il titolo sono situazioni differenti. Se esistenza e validità sono verificabili nelle banche dati accessibili agli organi di polizia stradale, il comma 8 esclude l'invito a esibire, salvo impossibilità tecnica di accesso: il controllo non deve imporre automaticamente un passaggio documentale superfluo.

| Verifica | Regola | Conseguenza da distinguere |
|---|---|---|
| Revisione di un'autovettura ordinaria, art. 80 | Prima entro quattro anni dall'immatricolazione, poi ogni due; alcune categorie sono annuali | Omessa revisione comporta sanzione e sospensione dalla circolazione sino alla revisione; ammesso il tragitto al solo scopo previsto dalla norma |
| Copertura assicurativa, art. 193 | Il veicolo non circola senza copertura; anche il proprietario deve verificarla se lo affida ad altri | Cessazione della circolazione e sequestro, oltre alla sanzione; restituzione o ulteriori conseguenze seguono le condizioni della norma |
| Patente o certificato dimenticato | Verificare esistenza e validità del titolo e modalità documentali ammesse | Non equivale automaticamente a guida senza abilitazione o senza copertura |

La revisione tutela le condizioni tecniche del mezzo; l'assicurazione la responsabilità civile verso terzi. Il controllo positivo di una non prova l'altra. Un'autovettura assicurata con revisione omessa non è per questo liberamente utilizzabile; l'avvenuta revisione non rende assicurato il mezzo. Anche sospensione dalla circolazione per revisione, sequestro per assicurazione e sospensione della patente sono misure diverse, riferite a oggetti e presupposti differenti.
''')
start=t.index('### 6. L. 177/2024:');end=t.index('### Caso guidato:',start)
t=t[:start]+'''### Alcol e stupefacenti: fattispecie diverse

Per un conducente ordinario, l'art. 186 distingue queste fasce di tasso alcolemico:

| Valore accertato | Natura e conseguenze di base |
|---|---|
| Oltre 0,5 e fino a 0,8 g/l | Illecito amministrativo; sospensione della patente da tre a sei mesi |
| Oltre 0,8 e fino a 1,5 g/l | Reato con ammenda e arresto; sospensione da sei mesi a un anno |
| Oltre 1,5 g/l | Reato con trattamento più grave; sospensione da uno a due anni e disciplina della confisca, salvo condizioni ed eccezioni previste |

I valori di confine contano: **0,8 rientra nella prima fascia, 1,5 nella seconda**. Incidenti provocati, reiterazione e appartenenza del veicolo incidono sulle conseguenze: non si trasferisce automaticamente a ogni caso il trattamento della situazione base. Per minori di ventuno anni, primi tre anni di patente B e categorie professionali o veicoli indicati dall'art. 186-bis opera il tasso zero: un valore superiore a zero e non oltre 0,5 è già sanzionato amministrativamente. Non va applicata indistintamente la soglia ordinaria a un neopatentato.

Il rifiuto degli accertamenti ha una propria fattispecie: non significa semplicemente attribuire d'ufficio al conducente il valore più alto. Le modalità dell'accertamento e gli avvertimenti difensivi devono essere rispettati. La riforma del 2024 ha inoltre previsto, per i condannati nelle fasce penali dell'art. 186, i codici unionali 68 e 69 sulla patente, relativi ad assenza di alcol e uso di veicoli con alcolock. La durata minima è, rispettivamente, due o tre anni dalla restituzione dopo la condanna, ferma la disciplina della revisione e dell'attuazione tecnica.

L'art. 187 riguarda la guida dopo assunzione di stupefacenti. La **Corte costituzionale, sentenza 10/2026**, ha chiarito che non basta una positività remota: occorre una prossimità alla guida e una sostanza che, per qualità e quantità scientificamente valutate, sia idonea ad alterare le capacità dell'assuntore medio. Non è però ripristinata la prova dell'effettiva alterazione individuale richiesta dalla versione precedente. Il test preliminare e l'analisi di conferma non sono equivalenti; il ritiro cautelare della patente in attesa dell'esito, fino a dieci giorni nei presupposti del comma 5-bis, non è la sanzione definitiva.

**Tre microcasi risolti.**

1. Conducente ordinario, tasso 0,8 g/l: fascia amministrativa dell'art. 186. Se invece ha vent'anni, va applicata anche la disciplina speciale dell'art. 186-bis.
2. Conducente ordinario, tasso 1,1 g/l: fascia penale intermedia. Si attivano gli atti di PG e le conseguenze sulla patente, senza trattare tutto come pagamento di un verbale amministrativo.
3. Test che rivela tracce riferibili a un'assunzione remota: la positività da sola non risolve il caso dell'art. 187. Servono riscontri tossicologici e temporali pertinenti; non si conclude automaticamente né per il reato né per l'irrilevanza senza verificarli.

''' + t[end:]
t=t.replace('- La L. 177/2024 impone di verificare il testo vigente prima di citare regole puntuali, termini o importi.', '- Alcol, stupefacenti e rifiuto degli accertamenti hanno presupposti distinti; documento dimenticato, titolo mancante e mezzo irregolare non coincidono.')
# Replace two generic checks with substantive application, preserving numbering and four answers.
a=t.index('### Quiz 4');z=t.index('### Quiz 6',a)
t=t[:a]+'''### Quiz 4

Il semaforo è verde, ma l'agente che regola l'incrocio ordina l'arresto. Quale regola si applica?

A. Prevale il verde se non esiste un'ordinanza temporanea scritta.
B. Prevale l'indicazione dell'agente.
C. L'agente prevale soltanto sui segnali orizzontali.
D. Il conducente può scegliere l'indicazione che permette il transito.

**Risposta corretta: B.** Gli artt. 38 e 43 attribuiscono prevalenza alle indicazioni dell'agente che regola il traffico; non occorre che il conducente riceva anche un'ordinanza scritta.

### Quiz 5

Un conducente di trentacinque anni, titolare da dieci anni di patente B e fuori dalle categorie speciali, presenta 0,8 g/l. Quale classificazione iniziale è corretta?

A. Fascia penale intermedia, perché 0,8 è compreso nel limite inferiore.
B. Nessuna violazione, perché la soglia ordinaria è 0,8.
C. Fascia penale più grave, con confisca in ogni caso.
D. Fascia amministrativa oltre 0,5 e fino a 0,8, con le conseguenze previste.

**Risposta corretta: D.** La fascia penale intermedia richiede un valore superiore a 0,8. Le condizioni della traccia escludono il regime speciale dell'art. 186-bis.

''' + t[z:]
t=t.replace('- decreto legislativo 30 aprile 1992, n. 285, Codice della strada, in particolare artt. 7, 11 e 12;', '- decreto legislativo 30 aprile 1992, n. 285: artt. 7, 11–12, 38, 43, 80, 116, 141–148, 172–173, 180, 186–187, 193 e 218-ter;\n- Corte costituzionale, sentenza 29 gennaio 2026, n. 10, sull’art. 187;')
source='sources/vol-02-pl-strada-verifica-2026-10-03'
for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
t=re.sub(r'^volume_chapter:.*$','volume_chapter: 38',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf-8')
statepath=art/'VOL-02-changes.json';s=json.loads(statepath.read_text(encoding='utf-8'));s['changes']['V02-40']={'files':[p.as_posix()],'change':'Regole stradali, segnaletica, documenti/revisione/assicurazione, fasce alcol e art.187 interpretato da Corte10/2026, riforma2024 e sospensione breve.','evidence':'Fonte vigente consolidata; casi numerici0,8/1,1 e tasso zero; quiz4/5 risolti; distinzione misure su veicolo e patente.','status':'Applicato; riesame trasversale e gate 15 ancora aperti'};statepath.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('FL04/04 applicato, V02-40')
