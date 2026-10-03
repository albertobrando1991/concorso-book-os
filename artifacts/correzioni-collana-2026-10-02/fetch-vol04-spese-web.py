from pathlib import Path
import subprocess,json,hashlib,re,html
R=Path('wiki/raw/correzioni-vol04-2026-10-03');A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04')
urls={
'corte-cost-3-2010':'https://www.cortecostituzionale.it/scheda-pronuncia/2010/3',
'unep-offerta-circolare2006':'https://www.giustizia.it/giustizia/it/mg_1_8_1.page?contentId=SDC1284731',
'casellario-datore-faq':'https://www.giustizia.it/giustizia/it/mg_3_3_7.page?tab=f',
'casellario-pendenti-scheda':'https://www.giustizia.it/giustizia/it/mg_3_3_3.page?tab=w',
'casellario-pescara-2026':'https://procura-pescara.giustizia.it/it/nuove_procedure.page',
'casellario-datore-padova':'https://procura-padova.giustizia.it/it/cert_art_25bis_dpr_3132002.page',
'patrocinio-decreto2025':'https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=25A03904&atto.dataPubblicazioneGazzetta=2025-07-11&tipoSerie=serie_generale&tipoVigenza=originario',
'patrocinio-circolare20250424':'https://www.giustizia.it/giustizia/page/it/provvedimento_ministeriale_selezionato?contentId=SDC1454004',
'spedigius-ministero':'https://www.giustizia.it/giustizia/page/it/come_fare_per_liquidazioni_spese_giustizia?tab=f',
'spedigius-udine':'https://tribunale-udine.giustizia.it/it/liquidazioni_s_g.page',
'spese-circolari2025':'https://www.giustizia.it/giustizia/page/it/decreti_circolari_direttive_provvedimenti_note?facetNode_1=0_50&facetNode_2=1_1%282025%29&selectedNode=0_50_2',
'corte-cost-106-2016':'https://www.cortecostituzionale.it/scheda-pronuncia/2016/106',
'patrocinio-cagliari':'https://tribunale-cagliari.giustizia.it/it/patrocinio_spese_stato.page',
}
rows=[]
for name,url in urls.items():
 p=R/(name+'.html')
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
 raw=p.read_text('utf-8',errors='replace')
 txt=html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\b.*?</\1>','',raw,flags=re.S)))
 (A/(name+'.txt')).write_text(re.sub(r'\s+',' ',txt),'utf-8')
 rows.append(dict(name=name,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
 if name=='spese-circolari2025':
  for match in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',raw,re.S):
   if '24 aprile 2025' in match.group(2): print('CIRCOLARE',match.group(1),re.sub('<[^>]+>','',match.group(2)))
 print(name,len(raw))
(A/'manifest-spese-web.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
base=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol04.py').read_text('utf-8')
ns={};exec(base[:base.index('jobs=[(name,urn,n)')].replace("'ordinamento-allegato')", "'ordinamento-allegato','cc-allegato','unep-allegato')"),ns)
extra=[ns['fetch'](('casellario','decreto.del.presidente.della.repubblica:2002-11-14;313',a)) for a in [2,6,18,40,42]]
(A/'manifest-casellario-extra.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2),'utf-8')
print('Norme casellario',[(r.get('article'),r.get('error')) for r in extra])
import concurrent.futures
jobs=[('unep-allegato','decreto.del.presidente.della.repubblica:1959-12-15;1229',a) for a in [106,107]]
jobs += [('cpc','regio.decreto:1940-10-28;1443',a) for a in [137,138,147,148,149,'149bis',479,492,513,514,518,543,555,557,608,615,617]]
jobs += [('cc-allegato','regio.decreto:1942-03-16;262',a) for a in [1206,1207,1208,1209,1210]]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(ns['fetch'],jobs))
(A/'manifest-unep-extra.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print('UNEP articoli',len(rows),'errori',[(r['name'],r.get('article'),r.get('error')) for r in rows if r.get('error')])
