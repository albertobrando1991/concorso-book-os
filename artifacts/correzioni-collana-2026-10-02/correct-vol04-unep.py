from pathlib import Path
import re,json,hashlib,shutil,datetime
A=Path('artifacts/correzioni-collana-2026-10-02');p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob('11-*.md'));t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest();b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
t=t.replace('Non sviluppa in modo analitico tutte le forme di notificazione, tutte le fasi dell\'espropriazione forzata o tutte le regole sui titoli esecutivi. Questi temi appartengono ai manuali di procedura civile e penale. Qui interessa la lettura d\'ufficio.',"Sviluppa i presupposti e i termini essenziali delle notificazioni e dell'esecuzione civile, collegandoli alla lettura d'ufficio e a documenti fittizi svolti. Le procedure speciali seguono le disposizioni proprie.")
t=t.replace('Restano fuori: formule di relata, calcolo di indennità','Restano fuori: formulari per ogni rito speciale, calcolo di indennità').replace('cioe su attività','cioè su attività')
t=t.replace('Al cut-off normativo del volume, Normattiva mostra il testo vigente, con ultimo aggiornamento dell\'atto indicato al 27 giugno 2015.',"Le disposizioni utilizzate sono verificate al 3 ottobre 2026; le denominazioni territoriali storiche vanno coordinate con l'attuale distribuzione degli uffici.")
t=t.replace('mentre termini, modalità, compensi, indennità, importi, registri e istruzioni locali vanno verificati alla data del bando e della prova.',"con i termini essenziali verificati qui indicati; eventuali modifiche successive e le istruzioni della sede vanno controllate prima della prova.")
at=t.index('### Notificazioni civili e penali')
t=t[:at]+'''### Competenza e scelta del canale

Gli artt. 106 e 107 del D.P.R. 1229/1959 collegano gli atti dell'ufficiale giudiziario al territorio della sede. La possibilità di notificare per posta senza limitazioni territoriali riguarda gli affari di competenza delle autorità giudiziarie della sede, il verbale dell'art. 492-bis e gli atti stragiudiziali previsti; non attribuisce una competenza nazionale indistinta per ogni accesso esecutivo. Per la consegna personale dell'art. 138 rileva la circoscrizione dell'ufficio. Nella richiesta si distinguono quindi luogo del destinatario, autorità cui appartiene l'affare e modalità scelta.

L'art. 137 c.p.c. coordina l'attività dell'UNEP con le notificazioni dell'avvocato: quando quest'ultimo è tenuto alla modalità telematica, il ricorso all'ufficiale giudiziario incontra le condizioni previste dalla norma, compresa la dichiarazione sull'impossibilità o sull'esito negativo non imputabile al destinatario. Non basta preferire lo sportello per eludere il canale obbligatorio.

### Consegna personale, destinatario assente e irreperibilità

**Art. 138: mani proprie.** La copia viene consegnata al destinatario di regola presso l'abitazione o, se non possibile, dove lo si trova nella circoscrizione. Se è proprio il destinatario a rifiutarla, il rifiuto è attestato nella relazione e la notificazione si considera fatta in mani proprie. Diverso è il rifiuto di una persona che potrebbe ricevere per lui.

**Art. 139: residenza, dimora o domicilio.** L'ufficiale cerca il destinatario nei luoghi previsti. Se non lo trova, la consegna può avvenire a persona di famiglia o addetta alla casa, all'ufficio o all'azienda, purché non minore di quattordici anni né palesemente incapace. In mancanza, segue il portiere; in mancanza anche di questo, il vicino che accetti. La successione non è a scelta libera. Per portiere o vicino la relazione indica anche come è stata accertata l'identità e occorre la raccomandata informativa.

| Regola | Presupposto | Adempimenti ed effetto |
|---|---|---|
| Art. 140 | Indirizzo individuato, ma impossibilità di consegna per assenza relativa, incapacità o rifiuto delle persone sostitutive. | Deposito nella casa comunale; avviso del deposito in busta chiusa e sigillata alla porta; raccomandata con avviso di ricevimento. |
| Art. 143 | Residenza, dimora e domicilio sconosciuti, dopo le ricerche pertinenti, senza procuratore ex art. 77. | Deposito nella casa comunale dell'ultima residenza o, se ignota, del luogo di nascita; se ignoti entrambi, consegna al PM. Perfezionamento nel ventesimo giorno successivo alle formalità. |

Per l'art. 140, la **Corte costituzionale n. 3/2010** stabilisce il perfezionamento per il destinatario con la ricezione della raccomandata informativa o, comunque, dopo dieci giorni dalla spedizione. La sola spedizione non fa decorrere immediatamente tutti i suoi termini. Per il notificante opera la scissione degli effetti: la consegna all'ufficiale giudiziario tutela la tempestività, subordinatamente al buon esito della notifica.

**Errore da evitare.** Una porta chiusa a un indirizzo noto non dimostra che residenza, dimora e domicilio siano sconosciuti. Non si passa all'art. 143 per abbreviare le formalità dell'art. 140. La relata descrive ricerche, informazioni raccolte e motivi della mancata consegna.

### Orari, ricevute e relata compilata

L'art. 147 pone per le notificazioni materiali la fascia **7–21**. Le notificazioni via PEC o servizio elettronico qualificato possono essere eseguite senza limiti orari: per il notificante rileva la ricevuta di accettazione, per il destinatario quella di consegna. Se quest'ultima è generata tra le 21 e le 7, il perfezionamento per il destinatario è alle 7. Questa regola delle notificazioni non si confonde con il deposito telematico del capitolo 12.

L'art. 148 richiede una relazione datata e sottoscritta, apposta all'originale e alla copia, con persona consegnataria, qualità e luogo oppure ricerche e ragioni della mancata consegna.

**Relata didattica fittizia — consegna a familiare.** Tutti i nomi, luoghi specifici e numeri seguenti sono inventati. Si assume che la notifica materiale sia consentita nel caso e che non vi sia obbligo telematico eluso.

| Campo | Relata compilata |
|---|---|
| Ufficio e richiesta | UNEP del Tribunale di Bologna; cronologico didattico 421/2026; richiesta dell'avv. Laura Riva per Alfa S.r.l. |
| Atto | Copia conforme dell'atto di citazione di Alfa S.r.l. contro Marco Neri. |
| Data, ora e luogo | 5 marzo 2026, ore 10:20, Bologna, via Esempio 18, abitazione del destinatario. |
| Ricerca ed esito | Cercato Marco Neri, non rinvenuto; presente Anna Neri, coniuge convivente, adulta e non palesemente incapace. |
| Consegna | Copia consegnata alla predetta familiare in busta chiusa e sigillata, recante il solo numero cronologico; osservate le cautele dell'art. 137. |
| Chiusura | Attestazione della consegna ex art. 139, data e sottoscrizione dell'ufficiale giudiziario nell'originale e nella copia. |

**Lettura dell'esempio.** Non si dichiara una consegna a mani proprie di Marco, perché ha ricevuto Anna. Non si inventa una raccomandata specifica per portiere o vicino quando il consegnatario è il familiare della diversa previsione del comma 2. Se Anna fosse minore di quattordici anni, l'esito indicato non sarebbe utilizzabile.

''' +t[at:]
t=t.replace("La pagina ministeriale richiama, tra le attività di esecuzione, sfratti, pignoramenti, sequestri, riconsegne di beni e offerte reali. In un concorso, questo elenco va trasformato in metodo.","Pignoramenti, rilascio e consegna perseguono l'attuazione coattiva di un diritto. Il sequestro ha la finalità propria del provvedimento che lo dispone. L'offerta reale, pur rientrando fra le attività dell'ufficiale giudiziario, appartiene invece al percorso di adempimento e di mora del creditore illustrato più avanti.")
t=t.replace('| Esecuzione | Lettura operativa |','| Attività | Lettura operativa |').replace('| Offerta reale | Attività formale collegata all\'adempimento offerto |','| Offerta reale | Adempimento offerto dal debitore e possibile mora del creditore; non espropriazione forzata. |')
at=t.index('### Pignoramenti e ricerca telematica dei beni')
end=t.index('### Rilascio, sfratto, sequestro e riconsegna',at)
t=t[:at]+'''### Titolo esecutivo e precetto

L'art. 474 richiede un **titolo esecutivo per un diritto certo, liquido ed esigibile**. Sono titoli le sentenze e gli altri provvedimenti o atti cui la legge attribuisce efficacia esecutiva; inoltre, nei rispettivi limiti, scritture private autenticate, cambiali e altri titoli di credito, atti ricevuti da notaio o pubblico ufficiale. Non qualsiasi documento che prova un credito consente l'esecuzione. Le scritture autenticate rilevano per le obbligazioni di somme di denaro; per consegna o rilascio valgono le categorie indicate dall'art. 474, terzo comma.

L'art. 475 richiede, nei casi previsti, **copia attestata conforme o duplicato informatico**. La tradizionale formula esecutiva non è più il requisito da cercare. Salvo diversa previsione, l'art. 479 impone la notificazione personale al debitore del titolo e del precetto, anche congiuntamente.

Il **precetto**, art. 480, intima di adempiere entro un termine non inferiore a dieci giorni e avverte che seguirà l'esecuzione. Deve contenere le indicazioni richieste: parti, titolo e sua notificazione se separata, eventuale trascrizione, giudice competente, domicilio o recapiti nei casi prescritti e avvertimenti di legge. È atto preparatorio: non coincide con il pignoramento e non determina da solo un vincolo su tutti i beni.

| Termine | Regola | Errore da evitare |
|---|---|---|
| Almeno dieci giorni | Artt. 480–482: attendere il termine intimato e comunque dieci giorni dalla notifica. | Iniziare dopo tre giorni perché il creditore dichiara urgenza. L'eccezione richiede autorizzazione giudiziale per pericolo nel ritardo. |
| Novanta giorni | Art. 481: il precetto diventa inefficace se l'esecuzione non inizia, salve sospensioni previste. | Confondere il termine con quello per chiedere la vendita dopo il pignoramento. |
| Quarantacinque giorni | Art. 497: il pignoramento perde efficacia se non è chiesta assegnazione o vendita nel termine. | Calcolare questi giorni dalla notificazione del precetto anziché dal pignoramento. |

### Tre forme di pignoramento

Il pignoramento vincola beni o crediti alla soddisfazione coattiva. L'art. 492 comprende l'ingiunzione di non sottrarli alla garanzia del credito, gli inviti su domicilio o recapito e gli avvertimenti sulla conversione e sulle opposizioni. La conversione consente di chiedere di sostituire i beni con una somma, alle condizioni di legge, fra cui il deposito iniziale non inferiore a un sesto dell'importo determinato dalla norma.

| Forma | Attività e documento | Successivo onere di iscrizione |
|---|---|---|
| Mobiliare presso il debitore | Ricerca nei luoghi consentiti, selezione di beni pignorabili, verbale con descrizione, stato, rappresentazione fotografica o audiovisiva, stima e conservazione; artt. 513–518. | Creditore: deposito degli atti entro quindici giorni dalla consegna, a pena di inefficacia, art. 518. |
| Presso terzi | Atto notificato a debitore e terzo, con intimazione al terzo di non disporre e invito alla dichiarazione entro dieci giorni; art. 543. | Deposito entro trenta giorni dalla consegna dell'atto. Avviso di iscrizione notificato al terzo entro l'udienza indicata e depositato, con conseguenze di inefficacia previste. |
| Immobiliare | Notificazione al debitore e trascrizione, con esatta individuazione di beni e diritti; art. 555. | Deposito entro quindici giorni dalla consegna dell'atto; nota di trascrizione nei termini dell'art. 557. |

I termini non hanno tutti lo stesso evento iniziale. Nel mobiliare, l'art. 514 sottrae al pignoramento beni essenziali nei limiti indicati: per esempio, letti, abiti, beni domestici indispensabili e animali da compagnia privi di finalità produttiva. Non si compila un verbale positivo soltanto perché nell'abitazione esistono oggetti. Nel presso terzi, la dichiarazione del terzo e l'assegnazione giudiziale sono passaggi diversi: il saldo comunicato dalla banca non è già una somma attribuita al creditore.

### Ricerca telematica dei beni: art. 492-bis

Nel percorso ordinario il creditore, munito di titolo e precetto e decorso il termine dell'art. 482, presenta istanza all'ufficiale giudiziario del tribunale del luogo in cui il debitore ha residenza, domicilio, dimora o sede. **Non serve sempre una preventiva autorizzazione del presidente del tribunale.** Quest'ultima è prevista per la ricerca anticipata, prima del precetto o prima della scadenza del termine, quando vi è pericolo nel ritardo.

L'ufficiale accede alle banche dati consentite, redige il verbale delle interrogazioni e dei risultati e ne dà comunicazione. La presentazione dell'istanza sospende il termine di novanta giorni del precetto fino agli esiti individuati dalla disposizione: comunicazione del verbale, mancata ricerca per difetto dei presupposti o rigetto nei casi previsti. Le date devono essere conservate e documentate.

La ricerca non equivale a pignoramento generalizzato né ad assegnazione automatica. Se emergono beni fuori dal territorio competente, la norma prevede il passaggio all'ufficiale territorialmente competente; se emergono crediti presso terzi, si seguono gli adempimenti specifici, proteggendo i dati non riferibili al singolo terzo.

### Opposizione all'esecuzione e agli atti

L'art. 615 riguarda il **diritto di procedere all'esecuzione** e, dopo l'inizio, anche la pignorabilità dei beni. L'art. 617 riguarda la **regolarità formale** degli atti e prevede il termine perentorio di venti giorni nei casi e dalle decorrenze indicate. Un pagamento già effettuato e un vizio della notificazione pongono quindi questioni differenti. La cancelleria o l'UNEP ricevono e trattano quanto di competenza, ma non decidono informalmente la controversia né sospendono ogni attività per la sola protesta del debitore.

''' +t[end:]
at=t.index('### Protesti')
t=t[:at]+'''Nel rilascio, l'**art. 608** fa iniziare l'esecuzione con la notificazione dell'avviso che comunica alla parte tenuta a rilasciare l'immobile giorno e ora dell'accesso, almeno dieci giorni prima. Titolo e precetto restano necessari nei casi previsti. Non si descrive l'accesso come conseguenza immediata della sola richiesta verbale del proprietario.

### Offerta reale: il debitore che vuole adempiere

L'offerta reale ha una direzione diversa dal pignoramento: è il debitore che offre la prestazione al creditore. Ai sensi degli artt. 1206–1209 c.c., il rifiuto senza motivo legittimo o la mancata cooperazione possono porre il creditore in mora. Servono requisiti precisi: soggetti capaci e legittimati, prestazione integrale con accessori dovuti, termine e condizione maturati, luogo e pubblico ufficiale competente.

L'offerta è reale per denaro, titoli di credito e cose mobili da consegnare al domicilio del creditore; per cose mobili da consegnare altrove opera l'intimazione prevista dall'art. 1209. Gli effetti della mora comprendono, alle condizioni dell'art. 1207, il rischio dell'impossibilità sopravvenuta non imputabile al debitore e le spese di custodia. **La sola offerta rifiutata non libera automaticamente dal debito**: il deposito accettato o dichiarato valido con sentenza passata in giudicato produce la liberazione secondo l'art. 1210.

**Esempio fittizio.** Il debitore offre l'intera somma scaduta con gli accessori prescritti, tramite pubblico ufficiale; il creditore rifiuta senza giustificazione. Il verbale documenta l'offerta e il rifiuto. Non si scrive «credito estinto» soltanto per questo: si distinguono mora del creditore e successivo percorso liberatorio.

''' +t[at:]
at=t.index('### Mappa BANDO del capitolo')
t=t[:at]+'''### Dossier svolto: calendario e verbale negativo

**Caso fittizio.** Una sentenza provvisoriamente esecutiva condanna Paolo Serra a pagare ad Alfa S.r.l. 4.000 euro. Titolo e precetto sono notificati personalmente il **3 marzo 2026**; il precetto intima dieci giorni. Non vi sono autorizzazioni urgenti, sospensioni o istanze ex art. 492-bis. L'accesso mobiliare è richiesto per il 16 marzo. Nel luogo indicato si trovano soltanto beni essenziali impignorabili; non emergono altri beni utilmente pignorabili né ulteriori indicazioni del debitore.

| Controllo | Soluzione |
|---|---|
| Termine iniziale | Escluso il 3 marzo, il decimo giorno è il 13 marzo. Il 16 è successivo al periodo minimo. |
| Novanta giorni | In assenza degli eventi sospensivi indicati, il novantesimo giorno dalla notifica è il 1° giugno 2026. Non sostituire questo termine con quello di quarantacinque giorni. |
| Esito dell'accesso | Non si vincolano i beni impignorabili per rendere artificiosamente positivo il verbale. Si documenta l'esito negativo. |
| Rischio residuo | Un accesso negativo non identifica da solo un bene vincolato: il creditore valuta il seguito processuale e l'efficacia del precetto. |

**Verbale didattico compilato.** Non è un modulo da utilizzare in un procedimento reale.

| Campo | Contenuto |
|---|---|
| Intestazione e parti | UNEP del Tribunale di Bologna, cronologico didattico 502/2026. Istante Alfa S.r.l., rappresentata dall'avv. Laura Riva; debitore Paolo Serra. |
| Documenti | Sentenza didattica 120/2026 del Tribunale di Bologna, copia conforme, e precetto notificati il 3 marzo; richiesta di accesso e riferimenti dei documenti allegati. |
| Accesso | 16 marzo 2026, dalle 10:00 alle 10:30, Bologna, via Esempio 25; presente il debitore, identificato tramite documento esibito, i cui estremi sono acquisiti nell'atto reale. |
| Operazioni | Ricercati beni nei luoghi consentiti; constatata la sola presenza di abiti, letti e dotazioni domestiche indispensabili del nucleo, senza beni di pregio esclusi dalla protezione. |
| Dichiarazioni | Invitato a indicare ulteriori beni utilmente pignorabili nei presupposti dell'art. 492, il debitore dichiara di non averne da indicare; dichiarazione riportata senza qualificarla come verifica universale del patrimonio. |
| Esito e chiusura | Nessun bene assoggettato a vincolo; esito negativo, restituzione degli atti e registrazione. Data e sottoscrizione dell'ufficiale; sottoscrizione della dichiarazione del debitore, con attestazione di eventuale rifiuto nell'atto reale. |

**Consegna, 20 minuti.** Ricostruisci il calendario, indica due controlli sul titolo e spiega perché il verbale non può elencare come pignorati i soli beni essenziali. **Griglia, 12 punti:** calendario10/90 (4); titolo esecutivo e corretta forma/notifica (4); impignorabilità ed esito documentato senza attribuire al verbale una ricerca patrimoniale completa (4).

''' +t[at:]
# Four columns, keeping all five-column content.
lines=t.splitlines();out=[];active=False
for line in lines:
 if line.startswith('| Richiesta | Atto o presupposto | Soggetto richiedente | Controllo UNEP | Esito |'):active=True;out.append('| Richiesta e richiedente | Atto o presupposto | Controllo UNEP | Esito |');continue
 if active and line.startswith('|'):
  c=[x.strip() for x in line.strip('|').split('|')]
  if len(c)==5:out.append('| '+' | '.join(['---']*4 if all(set(x)<=set('-: ') for x in c) else [c[0]+' — '+c[2],c[1],c[3],c[4]])+' |');continue
 if not line.startswith('|'):active=False
 out.append(line)
t='\n'.join(out)+'\n';i=t.index('### Quiz commentato');j=t.index('### Checklist di ripasso',i)
t=t[:i]+'''### Quiz commentati

1. **Il destinatario personalmente rifiuta la copia ex art. 138. Qual è l'effetto?**
   - A. Occorre sempre l'art. 143.
   - B. La notifica diventa inesistente.
   - C. Si consegna obbligatoriamente al vicino.
   - D. Il rifiuto attestato vale come notifica in mani proprie.
   **Risposta corretta: D.** Non si confonde il rifiuto personale con quello dei consegnatari sostitutivi.

2. **L'indirizzo è noto, ma il destinatario è temporaneamente assente e nessun soggetto idoneo riceve. Quale percorso va valutato?**
   - A. Art. 140, con le sue formalità e il perfezionamento coordinato con Corte cost. 3/2010.
   - B. Sempre art. 143 per residenza sconosciuta.
   - C. Semplice telefonata sostitutiva.
   - D. Eliminazione della raccomandata perché la porta è chiusa.
   **Risposta corretta: A.** L'assenza relativa non prova l'ignoranza di residenza, dimora e domicilio.

3. **Titolo e precetto notificati il 3 marzo 2026, termine di dieci giorni, senza urgenza. Il 6 marzo si può iniziare ordinariamente l'esecuzione?**
   - A. Sì, basta la richiesta del creditore.
   - B. Sì, perché il precetto è già un pignoramento.
   - C. No, il periodo minimo termina il 13 marzo.
   - D. No, occorre sempre attendere novanta giorni.
   **Risposta corretta: C.** Dieci giorni è il periodo minimo; novanta è il limite di efficacia del precetto, non un'attesa obbligatoria.

4. **Nella ricerca ordinaria ex art. 492-bis, con titolo, precetto e termine già decorso, occorre sempre l'autorizzazione del presidente?**
   - A. Sì, senza eccezioni.
   - B. No: la richiesta ordinaria è all'ufficiale competente; l'autorizzazione riguarda l'anticipazione urgente prevista.
   - C. No, perché può interrogare le banche dati direttamente qualsiasi creditore.
   - D. Sì, ma solo se si trovano rapporti bancari.
   **Risposta corretta: B.** Si distinguono percorso ordinario e ricerca prima del precetto o del termine dell'art. 482.

5. **La copia conforme o il duplicato informatico dell'art. 475 sostituiscono la verifica dell'efficacia esecutiva?**
   - A. Sì, ogni documento duplicato è titolo.
   - B. Sì, salvo i documenti in formato PDF.
   - C. No, occorre ancora la tradizionale formula esecutiva in ogni caso.
   - D. No: forma documentale e qualità di titolo ex art. 474 sono controlli distinti.
   **Risposta corretta: D.** L'abolizione della formula non rende esecutivo un atto che non lo è.

6. **Il creditore rifiuta un'offerta reale. Il solo verbale libera automaticamente il debitore?**
   - A. No: mora del creditore e deposito con effetti liberatori hanno presupposti distinti.
   - B. Sì, ogni rifiuto cancella il credito.
   - C. Sì, perché l'offerta è un'espropriazione.
   - D. No, perché l'ufficiale giudiziario non può mai partecipare all'offerta.
   **Risposta corretta: A.** Gli artt. 1206–1210 distinguono offerta, mora e deposito accettato o validato con gli effetti previsti.

''' +t[j:]
s='sources/vol-04-unep-verifica-2026-10-03.md';t=t.replace('source_refs: [','source_refs: [\n  "'+s+'",',1).replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/'+s+'",',1)
t=re.sub(r'updated_at: .*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true',1).replace('status: reviewed','status: revised_draft',1).replace('draft_stage: reviewed','draft_stage: editorial-revision',1)
assert datetime.date(2026,3,3)+datetime.timedelta(days=10)==datetime.date(2026,3,13)
assert datetime.date(2026,3,3)+datetime.timedelta(days=90)==datetime.date(2026,6,1)
p.write_text(t,'utf-8');result={'file':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(t.split()),'quizKeys':re.findall(r'Risposta corretta: ([A-D])',t),'source':s,'textApplied':True,'calendarVerified':True,'pdfVerified':False};(A/'VOL-04-unep-delta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf-8');print(json.dumps(result,ensure_ascii=False))
