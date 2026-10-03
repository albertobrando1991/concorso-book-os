import json,re,hashlib,shutil
from pathlib import Path
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');rows=[];missing=[]
for p in sorted(B.glob('*.md')):
 s=p.read_text('utf8');f=s.split('---',2)[1];refs=re.search(r'^source_refs:\s*(\[.*?\])',f,re.M|re.S);paths=re.findall(r'"([^"]+)"',refs[1]) if refs else []
 for r in paths:
  q=Path('wiki')/r
  if not q.exists():missing.append(str(q))
 rows.append(dict(file=p.as_posix(),sourceRefs=len(paths),brokenGlyphs=s.count(chr(65533)),bodyStaffLinks=bool(re.search(r'\[\[(sources|topics|entities|raw|planning|reviews)/',s.split('---',2)[2]))))
out=dict(chapters=len(rows),rows=rows,missing=missing,scope='Current17sourcechapters; exact source_refs and body staff links')
(A/'VOL-04-preflight-source-check.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
assert len(rows)==17 and not missing and all(r['sourceRefs']>0 and r['brokenGlyphs']==0 and not r['bodyStaffLinks'] for r in rows)
print(json.dumps(dict(chapters=len(rows),missing=missing,badGlyphs=sum(r['brokenGlyphs'] for r in rows),bodyStaffLinks=sum(r['bodyStaffLinks'] for r in rows))))
