from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02');source='sources/vol-02-pl-pubblica-sicurezza-verifica-2026-10-03'
def get(n):
 p=next(base.glob(n+'-*.md'));a=art/'before-fl04'/p.name
 if a.exists():raise RuntimeError('Già modificato '+n)
 t=p.read_text(encoding='utf-8');a.write_text(t,encoding='utf-8');return p,t
def add(t,a,b):
 assert t.count(a)==1,a
 return t.replace(a,b.strip()+'\n\n'+a)
def save(p,t):
 for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
 t=re.sub(r'^volume_chapter:.*$','volume_chapter: '+str(34+int(p.name[:2])),t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf-8')
p,t=get('08')
t=add(t,'## N-FL04-08-02', '''### Quattro articoli per leggere un titolo di polizia

| Norma TULPS | Regola | Applicazione |
|---|---|---|
| Art. 8 | Titolo personale; trasferimento e rappresentanza non sono liberi, salvo casi e condizioni di legge | Il subentro di un altro gestore non si risolve prestando la licenza |
| Art. 9 | L'autorità può imporre prescrizioni di pubblico interesse oltre alle condizioni stabilite dalla legge | Il controllo verifica anche le prescrizioni legittimamente inserite nel titolo |
| Art. 10 | Abuso del titolo può determinarne sospensione o revoca | La pattuglia documenta l'abuso; l'autorità titolare valuta il provvedimento |
| Art. 11 | Requisiti soggettivi, diniego obbligatorio o discrezionale e revoca | Distinguere ostacolo tassativo da valutazione motivata; verificare anche requisiti speciali |

L'art. 11 impone, fra l'altro, il diniego per condanna a pena restrittiva della libertà personale superiore a tre anni per delitto non colposo, in assenza di riabilitazione, e nelle ulteriori situazioni tassative indicate. Per alcune altre condanne, tra cui quelle per delitti violenti contro la persona o per furto, rapina ed estorsione, la norma configura un potere di diniego: l'esistenza del potere non elimina la motivazione. Quando vengono meno le condizioni cui il titolo è subordinato, opera la disciplina della revoca. Non si ricostruisce il sistema con una generica richiesta al cittadino di dimostrare la propria «buona condotta».

**Esempio.** Un esercente autorizzato opera in violazione di una prescrizione del titolo. Prima si identifica la prescrizione e si prova il fatto; poi si comunica all'autorità competente per la valutazione degli effetti sul titolo. La sospensione non nasce dalla sola annotazione della pattuglia e non coincide con l'eventuale sanzione pecuniaria.
''')
t=add(t,'## N-FL04-08-04', '''### Chi è autorità locale di pubblica sicurezza

L'art. 15 della L. 121/1981 precisa il riparto: nel capoluogo di provincia è il questore; negli altri comuni è il funzionario preposto al commissariato competente. **Dove non esiste un commissariato, le attribuzioni sono esercitate dal sindaco quale ufficiale del Governo.** Per eccezionali esigenze può essere inviato temporaneamente un funzionario della Polizia di Stato con le modalità previste dalla norma: in quel periodo è sospesa la competenza dell'autorità locale.

Questa attribuzione specifica non trasforma ogni atto del Comune in atto di PS. Il sindaco che esercita quel ruolo va distinto dal sindaco organo dell'amministrazione comunale, dagli uffici gestionali e dal comandante della Polizia locale.
''')
t=add(t,'## N-FL04-08-05', '''### Spettacoli: tre controlli distinti

Per uno spettacolo aperto al pubblico si distinguono **regime dell'attività, sicurezza del luogo e ulteriori adempimenti**. Gli artt. 68 e 69 TULPS riguardano spettacoli e trattenimenti; l'art. 80 riguarda solidità, sicurezza e uscite del luogo. Le funzioni amministrative indicate sono state trasferite ai Comuni dall'art. 19 DPR 616/1977: il richiamo storico al questore nel testo del TULPS non basta a individuare oggi l'ufficio competente.

| Regime | Condizioni essenziali | Conseguenza |
|---|---|---|
| Artt. 68–69 TULPS, semplificazione ordinaria | Fino a 200 partecipanti, conclusione entro le ore 24 del giorno d'inizio | SCIA al SUAP o ufficio analogo, con gli adempimenti di sicurezza pertinenti |
| Art. 7 DL 201/2024, regime speciale | Spettacoli dal vivo delle categorie indicate, come teatro, musica, danza e musical, e proiezioni cinematografiche; massimo 2.000 partecipanti; dalle 8 alle 1 del giorno successivo | SCIA speciale nei presupposti della legge, con dichiarazioni, relazione tecnica e documentazione sicurezza/rischio |
| Fuori dai presupposti di semplificazione | Attività, capienza, orario, luogo o competenza non compatibili | Individuare il procedimento autorizzatorio e tecnico pertinente; non estendere la SCIA per analogia |

Il regime speciale esclude i casi degli artt. 142–143 del regolamento TULPS e i luoghi soggetti a vincoli ambientali, paesaggistici o culturali. Comprende rassegne e festival su più giorni alle medesime condizioni artistiche e organizzative. La L. 182/2025, art. 34, ha precisato il corredo: numero massimo, luogo, orario, dichiarazioni, relazione del professionista abilitato e documentazione delle misure di sicurezza e contenimento del rischio. L'attività può iniziare dalla presentazione, ma la presentazione non rende lecita un'attività priva dei requisiti. Il controllo ordinario è entro sessanta giorni, con la disciplina speciale delle dichiarazioni false.

**Caso.** Un concerto per 1.500 persone dalle 20 alle 00.30 non rientra nella semplificazione ordinaria «200 persone entro le 24». Può rientrare nel regime speciale soltanto se ricorrono tutte le altre condizioni, compresi luogo e documentazione tecnica. La sola capienza inferiore a 2.000 non basta. Se il luogo è vincolato, non si applica automaticamente quel regime.

Un altro potere ancora è quello dell'**art. 100 TULPS**: il questore può sospendere la licenza di un esercizio, anche di vicinato, per tumulti, gravi disordini o gli altri presupposti di pericolo contemplati. La ripetizione dei fatti può condurre a revoca. Non è la semplice sanzione per un'irregolarità commerciale e non spetta alla pattuglia sostituirsi alla valutazione questorile.
''')
t=add(t,'### Caso guidato: controllo in un esercizio aperto al pubblico', '''### Soggiorno: termini, documenti e tutela

Per il cittadino di un Paese terzo, l'art. 5 D.Lgs. 286/1998 disciplina il permesso nei casi in cui esso è richiesto: la domanda è rivolta al questore della provincia entro **otto giorni lavorativi dall'ingresso**. Le regole dei soggiorni brevi e dei diversi titoli vanno tenute distinte; questa disciplina non si trasferisce indistintamente ai cittadini UE.

Nel testo applicabile dal 22 maggio 2026, modificato dal D.Lgs. 83/2026, il rinnovo è richiesto almeno **novanta giorni prima della scadenza**, fatti salvi termini speciali. Il termine previsto per rilascio, rinnovo o conversione è di **novanta giorni**. Il comma 9-bis tutela, alle condizioni prescritte, soggiorno e lavoro durante l'attesa, con ricevuta della richiesta e altri requisiti, fino alla comunicazione ostativa dell'autorità. Il documento materialmente scaduto non dimostra da solo soggiorno irregolare: occorre verificare la domanda pendente e la posizione concreta.

L'art. 6 distingue l'esibizione dei documenti di soggiorno nei procedimenti amministrativi dall'ordine di esibizione rivolto da ufficiali e agenti di PS nei presupposti di legge. Per i procedimenti pubblici vi sono eccezioni, fra cui prestazioni sanitarie dell'art. 35 e prestazioni scolastiche obbligatorie. Nel controllo di polizia rilevano identità, titolo o documento equivalente, ragione della mancata esibizione e qualifica dell'operatore. La mancata esibizione non va qualificata automaticamente come reato senza questi accertamenti.

L'art. 19 impone inoltre garanzie sostanziali: divieto di respingimento o espulsione verso persecuzioni, tortura o trattamenti inumani, protezioni specifiche per minori e altre categorie, attenzione alle vulnerabilità nell'esecuzione. La pattuglia documenta e attiva il raccordo con l'autorità competente; non dispone un'espulsione come conseguenza ordinaria della verifica dei documenti.

**Caso risolto.** Durante un controllo emerge un permesso scaduto, accompagnato dalla ricevuta di rinnovo. L'operatore verifica identità, autenticità ed estremi della richiesta tramite i canali competenti. Non equipara la data impressa sul documento a una decisione di irregolarità, ma considera il regime dell'attesa e gli eventuali provvedimenti dell'autorità. L'attività che ha dato origine al controllo mantiene il proprio procedimento.
''')
ds=['applicare il regime seguito dallo stesso locale negli anni precedenti, anche se l’attività è cambiata.','Sì, quando il regolamento comunale richiama una legge statale.','è conferita dal comandante dopo il periodo di prova.','L’ufficio che protocolla la pratica, anche quando la decisione è attribuita ad altra autorità.','Sì, se il documento reca una data scaduta, anche quando è prodotta ricevuta di rinnovo.','trasmettere tutti i profili soltanto al SUAP, che decide anche quelli penali.']
parts=t.split('### Quiz ')
for i in range(1,7):parts[i]=parts[i].replace('\n\n**Risposta corretta:','\nD. '+ds[i-1]+'\n\n**Risposta corretta:',1)
t='### Quiz '.join(parts)
t=t.replace('- R.D. 18 giugno 1931, n. 773, Testo unico delle leggi di pubblica sicurezza.', '- R.D. 18 giugno 1931, n. 773, artt. 8–11, 68–69, 80 e 100; L. 121/1981, art. 15; DPR 616/1977, art. 19.\n- DL 201/2024, art. 7, convertito dalla L. 16/2025, e L. 182/2025, art. 34, sugli spettacoli.');t=t.replace('- D.Lgs. 25 luglio 1998, n. 286, Testo unico sull’immigrazione.', '- D.Lgs. 25 luglio 1998, n. 286, artt. 5, 6 e 19; D.Lgs. 16 aprile 2026, n. 83, applicabile dal 22 maggio 2026.')
save(p,t)
p,t=get('09')
t=t.replace('L’ordinanza non è una scorciatoia per disciplinare stabilmente un fenomeno sociale. Se manca un pericolo concreto o l’urgenza richiesta dalla norma, occorre usare gli strumenti ordinari o costruire la risposta regolamentare competente.', 'L’ordinanza contingibile e urgente non è una scorciatoia per disciplinare stabilmente un fenomeno sociale. Se mancano i suoi presupposti, si usano gli strumenti ordinari, comprese le ordinanze ordinarie che una specifica norma consente senza richiedere contingibilità e urgenza. Il nome «ordinanza» non implica sempre un potere emergenziale.')
a=t.index('Il D.L. n. 48/2025, convertito dalla L. n. 80/2025, contiene');z=t.index('### Caso guidato:',a)
t=t[:a]+'''### Allontanamento e divieto di accesso: non sono lo stesso atto

Gli artt. 9 e 10 DL 14/2017, nel testo aggiornato anche nel 2025 e nel 2026, prevedono misure tipizzate. La parola «degrado» da sola non ne dimostra i presupposti.

| Misura | Presupposti e autorità | Durata e seguito |
|---|---|---|
| Ordine di allontanamento | Organo accertatore: condotta dell'art. 9, luogo compreso nell'ambito e presupposti dimostrati | Scritto e motivato; efficacia di 48 ore dall'accertamento del fatto; copia immediata al questore |
| Divieto di accesso del questore, art. 10, comma 2 | Reiterazione delle condotte indicate e pericolo per la sicurezza; anche specifica ipotesi su denunce/condanne per reati nei luoghi indicati | Fino a 12 mesi; luoghi espressamente individuati e modalità compatibili con mobilità, salute e lavoro |
| Divieto qualificato, comma 3 | Condotte e condanna definitiva o confermata in appello, negli ultimi cinque anni, per reati contro persona o patrimonio, nei presupposti della norma | Da 12 mesi a 2 anni; regole particolari per zone prefettizie |
| Zone urbane del prefetto, art. 9, commi 3-bis/ter | Zone caratterizzate da gravi o ripetuti episodi di criminalità o illegalità, individuate con provvedimento motivato e consultazione prevista | Zona per massimo 6 mesi, rinnovi nel limite massimo di 18; il divieto personale segue le condizioni e i limiti specifici dell'art. 10 |

L'art. 9, comma 1, riguarda condotte che impediscono accesso e fruizione delle infrastrutture di trasporto e pertinenze, violando i divieti di stazionamento o occupazione: sanzione amministrativa da 100 a 300 euro e allontanamento. Il comma 2 comprende le violazioni espressamente richiamate e, nel testo vigente, comportamenti violenti, minacciosi o insistentemente molesti da cui derivi concreto pericolo per la sicurezza. I regolamenti comunali possono individuare le ulteriori aree del comma 3, come quelle presso scuole, presidi sanitari, luoghi culturali, mercati, spettacoli o verde pubblico. Non ogni piazza è automaticamente ricompresa.

Per le **zone prefettizie**, le denunce negli ultimi cinque anni per i reati indicati dal comma 3-bis non bastano: occorre anche una condotta attuale violenta, minacciosa o insistentemente molesta che impedisca la libera fruizione e determini concreto pericolo. La zona è individuata sentito il comitato provinciale per l'ordine e la sicurezza pubblica, alla cui riunione è invitato il procuratore o un delegato. La durata della zona non coincide con le quarantotto ore dell'allontanamento personale.

L'ordine riporta fatti, luogo, motivi, durata ed effetti della violazione. Va trasmesso immediatamente al questore e, quando ricorrono le condizioni, segnalato ai servizi sociosanitari. La sua violazione ha la specifica conseguenza amministrativa prevista dall'art. 10; la violazione del divieto questorile ha invece le conseguenze penali tipizzate. Non si chiamano entrambe «multa per DASPO».

L'art. 10 contiene anche un'ipotesi specifica per i reati indicati commessi in occasione di manifestazioni o relativi ad armi, con condizioni, luoghi e durata propri. Per minori dai quattordici anni sono previste notifica agli esercenti la responsabilità genitoriale e comunicazione alla procura minorile. Le modalità devono rispettare le esigenze personali previste dalla norma; non si può costruire un divieto più ampio senza motivazione.

### Tutela e controllo della motivazione

La misura amministrativa deve essere motivata e indicare i rimedi. Il provvedimento lesivo può essere contestato davanti al giudice amministrativo con azione di annullamento entro sessanta giorni, ai sensi dell'art. 29 del codice del processo amministrativo. La sanzione pecuniaria segue invece il proprio procedimento: non le si trasferisce automaticamente il ricorso prefettizio del Codice della strada. Il vecchio comma 5 dell'art. 10 è stato abrogato nel 2025; non si insegna una convalida giudiziaria automatica per ogni divieto.

**Caso risolto.** Alle ore 18 un soggetto occupa l'accesso della stazione in violazione del divieto, impedendo concretamente il passaggio. L'organo competente descrive condotta e luogo, contesta la violazione e adotta l'ordine scritto motivato, che cessa alle ore 18 di due giorni dopo. Trasmette subito copia al questore. Non può trasformare da sé l'ordine in un divieto di dodici mesi: quest'ultimo richiede autorità e presupposti propri. Se il soggetto è soltanto seduto e non ricorre alcuna fattispecie prevista, il mero disagio percepito non giustifica quel medesimo ordine.

''' + t[z:]
ds=['No, salvo che una pattuglia operi fuori dal proprio territorio, quando acquisisce competenza generale.','Il singolo ordine di allontanamento della pattuglia.','soltanto l’esistenza di un precedente intervento nella zona.','requisiti richiesti da ogni ordinanza, comprese tutte quelle ordinarie.','può prolungare l’allontanamento di48ore fino a12mesi per ragioni di servizio.']
parts=t.split('### Quiz ')
for i in range(1,6):parts[i]=parts[i].replace('\n\n**Risposta corretta:','\nD. '+ds[i-1].replace('di48ore','di 48 ore').replace('a12mesi','a 12 mesi')+'\n\n**Risposta corretta:',1)
t='### Quiz '.join(parts);a=t.index('### Quiz 6');z=t.index('### Caso ragionato finale',a)
t=t[:a]+'''### Quiz 6

L'allontanamento previsto dagli artt. 9–10 DL 14/2017 coincide con il divieto di accesso del questore?

A. Sì, cambia soltanto il nome utilizzato nel verbale.
B. Sì, entrambi durano sempre dodici mesi.
C. No: l'ordine dell'accertatore dura 48 ore dal fatto; il divieto questorile richiede presupposti e provvedimento propri.
D. No: l'allontanamento è emesso sempre dal prefetto e dura sei mesi.

**Risposta corretta: C.** Sono distinti autorità, presupposti e durata. I sei mesi riguardano l'individuazione della zona prefettizia nella diversa ipotesi dell'art. 9, comma 3-ter.

''' + t[z:]
t=t.replace('- Aggiornamenti normativi recenti e necessità di verifica.', '- Allontanamento, divieti di accesso e zone prefettizie nella disciplina vigente.')
t=t.replace('## Riferimenti normativi e professionali essenziali','## Riferimenti normativi e professionali essenziali\n\n- DL 14/2017, artt. 9–10, nel testo vigente dopo DL 48/2025 e DL 23/2026, convertito dalla L. 54/2026; D.Lgs. 104/2010, art. 29.')
save(p,t)
sp=art/'VOL-02-changes.json';s=json.loads(sp.read_text(encoding='utf-8'))
for fid,n,c,e in [('V02-45','08','TULPS8–11/68–69/80/100, autorità locale PS, spettacoli200/2000, soggiorno aggiornato90giorni e garanzie.','Articoli letti e fonte consolidata; casi concerto1500 e ricevuta rinnovo; sei quiz A–D.'),('V02-46','09','MisureDL14 con presupposti, competenza,48ore/12–24mesi, zone2026, rimedi e distinzione ordinanze.','Artt.9/10 correnti e CPA29; caso allontanamento ore18; esclusa convalidaabrogata; quiz6 concreto.')]:s['changes'][fid]={'files':[next(base.glob(n+'-*.md')).as_posix()],'change':c,'evidence':e,'status':'Applicato; riesame trasversale e gate 15 ancora aperti'}
sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('FL04/08–09 applicati')
