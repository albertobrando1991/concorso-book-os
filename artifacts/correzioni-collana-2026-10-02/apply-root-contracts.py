import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-impiego-contabilita-contratti-correzioni-2026-10-03.md';u.REF=ref
s='contratti-pubblici-essenziali';t=u.read(s)
t=u.replace(t,'Il RUP presidia il ciclo del contratto secondo la disciplina applicabile.', 'Il RUP è nominato nel **primo atto di avvio dell’intervento pubblico** da realizzare mediante contratto, ai sensi dell’art. 15. La nomina non è una formalità rinviata dopo la programmazione. Il RUP presidia il ciclo del contratto secondo la disciplina applicabile.')
anchor='### 7. Schema dal fabbisogno all’esecuzione'
t=u.replace(t,anchor,'''**Dati essenziali dell’art. 37:** i programmi di lavori e di acquisti di beni e servizi sono **triennali**, con aggiornamenti annuali. Vi rientrano, rispettivamente, lavori di importo stimato **almeno 150.000 euro** e acquisti di beni e servizi **almeno 140.000 euro**. Il mancato superamento di queste soglie non elimina la verifica di fabbisogno e copertura.

L’art. 41 articola la progettazione dei lavori in **progetto di fattibilità tecnico-economica (PFTE)** e **progetto esecutivo**. Non ripetere i tre livelli del precedente Codice come regola attuale. Per servizi e forniture opera un unico livello. Per alcune manutenzioni sono previste semplificazioni: il comma 5 consente l’omissione del primo livello alle condizioni indicate; il comma 5-bis ammette determinate manutenzioni sulla base del PFTE minimo previsto, escludendo i casi strutturali o impiantistici lì individuati. La verifica concreta deve quindi partire dall’intervento.

'''+anchor)
t=u.replace(t,'Nel libro base non conviene memorizzare numeri destinati a cambiare; conviene capire la funzione delle procedure.', 'Per scegliere il percorso servono sia la funzione delle procedure sia i valori vigenti: usa la tabella datata della sezione seguente.')
a=t.index('Nel manuale base è preferibile non costruire lo studio su valori numerici,');b=t.index('\n![Figura 9.3',a)
t=t[:a]+'''#### Soglie da usare negli esercizi: quadro 2026–2027

Le cifre seguenti sono **al netto dell’IVA**. Per stimare il valore si considerano l’intero contratto e le opzioni o i rinnovi previsti, secondo l’art. 14; è vietato frazionare artificiosamente per eludere le regole. Le soglie UE operano a partire dall’importo indicato, non soltanto oltre.

| Settori ordinari: soglia UE | Importo |
|---|---:|
| Lavori | 5.404.000 euro |
| Servizi e forniture delle autorità governative centrali | 140.000 euro |
| Servizi e forniture delle amministrazioni subcentrali, come un Comune | 216.000 euro |
| Servizi sociali e altri servizi specifici dell’allegato XIV alla direttiva 2014/24/UE | 750.000 euro |

I primi tre valori derivano dal regolamento delegato UE 2025/2152, applicabile dal 1° gennaio 2026; per i servizi specifici vale la distinta soglia dell’art. 14. Settori speciali, concessioni e fattispecie particolari richiedono il proprio regime: non trasportare automaticamente questa tabella a ogni contratto pubblico.

| Art. 50: fascia sotto soglia UE | Modalità essenziale |
|---|---|
| Lavori inferiori a 150.000 euro | Affidamento diretto, anche senza consultare più operatori. |
| Servizi e forniture inferiori a 140.000 euro | Affidamento diretto, anche senza consultare più operatori. |
| Lavori da 150.000 a meno di 1 milione | Negoziata senza bando con almeno 5 operatori, ove esistenti. |
| Lavori da 1 milione alla soglia UE esclusa | Negoziata con almeno 10 operatori, ove esistenti; resta l’alternativa ordinaria prevista dalla norma. |
| Servizi e forniture da 140.000 alla pertinente soglia UE esclusa | Negoziata con almeno 5 operatori, ove esistenti. |

**Due trappole:** a 150.000 euro esatti un lavoro non rientra nel diretto della lettera a; per servizi di un’autorità centrale la soglia UE 2026 è già 140.000, quindi non esiste la fascia intermedia ordinaria che può invece esserci per un Comune. Restano interesse transfrontaliero certo, qualificazione della stazione appaltante, disciplina dell’oggetto, rotazione e altri presupposti. L’art. 48, comma 2, impone il percorso ordinario quando ricorre l’interesse transfrontaliero certo: il solo importo non basta.

**Prova rapida:** fornitura ordinaria comunale di 139.000 euro, nessuna opzione e nessun interesse transfrontaliero certo: il diretto è astrattamente ammesso. A 150.000 euro, nelle stesse condizioni, si entra nella fascia della negoziata sotto soglia con almeno cinque operatori ove esistenti. In entrambi i casi vanno verificati obblighi di acquisto, requisiti e copertura. Per il concorso successivo al periodo indicato aggiorna i valori sulla fonte, conservando la distinzione tra soglia UE e soglia del diretto.
''' +t[b:]
anchor='La logica è bilanciare due esigenze: evitare esclusioni inutilmente formalistiche e proteggere parità di trattamento, concorrenza e serietà dell’offerta.'
t=u.replace(t,anchor,anchor+'''

| Istituto dell’art. 101 | Termine e confine |
|---|---|
| Soccorso documentale, comma 1 | Da 5 a 10 giorni per integrazioni o regolarizzazioni ammesse, ferme le condizioni sul fascicolo virtuale. Non sana l’offerta tecnica/economica né l’assoluta incertezza sull’identità del concorrente. |
| Chiarimenti sull’offerta, comma 3 | Da 5 a 10 giorni; spiegano il contenuto, senza modificarlo. |
| Rettifica, comma 4 | L’operatore può richiederla fino al giorno fissato per l’apertura delle offerte, per errore materiale scoperto dopo la scadenza di presentazione, preservando anonimato e assenza di nuova offerta o modifica sostanziale. |

La mancata risposta al soccorso nel termine assegnato comporta esclusione. Garanzia provvisoria, contratto di avvalimento e impegno al mandato del raggruppamento non ancora costituito sono sanabili nei limiti indicati dalla norma con documenti aventi data certa anteriore alla scadenza: non si creano dopo requisiti o accordi che dovevano già esistere.

**Caso:** dopo la scadenza, l’operatore propone un prezzo diverso per diventare più competitivo. Non è un chiarimento né una rettifica materiale ammissibile. Un errore materiale riconoscibile segue invece il comma 4, con tutti i suoi limiti: non basta chiamarlo “refuso”.''')
t=u.replace(t,'| Trattativa diretta | Negoziazione con uno o più operatori nei casi consentiti. |','| Trattativa diretta | Negoziazione con un unico operatore economico. |\n| Confronto di preventivi | Strumento distinto per acquisire preventivi da più operatori. |')
t=u.replace(t,'Il portale non sostituisce il Codice.', 'Trattativa diretta, confronto di preventivi e altre RdO sono modalità della piattaforma; la loro denominazione non determina da sola la procedura giuridica. Il portale non sostituisce il Codice.')
a=t.index('Un Comune deve acquistare un servizio informatico');b=t.index('\n## Domanda da commissario',a)
t=t[:a]+'''**Dossier didattico:** un Comune deve acquistare un servizio informatico di prenotazione degli sportelli per **80.000 euro al netto IVA**, valore complessivo senza opzioni o rinnovi. Il fabbisogno è definito, lo stanziamento disponibile, non emerge interesse transfrontaliero certo e il fornitore considerato non è il contraente uscente. La verifica preliminare del dossier esclude una convenzione obbligatoria applicabile; il servizio è acquistabile sul MePA. L’ufficio propone di “scegliere il fornitore conosciuto, perché è rapido”.

**Soluzione ragionata.** La stazione appaltante nomina il RUP nel primo atto di avvio. Individua durata, prestazioni, livelli di servizio, protezione dati e assistenza; verifica copertura e obblighi di acquisto. L’importo è sotto 140.000 euro: ricorrono, nelle ipotesi date, le condizioni quantitative del diretto ai sensi dell’art. 50, comma 1, lettera b. Non è obbligatorio acquisire tre preventivi per il solo fatto di procedere in via diretta, ma la scelta deve essere motivata e la congruità valutata.

L’atto dell’art. 17, comma 2, indica oggetto, importo, contraente, ragioni della scelta e requisiti; l’essere “conosciuto” non sostituisce esperienza documentata e controlli. La trattativa diretta sul MePA si svolge con **un operatore**. Seguono adempimenti digitali, CIG, tracciabilità, stipula ed esecuzione; liquidazione e pagamento richiedono la verifica della prestazione.

**Variante:** se il valore fosse 150.000 euro, la stessa lettera b non consentirebbe il diretto. Per un servizio ordinario comunale sotto la soglia UE di 216.000 euro, il percorso dell’art. 50, comma 1, lettera e, prevede almeno cinque operatori ove esistenti, con le ulteriori condizioni applicabili. Il dato cambiato modifica la soluzione: non basta ricopiare il modello precedente.
''' +t[b:]
u.save(s,t,['V01-22','V01-23','V01-24'],ref)
u.record()
