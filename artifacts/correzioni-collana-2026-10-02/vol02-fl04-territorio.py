from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02')
def get(n):
 p=next(base.glob(n+'-*.md'));a=art/'before-fl04'/p.name
 if a.exists():raise RuntimeError('Già modificato '+n)
 t=p.read_text(encoding='utf-8');a.write_text(t,encoding='utf-8');return p,t
def add(t,a,b):
 assert t.count(a)==1,a
 return t.replace(a,b.strip()+'\n\n'+a)
def save(p,t,source):
 for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
 t=re.sub(r'^volume_chapter:.*$','volume_chapter: '+str(34+int(p.name[:2])),t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf-8')
p,t=get('10')
t=t.replace('L’avvio può dipendere da una segnalazione, da un provvedimento espresso oppure da una comunicazione, secondo la norma speciale.', 'L’avvio può dipendere da una segnalazione, da un’autorizzazione espressa o tacita nei casi ammessi, oppure da una comunicazione, secondo la norma speciale.')
t=t.replace('L’autorizzazione appartiene a una logica preventiva. Quando la norma subordina l’attività a un provvedimento espresso, il privato non può sostituirlo con una propria segnalazione. L’amministrazione deve svolgere la valutazione richiesta e adottare l’atto prima che l’attività sia legittimamente esercitabile, salvo le specifiche regole settoriali.', 'L’autorizzazione appartiene a una logica preventiva, ma non è necessariamente espressa: nei casi ammessi può formarsi per silenzio-assenso. Quando invece la legge richiede un atto espresso o esclude il silenzio-assenso, la sola attesa non abilita all’attività. Il privato non può sostituire il regime autorizzatorio con una SCIA scelta di propria iniziativa.')
t=t.replace('| Autorizzazione | Serve una valutazione preventiva e un provvedimento espresso. | L’atto necessario è stato adottato ed è efficace? |','| Autorizzazione | Assenso preventivo, espresso o formatosi per silenzio nei casi ammessi. | Il titolo esiste ed è efficace secondo il regime applicabile? |')
t=add(t,'## N-FL04-10-03', '''### SCIA unica, condizionata e silenzio-assenso

L'art. 19-bis L. 241/1990 distingue due concentrazioni. La **SCIA unica** raccoglie altre SCIA, comunicazioni, notifiche e attestazioni necessarie: un solo invio, trasmesso dallo sportello alle amministrazioni competenti per i controlli. La **SCIA condizionata** riguarda invece un'attività che richiede assensi, pareri o verifiche preventive: l'interessato presenta l'istanza allo sportello e deve attendere il rilascio degli atti necessari, comunicato dallo sportello, prima di iniziare.

La Tabella A del D.Lgs. 222/2016 collega attività e regime. Nell'apertura di un esercizio di vicinato alimentare, per esempio, la notifica sanitaria si concentra nella SCIA unica; il SUAP la trasmette all'ASL. Se occorre un autonomo assenso preventivo, la pratica unitaria non lo rende già ottenuto. La concessione di suolo pubblico per un dehors resta distinta dal titolo commerciale.

Il **silenzio-assenso**, art. 20, è invece l'effetto che la legge collega al decorso del termine in un procedimento autorizzatorio. Non nasce dalla presentazione di una SCIA e non opera indistintamente per ogni interesse: il comma 4 esclude, fra gli altri, procedimenti riguardanti ambiente, paesaggio, patrimonio culturale, pubblica sicurezza e salute, oltre agli altri casi previsti. Per una media struttura commerciale il regime indicato può contemplare autorizzazione con silenzio-assenso; questo non produce automaticamente l'assenso paesaggistico mancante.

**Esercizio risolto.** Il commerciante presenta SCIA di vicinato alimentare e notifica sanitaria: si ragiona in termini di SCIA unica e controllo dei requisiti. Un secondo progetto richiede anche un assenso preventivo: non parte soltanto perché il portale ha rilasciato ricevuta; occorre il regime condizionato e l'acquisizione dell'atto. In nessuno dei due casi «ricevuta» significa certificazione di conformità universale.
''')
t=add(t,'## N-FL04-10-04', '''### Categorie commerciali e requisiti da conoscere

Il commercio **all'ingrosso** vende a rivenditori o utilizzatori professionali; quello **al dettaglio** al consumatore finale. La superficie di vendita comprende gli spazi destinati alla vendita, anche occupati da banchi e scaffali, ma esclude magazzini, uffici e servizi. È diversa dalla superficie lorda rilevante per altre discipline, come la prevenzione incendi.

| Categoria | Quadro nazionale e differenza utile | Requisiti/regime da verificare |
|---|---|---|
| Esercizio di vicinato | Soglie statali di 150 o 250 m² secondo la classe demografica comunale, da coordinare con la legge regionale | SCIA per apertura, trasferimento e ampliamento; requisiti morali, e professionali se alimentare |
| Media struttura | Sopra il vicinato e fino alle soglie statali di 1.500 o 2.500 m², secondo classe comunale e disciplina regionale | Regime autorizzatorio e relativa disciplina, compreso il silenzio-assenso dove previsto |
| Grande struttura | Oltre la soglia della media struttura | Procedimento e programmazione pertinenti; non si usa la SCIA del vicinato |
| Somministrazione | Attività di consumo/servizio qualificata dalla disciplina di settore | Art. 64 D.Lgs. 59/2010: apertura/trasferimento con autorizzazione nelle zone tutelate; SCIA negli altri casi; requisiti morali e professionali |

Nel quadro statale le soglie inferiori riguardano i comuni sotto 10.000 abitanti e quelle superiori i comuni sopra 10.000; per applicare una traccia territoriale si usa la classificazione della legge regionale, senza dedurre automaticamente dalle sole dimensioni commerciali gli adempimenti sanitari, edilizi o antincendio. Il trasferimento della gestione o titolarità della somministrazione segue la SCIA nei casi dell'art. 64, con effettivo trasferimento dell'attività e requisiti del subentrante.

L'art. 71 D.Lgs. 59/2010 distingue **requisiti morali** e **professionali**. Fra gli impedimenti morali vi sono le categorie di condanne e misure previste dalla norma; riabilitazione, durata degli effetti e sospensione condizionale richiedono la specifica verifica. La somministrazione presenta anche ulteriori impedimenti espressamente indicati. Non basta una generica dichiarazione di «assenza di precedenti» per descrivere correttamente il controllo.

Per il dettaglio alimentare e la somministrazione destinati all'alimentazione umana il requisito professionale può derivare, alternativamente, da:

- corso professionale riconosciuto dalla Regione o Provincia autonoma, superato;
- almeno due anni, anche non continuativi, nel quinquennio precedente, nell'attività e nelle posizioni qualificate previste dalla legge;
- diploma o titolo di studio con materie attinenti a commercio, preparazione o somministrazione alimentare, nei termini dell'art. 71.

Può possederlo il titolare o rappresentante legale oppure il preposto. La nomina del preposto non elimina i requisiti morali richiesti agli altri soggetti. **Esempio:** un diploma privo delle materie pertinenti non diventa idoneo perché il titolare apre un bar; può invece rilevare un preposto effettivamente qualificato, se tutti gli altri presupposti sussistono. Una breve esperienza generica non equivale ai due anni qualificati nel quinquennio.
''')
t=t.replace('- D.P.R. 7 settembre 2010, n. 160', '- D.Lgs. 59/2010, artt. 64, 65 e 71; D.Lgs. 114/1998, art. 4; D.Lgs. 222/2016, Tabella A; L. 241/1990, artt. 19-bis e 20.\n- D.P.R. 7 settembre 2010, n. 160')
save(p,t,'sources/vol-02-pl-commercio-verifica-2026-10-03')
p,t=get('11')
t=t.replace('Il permesso di costruire è un provvedimento espresso necessario per gli interventi che la legge assoggetta a quel titolo.', 'Il permesso di costruire è il titolo richiesto per gli interventi individuati dalla legge; può essere espresso oppure formarsi per silenzio-assenso nei presupposti dell’art. 20, comma 8.')
t=t.replace('| Permesso di costruire | Provvedimento espresso richiesto per le fattispecie indicate dalla legge. | L’atto esiste, è efficace e comprende l’opera realizzata? |','| Permesso di costruire | Titolo espresso o tacito nei casi ammessi, per le fattispecie previste. | Il titolo si è formato, è efficace e comprende l’opera? |')
t=add(t,'## N-FL04-11-03', '''### I confini fra CILA, SCIA e permesso

La **CILA**, art. 6-bis, è residuale rispetto agli interventi degli artt. 6, 10 e 22 e richiede l'asseverazione prevista, anche quanto al mancato interessamento delle parti strutturali. Non è il titolo universale delle opere «piccole». La **SCIA ordinaria**, art. 22, comprende fra l'altro manutenzione straordinaria sulle parti strutturali o sui prospetti, restauro strutturale e ristrutturazioni non assoggettate al permesso: consente l'avvio dalla presentazione quando sono presenti tutti i presupposti, con controllo ordinario edilizio di trenta giorni. La **SCIA alternativa al permesso**, art. 23, opera nelle diverse fattispecie tipizzate ed è presentata almeno trenta giorni prima dell'inizio. Non si scambiano questi due termini: controllo successivo e attesa preventiva hanno funzioni differenti.

Il permesso può formarsi tacitamente alle condizioni dell'art. 20, comma 8. Nei casi con vincoli opera il raccordo previsto con gli assensi di tutela; la L. 182/2025 ammette la specifica ipotesi di assensi formali già acquisiti, validi e riferiti allo stesso intervento e agli stessi elaborati. Il silenzio del Comune non crea un assenso tacito dell'autorità paesaggistica. Nel controllo si verifica quindi anche la corrispondenza degli assensi, non soltanto il decorso del tempo.
''')
t=t.replace('La norma contiene anche ulteriori effetti, da verificare nel testo vigente.', 'Termini, inottemperanza ed effetti sono distinti nella scheda seguente.')
t=add(t,'## N-FL04-11-05', '''### Dall'accertamento alla repressione: termini essenziali

| Passaggio | Regola del DPR 380/2001 | Controllo richiesto |
|---|---|---|
| Sospensione lavori, art. 27 | Provvedimento immediato del dirigente/responsabile nei presupposti; efficacia fino ai provvedimenti definitivi, da adottare e notificare entro 45 giorni | Data, opere interessate, notifica e successivo provvedimento; non sospensione indefinita |
| Comunicazione PG, art. 27, comma 4 | In mancanza di permesso/cartello o presunta violazione, comunicazione immediata a AG, presidente della giunta regionale e dirigente/responsabile | Quest'ultimo verifica entro 30 giorni; la comunicazione penale non aspetta il suo assenso |
| Ingiunzione ex art. 31 | Proprietario e responsabile devono rimuovere/demolire e ripristinare, nei presupposti tipizzati | Individuazione dell'opera, soggetti e area acquisibile |
| Inottemperanza | Termine ordinario 90 giorni; proroga motivata fino al massimo di 240 nei casi tassativi di salute, assoluto bisogno o grave disagio socioeconomico | Non tutte le richieste dell'interessato producono proroga |
| Acquisizione | Nei presupposti, bene, sedime e area necessaria sono acquisiti gratuitamente; area fino al limite di dieci volte la superficie utile abusiva | Accertamento notificato, titolo per possesso e trascrizione; diritti e posizione dei soggetti da verificare |

La sanzione pecuniaria per inottemperanza, da 2.000 a 20.000 euro nel quadro statale, si aggiunge alle altre conseguenze: non compra il diritto di mantenere l'opera. L'opera acquisita segue la demolizione, salvo le rigorose condizioni del comma 5 per diverse determinazioni pubbliche; non basta che il Comune la consideri utile. L'acquisizione non va descritta come estinzione indiscriminata di ogni diritto: la Corte costituzionale n. 160/2024 ha tutelato l'ipoteca anteriore del creditore non responsabile nei termini indicati dalla decisione.

**Caso temporale.** Il dirigente sospende i lavori: il fascicolo deve condurre ai provvedimenti definitivi adottati e notificati entro quarantacinque giorni. Una successiva ingiunzione di demolizione ex art. 31 segue il proprio termine ordinario di novanta giorni. Non si sommano meccanicamente 45 e 90 come un unico termine dell'abuso; ogni atto ha presupposti, decorrenza e funzione propri.

### Tolleranze e sanatorie non si presumono

Le tolleranze dell'art. 34-bis qualificano scostamenti nei presupposti di legge; non sono una sanatoria ottenuta pagando. L'art. 36 riguarda assenza o totale difformità da permesso o SCIA alternativa e richiede conformità urbanistica ed edilizia sia alla realizzazione sia alla domanda. L'art. 36-bis riguarda le diverse ipotesi tipizzate, fra cui parziali difformità e casi di SCIA: richiede conformità urbanistica alla domanda ed edilizia all'epoca della realizzazione, con condizioni e verifiche specifiche. Non esiste quindi una sola «doppia conformità» da ripetere per ogni caso.

La pattuglia documenta epoca e caratteristiche dell'opera e le istanze effettivamente presentate, senza dichiarare da sola l'esito della sanatoria. Per definizioni degli interventi, confronto dei titoli, tolleranze e accertamenti di conformità, l'approfondimento nominativo è nel **VOL-10, «Urbanistica, edilizia ed espropriazioni»**. Qui restano essenziali qualificazione corretta del percorso repressivo e trasmissioni tempestive.
''')
t=add(t,'### Caso guidato: opera senza titolo apparente', '''### Il ramo penale dell'art. 44

L'art. 44 distingue inosservanze di norme e prescrizioni indicate nella lettera a), esecuzione in assenza o totale difformità dal permesso e prosecuzione nonostante la sospensione nella lettera b), lottizzazione abusiva e specifici interventi in aree vincolate nella lettera c). Le conseguenze penali dipendono dagli elementi della fattispecie, non dall'etichetta generica «abuso».

**Esempio risolto.** L'ufficio conferma che una nuova costruzione, osservata in esecuzione, richiede il permesso e ne è priva: oltre alla procedura comunale, il fatto presenta il ramo penale dell'art. 44, lettera b), da comunicare con i riscontri. La sola mancata esibizione della copia del titolo sul posto non dimostra invece quel medesimo fatto: si acquisiscono gli esiti della verifica, ferme le comunicazioni immediate dell'art. 27 nei suoi presupposti.
''')
t=t.replace('Per progettazione, parametri urbanistici, tecnica edilizia e casistica specialistica occorre la preparazione tecnica del relativo modulo avanzato. Il presente capitolo fornisce il metodo operativo richiesto alla Polizia locale.', 'Per progettazione e casistica tecnica ulteriore si rinvia al VOL-10, capitolo «Urbanistica, edilizia ed espropriazioni». I termini e gli atti di vigilanza richiesti al profilo PL sono sviluppati nelle schede di questo capitolo.')
t=t.replace('D. Solo se lo chiede il vicino.','D. Sì, purché l’opera sia ultimata.').replace('D. No, perché le pratiche non hanno mai valore.','D. No: occorre sempre una nuova autorizzazione anche per opere conformi.').replace('D. No, perché l’edilizia non può avere rilievo penale.','D. No: il procedimento penale può iniziare soltanto dopo la demolizione.')
t=t.replace('D. attribuita a chi l’ha resa e distinta dall’osservazione diretta;','D. attribuita a chi l’ha resa e distinta dall’osservazione diretta.')
save(p,t,'sources/vol-02-pl-edilizia-ambiente-verifica-2026-10-03')
p,t=get('12')
t=add(t,'### Caso guidato: materiali in area pubblica', '''### Abbandono: la mappa vigente non è «privato uguale amministrativo»

Le riforme hanno modificato profondamente l'apparato sanzionatorio. Nel testo vigente del D.Lgs. 152/2006 anche l'abbandono ordinario commesso da un privato può essere reato. La qualificazione richiede condotta, tipo di rifiuto, luogo, autore e circostanze.

| Fattispecie | Elementi distintivi | Natura del seguito |
|---|---|---|
| Art. 255, comma 1 | Abbandono/deposito incontrollato ordinario di rifiuti non pericolosi | Penale, ammenda; non ordinario verbale amministrativo al privato |
| Art. 255, comma 1.1 | Medesime condotte da titolare d'impresa o responsabile di ente | Trattamento penale specifico; verificare ruolo e collegamento con attività |
| Art. 255-bis | Non pericolosi nelle condizioni aggravate di pericolo o nei siti e accessi individuati | Delitto; non ogni cumulo integra automaticamente l'aggravante |
| Art. 255-ter | Rifiuti pericolosi, con ulteriori condizioni aggravanti previste | Delitto; pericolosità da accertare, non desunta dal solo aspetto |
| Art. 255, comma 1.2 | Rifiuti urbani accanto ai contenitori stradali, in violazione delle regole di conferimento, salvo che il fatto costituisca reato | Residuo amministrativo: 1.000–3.000 euro, oltre alla misura sul veicolo se usato nei presupposti |
| Art. 255, comma 1-bis | Mozziconi e rifiuti piccolissimi degli artt. 232-bis/ter, fuori dalla specifica fattispecie CdS | Residuo amministrativo: 80–320 euro |

Il CdS, art. 15, comma 1, lettera f-bis, disciplina il deposito o getto dai veicoli in sosta o movimento dei piccoli rifiuti non pericolosi richiamati, fuori dai casi penali indicati dalla norma. Non si sommano automaticamente questa sanzione e quella ambientale. Il rifiuto pericoloso e il materiale semplicemente ignoto sono categorie diverse; una verifica tecnica può cambiare la qualificazione, ma non giustifica il rinvio di una notizia di reato già riconoscibile.

**Tre casi a confronto.**

1. Un privato è osservato mentre abbandona un mobile non pericoloso su un terreno, fuori dall'area dei contenitori e senza le aggravanti della traccia: si inquadra il fatto nell'art. 255, comma 1, e si attiva il canale penale. Non si applica la vecchia equivalenza privato/sanzione amministrativa.
2. Rifiuti urbani sono collocati accanto ai contenitori stradali in violazione della regola comunale; la traccia esclude ulteriori elementi di reato: opera il residuo amministrativo del comma 1.2. Se invece emergono elementi penali, la clausola di riserva impone di rivedere la qualificazione.
3. Un mozzicone è abbandonato sul marciapiede da un pedone: rilevano gli artt. 232-bis e 255, comma 1-bis. Se il fatto avviene da un veicolo, si verifica prima la fattispecie speciale del CdS.

### Rimozione e proprietario dell'area: art. 192

Il divieto di abbandono è accompagnato dall'obbligo di rimuovere i rifiuti, avviarli a recupero o smaltimento e ripristinare i luoghi. Il proprietario o titolare di diritti sull'area risponde in solido con l'autore **soltanto se la violazione gli è imputabile per dolo o colpa**, accertati in contraddittorio. Essere proprietario non basta da solo.

Il sindaco ordina le operazioni e stabilisce il termine; se gli obbligati non provvedono, l'amministrazione procede in danno e recupera i costi. Questo percorso ripristinatorio è distinto dalla sanzione amministrativa o penale e non richiede di trasformare ordinariamente l'art. 192 in un'ordinanza contingibile e urgente.

**Caso.** Rifiuti vengono scaricati da ignoti su un terreno di Tizio. La proprietà è accertata, ma non emergono ancora dolo o colpa di Tizio: non si motiva l'obbligo solidale con la sola visura catastale. Si istruiscono condotta, disponibilità dell'area e circostanze pertinenti, assicurando contraddittorio. Il bisogno di rimuovere il cumulo resta da gestire con i poteri e le competenze previsti.
''')
t=t.replace('Un’area può dover essere rimossa o messa in sicurezza', 'I rifiuti possono dover essere rimossi e l’area messa in sicurezza')
t=t.replace('Redige un verbale soltanto se la violazione e il responsabile risultano accertati; altrimenti forma una relazione. Se emergono elementi penalmente rilevanti, apre il distinto canale di PG.', 'Per una fattispecie amministrativa forma il verbale quando ne sono accertati i presupposti. Se i fatti integrano una notizia di reato, attiva la PG anche quando l’autore non è ancora identificato: una relazione interna non sostituisce la comunicazione al PM. L’incertezza sulla pericolosità dei residui richiede la verifica tecnica, ma non cancella il possibile abbandono penale già documentato.')
save(p,t,'sources/vol-02-pl-edilizia-ambiente-verifica-2026-10-03')
sp=art/'VOL-02-changes.json';s=json.loads(sp.read_text(encoding='utf-8'))
for fid,n,c,e in [('V02-47','10','Categorie commerciali, requisiti morali/professionali, SCIA unica/condizionata e autorizzazione anche tacita.','D59 artt64/65/71 e L24119bis/20 correnti; TabellaA pagine pertinenti e schede DFP; caso preposto e concentrazione.'),('V02-48','11','Titoli/silenzio, sospensione45, comunicazioni27, demolizione90/proroga240, acquisizione, sanatorie e ramo44.','DPR38027/31/44; fonteVOL10 per20/34bis/36bis; casi termini e costruzione senza permesso; rinvio nominativo.'),('V02-49','12','Mappa255/255bis/255ter, residui amministrativi, art192 responsabilità soggettiva proprietario e ordine ripristinatorio.','Articoli correnti letti; casi mobile, cassonetto, mozzicone e proprietario; CNR anche contro ignoti; refuso area rimossa corretto.')]:s['changes'][fid]={'files':[next(base.glob(n+'-*.md')).as_posix()],'change':c,'evidence':e,'status':'Applicato; riesame trasversale e gate 15 ancora aperti'}
sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('FL04/10–12 applicati')
