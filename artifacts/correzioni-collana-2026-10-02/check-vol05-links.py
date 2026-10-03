from pathlib import Path
import re,json,unicodedata,hashlib
root=Path.cwd();rows=[]
def norm(t):return re.sub(r'[^a-z0-9]+','',unicodedata.normalize('NFKD',t.lower()).encode('ascii','ignore').decode())
for p in (root/'wiki/books/moduli/m-fc05-authority-indipendenti/chapters').glob('*.md'):
 body=p.read_text(encoding='utf-8').split('---',2)[-1]
 for m in re.finditer(r'\[\[([^\]]+)\]\]',body):
  target=m[1].split('|')[0];ref,_,anchor=target.partition('#');dest=root/'wiki'/(ref if ref.endswith('.md') else ref+'.md')
  if not dest.exists():rows.append({'path':p.name,'target':target,'issue':'missing file'});continue
  if anchor:
   headings=re.findall(r'(?m)^#{1,6}\s+(.+)$',dest.read_text(encoding='utf-8'))
   if norm(anchor) not in [norm(h) for h in headings]:rows.append({'path':p.name,'target':target,'issue':'missing heading'})
(root/'artifacts/correzioni-collana-2026-10-02/VOL-05-FC05-links.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:print(r)
print('Unresolved:',len(rows))
