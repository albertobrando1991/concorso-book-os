from pathlib import Path
import re,json,hashlib
A=Path(__file__).parent;changes=[]
for p in sorted(Path('wiki/books/moduli/m-ir04-cultura-beni-culturali/chapters').glob('*.md')):
 b=p.read_bytes();s=p.read_text(encoding='utf8');title=re.search(r'^title: (.*)$',s,re.M)[1].strip('"');s,n=re.subn(r'^# Capitolo \d+\. .*$',lambda m:'# '+title,s,count=1,flags=re.M);assert n==1,p
 p.write_text(s,encoding='utf8');changes.append({'path':p.as_posix(),'before':hashlib.sha256(b).hexdigest(),'after':hashlib.sha256(p.read_bytes()).hexdigest(),'change':'H1 allineato al titolo canonico: rimossa numerazione locale duplicata nella proiezione di volume, senza eliminare contenuto.'})
(A/'VOL-06-production-heading-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
p=A/'M-IR04-freeze.json';f=json.loads(p.read_text(encoding='utf8'));f['controlledPrintCorrections']={'date':'2026-10-03','files':changes,'description':'Allineamento dei 13 H1 al titolo canonico; testo sostanziale invariato, verifica PDF successiva necessaria.'};p.write_text(json.dumps(f,ensure_ascii=False,indent=2),encoding='utf8')
print(len(changes))
