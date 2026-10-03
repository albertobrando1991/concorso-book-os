import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-procedimento-correzioni-2026-10-03.md';u.REF=ref
for topic in ['procedimento-amministrativo','diritto-amministrativo','casi-pratici']:
 p=Path('wiki/topics')/(topic+'.md')
 with p.open('a',encoding='utf8') as out:out.write('\n\n## Procedimento: consolidamento del 3 ottobre 2026\n\n[[sources/vol-01-procedimento-correzioni-2026-10-03]] verifica termini conferenza30/60 dopo DL19/L50 del2026, distingue SCIA, motivazione, invalidità e revoca. Il raw storico della L241 contiene un indice e non prova lettura integrale degli articoli; riscontri sostanziali e limiti sono nella nuova nota.\n')
s='diritto-amministrativo-per-candidati';t=u.read(s)
t=u.replace(t,'La concessione di servizi si distingue perché il gestore assume un ruolo nella gestione del servizio verso l’utenza.', 'Nella concessione di servizi il criterio distintivo rispetto all’appalto è il trasferimento al concessionario del rischio operativo legato alla gestione, secondo il Codice dei contratti. Il contatto con gli utenti, da solo, non basta: anche un appaltatore può erogare un servizio al pubblico.')
t=u.replace(t,'Gli elementi essenziali da considerare sono soggetto competente, oggetto, contenuto, forma quando richiesta, motivazione, finalità pubblica e collegamento con il procedimento. La motivazione è decisiva: spiega il percorso logico e giuridico che collega istruttoria, interesse pubblico e decisione finale.', '''Separa la struttura dell’atto dalle condizioni della sua legittimità. La struttura comprende il soggetto cui l’atto è imputabile, l’oggetto, il contenuto dispositivo e la forma quando essenziale; la mancanza di un elemento essenziale può rilevare ai sensi dell’art. 21-septies. Competenza, procedimento, istruttoria, motivazione e corretto esercizio del potere vanno poi controllati secondo le rispettive norme. Non ogni loro difetto produce nullità.

La **motivazione**, ai sensi dell’art. 3, espone i presupposti di fatto e le ragioni giuridiche della decisione in rapporto all’istruttoria. Se richiama un altro atto, questo deve essere indicato e reso disponibile secondo la regola sulla motivazione per rinvio. L’art. 3, comma 2, esclude l’obbligo generale per atti normativi e atti a contenuto generale, ferme le discipline specifiche applicabili.

**Esempio:** un diniego individuale privo delle ragioni richieste non diventa automaticamente nullo; il difetto si valuta come vizio di legittimità, normalmente nell’ambito dell’annullabilità. Un atto adottato senza alcuna attribuzione del potere pone invece il diverso problema della nullità per difetto assoluto di attribuzione. Non confonderlo con la semplice incompetenza relativa fra organi della stessa amministrazione.''')
t=u.replace(t,'## 4. Responsabile del procedimento','''### Termini: regola, ambito ed eccezione

Prima di calcolare una scadenza individua la fonte che disciplina quel procedimento. L’art. 2 della legge 241/1990 non assegna indistintamente trenta giorni a ogni pratica di qualsiasi ente.

| Regola | Ambito e limite |
|---|---|
| 30 giorni residuali | Procedimenti di amministrazioni statali ed enti pubblici nazionali quando manca un diverso termine previsto dalle fonti indicate nell’art. 2. |
| Termini fino a 90 giorni | Individuati nei modi dei commi 3 e 5; non sono una proroga che il singolo ufficio decide liberamente. |
| Termini superiori a 90 e fino a 180 | Nei casi e con il procedimento del comma 4; restano le esclusioni per cittadinanza e immigrazione. |
| Decorrenza | Dall’avvio d’ufficio o dal ricevimento della domanda nei procedimenti a iniziativa di parte. |
| Sospensione istruttoria | Una sola volta, fino a 30 giorni, alle condizioni dell’art. 2, comma 7; non per acquisire ciò che l’ufficio possiede o può ottenere direttamente da altre PA. |

Per Regioni, enti locali e discipline settoriali occorre coordinare legge statale, ordinamento e termine specificamente applicabile. **Sospendere** ferma il conteggio e lascia il residuo; **interrompere**, quando una norma lo prevede, fa ripartire un nuovo termine: non sono sinonimi.

**Caso svolto:** il dossier assegna a una procedura un termine di 30 giorni. Sono trascorsi 12 giorni quando una sospensione legittima di 8 giorni ferma il conteggio. Alla ripresa restano **18 giorni**, non altri 30; in assenza di ulteriori eventi il tempo totale trascorso sarà 38 giorni. Il caso isola il calcolo: non autorizza sospensioni prive dei presupposti di legge.

## 4. Responsabile del procedimento''')
t=u.replace(t,'L’autotutela non è libertà illimitata.', '''### Quando il vizio non conduce all’annullamento

L’art. 21-octies, comma 2, distingue due ipotesi. Per un provvedimento **vincolato**, la violazione di norme sulla forma o sul procedimento non conduce all’annullamento se è palese che il contenuto dispositivo non avrebbe potuto essere diverso. Per la **mancata comunicazione di avvio**, spetta all’amministrazione dimostrare in giudizio che il contenuto non avrebbe potuto cambiare. Questa seconda regola non si applica alla violazione del preavviso di rigetto dell’art. 10-bis.

Non è un’autorizzazione a ignorare le garanzie. Occorre qualificare il vizio, l’attività e l’incidenza sul contenuto; un’istruttoria incompleta o una scelta discrezionale non diventano automaticamente irrilevanti perché l’ufficio dichiara che avrebbe deciso allo stesso modo.

### Revoca e indennizzo

La revoca dell’art. 21-quinquies riguarda il provvedimento a efficacia durevole: può fondarsi su sopravvenuti motivi di interesse pubblico, su un mutamento dei fatti non prevedibile all’adozione oppure, nei limiti di legge, su una nuova valutazione dell’interesse pubblico originario. Quest’ultima ragione non è ammessa per autorizzazioni e attribuzioni di vantaggi economici. La revoca impedisce ulteriori effetti; non presuppone l’illegittimità originaria propria dell’annullamento.

Se la revoca danneggia i soggetti direttamente interessati, sorge l’obbligo di indennizzo. Quando incide su rapporti negoziali, il comma 1-bis limita l’indennizzo al danno emergente e impone le valutazioni ulteriori indicate dalla norma. Indennizzo per un sacrificio conseguente a un atto legittimo e risarcimento da illecito hanno presupposti differenti: non promettere automaticamente tutti i guadagni attesi.

L’autotutela non è libertà illimitata.''')
a=t.index('La conferenza di servizi è uno strumento di coordinamento.',t.index('## 10. Conferenza'));b=t.index('\n## 11. Digitalizzazione',a)
t=t[:a]+'''La conferenza di servizi coordina l’esame di più interessi o l’acquisizione di assensi. I tre tipi si distinguono per funzione:

| Tipo | Funzione e presupposto |
|---|---|
| Istruttoria | L’amministrazione può indire un esame contestuale degli interessi pubblici coinvolti in uno o più procedimenti connessi, quando lo ritiene opportuno. |
| Decisoria | È indetta quando la conclusione positiva richiede più pareri, intese, concerti, nulla osta o altri assensi di amministrazioni diverse, compresi i gestori di beni o servizi pubblici, nei casi dell’art. 14, comma 2. |
| Preliminare | Per progetti complessi o insediamenti produttivi, su richiesta motivata corredata da studio di fattibilità, chiarisce anticipatamente le condizioni per ottenere i successivi assensi. |

Il tipo funzionale non va confuso con la modalità di svolgimento: **asincrona** significa scambio di determinazioni senza presenza contemporanea; **sincrona** significa confronto contestuale, anche telematico. La decisoria segue normalmente la forma semplificata, salvo le ipotesi di riunione previste.

**Termini aggiornati alla disciplina del 2026.** Il DL 19/2026, convertito dalla legge 50/2026, ha modificato gli artt. 14-bis e 14-ter. Nella semplificata il termine perentorio per le determinazioni è al massimo **30 giorni**; diventa **60 giorni** con le amministrazioni preposte a tutela ambientale, paesaggistico-territoriale, beni culturali, salute o incolumità pubblica, salvi maggiori termini del diritto UE. Nella simultanea i lavori si concludono entro **30 giorni dalla riunione**, oppure **60** nei casi qualificati previsti dal rinvio all’art. 14-bis, comma 7. Resta il termine finale del procedimento. I precedenti numeri 45 e 90 non vanno usati come regola generale vigente.

Le determinazioni devono essere motivate, indicare assenso o dissenso e precisare le condizioni utili all’assenso secondo la legge. Nei casi del nuovo art. 14-bis, comma 6, la riunione telematica conduce alla determinazione motivata sulle posizioni prevalenti: non è un semplice conteggio di voti. La determinazione conclusiva sostituisce gli assensi nel campo dell’art. 14-quater; i dissensi qualificati hanno le forme di opposizione dell’art. 14-quinquies.

**Caso:** un progetto richiede assensi di più amministrazioni, incluso quello paesaggistico. Non basta inviare tre richieste e sommare attese indipendenti: qualifica la conferenza decisoria, individua i soggetti e applica i termini del relativo regime. La presenza dell’autorità paesaggistica rileva per il termine di 60 giorni della semplificata; non elimina motivazione, condizioni e disciplina delle opposizioni.

### SCIA: avvio e controlli sono momenti diversi

La segnalazione certificata di inizio attività è un atto del privato. Opera nelle attività per le quali la legge la consente, quando l’abilitazione dipende dall’accertamento di requisiti e non da valutazioni discrezionali o contingenti, con le esclusioni dell’art. 19. Non sostituisce indiscriminatamente assensi ambientali, paesaggistici o altri titoli necessari.

La SCIA ordinaria consente l’avvio dalla presentazione all’amministrazione competente. Se l’attività richiede anche assensi presupposti, la **SCIA condizionata** segue l’art. 19-bis: occorre acquisire tali atti prima dell’inizio. Non dedurre dall’acronimo che si possa iniziare sempre subito.

| Passaggio | Termine e conseguenza |
|---|---|
| Controllo ordinario | Entro 60 giorni dal ricevimento; 30 giorni per SCIA edilizia. Se mancano requisiti, provvedimenti motivati inibitori e di rimozione degli effetti. |
| Conformazione possibile | L’amministrazione prescrive le misure e assegna almeno 30 giorni. La sospensione dell’attività segue gli specifici presupposti dell’art. 19, non ogni irregolarità. |
| Intervento successivo | Dopo il termine ordinario occorrono le condizioni dell’art. 21-nonies; resta, anche per la precisazione del 2026, la disciplina dell’art. 75 DPR 445/2000. |

**Caso:** una SCIA non edilizia è ricevuta e il controllo al giorno 20 individua un difetto sanabile. L’ufficio valuta e prescrive la conformazione, assegnando almeno 30 giorni. Sarebbe errato chiamare quel provvedimento “diniego dell’autorizzazione tacita”: la SCIA non è un’autorizzazione rilasciata dalla PA.

### Verifica dei concetti

1. **Manca la motivazione richiesta di un diniego individuale: è sempre nullo?** No: va qualificato il vizio di legittimità, senza trasformare ogni difetto in mancanza di un elemento essenziale.
2. **SCIA edilizia e ordinaria hanno sempre lo stesso termine di controllo?** No: rispettivamente 30 e 60 giorni nel regime indicato.
3. **La conferenza preliminare rilascia automaticamente il titolo finale?** No: anticipa le condizioni per i successivi assensi.
4. **L’ufficio può revocare un’autorizzazione solo perché rivaluta l’interesse pubblico originario?** L’art. 21-quinquies esclude questa specifica ragione per autorizzazioni e vantaggi economici; vanno distinti gli altri presupposti di revoca.
5. **La mancata comunicazione di avvio rende sempre annullabile l’atto?** Non necessariamente: occorre applicare il test dell’art. 21-octies, con prova dell’amministrazione in giudizio, senza estenderlo automaticamente al preavviso di rigetto.
6. **Nella semplificata il termine generale per le determinazioni è ancora 45 giorni?** No: dal 2026 il massimo generale è 30, con il regime di 60 per i soggetti qualificati e le eccezioni UE indicate.
''' +t[b:]
u.save(s,t,['V01-10','V01-11','V01-12'],ref)
s='prova-scritta-teorico-pratica';t=u.read(s)
t=u.replace(t,'Si invita pertanto l’interessato a trasmettere l’integrazione entro il termine indicato nella comunicazione, attraverso il canale previsto dall’amministrazione.', 'Si invita pertanto l’interessato a trasmettere l’integrazione entro [termine da ricavare dalla disciplina o dalla traccia], attraverso [canale previsto].')
anchor='È una griglia, non un modello da copiare in ogni situazione: pratica, carenza, richiesta, termine, canale, responsabilità e tracciabilità.'
t=u.replace(t,anchor,anchor+'''

Prima di richiedere documenti controlla se sono già detenuti dalla PA o acquisibili d’ufficio: gli artt. 18 della legge 241/1990 e 43 DPR 445/2000 impediscono di trasferire al cittadino un onere documentale che l’ufficio deve assolvere. Se la traccia non fornisce il termine, il segnaposto resta esplicito; non scrivere “entro il termine indicato” senza indicarlo.

### Elaborato completo: richiesta istruttoria

**Dossier didattico.** Il Comune fittizio di Rivafonte riceve il 2 ottobre 2026 la domanda protocollo 1250 di Anna Rossi per un contributo alla rimozione di barriere. La relazione tecnica richiesta dall’avviso non è allegata né disponibile presso altre PA. Il responsabile del procedimento è l’ufficio Servizi alla persona. L’avviso, richiamato nella traccia, ammette l’integrazione entro **10 giorni dalla ricezione della richiesta**, mediante il portale della pratica. La residenza è autocertificata e verificabile dall’ufficio. Redigi la comunicazione: non devi decidere se concedere il contributo.

> **Comune di Rivafonte — Servizi alla persona**
>
> **Alla sig.ra Anna Rossi**
>
> **Oggetto: domanda prot. 1250 del 2 ottobre 2026 — richiesta di integrazione istruttoria**
>
> L’esame della domanda ha rilevato l’assenza della relazione tecnica prevista dall’avviso per valutare l’intervento. Si invita a caricare tale relazione nel portale della pratica entro dieci giorni dalla ricezione della presente comunicazione, secondo la disposizione dell’avviso richiamata nel dossier.
>
> Non è richiesto un certificato di residenza: l’ufficio procederà alla verifica d’ufficio della dichiarazione resa. La richiesta riguarda esclusivamente la relazione tecnica mancante e non anticipa la decisione sul contributo.
>
> L’integrazione sarà inserita nel fascicolo e valutata ai fini della prosecuzione dell’istruttoria. In mancanza, l’ufficio adotterà l’esito previsto dall’avviso, con le garanzie procedimentali applicabili.
>
> Il responsabile del procedimento — ufficio Servizi alla persona.

**Perché funziona.** Sono identificati pratica, carenza, ragione della richiesta, termine e canale. Il termine deriva dal dossier, non da una regola universale. La residenza non viene richiesta come certificato e la comunicazione non finge di essere il provvedimento finale. L’obbligo generale di motivazione dei provvedimenti si ricava dall’art. 3 della legge 241/1990, con le eccezioni per atti normativi e a contenuto generale: nell’elaborato applicativo spiega sempre il collegamento tra fatti e richiesta, senza chiamare “motivazione del diniego” una semplice fase istruttoria.

**Autoverifica:** sarebbe corretto aggiungere “il contributo sarà sicuramente concesso”? No: mancano ancora istruttoria e decisione competente. Sarebbe corretto chiedere anche il certificato anagrafico? No, alle condizioni del dossier il controllo è d’ufficio.
''')
u.save(s,t,['V01-36'],ref)
u.record()
