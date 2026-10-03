from pathlib import Path
import re,json,hashlib,shutil
A=Path(__file__).parent;B=Path('wiki/books/il-metodo-bando');R=Path('wiki/reviews/pipeline/VOL-01')
archive=A/'before-text/VOL-01/review-reconciliation';archive.mkdir(parents=True,exist_ok=True)
for p in [B/'planning/00-scheda-pipeline.md',B/'planning/02-matrice-copertura-didattica.md',R/'14-il-metodo-bando.md']:
 target=archive/p.name
 if not target.exists():shutil.copy2(p,target)
fixes=[
'Separati programma, fase, peso/soglia e priorità personale nelle tre destinazioni.',
'Sport collocato nell’art.33, fuori dai principi fondamentali.',
'Preavviso obbligatorio per riunioni in luogo pubblico, distinto da autorizzazione.',
'Riserva di legge riferita ai trattamenti obbligatori; consenso distinto.',
'Aggiunti composizioni, elettorato, quorum, termini e sedi parlamentari; sei quiz e caso con maggioranze.',
'Art.90 circoscritto agli atti funzionali.',
'Separati controllo preventivo sugli atti, successivo sul bilancio e giurisdizione.',
'Distinti ente, organo e fonte; rinvii nominativi ai due capitoli specialistici locali.',
'Completate sette istituzioni UE e decisioni con o senza destinatari designati.',
'Separati struttura dell’atto, motivazione, vizi e nullità; esempio di diniego.',
'Termini procedimentali, SCIA, conferenze 2026, revoca e non annullabilità con casi e sei verifiche.',
'Concessione definita attraverso trasferimento del rischio operativo.',
'Riserva, preferenza e titoli valutabili distinti con tre graduatorie didattiche; glossario coordinato.',
'Art.317: entrambi i soggetti attivi, costrizione senza requisito autonomo di irresistibilità.',
'Art.3 D165, disciplina 10/30/20/120 giorni e PIAO; precisato il confine dei 50 dipendenti.',
'FOIA: interessi tipizzati e pregiudizio concreto, limiti assoluti/relativi e accesso parziale.',
'Canale interno obbligatorio nel campo pubblico; termini e condizioni ANAC/divulgazione distinti.',
'FOIA 30/10/15/20, GDPR un mese più due, data breach 72 ore, DPIA e divieti sanitari con casi.',
'Residui statali e armonizzati distinti; accertamento/impegno spiegati anche nelle 100 parole.',
'Insussistenza distinta da reimputazione; risultato 120, quota disponibile25, FPV/FCDE con calcoli.',
'Rinvio al capitolo9 corretto; CIG e CUP non alternativi.',
'Trattativa diretta con un unico operatore, distinta dal confronto di preventivi.',
'Soglie UE2026, diretto/negoziata, programmi triennali, livelli e art.101 con termini.',
'RUP al primo atto; caso informatico80.000 e variante150.000 risolti.',
'Percorso e URL validi, dichiarati esempi sintattici.',
'Documento informatico distinto da originalità ed efficacia della copia; glossari coordinati.',
'PEC e recapito certificato qualificato; email ordinaria esclusa dal domicilio digitale.',
'Open data: requisiti congiunti e regime economico, teoria/soluzioni/glossario coerenti.',
'JOIN/ORDER BY/chiave esterna eseguiti su database; formule e stampa unione riproducibili.',
'Quiz1/9/10 inglese resi univoci, dieci soluzioni commentate.',
'Its determinante e uso con own distinti dal possessivo autonomo ordinario.',
'Promessa linguistica delimitata; aggiunti passato, interrogative/negative e confronti.',
'Necessità compatibile con sufficienza; disgiunzione inclusiva/esclusiva esplicita.',
'Distribuzione10/40/30/20%=100%, su60ore; adattamento a totale invariato.',
'Valore atteso con premi, penalità, omissioni, due quiz e limite rispetto all’obiettivo di soglia.',
'Richiesta istruttoria completa con termine derivato dal dossier e acquisizione d’ufficio.',
'Quattro dossier autonomi risolti: integrazione, accesso, ritardo e acquisto urgente.',
'Otto situazionali con alternative plausibili, commenti e chiavi A/C/B/D/A/C/B/D.',
'13 mappe dichiarate selezione delle15 famiglie, raccordi e limiti qualitativi espliciti.',
'Eliminati riuso80% non documentato e lessico commerciale interno.',
'Piani15/30/60/90 con1/2/4/6giorni residui e griglia coerente.',
'Marta36corrette/12errate/2omesse:33punti,72%quesiti e75%risposte; lacuna/recupero e N/A distinti.',
'Campi misure DSA/disabilità, gravidanza/allattamento, riserve e preferenze, con ambito DPR487.',
'Eliminate garanzia del Decoder e colpevolizzazione; fattori di esito espliciti.',
'RPD informa/consiglia/sorveglia; finalità e mezzi al titolare, senza conflitti.',
'Area/famiglia, soggetti del Codice e aggiudicazione/stipula distinti.',
'Persona fisica nella definizione dati, performance distinta dalla misurazione, facilita corretto.',
'Ripristinato il nome Sara.',
'Rimossi riferimenti staff dal corpo; corretta anche una dipendenza storica mal localizzata.',
'Premessa coerente con pagina digitale; condizioni e collaudo effettivo ancora da completare.',
'Edizione2026 e data3ottobre aggiunte; recapito errata e identificativi effettivi ancora aperti.'
]
rows=json.loads((A/'registro-applicazione.json').read_text(encoding='utf8'));selected=sorted([x for x in rows if re.fullmatch(r'V01-\d+',x['id'])],key=lambda r:r['id']);assert len(selected)==51
structure=json.loads((A/'VOL-01-structure.json').read_text(encoding='utf8'));assert not structure['missingImages'] and not structure['internalBodyRefs'] and not structure['missingSourceRefs']
sources=sorted([p for p in Path('wiki/sources').glob('vol-01-*-2026-10-0[23].md') if any(z in p.name for z in ['correzioni','esempi-logica'])]);assert len(sources)==7,len(sources)
groups={
'V01-ARCH':(['V01-39','V01-40','V01-44','V01-49'],'Perimetro32unità, rinvii e promesse riesaminati.'),
'V01-MET':(['V01-01','V01-43','V01-49'],'Bando: programma, prova, peso e priorità separati; controlli candidatura espliciti.'),
'B-PA01':([f'V01-{n:02}' for n in range(2,10)],'Costituzione, regolamenti parlamentari, UE e distinzione ente/organo/fonte.'),
'B-PA02':(['V01-10','V01-11','V01-12','V01-36','V01-37'],'Termini e istituti aggiornati, casi risolti; INT01/02 preservati.'),
'B-PA03':(['V01-13','V01-15'],'Riserve/preferenze, ordinamenti, disciplina e PIAO; INT03 preservato.'),
'B-PA04':(['V01-14'],'Concussione: soggetti e distinzione dalla induzione; restante audit storico conservato.'),
'B-PA05':(['V01-19','V01-20','V01-21'],'Residui, risultato, fondi e identificativi; calcoli riprodotti.'),
'B-PA06':(['V01-22','V01-23','V01-24'],'Soglie2026, programmi, progettazione e soccorso; due importi nel caso.'),
'B-PA07':(['V01-16','V01-17','V01-18','V01-45'],'Accesso, segnalazioni e GDPR: regole, tempi, limiti e ruoli.'),
'B-PA08':(['V01-30','V01-31','V01-32'],'Quiz e possessivi verificati; base linguistica senza equivalenza QCER.'),
'B-PA09':(['V01-25','V01-26','V01-27','V01-28','V01-29'],'CAD e glossari coerenti; database e formule eseguiti.'),
'B-PA10':(['V01-33','V01-35','V01-38'],'Logica e probabilità esplicite, situazionali bilanciati; INT04 preservato.'),
'B-PA11':(['V01-36','V01-37'],'Modello di comunicazione e quattro dossier con decisioni qualificate.'),
'V01-PROVE':(['V01-34','V01-35','V01-36'],'Quote100%, valore atteso e condizioni della prova.'),
'V01-PROFILI':(['V01-39','V01-40','V01-41'],'Mappe qualitative e calendario completo, senza percentuali di riuso inventate.'),
'V01-KIT':(['V01-42','V01-43'],'Denominatori, categorie errori, misure di partecipazione e checklist.'),
'V01-APP':(['V01-01','V01-13','V01-19','V01-26','V01-27','V01-28','V01-39','V01-41','V01-43','V01-45','V01-46','V01-47','V01-48'],'Definizioni, strumenti e rinvii coordinati ai capitoli.')}
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8');lines=t.splitlines();new=[]
for line in lines:
 if line.startswith('| '):
  c=[x.strip() for x in line.strip('|').split('|')]
  if c[0] in groups:
   ids,note=groups[c[0]];linked=sorted({Path(f).stem for r in selected if r['id'] in ids for f in r.get('changedFiles',[]) if '/sources/' in f})
   c[3]+='; '+'; '.join('[[sources/'+s+']]' for s in linked)
   c[4]=re.sub(r'\[\[([^\]#]+)#[^\]]+\]\]',r'[[\1]]',c[4])
   c[10]='Delta ricontrollato il3ottobre2026: '+', '.join(ids)+'. Audit specialistico step15 prima del freeze; conferma umana soltanto finale.'
   c[11]='—';c[12]=note+' Evidenze e limiti: [[reviews/correzioni-collana-2026-10-02/VOL-01]].'
   line='| '+' | '.join(c)+' |'
 new.append(line)
t='\n'.join(new)+'\n';t=t.replace('updated_at: 2026-10-02','updated_at: 2026-10-03')
start=t.index('Il conteggio parole non prova');end=t.index('\n## Matrice obbligatoria',start)
t=t[:start]+'Il conteggio parole non prova la completezza. Le21righe sono aggregati didattici legacy, non nuclei del formato2. Il controllo integrale iniziale e la verifica dei49delta testuali sono documentati nel nuovo report. Le date delle fonti storiche non diventano automaticamente3ottobre: i riscontri nuovi sono puntuali e tracciati. I preliminari conservano due rilievi aperti; layout, PDF e conferma conclusiva restano separati. Nessuna modifica alle integrazioni INT01–08 estranee al delta.\n'+t[end:]
start=t.index('## Esito di copertura dopo la verifica delle integrazioni')
t=t[:start]+'''## Esito della riconciliazione del 3 ottobre 2026

I17aggregati storici e le4integrazioni INT01–04 restano sviluppati;49rilievi testuali sono stati corretti e ricontrollati rispetto all’audit iniziale. La tabella mantiene distinti la copertura e i gate specialistici/di produzione: non equivale a una certificazione del PDF. Nessuna migrazione fittizia al formato2. L’inventario VOL-01-structure.json identifica le32unità e gli hash; zero immagini mancanti, riferimenti interni nel corpo o dipendenze fonte mancanti nel controllo indicato.

I preliminari non sono assorbiti nelle21righe: V01-50 e V01-51 restano parzialmente applicati, in attesa dei dati reali su servizio digitale, errata e identificativi editoriali. Il cartaceo rimane autonomo. La conferma umana è quella conclusiva dello step24.
'''
p.write_text(t,encoding='utf8')
p=B/'planning/00-scheda-pipeline.md';t=p.read_text(encoding='utf8').replace('cut_off_date: 2026-08-21','cut_off_date: 2026-10-03',1).replace('updated_at: 2026-10-02','updated_at: 2026-10-03',1)
start=t.index('## Ciclo di integrazione del 2 ottobre 2026');end=t.index('## Perimetro escluso',start)
t=t[:start]+'''## Correzioni integrali del 3 ottobre 2026

Il ciclo corrente comprende i49rilievi del testo delle32unità autoriali e i due rilievi dei preliminari, oltre alle figure e all’impaginazione. Il precedente delta INT01–04 e le altre integrazioni esistenti sono preservati; i vecchi report sono archiviati prima della sostituzione. Cut-off dell’edizione3ottobre2026: i nuovi riscontri sono puntuali, con fonti e limiti nel report, senza dichiarare una lettura integrale aggiornata di ogni norma.

Target CLI: `il-metodo-bando`. La matrice conserva21aggregati legacy e aggiunge il collegamento ai49rilievi, senza promozione al formato2. Dopo step14 e15 occorre un nuovo freeze dei32testi; i preliminari con dati ancora pendenti e ogni prova PDF sono esclusi da quel giudizio. Nuova impaginazione, controllo di tutte le pagine e preflight richiesti prima della consegna. V01-50/51 non si chiudono tramite il freeze dei capitoli.

'''+t[end:];p.write_text(t,encoding='utf8')
out='''# Report editoriale — Correzioni integrali VOL-01

## 1. Sintesi editoriale

Manuale-workbook nazionale per concorsisti. Riconciliati i32testi del cartaceo con l’audit integrale iniziale e riesaminati i49interventi testuali: correzioni concettuali/normative, integrazioni teoriche e applicative, quiz, definizioni e strumenti. I due rilievi dei preliminari restano parzialmente applicati. Ricettario25–47 escluso. Le integrazioni preesistenti sono conservate. Il report non autorizza la stampa.

## 2. Punti applicati della checklist

Punti1–4: indice, perimetro e progressione. Punti6–15: copertura, coerenza, definizioni, casi, fonti e autonomia. Punti16–26 e29: lingua e forma dei delta, terminologia e residui editoriali. Punti5/30: giudizio limitato alle evidenze indicate. Punti27/28: Markdown e asset controllati; verifica del PDF corrente ancora da completare. L’audit iniziale resta immutato e identifica la posizione originale dei problemi.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione applicata | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
def cell(s):return re.sub(r'\s+',' ',str(s).replace('|','/')).strip()
for r in sorted(selected,key=lambda x:({'grave':0,'media':1,'medio':1,'lieve':2}.get(x['severity'].lower(),1),x['id'])):
 n=int(r['id'][-2:]);out+='| '+' | '.join(map(cell,[r['id'],r['position'],r['category'],r['severity'],r['description'],fixes[n-1],'Testo verificato; PDF separato' if n<=49 else 'Parziale; dati effettivi pendenti']))+' |\n'
out+='\n## 4. Osservazioni per capitolo\n\nInventario reale: titoli e consistenza sono controlli strutturali, non soglie sostitutive della qualità. I dettagli degli interventi sono nella tabella precedente.\n\n| Unità | Parole grezze | Figure | Rilievi applicati |\n| --- | ---: | ---: | --- |\n'
for unit in structure['units']:
 ids=[r['id'] for r in selected if unit['path'] in r.get('changedFiles',[])]
 out+='| '+Path(unit['path']).stem+' | '+str(unit['words'])+' | '+str(unit['images'])+' | '+(', '.join(ids) or 'Nessun delta obbligatorio nell’audit iniziale')+' |\n'
out+='''
## 5. Coerenza globale

Riconciliati glossari e capitoli per riserva/preferenza, residui, documento informatico, domicilio digitale, open data, RPD, performance e aggiudicazione. I calendari assegnano tutti i giorni; le percentuali dichiarano denominatore e limite. I31? conteggi non sono usati come prove: l’inventario effettivo contiene32unità. Nessun wikilink staff nel corpo, nessuna immagine mancante e nessuna fonte mancante nel controllo dei metadati. Una dipendenza storica del cap21 è stata corretta al percorso reale, senza alterare la fonte.

Le21righe della matrice sono aggregati legacy, non nuclei formato2. I controlli precedenti INT01–04 sono preservati e non assorbiti in una generica riscrittura. Gli esercizi numerici e SQL sono stati rieseguiti; le otto chiavi situazionali sono bilanciate e motivate. La qualità dei distrattori non equivale a validazione psicometrica.

## 6. Contenuto verificato e fonti

'''.replace('I31? conteggi non sono usati come prove: l’inventario effettivo contiene32unità.','L’inventario effettivo contiene32unità.')
out+=''.join('- [[sources/'+p.stem+']]\n' for p in sources)
out+='''
Le note distinguono fonti primarie, pagine effettivamente consultate, raw acquisiti e limiti dei riscontri. Verificati separatamente il regime attuale della sede redigente del Senato e l’esito referendario2026, senza usare vecchie versioni o progetti come norme vigenti. Calcoli, SQL, calendario e distribuzione delle risposte sono verifiche dirette; non provano da soli ogni proposizione normativa del volume.

## 7. Suggerimenti facoltativi

Ulteriori batterie possono estendere l’allenamento. Non si promettono equivalenza a un livello QCER, successo concorsuale o copertura universale di tutti i bandi.

## 8. Priorità degli interventi

Concludere audit specialistico e congelamento tramite CLI. Rigenerare il PDF con le19figure corrette e la nuova tipografia, controllare integralmente pagine, indice e rinvii. Completare i dati reali di V01-50/51 e verificare il flusso di attivazione prima del pacchetto finale.

## 9. Giudizio di pubblicabilità

**Pubblicabile dopo intervento medio di produzione e completamento dei preliminari.** I49rilievi dei capitoli sono risolti nel testo riesaminato; i preliminari e il nuovo impaginato non sono certificati. Nessuna pubblicazione esterna o approvazione conclusiva eseguita.

## 10. Limiti della revisione

Il controllo si appoggia alla lettura integrale iniziale e alla rilettura delle modifiche e dei raccordi, non a una nuova attestazione astratta di perfezione. Norme e fonti sono puntuali e datate; il digitale non è stato collaudato con account reale. Il precedente PDF non rappresenta i manoscritti correnti. Evidenze: VOL-01-structure.json, vol01-esempi-verificati.json, figure-vol01-corrette-manifest.json e registro-applicazione.json. I report storici rimangono archiviati.
'''
for old,new in [('32testi','32 testi'),('32unità','32 unità'),('49interventi','49 interventi'),('49rilievi','49 rilievi'),('21righe','21 righe'),('19figure','19 figure'),('17aggregati','17 aggregati'),('4integrazioni','4 integrazioni')]:out=out.replace(old,new)
(R/'14-il-metodo-bando.md').write_text(out,encoding='utf8');Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-01.md').write_text(out,encoding='utf8')
for r in selected:
 if int(r['id'][-2:])<=49:
  r['status']='applicato-verificato-testo';r['textVerified']=True;r['finalPublicationVerified']=False
  r['verification']=['Rilettura dei delta e raccordi; report14 aggiornato','32unità: riferimenti e immagini presenti, corpo autonomo','Esempi numerici/SQL rieseguiti; matrici riconciliate','PDF corrente e preliminari ancora da chiudere']
  r['fileHashes']={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in r.get('changedFiles',[]) if Path(f).exists()}
(A/'registro-applicazione.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print({'textFindingsVerified':49,'preliminaryFindingsPartial':2,'units':32,'sources':len(sources)})
