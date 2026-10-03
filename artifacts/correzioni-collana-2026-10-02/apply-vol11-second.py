from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile/chapters');SOURCE='sources/vol-11-rifiuti-controlli-rettifiche-2026-10-03'
def get(n):p=next(B.glob(f'{n:02d}-*.md'));return p,p.read_text(encoding='utf8')
def add(t,n,c,x):
 pat=rf'(^## N-TR04-{n:02d}-{c:02d}[^\n]*\n)';assert re.search(pat,t,re.M);return re.sub(pat,lambda m:m[1]+'\n'+x.strip()+'\n\n',t,count=1,flags=re.M)
def save(p,t):
 for key,val in [('source_refs',SOURCE),('last_compiled_from','wiki/'+SOURCE+'.md'),('topics','topics/ambiente-rettifiche-2026')]:
  m=re.search(r'^'+key+r': (\[.*\])$',t,re.M);a=json.loads(m[1]);a.append(val) if val not in a else None;t=t[:m.start(1)]+json.dumps(a,ensure_ascii=False)+t[m.end(1):]
 t=re.sub(r'^updated_at: .*$', 'updated_at: 2026-10-03',t,flags=re.M);t=re.sub(r'^draft_stage: .*$', 'draft_stage: revision-in-progress',t,flags=re.M);t=re.sub(r'^review_required: .*$', 'review_required: true',t,flags=re.M);p.write_text(t,encoding='utf8')
p,t=get(6)
t=add(t,6,1,'''### Quando il recupero produce un materiale che non è più rifiuto

L'art. 184-ter richiede un'operazione di recupero e criteri che dimostrino uso specifico, mercato o domanda, rispetto dei requisiti tecnici e delle norme sui prodotti, assenza di impatti complessivi negativi per ambiente e salute. Il valore economico non è sufficiente. Si applicano i criteri europei pertinenti; in loro mancanza quelli nazionali; in assenza di criteri specifici, l'autorizzazione caso per caso stabilisce i criteri dettagliati previsti dalla legge, con il parere obbligatorio e vincolante di ISPRA o ARPA competente.

La verifica copre rifiuti in ingresso, trattamento consentito, qualità in uscita, sistema di gestione e dichiarazione di conformità. **Caso risolto:** un impianto vende materiale recuperato ma non ha verificato il parametro previsto dal proprio criterio di cessazione. La fattura e l'esistenza dell'acquirente non dimostrano l'end of waste: manca una condizione della verifica. Fino alla cessazione legittima continua ad applicarsi la disciplina dei rifiuti.''')
t=add(t,6,3,'''### Codici reali e voci specchio

Il codice **15 01 01** identifica imballaggi in carta e cartone. Nel caso didattico di scatole vuote, pulite e non contaminate provenienti dall'apertura di confezioni, la classificazione segue materiale e origine. Se l'imballaggio contiene residui di sostanze pericolose o ne è contaminato, occorre invece valutare **15 01 10*** secondo le caratteristiche reali; non basta osservare che il contenitore è di carta.

Una coppia specchio è **17 05 03***, terre e rocce contenenti sostanze pericolose, e **17 05 04**, terre e rocce diverse dalla precedente voce. Per scegliere servono processo, storia, sostanze plausibili, rappresentatività dei campioni e valutazione delle caratteristiche di pericolo. Le sigle **HP** identificano proprietà come infiammabilità, tossicità, corrosività o ecotossicità secondo i criteri applicabili. L'asterisco segnala la voce pericolosa; non spiega da solo quali HP siano pertinenti.

**Esercizio:** lo scavo è qualificato come rifiuto; la scheda, completa e rappresentativa secondo la traccia, esclude le caratteristiche di pericolo pertinenti dopo aver individuato tutte le sostanze plausibili. La voce da motivare è 17 05 04. Se manca l'indagine sulla contaminazione storica, la stessa conclusione non è ancora sostenibile. Un superamento della CSC del suolo non attribuisce automaticamente una HP: bonifica del sito e classificazione del rifiuto applicano criteri e finalità diversi.''')
t=add(t,6,4,'''### Titolo dell'impianto e titolo del trasportatore

L'art. 208 disciplina l'autorizzazione per nuovi impianti di recupero o smaltimento, con raccordo alla VIA quando necessaria; nei casi assoggettati ad AIA questa sostituisce il titolo secondo la disciplina integrata. Gli artt. 214 e 216 prevedono invece procedure semplificate soltanto per attività, tipi, quantità e condizioni tecniche ammesse: ordinariamente l'attività di recupero può iniziare decorsi 90 giorni dalla comunicazione, ferme verifiche e disposizioni speciali. La comunicazione non rende ammissibile un rifiuto estraneo al perimetro tecnico.

L'iscrizione all'Albo gestori ambientali dell'art. 212 riguarda attività quali raccolta/trasporto, commercio/intermediazione senza detenzione e bonifiche; non sostituisce l'autorizzazione del sito di trattamento. Il trasporto dei propri rifiuti può seguire il regime specifico del comma 8, con requisiti e limiti propri. Nella scheda di filiera verifica separatamente iscrizione, categoria, classe, mezzi e rifiuti del trasportatore, poi titolo, operazione e rifiuti accettabili dell'impianto. **Errore da correggere:** «È iscritto all'Albo, quindi può recuperare qualsiasi rifiuto nel proprio capannone». L'iscrizione non prova né autorizzazione dell'impianto né ammissibilità del flusso.''')
t=add(t,6,5,'''### Chi si iscrive e chi è escluso

Al 3 ottobre 2026, l'art. 188-bis, comma 3-bis, come modificato dalla L. 199/2025, comprende enti e imprese che trattano rifiuti, produttori di rifiuti pericolosi, operatori professionali di raccolta/trasporto e commercio/intermediazione di pericolosi e, per i non pericolosi, i soggetti richiamati dall'art. 189, comma 3. Esclude i consorzi e sistemi dell'art. 237, comma 1, e i produttori cui si applicano i commi 5 e 6 dell'art. 190.

Fra i casi da distinguere vi sono produttori iniziali di soli rifiuti non pericolosi con non più di dieci dipendenti, agricoltori nei presupposti normativi, attività espressamente individuate e produttori non organizzati in ente o impresa. L'esclusione per i piccoli produttori di non pericolosi non si estende a ogni impresa con meno di undici dipendenti che produca pericolosi. Una piccola officina produttrice di pericolosi non è esclusa per la sola dimensione; una fattispecie particolare deve risultare dalla norma.

L'art. 190 prevede per i produttori annotazioni entro **10 giorni lavorativi** da produzione e scarico; per chi recupera o smaltisce entro **2 giorni lavorativi** dalla presa in carico. La conservazione ordinaria del registro è di **3 anni** dall'ultima annotazione, con regole speciali per discariche. Iscrizione, registro, FIR e MUD vanno verificati separatamente: un'esclusione da RENTRI non cancella automaticamente gli altri obblighi.''')
t=t.replace('### Dato operativo — transizione del FIR nel 2026','### Dato operativo — FIR digitale dal 16 settembre 2026')
a=t.index("Alla data dell'11 agosto 2026");b=t.index('\n\n- **Fonte ufficiale:**',a)
t=t[:a]+"Al 3 ottobre 2026, la fase transitoria che consentiva agli iscritti di scegliere il FIR cartaceo per ciascun trasporto è conclusa: dal **16 settembre 2026** il FIR digitale è obbligatorio per i soggetti iscritti al RENTRI. I non iscritti continuano a usare il FIR cartaceo nei casi in cui è richiesto. Le eventuali procedure di sicurezza per indisponibilità dei servizi sono disciplinate dalle istruzioni ufficiali e non ricreano una facoltà generale di scegliere il cartaceo."+t[b:]
t=t.replace("quadro controllato l'11 agosto 2026.","quadro del FIR e indicazioni RENTRI verificati il 3 ottobre 2026.")
t=t.replace('- **Audit:** prima dell\'applicazione pratica va verificata la pagina ufficiale RENTRI, perché decreti direttoriali e aggiornamenti tecnici possono modificare modalità e specifiche operative.',"- **Uso del dato:** verificare le modalità tecniche di continuità del servizio sul portale RENTRI; la gestione documentale richiede competenza ambientale e conoscenza dei ruoli della filiera.")
t=t.replace('Durante la transizione, l\'organizzazione deve evitare una gestione ibrida della stessa movimentazione. Se per un trasporto si sceglie il formato digitale, produttore, trasportatore e destinatario devono operare in modo coerente con quel formato. La scelta va compiuta prima della partenza, verificando che tutti gli attori siano pronti.',"Nella gestione digitale, produttore, trasportatore e destinatario devono operare in modo coerente lungo la stessa movimentazione. Prima della partenza si verifica che tutti gli attori siano abilitati e che i dati del carico corrispondano alla classificazione.")
t=add(t,6,6,'''### Registro e FIR: esempio compilato e riconciliato

**Ipotesi:** un'impresa iscritta al RENTRI produce imballaggi di cartone puliti, EER 15 01 01. Tutti i nomi e gli estremi seguenti sono didattici. Il 5 ottobre 2026 produce 120 kg e registra il carico C01 nei termini; il 7 ottobre produce altri 80 kg e registra C02. Il 9 ottobre affida 150 kg al trasportatore T, la cui iscrizione comprende quel flusso e il mezzo usato, per l'impianto R autorizzato all'operazione indicata nel titolo.

La scheda del FIR digitale contiene produttore e unità locale, EER 15 01 01, descrizione «imballaggi in carta e cartone», stato fisico solido, quantità 150 kg, trasportatore e mezzo, destinatario, estremi dei titoli verificati, operazione di destinazione, data e percorso. Le HP non sono attribuite perché il flusso è non pericoloso nelle ipotesi del caso. Non si inventano numeri di autorizzazione: nel modulo di allenamento si scrive «estremo didattico T» e «estremo didattico R».

**Soluzione:** carichi totali 120 + 80 = 200 kg; uscita 150; giacenza 50 kg. Lo scarico S01 richiama il FIR e i movimenti di carico pertinenti. Se il destinatario accetta 148 kg, si conserva la tracciabilità del dato iniziale e si riconcilia l'esito secondo le regole del sistema: non si cancella il FIR per far tornare il saldo. Nel caso il candidato deve chiedere se i 2 kg derivino da differenza di pesatura o da rifiuto non accettato, perché le due situazioni non hanno lo stesso significato. La formula aritmetica controlla i dati; non sostituisce la gestione dell'anomalia.''')
save(p,t)
p,t=get(7)
t=t.replace('e occorre compensare altrove la perdita residua','e occorre recuperare risorse o servizi equivalenti, anche in un sito alternativo se opportuno')
t=add(t,7,1,'''### Il caso di uguaglianza alla soglia

La definizione dell'art. 240, lettera f), usa la parola «inferiore». Nel decidere il percorso occorre però leggere anche le disposizioni sul **superamento**: l'art. 242, comma 2, riguarda CSC non superate; l'art. 240, lettera p), definisce l'obiettivo della bonifica come concentrazioni uguali o inferiori alle CSR. Il valore esattamente uguale non è superiore e non va trasformato automaticamente in contaminazione.

**Esempio didattico:** per lo stesso parametro e la stessa matrice la traccia assegna CSC = 50 mg/kg e CSR approvata = 120 mg/kg. I numeri sono ipotesi, non limiti nazionali di una sostanza specifica. Con 50 mg/kg la CSC non è superata; con 80 la CSC è superata e il sito è inizialmente potenzialmente contaminato, ma l'analisi approvata può collocare il valore sotto la CSR; con 150 è superata anche la CSR. Un risultato finale di bonifica di 120 raggiunge, per quel parametro e nelle condizioni del progetto, l'obiettivo uguale alla CSR. La chiusura richiede comunque verifica degli altri parametri, matrici, condizioni e atti: non basta una singola uguaglianza numerica.''')
t=add(t,7,3,'''### Calendario della procedura ordinaria

| Passaggio | Termine e decorrenza |
|---|---|
| Caratterizzazione dopo CSC superata | Piano nei successivi 30 giorni; autorizzazione regionale nei 30 successivi |
| Analisi di rischio | Presentazione entro 6 mesi dall'approvazione del piano di caratterizzazione |
| Approvazione dell'analisi | Entro 60 giorni dalla ricezione, con conferenza e contraddittorio |
| Progetto se CSR superate | Entro 6 mesi dall'approvazione dell'analisi |
| Approvazione del progetto | Entro 60 giorni dal ricevimento, con disciplina delle integrazioni |

Il calendario deriva dall'art. 242 e non comprende indistintamente ogni sospensione o procedura speciale. La prevenzione entro 24 ore e la comunicazione immediata non attendono questi termini. Se le CSC non sono superate, l'autocertificazione del ripristino segue entro 48 ore dalla comunicazione e i controlli nei successivi 15 giorni. Per un sito che supera le CSR non è corretto depositare soltanto un piano di monitoraggio: occorre il progetto di intervento previsto dal procedimento.''')
t=t.replace("gli interventi necessari sono realizzati dall'amministrazione competente secondo l'articolo 250.","gli interventi dell'art. 242 sono realizzati d'ufficio dal Comune territorialmente competente e, se questo non provvede, dalla Regione, secondo l'art. 250 e le priorità regionali.")
t=add(t,7,6,'''### Responsabilità e confini della Parte sesta

L'art. 298-bis della Parte sesta distingue il danno causato dalle attività professionali dell'allegato 5, per le quali il criterio non richiede la prova di dolo o colpa, dal danno causato da altre attività, per cui occorre un comportamento doloso o colposo. Anche nel primo caso restano necessari il danno o la minaccia rilevante e il collegamento causale con l'operatore: «responsabilità oggettiva» non significa responsabilità di chiunque possieda il terreno.

L'art. 303 delimita l'applicazione, fra l'altro per eventi eccezionali tipizzati, particolari regimi internazionali e nucleari, danni anteriori alla disciplina, decorso di oltre trent'anni e inquinamento diffuso quando non sia accertabile il nesso con singoli operatori. Queste esclusioni non cancellano automaticamente ogni altra tutela o il procedimento di bonifica. **Caso:** una perdita da attività inclusa nell'allegato 5 richiede verifica di evento, risorsa e causalità; non basta discutere se il gestore abbia adottato una generica diligenza. Per una diversa attività, la verifica di dolo o colpa entra invece nel presupposto descritto dalla norma.''')
save(p,t)
p,t=get(8)
t=add(t,8,2,'''### Valori e tempi di mediazione

Il **valore limite** è una concentrazione da raggiungere entro il termine normativo e poi non superare secondo il criterio previsto; il **valore obiettivo** mira a evitare o ridurre effetti nocivi, da conseguire ove possibile con le misure richieste. La **soglia di informazione** segnala un rischio per gruppi particolarmente sensibili dopo esposizione breve; la **soglia di allarme** riguarda il rischio per la popolazione nel suo complesso e richiede interventi immediati secondo la disciplina. Le quattro categorie non sono intercambiabili.

Riferimenti del D.Lgs. 155/2010 verificati al 3 ottobre 2026:

| Inquinante | Periodo | Criterio |
|---|---|---|
| PM10 | Giorno | 50 µg/m³, non oltre 35 superamenti per anno |
| PM10 | Anno | Media 40 µg/m³ |
| NO2 | Ora | 200 µg/m³, non oltre 18 superamenti per anno |
| NO2 | Anno | Media 40 µg/m³ |

**Caso:** una stazione ha media annua PM10 di 32 µg/m³ e 38 giorni oltre 50. Il limite sulla media annuale è rispettato, mentre non lo è il criterio dei superamenti giornalieri: 38 è maggiore di 35. La media non annulla i picchi. Confrontare un valore orario con un limite giornaliero senza aggregare correttamente il dato produce invece una conclusione non valida.

La direttiva (UE) 2024/2881 prevede un nuovo quadro e il recepimento entro l'11 dicembre 2026. Alla verifica, il fascicolo parlamentare italiano acquisito riguarda lo schema, Atto del Governo 435. Le soglie future non vanno applicate anticipatamente al caso corrente; anno di riferimento, norma e periodo di mediazione devono restare espliciti.''')
t=add(t,8,4,'''### Classi acustiche e limiti assoluti di immissione

La Tabella C del DPCM 14 novembre 1997 distingue i seguenti limiti di Leq in dB(A), riferiti all'insieme delle sorgenti nell'ambiente esterno, nei presupposti di applicazione del decreto.

| Classe e uso | Diurno, 6–22 | Notturno, 22–6 |
|---|---:|---:|
| I, particolarmente protette | 50 | 40 |
| II, prevalentemente residenziali | 55 | 45 |
| III, tipo misto | 60 | 50 |
| IV, intensa attività umana | 65 | 55 |
| V, prevalentemente industriali | 70 | 60 |
| VI, esclusivamente industriali | 70 | 70 |

I limiti di emissione della singola sorgente appartengono alla diversa Tabella B: non usare la Tabella C per rispondere a una domanda sull'emissione. Per infrastrutture di trasporto e fasce di pertinenza occorre inoltre il regime specifico.

Il **differenziale** confronta rumore ambientale con sorgente attiva e rumore residuo senza quella sorgente negli ambienti abitativi: limite 5 dB diurno e 3 notturno. L'art. 4 esclude, fra l'altro, la classe VI e le sorgenti del comma 3; prevede inoltre soglie di trascurabilità inferiori a 50/40 dB(A) a finestre aperte e a 35/25 a finestre chiuse. Il controllo considera tutte le condizioni pertinenti: non basta dire che ogni differenza superiore a 5 sia sanzionabile.

**Caso risolto:** in classe III, fuori dalle fasce speciali, Leq esterno diurno 62 dB(A) contro 60 indica uno scostamento di 2 dB. In abitazione, nelle condizioni corrette e senza esclusioni applicabili, ambientale 56 e residuo 49 danno differenziale 7, superiore a 5. Sono due verifiche distinte; il confronto interno non sostituisce quello esterno.''')
t=add(t,8,5,'''### Leq, Lden e Lnight

Il **Leq** è il livello continuo equivalente che rappresenta l'energia sonora nel periodo considerato; non è una media aritmetica dei decibel. **Lden** descrive l'esposizione di lungo periodo integrando giorno, sera e notte con le penalizzazioni previste; **Lnight** riguarda il periodo notturno nel quadro della mappatura acustica. Sono indicatori della disciplina del rumore ambientale, utili per mappe e piani d'azione, e non si sostituiscono automaticamente al Leq e ai tempi di riferimento usati per verificare la sorgente secondo il DPCM.

Un dato deve quindi riportare indicatore, periodo, punto e metodo. Se una mappa riporta Lden 62 e la classificazione comunale un limite diurno Leq 60, sottrarre 60 da 62 non dimostra da solo una violazione: grandezze e finalità non coincidono.''')
t=add(t,8,6,'''### Accesso alle informazioni ambientali

Il D.Lgs. 195/2005 permette a chiunque di richiedere le informazioni ambientali detenute dall'autorità pubblica senza dichiarare un interesse giuridico. L'art. 3 prevede risposta quanto prima e comunque entro **30 giorni**, estensibili a **60** per entità e complessità, informando il richiedente e motivando entro i primi 30. Una richiesta generica richiede il raccordo previsto dalla legge per precisarla.

L'art. 5 disciplina limiti, come pregiudizi a indagini, sicurezza, riservatezza o tutela di specie rare. Le esclusioni si interpretano restrittivamente, bilanciando l'interesse pubblico all'informazione; dove possibile si concede accesso parziale. Per le informazioni sulle emissioni non sono opponibili alcuni motivi specificamente indicati dal comma 4. Non è quindi corretto rifiutare l'intero rapporto perché contiene anche un dato personale oscurabile.

**Esercizio risolto:** un residente chiede i risultati delle misure di rumore vicino a casa senza allegare un titolo di proprietà. La mancanza del titolo non giustifica il rigetto dell'accesso ambientale. L'ufficio verifica quali informazioni detenga, applica gli eventuali limiti puntuali, oscura quanto necessario e comunica l'esito nei termini. Questa disciplina speciale va distinta dall'accesso documentale ordinario della L. 241/1990.''')
save(p,t)
p,t=get(9)
t=add(t,9,3,'''### Il percorso della L. 689/1981

Quando si applica la disciplina generale, l'art. 14 richiede contestazione immediata se possibile; altrimenti notifica entro **90 giorni dall'accertamento** ai residenti in Italia, **360** all'estero. L'accertamento non coincide necessariamente con il giorno della condotta o con il primo sopralluogo: decorrenza e completezza delle verifiche devono essere motivate secondo il caso.

L'art. 16 consente, quando ammesso, pagamento ridotto entro **60 giorni**: un terzo del massimo oppure, se più favorevole e previsto il minimo, il doppio del minimo, oltre spese. Per regolamenti e ordinanze comunali/provinciali può operare la determinazione della Giunta nei limiti di legge. L'art. 18 consente scritti, documenti e richiesta di audizione entro **30 giorni** dalla contestazione/notifica. L'autorità valuta le difese ed emette ordinanza motivata di ingiunzione o archiviazione. Il termine di pagamento dell'ingiunzione è 30 giorni, 60 per residenti all'estero; non è il termine per l'opposizione giudiziale.

**Calcolo:** minimo 600 euro, massimo 3.000. Un terzo del massimo è 1.000; doppio del minimo 1.200. Nel regime generale applicabile si pagano 1.000 euro più spese. La presentazione di difese non sospende automaticamente il termine per il pagamento ridotto. Prima di usare lo schema si verificano autorità e deroghe della disciplina ambientale specifica.''')
t=add(t,9,4,'''### La pena distingue contravvenzione e delitto

La distinzione formale dipende dalle pene: **arresto e ammenda** per le contravvenzioni; **reclusione, ergastolo e multa** per i delitti. «Multa» non è il nome tecnico generico di ogni pagamento amministrativo. Non confondere neppure arresto come pena e misure processuali limitative della libertà.

L'art. 256, comma 1, nel testo verificato il 3 ottobre 2026, punisce la gestione senza titolo di rifiuti non pericolosi, nella fattispecie ordinaria descritta, con arresto da tre mesi a un anno **o** ammenda da 2.600 a 26.000 euro; se i fatti riguardano rifiuti pericolosi prevede invece reclusione da uno a cinque anni. Le ulteriori condizioni dei commi successivi possono mutare il quadro. Non è più corretto chiamare indistintamente «contravvenzione» tutta la gestione non autorizzata.

**Caso:** l'impresa gestisce rifiuti non pericolosi autorizzati ma viola una prescrizione sul deposito. La traccia esclude i presupposti aggravati, il danno e il pericolo concreto attuale e specifica che il fatto non integra un reato più grave. Va esaminato il comma 4: arresto da due a sei mesi **o** ammenda da 2.000 a 18.000 euro. Se il flusso fosse pericoloso, lo stesso comma prevede reclusione da sei mesi a tre anni nei presupposti indicati, con conseguenze anche sull'accesso alla procedura estintiva.''')
t=add(t,9,5,'''### Sequenza e termini della procedura estintiva

La prescrizione dell'art. 318-ter assegna il tempo tecnicamente necessario. Per circostanze specifiche documentate non imputabili al contravventore, è possibile una sola proroga fino a **6 mesi**, motivata e comunicata al PM. L'organo verifica l'adempimento entro **60 giorni** dalla scadenza del termine prescritto.

Se l'adempimento è regolare, il pagamento deve avvenire entro **30 giorni** dall'ammissione ed è pari a **un quarto del massimo dell'ammenda**, oltre gli oneri tecnici dovuti. L'organo comunica adempimento e pagamento al PM entro **120 giorni dalla scadenza della prescrizione**; comunica invece l'inadempimento entro **90 giorni** dalla medesima scadenza. Questi termini hanno decorrenze diverse dal termine assegnato per regolarizzare.

**Applicazione al caso precedente:** se ricorrono tutti i presupposti della procedura e la fattispecie del comma 4 ha ammenda massima di 18.000 euro, la quota estintiva è 18.000/4 = **4.500 euro**, non un terzo del massimo come nel diverso schema della L. 689. Adempimento e pagamento tempestivi devono concorrere; il pagamento da solo non sana l'attività. La qualificazione come delitto esclude questo percorso. L'adempimento tardivo o con modalità diverse segue la valutazione dell'art. 318-septies, comma 3, e non produce automaticamente lo stesso esito. La sospensione penale non impedisce atti urgenti, incidente probatorio o sequestro preventivo nei presupposti di legge.''')
save(p,t)
print('Capitoli 06–09 integrati; registri/fonti da completare e verifica finale ancora aperta.')
