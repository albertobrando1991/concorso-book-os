from pathlib import Path
import subprocess,json,hashlib,html,re,fitz
R=Path('wiki/raw/correzioni-vol04-2026-10-03'); A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04')
urls={
'dm114-art1.html':'https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.versione=1&art.idGruppo=0&art.flagTipoArticolo=0&art.codiceRedazionale=26G00134&art.idArticolo=1&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.dataPubblicazioneGazzetta=2026-06-30&art.progressivo=0',
'cassazione-rassegna-tematica2025.pdf':'https://www.cortedicassazione.it/resources/cms/documents/Rassegna_tematica_aggiornata_al_30_giugno_2025.pdf',
'pct-specifiche2024.pdf':'https://pst.giustizia.it/PST/resources/cms/documents/m_dg.DOG07.07082024.0004292.ID_SPECIFICHETECNICHE_DM_44_2011_FINALE_31_.pdf',
'pct-rettifica-settembre2024.pdf':'https://pst.giustizia.it/PST/resources/cms/documents/m_dg.DOG07.16092024.0004740.ID_20240912_Modifica_art._27_comma_1_ST_V.pdf',
'pct-rettifica-ottobre2024.pdf':'https://pst.giustizia.it/PST/resources/cms/documents/m_dg.DOG07.30102024.0005785.ID_RettificaSpecificheTecniche_v2_signed.pdf',
'pct-accettazione2024.pdf':'https://pst.giustizia.it/PST/resources/cms/documents/m_dg.DOG07.19092024.0034552.U_20240916_Comunicazione_Dip._su_accetta.pdf',
'pct-reginde.html':'https://pst.giustizia.it/PST/it/paginadettaglio.page?contentId=ACC405',
}
rows=[]
for name,url in urls.items():
 p=R/name
 if not p.exists():subprocess.run(['curl.exe','-sS','-L','--retry','2','--max-time','50',url,'-o',str(p)],check=True)
 if p.suffix=='.pdf':
  doc=fitz.open(p); txt='\n'.join(f'\nPAGINA {n+1}\n'+page.get_text() for n,page in enumerate(doc))
 else:txt=html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\b.*?</\1>','',p.read_text('utf-8',errors='replace'),flags=re.S)))
 (A/(p.stem+'.txt')).write_text(txt,'utf-8')
 rows.append(dict(name=name,url=url,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),readComplete=False))
(A/'manifest-digitale.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
# Extract existing immutable ministerial texts without altering their originals.
for p in Path('wiki/raw/m-fc04-giustizia').glob('dm-*-processo-penale-telematico.html'):
 t=html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\b.*?</\1>','',p.read_text('utf-8',errors='replace'),flags=re.S)))
 (A/(p.stem+'.txt')).write_text(re.sub(r'\s+',' ',t),'utf-8')
print('Acquisite',len(rows),'fonti')
base=Path('artifacts/correzioni-collana-2026-10-02/fetch-vol04.py').read_text('utf-8')
ns={};exec(base[:base.index('jobs=[(name,urn,n)')],ns)
jobs=[('dm217','decreto:2023-12-29;217',3),('dm44','decreto:2011-02-21;44',13),('dm44','decreto:2011-02-21;44','13bis'),('cpp','decreto.del.presidente.della.repubblica:1988-09-22;447','111bis'),('cpp','decreto.del.presidente.della.repubblica:1988-09-22;447','175bis'),('disp-cpc','regio.decreto:1941-12-18;1368','196quater'),('cad','decreto.legislativo:2005-03-07;82','6bis'),('cad','decreto.legislativo:2005-03-07;82','6ter'),('cad','decreto.legislativo:2005-03-07;82','6quater')]
rows=[ns['fetch'](j) for j in jobs]
(A/'manifest-digitale-norme.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print([(r.get('name'),r.get('article'),r.get('characters'),r.get('error')) for r in rows])
