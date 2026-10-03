from pathlib import Path
import re,hashlib,json
p=Path('wiki/books/moduli/m-fc04-giustizia/chapters/13-giustizia-minorile-comunita-mediazione-riparativa.md')
s=p.read_text(encoding='utf8');before=s
archive=Path('artifacts/correzioni-collana-2026-10-02/VOL-04-cap13-prima.md')
assert not archive.exists(),'Non rieseguire integrazione'
archive.write_text(s,encoding='utf8')
def section(name,text):
 global s
 pat=r'(?ms)^### '+re.escape(name)+r'\n.*?(?=^### |\Z)'
 s,n=re.subn(pat,'### '+name+'\n\n'+text.strip()+'\n\n',s);assert n==1,name
section('Processo penale minorile: criteri essenziali','''Il D.P.R. 448/1988 adatta le regole processuali alla personalità e alle esigenze educative dell'imputato minorenne. Si considera l'età **al momento del fatto**: diventare maggiorenne durante il procedimento non trasforma retroattivamente il reato in un fatto commesso da adulto. La finalità educativa convive con difesa, accertamento della responsabilità e tutela della vittima.

| Età al fatto | Imputabilità: artt. 97–98 c.p. |
|---|---|
| Meno di 14 anni | Non imputabile per legge |
| Da 14 a meno di 18 anni | Imputabile solo se capace di intendere e di volere; pena diminuita |

La capacità del quindicenne non si presume dalla sola gravità dell'accusa. PM e giudice raccolgono elementi personali, familiari, sociali e ambientali, anche sentendo esperti, per valutare imputabilità, responsabilità e misure adeguate (art. 9). L'USSM fornisce informazioni e sostegno; non pronuncia il giudizio di imputabilità.

Il giudice spiega al ragazzo il significato delle attività e delle decisioni. L'assistenza affettiva e psicologica dei genitori o di altri esercenti la responsabilità genitoriale si affianca alla difesa tecnica: non la sostituisce. Nei casi dell'art. 12, per esempio quando la presenza del genitore contrasta con l'interesse superiore del minore, interviene altra persona idonea, indicata dal ragazzo e ammessa dall'autorità o designata da quest'ultima. Resta assicurata l'assistenza dei servizi, ferme le eccezioni per singoli atti previste dalla legge.

L'art. 13 vieta la diffusione di notizie o immagini che consentano di identificare il minore coinvolto: anche iniziali, scuola e luogo, combinati, possono identificarlo. La norma prevede l'eccezione dopo l'inizio del dibattimento quando il tribunale procede in udienza pubblica; non autorizza l'operatore a pubblicare il fascicolo.

Nel quadro vigente al 3 ottobre 2026 opera ancora il tribunale per i minorenni: il nuovo tribunale per le persone, per i minorenni e per le famiglie è rinviato al 2027. Nel processo minorile si distinguono GIP monocratico, GUP con un magistrato e due componenti onorari e collegio dibattimentale con due magistrati e due componenti onorari. Per l'organizzazione degli uffici si veda il capitolo 3, «Uffici giudiziari e ordinamento».

**Esempio.** Due persone di 13 e 16 anni sono coinvolte nello stesso fatto. Per la prima opera l'art. 97; per la seconda occorre accertare la capacità prevista dall'art. 98. Il progetto sociale può interessare entrambe, ma non produce la stessa risposta penale. Scrivere soltanto «sono entrambi minori» elimina la distinzione richiesta dal caso.''')
section('Messa alla prova minorile','''La sospensione del processo con messa alla prova consente al giudice di valutare la personalità del minorenne dopo un percorso educativo. Non è una misura alternativa a una pena definitiva: il processo è ancora pendente. Ai sensi degli artt. 28–29 del D.P.R. 448/1988, il giudice, sentite le parti, dispone la sospensione con ordinanza e affida il ragazzo ai servizi minorili per osservazione, trattamento e sostegno, anche con i servizi territoriali.

| Elemento | Regola da applicare |
|---|---|
| Durata massima ordinaria | Un anno |
| Reati con ergastolo o reclusione massima di almeno 12 anni | Tre anni; il richiamo alla pena edittale non significa che l'ergastolo sia irrogabile al minorenne |
| Prescrizione | Sospesa durante la prova |
| Revoca | Trasgressioni alle prescrizioni ripetute e gravi |
| Esito positivo | Sentenza del giudice che dichiara estinto il reato |
| Esito negativo | Il processo riprende secondo le regole del rito; non segue automaticamente una condanna |

Il programma traduce bisogni e risorse in attività verificabili: frequenza scolastica, formazione, incontri con i servizi, impegni compatibili con l'età, sostegno familiare e prescrizioni riparative. L'USSM documenta andamento e criticità; il giudice valuta comportamento ed evoluzione della personalità. Un'attestazione di frequenza non equivale da sola al successo della prova.

**Preclusioni da conoscere.** Il comma 5-bis esclude la prova per omicidio aggravato ai sensi dell'art. 576 c.p., violenza sessuale e violenza sessuale di gruppo aggravate ai sensi dell'art. 609-ter e rapine aggravate nelle ipotesi dell'art. 628, terzo comma, numeri 2, 3 e 3-quinquies. Per le due fattispecie sessuali, la Corte costituzionale n. 203/2025 ha rimosso il divieto quando ricorre l'attenuante dei casi di minore gravità. La sentenza n. 110/2026 non ha eliminato in generale le restanti preclusioni. Occorre quindi qualificare il reato e le circostanze, non limitarsi alla disponibilità di un buon progetto.

Un altro errore nasce dalla lettura isolata del comma 4: il divieto collegato alla richiesta di giudizio abbreviato o immediato è stato dichiarato illegittimo dalla Corte costituzionale n. 125/1995. Quelle richieste non escludono di per sé la prova.

**Caso breve.** Per un reato non precluso, punito con reclusione massima di dieci anni, si propone una prova di diciotto mesi. Il limite è un anno: un progetto convincente non consente al servizio di superarlo. Dopo la prova, una relazione positiva costituisce materiale valutativo; occorre comunque la sentenza del giudice per estinguere il reato. L'invito a un programma riparativo rimane distinto dalle prescrizioni: il rifiuto della vittima di partecipare non può essere trattato come violazione del minore.''')
section('Messa alla prova adulti e giustizia di comunità','''La prova adulta, introdotta dalla L. 67/2014 e disciplinata dagli artt. 168-bis–168-quater c.p. e 464-bis e seguenti c.p.p., richiede l'iniziativa dell'imputato, anche dopo proposta del PM. Riguarda i reati puniti con sola pena pecuniaria oppure con pena detentiva massima non superiore a quattro anni, sola o congiunta/alternativa alla pecuniaria, e gli ulteriori delitti elencati nell'art. 550, comma 2, c.p.p. L'ultima categoria impedisce di trasformare «quattro anni» in una regola senza eccezioni.

La richiesta si presenta entro i termini del rito: nell'udienza preliminare prima delle conclusioni; nel direttissimo prima dell'apertura del dibattimento; nella citazione diretta prima della conclusione dell'udienza predibattimentale. Giudizio immediato e decreto penale hanno termini specifici. Non si attende liberamente la fine del processo. L'imputato allega il programma elaborato d'intesa con l'UEPE oppure la richiesta di elaborarlo; il giudice verifica idoneità del programma e prognosi di astensione da altri reati, sentendo anche la persona offesa.

Il programma comprende interventi sociali, prescrizioni, eliminazione delle conseguenze dannose o pericolose e, ove possibile, risarcimento. **Il lavoro di pubblica utilità è necessario**: prestazione gratuita di almeno dieci giorni, anche non continuativi, con durata giornaliera non superiore a otto ore, compatibile con lavoro, studio, famiglia e salute. Non coincide con il lavoro penitenziario remunerato. Eventuali attività riparative richiedono le rispettive garanzie e non impongono alla vittima di incontrare l'imputato.

| Profilo | Prova minorile | Prova adulta |
|---|---|---|
| Servizio di riferimento | USSM | UEPE |
| Criterio centrale | Personalità ed evoluzione educativa | Programma idoneo e prognosi favorevole |
| Sospensione massima | Uno o tre anni secondo l'art. 28 | Due anni con pena detentiva; uno con sola pecuniaria |
| Lavoro di pubblica utilità | Non requisito generale dell'art. 28 | Requisito necessario |
| Esito positivo | Estinzione del reato | Estinzione del reato; restano eventuali sanzioni amministrative accessorie |

Per l'adulto la concessione è, di regola, una sola volta e non è ammessa ai delinquenti abituali, professionali o per tendenza indicati dalla legge. La Corte costituzionale n. 174/2022 consente una nuova ammissione quando un diverso procedimento riguarda reati in concorso formale o in continuazione con quelli già oggetto della prova: il giudice deve rivalutare programma e prognosi, rispettando il limite complessivo di durata. Non è un diritto a ripetere la prova per qualsiasi nuovo reato.

La revoca adulta segue violazioni gravi **o** ripetute, rifiuto del lavoro di pubblica utilità, oppure commissione durante la prova di un delitto non colposo o di un reato della stessa indole. Nel testo minorile le trasgressioni sono invece «ripetute e gravi». Con esito positivo il giudice dichiara estinto il reato; con esito negativo dispone la ripresa del procedimento. L'UEPE controlla e riferisce, senza assumere la decisione giurisdizionale.

**Confronto decisivo.** Prova processuale positiva: si estingue il reato. Affidamento in prova al servizio sociale del condannato: si sta eseguendo una pena, con gli effetti dell'art. 47 O.P. esaminati nel capitolo 14. Il nome simile non rende intercambiabili i due istituti.''')
section('Misure penali di comunità per minorenni','''Il D.Lgs. 121/2018 riguarda l'esecuzione della condanna, distinta dalla prova processuale. Le misure penali di comunità devono favorire educazione, responsabilizzazione, inclusione e prevenzione della recidiva. Il progetto considera maturità, salute, studio, formazione, famiglia e ambiente; può prevedere collocamento in comunità quando serve a renderlo praticabile.

| Misura | Soglia e contenuto essenziale |
|---|---|
| Affidamento in prova | Pena da eseguire fino a quattro anni; programma educativo e prescrizioni nella comunità |
| Affidamento con detenzione domiciliare | Stesso limite; permanenza domiciliare in giorni della settimana determinati dal provvedimento |
| Detenzione domiciliare | Pena fino a tre anni quando non ricorrono condizioni per l'affidamento; restano le ipotesi speciali richiamate dall'art. 6 |
| Semilibertà | Almeno un terzo della pena espiato; parte del giorno fuori per attività formative, lavorative o di reinserimento, con rientro in istituto |

Il decreto include anche l'affidamento in casi particolari, collegato alla disciplina terapeutica: la disponibilità di un posto in comunità da sola non ne dimostra i presupposti. Per la semilibertà l'art. 7 impone ulteriori valutazioni per i reati richiamati dall'art. 4-bis, comma 1, O.P., considerando il rapporto significativo fra pena espiata e residua.

**Chi decide.** Il tribunale di sorveglianza per i minorenni concede, sostituisce e revoca le misure. L'USSM prepara l'istruttoria e il programma con i servizi territoriali e riferisce sull'esecuzione; il magistrato di sorveglianza interviene sulle prescrizioni e nei casi di tutela provvisoria previsti dalla legge. Una relazione favorevole non è un titolo per uscire dall'istituto.

**Quali condizioni.** La misura deve essere idonea all'evoluzione positiva della personalità e non deve emergere pericolo di fuga o di nuovi reati. Il domicilio va verificato, la rete deve essere reale, gli orari devono permettere scuola e cura. La durata corrisponde normalmente alla pena residua. Le violazioni incompatibili con la prosecuzione possono determinare revoca: il servizio documenta il fatto, il giudice decide.

La Corte costituzionale n. 263/2019 ha eliminato il rinvio automatico dell'art. 2, comma 3, ai divieti dell'art. 4-bis O.P. Il tribunale deve valutare individualmente il percorso minorile: non è corretto né applicare in blocco tutte le preclusioni adulte né considerare ogni minore automaticamente ammesso.

**Caso breve.** Restano tre anni e sei mesi di pena, con programma scolastico e domicilio idoneo. La soglia consente di esaminare l'affidamento fino a quattro anni; non consente la domiciliare ordinaria dell'art. 6, limitata a tre. Il tribunale valuta anche rischio, risorse e prescrizioni. La sola sottrazione aritmetica della pena non decide la misura.''')
section('Accesso, centri, mediatori ed esito riparativo','''Gli artt. 42–58 del D.Lgs. 150/2022 distinguono accesso, preparazione, programma ed esito. L'accesso è gratuito e non è escluso in base al solo titolo o alla gravità del reato; è possibile in ogni fase, anche dopo l'esecuzione. I mediatori valutano fattibilità e protezione dei partecipanti: l'ampiezza dell'accesso non giustifica incontri pericolosi o forzati.

| Passaggio | Garanzia concreta |
|---|---|
| Informazione | Spiegare percorso, diritti, effetti e limiti in modo comprensibile |
| Consenso | Personale, libero, informato, scritto e revocabile |
| Preparazione | Colloqui preliminari anche separati e verifica della fattibilità |
| Svolgimento | Almeno due mediatori esperti adeguatamente formati, indipendenti e imparziali |
| Conclusione | Eventuale esito simbolico o materiale, proporzionato e rispettoso della dignità |

Per chi ha meno di quattordici anni il consenso è espresso da chi esercita la responsabilità genitoriale, dopo ascolto e assenso del minore capace di discernimento. Dai quattordici anni si raccoglie anche il consenso del minore; l'art. 48 disciplina la possibilità di procedere nel suo interesse in caso di dissenso del rappresentante. Non basta la firma dell'operatore del servizio. I difensori possono assistere nella raccolta del consenso quando richiesto.

La riservatezza protegge il dialogo: mediatori e personale non possono divulgare ciò che apprendono, salvo le eccezioni dell'art. 50, fra cui consenso, prevenzione di reati imminenti o gravi e dichiarazioni che costituiscono esse stesse reato. Gli artt. 51–52 prevedono inutilizzabilità delle dichiarazioni e segreto, con i limiti stabiliti dalla legge. Non si trasferiscono nel fascicolo del servizio i verbali informali del confronto riparativo come se fossero prove liberamente utilizzabili.

L'art. 58 consente al giudice di valutare lo svolgimento e l'esito del programma, ma **mancata partecipazione, interruzione o mancato raggiungimento dell'esito non producono effetti sfavorevoli** alla persona indicata come autore dell'offesa. L'eventuale mancanza di un accordo non dimostra scarsa collaborazione processuale e non autorizza sanzioni.

I centri per la giustizia riparativa organizzano i programmi; non coincidono con USSM o UEPE. L'assistente sociale che segue il caso non assume automaticamente il ruolo di mediatore: occorrono qualificazione e garanzie di indipendenza. Il programma può comprendere mediazione e dialogo riparativo anche con forme diverse dall'incontro diretto tra le persone del singolo fatto.''')
s=s.replace("con l'intervento di un mediatore esperto.","con l'intervento di almeno due mediatori esperti.").replace('adeguatamente informati','adeguatamente formati').replace('| Si |','| Sì |').replace('| No | Si |','| No | Sì |')
section('Quiz commentato','''**Q1. Un ragazzo aveva tredici anni al momento del fatto. Quale regola si applica?**

A) L'imputabilità dipende esclusivamente dalla perizia sulla maturità.
B) È imputabile se compie quattordici anni prima dell'udienza.
C) Non è imputabile per età, ai sensi dell'art. 97 c.p.
D) È imputabile soltanto per i delitti puniti con pena superiore a dodici anni.

**Risposta C.** Il dato decisivo è l'età al fatto. A trasferisce agli infraquattordicenni l'accertamento previsto per la fascia successiva; B cambia indebitamente il momento rilevante; D inventa un'eccezione fondata sulla gravità.

**Q2. La prova minorile riguarda un reato non precluso con massimo edittale di dieci anni. Qual è il limite della sospensione?**

A) Un anno.
B) Due anni.
C) Tre anni.
D) La durata del progetto, senza limite legale.

**Risposta A.** Il limite triennale richiede ergastolo edittale o reclusione massima almeno dodici anni. B confonde la prova adulta; C applica la fascia errata; D attribuisce al progetto il potere di superare la legge.

**Q3. Quale elemento è necessario nella messa alla prova adulta?**

A) Una condanna definitiva già eseguibile.
B) L'incontro diretto con la vittima.
C) L'ammissione del programma da parte del solo UEPE.
D) Il lavoro di pubblica utilità, oltre agli altri presupposti di legge.

**Risposta D.** Il LPU è condizione necessaria ex art. 168-bis. A confonde prova e misura esecutiva; B contrasta con la volontarietà riparativa; C sottrae la decisione al giudice.

**Q4. Nell'esecuzione minorile residuano tre anni e sei mesi. Quale affermazione è corretta, in assenza di ipotesi speciali?**

A) La domiciliare dell'art. 6 è concedibile perché la pena è sotto quattro anni.
B) La soglia permette di valutare l'affidamento, ma occorrono gli altri presupposti e la decisione del tribunale.
C) L'USSM può concedere direttamente l'affidamento.
D) Ogni misura è esclusa perché il residuo supera tre anni.

**Risposta B.** L'affidamento arriva a quattro anni; la domiciliare ordinaria a tre. A scambia i limiti, C scambia servizio e giudice, D ignora la misura pertinente.

**Q5. Una persona interrompe volontariamente il programma riparativo senza raggiungere un accordo. Quale conclusione è corretta?**

A) L'interruzione è una confessione implicita.
B) Il mediatore decide la revoca della prova.
C) L'interruzione non produce di per sé effetti sfavorevoli ai sensi dell'art. 58.
D) Il consenso non era revocabile dopo il primo incontro.

**Risposta C.** Il consenso resta revocabile e l'esito negativo del percorso non diventa sanzione. A nega le garanzie, B attribuisce poteri giudiziari al mediatore, D elimina la volontarietà.

**Q6. Quale confronto tra istituti è corretto?**

A) La prova processuale positiva estingue il reato; l'affidamento in prova riguarda una pena da eseguire.
B) Entrambi sospendono un processo ancora pendente.
C) Entrambi sono concessi direttamente dai servizi sociali.
D) L'affidamento in prova estingue sempre il reato, prima della condanna.

**Risposta A.** La fase processuale e l'oggetto dell'effetto sono diversi. B e D confondono cognizione ed esecuzione; C elimina il provvedimento del giudice.''')
s=s.replace('source_refs: [','source_refs: [\n  "sources/vol-04-minorile-penitenziario-verifica-2026-10-03.md",\n  "sources/vol-04-organizzazione-upp-verifica-2026-10-03.md",',1)
s=s.replace('topics: [','topics: ["topics/giustizia-minorile-e-penitenziaria-m-fc04.md", ',1)
s=s.replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/sources/vol-04-minorile-penitenziario-verifica-2026-10-03.md",\n  "wiki/topics/giustizia-minorile-e-penitenziaria-m-fc04.md",',1)
s=re.sub(r'updated_at: .*','updated_at: 2026-10-03',s,count=1)
p.write_text(s,encoding='utf8')
print(json.dumps({'file':p.as_posix(),'before':hashlib.sha256(before.encode()).hexdigest(),'after':hashlib.sha256(s.encode()).hexdigest(),'words':len(s.split())},indent=2))
