from pathlib import Path
import importlib.util,re
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-programmazione-sottosoglia-verifica-2026-10-03.md'
slug='03-strategia-fabbisogni-programmazione';t=u.read(slug)
anchor='Programmare priorità, risorse e responsabilità\n'
t=u.replace(t,anchor,'''### Valore stimato e lotti: prima il calcolo, poi la procedura

Ai sensi dell’art. 14, il valore stimato considera l’importo massimo pagabile, **IVA esclusa**, con opzioni, rinnovi e premi previsti. Per lavori comprende le forniture e i servizi messi a disposizione dall’amministrazione e necessari all’esecuzione. La stima si colloca all’avvio della procedura e non si riduce al prezzo della prima annualità. Per prestazioni regolari o rinnovabili occorre considerare l’aggregazione prevista dal comma 12; una serie di acquisti mensili non diventa una serie di bisogni indipendenti per il solo fatto di avere fatture diverse.

**Esempio.** Un Comune prevede assistenza per 24 mesi a 6.000 euro mensili, un rinnovo opzionale di 12 mesi alle stesse condizioni e una migrazione opzionale da 18.000 euro. Valore: 24 × 6.000 + 12 × 6.000 + 18.000 = **234.000 euro**, IVA esclusa. La base iniziale di 144.000 euro non è il valore complessivo. Il totale supera la soglia UE subcentrale 2026–2027 di 216.000 euro: non si sceglie la negoziata sotto soglia guardando soltanto al periodo iniziale. La disponibilità di bilancio e il valore per scegliere il regime sono controlli collegati ma distinti.

L’art. 58 pone la **suddivisione in lotti** a tutela dell’effettiva partecipazione delle micro, piccole e medie imprese. I lotti possono essere funzionali, prestazionali o quantitativi. La mancata suddivisione deve essere motivata nel bando o avviso; non basta scrivere “per esigenze dell’ente”. Anche dimensione e criteri di suddivisione devono essere spiegabili. Sono vietati sia il frazionamento per eludere le regole sia l’accorpamento artificioso che ostacola la partecipazione.

Se il servizio dell’esempio viene articolato in lotti distinti da 144.000, 72.000 e 18.000 euro, l’art. 14 impone di considerarne in via generale il valore complessivo per il regime UE. Il comma 11 consente una specifica deroga per piccoli lotti: ciascuno sotto 80.000 euro per servizi/forniture o sotto 1 milione per lavori, e somma dei lotti in deroga non oltre il 20% del totale. Qui il tetto è 46.800 euro: il lotto da 18.000 può rientrarvi, quello da 72.000 no, anche se singolarmente inferiore a 80.000. La deroga va motivata e non rende fittiziamente autonomo l’intero fabbisogno.

**Motivazione ragionata di un lotto unico.** Il Comune acquisisce un sistema di allarme con componenti che devono garantire una prestazione unitaria certificata. L’istruttoria documenta che la separazione proposta impedirebbe l’attribuzione delle responsabilità sulle interfacce e non garantirebbe l’accettazione del sistema completo; confronta anche una soluzione con lotti e coordinamento tecnico, risultata inadeguata per quelle specifiche interfacce. Nel bando motiva il lotto unico sulla base di tali dati e mantiene requisiti proporzionati, forme di partecipazione aggregata e accesso delle PMI. “Un solo fornitore è più comodo” non sarebbe sufficiente.

''' + anchor)
old='Nel Codice dei contratti pubblici la programmazione ha una disciplina specifica, da verificare nel testo vigente e negli allegati applicabili. Per il candidato, però, il ragionamento resta stabile: prima si decide se il fabbisogno è maturo, poi lo si colloca nel programma, poi si prepara la progettazione della procedura.'
t=u.replace(t,old,'''L’art. 37 richiede due programmi **triennali**, aggiornati annualmente: lavori di importo stimato pari o superiore a **150.000 euro**, acquisti di beni e servizi pari o superiori a **140.000 euro**. La parità al limite determina l’inserimento. I programmi devono essere coerenti con documenti programmatori e bilancio; per gli enti locali si raccordano con la programmazione economico-finanziaria. Il ricorso a una centrale qualificata non trasferisce a questa il compito di programmare il bisogno dell’amministrazione delegante.

Per lavori almeno pari alla soglia UE, l’inserimento triennale richiede il documento di fattibilità delle alternative progettuali (DOCFAP) approvato; quello nell’elenco annuale richiede il documento di indirizzo della progettazione (DIP). La manutenzione ordinaria sopra soglia può entrare nel triennale senza DOCFAP. Nell’annuale vanno comunque verificate copertura, avvio della procedura nell’anno, livello progettuale richiesto e conformità urbanistica. Lavori, servizi e forniture realizzati in amministrazione diretta non si inseriscono in questa programmazione.

L’allegato I.5 distingue gli schemi: per lavori **A** risorse, **B** opere incompiute, **C** immobili, **D** elenco triennale, **E** annuale, **F** interventi non riproposti; per beni/servizi **G** risorse, **H** acquisti, **I** acquisti non riproposti. Il **CUI**, codice unico di intervento, identifica lavoro o acquisto; non è il CIG della procedura né il CUP del progetto d’investimento. CUI e CUP, ove previsto, si mantengono nella riproposizione salvo modifiche sostanziali che mutino l’identità dell’intervento.

**Scheda H, estratto didattico compilato.** Un Comune programma il servizio informatico dell’esempio; dispone di copertura secondo il prospetto economico e avvia la gara nel 2026. I dati seguenti illustrano la riga e i suoi controlli: non sono un codice o un affidamento reale.

| Campo | Valore del caso |
| --- | --- |
| CUI | S00000000000202600001, codice esemplificativo non operativo |
| Oggetto e durata | Assistenza applicativa 24 mesi, rinnovo opzionale 12 mesi, migrazione opzionale |
| Avvio procedura | 2026 |
| Valore massimo stimato | 234.000 euro, IVA esclusa |
| Quadro delle risorse | Prospetto economico e copertura comprensivi degli oneri previsti; non confondere il netto per la soglia con la spesa complessiva |
| Priorità | Media nell’esempio, motivata da continuità applicativa e scadenza del contratto in corso |
| RUP | Funzionario designato nel primo atto, con requisiti e supporto tecnico adeguati |
| Ricorso a centrale | Sì: Comune non qualificato, procedura sopra soglia UE |
| CUP | Non previsto nell’ipotesi di servizio gestionale privo di autonomo progetto d’investimento; rivalutare se cambiano i fatti |

Ogni anno il programma scorre: un acquisto la cui procedura è già avviata non viene riproposto come nuovo. Le modifiche nel corso dell’anno richiedono approvazione competente nei casi dell’allegato I.5, per esempio risorse imprevedibili sopravvenute, anticipazione di un acquisto, cancellazione o variazione del quadro economico. Le eccezioni per eventi imprevedibili o nuove disposizioni non giustificano ordinariamente una programmazione omessa. Programmi e aggiornamenti sono pubblicati sul sito istituzionale e trasmessi alla BDNCP secondo la disciplina applicabile.''')
u.save(slug,t,['V09-09','V09-10'],u.REF)
slug='05-sotto-soglia-procurement-operativo';t=u.read(slug)
t=u.replace(t,'Significa che il contratto resta sotto le soglie di rilevanza europea o sotto altri limiti previsti dalla disciplina vigente, e che l\'amministrazione può usare percorsi più semplici rispetto alle procedure ordinarie.','Significa che il valore stimato del contratto è inferiore alla pertinente soglia di rilevanza europea. I limiti nazionali interni selezionano poi le procedure: “sotto soglia UE” e “affidabile direttamente” non sono sinonimi.')
old='Questo capitolo non riporta importi fissi, termini mobili o istruzioni tecniche di piattaforma. In materia di contratti pubblici questi dati cambiano e devono essere controllati al momento dell\'uso, nel Codice dei contratti pubblici vigente, negli atti ANAC applicabili, nelle regole dell\'ente, nelle piattaforme istituzionali e, quando rileva, nella disciplina speciale collegata a fondi europei o PNRR.'
t=u.replace(t,old,'Il quadro seguente è verificato al 3 ottobre 2026 e riguarda i settori ordinari. Le soglie UE 2026–2027 derivano dal regolamento delegato (UE) 2025/2152; le soglie nazionali delle procedure discendono dall’art. 50 del Codice. Leggi prima il valore complessivo secondo il capitolo 3, poi scegli il regime.')
anchor='### Mappa BANDO della procedura sotto soglia'
t=u.replace(t,anchor,'''### Soglie e procedura nel biennio 2026–2027

Per lavori ordinari la soglia UE è **5.404.000 euro**; per servizi e forniture ordinarie è **140.000 euro** per autorità governative centrali e **216.000 euro** per amministrazioni subcentrali. Per i servizi sociali e assimilati dell’allegato XIV la soglia specifica è 750.000 euro: non applicare a essi senza verifica la colonna dei servizi ordinari. Importi IVA esclusa; opzioni e rinnovi si computano. Al raggiungimento della soglia il contratto non è più sotto soglia.

| Oggetto e valore stimato | Regola dell’art. 50 |
| --- | --- |
| Lavori sotto 150.000 euro | Affidamento diretto, anche senza confronto tra più operatori, a soggetto con esperienze documentate idonee |
| Lavori da 150.000 a meno di 1 milione | Negoziata senza bando, almeno 5 operatori ove esistenti |
| Lavori da 1 milione a meno di 5.404.000 | Negoziata senza bando, almeno 10 operatori ove esistenti; resta prevista la possibilità di procedura ordinaria |
| Servizi/forniture sotto 140.000 euro | Affidamento diretto con esperienze documentate idonee |
| Servizi/forniture da 140.000 alla pertinente soglia UE, esclusa | Negoziata senza bando, almeno 5 operatori ove esistenti |

Per un Ministero, nella categoria ordinaria con soglia UE di 140.000 euro, l’ultima fascia non ha ampiezza: a 140.000 euro si applica già il regime europeo. Per un Comune, un servizio da 180.000 euro rientra invece nella fascia negoziata. La capacità di svolgere autonomamente la procedura va controllata secondo il capitolo 2; un valore sotto UE non rende qualsiasi ente automaticamente qualificato.

L’art. 48, comma 2, impone le procedure ordinarie se è accertato un **interesse transfrontaliero certo**, anche sotto soglia. La stazione deve motivare sulla base di elementi del contratto e del mercato, quali oggetto, caratteristiche tecniche, valore e localizzazione; non basta affermare che qualsiasi sito sia visibile dall’estero. Restano fermi gli obblighi di acquisto centralizzato.

Nella negoziata il numero minimo riguarda gli operatori da consultare, ove esistenti, non un obbligo di ricevere quel numero di offerte. Indagini ed elenchi seguono l’allegato II.1. Il sorteggio per selezionare gli invitati non è il metodo ordinario: è ammesso solo nei casi particolari motivati previsti dall’art. 50, comma 2, quando nessun altro metodo risulti praticabile. Sono previsti pubblicazione dell’avvio della consultazione, adempimenti sui soggetti consultati e avviso dell’esito. Il prezzo più basso non si sceglie quando ricorre una fattispecie che impone l’offerta qualità/prezzo ai sensi dell’art. 108, comma 2.

''' + anchor)
anchor='### Motivazione, rotazione e consultazione del mercato'
t=u.replace(t,anchor,'''### Tre casi di confine

**Lavori da 149.000 e da 150.000 euro.** Nel primo caso è ammesso l’affidamento diretto; nel secondo si entra nella negoziata con almeno cinque operatori ove esistenti. Le ipotesi assumono assenza di interesse transfrontaliero certo e di altre discipline speciali. Spezzare un intervento unitario in due ordini da 75.000 euro per restare nel diretto violerebbe il divieto di frazionamento elusivo.

**Servizio comunale da 130.000 euro più rinnovo da 40.000.** Valore 170.000 euro: non affidamento diretto. Il rinnovo è un’opzione prevista, quindi entra nel massimo stimato anche se l’ente potrà non esercitarlo. Si applica la fascia negoziata, insieme al controllo di qualificazione e degli strumenti obbligatori.

**Un’unica offerta ricevuta dopo cinque inviti regolari.** La sola presenza di un’offerta non dimostra che gli inviti fossero insufficienti. Occorre verificare la corretta consultazione, le condizioni della procedura, la validità e congruità dell’offerta e i requisiti. Non si deve simulare un numero di offerte che il mercato non ha presentato.

''' + anchor)
anchor='La rotazione serve a evitare'
start=t.index(anchor);end=t.index('\n\n',start)
t=t[:start]+'''La rotazione dell’art. 49 impedisce, in via ordinaria, due affidamenti consecutivi al contraente uscente nello stesso settore merceologico, categoria di opere o settore di servizi. L’ente può organizzare fasce di valore, applicando il divieto all’interno della fascia, senza creare fasce artificiose per eluderlo.

| Ipotesi | Regola ed evidenza |
| --- | --- |
| Deroga motivata, comma 4 | Struttura del mercato ed effettiva assenza di alternative, con previa verifica dell’esecuzione accurata e della qualità della prestazione precedente. I presupposti vanno documentati insieme. |
| Negoziata art. 50, lettere c), d), e), comma 5 | Rotazione non applicata se l’indagine non limita il numero degli operatori aventi requisiti da invitare. Pubblicare un avviso aperto e poi selezionare soltanto cinque candidati non realizza questa condizione. |
| Affidamento diretto sotto 5.000 euro, comma 6 | È consentita la deroga alla rotazione. A 5.000 euro esatti questa eccezione non opera; restano motivazione, requisiti e gli altri obblighi. |

**Caso:** servizio da 35.000 euro, stesso settore e fascia del precedente, tre operatori alternativi idonei. L’uscente ha lavorato bene e costa leggermente meno. La sola qualità pregressa non soddisfa il comma 4, perché manca l’effettiva assenza di alternative: non basta per riaffidargli il servizio. Per un acquisto realmente distinto da 4.800 euro la deroga del comma 6 è invece utilizzabile, senza frazionare un bisogno unitario.''' +t[end:]
anchor='I controlli sui requisiti vanno distinti dalle dichiarazioni.'
t=u.replace(t,anchor,'''**Controlli negli affidamenti diretti sotto 40.000 euro.** L’art. 52 consente all’operatore di attestare i requisiti con dichiarazione sostitutiva di atto di notorietà. La stazione verifica le dichiarazioni, anche mediante un campione scelto con modalità predeterminate annualmente. Non significa “requisiti non richiesti”: cambia il sistema di controllo. A 40.000 euro esatti non si applica la semplificazione riservata agli importi inferiori.

Se il controllo non conferma i requisiti dichiarati, la stazione risolve il contratto, escute l’eventuale garanzia definitiva, comunica ad ANAC e sospende l’operatore dalle proprie procedure da uno a dodici mesi. Durata ed effetti devono risultare dal provvedimento: non è una cancellazione universale automatica da ogni gara pubblica.

''' + anchor)
u.save(slug,t,['V09-14','V09-15'],u.REF);u.record()
