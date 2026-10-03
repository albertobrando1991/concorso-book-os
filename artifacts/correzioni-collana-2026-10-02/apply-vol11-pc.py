from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile/chapters'); S='sources/vol-11-protezione-civile-verifica-2026-10-03'
def add(t,n,c,x):
 return re.sub(rf'(^## N-TR04-{n:02d}-{c:02d}[^\n]*\n)',lambda m:m[1]+'\n'+x.strip()+'\n\n',t,count=1,flags=re.M)
def save(p,t):
 for key,val in [('source_refs',S),('last_compiled_from','wiki/'+S+'.md'),('topics','topics/ambiente-rettifiche-2026')]:
  m=re.search(r'^'+key+r': (\[.*\])$',t,re.M);a=json.loads(m[1]);a.append(val) if val not in a else None;t=t[:m.start(1)]+json.dumps(a,ensure_ascii=False)+t[m.end(1):]
 for k,v in [('updated_at','2026-10-03'),('review_required','true'),('draft_stage','revision-in-progress')]:t=re.sub(r'^'+k+r': .*$',k+': '+v,t,flags=re.M)
 p.write_text(t,encoding='utf8')
p=next(B.glob('10-*.md'));t=p.read_text(encoding='utf8')
t=t.replace("Il **Prefetto**, in raccordo", "Negli eventi dell'art. 7, comma 1, lettere **b) e c)**, oppure nella loro imminenza o quando siano preannunciati secondo l'allertamento, il **Prefetto**, in raccordo")
t=add(t,10,3,'''### Centri e direzione tecnica

Il **CCS**, Centro coordinamento soccorsi, organizza il raccordo provinciale presso la Prefettura; il **COM**, Centro operativo misto, è una struttura decentrata di raccordo sul territorio secondo il modello applicabile. Gli indirizzi di pianificazione del 2021 prevedono anche centri di coordinamento d'ambito, raccordati all'organizzazione regionale: il piano deve esplicitare quale assetto opera, senza sommare sigle come se fossero autorità concorrenti. La **DiComaC**, Direzione di comando e controllo, è una struttura nazionale di coordinamento sul territorio attivata per le esigenze dell'emergenza; non è il normale ufficio comunale.

Il COC resta il centro operativo comunale. Il coordinamento generale non trasferisce al Sindaco o al Prefetto la direzione tecnica di ogni intervento specialistico: il soccorso tecnico urgente mantiene le competenze del Corpo nazionale dei vigili del fuoco; assistenza sanitaria e ordine pubblico seguono le rispettive catene, raccordate nei centri. **Caso:** tre Comuni chiedono pompe e mezzi. Il raccordo provinciale ordina i fabbisogni e l'assegnazione; il responsabile tecnico dei soccorsi determina l'impiego tecnico sicuro. Il COC aggiorna accessi, persone fragili e assistenza locale.''')
t=add(t,10,5,'''### Tre aree con funzioni diverse

Le **aree di attesa** accolgono inizialmente la popolazione, forniscono informazioni e primi interventi; devono essere raggiungibili lungo percorsi sicuri e riconoscibili. Le **aree di assistenza** ospitano chi deve lasciare l'abitazione, con sistemazioni e servizi adeguati alla durata e alle necessità. Le **aree di ammassamento** servono invece a soccorritori e risorse: richiedono accessibilità logistica, spazi di manovra e collegamenti. Un parcheggio non è automaticamente idoneo a tutte e tre le funzioni.

Per ciascuna area il piano registra rischio del sito e degli accessi, capienza verificata, disponibilità, servizi, responsabile e alternativa. Nel caso di Vallechiara la piazza alta è area di attesa; la palestra verificata è struttura di assistenza; il piazzale logistico fuori dall'area esondabile ospita mezzi e soccorritori. La scelta è didattica: non attribuisce idoneità reale a una struttura senza verifiche. Il Consiglio comunale approva il piano ai sensi dell'art. 12; la deliberazione disciplina revisioni e aggiornamenti, che possono essere demandati agli organi o uffici previsti, e diffusione ai cittadini.''')
t=add(t,10,6,'''### Volontariato: attivazione e benefici

I benefici degli artt. 39–40 del Codice presuppongono volontariato organizzato iscritto e **attivazione autorizzata** dal soggetto competente. L'invio spontaneo sul posto non equivale all'attivazione. Per l'impiego operativo, l'art. 39 tutela posto di lavoro, trattamento economico e previdenziale e copertura assicurativa nei limiti previsti: ordinariamente fino a **30 giorni continuativi e 90 annui**; nelle emergenze nazionali, previa autorizzazione, fino a **60 continuativi e 180 annui**. Per pianificazione, addestramento e formazione autorizzati il riferimento è **10 continuativi e 30 annui**.

L'art. 40 regola i rimborsi delle spese autorizzate e documentate; le richieste vanno presentate al soggetto che ha disposto l'attivazione entro **due anni dalla conclusione dell'intervento o attività**. Non è un rimborso automatico di qualsiasi acquisto. Il registro deve conservare attivazione, presenza, mansione, giornate, autorizzazione di spesa e giustificativi. Un'esercitazione di dodici giorni consecutivi non rientra tutta nel limite ordinario di dieci per formazione: occorre verificare il regime effettivamente applicabile, senza estendere i limiti dell'emergenza a un'attività formativa.''')
save(p,t)
p=next(B.glob('11-*.md'));t=p.read_text(encoding='utf8')
t=t.replace('il sistema opera al massimo livello previsto dalle procedure applicabili','si attiva almeno la fase di preallarme, con eventuale innalzamento secondo scenario e piano')
t=t.replace("Un'allerta rossa richiede le massime attivazioni previste.","Le indicazioni nazionali del 10 febbraio 2016 fissano almeno **attenzione per giallo e arancione**, almeno **preallarme per rosso**. La fase può essere più elevata in base a piano, vulnerabilità e osservazioni; rosso non equivale automaticamente al massimo livello di attivazione.")
t=t.replace('Dato operativo · IT-alert al 17 agosto 2026','Dato operativo · IT-alert al 3 ottobre 2026').replace('stato nazionale verificato il 17 agosto 2026; da ricontrollare al text freeze','stato nazionale verificato il 3 ottobre 2026').replace("**Area dell'audit automatico:**","**Uso del dato:**")
t=add(t,11,1,'''### Il fenomeno cambia la catena di previsione e risposta

**Sisma.** Le reti localizzano e stimano i terremoti; la pericolosità descrive probabilità, non una previsione certa di data, luogo e magnitudo. Si lavora prima su edifici, vie sicure e piani, poi su ricognizione, soccorso e assistenza. Non esiste un bollettino meteo capace di annunciare il singolo terremoto.

**Vulcano.** Monitoraggio e scenari aiutano a valutare l'evoluzione, con incertezze proprie del sistema; livelli di allerta e fasi operative seguono piani specifici. Non si trasferiscono automaticamente le correlazioni dei colori meteo a Vesuvio, Campi Flegrei o altre aree vulcaniche.

**Maremoto da sisma.** Nel SiAM l'INGV, attraverso il CAT, elabora la valutazione scientifica; ISPRA fornisce i dati mareografici; il Dipartimento distribuisce i messaggi. Tempi di propagazione e prossimità della sorgente possono lasciare pochissimo preavviso. Il sistema non predice il sisma né copre senza limiti ogni possibile causa di maremoto.

**Incendio boschivo e di interfaccia.** Previsione del pericolo e piano regionale antincendio orientano prevenzione e risposta; nell'interfaccia l'esposizione di persone ed edifici richiede raccordo fra lotta attiva, soccorso tecnico, viabilità e protezione civile. Il dato di pericolosità non descrive da solo direzione e velocità di un incendio già in atto.

**Incidente industriale.** Per gli stabilimenti Seveso di soglia superiore il gestore predispone il **PEI**, piano di emergenza interna, ai sensi dell'art. 20 del D.Lgs. 105/2015. Per quelli di soglia inferiore la gestione interna segue le procedure del sistema di gestione della sicurezza. Il **PEE**, piano di emergenza esterna dell'art. 21, compete al Prefetto d'intesa con Regione ed enti locali, sentito il CTR e consultata la popolazione, per entrambe le soglie, salva la motivata ipotesi normativa di mancata predisposizione. PEI e PEE si raccordano ma non si sostituiscono; riesame, sperimentazione e aggiornamento necessario avvengono a intervalli non superiori a tre anni. Il Comune assicura il proprio contributo e l'informazione, senza redigere al posto del gestore il PEI.''')
a=t.index('| Ora/fonte | Fatto |');b=t.index('\n### Briefing modello',a)
t=t[:a]+'''| Ramo e ora | Dato e validità | Decisione motivata | Responsabile e verifica |
|---|---|---|---|
| A, 13:10 | Previsione regionale Z-4, valida 18:00–12:00 di domani | Preparare presidi e attivare la fase del piano prima dell'inizio della validità | Responsabile comunale; controllo reperibilità e successivo aggiornamento |
| A, 15:20 | Ruscellamento osservato e verificato, prima delle 18:00 | Agire sul fatto attuale, rafforzare presidio e controllare percorso alternativo | Funzione tecnica; fotografia localizzata e riscontro ogni 30 minuti |
| A, 15:35 | Autonomia RSA ridotta, causa non attribuita al meteo | Verificare assistenza e supporto elettrico compatibile | Raccordo sanitario e gestore; autonomia residua e soluzione registrate |
| B, 10:12 | Messaggio per incidente industriale, scenario alternativo | Applicare il PEE e le indicazioni ufficiali; comunicazione ridondante | Autorità e funzioni previste dal piano; riscontro aree e persone fragili |

I rami **A e B sono alternativi**, non una cronologia unica. Nel ramo A la validità della previsione comincia alle 18:00: alle 15:20 l'azione trova fondamento anche nel fatto già osservato. La preparazione può iniziare prima della finestra prevista, e una misura necessaria non attende che l'orologio entri in quella finestra. Nel briefing delle 16:00 si scrive quindi «allerta valida **dalle 18:00** alle 12:00 di domani; ruscellamento già osservato alle 15:20».
''' +t[b:]
t=t.replace('allerta arancione idrogeologica valida fino alle 12:00 di domani.','allerta arancione idrogeologica valida dalle 18:00 alle 12:00 di domani; ruscellamento già osservato alle 15:20.')
save(p,t)
print('Capitoli 10–11 aggiornati; fonte consolidata e successivi gate richiesti.')
