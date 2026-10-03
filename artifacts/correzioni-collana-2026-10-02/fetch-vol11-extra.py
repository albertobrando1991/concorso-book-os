from pathlib import Path
import subprocess,json,hashlib,fitz
B=Path('wiki/raw/correzioni-vol11-2026-10-03'); O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol11')
jobs=[('arera-rqti.pdf','https://www.arera.it/fileadmin/allegati/docs/17/917-17rqti.pdf'),('regolamento-sii-cap.pdf','https://atocittametropolitanadimilano.it/wp-content/uploads/Regolamento-SII-Cap-Holding-SpA-2022.pdf'),('camera-ied420.html','https://www.camera.it/leg19/682?atto=420&idLegislatura=19&tipoAtto=Atto'),('dpcm-rumore.pdf','https://www.isprambiente.gov.it/files/temi/dpcm-14-11-97.pdf'),('ambiente-art298bis-danno.html','https://www.normattiva.it/atto/caricaArticolo?art.versione=1&art.idGruppo=50&art.flagTipoArticolo=0&art.codiceRedazionale=006G0171&art.idArticolo=298&art.idSottoArticolo=2&art.idSottoArticolo1=10&art.dataPubblicazioneGazzetta=2006-04-14&art.progressivo=0'),('rentri-esclusioni.html','https://www.rentri.gov.it/news/esclusioni-dall-obbligo-di-iscrizione-al-rentri-0'),('arpav-pm10-2025.html','https://www.arpa.veneto.it/arpavinforma/indicatori-ambientali/indicatori_ambientali/atmosfera/qualita-dellaria/livelli-di-concentrazione-di-polveri-fini-pm10/2025'),('camera-aria435.html','https://www.camera.it/leg19/682?atto=435&idLegislatura=19&tipoAtto=Atto')]
rows=[]
jobs += [('fer-allegatoA.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-25;190~all1!vig='),('fer-allegatoB.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-25;190~all2!vig='),('fer-allegatoC.html','https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-25;190~all3!vig='),('tiad.pdf','https://www.arera.it/fileadmin/allegati/docs/22/727-22TIAD.pdf'),('red3-gu.pdf','https://www.gazzettaufficiale.it/eli/gu/2026/01/20/15/sg/pdf'),('energy-infrazioni-20261001.html','https://energy.ec.europa.eu/news/october-infringements-package-key-decisions-energy-2026-10-01_en'),('dpc-fasi2016.pdf','https://www.protezionecivile.gov.it/static/01ae0861c5853c2c70541d618e231305/Allegato_2_fasi_operative.pdf')]
jobs += [('cam2025-allegato.pdf','https://www.mase.gov.it/portale/documents/d/guest/allegato_1_cam_edilizia_30_10_25-def-pdf')]
jobs += [('cam-circolare2026.pdf','https://assets-eu-01.kc-usercontent.com/e9919b4d-1ae9-0168-4763-5ecd5c8178f0/5a372bd7-1085-4e20-acf4-da7e95040628/2026_04_10_cam_circolare.pdf')]
jobs += [(f'fer-allegato{a}-v2.html',f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-25;190~all{n}~art1!vig=') for a,n in [('A',1),('B',2),('C',3)]]
for name,url in jobs:
 p=B/name
 try:
  if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','80',url,'-o',str(p)],check=True)
  if name.endswith('.pdf'):
   d=fitz.open(p);(O/(name+'.txt')).write_text('\n'.join(f'PAGE {i+1}\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
  rows.append(dict(path=p.as_posix(),url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
 except Exception as e:rows.append(dict(url=url,error=str(e)))
(O/'manifest-extra.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
d=fitz.open('wiki/raw/correzioni-collana-2026-10-02/camera-costituzione-regolamento-2025.pdf')
for i,p in enumerate(d):
 t=p.get_text()
 if ('117.' in t or '118.' in t) and i<70:print('PAGE',i+1,t)
print('Fonti acquisite:',len(rows))
import re
html=(B/'fer-art6.html').read_text(encoding='utf8')
cookie=O/'normattiva-cookie.txt'
subprocess.run(['curl.exe','-sS','-L','--max-time','60','-c',str(cookie),'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-25;190~art6!vig=','-o',str(O/'fer-session.html')],check=True)
for label in ['A','B','C']:
 match=re.search(r"showArticle\('([^']+)'[^>]+>Allegato "+label+r'</a>',html)
 if match:
  url='https://www.normattiva.it'+match[1].replace('\n','').replace('\r','');p=B/f'fer-allegato{label}-session.html'
  if not p.exists():subprocess.run(['curl.exe','-sS','-L','--max-time','60','-b',str(cookie),url,'-o',str(p)],check=True)
  rows.append(dict(path=p.as_posix(),url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
(O/'manifest-extra.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
