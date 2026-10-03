from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02');archive=art/'before-fl04';archive.mkdir(exist_ok=True)
source='sources/vol-02-pl-qualifiche-sanzioni-verifica-2026-10-03'
def get(n):
 p=next(base.glob(n+'-*.md'));a=archive/p.name
 if a.exists():raise RuntimeError('Gia modificato '+n)
 t=p.read_text(encoding='utf-8');a.write_text(t,encoding='utf-8');return p,t
def insert(t,anchor,body):
 assert t.count(anchor)==1,anchor
 return t.replace(anchor,body.strip()+'\n\n'+anchor)
def save(p,t):
 for key,val in [('source_refs',source),('topics','topics/vol-02-polizia-locale-correzioni-2026'),('last_compiled_from','wiki/'+source+'.md')]:
  t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m.group(1)+', "'+val+'"]',t,count=1,flags=re.M)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
 t=re.sub(r'^volume_chapter:.*$','volume_chapter: '+str(34+int(p.name[:2])),t,count=1,flags=re.M)
 p.write_text(t,encoding='utf-8')
p,t=get('03')
t=t.replace('La collaborazione richiede una richiesta motivata delle autorità competenti per specifiche operazioni e si svolge secondo la direzione del sindaco.', 'La collaborazione richiede una richiesta motivata delle autorità competenti per specifiche operazioni e la previa disposizione del sindaco.')
t=insert(t,'## N-FL04-03-03', '''### Le tre ipotesi di attività esterna

L'art. 4 L. 65/1986 distingue:

- missioni fuori territorio per collegamento e rappresentanza, da autorizzare;
- operazioni esterne di iniziativa del singolo **durante il servizio**, consentite esclusivamente per necessità dovuta alla flagranza di un illecito commesso nel territorio di appartenenza;
- soccorso per calamità o disastri e rinforzo di altri servizi in occasioni stagionali o eccezionali, con appositi piani o accordi fra amministrazioni e previa comunicazione al prefetto.

La flagranza di un fatto osservato per la prima volta in un altro Comune non coincide con la seconda ipotesi. Un rinforzo estivo programmato in un Comune vicino segue invece la terza: l'ordine di servizio da solo non sostituisce il piano o l'accordo richiesto. Il regolamento disciplina il servizio entro questi presupposti, senza creare un potere generale di intervento nazionale.
''')
t=t.replace('La formula legislativa va letta interamente. Ripetere “la Polizia locale è PG” non esaurisce la risposta:', 'L’art. 57, comma 2, lettera b), c.p.p. comprende le guardie provinciali e comunali **quando sono in servizio**, nell’ambito territoriale dell’ente; il comma 3 conserva i limiti del servizio e delle attribuzioni delle qualifiche speciali. Non si estende quindi automaticamente la qualità operativa a ogni fatto fuori servizio o fuori territorio. Ripetere “la Polizia locale è PG” non esaurisce la risposta:')
t=insert(t,'### Procedimento, requisiti e conseguenze', '''I requisiti dell'art. 5, comma 2, sono: godimento dei diritti civili e politici; assenza della condanna a pena detentiva per delitto non colposo e della sottoposizione a misura di prevenzione indicate dalla disposizione; non essere stati espulsi dalle Forze armate o dai Corpi militarmente organizzati né destituiti dai pubblici uffici. Se viene meno un requisito, il prefetto, sentito il sindaco, dichiara la perdita della qualità.

Nell'esercizio delle funzioni di PG e di agente di PS, il personale messo a disposizione dal sindaco dipende **operativamente** dalla competente autorità giudiziaria o di pubblica sicurezza, nel rispetto delle intese previste dall'art. 5, comma 4. Per gli atti di PG e le comunicazioni al pubblico ministero si applica il capitolo «Polizia giudiziaria e atti essenziali»: il sindaco non decide se trasmettere una notizia di reato.
''')
save(p,t)
p,t=get('05')
t=t.replace('La contestazione differita non è un verbale “meno valido”. Richiede invece particolare precisione: l’atto deve indicare la ragione prevista dalla legge che ha impedito la contestazione immediata, senza usare formule stereotipate o una motivazione inventata.', 'La contestazione differita non rende di per sé invalido il verbale. L’art. 201, comma 1-bis, individua casi nei quali la contestazione immediata non è necessaria, come l’accertamento in assenza del trasgressore e del proprietario o le specifiche rilevazioni previste dalla norma. Fuori da tali casi, il comma 1-ter richiede di indicare nel verbale i motivi che l’hanno resa impossibile. La fattispecie tipizzata e la motivazione dell’impedimento concreto vanno distinte.')
t=insert(t,'## N-FL04-05-04', '''### Termini di notifica: a chi e da quando

| Fattispecie dell'art. 201 | Termine | Evento iniziale |
|---|---|---|
| Regime ordinario senza contestazione immediata | 90 giorni | Accertamento della violazione. |
| Contestazione immediata al trasgressore e notifica a un obbligato ex art. 196 | 100 giorni | Accertamento della violazione. |
| Destinatario residente all'estero | 360 giorni | Accertamento, nel regime previsto dall'articolo. |
| Identificazione successiva del trasgressore o di altro obbligato | 90 giorni | Momento individuato dalla norma in cui i dati risultano dai registri o la PA è posta in grado di identificare il soggetto. |

La contestazione al conducente non elimina automaticamente la notifica al proprietario o ad altro obbligato solidale. La solidarietà dell'art. 196 riguarda l'obbligo di pagamento e non rende il proprietario autore materiale della guida. Occorre individuare il soggetto previsto dalla norma, comprese le sue specialità, e trattarne separatamente la posizione.

**Caso.** Violazione accertata e contestata al conducente in servizio il giorno zero; il veicolo appartiene a una società non presente. L'ufficio non chiude il fascicolo dopo aver consegnato la copia al conducente: cura la notifica al soggetto solidale nel termine di cento giorni. Se invece il veicolo era in sosta e nessun soggetto era presente, il caso ordinario richiama novanta giorni. Una notifica tardiva estingue l'obbligo verso il destinatario interessato, non automaticamente verso ogni altro soggetto.

Nel calcolo si registrano separatamente accertamento, eventuale identificazione successiva, consegna dell'atto al notificatore e perfezionamento per il destinatario. Gli esempi con giorno zero/giorno uno illustrano la decorrenza; su date reali si applicano anche le regole sui giorni festivi e sul canale di notifica, senza sostituire ricezione e spedizione.
''')
old='Il Codice della strada disciplina il pagamento nei casi consentiti e prevede rimedi diversi contro il verbale. Per la prova orale non serve recitare ogni termine; occorre mostrare di conoscere la logica delle alternative. Se si sceglie il pagamento ammesso dalla legge, si segue una strada diversa da quella dell’impugnazione. Se si propone ricorso, bisogna individuare il destinatario, il termine vigente e gli effetti propri del rimedio.'
assert old in t
t=t.replace(old,'''Il Codice della strada prevede pagamento e rimedi alternativi, con termini differenti da conoscere insieme ai loro presupposti. Il pagamento in misura ridotta, quando ammesso, è pari al **minimo edittale entro sessanta giorni** dalla contestazione o notificazione. L'art. 202 riduce quel minimo del **30% se si paga entro cinque giorni**; le spese restano dovute. Non si usa la formula «un terzo del massimo o doppio del minimo» propria della L. 689.

Lo sconto del 30% è escluso nelle ipotesi di confisca e sospensione della patente indicate dall'art. 202; vanno inoltre verificate le esclusioni del pagamento ridotto stesso nei commi 3 e 3-bis. Sono due domande diverse: «posso pagare in misura ridotta?» e «posso applicare anche lo sconto?». Le discipline speciali, compresa la sospensione breve, vanno coordinate con la norma specifica.

| Scelta contro il verbale | Termine | Condizione essenziale |
|---|---|---|
| Pagamento del minimo | 60 giorni da contestazione/notifica | Pagamento ridotto ammesso. |
| Pagamento con riduzione del 30% | 5 giorni da contestazione/notifica | Nessuna esclusione dello sconto. |
| Ricorso al prefetto del luogo | 60 giorni da contestazione/notifica | Nessun pagamento nei casi ammessi; art. 203. |
| Opposizione al giudice di pace del luogo | 30 giorni; 60 se residente all'estero | Alternativa al ricorso prefettizio; art. 204-bis e art. 7 D.Lgs. 150/2011. |

**Esempio numerico.** Minimo ipotetico 100 euro e nessuna esclusione: 70 euro entro cinque giorni, 100 entro sessanta, più spese. Non sono importi attribuiti a una violazione reale. Una richiesta informale di riesame non equivale al ricorso e non sospende automaticamente i termini. Se non si paga e non si ricorre tempestivamente, l'art. 203, comma 3, attribuisce al verbale efficacia esecutiva per metà del massimo edittale e spese: non memorizzare un generico «raddoppio della multa».''')
t=t.replace('se la contestazione non è avvenuta','se la contestazione non è avvenuta o se occorre notificare a un obbligato solidale non raggiunto dalla contestazione')
t=insert(t,'## ▣ Verifica', '''### Caso di scelta del rimedio

Il destinatario residente in Italia riceve il verbale e intende contestarlo. Al quarantesimo giorno non ha pagato né proposto ricorso. Nel regime ordinario il termine di trenta giorni per l'opposizione diretta al giudice di pace è decorso, mentre resta il termine di sessanta giorni per il ricorso al prefetto. Non si conclude che tutti i rimedi siano ancora disponibili perché il pagamento può avvenire entro sessanta giorni. Restano distinti i presupposti di eventuali vicende eccezionali, non forniti da questa traccia.
''')
save(p,t)
p,t=get('06')
t=insert(t,'## N-FL04-06-02', '''### Chi risponde dell'illecito

Gli artt. 2 e 3 L. 689/1981 richiedono maggiore età, capacità di intendere e volere e una condotta cosciente e volontaria, dolosa o colposa. Per l'incapace risponde chi era tenuto alla sorveglianza, salvo prova di non avere potuto impedire il fatto; restano le eccezioni per incapacità colposa o preordinata. L'errore sul fatto esclude responsabilità soltanto se non determinato da colpa. Il controllo non si esaurisce quindi nell'identificazione di chi era materialmente presente.

La solidarietà dell'art. 6 riguarda, nei casi previsti, proprietario o altri titolari della cosa, soggetto investito di autorità o vigilanza, ente o imprenditore per il fatto di rappresentanti e dipendenti nell'esercizio delle funzioni. Il coobbligato non diventa per questo autore materiale; chi paga può esercitare il regresso contro l'autore. Le prove liberatorie previste dalla norma vanno valutate, non escluse in anticipo.

**Caso.** Una violazione amministrativa è commessa da un diciassettenne. Non si emette automaticamente a suo carico la sanzione personale: si verifica l'art. 2 e la posizione di chi doveva sorvegliarlo. In un altro caso, il dipendente maggiorenne agisce nelle proprie incombenze per un'impresa: autore e impresa possono assumere posizioni diverse di responsabilità personale e obbligazione solidale.
''')
t=insert(t,'## N-FL04-06-03', '''### Contestazione e prescrizione

L'art. 14 richiede la contestazione immediata quando possibile al trasgressore e all'obbligato solidale. Se non avviene, gli estremi sono notificati entro **novanta giorni dall'accertamento** ai residenti in Italia e **trecentosessanta giorni** ai residenti all'estero. Non si identifica automaticamente l'accertamento con il primo sopralluogo: occorre ricostruire quando siano stati acquisiti gli elementi necessari. Se gli atti provengono dall'autorità giudiziaria, rileva la ricezione secondo la norma.

L'omessa tempestiva notifica estingue l'obbligazione verso il soggetto interessato. Diversa è la prescrizione dell'art. 28: il diritto a riscuotere si prescrive in **cinque anni dal fatto**, con interruzione secondo il codice civile. «Novanta giorni» e «cinque anni» non sono due termini alternativi per notificare il verbale.
''')
t=t.replace('Il manuale non fissa importi variabili: insegna a trovare la regola corretta.', '''Nel regime generale dell'art. 16, entro **sessanta giorni** da contestazione o notifica si paga la somma più favorevole fra un terzo del massimo edittale e il doppio del minimo, se un minimo è previsto, oltre le spese. Per violazioni di regolamenti e ordinanze comunali e provinciali la Giunta può determinare un diverso importo nei limiti edittali secondo il comma 2; le discipline speciali possono escludere o modificare il meccanismo.

**Calcolo.** Minimo 400, massimo 3.000: doppio minimo 800, terzo massimo 1.000; si pagano 800 euro più spese. Con minimo 600 e massimo 3.000, il confronto è 1.200 contro 1.000: si pagano 1.000 più spese. Non scegliere sempre il doppio del minimo e non importare lo sconto stradale del 30%.

L'art. 18 consente di presentare **entro trenta giorni** da contestazione o notifica scritti difensivi e documenti e di chiedere audizione. Il deposito delle difese non sospende automaticamente il termine del pagamento ridotto. L'autorità valuta le difese e sente chi ne ha fatto richiesta prima di decidere.''')
old='L’opposizione appartiene alla fase successiva e segue la disciplina applicabile. Nel concorso è sufficiente mostrare la catena logica: **verbale non pagato o difese presentate -> valutazione dell’autorità -> archiviazione oppure ordinanza -> rimedio nei termini di legge**. Termini, importi, giudice competente e forme dell’opposizione vanno verificati sul testo vigente e sulla fonte speciale.'
assert old in t
t=t.replace(old,'''L'ingiunzione si paga entro trenta giorni dalla notificazione, sessanta per residenti all'estero, ai sensi dell'art. 18. L'opposizione segue invece l'art. 6 D.Lgs. 150/2011: ricorso entro trenta giorni dalla notificazione del provvedimento, sessanta se il ricorrente risiede all'estero, al giudice del luogo della violazione. La coincidenza numerica non rende pagamento e opposizione la stessa facoltà.

È competente ordinariamente il giudice di pace; decide il tribunale nelle materie e nelle ipotesi del medesimo art. 6, fra cui ambiente, lavoro e igiene degli alimenti, e secondo i criteri di valore e natura della sanzione. Non scrivere «sempre giudice di pace». Il giudizio segue il rito del lavoro con le specialità previste e il ricorso non sospende da solo l'efficacia dell'ordinanza: occorre il provvedimento del giudice nei presupposti di legge.''')
t=t.replace('Per l’esame è preferibile spiegare la funzione dell’opposizione e segnalare che dettagli variabili devono essere verificati, anziché recitare termini o competenze senza aver controllato la disciplina attuale.', 'Per l’esame si indicano insieme funzione dell’opposizione, termine di trenta o sessanta giorni e criterio di competenza, applicandoli alla materia e alla sanzione della traccia.')
t=insert(t,'## ▣ Verifica', '''### Ordinanza-ingiunzione: esempio didattico completo

**Presupposti della traccia, interamente fittizi.** Il Comune Alfa ha un regolamento che vieta l'uso di un impianto comunale fuori dagli orari esposti; l'esercizio attribuisce la competenza sanzionatoria al responsabile del servizio. La violazione è punita da 400 a 3.000 euro. Il verbale n. 12 è stato notificato regolarmente; nessun pagamento è intervenuto. L'interessato ha chiesto audizione e prodotto una prenotazione che copre un diverso orario. L'audizione si è svolta e la violazione è provata. Il riferimento regolamentare è simulato, non una disposizione vigente di un Comune reale.

**Comune Alfa — Servizio competente. Ordinanza-ingiunzione n. 4, esercizio didattico.**

**Oggetto:** violazione del regolamento dell'impianto comunale, verbale n. 12.

Il responsabile, richiamata la competenza attribuita nella traccia e la L. 689/1981, esamina il verbale, le fotografie, la prova della notifica, la memoria e il verbale di audizione. L'accesso fuori orario risulta dagli accertamenti descritti nel verbale; la prenotazione prodotta riguarda una fascia diversa e non giustifica la condotta contestata. Le difese non modificano pertanto l'accertamento. L'assenza di precedenti e la limitata gravità descritte nell'esercizio motivano la sanzione al minimo di 400 euro, oltre le spese effettivamente documentate.

**Dispone:** ingiunge al trasgressore il pagamento di 400 euro e delle spese indicate nel prospetto allegato; ne cura la notifica; indica pagamento entro trenta giorni dalla notifica, sessanta per residente all'estero, con il canale istituzionale riportato nell'avviso. L'opposizione può essere proposta al giudice competente del luogo della violazione entro trenta giorni, sessanta per residente all'estero, ai sensi dell'art. 6 D.Lgs. 150/2011. Nel caso simulato ordinario, senza presupposti di competenza del tribunale, è competente il giudice di pace. Il ricorso non sospende automaticamente l'esecuzione.

**Allegati:** verbale, prova della notifica, memoria, audizione, riscontri e prospetto delle spese. **Sottoscrizione:** responsabile competente.

**Perché l'importo è 400 e non 800?** Gli 800 euro erano il pagamento ridotto dell'art. 16, non effettuato. L'ordinanza determina la sanzione nei limiti edittali motivandola: non copia automaticamente l'importo ridotto. Nell'esercizio i fatti giustificano il minimo; in un caso diverso la motivazione e l'importo potrebbero cambiare.
''')
save(p,t)
statepath=art/'VOL-02-changes.json';s=json.loads(statepath.read_text(encoding='utf-8'))
for fid,nums,change,evidence in [('V02-39',['03'],'Condizione di servizio e territorio ex art. 57; requisiti PS, perdita della qualità, dipendenza operativa e missioni esterne tipizzate.','L.65 artt.3–5/9 e CPP57 letti; caso rinforzo/flagranza; rinvio nominativo al capitolo PG.'),('V02-41',['05'],'Termini 90/100/360, pagamento 60 e sconto entro5, rimedi prefetto60/GdP30–60, titolo esecutivo e casi.','Artt.201–204bis e D1507 vigenti; calcolo100→70; caso ricorso al giorno40.'),('V02-42',['05'],'Notifica solidale anche dopo contestazione al conducente; distinti casi tipizzati e impedimento motivato.','Art.201 commi1/1bis/1ter; esempio società proprietaria non presente.'),('V02-43',['06'],'Responsabilità personale/solidale, termini, formula, prescrizione, opposizione e ordinanza didattica con motivazione e rimedi.','L6892/3/6/28 e nota14/16/18; D1506; calcoli800/1000 e distinzione ordinanza400.')]:
 s['changes'][fid]={'files':[next(base.glob(n+'-*.md')).as_posix() for n in nums],'change':change,'evidence':evidence,'status':'Applicato; riesame modulo e gate 15 ancora aperti'}
statepath.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('FL04: capitoli03,05,06 integrati; quattro rilievi registrati')
