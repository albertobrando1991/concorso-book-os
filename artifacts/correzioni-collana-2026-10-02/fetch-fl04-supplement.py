from pathlib import Path
import subprocess,re,json,hashlib
base=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl04')
exec(Path('artifacts/correzioni-collana-2026-10-02/fetch-fl04.py').read_text(encoding='utf-8').split("base=Path(")[0])
items=[('disp113-correct','stato:decreto.legislativo:1989-07-28;271', '113'),('disp114-correct','stato:decreto.legislativo:1989-07-28;271','114'),('tulps1-correct','stato:regio.decreto:1931-06-18;773','1'),('d152-232ter-correct','stato:decreto.legislativo:2006-04-03;152','232ter'),('l689-art11','stato:legge:1981-11-24;689','11'),('cds-art15','stato:decreto.legislativo:1992-04-30;285','15'),('cpp357-correct','stato:decreto.del.presidente.della.repubblica:1988-09-22;447','357')]
rows=[]
items += [('l121-art15','stato:legge:1981-04-01;121','15'),('d286-art19','stato:decreto.legislativo:1998-07-25;286','19'),('cpa29','stato:decreto.legislativo:2010-07-02;104','29')]
items += [('d59-art64','stato:decreto.legislativo:2010-03-26;59','64'),('d59-art65','stato:decreto.legislativo:2010-03-26;59','65')]
items += [('d66-art'+str(n),'stato:decreto.legislativo:2003-04-08;66',str(n)) for n in [2,4,7,8,9]]
for name,urn,art in items:
 url='https://www.normattiva.it/uri-res/N2Ls?urn:nir:'+urn+'!vig='
 idx=base/(name+'-index.html');cookie=base/(name+'.cookies');p=base/(name+'.html')
 if not idx.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','90','-c',str(cookie),url,'-o',str(idx)],check=True)
 links=re.findall(r"showArticle\('([^']+)'[^>]*>([^<]+)</a>",idx.read_text(encoding='utf-8'))
 candidates=[u for u,label in links if label.replace('art.','').replace(' ','').replace('-','').strip()==art]
 if not candidates:print(name,'NO LINK');continue
 url='https://www.normattiva.it'+candidates[-1]
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','90','-b',str(cookie),url,'-o',str(p)],check=True)
 e=Extractor();e.feed(p.read_text(encoding='utf-8'));txt='\n\n'.join(e.parts);(base/(name+'.txt')).write_text(txt,encoding='utf-8')
 rows.append(dict(name=name,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),characters=len(txt),readComplete=False));print(name,len(txt),flush=True)
(base/'manifest-supplement.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
url='https://www.cortecostituzionale.it/scheda-pronuncia/2026/10'
p=base/'corte-10-2026.html'
if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','90',url,'-o',str(p)],check=True)
