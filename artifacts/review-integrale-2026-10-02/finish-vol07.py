import json, hashlib, re
from pathlib import Path

base=Path('artifacts/review-integrale-2026-10-02')
lp=base/'VOL-07-ledger.json'
d=json.loads(lp.read_text(encoding='utf-8'))
chap={}
for f in d['files']:
 p=Path(f['path']); key=p.parts[3].split('-')[1].upper()+'/'+p.name[:2]; chap[key]=f; f['findings']=[]

# Posizioni ricavate dagli originali effettivamente letti; nessuna modifica al testo.
rows=[]
def add(key,anchor,cat,severity,problem,proposal):
 f=chap[key]; lines=Path(f['path']).read_text(encoding='utf-8').splitlines()
 start=next((i for i,s in enumerate(lines) if s.startswith('# ')),0)
 n=next((i+1 for i,s in enumerate(lines) if i>=start and anchor.casefold() in s.casefold()),start+1)
 fid=f'V07-{len(rows)+1:02d}'
 rows.append(dict(id=fid,key=key,path=f['path'],line=n,anchor=anchor,category=cat,severity=severity,problem=problem,proposal=proposal))
 f['findings'].append(fid)

add('SA01/05','pregiudizio concreto','Normativa','Grave','La sezione FOIA presenta il rilascio di dati sanitari come bilanciamento del pregiudizio concreto, senza spiegare il divieto di diffusione e la relativa eccezione assoluta.','Anteporre art. 2-septies, c. 8, Codice privacy e artt. 7-bis, c. 6, e 5-bis, c. 3, D.Lgs. 33/2013; valutare accesso parziale solo se i dati residui non consentono reidentificazione. Fonte E01.')
add('SA01/05','Accesso documentale','Normativa','Grave','Manca il requisito del diritto di rango almeno pari per accesso documentale a salute di terzi. Interesse diretto, concreto e attuale da solo non esaurisce il test.','Aggiungere art. 60 Codice privacy, raccordo art. 24, c. 7, L. 241/1990 e caso distinto dal FOIA. Fonte E02.')
add('SA01/05','termini','Completezza','Grave','Il lettore viene rinviato ai termini della procedura senza apprendere la regola nazionale speciale sul rilascio della documentazione sanitaria.','Inserire L. 24/2017, art. 4, c. 2: documentazione disponibile entro sette giorni; integrazioni entro trenta dalla richiesta, aventi diritto e controlli di legittimazione. Non trattare il termine come soltanto aziendale. E03.')
add('SA01/05','Fascicolo sanitario elettronico','Completezza','Medio','FSE e dossier sono distinti nominalmente ma manca la distinzione essenziale fra alimentazione e consenso alla consultazione per cura.','Aggiungere quadro nazionale FSE 2.0: alimentazione senza consenso, consenso alla consultazione per cura e relative eccezioni/garanzie, oscuramento; separare il dossier e la sua disciplina. E04–E05.')
add('SA01/05','richiesta di integrazione**,','Coerenza concettuale','Medio','La richiesta di integrazione è enumerata insieme agli esiti conclusivi.','Separare atto istruttorio interlocutorio da accoglimento, parziale, differimento e diniego; precisare effetti sui termini solo con fonte applicabile.')
add('SA01/05','Un file o una scansione','Definizione','Medio','La frase confonde appartenenza alla categoria documento informatico ed efficacia probatoria della copia o scansione.','Definire prima il documento informatico; spiegare poi che firma, integrità e conformità incidono su efficacia e valore probatorio, non sull’essere un documento informatico.')
add('SA01/04','Atti, procedimenti e flussi','Struttura','Lieve','Il capitolo ampliato comprende SSN, organi, LEA e accreditamento; titolo e seconda apertura mantengono la precedente enfasi su atti e flussi.','Adeguare titolo/sommario e raccordare le due aperture. Conservare le integrazioni nazionali del 2 ottobre, che colmano le lacune precedentemente segnalate.')
add('SA01/06','Da otto a dieci punti','Didattica','Medio','La valutazione sommativa può qualificare buona una risposta pur con errore su riservatezza o competenza.','Aggiungere condizioni di insufficienza per divulgazione indebita, accesso illegittimo o promessa fuori competenza, indipendenti dal totale; raccordo con la rubrica dei casi SA02/10.')
add('SA01/06','riscrittura','Chiarezza','Lieve','Gli esempi di comunicazione semplificata conservano formule come documento indicato nel modulo/canale previsto/ufficio competente.','Completare un esempio fittizio con documento, ufficio, canale e azione realmente nominati, indicando che i dati sono illustrativi.')
add('SA01/09','−4,45%','Calcolo','Lieve','Il calcolo usa il costo unitario già arrotondato: la variazione esatta da 20 a 516000/27000 è −4,4444…%, non −4,45%.','Conservare precisione nei passaggi intermedi e scrivere circa −4,44% nelle due occorrenze; costo 19,11 euro e differenza −0,89 euro restano corretti come importi arrotondati.')
add('SA01/09','bilancio','Completezza','Medio','La trattazione contabile non offre un quadro completo dei documenti fondamentali del bilancio sanitario, dei ruoli e del relativo ciclo nazionale.','Integrare prospetto essenziale D.Lgs. 118/2011 Titolo II, documenti ex art. 26 e adozione/approvazione ex art. 31; verificare il consolidato prima di attivare termini. Aggiungere un esempio economico-patrimoniale su ammortamento e contributo per investimento.')
add('SA01/10','farmaci','Completezza','Grave','Farmaci e dispositivi nel titolo ricevono soprattutto la stessa logica generale di acquisto. Mancano nozioni settoriali per distinguere medicinale, dispositivo e relative autorizzazioni/classi; SA04/04 copre solo parte del bisogno.','Inserire nucleo amministrativo su AIC e classi di rimborsabilità A/H/C, rinvio preciso a SA04/04 per MDR/IVDR, centralizzazione acquisti/soggetti aggregatori e NSO; fonti AIFA, MEF e normativa ufficiale. Escludere prescrizioni terapeutiche.')
add('SA01/10','scorte','Completezza','Medio','Magazzino tratta tracciabilità e anomalie ma lascia troppo impliciti rotazione per scadenza e condizioni di conservazione.','Spiegare FEFO, segregazione prodotti non conformi/ritirati e principio di catena del freddo senza inventare temperature universali; esempio con scorte, consumo e tempo di riordino.')
add('SA01/10','definisce','Lingua','Lieve','Nello stesso elenco operativo si alternano imperativi e indicativi: identifica/definisce/distingue/propone.','Uniformare in identifica, definisci, distingui, proponi; verificare anche prevede/prevedi nell’esercizio SA02/05.')
add('SA02/03','Legge 24','Completezza','Grave','Responsabilità e consenso restano una cornice: non sono spiegati i principali regimi della L. 24/2017 né DAT, minori e pianificazione condivisa della L. 219/2017.','Aggiungere tabella struttura/professionista/responsabilità civile e penale, art. 590-sexies con limiti, cenno assicurativo; distinguere consenso, rifiuto, DAT e pianificazione. Rinvio a SA02/06 per la relazione di cura già presente.')
add('SA02/04','processo assistenziale','Completezza','Grave','Il capitolo di tecniche assistenziali insiste su verificare procedure e confini, ma omette nozioni teoriche fondamentali utilizzabili al concorso.','Inserire diagnosi infermieristica distinta da diagnosi medica, cinque momenti dell’igiene mani e precauzioni standard/per trasmissione, logica delle scale di dolore/funzione/rischio e principi di prevenzione delle infezioni da catetere. Nessun bisogno di settaggi locali o dosi.')
add('SA02/05','scala 2 prevista dal documento per BPCO','Errore clinico','Grave','La scala 2 NEWS2 è presentata come scala per BPCO, estensione che può determinare una classificazione errata.','Precisare insufficienza respiratoria ipercapnica confermata da emogasanalisi corrente/precedente e decisione clinica documentata del target 88–92%; BPCO isolata non basta. Negli altri casi scala 1. Fonte RCP E06.')
add('SA02/05','NEWS2','Completezza clinica','Medio','La tabella NEWS2 è inserita in capitolo anche ostetrico senza rendere esplicito il perimetro di validazione e le esclusioni.','Esplicitare applicazione adulti e non uso standard sotto i 16 anni/in gravidanza; indicare strumenti appropriati al setting, verificati nelle linee correnti. E06.')
add('SA02/05','triage','Completezza','Grave','Non viene insegnato il sistema nazionale a cinque priorità con relativi tempi; il rinvio ai protocolli locali rischia di occultare il nucleo nazionale.','Aggiungere tabella 1–5: immediato, 15, 60, 120 e 240 minuti con definizioni e rivalutazione; distinguere il colore regionale dal codice nazionale. Fonti E07–E08.')
add('SA02/05','BLS','Completezza','Grave','BLS/ALS/NLS sono soprattutto differenze di finalità e organizzazione; emergenze ostetriche sono etichette senza definizioni e segni discriminanti sufficienti.','Integrare riconoscimento teorico dell’arresto e sequenza concettuale degli algoritmi versionati; definire e distinguere eclampsia, distocia di spalla, prolasso del funicolo e sepsi materna. Validare su linee correnti senza trasformare il libro in protocollo clinico universale.')
add('SA02/06','Centrale','Rinvii e completezza','Medio','Il quadro territoriale si appoggia soprattutto al manuale AGENAS 2022; il lettore non è guidato ai nuovi contenuti SSN del capitolo SA01/04.','Rinvio preciso a SA01/04 e sintesi D.M. 77/2022 su Casa della comunità, COT, Ospedale di comunità e IFeC, distinguendo standard nazionale e attuazione locale.')
add('SA02/08','lo scarto non prova','Errore quantitativo','Grave','47,4−39,3−7,7=0,4 punti; 77,7−46,8−30,7=0,2. I due scarti sono attribuiti ad arrotondamento e pesatura senza prova. Arrotondare tre valori al decimo non spiega scarti oltre 0,15 punti; pesi comuni non eliminano l’additività.','Conservare i dati originali se fedeli alla fonte, ma ricostruire denominatori, categorie mancanti e note della tabella. Finché non riconciliati, scrivere che le componenti pubblicate non sommano al totale e che la causa non è stabilita; correggere anche source note e soluzione dell’esercizio cervicale.')
add('SA02/08','definizione operativa','Terminologia','Medio','La sezione usa definizione operativa di focolaio per criteri che individuano il caso nell’indagine.','Rinominare definizione operativa di caso e distinguere l’aggregazione epidemiologica del focolaio; il capitolo SA03/05 e la source PREMAL offrono già la distinzione corretta.')
add('SA02/08','screening','Completezza','Medio','Si calcolano coperture senza una mappa essenziale dei tre programmi oncologici, popolazioni, test e intervalli; PREMAL non separa bene termini nazionali e organizzazione locale.','Aggiungere quadro dei programmi con data e limiti regionali, poi tabella del flusso PREMAL dal medico ai livelli aziendale/regionale/nazionale, termini verificati nel decreto e definizioni pertinenti.')
add('SA02/09','689','Completezza normativa','Grave','L. 689/1981 e D.Lgs. 758/1994 sono nominati senza una sequenza normativa sufficiente per risolvere una prova su contestazione, prescrizione ed estinzione.','Aggiungere due schemi distinti: accertamento/notifica, difesa/pagamento e ordinanza; prescrizione, verifica adempimento, pagamento e comunicazioni. Verificare termini e condizioni negli articoli vigenti; distinguere il procedimento ambientale del D.Lgs. 152/2006, parte VI-bis.')
add('SA02/09','AIA','Completezza','Grave','AIA/AUA, controlli alimentari e sicurezza del lavoro ricevono soprattutto una mappa del controllo; mancano presupposti essenziali dei regimi e contenuti dei relativi oggetti.','Integrare confronto AIA/AUA, quadro DVR e ruoli prevenzionistici, HACCP/rintracciabilità e diritti di controperizia/controversia ex D.Lgs. 27/2021. Un verbale didattico compilato deve mostrare fatti, norma, qualificazione e seguito.')
add('SA02/10','Caso','Didattica','Medio','I cinque casi esercitano prevalentemente interruzione/allerta/rinvio; tali mosse sono corrette ma ripetono i capitoli precedenti.','Aggiungere almeno un caso completo per profilo con dati sufficienti e un output valutabile fino alla conclusione nel perimetro di competenza; mantenere i casi di escalation come tipologia distinta.')
add('SA03/01','la presenza e la modalità','Normativa e quiz','Grave','Presenza dell’inglese/informatica trattata come variabile puramente eventuale; esercizio classifica inglese come M senza distinguere obbligo generale e modalità concreta.','Esporre art. 37 D.Lgs. 165/2001 e coordinamento con disciplina speciale; classificare come mobile la modalità/livello, non genericamente l’obbligo. Correggere spiegazione e soluzione; analogo SA04/01 riga 174. Fonte E09.')
add('SA03/01','punteggi','Completezza normativa','Medio','Punteggi e soglie sono quasi soltanto dati da recuperare nel bando: manca lo schema ordinario del D.P.R. 483/1997 per profilo.','Insegnare quadro nazionale ordinario con eccezioni e coordinamento normativo, poi far confrontare il bando. Analogo D.P.R. 220/2001 per SA02/01 e SA04/01; non generalizzare da un singolo bando.')
add('SA03/02','LEA','Rinvii e completezza','Medio','La programmazione dirigenziale è prevalentemente metodo astratto, con standard e indicatori nominati. La matrice dichiara NSG/NSIS coperti mentre la source governance esclude i claim NSG per acquisizione bloccata.','Raccordare teoria a SA01/04, aggiungere un cruscotto con definizioni di indicatori, numeratori/denominatori e target didattici; acquisire fonte NSG valida e riconciliare matrice e fonti.')
add('SA03/03','autonomamente','Adeguatezza destinatario','Medio','La formula che il testo non autorizza a scegliere autonomamente una terapia è ambigua in un capitolo rivolto a dirigenti medici già abilitati.','Riformulare come limite del manuale concorsuale: la decisione clinica resta responsabilità del professionista nel caso reale, secondo evidenze e competenze; evitare negazioni generali dell’autonomia medica.')
add('SA03/04','rischio','Completezza','Medio','Strumenti di rischio clinico ancora poco sviluppati: evento sentinella/SIMES, RCA e FMEA non hanno un confronto operativo sufficiente.','Definire evento avverso, near miss ed evento sentinella; distinguere RCA retrospettiva e FMEA proattiva, con una piccola applicazione e rinvio al contributo RCA di SA04/04.')
add('SA03/06','Caso','Didattica','Medio','Il caso dispone di parametri ma la soluzione resta su categorie di ipotesi, senza mostrare un confronto diagnostico discriminante.','Completare il solo caso illustrativo con ipotesi esemplificative, dati a favore/contro e verifiche discriminanti; non aggiungere un’enciclopedia delle specialità esclusa dal progetto.')
add('SA03/07','revisione entrata in vigore il 1° dicembre 2023','Normativa professionale','Grave','Il codice CNOP 2023 è indicato come vigente; il sito ufficiale lo archivia nel periodo 1/12/2023–24/12/2024 a seguito della sentenza del Consiglio di Stato.','Sostituire il riferimento con la pagina CNOP del codice attualmente vigente, confrontare gli articoli eventualmente recepiti e correggere la source deontologia. La revisione in corso nel 2026 non rimette in vigore il testo 2023. E10–E11.')
add('SA04/02','Discipline','Completezza','Grave','Biochimica, microbiologia, ematologia e immunologia sono una mappa orientativa, ma la matrice dichiara complete le discipline applicate. Mancano anche precisione/esattezza, calibrazione e interpretazione di controllo qualità.','Integrare principi analitici di base, differenza calibrazione/controllo, precisione/esattezza e un grafico QC commentato; esempi concettuali per le principali discipline senza reagenti o settaggi universali.')
add('SA04/02','biosicurezza','Completezza normativa','Grave','Approccio OMS al rischio senza quadro essenziale dei gruppi di agenti e misure minime nazionali; decontaminazione e rifiuti restano generici.','Raccordare D.Lgs. 81/2008, Titolo X e allegati pertinenti: gruppi/containment, differenze cappe, disinfezione/sterilizzazione e categorie dei rifiuti sanitari. L’approccio al rischio non elimina gli obblighi legali.')
add('SA04/03','dosimetria','Completezza','Grave','Grandezze Bq/Gy/Sv sono spiegate, ma mancano indicatori dosimetrici di uso concorsuale e principi fisici essenziali per collegare imaging e rischio.','Definire CTDIvol, DLP e prodotto dose-area con unità e limiti; effetti stocastici/reazioni tissutali, tempo-distanza-schermatura, limiti di dose professionali/pubblico e distinzione dalle esposizioni mediche; verificare i valori nella norma vigente.')
add('SA04/03','risonanza','Completezza','Medio','Risonanza e particolari esposizioni non ricevono un quadro sufficiente dei rischi specifici.','Aggiungere rischio proiettile, impianti/compatibilità, RF, rumore e criogeni; riferimento al D.M. 14/1/2021 e criteri generali di sicurezza, più esposizioni in gravidanza; nessun protocollo esecutivo.')
add('SA04/03','artefatt','Apparati','Medio','Il capitolo promette ragionamento sulla qualità dell’immagine e sugli artefatti ma non presenta un’immagine o schema esaminabile.','Inserire almeno due immagini didattiche originali o con licenza e didascalia, domanda, risposta e limite interpretativo.')
add('SA04/04','incidente grave','Definizione e completezza','Medio','Definizione di incidente grave circolare, rinvia alle conseguenze definite nel regolamento senza renderle apprendibili; classi e identificazione restano poco sviluppate.','Esplicitare morte, grave deterioramento della salute e grave minaccia per la salute pubblica; aggiungere classi MDR/IVDR, UDI e distinzione FSCA/FSN. Conservare i termini corretti del D.M. 1/7/2025: tempestivamente entro 10 giorni per grave, facoltà entro 30 per non grave. E12.')
add('SA03/07','Humanizer','Residui editoriali','Medio','Istruzioni di produzione sono presenti nella prosa per il lettore: gate, Humanizer, audit step 15. Ricorrono anche SA03/06 e SA04/04.','Togliere dalla destinazione pubblica le istruzioni di pipeline, mantenendole nei report di lavoro; conservare soltanto cut-off e limiti informativi utili al candidato.')

urls={
'E01':('Divieto FOIA salute','https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9461036'),
'E02':('Pari rango e accesso, parere 18 giugno 2026','https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/10267085'),
'E03':('L.24/2017 art.4','https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=17G00041&art.dataPubblicazioneGazzetta=2017-03-17&art.flagTipoArticolo=0&art.idArticolo=4&art.idGruppo=0&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1'),
'E04':('Garante FSE','https://www.garanteprivacy.it/temi/fse'),
'E05':('Garante dossier','https://www.garanteprivacy.it/faq/dossier-sanitario'),
'E06':('RCP NEWS2 report','https://www.rcp.ac.uk/media/a4ibkkbf/news2-final-report_0_0.pdf'),
'E07':('Ministero triage nazionale 2019','https://www.salute.gov.it/new/it/news-e-media/notizie/pronto-soccorso-libera-della-conferenza-stato-regioni-alle-nuove-linee-di/'),
'E08':('Linee nazionali triage PDF','https://www.salute.gov.it/imgs/C_17_pubblicazioni_3145_allegato.pdf'),
'E09':('D.Lgs.165/2001 art.37','https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2001-03-30%3B165~art37%21vig='),
'E10':('CNOP archivio codice 2023–2024','https://www.psy.it/la-professione-psicologica/codice-deontologico-degli-psicologi-italiani/codice-deontologico-vigente-dal-01-dicembre-2023-al-24-dicembre-2024/'),
'E11':('CNOP codice vigente','https://www.psy.it/la-professione-psicologica/codice-deontologico-degli-psicologi-italiani/codice-deontologico-vigente/'),
'E12':('DM1 luglio2025 art4 termini vigilanza','https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=25A05071&art.dataPubblicazioneGazzetta=2025-09-19&art.flagTipoArticolo=0&art.idArticolo=4&art.idGruppo=0&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1'),
'E13':('CCNL Area Sanità definitivo27/2/2026','https://www.aranagenzia.it/novita/ccnl-area-sanita-2022-2024/'),
'E14':('PNP2026–2031','https://www.salute.gov.it/new/it/tema/il-piano-nazionale-della-prevenzione/'),
'E15':('PNHTADM2026–2028','https://www.agenas.gov.it/aree-tematiche/comunicazione/primo-piano/2698-pnhta-dm-2026%E2%80%932028-sbloccate-le-risorse-del-fondo%2C-al-via-la-fase-operativa-del-sistema-nazionale-hta-sui-dispositivi-medici'),
'E16':('Raccomandazione Euratom2026/403','https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX%3A32026H0403'),
'E17':('FNOPI codice2025','https://www.fnopi.it/2025/03/24/codice-deontologico-in-vigore/'),
'E18':('FNOFI stato revisione codice','https://www.fnofi.it/w/il-nuovo-codice-deontologico-del-fisioterapista'),
'E19':('GU227/2026 aggiornamentiLEA, artt.8 e12; PDF pp27 e51','https://www.gazzettaufficiale.it/eli/gu/2026/09/30/227/sg/pdf'),
'E20':('ISS PASSI colorettale','https://www.epicentro.iss.it/passi/dati/ScreeningColorettale')}
claims={'SA01/04':['E19'],'SA01/05':['E01','E02','E03','E04','E05'],'SA02/03':['E17','E18'],'SA02/05':['E06','E07','E08'],'SA02/06':['E14'],'SA02/08':['E20'],'SA03/01':['E09','E13'],'SA03/04':['E15'],'SA03/05':['E14'],'SA03/07':['E10','E11'],'SA04/01':['E09'],'SA04/03':['E16'],'SA04/04':['E12','E15']}
changed=[]
for key,f in chap.items():
 current=hashlib.sha256(Path(f['path']).read_bytes()).hexdigest()
 f['sha256Final']=current; f['unchangedSinceRead']=current==f['sha256']
 if current!=f['sha256']: changed.append(key)
 f['externalClaimsChecked']=[{'claim':urls[e][0],'url':urls[e][1],'checkedAt':'2026-10-02'} for e in claims.get(key,[])]
 f['limitations']=['Lettura integrale del Markdown; verifiche normative esterne mirate, non certificazione di ogni comma o protocollo clinico; controllo PDF separato.']
for f in d['supportingSources']:
 f['readComplete']=True; f['sha256']=hashlib.sha256(Path(f['path']).read_bytes()).hexdigest()
extras=list(Path('wiki/books/moduli').glob('m-sa*/index.md'))+list(Path('wiki/books/moduli').glob('m-sa*/planning/02-matrice-copertura-didattica.md'))
vb=Path('wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie')
extras += [vb/'index.md',vb/'planning/02-matrice-copertura-didattica.md',vb/'planning/03-mappa-fonti-specialistiche.md',vb/'planning/04-bibbia-del-volume.md']
d['supportingPlanning']=[dict(path=str(p).replace('\\','/'),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=True) for p in extras]
d['status']='text-review-complete-pdf-separate'
d['findingsDetails']=rows
d['externalEvidence']={e:{'claim':t,'url':u} for e,(t,u) in urls.items()}
lp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

report=['# VOL-07 — Revisione integrale testuale prepubblicazione\n','Data: 2 ottobre 2026. Solo rilievi e proposte; nessuna modifica ai capitoli.\n',
'## 1. Sintesi\n',
'Letti integralmente i 25 capitoli originali correnti, inclusi tutti i quiz, commenti, domande aperte, classificazioni, casi e riferimenti. Letti anche 77 source note direttamente collegate, indici, quattro matrici modulari, matrice del volume, mappa fonti e Bibbia. Hash nel ledger. Le integrazioni del 2 ottobre nei capitoli SA01/04 e SA01/09 sono comprese: i precedenti rilievi di assenza di fondamenti SSN e finanziamento non sono riproposti come lacune assolute.\n',
'Esito: **non pubblicabile senza correzioni sostanziali**. Errori certi su NEWS2, codice degli psicologi, regimi di accesso e spiegazione di dati PASSI; lacune teoriche in nuclei dichiarati completi. La buona separazione fra competenze professionali e procedure locali non compensa l’assenza di principi nazionali e definizioni necessarie al concorso.\n',
'## 2. Verifica dei 30 punti\n',
'| Punti | Esito | Evidenza |\n| --- | --- | --- |',
'| 1–5 Indice, struttura, progressione, titoli, pubblicazione | Da correggere | Nuovo contenuto SA01/04 non pienamente riflesso nel titolo; capitoli dirigenziali molto più brevi; gate non equivalgono a qualità editoriale |',
'| 6–9 Coerenza interna, trasversale, terminologia, completezza | Criticità sostanziali | NEWS2, focolaio/caso, autonomia clinica; teoria professionale incompleta; fonti e matrici discordanti |',
'| 10–15 Definizioni, concetti, normativa, esempi, apparati, fonti | Criticità sostanziali | Privacy, CNOP, PASSI; casi troppo spesso senza conclusione; mancano apparati di imaging |',
'| 16–20 Sintassi, chiarezza, tono, didattica, ripetizioni | Migliorabile | Ripetizione di verificare protocollo/confini; imperativi incoerenti; duplicazioni epidemiologia/evidenze |',
'| 21–25 Contraddizioni, grammatica, ortografia, punteggiatura, refusi | Rilievi localizzati | Contraddizioni matrice/fonti e classificazione inglese; non rilevata una serie di chiavi MCQ rimappate male |',
'| 26 Grafica testuale | Verificata nel Markdown | Gerarchie e tabelle presenti; manca immagine didattica dove richiesta dal compito |',
'| 27–29 PDF, impaginazione, leggibilità | Controllo separato | Rinviare a PDF-VOL-07.md; questo rapporto non certifica l’impaginato |',
'| 30 Giudizio complessivo | Non pubblicabile | Correggere errori e integrare i nuclei assegnati prima del nuovo impaginato |\n',
'## 3. Tabella degli errori e delle integrazioni\n',
'I percorsi SAxx/nn sono risolti nei collegamenti; le righe si riferiscono agli originali con hash nel ledger. Stato di tutti i rilievi: aperto, proposta non applicata.\n',
'| ID | Posizione / estratto | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |']
for r in rows:
 path='/C:/Users/info/OneDrive/Desktop/concorso-book-os/'+r['path']
 report.append(f"| {r['id']} | [{r['key']}:{r['line']}]({path}:{r['line']}) — «{r['anchor']}» | {r['category']} | {r['severity']} | {r['problem']} | {r['proposal']} | Aperto |")
report += ['\n## 4. Osservazioni per capitolo\n','Tutti i capitoli hanno lettura e revisione esercizi complete. La tabella integra i rilievi sopra con gli esiti positivi; non equivale a certificazione specialistica clinica.\n','| Capitolo | Esito del controllo |\n| --- | --- |']
notes={
'SA01/04':'10 quiz nuovi coerenti. Organizzazione, LEA e finanziamento ricollegati correttamente; LEA pubblicati il 30/9 con efficacia dal 30/10, distinzione corretta.',
'SA01/05':'Domande aperte e caso delega coerenti, ma non colmano i regimi privacy e i termini mancanti.',
'SA01/06':'Sei classificazioni coerenti. Rafforzare criteri critici della rubrica e concretezza del messaggio.',
'SA01/09':'Cinque quiz e dieci classificazioni coerenti. Scostamenti 7,5%, 12,5%, 8% corretti; errore lieve soltanto nell’arrotondamento del costo unitario.',
'SA01/10':'Totale 295.200 euro e mini-esercizio 28.800 corretti; scorta 37.500/2.800 = 13,39 settimane. Aggiungere controllo del fabbisogno: ordine mensile 36.000 rispetto a consumo settimanale 2.800 merita motivazione.',
'SA02/01':'Dieci classificazioni e quattro abbinamenti coerenti; OSS distinto dalle professioni sanitarie ordinistiche. Integrare quadro concorsuale nazionale.',
'SA02/03':'Quiz B,C,B corretti e commenti coerenti. Rafforzare responsabilità e consenso.',
'SA02/04':'Quiz B,C,C corretti; caso Anna coerente. Mancano alcuni fondamenti assistenziali.',
'SA02/05':'Quiz C,C,C,C,B,C,C coerenti; calcoli NEWS2 corretti rispetto ai parametri. Correggere selezione scala e completare teoria.',
'SA02/06':'Quiz B,A,C,B corretti; caso Elena coerente. PNP corrente confermato.',
'SA02/07':'Quiz D,B,B,B,C corretti; solido nucleo PICO/GRADE/EtD. Facoltativo un esempio di ricerca con MeSH/stringa PubMed.',
'SA02/08':'Quiz B,A,C,B,C corretti; RR13, RR1,25%,43%,85,7% corretti. Errata la causa attribuita agli scarti PASSI.',
'SA02/09':'Quiz B,B,C,B,B corretti; classificazioni e caso compatibili con perimetro. Necessaria teoria giuridico-tecnica.',
'SA02/10':'Quiz B,C,B,C,C corretti e commenti coerenti; cinque casi in prevalenza di sospensione/escalation.',
'SA03/01':'Classificazioni da rivedere per inglese; CCNL27/2/2026 confermato. Nessun errore su distinzione D.P.R.483/220.',
'SA03/02':'Domande aperte coerenti; caso di piano privo di valori con cui verificare risultato.',
'SA03/03':'Domande aperte coerenti; duplicazione con SA02/07 e formula impropria sull’autonomia terapeutica.',
'SA03/04':'Audit/re-audit e assessment/appraisal corretti; PNHTA2026–2028 confermato.',
'SA03/05':'Calcoli corretti: RR2 e differenza5 punti; test18VP/2FN/49FP/931VN, VPP26,87%; mini4%,8%,2,67%,RR3,differenza5,33 punti.',
'SA03/06':'Caso con parametri presente, ma soluzione da rendere maggiormente discriminante; residui di pipeline.',
'SA03/07':'Tre casi coerenti e distinti per profilo; errore accertato nel codice CNOP e residui di pipeline.',
'SA04/01':'Classificazione P,R,M,P,R,M,M,R corretta nel contesto; distinguere modalità del bando da obblighi generali.',
'SA04/02':'Casi coerenti sul contenimento delle non conformità; insufficiente sviluppo delle discipline e della biosicurezza normativa.',
'SA04/03':'Cinque classificazioni coerenti; Bq/Gy/Sv e DRL distinti correttamente; raccomandazione Euratom2026/403 confermata.',
'SA04/04':'Cinque classificazioni e casi coerenti; termini vigilanza10/30giorni confermati, con natura obbligatoria/facoltativa distinta; integrare definizioni/classi.'}
for k in chap: report.append('| '+k+' | '+notes[k]+' |')
report += ['\n## 5. Coerenza globale\n',
'La matrice del volume dichiara 41 nuclei completi e otto righe SA01; la matrice SA01 corrente ne contiene dodici dopo le quattro integrazioni. Aggiornare il totale aggregato a 45 solo dopo la riconciliazione sostanziale, senza usare il conteggio come attestazione di completezza. La mappa fonti del luglio 2026 conserva fonti già acquisite come da acquisire e una chiusura che dichiara la scrittura bloccata: va storicizzata o riallineata.\n',
'Numerose source note dichiarano ancora parzialità e review indipendente pendente mentre le matrici attestano audit automatico chiuso. Non è prova automatica che ogni fonte sia invalida, ma manca una catena coerente e attuale di esiti. Caso specifico: matrice SA03 promette NSG coperto e fonte governance lo esclude. Riconciliare per claim.\n',
'Le ripetizioni su verificare fonte, setting e confine professionale occupano spazio sottratto alle definizioni. Ridurre ripetizioni e usare rinvii interni precisi: SA02/07→SA03/03, SA02/08→SA03/05, SA04/04→SA01/10. Non accorpare profili diversi né richiedere specialità escluse dalla Bibbia.\n',
'## 6. Contenuti verificati e da verificare\n',
'Riscontri esterni mirati effettivamente consultati, non audit integrale di tutti gli atti. I seguenti confermano correzioni o claim indicati; per proposte di nuove tabelle/termini occorre verifica puntuale prima della futura redazione.\n']
for e,(t,u) in urls.items(): report.append(f'- {e}: [{t}]({u}).')
report += ['\nE19 verificato anche sulla copia ufficiale locale: articoli finali nelle pagine PDF27 e51 stabiliscono il trentesimo giorno successivo alla pubblicazione. Non attestata l’assenza di ogni successiva intesa regionale/nazionale sull’accreditamento. ISS-BLS giugno2026: la pagina pubblica è stata respinta dal WAF; tale controllo esterno resta limitato, non viene dichiarato concluso. Le note ufficiali acquisite non equivalgono a lettura integrale di tutte le migliaia di pagine dei corpus raw.\n',
'## 7. Suggerimenti facoltativi\n',
'Una pagina di navigazione per ciascun profilo, un caso concluso per famiglia e un glossario delle sigle ridurrebbero il carico dei rinvii. Per la ricerca di evidenze è utile un esempio completo di interrogazione bibliografica. Una batteria finale può separare conoscenze disciplinari e ragionamento organizzativo.\n',
'## 8. Priorità operative\n',
'1. Correggere NEWS2, codice CNOP, accesso a dati sanitari, termini documentazione, inglese e spiegazioni PASSI.\n2. Completare definizioni e teoria nazionale dei nuclei dichiarati completi, mantenendo le esclusioni cliniche del progetto.\n3. Rendere risolvibili e differenziati i casi; controllare nuovamente tutte le soluzioni toccate.\n4. Allineare fonti, matrici, titolo e rinvii; togliere residui di pipeline.\n5. Rigenerare il candidato da testi aggiornati e ripetere controllo PDF.\n',
'## 9. Giudizio di pubblicabilità\n',
'**Non pubblicabile allo stato esaminato.** La revisione testuale è integrale per il corpus dichiarato. Nessuna autorizzazione alla pubblicazione è implicita nei precedenti gate o nel presente controllo. Non sono state applicate correzioni.\n',
'## 10. Limiti e tracciabilità\n',
f'Ledger: `artifacts/review-integrale-2026-10-02/VOL-07-ledger.json`; checkpoint di lettura nella stessa cartella. File capitolo cambiati dopo la lettura: {changed if changed else "nessuno"}. ',
'`quizReview: complete` significa verifica dei materiali effettivamente presenti, non validazione clinica esterna né esistenza di MCQ in ogni capitolo. Tutte le chiavi a scelta multipla lette sono semanticamente coerenti con le opzioni; non trovato il difetto di rimappatura delle lettere segnalato in altri volumi. La classificazione inglese e gli esercizi PASSI richiedono però le correzioni indicate. Per PDF, export e confronto con le versioni congelate vedere il rapporto separato e l’audit globale del coordinatore.\n']
out=Path('wiki/reviews/audit-integrale-2026-10-02/VOL-07.md'); out.write_text('\n'.join(report)+'\n',encoding='utf-8')
print(json.dumps({'report':str(out),'chapters':len(chap),'sources':len(d['supportingSources']),'findings':len(rows),'changed':changed}))
