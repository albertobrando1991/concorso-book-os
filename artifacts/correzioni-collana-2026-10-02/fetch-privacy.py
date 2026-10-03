from pathlib import Path
import urllib.request, hashlib, json
base=Path('wiki/raw/correzioni-collana-2026-10-02')
urls={
 'anac-whistleblowing-20261003.html':'https://www.anticorruzione.it/en/-/whistleblowing',
 'garante-data-breach-20261003.html':'https://www.garanteprivacy.it/data-breach',
 'garante-diritti-20261003.html':'https://www.garanteprivacy.it/regolamentoue/diritti-degli-interessati',
 'gu-foia-circolare2-2017.html':'https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=17A04795&atto.dataPubblicazioneGazzetta=2017-07-13&atto.tipoProvvedimento=CIRCOLARE',
 'gu-foia-lineeguida-2016.html':'https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=17A00068&atto.dataPubblicazioneGazzetta=2017-01-10&atto.tipoProvvedimento=DELIBERA',
 'garante-salute-10177128.html':'https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/10177128'
}
rows=[]
for name,url in urls.items():
 p=base/name
 if not p.exists():
  try:
   data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20).read()
   p.write_bytes(data)
  except Exception as exc:
   print(name,str(exc)); continue
 rows.append(dict(path=p.as_posix(),url=url,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 print(name,p.stat().st_size)
Path('artifacts/correzioni-collana-2026-10-02/privacy-raw-manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
