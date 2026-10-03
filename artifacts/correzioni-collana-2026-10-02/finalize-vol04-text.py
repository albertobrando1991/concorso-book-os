from pathlib import Path
import re,json,hashlib,collections,datetime
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia');V=Path('wiki/books/vol-04-giustizia-upp');R=Path('wiki/reviews/pipeline/VOL-04')
chapters=sorted((B/'chapters').glob('*.md'))
sourceRefs=[p.relative_to('wiki').as_posix() for p in Path('wiki/sources').glob('vol-04-*-verifica-2026-10-03.md')]
# Front matter and index must describe this revision, not the previous candidate.
for p in (V/'front-matter').glob('*.md'):
 t=p.read_text('utf-8').replace('18 agosto 2026','3 ottobre 2026').replace('Edizione revisionata: agosto 2026','Edizione revisionata: ottobre 2026')
 t=t.replace("Il volume è autonomo e contiene tutto il percorso editoriale dichiarato nell'indice.","Il volume contiene spiegazioni, esercizi e soluzioni del percorso specialistico dichiarato nell'indice. Presuppone le basi comuni richiamate nella premessa; appendici e simulazioni si svolgono senza servizi digitali aggiuntivi.")
 t=t.replace('verso M-SP03/VOL-12','verso il VOL-12, Carriere speciali premium, parte Magistratura, Avvocatura e Notariato, nelle sezioni «Mappa delle tre professioni e scelta del binario» e «Magistratura ordinaria: accesso, prove e ordinamento»')
 t=t.replace('- ISBN: da associare al canale di pubblicazione prima della distribuzione commerciale.\n','')
 if p.name.startswith('05-'):t+='\nPer profili giuridico-pedagogici o di servizio sociale, questo volume sviluppa il quadro giuridico e organizzativo della giustizia. Le discipline professionali ulteriori richieste dal singolo bando richiedono lo studio specifico indicato dal relativo programma.\n'
 p.write_text(t,'utf-8')
for p in [V/'index.md',B/'index.md']:
 t=p.read_text('utf-8');t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1);t=t.replace('review_required: false','review_required: true').replace('status: reviewed','status: revised_draft')
 t=t.replace('Il volume ha completato revisione editoriale, fact-check prioritario, proofreading, controllo didattico e preflight del PDF KDP. I quattordici capitoli disciplinari, le appendici, i cinque strumenti operativi, la conclusione e l’apparato delle fonti sono presenti. Restano le normali verifiche di aggiornamento immediatamente precedenti alla distribuzione e l’eventuale produzione di un EPUB, non prevista dall’esportatore corrente.','Il testo corretto al 3 ottobre 2026 comprende 14 capitoli disciplinari, 84 quiz, sei simulazioni finali risolte e gli apparati. Il nuovo audit specialistico, il freeze e il PDF devono essere chiusi nel ciclo corrente; le verifiche del candidato di agosto non attestano la nuova pubblicabilità.')
 # The existing paragraph uses straight apostrophes.
 t=re.sub(r'Il volume ha completato revisione editoriale, fact-check prioritario.*?esportatore corrente\.', 'Il testo corretto al 3 ottobre 2026 comprende 14 capitoli disciplinari, 84 quiz, sei simulazioni finali risolte e gli apparati. Audit specialistico, freeze e PDF devono essere chiusi nel ciclo corrente; le verifiche del candidato di agosto non attestano la nuova pubblicabilità.',t,flags=re.S)
 t+='\n\n## Delta normativo del 3 ottobre 2026\n\n'+ '\n'.join('- [['+s.removesuffix('.md')+']]' for s in sourceRefs)+'\n'
 p.write_text(t,'utf-8')
# Preserve the former matrix as an audit artifact before replacing it with actual evidence.
p=V/'planning/02-matrice-copertura-didattica.md';old=p.read_text('utf-8');arc=A/'VOL-04-matrice-prima-riallineamento.md'
if not arc.exists():arc.write_text(old,'utf-8')
fm=old.split('---',2)[1].replace('review_required: true','review_required: false').replace('draft_stage: reviewed','draft_stage: editorial-revision')
fm=re.sub(r'source_refs: \[.*?\]','source_refs: '+json.dumps(sourceRefs),fm,flags=re.S)
rows=[
('Sistema e profili','funzione giudiziaria/giudicante/requirente; amministrazione; confini disciplinari','organizzazione-upp','Mappa bando/ufficio e correzione del cambio civile-DAP','Caso di classificazione, quiz1–6'),
('Ministero','cinque dipartimenti; DAG/DOG; quattro direzioni DIT; archivi notarili','organizzazione-upp','Mappa competenze e soggetti, DGSIA storica','Caso bando, quiz1–6'),
('Uffici giudiziari','merito/legittimità; GIP/GUP; assise; territorio; doppia dirigenza','organizzazione-upp','Tavole funzioni/composizione e caso di attribuzione','Caso e quiz1–6'),
('UPP','sedi/composizione/coordinamento; DL100/L145; DL144art7; struttura/personale','organizzazione-upp','Progetto, mansioni e limiti decisori','Caso arretrato e quiz1–6'),
('Lavoro AUPP','atti/allegazioni; cronologia; questione; udienza; ricerca; nota','processo-civile','Dossier8documenti e quattro prodotti compilati; simulazione15.1','Dossier guidato,6quiz e rubrica finale30punti'),
('Civile operativo','termini120/150,10/70,15/55/45,40/20/10; riti; provvedimenti; impugnazioni','processo-civile','Calendario udienza29giugno; confronto ordinario/semplificato/lavoro','Caso calendario e6quiz'),
('Penale operativo','335/45bis; qualità60; indagini/415bis; archiviazione; fascicoli; riti; impugnazioni','processo-penale','Cronologia6atti; simulazione15.2 interrogatorio e termine20','6quiz e rubrica finale30punti'),
('Cancelleria','registri21/44/45/45bis e civili; copie475; accesso76/116; dati9/10/51','cancelleria','Rettifica RG e richieste di accesso con titolo e limiti','Dossier e6quiz'),
('Spese','CUscaglioni/minimo; reddito13659.64/famiglia; ammissioni; liquidazioni/opposizione; recupero','spese','Calcoli familiari e CU; ramoCOApendente;SPEdiGIUS;simulazione15.3','6quiz,calcoli,soluzioni e rubrica30'),
('Casellario','iscrizione/imputato; menzionabilità/eliminazione;25bis;visura;PDND;40','casellario','Dossier4richieste;cooperativaminori in15.3','6quiz e soluzioni'),
('UNEP','competenza;139/140/143;relata;474–482;forme pignoramento;492bis;offertareale','unep','Relata e verbale negativo;calendario10/90/45;simulazione15.4','6quiz e rubrica30'),
('Digitale','196sexies+art17c11primaPEC;WARN/ERROR/FATAL;PPT2026–30;registri;malfunzionamenti','digitale','Tre depositi con orari/esiti;atto.enc/PDP;simulazione15.3','6quiz e caso12punti'),
('Minorile e comunità','età/imputabilità;MAPminori/adulti;misure121;garanzie riparative','minorile-penitenziario','Confronti istituti;progetto correttivo in15.5','6quiz e simulazione30punti'),
('Penitenziario','istituti;programma6mesi;misure/soglie;35bis/ter;giurisprudenza;656','minorile-penitenziario','Calcoli60/10e60x8;programma/affidamento/rimedi in15.6','6quiz e simulazione30punti')]
body='''\n\n# Matrice di copertura didattica — VOL-04\n\nRicostruita sul testo corretto al3ottobre2026. Copertura significa regola spiegata, applicazione e verifica nel perimetro amministrativo/operativo dichiarato; non copertura universale di ogni bando o delle discipline pedagogiche esterne. Il testo resta legacy, senza promozione al formato2. Le verifichePDF e i gate finali sono separati.\n\n| Capitolo/materia | Nuclei effettivamente sviluppati | Fonte del delta | Applicazione/output | Verifica | Stato |\n|---|---|---|---|---|---|\n'''
for i,(name,nuc,src,app,test) in enumerate(rows,1):body+=f'| {i:02} — {name} | {nuc} | [[sources/vol-04-{src}-verifica-2026-10-03]] | {app} | {test} | completo nel perimetro dichiarato |\n'
body+='''\n## Apparati e rinvii\n\n15: cinque strumenti e sei simulazioni con dati/soluzioni/rubriche;16: conclusione ancorata alle prove presenti;17: riferimenti percapitolo, norme vigenti e decisioni distinte dai comunicati. Le basi comuni rinviano aVOL01 con titoli nelcap15; il percorsoMagistratura rinvia aVOL12sezioni nominate senza promettere un manuale istituzionale completo.\n\n## Esito testuale e limiti\n\nLe29criticità del precedente audit hanno interventi identificabili e verifiche nel registroVOL04. La presenza di6quiz non è da sola la prova di copertura: la colonna nuclei indica ciò che è stato sviluppato. Mancano ancora audit15/freeze16 del ciclo corrente e controllo del nuovoPDF; nessuna pubblicabilità attestata da questa matrice. ISBNcanale finale da associare prima distribuzione, senza segnaposto nel libro.\n'''
p.write_text('---'+fm+'---'+body,'utf-8')
# Current textual evidence, without altering the immutable 2 October audit.
data=[];keys=[]
for i,p in enumerate(chapters,1):
 t=p.read_text('utf-8');k=[a or b for a,b in re.findall(r'Risposta corretta: ([A-D])|\*\*Risposta ([A-D])\.',t)];keys+=k
 assert len(k)==(6 if i<=14 else 0)
 data.append(dict(chapter=i,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),quizKeys=k,words=len(t.split('---',2)[-1].split())))
assert datetime.date(2026,10,6)+datetime.timedelta(days=20)==datetime.date(2026,10,26)
assert datetime.date(2026,3,3)+datetime.timedelta(days=90)==datetime.date(2026,6,1)
assert 237-43==194 and 60//10==6 and 60*8==480
e=dict(date='2026-10-03',chapters=data,quizTotal=len(keys),keyDistribution=dict(collections.Counter(keys)),finalSimulations=6,publicationReady=False,remaining=['audit15','freeze16','PDF','revisione21','preflight22','pacchetto23','conferma24'])
(A/'VOL-04-text-verifica.json').write_text(json.dumps(e,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps({k:v for k,v in e.items() if k!='chapters'},ensure_ascii=False))
