from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');R=Path('wiki/reviews/pipeline/VOL-05')
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records=load(A/'VOL-05-native-schemes.json')['records'];check=load(A/'VOL-05-native-checkpoint.json');g=load(A/'VOL-05-FC05-gates.json')
assert len(records)==75 and len(g)==15 and all(x['result']['passed'] and not x['result']['warnings'] for x in g)
assert check['allQuizAndCaseBodiesPreserved'] and not load(A/'VOL-05-FC05-links.json')
delta='''

## Delta di produzione del 3 ottobre 2026 — 75 schemi nativi

Sostituiti i 70 diagrammi generici dei capitoli 2–15 e, dopo la prova PDF, le cinque tavole iniziali troppo minute. Gli originali raster restano invariati. Le nuove tabelle esplicitano competenze, distinzioni e condizioni già verificate nel testo; Consob non conduce automaticamente alla sanzione e la protezione whistleblowing accompagna il procedimento. BANDO significa Bando, Aree, Nuclei, Diario, Output. Il Decoder ha campi verticali compilabili, inclusa la scadenza della domanda.

La verifica differenziale confronta tutti i 15 hash del freeze originario e isola solo i 75 schemi, le vecchie didascalie e lo spostamento del confine del nucleo 8.3. Nessun testo teorico, quesito, caso o soluzione è stato omesso. Due schemi del capitolo 13, non più presenti dopo l'integrazione normativa, sono ripristinati con contenuto coerente. Tutti i 15 gate passano senza warning; zero rinvii irrisolti. Registro: `VOL-05-native-schemes.json`; controllo inverso: `VOL-05-native-checkpoint.json`.

La prima prova corrente conta 239 pagine, 90 voci di indice corrette e 75 schemi presenti, senza overflow. Visionate tutte le 15 tavole contatto; questa copertura non equivale alla lettura del testo minuto di ogni pagina. È in corso la verifica della proiezione che rende leggibili 20 link esterni e anticipa la bibliografia ANAC al caso conclusivo, preservando tutti i riferimenti. I master conservano link completi e ordine originale; il manifest registra la trasformazione di stampa.

Nessuna nuova regola normativa è introdotta dalla conversione. Restano validi ambiti e limiti delle note del 3 ottobre 2026. Non si dichiara la pubblicabilità finale; servizi digitali, dati editoriali commerciali e prova fisica restano separati.
'''
for p in [R/'14-moduli-m-fc05-authority-indipendenti.md',R/'15-moduli-m-fc05-authority-indipendenti.md',Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-05.md')]:
 s=p.read_text(encoding='utf8');marker='\n## Delta di produzione del 3 ottobre 2026 — 75 schemi nativi\n';p.write_text(s.split(marker)[0]+delta,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8');marker='\n## Delta degli schemi, 3 ottobre 2026\n';p.write_text(s.split(marker)[0]+marker+'\n75 tavole native specifiche, cinque per capitolo; nuclei, 90 quesiti, 15 casi finali e 10 simulazioni conservati. Il confine 8.3 precede le liste nere, senza spostare materia fra capitoli. Verifica differenziale e gate aggiornati negli artefatti VOL-05.\n',encoding='utf8')
f=A/'M-FC05-freeze.json';backup=A/'M-FC05-freeze-before-graphics.json'
if not backup.exists():shutil.copy2(f,backup)
d=load(f);d['controlledLayoutDelta']={'date':'2026-10-03','previousManifest':str(backup),'nativeSchemes':75,'allBodyOutsideDeclaredDeltaPreserved':True,'checkpoint':str(A/'VOL-05-native-checkpoint.json'),'projectionManifest':str(A/'vol05-proof/projection-manifest.json')}
for r in d['files']:
 old=r['sha256'];r['sha256']=sha(Path(r['path']))
 if old!=r['sha256']:r['preGraphicsSHA256']=old
save(f,d)
for p in [R/'16-moduli-m-fc05-authority-indipendenti.md',B/'planning/18-text-freeze-manifest.md']:
 s=p.read_text(encoding='utf8')
 for row in d['files']:
  if row.get('preGraphicsSHA256'):s=s.replace(row['preGraphicsSHA256'],row['sha256'])
 marker='\n## Delta controllato di produzione\n';s=s.split(marker)[0]+marker+'\n75 schemi nativi, didascalie uniformate e confine 8.3 riequilibrato. Snapshot originario preservato in M-FC05-freeze-before-graphics.json; corpo, quiz e casi controllati per inversione del delta. Hash della tabella aggiornati al master corrente; proiezione bibliografica tracciata separatamente.\n';p.write_text(s,encoding='utf8')
ledger=load(A/'VOL-05-ledger.json')
for r in ledger['files']:r['sha256']=sha(Path(r['path']))
ledger['controlledLayoutDelta']=d['controlledLayoutDelta'];save(A/'VOL-05-ledger.json',ledger)
progress=load(A/'VOL-05-progress.json');progress['pending']=['Verifica proiezione PDF finale','Pacchetto e dipendenze comuni'];progress['production']={'nativeSchemes':75,'firstProofPages':239,'allFirstProofContactSheetsViewed':True};save(A/'VOL-05-progress.json',progress)
proof=A/'vol05-proof';sheets=load(proof/'contact-ledger.json')
for s in sheets:s['viewed']=True
save(proof/'first-proof-visual-review.json',{'pdfSha256':load(proof/'verification.json')['pdfSha256'],'pages':239,'contactSheets':sheets,'allContactSheetsViewed':True,'findings':['20 external Markdown links printed literally','Chapter 14 final page 220 contains bibliography only'],'limitations':['Panoramic geometry review; not full-size reading of every page.']})
print('Audit addenda, matrix, controlled freeze and first visual review saved.')
