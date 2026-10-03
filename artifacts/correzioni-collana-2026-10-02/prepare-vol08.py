from pathlib import Path
import re,shutil,json,hashlib
from html.parser import HTMLParser
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale');D=A/'before-text/VOL-08';D.mkdir(parents=True,exist_ok=True)
for p in list((B/'chapters').glob('*.md'))+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md']:
 out=D/p.name
 if not out.exists():shutil.copy2(p,out)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.href=None;self.label='';self.entries=[]
 def handle_starttag(self,t,a):
  if t=='a':self.href=dict(a).get('href');self.label=''
 def handle_data(self,d):
  if self.href:self.label+=d
 def handle_endtag(self,t):
  if t=='a' and self.href:self.entries.append((self.label.strip(),self.href));self.href=None
p=Links();p.feed((A/'acn-normativa.html').read_text(encoding='utf8'))
for label,url in p.entries:
 if any(x in label for x in ['127434','379907','138','90/2024']):print(label,url)
s=(A/'recall-vol03.ts').read_text(encoding='utf8').replace('VOL-03 ministeri agenzie fiscali enti previdenza INPS INAIL','VOL-08 ICT cyber cloud NIS2 AI open data procurement')
(A/'recall-vol08.ts').write_text(s,encoding='utf8')
