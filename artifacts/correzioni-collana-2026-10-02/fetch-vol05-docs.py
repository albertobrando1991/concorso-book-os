from pathlib import Path
import subprocess,json,hashlib,concurrent.futures
B=Path('wiki/raw/correzioni-vol05-2026-10-03');A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol05')
jobs=[('statuto-ivass.pdf','https://www.ivass.it/normativa/nazionale/primaria/Statuto_IVASS.pdf'),('statuto-banca.pdf','https://www.bancaditalia.it/chi-siamo/funzioni-governance/disposizioni-generali/statuto.pdf'),('ptpct-banca-2026.pdf','https://www.bancaditalia.it/chi-siamo/responsabile-trasparenza/Piano-triennale-prevenzione-corruzione-2026-2028.pdf'),('arera-air-255-2025.pdf','https://www.arera.it/fileadmin/allegati/docs/25/255-2025-A.pdf'),('arera-chi-siamo.html','https://www.arera.it/chi-siamo'),('anac-personale-art52quater.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2017-04-24;50~art52quater!vig='),('banca-art19bis.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2005-12-28;262~art19bis!vig='),('banca-art19ter.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2005-12-28;262~art19ter!vig=')]
jobs += [('banca-art29ter.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2005-12-28;262~art29ter!vig='),('banca-art29quater.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2005-12-28;262~art29quater!vig=')]
def fetch(job):
 name,url=job;p=B/name
 try:
  if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60',url,'-o',str(p)],check=True)
  return dict(path=p.as_posix(),url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,readComplete=False)
 except Exception as e:return dict(path=p.as_posix(),url=url,error=str(e),readComplete=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,jobs))
(A/'manifest-docs.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print([(r['path'].split('/')[-1],r.get('bytes',r.get('error'))) for r in rows])
