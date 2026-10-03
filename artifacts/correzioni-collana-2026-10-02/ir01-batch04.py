from pathlib import Path
import json,re
B=Path('wiki/books/moduli/m-ir01-scuola/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
def add(n,txt):
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text(encoding='utf8');i=t.index('\n## Il Bando Decoder');t=t[:i]+'\n'+txt.strip()+'\n'+t[i:];t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8');return str(p).replace('\\','/')
files=[]
files.append(add(11,'''## Modelli dell’apprendimento: concetti da usare nel caso

Una teoria seleziona aspetti del processo di apprendimento e permette di formulare domande. Non prescrive da sola una metodologia valida per qualsiasi disciplina. Nella risposta concorsuale occorre esporre il concetto, collegarlo alla situazione e indicare un limite: il nome dell’autore senza questo passaggio non spiega la scelta.

### Comportamento, rinforzo e apprendimento osservativo

Nel **condizionamento classico**, studiato da Pavlov, uno stimolo inizialmente neutro può evocare una risposta dopo l’associazione con uno stimolo che la produceva. Nel **condizionamento operante**, sviluppato da Skinner, sono centrali le conseguenze di un comportamento: il rinforzo ne aumenta la probabilità futura. Positivo significa che si aggiunge una conseguenza; negativo che si rimuove una condizione avversiva. Non significa rispettivamente “buono” e “cattivo”: il rinforzo negativo non è una punizione. La punizione mira invece a ridurre un comportamento.

In classe un feedback preciso può rendere riconoscibile una strategia efficace: «Hai controllato il denominatore prima del confronto». Non equivale a lodare indistintamente ogni risposta né dimostra, da solo, comprensione. Se lo studente riproduce il procedimento solo in presenza del premio, resta da verificare se sa trasferirlo a una situazione nuova. Nell’**apprendimento osservativo**, associato a Bandura, osservare un modello è una via di acquisizione: attenzione, possibilità di ricordare e riprodurre l’azione e motivazione incidono sul risultato. Il docente che pensa ad alta voce mostra un processo; successivamente deve lasciare all’allievo la possibilità di provarlo.

### Elaborazione cognitiva e costruzione della conoscenza

Il **cognitivismo** porta l’attenzione sui processi mentali: selezione dell’informazione, memoria, rappresentazioni, strategie e soluzione di problemi. Un alunno può fallire perché deve tenere attivi troppi passaggi, anche se possiede singolarmente le conoscenze richieste. Segmentare una consegna e mostrare un esempio svolto riduce richieste concorrenti; il passaggio successivo è togliere parte del sostegno e verificare l’autonomia. Non si deduce un deficit stabile da un solo errore.

Per **Piaget** la conoscenza si costruisce nell’interazione con l’esperienza. L’**assimilazione** interpreta una nuova situazione attraverso schemi già disponibili; l’**accomodamento** modifica quegli schemi quando non bastano. Un bambino può inizialmente classificare tutti i quadrilateri come rettangoli perché usa un modello familiare; confrontare un rombo con angoli non retti rende necessaria una revisione della categoria. Il conflitto tra previsione e osservazione diventa utile se il docente aiuta a esaminarlo, non se si limita a dichiarare sbagliata la risposta.

La teoria piagetiana distingue periodi sensomotorio, preoperatorio, delle operazioni concrete e delle operazioni formali. Il passaggio descrive una trasformazione delle strutture del pensiero, dall’azione e dalla rappresentazione simbolica al coordinamento logico e al ragionamento su ipotesi. Queste categorie storiche non sono una griglia diagnostica che autorizza a fissare capacità e limiti di ogni alunno dalla sola età: compito, esperienza, linguaggio e contesto contano. In progettazione si osservano le prestazioni effettive e si scelgono rappresentazioni adeguate.

### Mediazione sociale, scaffolding e autoregolazione

Per **Vygotskij** lo sviluppo delle funzioni cognitive va letto anche nella mediazione sociale e culturale. La **zona di sviluppo prossimale** riguarda la distanza fra ciò che l’allievo riesce a fare autonomamente e ciò che riesce a fare con una guida o un pari più competente. Una scheda già risolta che l’alunno copia non basta a mostrare apprendimento: occorre controllare che possa affrontare un nuovo compito con meno aiuto.

Lo **scaffolding**, associato al lavoro di Wood, Bruner e Ross, è un sostegno adattato al compito e alla competenza dell’allievo, destinato a ridursi. Si può iniziare mostrando un esempio, poi offrire solo domande guida e infine richiedere una soluzione autonoma. L’aiuto permanente che sostituisce l’azione dell’alunno non è il risultato atteso. Nel **curricolo a spirale** di Bruner si riprendono idee fondamentali a livelli progressivamente più complessi: non si ripete identicamente la stessa scheda ogni anno.

L’**autoefficacia**, nel modello di Bandura, è la convinzione di poter affrontare un compito; non coincide con l’abilità effettiva né con l’autostima generale. Un obiettivo intermedio raggiungibile e un feedback sulla strategia possono aiutare a leggere il progresso. La **metacognizione** comprende conoscenza e controllo dei propri processi: pianificare, monitorare la comprensione e valutare l’esito. Chiedere «Quale passaggio controllerai? Perché?» rende osservabile una strategia; chiedere soltanto «Hai capito?» produce un’indicazione debole.

**Caso risolto.** Sara risolve un problema con un esempio davanti, ma sbaglia quando cambiano i dati. Il docente non conclude che “non è portata”: le chiede di spiegare perché ha scelto l’operazione, propone un problema analogo con una domanda guida e poi uno nuovo senza modello. La prima prestazione era assistita; la terza verifica il trasferimento. Se l’errore resta, analizza il passaggio specifico anziché moltiplicare esercizi identici. Nella lettura teorica ricorrono mediazione, graduale ritiro dell’aiuto e controllo metacognitivo.

## PEI, PDP e gruppi di lavoro: la distinzione operativa

Il **Piano educativo individualizzato (PEI)** riguarda l’alunno con accertata condizione di disabilità ai fini dell’inclusione. In base all’art. 7 del D.Lgs. 66/2017, è elaborato e approvato dal **Gruppo di lavoro operativo per l’inclusione (GLO)**. Considera il profilo di funzionamento, barriere e facilitatori; collega obiettivi, strumenti, sostegno, verifiche, valutazione e interventi. Il docente di sostegno è contitolare della classe: l’inclusione non è una sua responsabilità esclusiva.

Il GLO coinvolge team docente o consiglio di classe, genitori o chi esercita la responsabilità genitoriale, figure professionali pertinenti e supporto multidisciplinare; è assicurata la partecipazione attiva dello studente nel rispetto dell’autodeterminazione. Il **GLI**, Gruppo di lavoro per l’inclusione, opera invece a livello d’istituto, sostenendo il Piano per l’inclusione e l’attuazione dei PEI. Confondere GLO e GLI significa attribuire al livello sbagliato il progetto individuale.

### Le modifiche vigenti dal 1° ottobre 2026

Il D.L. 30 settembre 2026, n. 170, art. 1, ha modificato il quadro. Per nuova iscrizione o nuova certificazione, il PEI è provvisorio entro giugno e definitivo entro il **15 ottobre**. Per chi è già inserito nel percorso di supporto e già iscritto nella medesima scuola, è definitivo entro giugno, con aggiornamenti, correttivi e integrazioni nelle prime due settimane di ottobre; restano possibili successive modifiche per nuove condizioni di funzionamento. Non basta quindi ricordare il precedente termine generico di ottobre. Al 3 ottobre 2026 il decreto-legge è vigente e attende conversione: per procedure successive si controlla anche l’esito parlamentare.

Il PEI definisce con adeguata motivazione le ore di sostegno da assegnare alla classe. Nel passaggio d’anno si valuta prioritariamente il mantenimento delle ore precedenti, salva l’assegnazione dell’organico e gli aggiornamenti motivati previsti: non si tratta di una conferma automatica indipendente dal caso. Restano le verifiche periodiche. L’art. 15, comma 11-bis, della L. 104/1992 consente, alle condizioni indicate, l’approvazione anche se manca una componente regolarmente convocata e l’assenza impedirebbe il rispetto dei termini; non consente di escludere la famiglia dalla convocazione.

### DSA: documentare la didattica nel PDP

Il **Piano didattico personalizzato (PDP)** formalizza, nel quadro della L. 170/2010 e del D.M. 5669/2011, attività individualizzate e personalizzate, strumenti compensativi, misure dispensative e forme di verifica e valutazione. Il team o consiglio di classe lo costruisce in raccordo con la famiglia; le Linee guida del 2011 prevedono la documentazione entro il primo trimestre. Non è un PEI abbreviato e la sola certificazione di DSA non attribuisce automaticamente il docente di sostegno.

L’**individualizzazione** adatta metodi e percorsi per raggiungere competenze comuni; la **personalizzazione** considera bisogni, interessi e potenzialità della persona. Nel quadro DSA questo non autorizza a ridurre arbitrariamente gli obiettivi curricolari. La sintesi vocale è uno strumento compensativo per accedere al testo; la dispensa da una prestazione non essenziale evita un ostacolo connesso al disturbo. Nessuna delle due garantisce comprensione: la verifica deve ancora raccogliere un’evidenza dell’obiettivo.

**Esempio.** La consegna richiede di spiegare le cause di un fenomeno storico. Per un alunno con DSA, il PDP prevede ascolto del testo e mappa. La prova può consentire questi strumenti e chiedere una spiegazione motivata delle cause. La mappa non viene valutata come una concessione indebita, ma non sostituisce la risposta. Se invece la prova mira a un’abilità specifica di lettura, modalità e criteri vanno progettati coerentemente con quel diverso obiettivo e con il PDP.

## Verifica commentata dei concetti

**1. Quale descrizione corrisponde all’accomodamento?** A. Ripetere uno schema invariato. B. Modificare uno schema per interpretare una nuova esperienza. C. Aumentare una risposta con un premio. D. Valutare l’esito del proprio studio.

**2. Un allievo riesce con domande guida ma non ancora da solo. Quale distinzione è pertinente?** A. Competenza certificata e voto. B. Rinforzo e punizione. C. Prestazione autonoma e assistita nella zona prossimale. D. Età anagrafica e obbligo scolastico.

**3. Il rinforzo negativo è:** A. rimozione di una condizione avversiva che aumenta un comportamento; B. qualsiasi rimprovero; C. abbassamento del voto; D. esclusione dal gruppo.

**4. Chi elabora e approva il PEI?** A. Il GLI al posto dei docenti. B. Il solo docente di sostegno. C. Il consiglio d’istituto. D. Il GLO.

**5. La sintesi vocale, nel quadro del PDP, è:** A. una diagnosi; B. uno strumento compensativo; C. una dispensa da ogni verifica; D. un obiettivo differenziato automatico.

**6. Quale domanda sollecita un controllo metacognitivo?** A. «Quanti anni hai?» B. «Hai copiato il modello?» C. «Quale passaggio hai controllato e perché?» D. «Qual è il tuo voto precedente?»

**Soluzioni.** 1 B: lo schema cambia; A descrive uso invariato, C rinforzo, D autovalutazione. 2 C: si confrontano due livelli di prestazione nello stesso compito; le altre coppie non descrivono l’aiuto didattico. 3 A: “negativo” riguarda la rimozione; B–D non definiscono il rinforzo e possono avere funzioni diverse. 4 D: il GLO è il gruppo del singolo alunno; GLI, consiglio d’istituto e singolo docente non lo sostituiscono. 5 B: facilita l’accesso al testo senza cancellare l’obiettivo; A, C e D confondono strumento, accertamento e valutazione. 6 C: chiede strategia e motivazione, mentre le altre domande raccolgono dati diversi.'''))
files.append(add(13,'''## Lezione svolta: quando due frazioni rappresentano la stessa quantità

**Traccia di allenamento originale.** Progetta una lezione sulle frazioni equivalenti per una classe quarta primaria. Motiva attività, inclusione e valutazione. Assumiamo 22 alunni, 60 minuti, conoscenza di numeratore e denominatore e materiali cartacei. Questi dati sono ipotesi progettuali, non condizioni attribuite a un bando. Non ipotizziamo diagnosi; eventuali PEI e PDP effettivamente presenti guiderebbero gli adattamenti individuali.

**Obiettivo osservabile.** Al termine, l’alunno rappresenta 1/2 e 2/4 sullo stesso intero, riconosce l’uguaglianza della quantità e la spiega con disegno e parole. Il confronto mantiene uguale l’intero: metà di una striscia lunga e metà di una corta non sono la stessa quantità assoluta.

### Contenuto e materiali pronti all’uso

La frazione indica quante parti uguali dell’intero consideriamo. In 2/4, il denominatore 4 indica la suddivisione in quattro parti uguali; il numeratore 2 le parti considerate. Se ogni metà viene divisa in due, la metà inizialmente colorata comprende ora due quarti: la quantità colorata non cambia. Moltiplicare numeratore e denominatore per lo stesso numero naturale non nullo produce una frazione equivalente. Qui la regola si ricava dalla rappresentazione, prima di applicarla simbolicamente.

Ogni coppia riceve tre strisce rettangolari identiche, matita e righello; il docente prepara un modello alla lavagna. La prima striscia è divisa in due parti uguali, la seconda in quattro, la terza in otto. Le strisce possono essere predisposte con suddivisioni marcate, così l’abilità motoria richiesta dal disegno non impedisce di ragionare sulla quantità. I materiali non contengono dati personali e funzionano senza dispositivi digitali.

### Sequenza di 60 minuti

| Tempo | Attività | Evidenza raccolta |
| --- | --- | --- |
| 0–8 minuti | Richiamo: colorare 1/2 su una striscia e spiegare i due numeri | Riconoscimento delle parti uguali e del significato della frazione |
| 8–20 minuti | Dimostrazione guidata: confrontare 1/2 e 2/4 su interi uguali | Previsione, sovrapposizione e spiegazione dell’uguaglianza |
| 20–35 minuti | A coppie: rappresentare 4/8 e confrontarlo con le prime due strisce | Disegno, discussione e motivazione |
| 35–45 minuti | Discussione di un errore: «2/4 è maggiore perché 2 è maggiore di 1» | Correzione che considera anche denominatore e intero |
| 45–55 minuti | Compito individuale con dati nuovi | Trasferimento oltre l’esempio svolto |
| 55–60 minuti | Restituzione e domanda finale | Punto compreso e passaggio ancora da chiarire |

**Parole del docente.** «Le due strisce hanno la stessa lunghezza. Nella prima coloriamo una delle due metà; nella seconda due dei quattro quarti. Prima di sovrapporle, prevedete se una parte colorata sarà più lunga. Poi controllate. Che cosa è cambiato: la quantità oppure il modo di dividerla e nominarla?» Non anticipo la risposta di tutti: ascolto anche chi confonde il numero delle parti con la loro grandezza.

Nella coppia, un alunno rappresenta e l’altro controlla la suddivisione; a metà lavoro i ruoli si scambiano. Il prodotto comune non basta per valutare entrambi: il compito finale è individuale. Le consegne sono lette e mostrate per passaggi; chi necessita di un accesso diverso può usare strisce già divise o spiegazione orale coerente con l’obiettivo. Non si attribuiscono dispense o obiettivi individuali senza i documenti pertinenti.

### Verifica finale, soluzione e feedback

La scheda contiene tre richieste: **a)** rappresenta 3/6 su una striscia e scrivi una frazione equivalente con denominatore 2; **b)** confronta 1/2 e 1/3 sullo stesso intero; **c)** spiega perché 2/4 non è maggiore di 1/2 nonostante il numeratore maggiore. Si può rispondere con disegno e spiegazione breve; quando previsto, il docente raccoglie una spiegazione orale equivalente.

**Soluzione.** a) Si colorano tre delle sei parti uguali: 3/6 = 1/2. b) 1/2 è maggiore di 1/3 perché, a parità di intero e con una sola parte considerata, dividere in due produce parti più grandi che dividere in tre. c) Il numeratore non si confronta isolatamente: due quarti occupano la stessa metà dell’intero. Disegni con interi diversi non dimostrano il confronto richiesto.

| Criterio | Da sostenere | In sviluppo | Autonomo nel compito |
| --- | --- | --- | --- |
| Rappresentazione | Parti disuguali o quantità non coerente | Rappresentazione corretta con un richiamo | Parti e quantità corrette senza aiuto |
| Equivalenza | Decide solo dal numeratore | Riconosce l’equivalenza con il modello | Riconosce 3/6 = 1/2 nel caso nuovo |
| Spiegazione | Non collega disegno e simbolo | Collega con domande guida | Motiva mantenendo uguale l’intero |

Questa rubrica serve a osservare il compito e dare feedback; non converte automaticamente una singola prestazione nei giudizi periodici dell’O.M. 3/2025. Un feedback utile è: «La suddivisione è corretta; ora spiega perché le parti colorate sono la stessa quantità». Se prevale l’errore del numeratore, la lezione successiva riprende confronti visivi con interi uguali; se il concetto è acquisito, introduce nuove equivalenze e il collegamento alla retta numerica.

### Difendere le scelte all’orale

**Perché iniziare dalla striscia?** Per rendere osservabile che cambia la partizione, mentre resta invariata la quantità. La rappresentazione sostiene il passaggio al simbolo; non sostituisce indefinitamente il ragionamento astratto.

**Perché una prova individuale dopo le coppie?** Per distinguere il risultato del gruppo dalla prestazione autonoma. Un compagno può guidare senza che l’altro abbia ancora acquisito il concetto.

**Come ridurre la lezione a 40 minuti?** Ridurrei il confronto collettivo e il numero delle rappresentazioni, mantenendo attivazione, un esempio ragionato e la verifica individuale. Non eliminerei la verifica per conservare più attività.

**Come preparare la prova reale?** Per infanzia e primaria leggo D.M. 206/2023 e allegato della procedura; per secondaria D.M. 205/2023, programma della classe e prescrizioni del bando applicabile. La durata di questa attività in classe non è la durata dell’orale concorsuale. I contenuti specialistici di ogni disciplina vanno preparati sul programma identificato: questo esempio insegna a progettare e motivare, non dichiara coperti tutti i programmi disciplinari.'''))
p=next(B.glob('13-*.md'));t=p.read_text(encoding='utf8');t=t.replace('[[sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994]]','[[sources/programmi-concorsi-docenti-dm-205-206-2023]]');t=t.replace('La disciplina della classe di concorso o del posto resta da preparare nel verticale specifico: qui impari a darle una forma didattica e orale.','Per la disciplina della classe di concorso o del posto, la destinazione è il programma dell’allegato A al D.M. 205/2023 o al D.M. 206/2023 pertinente, integrato dal bando applicabile: questo capitolo tratta il nucleo progettuale comune e offre una lezione completa di esempio.');p.write_text(t,encoding='utf8')
batch={'V06-08':{'change':'Integrati modelli psicopedagogici, PEI/PDP/GLO/GLI, individualizzazione e personalizzazione, sei quiz commentati e lezione completa su frazioni equivalenti con materiali, tempi, soluzione e rubrica. Aggiornato PEI al D.L.170/2026 e sostituito il richiamo improprio al DPR487 nella prova docente.','files':files+['wiki/sources/inclusione-scolastica-disabilita-dsa-dlgs-66-2017-legge-170-2010.md','wiki/sources/programmi-concorsi-docenti-dm-205-206-2023.md'],'evidence':'Letti art.7 D.Lgs.66, art.15 L.104 e art.1 D.L.170 vigenti; Linee guida DSA pp.6–8; quiz e calcoli delle frazioni risolti. Conversione D.L.170 da seguire dopo la data editoriale.','status':'applicato'}}
(A/'VOL-06-batch04.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('IR01/11 e13 integrati')
