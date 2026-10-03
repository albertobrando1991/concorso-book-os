from pathlib import Path
import json, concurrent.futures, subprocess, hashlib
base=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol04.py').read_text('utf-8')
ns={};exec(base[:base.index('jobs=[(name,urn,n)')],ns)
articles=[74,90,172,190,192,329,'335quinquies',405,406,425,432,533,544,548,550,'554bis','554ter',648,650,655,656,665,666]
jobs=[('cpp','decreto.del.presidente.della.repubblica:1988-09-22;447',a) for a in articles]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(ns['fetch'],jobs))
p=ns['R']/'circolare-modello45bis-20260507.html'
url='https://www.giustizia.it/giustizia/it/mg_1_8_1.page?contentId=SDC1503265'
if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
rows.append(dict(name='circolare45bis',url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
(ns['A']/'manifest-penale-extra.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print('Acquisiti',len(rows),'errori',[(r['name'],r.get('article'),r.get('error')) for r in rows if r.get('error')])
registry_jobs=[('privacy-penale','decreto.legislativo:2018-05-18;51',a) for a in [1,2,3,7,9]]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: more=list(pool.map(ns['fetch'],registry_jobs))
urls={
 'registri-civili-statistiche':'https://www.giustizia.it/giustizia/en/mg_1_14_1.page?contentId=SST243978',
 'registri-penali-circolare2016':'https://www.giustizia.it/giustizia/it/mg_1_8_1.page?contentId=SDC1287690',
 'sistema-sicp':'https://www.giustizia.it/giustizia/it/mg_1_11_1.wp?contentId=SPR31349',
 'registro-modello45-circolare2011':'https://www.giustizia.it/giustizia/it/mg_1_8_1.page?contentId=SDC632441',
}
for name,url in urls.items():
 p=ns['R']/f'{name}.html'
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
 more.append(dict(name=name,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
(ns['A']/'manifest-cancelleria-extra.json').write_text(json.dumps(more,ensure_ascii=False,indent=2),'utf-8')
print('Cancelleria acquisiti',len(more))
spese_jobs=[('spese','decreto.del.presidente.della.repubblica:2002-05-30;115',a) for a in [30,74,84,91,92,93,96,100,104,107,133,134,165,168,199,208,212,'227bis','227ter',248]]
spese_jobs += [('rito-spese','decreto.legislativo:2011-09-01;150',15)]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: more=list(pool.map(ns['fetch'],spese_jobs))
(ns['A']/'manifest-spese-extra.json').write_text(json.dumps(more,ensure_ascii=False,indent=2),'utf-8')
print('Spese acquisiti',len(more),[(r['name'],r.get('article'),r.get('error')) for r in more if r.get('error')])
