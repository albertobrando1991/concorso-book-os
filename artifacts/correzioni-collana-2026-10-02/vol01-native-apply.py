from pathlib import Path
import json,re,hashlib,sys,shutil
A=Path(__file__).parent;D=A/'vol01-native';B=Path('wiki/books/il-metodo-bando/chapters')
inv=json.loads((A/'VOL-01-native-inventory.json').read_text(encoding='utf8'));ledgerpath=A/'VOL-01-native-ledger.json'
ledger=json.loads(ledgerpath.read_text(encoding='utf8')) if ledgerpath.exists() else []
done={r['id'] for r in ledger};wanted=set(sys.argv[1:]);rows=[r for r in inv if r['id'] in wanted];assert len(rows)==len(wanted)
for r in rows:
 assert r['id'] not in done,'Gia applicato: '+r['id']
 p=B/r['chapter'];s=p.read_text(encoding='utf8');old=f"![{r['alt']}]({r['asset']})";assert s.count(old)==1
 backup=D/'before'/p.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():shutil.copyfile(p,backup)
 replacement=(D/(r['id']+'.md')).read_text(encoding='utf8').strip()
 assert replacement and '-stampa.png' not in old
 oldhash=hashlib.sha256(p.read_bytes()).hexdigest()
 s=s.replace(old,replacement)
 # La didascalia resta nella collocazione originaria come etichetta dello schema nativo.
 position=s.index(replacement)+len(replacement)
 tail=s[position:];tail=re.sub(r'^(\s*\*)Figura ([\d.]+)',r'\1Schema \2',tail,count=1)
 s=s[:position]+tail
 p.write_text(s,encoding='utf8')
 ledger.append({'id':r['id'],'chapter':p.as_posix(),'originalAsset':r['path'],'originalSHA256':r['sha256'],'originalPage':r['page'],'beforeChapterSHA256':oldhash,'afterChapterSHA256':hashlib.sha256(p.read_bytes()).hexdigest(),'replacement':(D/(r['id']+'.md')).as_posix(),'classification':'schema testuale con relazioni conservate','originalVisualReview':True,'svgTextRead':True,'semanticReview':'complete','applied':True,'pdfReview':'pending'})
ledgerpath.write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'applied':len(rows),'total':len(ledger),'remaining':133-len(ledger)}))
