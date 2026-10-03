from pathlib import Path
import re,shutil
root=Path.cwd();base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters';backup=root/'artifacts/correzioni-collana-2026-10-02/before-text/VOL-03'
def append(relative,title,body):
 p=root/relative;s=p.read_text(encoding='utf-8')
 if title not in s:p.write_text(s+'\n## '+title+'\n\n'+body+'\n',encoding='utf-8')
append('wiki/sources/contabilita-aziendale-bilancio-reddito-impresa-aggiornamento-2026-07-18.md','Rettifiche del 3 ottobre 2026',"OIC 16, paragrafi 56 e seguenti: ammortamento delle immobilizzazioni materiali a utilità limitata; i terreni di regola non si ammortizzano, salvo utilità esauribile (cave/discariche). OIC 24 per le immateriali; partecipazioni/titoli seguono criteri propri, non quote di ammortamento del cespite. OIC 13 e art. 2426, n. 9: rimanenze al minore fra costo e realizzo desumibile dal mercato. Fonti: [OIC 16](https://www.fondazioneoic.eu/wp-content/uploads/2011/02/2024-03-OIC-16-Immobilizzazioni-materiali.pdf), [OIC 13](https://www.fondazioneoic.eu/wp-content/uploads/2011/02/2017-12-OIC-13-Rimanenze.pdf), coordinati con gli emendamenti definitivi dicembre 2025 già collegati. Per l'analisi didattica si definiscono esplicitamente margine di struttura primario = patrimonio netto − immobilizzazioni nette e secondario = patrimonio netto + passività consolidate − immobilizzazioni nette: convenzioni di riclassificazione, non soglie legali.")
append('wiki/sources/diritto-civile-obbligazioni-contratti-m-fc02-2026-07-17.md','Integrazioni del 3 ottobre 2026',"Artt. 1268–1273 c.c.: nella delegazione il debitore assegna al creditore un terzo che assume l'obbligazione; nell'espromissione il terzo assume verso il creditore senza delegazione; nell'accollo l'accordo nasce fra debitore e terzo e il creditore può aderirvi. La liberazione del debitore originario non si presume. Art. 2808: iscrizione costitutiva dell'ipoteca ([testo MEF](https://def.giustiziatributaria.gov.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&articolo=Articolo+2808&codiceOrdinamento=0000000000028080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7B9E93F1BE-06AE-4F24-8E9D-B838F7E0C2E6%7D)). Nullità: art. 1418, requisiti e norme imperative; annullabilità: incapacità e vizi del consenso artt. 1425 ss.; rescissione: pericolo o lesione ultra dimidium da bisogno sfruttato, artt. 1447–1448; risoluzione: art. 1453 e altri rimedi sul rapporto. Queste integrazioni alimentano casi distinti nel capitolo 12; non sostituiscono la disciplina tributaria speciale.")
append('wiki/sources/assetti-organizzativi-ae-adm-ader-verifica-2026-07-17.md','Organi: integrazione del 3 ottobre 2026',"Per AE e ADM l'art. 67 D.Lgs. 300/1999 individua Direttore, Comitato di gestione e Collegio dei revisori dei conti. Il terzo organo non va omesso. Direzione/gestione, deliberazioni organizzative e controllo contabile restano funzioni distinte. Riscontro istituzionale: [Camera dei deputati, dossier sulle agenzie fiscali](https://documenti.camera.it/Leg17/Dossier/Testi/CPTAGLIAEN02.htm). Il rinvio riguarda il modello degli organi, non nominativi, che non sono riportati nel capitolo.")
def load(n):
 p=next(base.glob(n+'-*.md'))
 if not (backup/p.name).exists():shutil.copy2(p,backup/p.name)
 return p,p.read_text(encoding='utf-8')
def save(p,s):
 s=s.replace('status: final','status: revised_draft').replace('draft_stage: text_frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true')
 s=re.sub(r'updated_at: [^\n]+','updated_at: 2026-10-03',s,count=1);p.write_text(s,encoding='utf-8')
p,s=load('11')
s=s.replace("L'ammortamento ripartisce il costo di un'immobilizzazione lungo la vita utile.","L'ammortamento ripartisce sistematicamente il valore ammortizzabile delle immobilizzazioni materiali e immateriali la cui utilizzazione è limitata nel tempo.")
s=s.replace('Le rimanenze sono valutate secondo costo e valore di realizzo nei limiti dei principi applicabili.',"Le rimanenze sono valutate al **minore tra costo e valore di realizzazione desumibile dall'andamento del mercato**, secondo l'art. 2426, n. 9, c.c. e l'OIC 13. Se il costo è 12.000 euro e il valore netto di realizzo è 10.500, si iscrive 10.500, con svalutazione di 1.500; non si sceglie il valore maggiore per conservare l'utile.")
s=s.replace('Le immobilizzazioni sono iscritte al costo e ammortizzate sistematicamente lungo la vita utile; perdite durevoli richiedono svalutazione.',"Le immobilizzazioni materiali e immateriali sono inizialmente iscritte al costo nei casi e con gli elementi ammessi; quelle la cui utilizzazione è limitata nel tempo si ammortizzano sistematicamente lungo la vita utile. Il terreno normalmente non si ammortizza, perché la sua utilità non si esaurisce; cave e discariche possono invece avere utilità limitata. Le immobilizzazioni finanziarie, come partecipazioni e titoli, seguono criteri propri e non si ammortizzano come un impianto. La svalutazione per perdita durevole è distinta dalla ripartizione programmata del costo: può aggiungersi all'ammortamento quando ne ricorrono i presupposti.")
s=s.replace('Il margine di struttura confronta fonti stabili e immobilizzazioni.',"Il **margine di struttura primario** è patrimonio netto meno immobilizzazioni nette; il **secondario** aggiunge al patrimonio netto le passività consolidate prima di sottrarre le immobilizzazioni. Esempio: patrimonio netto 160, debiti consolidati 90 e immobilizzazioni nette 250 danno primario −90 e secondario 0. Gli investimenti durevoli non sono coperti interamente dai mezzi propri, ma lo sono dall'insieme delle fonti stabili. La configurazione e le scadenze dei debiti vanno dichiarate: il margine non dimostra da solo solvibilità.")
save(p,s)
p,s=load('10')
s=s.replace("Rende pubblica la garanzia e, nei casi previsti, ne costituisce elemento essenziale.","Ha efficacia costitutiva: l'ipoteca si costituisce mediante iscrizione nei registri immobiliari (art. 2808 c.c.). Il titolo per iscrivere — per esempio contratto o sentenza — non è ancora l'iscrizione.")
needle='In casi complessi possono essere usati procedimenti finanziari o di trasformazione.'
s=s.replace(needle,needle+"""

### Tre calcoli estimativi, con ipotesi esplicite

**Comparazione.** Il valore si stima da prezzi di compravendite comparabili, resi omogenei per data, posizione, superficie e caratteristiche. Se tre valori unitari già corretti sono 1.900, 2.000 e 2.100 euro/m² e hanno uguale attendibilità, la media è 2.000 euro/m². Per 85 m² commerciali, V = 85 × 2.000 = 170.000 euro. Non si applica una media grezza fra immobili non confrontabili, né si considera una quotazione OMI prova del valore del singolo immobile.

**Capitalizzazione.** Con un reddito netto annuo ordinario R assunto costante e un saggio i coerente con il mercato, V = R / i. Con R = 8.000 euro e i = 4%, V = 200.000 euro. Il reddito è netto dei costi pertinenti; il tasso si scrive 0,04 nel calcolo. Se si assumono durata finita o redditi variabili, la semplice rendita perpetua non è appropriata: occorre attualizzare i flussi attesi.

**Costo.** Si stima il terreno e si aggiunge il costo di ricostruzione o sostituzione del fabbricato, sottraendo il deprezzamento pertinente. Con terreno 60.000, costo a nuovo 160.000 e deprezzamento complessivo stimato 25%, V = 60.000 + 160.000 × 0,75 = 180.000 euro. Il deprezzamento riguarda qui il fabbricato; non si applica indistintamente anche al terreno.

I tre risultati non sono intercambiabili: scopo, dati e ipotesi determinano il procedimento. **Esercizio:** se il reddito netto scende a 7.200 e il saggio resta 4%, il valore reddituale diventa 180.000; se cambia anche il rischio, mantenere lo stesso saggio può essere ingiustificato. Riferimento professionale: criteri comparativo e di capitalizzazione illustrati dall'Agenzia delle entrate nella guida all'acquisto della casa.
""")
save(p,s)
p,s=load('12')
s=s.replace('Delegazione, espromissione e accollo intervengono sul lato passivo con strutture differenti. Bisogna quindi stabilire se il debitore originario sia liberato o resti obbligato insieme al nuovo soggetto.',"""Delegazione, espromissione e accollo modificano il lato passivo, ma l'accordo nasce fra soggetti diversi:

| Istituto | Struttura essenziale | Esempio |
| --- | --- | --- |
| Delegazione, art. 1268 c.c. | Il debitore indica al creditore un terzo che assume il debito. | Alfa, debitrice di Beta, incarica Gamma di obbligarsi verso Beta. |
| Espromissione, art. 1272 c.c. | Il terzo assume il debito verso il creditore senza delegazione del debitore. | Gamma si impegna verso Beta a pagare il debito di Alfa, senza incarico di Alfa. |
| Accollo, art. 1273 c.c. | Debitore e terzo concordano che il terzo assuma il debito; il creditore può aderire. | Chi compra un immobile concorda con il venditore di assumere il mutuo. |

Il debitore originario non è liberato solo perché compare un terzo: serve la liberazione secondo la disciplina dell'istituto. Nell'accollo interno il creditore rimane estraneo all'accordo e non acquista per questo un'azione diretta verso l'accollante; nell'accollo esterno può aderire. Se la banca non libera il venditore, l'assunzione del mutuo non rende quest'ultimo automaticamente estraneo al debito. L'adempimento del terzo è ancora diverso: un terzo paga, senza necessariamente assumere per il futuro la posizione di debitore.

**Verifica:** l'acquirente e il venditore pattuiscono che il primo sostenga il mutuo, senza coinvolgere la banca. È espromissione? No: l'accordo nasce fra debitore e terzo, quindi è accollo; la banca conserva i propri diritti verso il debitore originario.""")
needle="Il recesso è il potere unilaterale"
s=s.replace(needle,"""| Istituto | Presupposto da riconoscere | Esempio e conseguenza |
| --- | --- | --- |
| Nullità | Contrasto con norma imperativa salvo diversa conseguenza, mancanza di requisito essenziale o illiceità nei casi dell'art. 1418. | Vendita immobiliare senza la forma scritta richiesta: il contratto non produce gli effetti negoziali voluti; pagare l'imposta di registro non lo sana. |
| Annullabilità | Incapacità legale o consenso viziato da errore essenziale e riconoscibile, violenza o dolo determinante. | Acquisto determinato da un raggiro: la parte protetta può chiedere annullamento; il semplice cattivo affare non basta. |
| Rescissione | Stato di pericolo noto alla controparte oppure bisogno sfruttato con lesione oltre la metà e altri requisiti di legge. | Non ogni prezzo basso è rescindibile: occorrono gli elementi degli artt. 1447–1448. |
| Risoluzione | Inadempimento non di scarsa importanza, impossibilità sopravvenuta o eccessiva onerosità nei relativi presupposti. | Mancata consegna essenziale: problema nell'esecuzione di un contratto valido, non nullità originaria. |

La nullità può essere fatta valere da chi vi ha interesse e rilevata d'ufficio nei limiti processuali; l'annullabilità tutela invece, di regola, la parte indicata dalla legge. La convalida è prevista per il contratto annullabile; non è un rimedio generale per quello nullo. **Caso:** il compratore denuncia un ritardo nella consegna e chiede «annullamento per nullità». Prima di scegliere il rimedio occorre stabilire se il contratto è valido e se il ritardo integra inadempimento rilevante: la corretta categoria può essere la risoluzione, con eventuale risarcimento.

"""+needle)
needle='## 12.';pos=s.index(needle)
s=s[:pos]+"""### Chi risponde nelle diverse società

Nella **società semplice** rispondono personalmente e solidalmente i soci che hanno agito in nome e per conto della società e, salvo patto opponibile ai terzi, gli altri soci (art. 2267). Nella **SNC** tutti i soci rispondono solidalmente e illimitatamente; un patto interno di limitazione non è opponibile ai terzi (art. 2291). Nella **SAS** gli accomandatari hanno responsabilità illimitata e solidale, gli accomandanti sono limitati alla quota conferita, salvo le ipotesi legali, come l'ingerenza vietata nella gestione (artt. 2313 e 2320).

Nella **SPA** e nella **SRL** risponde ordinariamente la società con il proprio patrimonio (artt. 2325 e 2462); non basta essere socio per diventare debitore di ogni debito sociale. Restano, fra l'altro, le eccezioni dell'unico socio nei casi previsti e le responsabilità per condotte proprie. Nella **SAPA**, pur essendo società di capitali, gli accomandatari rispondono illimitatamente e solidalmente, mentre gli accomandanti nei limiti della quota sottoscritta (art. 2452).

Il beneficio di preventiva escussione del patrimonio sociale opera secondo le regole del tipo e della regolarità della società: non coincide con assenza di responsabilità del socio. **Caso risolto:** una SNC non paga un fornitore. Il socio non può opporre al creditore il patto interno che gli attribuisce solo il 10% dei debiti; la ripartizione potrà rilevare nei rapporti fra soci. Se il debitore è invece una SRL, la sola qualità di socio non fonda la pretesa personale. Una fideiussione prestata dal socio costituisce però un titolo separato di responsabilità.

"""+s[pos:]
save(p,s)
p,s=load('03')
s=s.replace('Per AE e ADM il Direttore e il Comitato di gestione appartengono al lessico essenziale del modello agenziale.',"Per AE e ADM gli organi previsti dall'art. 67 del D.Lgs. 300/1999 sono **Direttore, Comitato di gestione e Collegio dei revisori dei conti**. Il Direttore rappresenta e dirige l'agenzia; il Comitato delibera sugli atti generali organizzativi e di gestione attribuiti dalla legge e dallo statuto; il Collegio verifica la regolarità contabile e finanziaria e riferisce sui bilanci. Il controllo dei revisori non sostituisce le scelte di gestione.")
save(p,s)
print('Updated FC02 03/10/11/12 and source deltas')
