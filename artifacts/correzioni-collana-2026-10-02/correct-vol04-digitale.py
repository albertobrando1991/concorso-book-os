from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');p=next(B.glob('12-*'));t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest()
t=t.replace('status: reviewed','status: revised_draft').replace('draft_stage: reviewed','draft_stage: editorial-revision').replace('review_required: false','review_required: true').replace('2026-08-18T12:00:00+02:00','2026-10-03T12:00:00+02:00')
t=t.replace('source_refs: [','source_refs: [\n  "sources/vol-04-digitale-verifica-2026-10-03.md",',1).replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/sources/vol-04-digitale-verifica-2026-10-03.md",',1)
t=t.replace('percio','perciò').replace('al 18 agosto 2026','al 3 ottobre 2026')
t=t.replace('8. la cancelleria o segreteria effettua l’intervento di competenza;','8. il sistema o la cancelleria completa l’accettazione secondo la tipologia e gli esiti;').replace("8. la cancelleria o segreteria effettua l'intervento di competenza;","8. il sistema o la cancelleria completa l'accettazione secondo la tipologia e gli esiti;")
t=t.replace("4. **esito dell'intervento di cancelleria:** l'ufficio accetta o rifiuta il deposito secondo la disciplina e le istruzioni applicabili.","4. **esito dell'accettazione del deposito:** comunica l'accettazione, automatica o dopo intervento della cancelleria, oppure il rifiuto nei casi previsti.")
a=t.index('Queste tracce descrivono passaggi diversi.');b=t.index('### Portale dei Servizi Telematici',a)
t=t[:a]+'''### Quando il deposito civile è tempestivo

L'art. 196-sexies delle disposizioni di attuazione del c.p.c. considera il deposito avvenuto quando è generata la conferma del completamento della trasmissione prevista dalle regole applicabili. La conferma deve essere generata entro la fine del giorno di scadenza; si applicano i commi quarto e quinto dell'art. 155 c.p.c. sul giorno festivo e sul sabato per gli atti processuali fuori udienza. Non occorre che l'ufficio lavori l'atto entro l'orario di apertura dello sportello.

Per il deposito civile tramite PEC regolato dalle specifiche tecniche del 7 agosto 2024, efficaci dal 30 settembre 2024, l'art. 17, comma 11, precisa il momento: **se l'atto viene accettato, gli effetti risalgono alla generazione della ricevuta di accettazione del gestore PEC del depositante, cioè la prima PEC (RdA)**. L'accettazione finale può essere automatica o seguire l'intervento della cancelleria. Non confondere questa prima ricevuta del gestore PEC con la quarta comunicazione che dà l'esito dell'accettazione del deposito.

La **RdAC**, seconda PEC, attesta la consegna alla casella dell'ufficio. Era il riferimento espresso della disciplina previgente dell'art. 16-bis, comma 7, del D.L. 179/2012. Leggendo precedenti o schede meno recenti bisogna quindi individuare la disciplina applicabile al deposito: non trasformare la regola storica della seconda PEC in una regola universale attuale. La Rassegna tematica della Corte di cassazione aggiornata al 30 giugno 2025, sezione sul deposito telematico, illustra questo passaggio.

La condizione del buon fine è decisiva. La prima PEC tempestiva non sana una busta rifiutata per un errore FATAL e non autorizza a ignorare gli esiti successivi. La cancelleria registra le evidenze; la valutazione giurisdizionale di decadenze, validità o rimessione in termini compete al giudice.

| Evidenza nel regime attuale | Che cosa prova | Che cosa controllare ancora |
|---|---|---|
| RdA, prima PEC | Presa in carico del gestore del depositante; momento cui risalgono gli effetti se il deposito è accettato | Consegna, controlli e buon fine |
| RdAC, seconda PEC | Consegna alla casella destinataria | Coerenza ufficio/fascicolo ed esiti del deposito |
| Terza comunicazione | Risultato dei controlli automatici | Natura di eventuali WARN, ERROR o FATAL |
| Quarta comunicazione | Accettazione automatica/manuale o rifiuto | Associazione al fascicolo, ragione dell'esito e adempimenti |

**Esempio fittizio.** Termine il 6 ottobre 2026. RdA alle 23:58 del 6 ottobre, RdAC alle 00:01 del 7 ottobre, controlli positivi e accettazione alle 09:10 del 7 ottobre: nel regime appena descritto gli effetti risalgono alle 23:58 e il deposito è tempestivo. Se invece il sistema rifiuta una busta indecifrabile, la prima PEC non basta a dare per perfezionato il deposito; occorrono una reazione tempestiva e l'esame dei rimedi applicabili. Non aspettare l'ultimo minuto: l'esempio serve a capire la regola, non a consigliare una strategia rischiosa.

### Formati, dimensioni e tre classi di anomalia

L'atto principale civile deve essere PDF o PDF/A ottenuto da un documento testuale, selezionabile e copiabile, senza elementi attivi e senza password, con la firma richiesta. La scansione di un foglio non sostituisce ordinariamente questo atto principale. Gli allegati seguono l'art. 16 delle specifiche: possono comprendere altri formati ammessi; la firma è richiesta nei casi previsti dalla legge, non indistintamente su ogni file. Nel penale sono previste regole specifiche anche per la scansione degli atti formati personalmente dalle parti.

Nel civile il limite di 60 MB delle specifiche, dopo la rettifica del 16 settembre 2024, riguarda **Atto.enc**, il file cifrato, non l'intero messaggio PEC. Il gestore di posta può imporre ulteriori limiti tecnici: verificare entrambi. Se gli atti eccedono le dimensioni ammesse, l'art. 196-sexies consente più trasmissioni; ciascuna deve essere tracciata e tempestiva per i documenti che contiene. Una prima trasmissione puntuale non rende automaticamente tempestivi allegati inviati dopo la scadenza.

| Codice | Significato nelle specifiche | Conseguenza operativa |
|---|---|---|
| WARN / WARNING | Anomalia non bloccante; può segnalare, per esempio, un problema relativo alla procura o al certificato di firma | Leggere il rilievo; non dedurre automaticamente invalidità o rifiuto |
| ERROR | Anomalia che richiede intervento della cancelleria per consentire l'accettazione | L'operatore effettua le verifiche necessarie; non equivale a FATAL |
| FATAL | Anomalia non gestita o non gestibile, per esempio busta indecifrabile o elementi essenziali mancanti | Comunicazione di rifiuto; la busta non si sblocca con una semplice accettazione manuale |

Non attribuire un codice in base alla sola impressione: una firma problematica non è sempre FATAL. Si legge l'esito realmente restituito, si verifica la causa e si conserva la sequenza. L'operatore non decide con il codice tecnico l'ammissibilità processuale dell'atto.

Le specifiche prevedono l'**accettazione automatica** salvo anomalie o necessità di intervento dell'ufficio. La circolare del 19 settembre 2024 ne ha regolato l'avvio per determinate categorie di atti, tra cui memorie dell'art. 171-ter, mantenendo le quattro comunicazioni e distinguendo nel quarto esito l'accettazione automatica da quella manuale. Nella prima implementazione, WARN ed ERROR restavano alla lavorazione dell'ufficio. Per il servizio concreto si controlla la versione attiva: non si assume né che tutti gli atti siano automatici né che ogni quarta PEC richieda un'operazione manuale.

''' +t[b:]
t=t.replace("Nel luglio 2026 la pagina malfunzionamenti mostra segnalazioni relative al Portale Deposito Penale, ad applicativi penali e a sistemi civili e penali. Questo conferma una regola pratica: in materia telematica, l'evento tecnico può avere rilievo operativo.","Le attestazioni di malfunzionamento identificano servizio e intervallo interessati. In materia telematica l'evento tecnico può avere rilievo operativo, ma non produce sempre una proroga automatica.")
a=t.index('Il D.M. 114/2026 rimodula la transizione');b=t.index('### Deposito penale e Portale deposito atti',a)
t=t[:a]+'''Il riferimento operativo è l'art. 3 del D.M. 217/2023 nel testo vigente. Il calendario va letto insieme all'art. 111-bis c.p.p.: restano gli atti e documenti non acquisibili in copia informatica per natura o specifiche esigenze processuali; gli atti che le parti e la persona offesa compiono personalmente possono essere depositati anche con modalità non telematiche.

| Ambito | Regola al 3 ottobre 2026 | Limite da ricordare |
|---|---|---|
| Procure ordinarie, Procura europea, GIP, tribunali ordinari; PG per avocazione | Deposito telematico come regola dal 1° gennaio 2025 | Leggere le deroghe e le categorie dei commi successivi |
| Depositi degli abilitati interni relativi alle intercettazioni | Ammessi anche non telematicamente sino al 31 dicembre 2026 | Deroga del comma 3-bis, non estesa a ogni deposito penale |
| Corte d'appello e relativa PG | Obbligo generale previsto dal 1° luglio 2027 | Esclusi gli ambiti speciali del comma 5 e del 5-bis |
| Cassazione, PG Cassazione e giudice di pace | Obbligo previsto dal 1° gennaio 2028 | Con le esclusioni specifiche della norma |
| Tribunale e Procura minorili; sezione minorile d'appello | Decorrenza prevista 1° gennaio 2029 | Non anticiparla alla generalità del penale ordinario |
| Tribunale di sorveglianza | Decorrenza prevista 1° gennaio 2030 | Distinta dal calendario generale dell'esecuzione |

Le deroghe dei commi 2 e 3 sono cessate il 31 dicembre 2025; quella del comma 3-ter il 31 marzo 2026. Non presentarle come tuttora aperte. Il comma 5-bis stabilisce inoltre date proprie: impugnazioni contro i provvedimenti del giudice di pace dal **1° gennaio 2028**; procedimenti del libro X c.p.p., sull'esecuzione, dal **1° luglio 2029**; riparazione per ingiusta detenzione, rescissione del giudicato, revisione, rapporti giurisdizionali con autorità straniere e procedimenti in materia di prevenzione, mandato d'arresto europeo e consegna tra Stati membri dal **1° luglio 2030**. Queste disposizioni specifiche impediscono di applicare meccanicamente la data generale dell'ufficio.

Il comma 6 consente ai soggetti esterni il deposito anche telematico in appello sino al 30 giugno 2027 e in Cassazione e davanti al giudice di pace sino al 31 dicembre 2027. Il comma 7 contempla ulteriori attivazioni anticipate, negli ambiti indicati, previo provvedimento che attesti la funzionalità dei sistemi pubblicato sul PST. Il comma 9 mantiene per i difensori il deposito PEC disciplinato dall'art. 87-bis D.Lgs. 150/2022 nei casi in cui è ammesso anche il deposito non telematico: **la PEC non è un'alternativa libera al PDP dove quest'ultimo è obbligatorio**.

Per risolvere un quesito, indica quindi: data del deposito, soggetto interno o esterno, ufficio, atto e procedimento, comma applicabile, eventuale attestazione di funzionalità o malfunzionamento. Le date future qui riportate sono quelle programmate dal testo vigente al 3 ottobre 2026: vanno ricontrollate per prove successive.

''' +t[b:]
needle='Una risposta professionale non deve trasformarsi in istruzione per usare il portale. Deve spiegare il metodo di controllo.'
t=t.replace(needle,'''Nel PDP l'art. 13-bis D.M. 44/2011 collega la ricezione alla ricevuta di accettazione generata dal portale, salvo anomalie bloccanti. Le specifiche prevedono una ricevuta scaricabile con identificativo unico nazionale, dati inseriti e data/ora dell'operazione di invio rilevate dai sistemi ministeriali. L'art. 172, comma 6-bis, c.p.p. permette il deposito sino alle ore 24 del giorno di scadenza e richiede l'accettazione dal sistema entro quel termine: non basta l'orario visualizzato sul computer del mittente.

Gli stati **INVIATO**, **IN TRANSITO**, **IN VERIFICA**, **ACCETTATO**, **RIFIUTATO** ed **ERRORE TECNICO** descrivono fasi diverse. In verifica l'ufficio deve risolvere la mancata coincidenza dei dati; il rifiuto è motivato nel portale; l'errore tecnico richiede la nuova trasmissione indicata dal sistema. Le notifiche email di cortesia non sostituiscono la ricevuta e gli esiti disponibili nel PDP.

Per denuncia, querela e istanza di procedimento, l'accoglimento equivale al **ricevimento nel ReGeWEB**, come chiarito dalla rettifica del 30 ottobre 2024: non implica da solo l'iscrizione automatica di una notizia di reato contro un determinato indagato. Il limite delle specifiche è 60 MB per singolo file e 600 MB per l'intero deposito PDP, diverso dal limite civile di Atto.enc.''')
t=t.replace("Il RegIndE e gli altri elenchi rilevanti servono a individuare indirizzi e soggetti abilitati secondo le regole. L'errore da evitare è pensare che qualsiasi PEC trovata online sia valida per il processo.",'''Il **ReGIndE**, Registro generale degli indirizzi elettronici, è gestito dal Ministero della giustizia e censisce dati identificativi e PEC dei soggetti abilitati esterni, come difensori e ausiliari. L'iscrizione non attribuisce da sola il diritto di consultare ogni fascicolo.

| Registro o indice | Soggetti e funzione | Distinzione utile |
|---|---|---|
| ReGIndE | Soggetti abilitati esterni ai servizi della giustizia | Non è l'elenco generale di tutti i cittadini |
| INI-PEC, art. 6-bis CAD | Imprese e professionisti; comprende le ulteriori categorie professionali previste dalla legge | Non è il registro delle abilitazioni al fascicolo |
| INAD, art. 6-quater CAD | Persone fisiche, professionisti e altri enti privati non tenuti a INI-PEC, con le regole di coordinamento previste | Un domicilio digitale personale non equivale a qualifica di difensore |
| IPA, art. 6-ter CAD | PA, gestori di pubblici servizi e società a controllo pubblico | Distinto dal Registro PP.AA. del Ministero della giustizia |

Per una notificazione si controlla quale pubblico elenco sia utilizzabile secondo la specifica disciplina processuale. Una PEC trovata sul sito del destinatario, o la sola presenza in un indice, non sostituisce questa verifica.''')
needle='Una buona risposta non cerca il colpevole. Ricostruisce il flusso e individua il punto di rottura.'
t=t.replace(needle,'''### Malfunzionamento: civile e penale hanno regole distinte

Nel **civile**, l'art. 196-quater disp. att. c.p.c. permette al capo dell'ufficio di autorizzare il deposito non telematico quando ricorre l'urgenza e l'indisponibilità dei sistemi del dominio giustizia è certificata dall'autorità ministeriale competente e pubblicata sul PST. Separatamente, il giudice può ordinare singoli atti o documenti cartacei necessari alla decisione, specificandone la ragione. Un guasto al computer personale non equivale a certificazione ministeriale.

Nel **penale**, l'art. 175-bis c.p.p. disciplina sia il malfunzionamento certificato centralmente sia quello accertato e attestato dal dirigente dell'ufficio, con comunicazione dell'intervallo interessato. Durante l'indisponibilità si usano le forme non telematiche previste. Se scade un termine a pena di decadenza, la restituzione nel termine non è automatica: occorre provare che caso fortuito o forza maggiore hanno impedito il deposito tempestivo anche attraverso la modalità sostitutiva, applicando l'art. 175.

La scheda dell'operatore registra sistema, inizio/fine, attestazione, tentativi, canale sostitutivo e provvedimenti. Conserva le prove senza promettere all'utente che «il termine si allunga sempre».''')
a=t.index('### Caso guidato: deposito civile con anomalia');b=t.index('### Caso guidato: deposito penale in regime transitorio',a)
t=t[:a]+'''### Dossier svolto: tre depositi civili a confronto

**Caso fittizio, regime attuale delle specifiche 2024.** Il termine indicato dalla traccia scade il 6 ottobre 2026. Non vi sono malfunzionamenti ministeriali né proroghe. La cancelleria riceve questi estratti dei registri; i nomi sono inventati.

**Documento A — difensore Rossi.** RdA 6 ottobre ore 23:58; RdAC 7 ottobre ore 00:01; controllo positivo; quarta comunicazione «accettato automaticamente» 7 ottobre ore 00:03. Atto associato al fascicolo corretto.

**Documento B — difensore Verdi.** RdA 6 ottobre ore 18:10; RdAC ore 18:11; esito ERROR per dati che richiedono verifica; 7 ottobre ore 09:20 la cancelleria identifica univocamente il fascicolo e accetta il deposito. Non emerge alcun diverso vizio processuale.

**Documento C — difensore Neri.** RdA 6 ottobre ore 17:30; RdAC ore 17:31; FATAL: Atto.enc indecifrabile; comunicazione di rifiuto ore 17:32. Nessun nuovo deposito risulta nella documentazione.

**Consegna — 20 minuti.** Per ciascun deposito scrivi una riga con esito, riferimento temporale, azione dell'ufficio e limite della conclusione. Poi indica se l'orario della quarta comunicazione determina la tardività.

| Deposito | Soluzione motivata | Seguito |
|---|---|---|
| A | Tempestivo: buon fine e RdA entro il 6 ottobre; la RdAC dopo mezzanotte non sposta l'effetto previsto dall'art. 17, comma 11 | Registrare corretta associazione; nessuna accettazione manuale da inventare |
| B | Tempestivo nel caso: ERROR è stato risolto e gli effetti dell'accettazione risalgono alla RdA delle 18:10 | Conservare rilievo e intervento, senza equiparare ERROR a FATAL |
| C | Non attestare deposito perfezionato: la busta è stata rifiutata; la RdA non neutralizza il FATAL | Tracciare rifiuto; il depositante deve reagire, il giudice valuta gli eventuali rimedi |

**Punteggio: 12 punti.** Tre per ogni deposito: uno per l'esito, uno per il momento o l'impedimento decisivo, uno per l'azione corretta. Tre finali per distinguere RdA da RdAC, quarto esito da momento cui risalgono gli effetti, e registrazione amministrativa da decisione del giudice. Una risposta che usa la quarta comunicazione del 7 ottobre per dichiarare tardivi A e B perde i punti relativi al tempo.

''' +t[b:]
t=t.replace('Questa scheda è volutamente generale. In prova non ti chiederanno di gestire davvero il sistema, ma possono chiederti di ragionare come un funzionario che sa leggere il percorso dell’atto.','La scheda serve a ricostruire il percorso dell’atto. Se il bando prevede una prova su applicativi, aggiungi l’allenamento alle funzioni effettivamente richieste.').replace("Questa scheda è volutamente generale. In prova non ti chiederanno di gestire davvero il sistema, ma possono chiederti di ragionare come un funzionario che sa leggere il percorso dell'atto.","La scheda serve a ricostruire il percorso dell'atto. Se il bando prevede una prova su applicativi, aggiungi l'allenamento alle funzioni effettivamente richieste.")
a=t.index('### Quiz commentato');b=t.index('### Checklist di ripasso',a)
t=t[:a]+'''### Quiz commentato

1. **Nel regime delle specifiche del 2024, un deposito civile è accettato il giorno dopo la scadenza. La RdA è delle 23:58 del giorno di scadenza. Quale conclusione è corretta, in assenza di altri vizi?**
   - A. È tardivo perché conta sempre la quarta PEC.
   - B. È tempestivo solo se il cancelliere aveva aperto la busta prima di mezzanotte.
   - C. L'effetto dell'accettazione risale alla RdA tempestiva del depositante.
   - D. È tempestivo perché ogni accettazione proroga il termine di un giorno.
   **Risposta corretta: C.** Art. 196-sexies e art. 17, comma 11, delle specifiche: prima PEC, subordinatamente al buon fine. A e B spostano il tempo sull'ufficio; D inventa una proroga.

2. **Quale coppia distingue correttamente ERROR e FATAL?**
   - A. ERROR richiede intervento dell'ufficio; FATAL indica un'anomalia non gestibile che porta al rifiuto.
   - B. ERROR riguarda sempre il contenuto giuridico; FATAL è un avviso non bloccante.
   - C. Entrambi vengono sempre sanati dall'accettazione automatica.
   - D. ERROR prova sempre tardività; FATAL prova sempre difetto di procura.
   **Risposta corretta: A.** Le specifiche distinguono possibilità di intervento e impossibilità di elaborazione. Le altre risposte attribuiscono ai codici effetti o cause che non hanno.

3. **Quale descrizione del ReGIndE è corretta?**
   - A. Censisce obbligatoriamente tutte le persone residenti in Italia.
   - B. Coincide con IPA e con il Registro PP.AA. della giustizia.
   - C. Attribuisce a ogni iscritto accesso a tutti i fascicoli.
   - D. Contiene dati identificativi e PEC dei soggetti abilitati esterni ai servizi della giustizia.
   **Risposta corretta: D.** È un registro ministeriale di soggetti abilitati. Censimento, domicilio digitale e autorizzazione al singolo fascicolo sono piani distinti.

4. **Il 3 ottobre 2026 un soggetto interno deposita un atto relativo a intercettazioni. Quale deroga temporale del D.M. 217/2023 vigente deve considerare?**
   - A. Tutti i depositi penali sono facoltativi sino al 2030.
   - B. Il comma 3-bis consente anche modalità non telematiche sino al 31 dicembre 2026 per gli atti indicati.
   - C. Si applica sempre la deroga cessata il 31 marzo 2026.
   - D. L'esistenza di una PEC personale autorizza qualsiasi canale.
   **Risposta corretta: B.** La deroga è specifica per soggetti interni e materia. A la generalizza, C usa una disposizione temporalmente esaurita, D confonde indirizzo e canale consentito.

5. **Quale limite è correttamente associato al sistema?**
   - A. Nel PCT 600 MB per ciascuna PEC.
   - B. Nel PDP 60 MB per l'intero deposito, senza possibilità di più file.
   - C. Nel PCT 60 MB per Atto.enc; nel PDP 60 MB per file e 600 MB per deposito.
   - D. Nessun limite se tutti i file sono firmati.
   **Risposta corretta: C.** Si applicano art. 17 rettificato e art. 19 delle specifiche; restano da verificare i limiti tecnici del gestore PEC. La firma non aumenta le dimensioni ammesse.

6. **Durante un malfunzionamento penale attestato scade un termine a pena di decadenza. La restituzione nel termine è automatica?**
   - A. Sì, per tutti gli atti e per qualsiasi durata del guasto.
   - B. Sì, purché esista uno screenshot del computer personale.
   - C. No: è sempre esclusa perché esiste il cartaceo.
   - D. No: occorre dimostrare l'impedimento da caso fortuito o forza maggiore anche rispetto al deposito sostitutivo previsto.
   **Risposta corretta: D.** L'art. 175-bis, comma 5, richiede la prova e rinvia all'art. 175. Non vi è né proroga indiscriminata né esclusione assoluta del rimedio.

''' +t[b:]
t=t.replace('| Fascicolo, deposito, busta, ricevuta, controllo, anomalia, RegIndE, PST, DGSIA |','| Fascicolo, deposito, RdA/RdAC, WARN/ERROR/FATAL, ReGIndE, PST, DIT |')
t=t.replace('- So distinguere busta telematica, PEC, firma, dati XML, ricevute e controlli?','- So distinguere RdA, RdAC e quarto esito, spiegando quale regola temporale applicare al deposito attuale?\n- So distinguere WARN, ERROR e FATAL e accettazione automatica da manuale?')
assert len(re.findall('Risposta corretta:',t))==6
assert 'In prova non ti chiederanno' not in t
p.write_text(t,'utf-8')
Path('artifacts/correzioni-collana-2026-10-02/VOL-04-digitale-delta.json').write_text(json.dumps(dict(path=p.as_posix(),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest(),quizKeys=re.findall(r'Risposta corretta: ([A-D])',t),words=len(t.split()),auditIDs=['V04-18','V04-19'],publicationReady=False),ensure_ascii=False,indent=2),'utf-8')
print('Digitale',len(t.split()),'parole',re.findall(r'Risposta corretta: ([A-D])',t))
