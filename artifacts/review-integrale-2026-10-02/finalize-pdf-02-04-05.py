import json, hashlib, pathlib
R=pathlib.Path(__file__).resolve().parents[2]
A=R/'artifacts/review-integrale-2026-10-02'
W=R/'wiki/reviews/audit-integrale-2026-10-02'
inventory=json.loads((A/'pdf/inventory.json').read_text(encoding='utf-8-sig'))
config={
'02': dict(pages=867,sheets=37,stem='vol-02-interior-kdp-rebuild',zooms=[6,27,148,184,292,315,576,580,655,730,832,867],rows=[
('p.292, Capitoli da attivare','Rinvii','Grave','«Capitolo 3 su uffici e organizzazione», «4 su atti», «5 su procedimento», «6 su gestione documentale», «12 su procurement» usano i numeri locali del modulo, incompatibili con indice e intestazioni stampate.','Convertire rispettivamente in capitoli 6, 7, 8, 9 e 15; controllare tutti i rinvii locali durante l’assemblaggio, mantenendo anche titolo del capitolo.'),
('p.184, tavola obiettivo-risorsa-responsabile-indicatore','Impaginazione','Media','Le celle spezzano parole senza sillabazione: «Document/i interessat/i», «Responsa/bile», «investimento» e «manutenzione» con una lettera su nuova riga.','Ribilanciare colonne, abbreviare le intestazioni e usare interruzioni linguistiche; se necessario dividere la tavola in due tabelle coordinate.'),
('p.148, apertura capitolo 11','Gerarchia dei titoli','Lieve','Il titolo Welfare locale… compare due volte consecutive, nero grande e bordeaux, prima di Obiettivo del capitolo. Il modello ricorre in altre aperture.','Eliminare il duplicato sorgente/renderizzato e conservare un solo titolo di capitolo.'),
('p.730, ultima pagina capitolo 39','Paginazione','Media','Una pagina intera contiene soltanto «procedure e modulistica dell’ente, verificate rispetto alla disciplina vigente».','Ricondurre l’ultimo punto elenco alla pagina precedente intervenendo su spaziature o blocchi indivisibili; controllare analoghi finali brevi nelle altre sezioni.'),
('pp.315 e 580, figure 18.1 e 30.1; tutti i 10 asset','Leggibilità delle figure','Media','Le etichette secondarie risultano molto più piccole del testo del manuale; titoli gialli su fondi chiari hanno contrasto debole. Il largo spazio vuoto non si traduce in caratteri più leggibili.','Ridisegnare le tavole per la misura effettiva nel libro: aumentare corpo e contrasto, ridurre spazi vuoti, verificare una prova in scala reale e in grigio.'),
('p.27, Riferimenti consolidati e Note di review','Apparati','Media','Restano etichette interne come «Template Bando Decoder Metodo Bando», «Logica Volumi Copertura Concorsobook V4» e il titolo «NOTE DI REVIEW». Non sono riferimenti bibliografici recuperabili dal lettore.','Trasformare i riferimenti utili in citazioni o rinvii leggibili e rinominare l’avvertenza per il lettore; escludere i riferimenti di lavorazione. Riscontro grafico dei rilievi testuali sugli apparati.'),
('p.320, figura 18.4; asset FL02/chapter-01/04-catena-avviso-regionale-comuni.png','Figura illeggibile','Grave','I bollini numerati coprono l’inizio delle parole Programma, Domanda, Istruttoria, Concessione, Attuazione e Monitoraggio. Difetto presente nel PNG originale 1600×900.','Separare il numero dal titolo della fase riservando due righe o un margine laterale adeguato; rigenerare e controllare sia PNG sia resa PDF.'),
('Figure 18.2, 18.3, 18.5, 30.2, 30.4; PNG originali','Ortografia nelle figure','Lieve','Gli asset perdono accenti: «Sussidiarieta», «Citta», «prossimita», «legalita», «pubblicita», «unita», «e» al posto di «è» in frasi complete.','Correggere le stringhe delle figure e preservare UTF-8 e caratteri accentati in generazione; rileggere gli asset, non solo le didascalie.'),
('p.584, figura 30.3; asset 03-sistema-camerale-unioncamere.png','Coerenza grafica','Media','La nota dice che la rete non è un comando gerarchico semplice, ma Unioncamere è in alto con frecce discendenti verso tutti gli enti, senza legenda sui rapporti.','Rappresentare una rete con collegamenti etichettati (rappresentanza, raccordo, servizi condivisi), evitando che la sola freccia verticale suggerisca subordinazione.')]),
'04': dict(pages=303,sheets=13,stem='vol-04-interior-kdp',zooms=[6,8,52,65,97,152,300,303],rows=[
('p.65, quiz 4–6 e continuazione quiz 3','Didattica dei quiz','Grave','La risposta corretta e il commento sono stampati prima delle alternative: per il quiz 4 si legge già «B» prima dell’elenco A/B/C.','Disporre domanda e alternative prima della soluzione; raccogliere le soluzioni commentate alla fine della verifica o in sezione separata.'),
('p.152, tabella della sequenza operativa','Impaginazione','Media','Le celle spezzano «Ricevuta/registr/o», «Cancelleria/UN/EP», «Traduzione/inte/rprete», «spese/magistrat/o». Non mancano lettere, ma la lettura è ostacolata.','Ribilanciare le colonne e riscrivere le etichette lunghe; evitare interruzioni arbitrarie all’interno delle parole e degli acronimi.'),
('p.8, apertura capitolo 1','Gerarchia dei titoli','Lieve','«Il sistema Giustizia visto dal candidato» è ripetuto in due titoli consecutivi, nero e bordeaux, separati soltanto dalla fascia BANDO.','Conservare un unico titolo di capitolo e iniziare subito con il primo sottotitolo effettivo; verificare le altre aperture con lo stesso modello.'),
('pp.97, 300 e 303','Paginazione','Media','Finali di capitolo occupati soltanto da pochi punti elenco o due brevi paragrafi, con quasi tutta la pagina vuota.','Ricomporre i blocchi di chiusura e le spaziature, mantenendo insieme checklist e conclusione quando possibile; non ridurre indiscriminatamente il corpo del testo.')]),
'05': dict(pages=213,sheets=9,stem='vol-05-interior-kdp',zooms=[6,10,14,18,37,46,137,213],rows=[
('pp.10, 14 e 137, figure 1.1, 1.2 e 10.4','Didascalie','Media','La didascalia grigia sotto l’immagine è seguita da una seconda didascalia nel corpo. A p.14 e p.137 tra le due compare perfino il titolo della nuova sezione.','Mantenere una sola didascalia canonica e unire figura e didascalia nello stesso blocco; collocare il titolo della sezione dopo il blocco completo.'),
('pp.37 e 137, figure 3.3 e 10.4; confronto con p.10','Leggibilità delle figure','Media','Etichette e sottotitoli nelle figure sono minuti rispetto al testo della pagina; le schede contengono ampi spazi vuoti e scritte gialle poco contrastate.','Aumentare corpo e contrasto delle etichette alla dimensione di stampa e ridurre l’area vuota; verificare gli originali e una prova in scala reale.'),
('p.37, figura 3.3; p.137, figura 10.4','Utilità didattica delle figure','Media','Nella sequenza «problema, coordinamento, istruttoria, esito» ogni scheda ripete «fatto, criterio, azione». Le tre distinzioni della figura 10.4 ripetono «definisci, distingui, applica». La grafica non esplicita passaggi, presupposti o conseguenze.','Sostituire le etichette generiche con dati e decisioni di un caso risolto; attribuire a ciascuna fase un contenuto diverso e verificabile.'),
('p.18, caso guidato, ripasso selettivo','Rinvii','Grave','È stampata la sequenza «su , e ;»: i rinvii mancanti del sorgente arrivano al lettore.','Ripristinare capitoli e nuclei corretti con titolo e numero; controllare l’assenza di riferimenti vuoti in tutti i casi. Riscontro PDF di V05-01, non ulteriore errore normativo.')])}
for num,c in config.items():
 v='VOL-'+num
 pdf='delivery/'+v+'/candidate/'+c['stem']+'.pdf'
 rec=next(x for x in inventory if x['file']==pdf)
 assert hashlib.sha256((R/pdf).read_bytes()).hexdigest()==rec['sha256']
 report='wiki/reviews/audit-integrale-2026-10-02/PDF-'+v+'.md'
 rows=[]
 for i,(pos,cat,sev,desc,fix) in enumerate(c['rows'],1): rows.append(f'| P{num}-{i:02} | {pos} | {cat} | {sev} | {desc} | {fix} | Aperto |')
 txt=f'''# Controllo visivo PDF — {v}

Data: 2 ottobre 2026. Revisione senza applicazione di correzioni.

**Candidato:** `{pdf}`. SHA-256: `{rec['sha256']}`.

Esaminati tutti i {c['sheets']} fogli di contatto, che coprono le {c['pages']} pagine del candidato, in ordine. Ingrandite e lette nelle parti pertinenti le pagine {', '.join(map(str,c['zooms']))}, renderizzate a 144 dpi. Le immagini di controllo sono in `artifacts/review-integrale-2026-10-02/pdf/{v}/`; i fogli del candidato sono nella sottocartella `{c['stem']}`.

**Limite:** la copertura visiva comprende tutte le pagine in miniatura, con controlli ravvicinati selettivi. Non equivale a una rilettura di ogni riga del PDF a piena leggibilità né a una prova fisica di stampa. La lettura integrale del testo sorgente è documentata separatamente in [{v}.md]({v}.md). Il controllo geometrico automatico del coordinatore è in `pdf/inventory.json`: nessuna pagina segnalata fuori area, vuota o con carattere sostitutivo; tali esiti non certificano leggibilità di immagini, correttezza dei rinvii o qualità della paginazione.

Nel controllo d’insieme non sono emersi tagli macroscopici del corpo del testo o sovrapposizioni tra corpo e piè di pagina. Il testo corrente nelle pagine ingrandite è leggibile. Restano aperti i rilievi seguenti, oltre ai rilievi sostanziali del rapporto testuale.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'\n'
 if num=='02':
  txt+='''
Il candidato precedente `vol-02-interior-kdp.pdf`, di 830 pagine, non è incluso in questa revisione visiva: non trasferire i numeri di pagina tra i due file. Il rebuild esaminato contiene 867 pagine. L’indice globale e i frontespizi verificati (pp.6, 576 e 655) usano correttamente 51 capitoli e i blocchi camerale 30–34 e PL 35–49. Le sequenze obsolete rinvenute nei sorgenti dei frontespizi non vanno quindi attribuite automaticamente a questo PDF; il difetto dei rinvii nel corpo a p.292 è invece confermato.

Esaminati anche **tutti i 10 PNG originali a risoluzione 1600×900**, oltre ai tre fogli di contatto delle figure. Manifest con percorsi e hash: `artifacts/review-integrale-2026-10-02/figures-VOL-02/manifest.json`. I dieci asset appartengono ai capitoli globali 18 e 30. Le etichette sono presenti nei raster, ma la scala nel libro le riduce; la figura 18.4 ha invece una sovrapposizione già nell’originale. Gli accenti mancanti sono difetti degli asset, non del testo estratto dal PDF.
'''
 if num=='04':txt+='\nL’errore normativo relativo alla conversione del DL 100/2026 è visibile anche alle pp.52 e 65 ed è trattato nel rapporto testuale V04-04: non è contato nuovamente tra i difetti di impaginazione. Il censimento dell’export corrente non contiene figure raster per questo volume.\n'
 if num=='05':txt+='\nIl volume contiene 75 figure nel censimento dell’export. Il presente rapporto ne valuta la resa complessiva attraverso tutte le pagine e approfondisce le figure nelle pagine indicate; il controllo integrale degli originali è affidato al coordinatore e va documentato separatamente. Le risposte generiche dei quiz a p.46 e la simulazione a p.213 confermano i rilievi testuali, senza costituire qui ulteriori errori di layout.\n'
 txt+='\n**Esito:** candidato da correggere e rigenerare prima della chiusura editoriale; successivo controllo delle pagine interessate e delle nuove interruzioni di pagina. Nessun file del libro o della pipeline modificato.\n'
 (R/report).write_text(txt,encoding='utf-8')
 lp=A/(v+'-ledger.json'); l=json.loads(lp.read_text(encoding='utf-8'))
 l['pdfReview']={'candidate':pdf,'sha256':rec['sha256'],'pages':c['pages'],'contactSheetsViewed':c['sheets'],'allContactSheetsViewed':True,'zoomPages':c['zooms'],'mode':'all-pages-contact-sheet-plus-targeted-full-page','fullLegibilityAllPages':False,'report':report,'findingIds':[f'P{num}-{i:02}' for i in range(1,len(c['rows'])+1)],'changesApplied':False}
 if num=='02':l['pdfReview']['originalFigures']={'count':10,'allViewedAtOriginalResolution':True,'manifest':'artifacts/review-integrale-2026-10-02/figures-VOL-02/manifest.json'}
 lp.write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 main=W/(v+'.md'); mt=main.read_text(encoding='utf-8')
 mt+='\n\n## Integrazione del controllo PDF\n\nControllo visivo completato su tutti i fogli di contatto del candidato, con ingrandimenti selettivi e limiti espliciti: [rapporto PDF-'+v+'](PDF-'+v+'.md). Questa integrazione aggiorna i precedenti rinvii al controllo PDF demandato al coordinatore; non dichiara una rilettura integrale del PDF a piena leggibilità.\n'
 main.write_text(mt,encoding='utf-8')
 print(v,c['pages'],len(c['rows']),rec['sha256'])
