from pathlib import Path
import json,re,unicodedata,pymupdf
A=Path(__file__).parent;D=A/'vol01-native';doc=pymupdf.open(A/'vol-01-native-release-20261003-proof.pdf')
def norm(t):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',t)).lower()
pages=[norm(p.get_text()) for p in doc]
rows=[]
for p in sorted(D.glob('F???.md')):
 lines=p.read_text(encoding='utf8').splitlines();title=norm(lines[0]);start=next(i for i,t in enumerate(pages) if title in t)
 structured=next((i for i,l in enumerate(lines) if l.startswith('|') or re.match(r'^(\d+\.|[-*])\s',l)),None)
 anchor=([l for l in lines if l.strip()][2] if structured is None else lines[structured+2] if lines[structured].startswith('|') else lines[structured])
 anchor=re.sub(r'^\d+\.\s*','',anchor);key=norm(anchor)[:70]
 body=next((i for i in range(start,min(start+4,len(pages))) if key in pages[i]),None)
 rows.append({'id':p.stem,'headingPage':start+1,'firstBodyPage':body+1 if body is not None else None,'samePage':body==start,'anchor':anchor})
result={'pdfPages':len(doc),'schemas':len(rows),'samePage':sum(r['samePage'] for r in rows),'rows':rows}
(A/'VOL-01-native-release-chain-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(doc),'schemas':len(rows),'samePage':result['samePage'],'exceptions':[r for r in rows if not r['samePage']]},ensure_ascii=False))
