from pathlib import Path
import re,hashlib,json
p=Path('wiki/books/moduli/m-fc04-giustizia/chapters/14-amministrazione-penitenziaria-trattamento-istituti-esecuzione-esterna.md')
s=p.read_text(encoding='utf8');before=s
archive=Path('artifacts/correzioni-collana-2026-10-02/VOL-04-cap14-prima.md')
assert not archive.exists(),'Non rieseguire integrazione'
archive.write_text(s,encoding='utf8')
def section(name,text):
 global s
 pat=r'(?ms)^### '+re.escape(name)+r'\n.*?(?=^### |\Z)'
 s,n=re.subn(pat,'### '+name+'\n\n'+text.strip()+'\n\n',s);assert n==1,name
s=s.replace('perde meta del capitolo', 'perde metà del capitolo').replace("perde l'altra meta", "perde l'altra metà").replace("l'internato è sottoposto a misura di sicurezza;", "l'internato è sottoposto a una misura di sicurezza detentiva;")
needle='### Fonti dell\'ordinamento penitenziario'
insert='''### Case circondariali, case di reclusione e titolo della presenza

La **casa circondariale** è destinata alla custodia degli imputati a disposizione delle autorità giudiziarie e accoglie anche persone arrestate o fermate in transito. La **casa di reclusione** è destinata all'esecuzione della pena della reclusione. Gli artt. 59–61 O.P. distinguono istituti per custodia, esecuzione, misure di sicurezza e osservazione.

Questa destinazione organizzativa non permette di dedurre il titolo di ogni persona dalla sola insegna dell'istituto: sono previste sezioni e assegnazioni che consentono anche la presenza di condannati nelle case circondariali. Nel fascicolo occorre verificare il provvedimento, la definitività della condanna e l'eventuale cumulo di titoli.

**Esempio.** Una persona è ospitata in casa circondariale ma la sua sentenza è divenuta definitiva. Non si continua a descriverla come imputato solo perché l'istituto non è una casa di reclusione. L'ufficio aggiorna la posizione giuridica e il raccordo con osservazione e trattamento sulla base degli atti ricevuti.

'''
assert needle in s;s=s.replace(needle,insert+needle,1)
needle='### Lavoro penitenziario'
insert='''### Dall'osservazione all'approvazione del programma

L'art. 13 O.P. impone la prima formulazione del programma **entro sei mesi dall'inizio dell'esecuzione**. L'osservazione inizia subito e prosegue durante la pena: il semestre non è un periodo nel quale lasciare la persona senza attività o sostegno. Il precedente termine di nove mesi ancora leggibile nell'art. 27 del regolamento va coordinato con la norma primaria successiva, che prevale.

| Passaggio | Responsabilità e documento |
|---|---|
| Raccolta degli elementi | Operatori e specialisti: dati personali, sociali, sanitari pertinenti e osservazioni documentate |
| Formulazione | Gruppo presieduto dal direttore, ex art. 29 del regolamento: programma individuale e sue modifiche |
| Controllo sui diritti | Magistrato di sorveglianza: approvazione con decreto o restituzione con osservazioni per nuova formulazione |
| Attuazione e verifica | Servizi e operatori competenti: attività, risultati, criticità e aggiornamenti della cartella personale |

Il G.O.T. allargato alimenta l'osservazione e il coordinamento; la decisione collegiale sul programma e il decreto del magistrato non sono sostituiti da un colloquio dell'educatore. La cartella accompagna la persona nei trasferimenti, evitando di ricominciare ogni volta senza la storia del percorso.

**Caso breve.** Dopo quattro mesi emerge che il corso previsto coincide con cure necessarie. L'operatore documenta l'incompatibilità; il gruppo riformula orari e obiettivi e segue il percorso di approvazione delle modifiche. Non si registra «scarsa adesione» attribuendo al detenuto un ostacolo organizzativo del servizio.

'''
assert needle in s;s=s.replace(needle,insert+needle,1)
section('Lavoro penitenziario','''Il lavoro dell'art. 20 O.P. è un elemento del trattamento: non ha carattere afflittivo ed è **remunerato**. Organizzazione e metodi devono avvicinarsi a quelli del lavoro libero, così da costruire competenze spendibili dopo la detenzione. Non va confuso con il lavoro di pubblica utilità gratuito previsto da differenti istituti, come la messa alla prova processuale.

Sono garantiti durata della prestazione entro i limiti di legge, riposo festivo, riposo annuale retribuito e tutela assicurativa e previdenziale. I corsi professionali e i tirocini hanno le tutele previste dalla disciplina applicabile. Detenzione e condanna non cancellano automaticamente i diritti connessi al rapporto di lavoro.

| Profilo | Regola organizzativa |
|---|---|
| Assegnazione | Commissione dell'istituto: elenchi generici e per qualifica |
| Criteri | Disoccupazione maturata durante detenzione, carichi familiari e abilità lavorative; a parità, preferenza prevista per i condannati |
| Sicurezza | Attività riservate e deroghe ammesse dalla legge, con specifica giustificazione |
| Organizzazione | Lavorazioni interne, imprese, enti, cooperative e convenzioni per opportunità interne o esterne |
| Verifica educativa | Competenze acquisite, frequenza, rispetto delle regole e continuità del percorso |

L'amministrazione favorisce lavoro e formazione, ma la funzione educativa non autorizza a promettere un posto inesistente. Una relazione professionale distingue disponibilità effettiva, candidatura e assegnazione. Scrivere «avviato al lavoro» quando esiste soltanto una richiesta falsifica l'andamento del programma.

Il lavoro all'esterno ex art. 21, esaminato più avanti, richiede un titolo specifico; un contratto o la disponibilità dell'impresa non autorizzano da soli l'uscita. Questa distinzione consente di collegare opportunità, provvedimento e verifica senza ridurre il lavoro a una semplice attività per occupare il tempo.''')
section('Ordine, disciplina e sicurezza','''Ordine e sicurezza rendono possibile la vita dell'istituto, ma il potere disciplinare è regolato. Gli artt. 38–41 O.P. richiedono un'infrazione prevista, la contestazione dell'addebito, la possibilità di discolparsi e una decisione motivata. La sanzione considera natura e gravità del fatto, comportamento e condizioni personali; un rapporto di servizio non coincide con una colpevolezza già accertata.

| Sanzione | Limite e autorità |
|---|---|
| Richiamo e ammonizione | Direttore |
| Esclusione da attività ricreative e sportive | Fino a dieci giorni; consiglio di disciplina |
| Isolamento durante la permanenza all'aria aperta | Fino a dieci giorni; consiglio di disciplina |
| Esclusione dalle attività in comune | Fino a quindici giorni; consiglio di disciplina, previo giudizio sanitario di idoneità e controlli durante l'esecuzione |

Il consiglio comprende direttore o delegato, educatore e un esperto dell'art. 80. Le protezioni di legge impediscono l'esecuzione dell'esclusione dalle attività comuni nei confronti delle gestanti, delle puerpere fino a sei mesi e delle madri che allattano fino a un anno. La certificazione sanitaria non serve a decidere se il fatto è avvenuto: riguarda la compatibilità della sanzione con la salute.

La forza fisica è ammessa nei casi indispensabili previsti dall'art. 41, per fronteggiare violenza, impedire evasione o vincere resistenza agli ordini: deve essere immediatamente riferita e comporta gli accertamenti previsti. I mezzi di coercizione non possono essere usati come sanzione disciplinare. Non si aggiunge informalmente una punizione alla sanzione deliberata.

Il detenuto può proporre reclamo disciplinare ai sensi dell'art. 35-bis **entro dieci giorni dalla comunicazione**. Il magistrato controlla competenza e costituzione dell'organo, contestazione e difesa; per isolamento all'aria aperta ed esclusione dalle attività comuni valuta anche il merito. L'eventuale annullamento è un provvedimento giudiziario, non una nuova valutazione dell'operatore che aveva scritto il rapporto.

**Esempio.** Si propone una sanzione perché una persona non ha partecipato a un'attività coincidente con una visita sanitaria documentata. Prima della decisione occorrono contestazione, ascolto e verifica della giustificazione: non basta contare l'assenza come rifiuto del trattamento.''')
section('Misure alternative e benefici','''Le misure alternative modificano il modo di eseguire una pena definitiva; i benefici incidono su aspetti della sua esecuzione. Non sono concessi automaticamente per il solo decorso del tempo. La sequenza di lavoro è: titolo esecutivo, pena da espiare, reato ed eventuali preclusioni, requisiti personali, istruttoria, decisione dell'autorità competente, prescrizioni e controllo.

**Affidamento in prova al servizio sociale — art. 47 O.P.** La persona esegue la pena nella comunità secondo prescrizioni e con sostegno e controllo dell'UEPE. Il limite ordinario è tre anni da espiare; il comma 3-bis consente fino a quattro anni, anche residui, quando almeno nell'ultimo anno il comportamento permette una prognosi favorevole. Il tribunale di sorveglianza valuta che la misura favorisca la rieducazione e prevenga altri reati. Non basta un'offerta di lavoro. Osservazione, domicilio, ambiente e condotta concorrono alla valutazione.

Le prescrizioni possono riguardare dimora, spostamenti, attività, rapporti e impegni riparativi. Il magistrato può modificarle e, nei presupposti di urgenza, disporre applicazione provvisoria in attesa del tribunale. La revoca consegue a condotta incompatibile con la prosecuzione, valutata dal giudice. L'esito positivo estingue la pena detentiva e gli altri effetti penali, salvo le pene accessorie perpetue; il giudice può dichiarare estinta anche la pena pecuniaria nelle condizioni economiche previste. **Non estingue il reato** come la messa alla prova processuale.

**Detenzione domiciliare — art. 47-ter O.P.** La pena si esegue nell'abitazione o negli altri luoghi consentiti, con prescrizioni e controlli. L'uscita richiede il titolo previsto: abitare fuori dall'istituto non equivale a libertà senza vincoli.

| Ipotesi | Condizioni essenziali |
|---|---|
| Comma 1 | Reclusione fino a quattro anni, anche residui, o arresto, per le categorie familiari, sanitarie o di età indicate dalla legge |
| Comma 1-bis | Pena fino a due anni, anche residui, se non ricorrono condizioni per affidamento e la misura previene altri reati; esclusi i reati dell'art. 4-bis |
| Comma 1-ter | Alternativa al rinvio dell'esecuzione nei casi previsti, anche oltre i limiti ordinari; comprende la grave infermità psichica sopravvenuta dopo Corte cost. 99/2019 |

Le categorie del comma 1 comprendono donna incinta o madre convivente con figlio sotto dieci anni; padre convivente quando la madre è morta o assolutamente impossibilitata ad assisterlo; persona con salute particolarmente grave e bisogno di costanti contatti sanitari territoriali; ultrasessantenne anche parzialmente inabile; minore di ventuno anni per comprovate esigenze di salute, studio, lavoro o famiglia. Il comma 01 disciplina separatamente gli ultrasettantenni con specifiche esclusioni. Decide il tribunale, salvi provvedimenti provvisori del magistrato. Non è sufficiente dichiarare un disagio familiare o indicare una qualunque patologia.

**Semilibertà — artt. 48 e 50 O.P.** Consente una parte della giornata fuori dall'istituto per lavoro, studio o altre attività utili al reinserimento, con rientro secondo il programma. Decide il tribunale sulla base dei progressi e delle condizioni del reinserimento.

| Regola temporale | Applicazione |
|---|---|
| Metà della pena | Regola ordinaria |
| Due terzi | Delitti nelle categorie dell'art. 4-bis richiamate dall'art. 50 |
| Venti anni | Ergastolo |
| Arresto o reclusione fino a sei mesi | Possibile ammissione ai sensi del comma 1 quando non si è affidati in prova |

L'art. 50 consente inoltre, nei casi di pena rientrante nel limite dell'art. 47 e fuori dalle esclusioni indicate, l'ammissione prima della metà quando mancano i presupposti dell'affidamento. L'internato può essere ammesso in ogni tempo, nei requisiti previsti. Non si sostituisce questo esame con la formula «basta aver espiato metà pena».

### Liberazione anticipata, permessi premio e lavoro all'esterno

Sono tre istituti differenti: il primo riduce la pena, il secondo permette un'uscita temporanea finalizzata, il terzo organizza un'attività lavorativa esterna.

| Istituto | Contenuto e decisione |
|---|---|
| Liberazione anticipata, art. 54 | Quarantacinque giorni per semestre di pena espiata, con partecipazione all'opera di rieducazione; decide il magistrato di sorveglianza |
| Permesso premio adulti, art. 30-ter | Fino a quindici giorni per volta e quarantacinque complessivi all'anno; decide il magistrato, sentito il direttore |
| Lavoro esterno, art. 21 | Ammissione del direttore, esecutiva per condannati e internati dopo approvazione del magistrato; per imputati occorre autorizzazione giudiziaria |

La liberazione anticipata valuta ogni semestre e considera anche periodi di custodia cautelare e detenzione domiciliare nei presupposti di legge. Due semestri riconosciuti producono novanta giorni di riduzione; la semplice assenza di sanzioni non rende automatico il riconoscimento. La riduzione è computata come pena espiata anche per i benefici indicati dall'art. 54.

Il permesso premio richiede regolare condotta e assenza di pericolosità sociale, per coltivare interessi affettivi, culturali o lavorativi. Per arresto e reclusione fino a quattro anni non è prevista la frazione preliminare ordinaria; oltre quattro anni occorre almeno un quarto della pena. Per i reati dell'art. 4-bis richiamati dall'art. 30-ter occorre almeno metà, con massimo dieci anni; per l'ergastolo almeno dieci anni. Restano le altre condizioni e preclusioni. I limiti qui indicati sono per adulti e non si trasferiscono ai permessi minorili.

Il lavoro esterno resta attività trattamentale, non è di per sé misura alternativa. Per i condannati per i delitti dell'art. 4-bis richiamati dall'art. 21 sono richiesti almeno un terzo della pena e comunque non oltre cinque anni; per l'ergastolo almeno dieci anni. Queste frazioni non dispensano dagli ulteriori requisiti dell'art. 4-bis. Il datore disponibile non può autorizzare l'uscita.

### Reati ostativi: leggere l'art. 4-bis senza automatismi impropri

L'art. 4-bis differenzia l'accesso a lavoro esterno, permessi premio e misure alternative per gruppi di reato; **la liberazione anticipata è esclusa dal divieto generale del comma 1**. Occorre individuare il reato e il comma pertinente, non applicare un'etichetta unica a ogni delitto grave.

Il testo riformato dal D.L. 162/2022, convertito nella L. 199/2022, consente nei casi dei commi 1-bis e 1-bis.1 l'accesso anche in assenza di collaborazione. Sono richiesti adempimento delle obbligazioni civili e riparatorie o assoluta impossibilità e specifici elementi ulteriori rispetto alla buona condotta e alla partecipazione al trattamento. Per i reati associativi indicati si deve escludere sia l'attualità dei collegamenti criminali sia il pericolo di ripristino; il regime per altri delitti considera il contesto criminale secondo il comma applicabile.

Il giudice acquisisce informazioni e pareri, svolge gli accertamenti prescritti e motiva l'esito. Sono previste condizioni ulteriori, fra cui osservazione collegiale della personalità per almeno un anno per i reati del comma 1-quater e valutazione di programmi specifici nei casi del comma 1-quinquies. Il regime speciale dell'art. 41-bis deve essere revocato o non prorogato perché possano essere concessi i benefici del comma 1. Né la mancata collaborazione né una relazione educativa favorevole vanno trasformate, da sole, in una risposta valida per tutti i casi.

### Ordine di esecuzione e domanda dalla libertà

Il PM emette l'ordine di esecuzione; la sospensione dell'art. 656 c.p.p. permette, quando ne ricorrono i presupposti, di presentare domanda di misura alternativa senza ingresso immediato in carcere. Il limite ordinario è **quattro anni** dopo Corte costituzionale n. 41/2018: la parola «tre» ancora presente nel comma 5 non va letta senza la nota della decisione. L'avviso indica il termine di trenta giorni per presentare l'istanza; il PM la trasmette al tribunale di sorveglianza.

La sospensione incontra i divieti del comma 9 e le relative eccezioni: non coincide con la concessione della misura. La disciplina terapeutica degli artt. 90, 94 e 94-ter del D.P.R. 309/1990 prevede percorsi e limiti speciali, distinti dalla soglia ordinaria; il rinvio normativo non permette di attribuire automaticamente otto anni a qualunque richiesta di affidamento. Nei casi dei commi 9-bis e 9-ter interviene inoltre il magistrato per la domiciliare provvisoria di ultrasettantenni con residuo tra due e quattro anni, con le esclusioni previste, o di persone già agli arresti domiciliari per gravissimi motivi di salute.

**Caso breve.** Un condannato libero, con residuo di tre anni e sei mesi e senza impedimenti alla sospensione, riceve ordine e decreto di sospensione. Non è già affidato in prova: deve presentare tempestiva domanda documentata e il tribunale deve valutare il comma 3-bis dell'art. 47. Confondere la soglia per sospendere con i presupposti per concedere elimina un intero passaggio del procedimento.''')
section('Diritti, doveri, Carta e reclami','''La Carta dei diritti e dei doveri orienta la persona all'ingresso: regole dell'istituto, prestazioni, attività, doveri e forme di tutela. Il reclamo amministrativo o la segnalazione al direttore non sostituiscono i rimedi giurisdizionali quando ne ricorrono i presupposti.

**Art. 35-bis O.P.: far cessare una lesione attuale.** Se l'inosservanza delle norme da parte dell'amministrazione provoca un pregiudizio attuale e grave a un diritto, il detenuto o internato può rivolgersi al magistrato di sorveglianza. Accertata la lesione, il giudice ordina all'amministrazione di porvi rimedio entro un termine. Il procedimento assicura contraddittorio e possibilità per l'amministrazione di comparire o presentare osservazioni.

La decisione è reclamabile al tribunale di sorveglianza entro quindici giorni dalla notificazione o comunicazione dell'avviso di deposito; la decisione del tribunale è ricorribile in Cassazione per violazione di legge entro quindici giorni. Se l'ordine definitivo non viene eseguito, si può chiedere ottemperanza: il magistrato indica modalità e tempi, può dichiarare nulli atti elusivi e nominare un commissario ad acta. La stessa procedura tratta i reclami disciplinari, con il distinto termine iniziale di dieci giorni illustrato nella sezione sulla disciplina.

**Art. 35-ter O.P.: compensare condizioni contrarie all'art. 3 CEDU.** Il rimedio riguarda il pregiudizio derivante da condizioni detentive inumane o degradanti secondo i criteri della Corte europea, non qualsiasi disagio o irregolarità.

| Situazione | Rimedio previsto |
|---|---|
| Almeno quindici giorni di pregiudizio e pena residua sufficiente | Riduzione di un giorno di pena ogni dieci giorni di pregiudizio, disposta dal magistrato |
| Pena residua insufficiente | Per la parte non compensabile, otto euro per ogni giorno di pregiudizio |
| Periodo inferiore a quindici giorni | Compensazione monetaria di otto euro per giorno nei presupposti del comma 2 |
| Pena già espiata oppure custodia non computabile nella pena | Azione al tribunale civile del capoluogo del distretto di residenza, entro sei mesi dalla cessazione della detenzione/custodia |

**Confronto.** Una lesione può richiedere subito un ordine di cessazione e, ricorrendone i diversi presupposti, anche una compensazione. Il primo rimedio non assegna automaticamente denaro; il secondo non sostituisce l'intervento per rimuovere una condizione ancora lesiva. Il fascicolo deve distinguere periodo, fatti, prove, situazione attuale e domanda formulata.''')
section('Giurisprudenza costituzionale essenziale','''**Corte costituzionale n. 99/2019 — salute psichica.** Il problema era l'assenza di una risposta extramuraria adeguata alla grave infermità psichica sopravvenuta. La Corte ha ampliato l'art. 47-ter, comma 1-ter: il tribunale di sorveglianza può disporre domiciliare anche oltre i limiti ordinari. Occorrono valutazione clinica, possibilità di cura e considerazione della pericolosità; non segue una scarcerazione automatica per qualsiasi diagnosi.

**Corte costituzionale n. 253/2019 — permessi premio.** La preclusione assoluta per il non collaborante non lasciava spazio a provare il venir meno dei legami criminali. La decisione ha aperto l'accesso ai permessi quando siano esclusi collegamenti attuali e pericolo di ripristino. Non ha abolito l'ergastolo né esteso automaticamente ogni misura. Oggi il caso va risolto anche con il testo riformato dell'art. 4-bis spiegato sopra.

**Corte costituzionale n. 10/2024 — colloqui intimi.** La regola inderogabile del controllo a vista impediva l'espressione dell'affettività con coniuge, parte dell'unione civile o convivente stabile. La Corte ha reso possibile il colloquio senza quel controllo quando non ostino sicurezza, ordine, disciplina o, per l'imputato, ragioni giudiziarie. La decisione non riguarda il regime speciale dell'art. 41-bis e la sorveglianza particolare. L'amministrazione valuta i presupposti e organizza spazi e modalità; il diniego lesivo può essere sottoposto al magistrato con il reclamo dell'art. 35-bis.

**Metodo per l'orale.** Si espongono il problema, la disposizione incisa e l'effetto pratico. Dire soltanto «la Corte tutela la dignità» non spiega quale provvedimento può essere richiesto né chi debba adottarlo.''')
section('Caso guidato: reclamo su condizioni detentive','''**Dati del caso.** Una persona sta ancora espiando una pena sufficientemente lunga. Il fascicolo documenta sessanta giorni di condizioni che il giudice accerta essere contrarie all'art. 3 CEDU; la lesione persiste. Il candidato deve distinguere richiesta urgente di cessazione e compensazione.

**Passo 1 — Ricostruire i fatti.** Si ordinano date, celle occupate, presenze, condizioni materiali e documentazione disponibile, distinguendo allegazioni e accertamenti. Non basta scrivere «istituto sovraffollato» per dimostrare il pregiudizio individuale.

**Passo 2 — Far cessare la lesione.** Per il pregiudizio attuale e grave derivante dall'inosservanza amministrativa si individua il reclamo ex artt. 35-bis e 69, comma 6, al magistrato di sorveglianza. L'ordine giudiziale indica termine e rimedio; l'amministrazione deve documentare l'adempimento, non limitarsi a rispondere di aver ricevuto il reclamo.

**Passo 3 — Compensare il periodo.** Sessanta giorni superano la soglia dei quindici. Con pena residua sufficiente, l'art. 35-ter consente sei giorni di riduzione: 60 ÷ 10 = 6. Non sono quarantacinque giorni per semestre, che appartengono alla liberazione anticipata e richiedono altri presupposti.

**Variante.** Se la persona ha già terminato la pena, non si sottraggono giorni inesistenti: la domanda segue la via civile distrettuale del comma 3, entro sei mesi dalla cessazione, e la compensazione per sessanta giorni accertati è 60 × 8 = 480 euro.

**Output sintetico.** «Distinguerei tutela della lesione attuale e compensazione del periodo pregresso. Verificherei titolo, date e condizioni individuali; nel primo caso individuerei il magistrato di sorveglianza e nel secondo applicherei la disciplina coerente con lo stato detentivo, senza confondere 35-ter e liberazione anticipata».''')
section('Quiz commentato','''**Q1. Quale definizione di internato è corretta in questo capitolo?**

A) Persona sottoposta a misura di sicurezza detentiva.
B) Qualunque persona sottoposta a libertà vigilata.
C) Qualunque imputato detenuto in attesa di giudizio.
D) Ogni condannato a reclusione definitiva.

**Risposta A.** Il riferimento è alla misura di sicurezza detentiva. B estende il termine a misura non detentiva; C e D confondono custodia cautelare, pena e misura di sicurezza.

**Q2. Chi approva il programma di trattamento formulato dal gruppo presieduto dal direttore?**

A) Il PM che ha sostenuto l'accusa.
B) L'UEPE, senza altri provvedimenti.
C) Il consiglio di disciplina.
D) Il magistrato di sorveglianza, che può restituirlo con osservazioni se viola diritti.

**Risposta D.** L'art. 69, comma 5, distingue formulazione e approvazione. A, B e C attribuiscono l'atto ad autorità con funzioni diverse.

**Q3. Un condannato ha tre anni e sei mesi residui e un'offerta lavorativa. Che cosa si può concludere sull'affidamento?**

A) È automaticamente concesso dal direttore.
B) Può essere valutato nell'art. 47, comma 3-bis, con gli altri requisiti e decisione del tribunale.
C) È sempre escluso perché supera tre anni.
D) Estingue subito il reato alla presentazione della domanda.

**Risposta B.** Il comma 3-bis arriva a quattro anni, ma richiede comportamento e prognosi favorevoli. A scambia autorità e automatismo, C ignora il comma pertinente, D confonde domanda, esito e oggetto dell'effetto.

**Q4. Sono accertati sessanta giorni di detenzione contraria all'art. 3 CEDU, con pena residua sufficiente. Qual è la compensazione dell'art. 35-ter?**

A) Quarantacinque giorni di riduzione.
B) Sei mesi di sospensione del processo.
C) Sei giorni di riduzione.
D) Sessanta giorni di riduzione.

**Risposta C.** Si applica il rapporto un giorno ogni dieci: 60 ÷ 10 = 6. A usa la liberazione anticipata; B introduce un istituto processuale estraneo; D applica un rapporto uno a uno inesistente.

**Q5. Quale affermazione sulla Corte costituzionale n. 253/2019 è corretta?**

A) Ha eliminato ogni condizione per i benefici dei non collaboranti.
B) Ha abolito l'ergastolo in ogni sua forma.
C) Ha attribuito al direttore la concessione dei permessi premio.
D) Ha consentito permessi premio senza collaborazione nei presupposti indicati, senza concessione automatica.

**Risposta D.** La decisione concerne permessi e valutazione dei collegamenti criminali; va coordinata con l'art. 4-bis vigente. A, B e C estendono il dispositivo a effetti che non contiene.

**Q6. Una lesione grave e attuale di un diritto deriva dall'inosservanza amministrativa. Quale rimedio mira a farla cessare?**

A) Il reclamo ex art. 35-bis al magistrato di sorveglianza.
B) Soltanto la domanda monetaria ex art. 35-ter al giudice civile.
C) La messa alla prova processuale.
D) La liberazione anticipata concessa dal direttore.

**Risposta A.** Il magistrato può ordinare di rimediare al pregiudizio. B confonde tutela attuale e compensazione; C riguarda un processo pendente; D sbaglia funzione e autorità.''')
s=s.replace('| Si |','| Sì |')
s=s.replace('source_refs: [','source_refs: [\n  "sources/vol-04-minorile-penitenziario-verifica-2026-10-03.md",',1)
s=s.replace('topics: [','topics: ["topics/giustizia-minorile-e-penitenziaria-m-fc04.md", ',1)
s=s.replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/sources/vol-04-minorile-penitenziario-verifica-2026-10-03.md",\n  "wiki/topics/giustizia-minorile-e-penitenziaria-m-fc04.md",',1)
s=re.sub(r'updated_at: .*','updated_at: 2026-10-03',s,count=1)
p.write_text(s,encoding='utf8')
print(json.dumps({'file':p.as_posix(),'before':hashlib.sha256(before.encode()).hexdigest(),'after':hashlib.sha256(s.encode()).hexdigest(),'words':len(s.split())},indent=2))
