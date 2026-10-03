from pathlib import Path
import fitz,re,json,hashlib
from html.parser import HTMLParser
B=Path('wiki/raw/correzioni-vol11-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol11')
class P(HTMLParser):
 def __init__(self):super().__init__();self.b=[]
 def handle_data(self,d):self.b.append(d)
for f in B.glob('fer-allegato*-v2.html'):
 p=P();p.feed(f.read_text(encoding='utf8'));t=' '.join(' '.join(p.b).split());(O/(f.stem+'.txt')).write_text(t,encoding='utf8');i=t.find('Sezione I');print(f.name,len(t),t[i:i+4200])
d=fitz.open(B/'cam2025-allegato.pdf')
for i,p in enumerate(d):
 t=p.get_text()
 if '2.5.3' in t and i>10:print('CAM PAGE',i+1,t)
print('CAM pages',len(d))
for name,needle in [('tiad.pdf','energia elettrica condivisa'),('red3-gu.pdf','DECRETO LEGISLATIVO 9 gennaio 2026')]:
 d=fitz.open(B/name)
 for i,p in enumerate(d):
  t=p.get_text()
  if needle in t and i>1:print(name,'PAGE',i+1,t[:7500]);break
