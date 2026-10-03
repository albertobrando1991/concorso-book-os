from pathlib import Path
import json,hashlib
A=Path(__file__).parent
def read(name): return json.loads((A/name).read_text(encoding='utf8'))
def save(name,data): (A/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
m=read('VOL-01-native-pdf-map.json'); sheets=read('VOL-01-native-pdf-visual-ledger.json'); ledger=read('VOL-01-native-ledger.json')
assert len(sheets)==49 and all(r['visualReviewed'] for r in sheets)
orphans=[47,134,166,225,314,349,353,356,369,399,406,424,439,456,461,485,495,508,549,551]
findings=[]
for p in orphans:
 rows=[r for r in m['native'] if r['start']==p and r['end']>p]
 findings.append({'page':p,'nextPage':p+1,'ids':[r['id'] for r in rows],'issue':'Titolo e descrizione dello schema nella pagina precedente al corpo dello schema.','status':'pending-renderer'})
for r in m['native']:
 r['visualReview']=True
 r['layoutFinding']=any(r['id'] in f['ids'] for f in findings)
for r in m['protected']: r['visualReview']=True
pdf=Path(m['pdf']);pdfhash=hashlib.sha256(pdf.read_bytes()).hexdigest()
for r in ledger:
 p=next(x for x in m['native'] if x['id']==r['id'])
 r['pdfReview']='complete-with-layout-finding' if p['layoutFinding'] else 'complete'
 r['pdfPages']=p['pages'];r['proofSHA256']=pdfhash
 r['currentChapterSHA256']=hashlib.sha256(Path(r['chapter']).read_bytes()).hexdigest()
save('VOL-01-native-pdf-map.json',m);save('VOL-01-native-ledger.json',ledger)
save('VOL-01-native-layout-findings.json',{'pdf':str(pdf),'sha256':pdfhash,'pages':670,'selectedPages':194,'sheetsViewed':49,'nativeReviewed':133,'protectedReviewed':19,'findings':findings,'otherOrphans':[462,476,492,537,394],'caseCorrectionsAfterProof':['diario-degli-errori.md: domanda Perché il diario','famiglie-concorsi-pubblici.md: domanda Perché un candidato'],'miniExercise19':'Titolo, introduzione e griglia uniti a pagina 459; verificato visivamente.','crossReference20':'Le percentuali dell’esempio precedente: corretto nel manoscritto e verificato nel PDF a pagina 478.','limitations':['Non è una rilettura integrale delle 670 pagine.','Modifiche di maiuscole successive alla prova da rigenerare.','Difetti di raccordo titolo-corpo ancora aperti.']})
print(json.dumps({'native':133,'protected':19,'sheets':49,'orphans':len(findings),'ids':[f['ids'] for f in findings]}))
