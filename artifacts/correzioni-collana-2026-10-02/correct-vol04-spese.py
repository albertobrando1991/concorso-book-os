from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob('09-*.md'));t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest();b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
def section(start,end,new):
 global t
 i=t.index(start);j=t.index(end,i);t=t[:i]+new+'\n\n'+t[j:]
t=t.replace("Al cut-off normativo del volume, Normattiva mostra il Testo unico con aggiornamenti successivi e con ultimo aggiornamento dell'atto indicato nella vista consultata al 1° luglio 2026. Il capitolo spiega la logica stabile; importi, soglie, formule e istruzioni operative vanno verificati alla data del bando e della prova.","Le regole e gli importi riportati sono verificati al 3 ottobre 2026. Le cifre vanno studiate insieme a presupposti, eccezioni e data di aggiornamento: il controllo di eventuali modifiche prima della prova completa lo studio, non lo sostituisce.")
t=t.replace("Non sostituisce un commentario al D.P.R. 115/2002 e non contiene importi aggiornati, per una ragione precisa: gli importi e le soglie sono materia esposta ad adeguamenti, istruzioni ministeriali, circolari e prassi operative.","Presenta i principali importi e i calcoli necessari per applicare le regole; distingue la disciplina nazionale dalle istruzioni tecniche della singola sede.")
section('### Contributo unificato e anticipazioni','### Patrocinio a spese dello Stato', '''### Contributo unificato: quando è dovuto e come si calcola

Il contributo unificato finanzia il servizio giudiziario e si applica, secondo l'art. 9 del D.P.R. 115/2002, per ciascun grado dei processi compresi nel suo ambito. Non è un costo indistinto di qualsiasi atto penale. Nel civile, l'art. 14 individua il soggetto tenuto al versamento: in particolare, la parte che si costituisce per prima, deposita il ricorso introduttivo o presenta l'istanza di assegnazione o vendita nell'esecuzione. Domande riconvenzionali, interventi e modifiche della domanda richiedono il controllo delle specifiche regole del comma 3.

**Scaglioni civili ordinari di base, art. 13, comma 1; importi verificati al 3 ottobre 2026.** La tabella non assorbe esenzioni, procedimenti speciali, riduzioni o maggiorazioni.

| Valore della causa | CU base |
|---|---:|
| Fino a 1.100 euro | 43 euro |
| Oltre 1.100 e fino a 5.200 euro | 98 euro |
| Oltre 5.200 e fino a 26.000 euro | 237 euro |
| Oltre 26.000 e fino a 52.000 euro | 518 euro |
| Oltre 52.000 e fino a 260.000 euro | 759 euro |
| Oltre 260.000 e fino a 520.000 euro | 1.214 euro |
| Oltre 520.000 euro | 1.686 euro |

Il valore, determinato secondo le regole processuali ed escludendo gli interessi ai fini della dichiarazione prevista dall'art. 14, va dichiarato nelle conclusioni. Le impugnazioni comportano l'aumento della metà e il giudizio di cassazione il raddoppio; procedimenti e materie speciali seguono le rispettive disposizioni. Il rito semplificato di cognizione non è di per sé sinonimo di contributo dimezzato. Le esenzioni hanno una base normativa: l'art. 10 contempla, tra gli altri, i procedimenti in materia di prole, e non autorizza a dichiarare esente ogni lite familiare.

**Esempio.** Causa contrattuale ordinaria di primo grado del valore dichiarato di 12.000 euro, senza esenzione o regime speciale: CU di 237 euro. Il versamento forfettario dell'art. 30 è una voce distinta, ordinariamente di 27 euro nei casi cui si applica. Non si deve chiamare «CU di 264 euro» la somma delle due voci: 237 + 27 = 264 euro, con due diverse basi giuridiche. Diritti di copia e certificato dipendono invece dal servizio richiesto e dalle relative esenzioni.

### Il minimo per l'iscrizione civile e il pagamento insufficiente

L'art. 14, comma 3.1, prevede che, ferme le esenzioni di legge, la causa civile non possa essere iscritta a ruolo senza il pagamento di almeno **43 euro**, oppure del minore contributo dovuto per il procedimento. Se il contributo complessivo è maggiore, pagare il minimo non estingue il debito residuo.

La **Corte costituzionale, sentenza n. 137/2026, depositata il 21 luglio**, non ha eliminato questa disposizione: ha dichiarato inammissibile la questione relativa al potere attribuito al cancelliere e non fondate le altre questioni esaminate, richiamando il legislatore a intervenire. Il monito non equivale a una dichiarazione di illegittimità costituzionale.

Per il patrocinio pendente vale il chiarimento della **circolare ministeriale del 24 aprile 2025**: l'ufficio procede all'iscrizione se è allegata l'istanza regolarmente depositata e protocollata presso il competente Consiglio dell'Ordine degli Avvocati, anche se manca ancora la delibera. Apre il foglio notizie e segue l'esito; se la domanda è respinta e non accolta dal magistrato, cura il recupero delle spese annotate. La semplice intenzione di chiedere il beneficio non basta.

| Situazione | Controllo ed effetto |
|---|---|
| CU ordinario 237 euro, versati 43 | Soddisfatto il minimo; restano 194 euro da versare. |
| CU dovuto, nessun pagamento e nessuna esenzione o istanza protocollata | Opera il limite all'iscrizione previsto dall'art. 14, comma 3.1. |
| Istanza di patrocinio presentata e protocollata al COA, decisione pendente | Iscrizione con documentazione dell'istanza e apertura del foglio notizie. |
| Procedimento esente | Verifica della norma e della sua effettiva applicabilità, non riscossione automatica di 43 euro. |

Per il **recupero del CU civile**, l'art. 248, comma 3-bis, detta una disciplina specifica: se il pagamento integrale manca entro trenta giorni dall'iscrizione o dal diverso momento di insorgenza dell'obbligo, si procede al ruolo per quanto dovuto, interessi e sanzione. Vi provvede l'ufficio o la società convenzionata nei casi previsti. Non si sovrappone a questa disciplina la sequenza generale dell'invito al pagamento prevista dal comma 1. L'art. 16 collega gli interessi al deposito dell'atto e richiama la sanzione tributaria: il controllo distingue capitale, interessi e sanzione, senza inventare un'unica voce forfettaria.''')
section('Il limite reddituale è periodicamente adeguato con decreto.','### Istanza, dichiarazioni e controlli nel patrocinio', '''### Soglia e reddito familiare: civile e penale

Il decreto del 22 aprile 2025, pubblicato nella GU n. 159 dell'11 luglio 2025, fissa il limite dell'art. 76 a **13.659,64 euro**. È la soglia verificata al 3 ottobre 2026. L'adeguamento biennale dell'art. 77 richiede un decreto: non si aumenta autonomamente il limite applicando un indice e non lo si considera scaduto dopo un anno.

Il riferimento è il reddito annuo imponibile risultante dall'ultima dichiarazione, con le inclusioni richieste dall'art. 76: anche redditi esenti dall'IRPEF o soggetti a ritenuta a titolo d'imposta o a imposta sostitutiva. L'ISEE non è il sostituto automatico di questo calcolo. Se il richiedente convive con il coniuge o altri familiari, si sommano i redditi dei componenti conviventi. Si considera il solo reddito personale nelle controversie su diritti della personalità o quando gli interessi del richiedente sono in conflitto con quelli dei familiari conviventi.

**Solo nel processo penale**, l'art. 92 aumenta il limite di **1.032,91 euro per ciascun familiare convivente**. L'aumento non è una franchigia da sottrarre al reddito e non si trasferisce in via generale al processo civile.

| Nucleo del richiedente | Limite ordinario civile | Limite penale ex art. 92 |
|---|---:|---:|
| Nessun familiare convivente | 13.659,64 euro | 13.659,64 euro |
| Un familiare convivente | 13.659,64 euro | 14.692,55 euro |
| Due familiari conviventi | 13.659,64 euro | 15.725,46 euro |

**Esempio fittizio.** Anna dichiara 8.000 euro rilevanti e il coniuge convivente 6.000; non vi sono altri redditi né un conflitto di interessi. Il totale è 14.000 euro: supera il limite civile ordinario, ma rientra nel limite penale di 14.692,55 euro. Ciò risolve il requisito reddituale, non sostituisce la verifica delle altre condizioni.

Nel civile, l'art. 74 richiede anche che le ragioni dell'interessato non siano manifestamente infondate. Il medesimo filtro non si trasferisce come giudizio anticipato sulla fondatezza della difesa dell'imputato. L'art. 76 prevede inoltre deroghe per determinate vittime e situazioni: per esempio, per i reati indicati di maltrattamenti, violenza sessuale e atti persecutori. È necessario individuare la fattispecie e le condizioni previste; non ogni persona offesa è esonerata dal requisito economico. La nomina di un difensore d'ufficio, da sola, non equivale all'ammissione al patrocinio.

### Chi decide e quali rimedi si applicano

| Profilo | Civile | Penale |
|---|---|---|
| Presentazione | COA individuato dall'art. 124 in relazione al giudice competente. | Ufficio del giudice davanti al quale pende il procedimento; in Cassazione, giudice del provvedimento impugnato, art. 93. |
| Prima decisione | COA entro dieci giorni: ammissione anticipata e provvisoria, art. 126. | Giudice entro dieci giorni, con decreto motivato e controlli, art. 96. |
| Esito negativo | Istanza riproponibile al magistrato competente, art. 126. | Ricorso entro venti giorni dalla notizia del rigetto al presidente del tribunale o della corte d'appello competente, art. 99; notificazione all'ufficio finanziario. |
| Verifiche successive | Reddito, presupposti e condotta processuale; revoca ex art. 136. | Verifiche reddituali e cause di revoca dell'art. 112. |

Le competenze non si identificano con lo sportello che riceve materialmente il documento. La cancelleria istruisce e comunica nei limiti delle attribuzioni; non sostituisce COA o giudice nella decisione.''')
t=t.replace("L'istanza di ammissione non è una richiesta informale. Contiene dichiarazioni, dati reddituali, generalità, riferimento al procedimento e impegno a comunicare variazioni rilevanti, secondo le regole applicabili.","L'istanza deve essere sottoscritta e contenere i dati prescritti dagli artt. 78 e 79: generalità e codice fiscale del richiedente e dei familiari conviventi, dichiarazione del reddito rilevante e impegno a comunicare le variazioni. Quest'ultima comunicazione va effettuata entro trenta giorni dalla scadenza di un anno dalla domanda o dalla precedente comunicazione: non è un obbligo di presentare ogni mese una nuova istanza. Restano gli accertamenti e le integrazioni documentali previsti dalla legge.")
at=t.index('### Liquidazioni: ausiliari')
t=t[:at]+'''Nel civile, l'art. 131 distingue concretamente le voci: il contributo unificato è prenotato a debito, mentre compensi e spese di difensori, ausiliari e consulenti di parte, nei casi previsti dal testo vigente, sono anticipati. Nel penale, l'art. 107 rende gratuite le copie necessarie alla difesa e prevede l'anticipazione delle voci elencate. Una copia estranea alla necessità difensiva non diventa gratuita solo perché richiesta da un beneficiario.

La revoca civile dell'art. 136 per sopravvenute variazioni reddituali opera dal momento accertato della modifica; per mancanza originaria dei presupposti o condotta con malafede o colpa grave ha efficacia retroattiva. Nel penale l'art. 112 disciplina cause proprie, tra cui perdita dei requisiti e mancata comunicazione delle variazioni: non si copia meccanicamente la tabella del civile. Per il recupero occorrono provvedimento, periodo coperto e singole voci.

''' +t[at:]
at=t.index('### Funzionario delegato e pagamento')
t=t[:at]+'''### Ordine, decreto e opposizione: le distinzioni da ricordare

L'art. 165 stabilisce la regola dell'**ordine di pagamento del funzionario**, salvo i casi attribuiti al magistrato. Gli onorari del difensore ammesso al patrocinio seguono gli artt. 82–83; gli ausiliari e i custodi ricevono il decreto motivato del magistrato secondo l'art. 168. Non tutti i rimborsi richiedono quindi lo stesso autore o lo stesso provvedimento. Per esempio, l'art. 199 contempla l'ordine del funzionario per le indennità del testimone citato su richiesta di parte, a carico di quest'ultima.

Anche i termini della domanda vanno riferiti alla voce: l'art. 71 prevede la decadenza dopo **cento giorni** dalla testimonianza o dal compimento delle operazioni per le indennità e spese cui si riferisce; per le spese e indennità di viaggio e soggiorno delle categorie indicate prevede **duecento giorni**. Non è corretto applicare indistintamente cento giorni alle istanze degli avvocati per i compensi della difesa.

Contro i decreti di liquidazione, gli artt. 84 e 170 rinviano alla disciplina dell'**art. 15 del D.Lgs. 150/2011**: oggi il rito è semplificato di cognizione. Il ricorso si propone al capo dell'ufficio cui appartiene il magistrato, con le competenze specifiche previste per provvedimenti del giudice di pace o del PM. Le parti possono stare personalmente nel giudizio di merito; la sospensione dell'efficacia esecutiva può essere richiesta e la sentenza finale non è appellabile.

Il termine di **trenta giorni dalla comunicazione o notificazione** deriva dall'interpretazione giurisprudenziale, illustrata dalla Corte costituzionale n. 106/2016; non è il vecchio termine di venti giorni dell'art. 170 e non va attribuito al testo letterale dell'art. 15. Il termine di venti giorni dell'art. 99 riguarda invece il diverso rimedio contro il rigetto del patrocinio penale. Per un caso con omessa comunicazione o regime transitorio occorre ricostruire i relativi presupposti, senza calcolare la decorrenza dal giorno in cui il professionista ha presentato la richiesta di compenso.

''' +t[at:]
# Replace obsolete digital section, preserve next section.
i=t.index('### ',t.index('### Funzionario delegato e pagamento')+4)
j=t.index('### Foglio notizie',i)
t=t[:i]+'''### SPEdiGIUS e domanda telematica

La scheda del Ministero aggiornata al 19 agosto 2026 indica **SPEdiGIUS disponibile agli uffici dal 1° luglio 2026**, in sostituzione del precedente sistema SIAMM. Le funzioni riguardano spese pagate o anticipate, comprese le intercettazioni, foglio notizie e recupero crediti, con trasmissione a Equitalia Giustizia. Il sistema collega dati dei registri e firma digitale remota: conoscere il nome dell'applicativo serve a collocare queste attività, non ad attribuirgli poteri decisionali.

Il portale dei beneficiari è **lsg.giustizia.it**. La domanda deve riferirsi all'ufficio e al procedimento corretti; dati anagrafici, fiscali, documenti e coordinate di pagamento vanno controllati. Le istruzioni applicabili al rito e alla sede precisano il canale effettivo e gli eventuali passaggi tra deposito processuale e istanza contabile. Un avviso di una singola sede non va trasformato in una regola nazionale per ogni atto.

La ricevuta di invio dimostra l'operazione compiuta, non l'accoglimento della domanda né l'avvenuto pagamento. La sequenza resta: istanza documentata, istruttoria, provvedimento competente, controlli contabili e fiscali, pagamento e tracciamento.

''' +t[j:]
at=t.index('### Raccordo con cancelleria')
t=t[:at]+'''L'art. 208 individua l'ufficio competente al recupero: nel civile quello del magistrato, diverso dalla Cassazione, il cui provvedimento è divenuto definitivo; nel penale quello del giudice competente per l'esecuzione. Per i crediti del relativo ambito, gli artt. 227-bis e 227-ter regolano quantificazione e iscrizione a ruolo, entro un mese dal titolo definitivo, con intervento di Equitalia Giustizia secondo la convenzione. La riscossione è attività successiva e distinta: non si deve chiamare Equitalia Giustizia «giudice della condanna» o confondere tutti i suoi compiti con quelli dell'agente della riscossione.

**Esempio.** Una parte ammessa al patrocinio vince la causa contro una parte non ammessa. Se ricorrono i presupposti dell'art. 133, il provvedimento dispone il pagamento delle spese a favore dello Stato. Il beneficiario del recupero non si ricava soltanto da chi ha vinto; si legge il titolo e si raccorda alle voci annotate. Il foglio notizie documenta il credito, ma non sostituisce la decisione che ne fonda il recupero.

''' +t[at:]
t=t.replace("La distinzione evita un errore frequente: attribuire all'UPP compiti di pagamento o recupero. L'UPP supporta l'attività dell'ufficio; le spese seguono competenze amministrative e contabili proprie.","Il supporto UPP non trasferisce i poteri contabili o decisori. Gli eventuali compiti residuali di cancelleria del personale previsto dagli artt. 5 e 6 del D.Lgs. 151/2022 seguono l'assegnazione e i limiti illustrati nel capitolo 4.")
# Reduce 5-column table into four, preserving all cells.
lines=t.splitlines();out=[];in_table=False
for line in lines:
 if line.startswith('| Evento | Voce possibile | Ufficio coinvolto | Documento | Controllo |'):
  in_table=True;out.append('| Evento e voce | Ufficio coinvolto | Documento | Controllo |');continue
 if in_table and line.startswith('|'):
  cells=[x.strip() for x in line.strip('|').split('|')]
  if len(cells)==5:out.append('| '+' | '.join(['---']*4 if all(set(c)<=set('-: ') for c in cells) else [cells[0]+' — '+cells[1],*cells[2:]])+' |');continue
 if in_table and not line.startswith('|'):in_table=False
 out.append(line)
t='\n'.join(out)+'\n'
section('### Caso guidato: contributo non verificato','### Caso guidato: istanza di patrocinio', '''### Caso svolto: contributo minimo e patrocinio pendente

**Dossier fittizio, 6 ottobre 2026.** Sono presentate due cause contrattuali ordinarie di primo grado, ciascuna del valore dichiarato di 12.000 euro. Non ricorrono esenzioni di materia. Nella pratica A è allegata la ricevuta di 43 euro di CU. Nella pratica B non vi è versamento, ma è allegata la domanda di patrocinio depositata e protocollata al COA il 2 ottobre, ancora priva di delibera. Per semplicità, le altre voci di spesa non sono oggetto del quesito.

**Consegna, 15 minuti.** Scrivi una nota di sei righe che distingua iscrizione, debito residuo, titolo documentale e successivi adempimenti.

| Pratica | Soluzione |
|---|---|
| A | CU complessivo 237 euro, minimo43 assolto: iscrizione consentita per questo profilo, residuo194 da versare. Verificare l'adempimento e, in mancanza, il recupero civile ex248c3-bis. |
| B | L'istanza protocollata consente l'iscrizione secondo la circolare24aprile2025. Aprire il foglio notizie e seguire la decisione; non dichiarare il patrocinio già concesso. |

**Nota modello.** «La pratica A presenta CU ordinario di237 euro e pagamento parziale di43: il requisito minimo di iscrizione risulta assolto e il residuo è194. Nella pratica B la domanda di patrocinio risulta già depositata e protocollata al COA: si procede all'iscrizione con apertura del foglio notizie, riservando gli effetti definitivi all'esito della domanda. Non risultano, nei documenti forniti, esenzioni di materia. Restano distinti controllo del versamento e decisione sull'ammissione.»

**Griglia, 10 punti.** Due punti per ogni elemento corretto: CU237; residuo194; applicazione del minimo senza esenzione totale; efficacia della domanda protocollata; foglio notizie e controllo dell'esito. Un'affermazione di «ammissione automatica» non ottiene i punti degli ultimi due elementi.''')
section('### Quiz commentato','### Checklist di ripasso', '''### Quiz commentati

1. **In una causa civile ordinaria di 12.000 euro senza esenzione, sono versati43 euro. Che cosa consegue per questo profilo?**
   - A. Il contributo è integralmente assolto.
   - B. È assolto il minimo di iscrizione, ma restano194 euro di CU.
   - C. L'iscrizione richiede sempre il previo pagamento di237 euro.
   - D. Il minimo è stato annullato dalla Corte costituzionale137/2026.
   **Risposta corretta: B.** Il minimo non assorbe lo scaglione ordinario di237 euro; la pronuncia non ha annullato la regola.

2. **Richiedente e unico familiare convivente hanno redditi rilevanti complessivi di14.000 euro. Nessun conflitto o deroga. Quale confronto è corretto?**
   - A. Limite di14.692,55 euro sia civile sia penale.
   - B. Limite di13.659,64 euro in entrambi i riti.
   - C. Conta solo il reddito personale in entrambi.
   - D. Oltre il limite civile ordinario; entro quello penale con un familiare.
   **Risposta corretta: D.** L'aumento di1.032,91 euro dell'art.92 è proprio del penale; gli altri requisiti restano da verificare.

3. **La domanda civile di patrocinio è protocollata al COA e non ancora decisa. Qual è il trattamento del minimoCU?**
   - A. L'iscrizione può procedere con l'istanza documentata e foglio notizie.
   - B. La domanda vale come ammissione definitiva.
   - C. Deve sempre essere anticipato il minimo43 euro.
   - D. Basta una dichiarazione di futura presentazione della domanda.
   **Risposta corretta: A.** La circolare24aprile2025 tutela l'accesso durante l'attesa, conservando controllo e recupero secondo l'esito.

4. **Quale attribuzione è corretta nel sistema delle liquidazioni?**
   - A. Ogni spesa è liquidata dal funzionario delegato nel merito.
   - B. Ogni rimborso richiede necessariamente un decreto del magistrato.
   - C. La regola dell'ordine del funzionario convive con i casi riservati al magistrato.
   - D. Il beneficiario determina unilateralmente l'importo esecutivo.
   **Risposta corretta: C.** L'art.165 va coordinato, tra gli altri, con82–83 e168; liquidazione e pagamento restano distinti.

5. **Il CU civile resta parzialmente insoluto oltre trenta giorni dall'iscrizione. Quale disposizione specifica governa il recupero?**
   - A. L'art.99 sul rigetto del patrocinio penale.
   - B. L'art.248, comma3-bis, con ruolo, interessi e sanzione nei termini previsti.
   - C. L'art.92 sull'aumento per familiari conviventi.
   - D. Nessuna: il versamento minimo cancella il residuo.
   **Risposta corretta: B.** Non si sostituisce la disciplina speciale civile con la diversa sequenza generale dell'invito.

6. **Nel patrocinio civile, quale distinzione descrive correttamente l'art.131 vigente?**
   - A. Tutte le voci sono esenti e non vanno annotate.
   - B. I compensi del difensore sono sempre pagati direttamente dall'assistito.
   - C. CU e compensi sono sempre anticipati con un unico mandato.
   - D. Il CU è prenotato a debito; i compensi previsti sono anticipati dallo Stato.
   **Risposta corretta: D.** Prenotare significa annotare senza pagamento immediato; anticipare implica un esborso statale secondo il titolo.''')
t=t.replace('Memorizzare importi, confondere gratuito e anticipato','Usare importi senza data o presupposti, confondere gratuito e anticipato')
t=t.replace('come ciclo operativo, non come tariffario','collegando regole, importi e ciclo operativo')
t=t.replace('So evitare importi e soglie non verificati?','So applicare soglia, somma dei redditi, aumento penale e principali scaglioni del CU?')
s='sources/vol-04-spese-verifica-2026-10-03.md'
t=t.replace('source_refs: [','source_refs: [\n  "'+s+'",',1).replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/'+s+'",',1)
t=re.sub(r'updated_at: .*','updated_at: 2026-10-03',t,1).replace('review_required: false','review_required: true',1).replace('status: reviewed','status: revised_draft',1).replace('draft_stage: reviewed','draft_stage: editorial-revision',1)
# Normalize number-word joins introduced in compact drafting, preserving legal codes.
for a,bv in [('minimo43','minimo di 43'),('CU237','CU di 237'),('residuo194','residuo di 194'),('di237','di 237'),('di43','di 43'),('è194','è 194'),('euro di237','euro di 237'),('versati43','versati 43'),('di14.000','di 14.000'),('di14.692','di 14.692'),('di13.659','di 13.659'),('di1.032','di 1.032'),('dell’art.92','dell’art. 92'),("dell'art.92","dell'art. 92"),('minimoCU','minimo CU'),('circolare24aprile2025','circolare del 24 aprile 2025'),('ex248c3-bis','ex art. 248, comma 3-bis'),('comma3-bis','comma 3-bis'),('art.165','art. 165'),('con82–83 e168','con gli artt. 82–83 e 168'),('costituzionale137/2026','costituzionale n. 137/2026'),('131 vigente','131 vigente')]:t=t.replace(a,bv)
p.write_text(t,'utf-8')
result={'file':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(t.split()),'quizKeys':re.findall(r'Risposta corretta: ([A-D])',t),'source':s,'textApplied':True,'pdfVerified':False}
(A/'VOL-04-spese-delta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf-8');print(json.dumps(result,ensure_ascii=False))
