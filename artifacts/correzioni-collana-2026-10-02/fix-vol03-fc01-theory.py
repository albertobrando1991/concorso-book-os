from pathlib import Path
import re,shutil
B=Path('wiki/books/moduli/m-fc01-ministeri/chapters');A=Path('artifacts/correzioni-collana-2026-10-02/before-text/VOL-03')
for p in B.glob('*.md'):
 dest=A/('FC01-'+p.name)
 if not dest.exists():shutil.copy2(p,dest)
def edit(n,fn):
 p=next(B.glob(n+'-*.md'));s=p.read_text(encoding='utf8');s=fn(s)
 fm,body=s.split('---',2)[1:];fm=re.sub(r'^status:.*$','status: revised_draft',fm,flags=re.M);fm=re.sub(r'^draft_stage:.*$','draft_stage: revision-in-progress',fm,flags=re.M);fm=re.sub(r'^review_required:.*$','review_required: true',fm,flags=re.M);fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
 fm=fm.replace('source_refs: [','source_refs: ["sources/ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md", ',1)
 fm=fm.replace('"text-frozen"','"revision-in-progress"')
 p.write_text('---'+fm+'---'+body,encoding='utf8')
def add(s,anchor,t):
 assert anchor in s,anchor
 return s.replace(anchor,t+'\n\n'+anchor,1)
areas='''### Le quattro aree delle Funzioni Centrali

L'ordinamento introdotto dal CCNL 9 maggio 2022 distingue quattro aree. I successivi rinnovi, compreso il contratto definitivo 2025–2027 del 6 agosto 2026, vanno letti insieme alle disposizioni precedenti rimaste applicabili. Le aree non corrispondono a quattro materie d'esame: descrivono livelli di competenza e responsabilità.

| Area | Attività e responsabilità essenziali | Requisito di base per l'accesso |
| --- | --- | --- |
| Operatori | Supporto ai processi e ai servizi, compiti semplici e problemi di routine | Assolvimento dell'obbligo scolastico |
| Assistenti | Fasi o processi entro direttive generali e procedure, problemi di media complessità, responsabilità sul risultato assegnato | Diploma di scuola secondaria di secondo grado |
| Funzionari | Conoscenze specialistiche, processi complessi, autonomia organizzativa e responsabilità amministrativa e di risultato | Laurea triennale o magistrale |
| Elevate professionalità | Funzioni altamente specialistiche oppure coordinamento di processi articolati di particolare responsabilità | Laurea magistrale, normalmente con esperienza pluriennale pertinente; eventuale iscrizione professionale |

La tabella riassume l'allegato A al CCNL: il bando specifica le classi di laurea, gli ulteriori requisiti ammessi e le competenze del posto. Le elevate professionalità appartengono al personale non dirigente; l'elevata autonomia non attribuisce da sola tutti i poteri di un dirigente. Le regole dell'area non si trasferiscono automaticamente al comparto autonomo PCM.

**Caso breve.** Due concorsi richiedono rispettivamente diploma e laurea e prevedono attività contabili. Non basta dire che sono «lo stesso profilo»: confronta Assistenti e Funzionari, responsabilità e complessità delle attività. La materia può coincidere, mentre profondità della prova e autonomia attesa differiscono.'''
edit('03',lambda s:add(s,'### Profilo, competenze e mansioni',areas))
def pcm(s):
 start=s.index('Il Segretario generale è un riferimento centrale');end=s.index('## Un assetto che va verificato',start)
 return s[:start]+'''Il Segretario generale risponde del funzionamento del Segretariato generale e della gestione delle risorse umane e strumentali della Presidenza. L'art. 7 del D.Lgs. 303/1999 distingue questa responsabilità da quella dei funzionari preposti alle strutture affidate a Ministri o Sottosegretari delegati. Nell'ambito delle rispettive competenze, vengono definiti organizzazione interna, parametri funzionali e obiettivi di gestione e di risultato. Non si tratta di direzione politica del Governo, che resta al Presidente e agli organi costituzionalmente competenti.

L'art. 8 riconosce alla Presidenza autonomia contabile e di bilancio: gestione delle spese entro le disponibilità assegnate, con struttura dei bilanci e regole di gestione definite da decreti del Presidente nel quadro dei principi di contabilità pubblica. Autonomia non significa assenza di limiti finanziari o controlli.

### Strutture di missione

Il Presidente può istituire con decreto strutture per compiti particolari, risultati determinati o programmi specifici. L'atto ne precisa la durata temporanea, che secondo l'art. 7, comma 4, non può superare quella del Governo che le ha istituite. Non vanno confuse con strutture permanenti né con unità disciplinate da leggi speciali, delle quali va verificata la specifica durata.

**Caso breve.** Una struttura di missione è prevista per un obiettivo biennale; il Governo istitutore termina prima del biennio. Non basta il termine numerico per presumere la prosecuzione: occorre applicare il limite legale e verificare l'eventuale nuovo titolo istitutivo. La denominazione immutata sul sito non prova da sola la continuità giuridica.

'''+s[end:]
edit('05',pcm)
edit('06',lambda s:add(s,'### Confronto essenziale','''### Il Segretario generale nei due modelli

Gli artt. 3 e 6 del D.Lgs. 300/1999 fissano una distinzione precisa. Se le strutture di primo livello sono **dipartimenti**, non può essere istituita la figura del Segretario generale. Se sono **direzioni generali**, il Segretario generale può essere previsto: opera alle dirette dipendenze del ministro, cura l'istruttoria degli indirizzi e dei programmi ministeriali, coordina uffici e attività, vigila su efficienza e rendimento e riferisce al ministro. «Può» non equivale a presenza obbligatoria in qualsiasi Ministero.

Nel modello dipartimentale il capo dipartimento assicura invece direzione, coordinamento e controllo degli uffici del proprio dipartimento ed è responsabile dei risultati complessivi, secondo l'art. 5. I poteri gestionali restano distribuiti dalle fonti: il coordinamento non assorbe ogni atto dei dirigenti.

**Verifica.** Un organigramma didattico colloca insieme dipartimenti di primo livello e un Segretario generale ministeriale. È coerente con il modello generale? No: l'art. 3 esclude quella compresenza. Prima di invocare una disciplina speciale occorre individuarne la fonte, non presumere una deroga dal disegno.'''))
edit('07',lambda s:add(s,'Nel patrocinio vanno distinti tre elementi:','''Il **patrocinio obbligatorio** dell'art. 1 del R.D. 1611/1933 riguarda le amministrazioni dello Stato, anche organizzate ad ordinamento autonomo; gli avvocati dello Stato esercitano la funzione secondo legge senza necessità di un mandato professionale per ogni causa. Restano ferme le disposizioni processuali speciali che consentono la difesa diretta dell'amministrazione in determinati giudizi.

Il **patrocinio autorizzato**, disciplinato dall'art. 43, riguarda amministrazioni pubbliche non statali ed enti per i quali esiste uno specifico titolo di ammissione. Non si deduce dalla sola natura pubblica. Una volta autorizzato, opera secondo la disciplina prevista, salvi conflitti e casi speciali; non è un incarico liberamente intercambiabile con qualsiasi difensore privato.

La competenza interna segue ufficio giudiziario e territorio. L'Avvocatura generale, con sede a Roma, cura le cause davanti alle giurisdizioni superiori e quelle del proprio ambito territoriale; le distrettuali curano gli affari nelle rispettive circoscrizioni, secondo il R.D. 1612/1933 e le norme speciali. Il **foro dello Stato** (art. 25 c.p.c. e R.D. 1611/1933) è una regola sulla competenza del giudice, con eccezioni: non coincide con l'organigramma dell'Avvocatura. Un atto notificato non va quindi inoltrato automaticamente a Roma senza identificare giudice e ufficio legale competente.

**Caso breve.** Un ente pubblico non statale domanda assistenza: il primo controllo è il titolo normativo che ammette il patrocinio. Per un Ministero convenuto davanti a un giudice territoriale si identificano invece l'Avvocatura competente e i termini dell'atto; il funzionario trasmette tempestivamente il fascicolo, senza decidere la strategia processuale.'''))
edit('08',lambda s:add(s,'In una risposta concorsuale, le sezioni del Piano vanno ricondotte alle domande organizzative cui rispondono.','''Il piano tipo allegato al D.M. 132/2022 ha **quattro sezioni formali**, diverse dalle cinque dimensioni didattiche della tabella successiva:

| Sezione | Contenuto |
| --- | --- |
| 1. Scheda anagrafica dell'amministrazione | Identità e dati essenziali dell'ente |
| 2. Valore pubblico, performance e anticorruzione | Risultati attesi, obiettivi misurabili, rischi corruttivi e trasparenza |
| 3. Organizzazione e capitale umano | Struttura, lavoro agile, fabbisogni e sviluppo delle persone |
| 4. Monitoraggio | Modalità, responsabilità e tempi di verifica dell'attuazione |

Il PIAO ha durata triennale ed è aggiornato ogni anno; il termine ordinario è il **31 gennaio**, fatte salve le specifiche disposizioni di differimento. Non applicare ai Ministeri una proroga prevista soltanto per un altro comparto. L'organo di indirizzo politico lo adotta; il RPCT predispone la sottosezione rischi corruttivi e trasparenza sulla base degli obiettivi strategici. Dirigenti, strutture del personale e OIV intervengono secondo le rispettive competenze, senza diventare un unico soggetto responsabile di tutto. Sono previste pubblicazione sul sito istituzionale e trasmissione al Dipartimento della funzione pubblica tramite il portale dedicato.

**Verifica.** Un ufficio colloca il fabbisogno di personale nella sezione 2 perché «serve al risultato». Il collegamento è corretto sul piano funzionale, ma la collocazione formale è la sezione 3. Integrare significa rendere coerenti le parti, non confonderne nomi e competenze.'''))
def cont(s):
 s=s.replace('I **residui attivi** sono entrate accertate e non ancora riscosse;','Nel bilancio dello Stato i **residui attivi** comprendono entrate accertate non ancora riscosse e somme riscosse ma non ancora versate in tesoreria;')
 s=s.replace('diritto sorto ma non incassato, residuo attivo;','entrata accertata non riscossa oppure riscossa non versata, residuo attivo;')
 s=s.replace("l'entrata accertata non è riscossa o la spesa impegnata non è pagata","l'entrata accertata non è riscossa oppure il riscosso non è versato, o la spesa impegnata non è pagata")
 s=s.replace('Non inventa il numero del capitolo','Non inventare il numero del capitolo')
 s=add(s,'Schema mentale:','''**Esempio statale.** Nell'esercizio sono accertati 100, riscossi 80 e versati 60. Restano 20 da riscuotere e 20 da versare: i residui attivi sono **40**, non 20. La distinzione tra riscossione e versamento spiega perché un credito pagato all'agente possa non essere ancora entrato in tesoreria.''')
 s=add(s,'### Competenza e cassa','''### Le due sezioni della legge di bilancio e le unità di voto

La legge di bilancio, nella struttura della L. 196/2009, riunisce una **prima sezione** con misure normative dirette agli obiettivi di finanza pubblica e una **seconda sezione** con le previsioni di entrata e di spesa, sulle quali incidono le misure della prima. Non va presentata come la vecchia coppia di leggi separate «stabilità più bilancio».

Il disegno di legge comprende lo stato di previsione dell'entrata, gli stati di previsione della spesa dei Ministeri e il quadro generale riassuntivo. Le **unità di voto parlamentare** sono le tipologie per l'entrata e i programmi per la spesa. Capitoli e piani gestionali articolano ulteriormente le risorse per la gestione; le azioni specificano le finalità sottostanti ai programmi. Un capitolo non è dunque, per questo solo fatto, un'autonoma unità di voto del Parlamento.

**Verifica.** Un quiz contrappone missione, programma e capitolo come unità di voto della spesa. La risposta è programma: la missione esprime la finalità strategica più ampia; il capitolo serve alla gestione analitica.''')
 s=add(s,'### La linea del tempo dei documenti','''### Documenti di programmazione: quadro verificato nel 2026

La riforma europea della governance economica richiede di leggere i documenti nazionali insieme al **Piano strutturale di bilancio di medio termine 2025–2029**, che espone percorso della spesa netta, riforme e investimenti. Nel 2026 il Governo ha presentato il **Documento di finanza pubblica (DFP)** il 22 aprile in luogo del DEF: descrive quadro macroeconomico e andamento dei conti e segue l'attuazione del Piano. Non basta sostituire una sigla in un calendario tradizionale senza controllare funzione e versione.

Sul versante autunnale, nel 2025 è stato utilizzato il **Documento programmatico di finanza pubblica (DPFP)** al posto della NADEF per aggiornare il quadro e preparare la manovra. Va distinto dal **Documento programmatico di bilancio (DPB, o DBP nella sigla europea)**, trasmesso alla Commissione europea entro il termine previsto per la valutazione dei progetti di bilancio dell'area euro. Sono diversi anche dal disegno di legge di bilancio, che deve essere approvato dal Parlamento. Queste denominazioni descrivono i documenti ufficiali acquisiti; gli atti dell'autunno 2026 devono essere identificati nella versione effettivamente adottata, senza presumere contenuti futuri.

**Caso di classificazione.** «Il documento contiene gli obiettivi di medio termine» richiama il Piano; «autorizza le spese ministeriali dell'esercizio» richiama la legge di bilancio; «espone i risultati della gestione conclusa» richiama il rendiconto. La funzione permette di distinguere documenti anche quando il calendario cambia.''')
 s=add(s,'### Controlli e responsabilità','''### I due conti e la parificazione

Il rendiconto generale dello Stato comprende **conto del bilancio** e **conto generale del patrimonio**. Il primo espone entrate e spese, competenza, cassa e residui rispetto alle autorizzazioni; il secondo rappresenta consistenze patrimoniali e variazioni, raccordandole con i risultati finanziari. Un avanzo di cassa e una variazione patrimoniale non sono la stessa informazione.

Prima dell'approvazione parlamentare, la Corte dei conti svolge il **giudizio di parificazione**: confronta le risultanze del rendiconto con le scritture e le autorizzazioni di bilancio e accompagna la decisione con la relazione al Parlamento. Parificare non significa approvare politicamente il rendiconto né autorizzare spese nuove. La legge parlamentare di approvazione costituisce un passaggio distinto.

Il controllo preventivo di legittimità della Corte riguarda gli atti individuati dalla legge; il controllo successivo sulla gestione valuta anche risultati e regolarità nel proprio ambito. I controlli di regolarità amministrativa e contabile degli uffici del sistema RGS, disciplinati fra l'altro dal D.Lgs. 123/2011, non coincidono con la parificazione. **Esempio:** il riscontro su un atto di spesa ministeriale è un controllo sulla gestione in corso; il confronto annuale del rendiconto con le scritture appartiene a un'altra sede e a un altro oggetto.''')
 return s
edit('09',cont)
edit('10',lambda s:add(s,'## N-FC01-10-02', '''### Il controllo Consip negli acquisti ministeriali

Per un Ministero, scegliere una procedura sotto soglia non esaurisce i controlli. L'art. 1, comma 449, della L. 296/2006 impone alle amministrazioni statali centrali e periferiche del relativo perimetro il ricorso alle convenzioni Consip per gli acquisti interessati. La disciplina contempla eccezioni e deroghe specifiche: la preferenza dell'ufficio per un fornitore non è una deroga.

Per beni e servizi di importo almeno pari a **5.000 euro** e inferiore alla soglia europea, il comma 450 disciplina l'obbligo di ricorso al mercato elettronico per le amministrazioni statali considerate. Sotto 5.000 euro non opera quell'obbligo di MePA, ma restano applicabili regole del contratto, tracciabilità e digitalizzazione. Una piattaforma certificata non coincide necessariamente con il MePA; obbligo di piattaforma e obbligo dello strumento d'acquisto rispondono a norme diverse.

La sequenza è: categoria e fabbisogno → convenzione pertinente e obbligo soggettivo → importo complessivo stimato, senza IVA e senza frazionamenti artificiosi → strumento utilizzabile → procedura e qualificazione della stazione appaltante. Per categorie soggette a ulteriori obblighi di centralizzazione, oppure per un acquisto fuori convenzione, occorre verificare la specifica base legale e motivare l'esito.

**Caso breve.** Un Ministero deve comprare un servizio di pulizia da 40.000 euro e trova una convenzione applicabile che soddisfa il fabbisogno. L'importo compatibile con un affidamento diretto non autorizza a ignorare la convenzione obbligatoria. Se la prestazione richiesta non è coperta, si documenta il controllo e si applicano le regole pertinenti allo strumento e alla procedura.

Per il quadro generale e la versione delle soglie usa il VOL-01, capitolo Contratti pubblici essenziali, § [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali#9. Soglie e scelta della procedura|Soglie e scelta della procedura]] e § [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali#16. Consip, Acquisti in Rete, MEPA, convenzioni e accordi quadro|Consip e strumenti]]. Il limite per l'affidamento diretto e la soglia UE sono controlli distinti.'''))
def behavior(s):
 s=add(s,'Un rapporto personale non rende automaticamente impossibile ogni attività.','''Quando ricorrono i presupposti dell'art. 6-bis della L. 241/1990 o degli artt. 6–7 del D.P.R. 62/2013, il dipendente deve **astenersi** dalla decisione e dalle attività coinvolte nel conflitto, anche potenziale, e segnalare la situazione. La comunicazione non consente di continuare indisturbati l'istruttoria; il responsabile valuta l'astensione e organizza sostituzione e continuità del servizio. Le scadenze vanno segnalate insieme al conflitto, senza usare l'urgenza per eluderlo.''')
 s=s.replace('Rappresenta tempestivamente il rapporto al responsabile con i fatti necessari, protegge il fascicolo e segue la determinazione sulla gestione della pratica.','Rappresenta tempestivamente il rapporto al responsabile con i fatti necessari, si astiene dalle attività interessate quando sussistono i presupposti, protegge il fascicolo e segue la determinazione sulla sostituzione e gestione della pratica.')
 s=add(s,'Una formula utile è:','''La regola contrattuale è precisa: se l'ordine è **palesemente illegittimo**, il dipendente fa rimostranza a chi lo ha impartito spiegandone le ragioni. Se il superiore lo rinnova per iscritto, deve eseguirlo, **salvo che l'atto sia vietato dalla legge penale o costituisca illecito amministrativo** (art. 42, comma 3, lettera h), CCNL Funzioni Centrali 9 maggio 2022). La conferma scritta non autorizza quindi una falsificazione o un altro atto rientrante nelle eccezioni. Il dubbio interpretativo ordinario richiede invece chiarimento: non ogni disaccordo è palese illegittimità.

**Verifica.** Il superiore rinnova per iscritto l'ordine di attestare come svolto un controllo mai eseguito. La forma scritta non sana il falso: il dipendente non esegue l'atto vietato e attiva i canali competenti documentando i fatti.''')
 return s
edit('12',behavior)
print('FC01: integrate aree, PCM, modelli, Avvocatura, PIAO, contabilità, Consip e comportamento; snapshot conservati.')
