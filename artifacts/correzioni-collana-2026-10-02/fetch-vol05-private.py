from pathlib import Path
import subprocess,json,hashlib,concurrent.futures
header=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol05.py').read_text(encoding='utf8').split('base=Path(')[0];exec(header)
D=Path('wiki/raw/correzioni-vol05-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05')
jobs=[('civile','regio.decreto:1942-03-16;262:2',n) for n in [1218,1325,1418,1425,1427,2325,2380,2392]]+ [('aml','decreto.legislativo:2007-11-21;231',n) for n in [18,31,35,39]]
def run(j):
 slug,urn,n=j;u=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{n}!vig=';p=D/f'{slug}-art{n}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',u,'-o',str(p)],check=True)
 q=Parser();q.feed(p.read_text(encoding='utf8'));txt='\n\n'.join(q.parts);(O/f'{slug}-art{n}.txt').write_text(txt,encoding='utf8');return {'id':slug,'article':n,'url':u,'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(txt),'readComplete':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:rows=list(e.map(run,jobs))
(O/'private-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print([(r['id'],r['article'],r['characters']) for r in rows])
