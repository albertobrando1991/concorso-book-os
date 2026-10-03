from pathlib import Path
import subprocess,json
items=[('dlgs118','decreto.legislativo:2011-06-23;118',[26,29,31,32]),('dlgs101','decreto.legislativo:2020-07-31;101',[146,166]),('dlgs297','decreto.legislativo:1994-04-16;297',[5,7,8,10,37]),('dlgs165','decreto.legislativo:2001-03-30;165',[25]),('di129','decreto:2018-08-28;129',[12,13,15,16,17,30,31,33]),('dpr275','decreto.del.presidente.della.repubblica:1999-03-08;275',[3]),('dlgs81','decreto.legislativo:2008-04-09;81',[18])]
items += [('l240','legge:2010-12-30;240',[2]),('dm270','decreto:2004-10-22;270',[3,5,7,11]),('dpr132','decreto.del.presidente.della.repubblica:2003-02-28;132',[4,6,7]),('dpr212','decreto.del.presidente.della.repubblica:2005-07-08;212',[3,6,8])]
base=Path('artifacts/correzioni-collana-2026-10-02'); records=[]
for key,urn,arts in items:
 for art in arts:
  p=base/f'{key}-art{art}-current.html';url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:{urn}~art{art}!vig='
  if not p.exists(): subprocess.run(['curl.exe','-L','--fail','--silent',url,'-o',str(p)],check=True)
  good='comma-num-akn' in p.read_text(encoding='utf8')
  records.append({'file':str(p),'url':url,'hasArticle':good});print(key,art,good)
(base/'ir-sa-norms-fetch.json').write_text(json.dumps(records,indent=2),encoding='utf8')
