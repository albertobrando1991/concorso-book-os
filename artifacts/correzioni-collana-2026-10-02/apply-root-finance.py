import importlib.util,re
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-impiego-contabilita-contratti-correzioni-2026-10-03.md';u.REF=ref
for topic in ['pubblico-impiego','contabilita-pubblica','contratti-pubblici']:
 p=Path('wiki/topics')/(topic+'.md');assert p.exists(),p
 with p.open('a',encoding='utf8') as f:f.write('\n\n## Integrazioni comuni — 3 ottobre 2026\n\n[[sources/vol-01-impiego-contabilita-contratti-correzioni-2026-10-03]] consolida distinzioni concorsuali, termini disciplinari, PIAO, residui statali/armonizzati, calcoli del risultato e dati essenziali dei contratti. Destinazioni: capitoli 6, 8, 9 e glossari del Metodo BANDO.\n')
s='pubblico-impiego-e-organizzazione-pa';t=u.read(s)
t=u.replace(t,'Alcune categorie possono avere regimi speciali. Il candidato non deve imparare un elenco fuori contesto, ma deve capire la logica: alcune funzioni richiedono regole particolari per status, autonomia, garanzie o disciplina di servizio.', '''L’art. 3 del D.Lgs. 165/2001 mantiene specifiche categorie nei rispettivi ordinamenti pubblicistici. Ecco il perimetro essenziale:

| Gruppo | Categorie da riconoscere |
|---|---|
| Giustizia e rappresentanza dello Stato | Magistrati ordinari, amministrativi, contabili e tributari; avvocati e procuratori dello Stato. |
| Sicurezza e amministrazione statale | Personale militare e delle Forze di polizia di Stato; carriere diplomatica e prefettizia. |
| Ordinamenti specifici | Personale degli enti nei settori richiamati dal comma 1, tra cui Banca d’Italia, Consob e AGCM; personale dei Vigili del fuoco nei limiti del comma 1-bis; carriera dirigenziale penitenziaria. |
| Università | Professori e ricercatori universitari secondo il comma 2, non indistintamente tutto il personale dell’ateneo. |

**Confronto:** un agente di polizia locale non rientra per questo solo fatto nelle Forze di polizia di Stato; un impiegato amministrativo universitario non diventa personale non contrattualizzato perché lavora accanto a un professore. Prima individua categoria e ordinamento, poi il contratto eventualmente applicabile.''')
t=u.replace(t,'| Riserve | Quote o preferenze previste dalla legge per categorie determinate. | Ignorare che devono avere base normativa. |', '| Riserve | Quote di posti destinate a categorie individuate dalla legge, applicate secondo la disciplina concorsuale. | Confonderle con preferenze a parità di punteggio. |')
anchor='Il candidato deve collegare sempre accesso, fabbisogno e competenze:'
t=u.replace(t,anchor,'''#### Riserva, preferenza e titolo valutabile: tre effetti diversi

La **riserva** incide sui posti da assegnare a determinate categorie; la **preferenza** ordina candidati a parità secondo la normativa; il **titolo valutabile** attribuisce punti se la procedura li prevede. La riserva non elimina requisiti e idoneità.

**Tre esempi separati, con dati didattici:**

- Due posti, uno riservato: Anna 90, Bruno 85, Carla 80; tutti idonei, solo Carla ha la riserva. Applicando questa ipotesi, il posto riservato va a Carla e l’altro ad Anna. Non si aggiungono punti a Carla.
- Un posto, Anna e Bruno entrambi a 85: se Bruno possiede la preferenza applicabile e prevalente nel caso, viene prima di Anna. Entrambi conservano 85 punti.
- Concorso per titoli ed esami: Anna ha 80 nelle prove e 3 nei titoli, Bruno 82 e 0. I totali sono 83 e 82: qui l’ordine cambia per punti, non per una preferenza.

Nella domanda controlla separatamente dichiarazione, possesso alla data richiesta e documentazione dei benefici. Non inventare una riserva a partire da una semplice preferenza.

Il candidato deve collegare sempre accesso, fabbisogno e competenze:''')
t=u.replace(t,'| Concussione | Il pubblico ufficiale, abusando della qualità o dei poteri, costringe qualcuno a dare o promettere un’utilità indebita. | La parola chiave è costringe: la pressione annulla la libertà di scelta del privato. |', '| Concussione | Il pubblico ufficiale o l’incaricato di pubblico servizio, abusando della qualità o dei poteri, costringe a dare o promettere indebitamente a sé o a un terzo denaro o altra utilità. | Art. 317 c.p.: costrizione, distinta da induzione e accordo corruttivo. Non occorre descriverla come annullamento assoluto della volontà. |')
t=u.replace(t,'| Il privato subisce una pressione irresistibile dal pubblico ufficiale. | Costrizione: il privato non negozia su un piano di libertà effettiva. |', '| Il pubblico ufficiale o l’incaricato di pubblico servizio abusa del ruolo per costringere il privato. | Costrizione: la libertà di autodeterminazione è gravemente limitata; “irresistibile” non è un requisito testuale autonomo. |')
anchor='Il PIAO è quindi un ponte tra questo capitolo e quelli su trasparenza, anticorruzione e metodo di studio dei profili amministrativi.'
t=u.replace(t,anchor,'''Il piano ha durata **triennale** e aggiornamento **annuale**. Il Piano tipo comprende scheda anagrafica, valore pubblico/performance/anticorruzione, organizzazione e capitale umano, monitoraggio, con le semplificazioni applicabili. Le istituzioni scolastiche e le scuole di ogni ordine e grado sono escluse dall’ambito indicato dall’art. 6 del DL 80/2021.

**Attenzione al numero 50:** nell’impostazione applicativa ANAC del PNA 2022, almeno 50 dipendenti comportano il regime ordinario e meno di 50 quello semplificato. I testi hanno formulazioni non identiche: il DPR 81/2022 parla anche di “non più di cinquanta”, mentre l’art. 6 del DM 132/2022 usa “meno di cinquanta”. Non collocare automaticamente un ente con esattamente 50 dipendenti nel semplificato, né affermare che le formule normative siano uguali. Se il quiz cita uno specifico articolo, rispetta il suo tenore; nel caso applicativo considera il coordinamento ANAC.

**Caso:** il Comune intende ridurre i tempi di risposta. Il PIAO deve collegare obiettivo e indicatore ai processi, alle competenze necessarie, alla formazione e ai rischi; non basta ripetere “migliorare i servizi”. Il bilancio conserva la propria funzione finanziaria: il PIAO non lo sostituisce.''')
anchor='### 6. Mansioni, orario e trattamento economico'
t=u.replace(t,anchor,'''#### Il procedimento disciplinare ordinario: soggetti e termini

Per il rimprovero verbale è competente il responsabile della struttura e si applica il CCNL. Per sanzioni superiori opera l’UPD, secondo l’art. 55-bis, ferme le discipline speciali.

| Passaggio | Regola ordinaria |
|---|---|
| Segnalazione all’UPD | Immediata, comunque entro 10 giorni dalla conoscenza dei fatti da parte del responsabile della struttura. |
| Contestazione scritta | Immediata, comunque entro 30 giorni dalla segnalazione ricevuta o dalla piena conoscenza dei fatti da parte dell’UPD. |
| Audizione | Preavviso di almeno 20 giorni; contraddittorio e possibilità di assistenza di procuratore o rappresentante sindacale. |
| Conclusione | Archiviazione o sanzione entro 120 giorni dalla contestazione. |

Il dipendente può depositare memorie e chiedere una sola volta il differimento dell’audizione per grave e oggettivo impedimento, con corrispondente proroga finale. Contestazione e conclusione sono termini perentori nel regime richiamato dal comma 9-ter. Non estendere la tabella ai procedimenti accelerati per falsa attestazione della presenza o alle competenze speciali scolastiche del comma 9-quater.

**Caso:** il responsabile ritiene un fatto punibile oltre il rimprovero verbale. Deve trasmetterlo tempestivamente all’UPD, non irrogare da sé una sospensione secondo il regime ordinario. I 120 giorni decorrono dalla contestazione, non dalla prima voce informale ricevuta in ufficio. Per ferie, permessi e sanzioni contrattuali consulta sul portale ARAN il **CCNL del comparto/area applicabile**, sezioni «Rapporto di lavoro» e «Responsabilità disciplinare», controllando periodo, testo definitivo e decorrenza della singola clausola.

'''+anchor)
u.save(s,t,['V01-13','V01-14','V01-15'],ref)
s='contabilita-pubblica-essenziale';t=u.read(s)
t=u.replace(t,'| Contratti pubblici | Capitolo 5 |','| Contratti pubblici | Capitolo 9 |')
a=t.index('I **residui attivi**');b=t.index('### 7. Tesoreria',a)
t=t[:a]+'''I **residui** presuppongono operazioni giuridico-contabili già sorte: una semplice previsione non realizzata non genera da sola un residuo. Occorre distinguere il sistema considerato.

| Contesto | Residui attivi e passivi |
|---|---|
| Enti territoriali armonizzati | Attivi: entrate accertate, esigibili e non riscosse; passivi: spese impegnate, esigibili e non pagate, da mantenere dopo la verifica dei presupposti. |
| Bilancio dello Stato | I residui attivi comprendono somme accertate e non versate in tesoreria: sia ancora da riscuotere, sia riscosse dall’agente ma non versate. I passivi derivano dagli impegni non pagati secondo il regime statale. |

**Esempio statale:** accertato 100, riscosso 80, versato 60. Restano 20 da riscuotere e 20 riscossi ma da versare: residui attivi **40**. Rispondere 20 confonde riscossione e versamento.

Il **riaccertamento** negli enti armonizzati verifica esistenza, titolo, importo ed esigibilità. Un credito insussistente va cancellato con le motivazioni previste; un’obbligazione ancora esistente ma esigibile in un esercizio successivo va reimputata secondo il principio applicato, con il pertinente trattamento del FPV. Non chiamare “inesistente” un credito solo perché non è ancora scaduto.

Le **economie di spesa** sono, nel rispettivo regime, stanziamenti non impegnati o minori spese rispetto agli impegni mantenibili; non coincidono automaticamente con denaro libero da usare. Un debito non ancora pagato non è un’economia.

#### Risultato, FPV e FCDE: un calcolo completo

Per un ente locale, l’art. 186 TUEL collega il risultato di amministrazione a cassa e residui, al netto del FPV di spesa. Nel seguente esempio le verifiche sui residui sono già svolte e tutti gli importi sono in migliaia di euro.

| Dato | Importo |
|---|---:|
| Fondo cassa finale | 120 |
| Residui attivi | +80 |
| Residui passivi | −50 |
| FPV di spesa | −30 |
| Risultato di amministrazione | **120** |

La formula è **120 + 80 − 50 − 30 = 120**. Il risultato si distingue poi nelle componenti dell’art. 187:

| Componente | Importo |
|---|---:|
| Accantonata, di cui FCDE 35 | 45 |
| Vincolata | 40 |
| Destinata agli investimenti | 10 |
| Disponibile | **25** |

La parte disponibile è **120 − 45 − 40 − 10 = 25**. Il FCDE è già incluso nei 45 accantonati: sottrarlo una seconda volta sarebbe un errore. Se, a parità degli altri dati, la parte accantonata fosse 80, la disponibile sarebbe **−10**: un risultato complessivo positivo non esclude un disavanzo della componente disponibile. L’utilizzo delle quote resta soggetto ai vincoli e alle condizioni di legge.

Il **FPV** collega copertura finanziaria e spesa imputata a esercizi successivi. Esempio distinto: un’entrata vincolata di 100 è accertata nell’anno N; un’obbligazione di spesa perfezionata di 100 è esigibile per 40 in N e per 60 in N+1. Nelle condizioni del principio applicato, il FPV di 60 conserva il collegamento della copertura alla spesa futura. Non è un fondo per crediti difficili da incassare né un nuovo incasso nell’anno successivo.

Il **FCDE** è un accantonamento prudenziale per crediti di dubbia riscossione. Se, in un esempio semplificato, la base soggetta ad accantonamento è 100 e il coefficiente prudenziale già determinato secondo il principio contabile è 30%, l’accantonamento è **30**. Non basta però scegliere una percentuale a piacere: base, esclusioni, serie storiche e modalità effettive seguono il principio applicato. L’accantonamento non cancella il credito e non sospende il dovere di riscuoterlo.

**Verifica:** stanziamento 50 senza obbligazione perfezionata significa residuo passivo 50? No. FPV e FCDE hanno la stessa funzione? No: il primo raccorda esercizi di imputazione e copertura, il secondo protegge gli equilibri dal rischio di mancata riscossione. Nell’esempio del risultato, la somma delle quattro componenti deve tornare a 120.

''' +t[b:]
t=u.replace(t,'Confondere CIG e CUP è un errore frequente.', 'I codici hanno funzioni diverse e, quando il progetto richiede CUP, possono accompagnare insieme il medesimo contratto: non sono alternative liberamente intercambiabili.')
t=t.replace('Traccia normativa e mappa di studio P9','Traccia normativa e mappa di studio').replace('**Checkpoint P9.**','**Checkpoint.**').replace('Fonte consolidata nel wiki','Riferimento normativo').replace('CIG o CUP →','CIG e CUP quando richiesti →')
sources={'contabilita-generale-stato-e-bilancio-stato':'L. 196/2009 e regolamento di contabilità statale','armonizzazione-contabile-enti-territoriali-d-lgs-118-2011':'D.Lgs. 118/2011','ordinamento-finanziario-enti-locali-tuel-dup-peg-rendiconto-revisione':'TUEL, parte II','corte-conti-controlli-responsabilita-agenti-contabili':'L. 20/1994 e D.Lgs. 174/2016','pagamenti-tracciabilita-contratti-pnrr-rendicontazione':'L. 136/2010 e L. 3/2003, art. 11'}
for key,val in sources.items():t=t.replace('[[sources/'+key+']]',val)
t=u.replace(t,'| Residuo attivo | Entrata accertata e non riscossa. |','| Residuo attivo | Entrata accertata e non riscossa negli enti armonizzati; nello Stato anche riscossa e non versata, secondo la sezione 6. |')
u.save(s,t,['V01-19','V01-20','V01-21','V01-49'],ref)
s='appendice-a-glossario-essenziale-pa';t=u.read(s)
t=u.replace(t,'| Preferenza | Criterio che può incidere sull’ordine tra candidati in condizioni previste. | Non aumenta il punteggio della prova se il bando non lo prevede. |','| Preferenza | Criterio legale che ordina candidati a parità nelle condizioni previste. | Non attribuisce punti: distinguere titoli valutabili e riserva di posti. |')
t=u.replace(t,'| Area o famiglia professionale | Raggruppamento di profili simili per funzioni, livello e competenze. | Serve a capire che cosa resta comune e che cosa cambia tra concorsi. |','| Area di inquadramento | Livello della classificazione professionale previsto dal contratto applicabile. | Non coincide con la famiglia professionale. |\n| Famiglia professionale | Insieme di ambiti professionali omogenei, definito nel relativo sistema organizzativo. | Collega conoscenze e competenze funzionali senza sostituire l’area di inquadramento. |')
t=t.replace('Soggetto pubblico che affida un contratto di appalto.','Soggetto pubblico o altro soggetto tenuto alla disciplina del Codice che affida un appalto.').replace('Non coincide sempre con stipula o avvio dell’esecuzione.','È distinta dalla stipula: l’aggiudicazione non conclude il contratto.')
u.save(s,t,['V01-13','V01-46'],ref)
s='appendice-b-100-parole-chiave-concorsi';t=u.read(s)
t=t.replace('facilità controlli','facilita controlli')
t=u.replace(t,'| 67 | Residui | Entrate o spese non riscosse o non pagate entro l’esercizio. | “I residui mostrano effetti della gestione oltre l’anno di competenza.” |','| 67 | Residui | Entrate accertate o spese impegnate rimaste da riscuotere o pagare secondo il regime applicabile; nello Stato gli attivi comprendono anche somme riscosse non versate. | “La sola previsione non genera un residuo.” |')
t=u.replace(t,'## 8. Bando e concorso','''**Collegamento tra entrata e spesa.** L’**accertamento** verifica ragione del credito, titolo, debitore, importo e scadenza secondo il regime contabile; l’**impegno** segue un’obbligazione passiva giuridicamente perfezionata, individua creditore, ragione, importo e scadenza e vincola lo stanziamento. Negli enti armonizzati l’imputazione segue l’esigibilità. Nessuno dei due coincide con il movimento di cassa. Riprendi il Capitolo 8, sezioni sulle fasi di entrata e spesa e «Gestione del bilancio».

## 8. Bando e concorso''')
u.save(s,t,['V01-19','V01-47'],ref)
u.record()
