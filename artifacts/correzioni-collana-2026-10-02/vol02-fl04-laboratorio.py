from pathlib import Path
import re,json,shutil
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters');art=Path('artifacts/correzioni-collana-2026-10-02');p=next(base.glob('15-*.md'));b=art/'before-fl04'/p.name
assert not b.exists();shutil.copy2(p,b);t=p.read_text(encoding='utf-8')
anchor='## N-FL04-15-03'
block='''### Elaborato svolto 1: verbale amministrativo ex L. 689/1981

**Dossier della prova.** Ente, persone, luoghi, numeri di atti e norma settoriale di questo esercizio sono interamente fittizi. La traccia fornisce una legge regionale didattica che vieta l'accesso motorizzato al prato di un parco, salvo autorizzazione o soccorso, e prevede sanzione da **100 a 600 euro**. Indica come autorità competente il dirigente del servizio Parchi del Comune, ammette il pagamento ridotto ordinario dell'art. 16 L. 689/1981 e non prevede misure accessorie. Nessuna di queste indicazioni va citata come norma reale. La procedura della L. 689, invece, è quella studiata nel capitolo «Il sistema delle sanzioni amministrative».

La pattuglia osserva direttamente l'accesso, ferma il conducente e accerta che è maggiorenne, proprietario del mezzo e privo di autorizzazione; non ricorre una situazione di soccorso. La segnalazione del divieto è visibile. Redigi il verbale senza inventare un diverso coobbligato.

**Comune didattico di Fontechiara — Corpo di polizia locale**

**Verbale di accertamento e contestazione n. 12/ES — 3 ottobre 2026.**

Alle ore 10.15 del 3 ottobre 2026, nel Parco dei Tigli, accesso sud di via Studio, gli agenti Anna Esempio e Bruno Esempio, in servizio di vigilanza, accertano quanto segue.

**Trasgressore.** Marco Esempio, nato nel Comune didattico il 10 maggio 1985, residente in via Prova n. 8, identificato mediante carta d'identità fittizia DID-001. Conducente e proprietario del veicolo descritto nella scheda V1 allegata; targa didattica V1, da non utilizzare come targa reale.

**Fatto accertato.** Alle ore 10.10 entrambi gli agenti hanno osservato il veicolo V1 attraversare l'accesso sud e percorrere circa venti metri sul prato. Il cartello di divieto, fotografato in F01, era visibile all'ingresso. Il conducente è stato fermato alle ore 10.12. Non ha esibito un'autorizzazione e ha dichiarato di non possederla; la verifica svolta tramite l'ufficio Parchi alle ore 10.18 non ha rilevato titoli relativi al veicolo o al conducente. Non sono state osservate attività di soccorso.

**Norma e qualificazione.** La condotta integra il divieto di accesso motorizzato della disposizione regionale didattica fornita dalla traccia; sanzione edittale 100–600 euro. Non si contestano violazioni del Codice della strada e non si applicano sanzioni accessorie assenti dal dossier. Il trasgressore coincide con il proprietario: non viene creato un secondo debitore distinto.

**Contestazione e dichiarazioni.** La violazione è contestata personalmente alle ore 10.25. L'interessato dichiara: «Ero entrato per scaricare una sedia; non avevo autorizzazione». La dichiarazione è riportata come tale e non modifica i fatti direttamente osservati. Una copia del presente verbale è consegnata al trasgressore alle ore 10.30, con attestazione di ricezione.

**Pagamento in misura ridotta.** Entro sessanta giorni dalla contestazione è ammesso il pagamento di **200 euro**: un terzo del massimo è 600/3 = 200; il doppio del minimo è 2 × 100 = 200. Le due quantità coincidono. Nel caso non sono sostenute spese di notificazione. Il versamento va riferito al verbale n. 12/ES tramite il canale di pagamento dell'ente indicato nell'avviso didattico allegato; l'esercizio non contiene coordinate utilizzabili per pagamenti reali. Non si applica lo sconto stradale del 30% entro cinque giorni.

**Facoltà difensive.** Entro trenta giorni dalla contestazione l'interessato può far pervenire scritti difensivi e documenti al dirigente del servizio Parchi, autorità indicata nel dossier, e chiedere di essere sentito, ai sensi dell'art. 18 L. 689/1981. L'eventuale ordinanza-ingiunzione e il relativo rimedio sono fasi successive: questo verbale non è già un'ordinanza e non indica come rimedio immediato il ricorso al prefetto previsto dal CdS.

**Allegati e chiusura.** F01–F03, fotografie degli agenti con orari e punti di ripresa; scheda V1; esito della verifica con ufficio Parchi; avviso didattico di pagamento. Verbale chiuso alle ore 10.30. Sottoscrizioni: agenti Anna Esempio e Bruno Esempio; Marco Esempio per ricezione della copia. La firma per ricezione non equivale a confessione né a rinuncia alle difese.

**Controllo della soluzione.** La cronologia distingue osservazione, fermo, verifica del titolo, contestazione e consegna. Il calcolo applica l'art. 16, non il minimo stradale. Le difese sono indirizzate all'autorità fornita dalla traccia. Se non avviene il pagamento e ne ricorrono i presupposti, gli accertatori inoltrano il rapporto all'autorità competente: la pattuglia non emette autonomamente l'ordinanza-ingiunzione. In una variante con proprietario diverso si esamina separatamente l'obbligazione solidale dell'art. 6 e la contestazione/notificazione nei suoi confronti.

'''
assert t.count(anchor)==1;t=t.replace(anchor,block+anchor)
anchor='## N-FL04-15-04'
block='''### Elaborato svolto 2: annotazione di PG e seguito

**Scenario fittizio.** Una pattuglia vede una persona scaricare un mobile su un terreno pubblico lontano dai cassonetti. Il dossier qualifica il mobile come rifiuto non pericoloso, esclude altre aggravanti e identifica l'autore come privato. Si applica quindi la mappa vigente dell'art. 255, comma 1, D.Lgs. 152/2006 spiegata nel capitolo «Ambiente, rifiuti e controlli locali»: non un comune illecito amministrativo soltanto perché l'autore è un privato.

**Comune didattico di Fontechiara — Corpo di polizia locale**

**Annotazione di PG n. 13/ES — attività d'iniziativa del 3 ottobre 2026.**

I sottoscritti agenti Anna Esempio e Bruno Esempio annotano le seguenti attività, compiute in servizio nel territorio comunale.

**Ore 14.05, terreno pubblico di via Laboratorio, fronte civico didattico 20.** Entrambi gli operatori osservano una persona estrarre un mobile da un furgone e posarlo sul terreno; terminato lo scarico, la persona risale sul mezzo. L'area non ospita contenitori stradali per la raccolta. La posizione del mobile e l'inquadramento dei luoghi sono documentati nelle fotografie F01–F04, eseguite dall'agente Bruno Esempio fra le 14.06 e le 14.08. La scheda di rilievo allegata descrive dimensioni, materiale visibile e collocazione; la qualificazione non pericolosa è dato espressamente fornito dalla traccia.

**Ore 14.09.** Il conducente viene identificato come Paolo Esempio, nato il 4 aprile 1980 nel Comune didattico, residente in via Test n. 4, mediante documento fittizio DID-002. L'identificazione è documentata nel separato verbale con gli adempimenti previsti per la qualità processuale assunta: l'annotazione non lo sostituisce. Non si raccolgono nel presente atto dichiarazioni sul fatto eludendo le garanzie difensive.

**Qualificazione provvisoria e seguito.** I fatti osservati sono rappresentati come possibile abbandono di rifiuto non pericoloso ex art. 255, comma 1. Alle ore 14.20 gli elementi essenziali, le fonti di prova e le attività compiute sono trasmessi senza ritardo al PM mediante separata comunicazione di notizia di reato; si conserva la ricevuta nel fascicolo. L'invio non è rinviato all'ultimazione delle verifiche sul ripristino dell'area. Non si indica in questa annotazione una convalida di sequestro, perché il dossier non descrive alcun sequestro.

**Allegati.** F01–F04 con autore e orari; scheda di rilievo; separato verbale di identificazione; copia della CNR e ricevuta di trasmissione. Per il distinto seguito ripristinatorio dell'art. 192, i fatti pertinenti sono trasmessi all'ufficio comunale competente, nei limiti consentiti dal procedimento penale e dalla tutela dei dati. Chiusura alle ore 14.35. Sottoscrizioni degli agenti Anna Esempio e Bruno Esempio.

**Perché la soluzione regge.** La condotta è descritta prima di qualificarla; l'autore dell'osservazione e delle fotografie è riconoscibile; l'atto non pretende di sostituire identificazione, CNR o eventuali altri verbali necessari. Il ramo penale e quello di ripristino hanno destinatari e presupposti distinti. Una CNR può essere necessaria anche contro ignoti: nella variante in cui il conducente riesce ad allontanarsi, non si archivia l'intervento come semplice relazione interna per la sola mancanza del nominativo.

'''
assert t.count(anchor)==1;t=t.replace(anchor,block+anchor)
t=t.replace('Non offre fac-simili ufficiali, che dipendono da regolamenti, gestionali e procedure del singolo ente; propone una sequenza di ragionamento con cui affrontare una traccia concorsuale e verificare la tenuta di un documento prima della firma.','Propone una sequenza di ragionamento e due elaborati didattici svolti, distinti dalla modulistica ufficiale dell’ente, per affrontare una traccia concorsuale e verificare la tenuta di un documento prima della firma.')
for source in ['sources/vol-02-pl-qualifiche-sanzioni-verifica-2026-10-03','sources/legge-689-procedura-verifica-2026-10-03','sources/vol-02-pl-pg-verifica-2026-10-03','sources/vol-02-pl-edilizia-ambiente-verifica-2026-10-03']:
 for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
t=re.sub(r'^volume_chapter:.*$','volume_chapter: 49',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf-8')
sp=art/'VOL-02-changes.json';s=json.loads(sp.read_text(encoding='utf-8'));r=s['changes']['V02-20'];r['files']=list(dict.fromkeys(r['files']+[p.as_posix()]));r['change']+=' Laboratorio FL04: verbale L689 completo e annotazione PG svolta.';r['evidence']+=' Pagamento200/difese30gg, qualificazione rifiuto255 e CNR distinta; dati e norma settoriale didattica espressamente fittizi.';r['status']='Parziale: tre laboratori applicati; resta simulazione integrata capitolo50';sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('FL04/15 integrato')
