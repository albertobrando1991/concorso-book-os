from pathlib import Path
import re,json,shutil
base=Path('wiki/books/moduli/m-fl04-polizia-locale/chapters'); art=Path('artifacts/correzioni-collana-2026-10-02')
def get(n):
 p=next(base.glob(n+'-*.md')); b=art/'before-fl04'/p.name
 if b.exists(): raise RuntimeError('Backup già esistente: '+n)
 shutil.copy2(p,b); return p,p.read_text(encoding='utf-8')
def add(t,a,b):
 assert t.count(a)==1,a
 return t.replace(a,b.strip()+'\n\n'+a)
def save(p,t):
 source='sources/vol-02-pl-sinistri-turni-verifica-2026-10-03'
 for k,v in [('source_refs',source),('last_compiled_from','wiki/'+source+'.md')]:t=re.sub(r'^'+k+r': \[(.*)\]$',lambda m:k+': ['+m.group(1)+', "'+v+'"]',t,count=1,flags=re.M)
 t=re.sub(r'^volume_chapter:.*$','volume_chapter: '+str(34+int(p.name[:2])),t,flags=re.M)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
 p.write_text(t,encoding='utf-8')
p,t=get('13')
t=add(t,'## N-FL04-13-03', '''### Rilievo metrico risolto: coordinate e croquis

**Scenario didattico fittizio.** Dopo soccorso e messa in sicurezza, la pattuglia rileva un tratto rettilineo largo 6,00 metri. Nessun mezzo viene spostato durante queste misure. Il caposaldo O è lo spigolo sud-ovest di un manufatto stabile, fotografato nell'immagine F01; l'asse x segue il margine sud della carreggiata verso est e l'asse y è perpendicolare, verso nord. Le coordinate sono espresse in metri: x è la distanza lungo il riferimento, y lo scostamento ortogonale.

| Punto | Elemento osservato | x | y |
|---|---|---:|---:|
| O | Caposaldo stabile | 0,00 | 0,00 |
| A | Centro ruota anteriore sinistra del veicolo 1 in quiete | 8,00 | 2,00 |
| B | Centro ruota posteriore sinistra del medesimo veicolo | 5,50 | 2,00 |
| C | Estremo ovest di una traccia rettilinea osservata | 3,00 | 4,00 |
| D | Estremo est della stessa traccia | 7,00 | 4,00 |

**Croquis orientativo, non in scala.** Il disegno localizza i punti; le quote valide sono quelle della tabella, non le distanze sulla pagina.

```text
                    NORD / y
                       ↑
Margine nord    y = 6,00 m
                  C────D     traccia
                    B───A    ruote V1
O────────────────────────→ EST / x
Margine sud     y = 0,00 m
```

**Lettura e controllo.** La traccia C–D misura 7,00 − 3,00 = 4,00 metri. La distanza A–B è 8,00 − 5,50 = 2,50 metri. I punti hanno ordinate comprese fra 0 e 6,00 metri e ricadono quindi entro la carreggiata dello schema. Per verificare A con una misura indipendente si può confrontare la distanza diretta O–A con √(8² + 2²), circa 8,25 metri: lo scarto va valutato rispetto a metodo, strumento e precisione dichiarati, senza correggere artificiosamente le misure per farle coincidere.

La relazione collega A e B alle foto F02–F03 e C/D a F04. Scrive «traccia osservata» finché non è accertata la natura del segno; non inventa una frenata del veicolo 1. Due punti sulle ruote aiutano a rappresentare l'orientamento del mezzo, ma non descrivono tutto l'ingombro: per il disegno completo servono ulteriori punti e dimensioni rilevate.

Il conducente dichiara che l'urto sia avvenuto prima della posizione A. Questo è un **dato dichiarato** da registrare separatamente; A è una posizione di quiete **misurata**. La tabella non identifica il punto d'urto e non permette da sola di calcolare velocità, precedenza violata o responsabilità. È proprio questa distinzione che rende il rilievo utilizzabile nel successivo accertamento.
''')
t=add(t,'### Caso guidato: motociclista ferito e versioni discordanti', '''### Lesioni, omicidio stradale e obblighi dopo il sinistro

Gli artt. **589-bis e 590-bis c.p.** richiedono un evento, una condotta colposa in violazione delle norme stradali e il collegamento causale fra condotta ed evento. Il primo riguarda la morte; il secondo le lesioni **gravi o gravissime**. La presenza di un ferito non basta per affermare il secondo reato e la pattuglia non sostituisce la valutazione medico-legale della gravità con una propria diagnosi.

L'omicidio stradale nella forma base è punito con reclusione da due a sette anni. Le aggravanti dei due articoli dipendono da presupposti precisi: fasce alcolemiche e qualità del conducente, stato di alterazione psicofisica da stupefacenti, determinate velocità o manovre, e altre condizioni indicate dalla legge. Per le lesioni dell'art. 590-bis, in assenza delle aggravanti previste, la procedibilità è a querela; non si estende questa regola alle ipotesi aggravate.

**Attenzione al raccordo con l'art. 187 CdS.** Dopo la riforma e la sentenza costituzionale n. 10/2026, il reato di guida dopo assunzione ha i presupposti spiegati nel capitolo «Servizi di polizia stradale». Le aggravanti degli artt. 589-bis e 590-bis conservano invece il requisito dello stato di alterazione psicofisica. Una positività, da sola, non dimostra automaticamente quella specifica aggravante né il nesso causale con il sinistro.

**Caso penale risolto.** La traccia dà per acquisiti questi elementi: un automobilista passa col rosso; le riprese mostrano la collisione causalmente collegata alla violazione; la documentazione sanitaria qualifica la lesione come grave; non risultano alcol o stupefacenti. Il fatto è da riferire al PM come possibile lesione stradale aggravata ai sensi dell'art. 590-bis, perché il passaggio col rosso è una delle manovre tipizzate dalla norma. Non si attende una querela invocando la regola della forma non aggravata. Si documentano filmato e sua provenienza, segnaletica, rilievi, certificazione acquisita, identificazioni e tempi della conoscenza del fatto; dichiarazioni e atti seguono le garanzie proprie della qualità assunta dai soggetti. L'assenza di alcol non esclude l'aggravante della manovra.

**Variante.** Se la traccia esclude tutte le aggravanti dell'art. 590-bis e descrive una diversa violazione colposa causalmente collegata alla lesione grave, si considera la procedibilità a querela; restano le attività consentite prima della condizione di procedibilità e la tutela delle fonti. Se invece sopravviene il decesso collegato alle lesioni, si aggiorna tempestivamente la notizia e si valuta l'art. 589-bis, conservando la cronologia delle informazioni.

L'art. **189 CdS** distingue, infine, fermarsi e prestare assistenza: lasciare i dati non equivale a soccorrere chi ne ha bisogno. Il mancato arresto dopo un incidente con soli danni alle cose ha disciplina amministrativa; in presenza di danni alle persone, la fuga e l'omessa assistenza possono integrare i distinti reati previsti. Occorre accertare i presupposti di ciascuna condotta, senza dedurre ogni responsabilità dal solo allontanamento narrato da un presente.
''')
t=t.replace('C. riportata senza indicare quando è stata raccolta.','C. riportata senza indicare quando è stata raccolta;').replace('D. attribuita al soggetto e distinta dalle osservazioni della pattuglia;','D. attribuita al soggetto e distinta dalle osservazioni della pattuglia.')
t=t.replace('- Codice di procedura penale, artt. 347 e 357,', '- Codice penale, artt. 589-bis e 590-bis; Corte costituzionale, sentenza n. 10/2026.\n- Codice di procedura penale, artt. 347 e 357,')
save(p,t)
p,t=get('14')
t=add(t,'## N-FL04-14-02', '''### Il rapporto fra comandante e sindaco

L'art. 9 L. 65/1986 rende il comandante responsabile verso il sindaco per **addestramento, disciplina e impiego tecnico-operativo** degli appartenenti al Corpo. È una relazione specifica di responsabilità organizzativa. Non trasforma il sindaco nel titolare di ogni atto gestionale e non elimina, quando si svolge attività di PG, la dipendenza funzionale dall'autorità giudiziaria.

**Esempio.** Il sindaco indica la priorità di migliorare la sicurezza degli accessi scolastici. Il comandante organizza servizi, addestramento e controllo dell'impiego; gli atti di viabilità e gestione sono adottati dai soggetti competenti secondo legge e assetto comunale. Se durante il servizio emerge un reato, gli adempimenti verso il PM seguono il c.p.p.: la comunicazione non è subordinata al consenso politico.
''')
t=add(t,'## N-FL04-14-04', '''### Orario e riposi: le regole contrattuali da applicare

Il CCNL Comparto Funzioni Locali del **23 febbraio 2026**, artt. 22–26, offre regole concrete. La sperimentazione delle **36 ore su quattro giorni** richiede confronto, volontarietà e salvaguardia dei servizi: non autorizza il singolo a scegliere liberamente quattro giorni. L'orario multiperiodale concentra e riduce le prestazioni secondo una programmazione, con periodi normalmente non superiori a tredici settimane ciascuno; non consiste nell'accumulare indefinitamente ore da recuperare.

Per la **turnazione** dell'art. 25 occorrono rotazione effettiva e articolazioni giornaliere prestabilite. Il calendario distribuisce in modo equilibrato e avvicendato i turni nel mese; la mera presenza pomeridiana non dimostra da sola il relativo istituto. Il servizio giornaliero cui si riferiscono le prestazioni diurne in turnazione deve durare almeno dieci ore. La sovrapposizione è limitata alle consegne e alle esigenze impreviste considerate dalla clausola.

| Regola contrattuale | Conseguenza organizzativa |
|---|---|
| Almeno 11 ore consecutive di riposo ogni 24 | Controllare fine di un turno e inizio del successivo, non solo il totale settimanale |
| Fascia notturna 22–6 | Classificare le ore effettivamente prestate nella fascia |
| Di norma non oltre dieci turni notturni al mese | Le eccezioni richiedono i presupposti contrattuali o la disciplina integrativa ammessa |
| Equilibrio e rotazione mensili | Evitare assegnazioni ricorrenti immotivate e rispettare le tutele personali applicabili |
| Indennità per effettiva prestazione in turno | Non attribuirla per la sola appartenenza al servizio |

Il D.Lgs. 66/2003 contiene la disciplina generale dell'orario, ma l'art. 2, comma 3, esclude gli addetti alla polizia municipale e provinciale **in relazione alle attività operative specificamente istituzionali**. Perciò non si applicano automaticamente tutti i suoi limiti a qualsiasi servizio PL e, all'opposto, non si ricava dall'esclusione la libertà di ignorare il CCNL. Si individua l'attività concreta e si applicano le clausole contrattuali e le ulteriori fonti pertinenti.

L'art. 26 del CCNL regola il mancato riposo settimanale per particolari esigenze di servizio: oltre alla maggiorazione prevista, spetta un riposo compensativo di almeno 24 ore consecutive, normalmente entro quindici giorni e comunque entro il bimestre successivo. È una fattispecie diversa dal lavoro festivo infrasettimanale o dal sabato normalmente non lavorativo; un prospetto paga non può sommare trattamenti incompatibili soltanto perché il servizio cade in un giorno festivo.

**Caso risolto.** Per un agente turnista si propongono sabato 16–24 e domenica 7–13. Fra i due servizi ci sono sette ore: il piano non rispetta le undici ore contrattuali. Una correzione è assegnare il secondo servizio a un altro operatore che abbia riposo e competenze adeguati; un'altra è differire l'inizio almeno alle 11, se copertura e durata del servizio lo consentono. Scrivere «evento importante» non sana da solo la pianificazione. Occorre controllare anche tutte le altre assegnazioni, le tutele e il riposo settimanale: il calcolo di questo intervallo non certifica l'intero calendario.
''')
start=t.index('### Quiz 1',t.index('## ▣ Verifica'));end=t.index('### Caso ragionato finale',start)
quiz='''### Quiz 1

**La qualifica di ufficiale di PG comporta automaticamente il comando del Corpo?**

A. Sì, se il dipendente appartiene all'area dei funzionari.

B. Sì, in assenza di un dirigente assegnato al servizio.

C. No: qualifica operativa e incarico organizzativo hanno fonti distinte.

D. Sì, ma soltanto per la durata dell'atto di PG.

**Risposta corretta: C.** La funzione di PG non attribuisce da sola l'incarico di comando, neppure temporaneamente.

### Quiz 2

**Verso chi risponde il comandante per addestramento, disciplina e impiego tecnico-operativo ai sensi dell'art. 9 L. 65/1986?**

A. Verso il sindaco.

B. Verso il prefetto per tutte e tre le funzioni.

C. Verso il consiglio comunale, che approva ogni ordine.

D. Verso il PM anche per la turnazione ordinaria.

**Risposta corretta: A.** La responsabilità verso il sindaco coesiste con gli altri rapporti funzionali previsti dalle rispettive discipline.

### Quiz 3

**A un turnista soggetto all'art. 25 CCNL si assegnano 16–24 e, il giorno seguente, 7–13. Quale rilievo è fondato?**

A. Sono sette ore di riposo e il calendario non rispetta le undici ore contrattuali.

B. La pausa è sufficiente perché ciascun turno non supera otto ore.

C. La pausa è sufficiente se non si superano 36 ore nella settimana.

D. Il limite riguarda esclusivamente le ore comprese fra 22 e 6.

**Risposta corretta: A.** Durata del singolo turno, totale settimanale e intervallo di riposo sono controlli distinti.

### Quiz 4

**La settimana di 36 ore su quattro giorni prevista dall'art. 22 CCNL 2026 è:**

A. obbligatoria per ogni Corpo con servizio serale.

B. liberamente scelta dal lavoratore senza confronto organizzativo.

C. una riduzione automatica a 32 ore senza perdita retributiva.

D. una sperimentazione volontaria alle condizioni contrattuali, preservando i servizi.

**Risposta corretta: D.** Restano 36 ore e servono i presupposti organizzativi e le relazioni sindacali indicati dal contratto.

### Quiz 5

**L'esclusione dell'art. 2 D.Lgs. 66/2003 per attività operative specificamente istituzionali della PL:**

A. impone di distinguere l'ambito legislativo dalle regole contrattuali applicabili.

B. elimina anche ogni riposo previsto dal CCNL.

C. si applica indistintamente a tutti i dipendenti comunali.

D. consente al comandante di sospendere il contratto con ordine di servizio.

**Risposta corretta: A.** Un'esclusione di ambito non abroga le tutele contrattuali del personale.

### Quiz 6

**Per una notizia di reato emersa durante il servizio scolastico occorre:**

A. attendere la validazione del sindaco prima della CNR.

B. sostituire la CNR con la relazione di fine turno.

C. attendere il riepilogo mensile del comando.

D. adempiere verso il PM secondo il c.p.p., rispettando termini e garanzie.

**Risposta corretta: D.** Il rapporto organizzativo comandante-sindaco non subordina gli obblighi di PG a un'autorizzazione politica.

'''
t=t[:start]+quiz+t[end:]
save(p,t)
p=next(base.glob('11-*.md'));t=p.read_text(encoding='utf-8').replace('Urbanistica, edilizia ed espropriazioni','Urbanistica e governo del territorio');p.write_text(t,encoding='utf-8')
sp=art/'VOL-02-changes.json';s=json.loads(sp.read_text(encoding='utf-8'))
for fid,n,c,e in [('V02-50','13','Rilievo metrico con croquis, coordinate e controlli; lesioni/omicidio e caso penale aggravato risolto.','Art189, CP589bis/590bis integralmente letti; distinte fonti misurate/dichiarate, querela/aggravanti e art187.'),('V02-51','14','Regole CCNL23feb2026, turni/riposi, art9L65; sei quiz sostituiti con distrattori plausibili.','CCNL22–26 letti; D662/4/7/8/9; caso intervallo7ore e correzione11; distinta esclusione attività operative.')]:s['changes'][fid]={'files':[next(base.glob(n+'-*.md')).as_posix()],'change':c,'evidence':e,'status':'Applicato; riesame trasversale e gate 15 ancora aperti'}
sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('FL04/13–14 applicati; rinvio VOL10 corretto')
