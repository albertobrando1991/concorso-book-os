from pathlib import Path
import json,hashlib
A=Path(__file__).parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
cfg={
'06':{'label':'vol-06-release-20261003','pages':617,'previous':'vol-06-final-20261003','direct':[272,*range(416,429),430],'detailsPrevious':[6,7,20,21,29,30,37,38,55,56,66,67,58,85,107,108,212,227,241,242,430],'details':[]},
'07':{'label':'vol-07-release-20261003','pages':456,'previous':'vol-07-print-20261003','detailsPrevious':[6,7,16,37,91,120,201,203,268,402,421,422],'details':[201,202,204,404,423,424]},
'12':{'label':'vol-12-final-20261003','pages':492,'previous':'vol-12-release-20261003','direct':[*range(1,17),*range(113,493)],'detailsPrevious':[126,127,128,141,175,198,223,225,226,227,295,305,338],'details':[127,128,142,416,449,450,474,475]}}
for v,c in cfg.items():
 label=c['label'];pdf=A/(label+'-proof.pdf');verification=json.loads((A/(label+'-verification.json')).read_text(encoding='utf8'));geo=json.loads((A/(label+'-proof-audit/metrics.json')).read_text(encoding='utf8'));comp=json.loads((A/(label+'-render-comparison.json')).read_text(encoding='utf8'))
 assert verification['sha256']==sha(pdf) and verification['pageCountMatch'] and not verification['indexMismatches'] and not verification['overflowPages'] and not verification['internalLeaks'] and verification['allFontsEmbedded']
 assert not any(p['textOutsidePage'] or p['replacementGlyphs'] for p in geo['pagesData'])
 direct=c.get('direct',[p['page'] for p in comp['pages'] if not p['matchesReviewedPage']]);transferred=[p for p in comp['pages'] if p['matchesReviewedPage'] and p['page'] not in direct]
 assert set(direct)|{p['page'] for p in transferred}==set(range(1,c['pages']+1))
 ledger={'volume':'VOL-'+v,'pdf':str(pdf),'sha256':sha(pdf),'pages':c['pages'],'panoramaCoverageComplete':True,'directPanoramaPages':direct,'pixelMatchedPreviouslyReviewedPages':transferred,'comparisonArtifact':str(A/(label+'-render-comparison.json')),'previousProof':c['previous'],'closeupsSeenCurrentProof':c['details'],'closeupsSeenPreviousProof':c['detailsPrevious'],'method':'Panoramica di tutte le pagine, direttamente o mediante corrispondenza pixel con pagine già viste; dettagli a piena risoluzione nelle pagine elencate. Il confronto esclude soltanto i 40 pt inferiori del piè di pagina; numerazione e indice verificati separatamente sul PDF.','limits':['Non è correzione di bozze a piena risoluzione di ogni pagina.','Verifiche normative selettive documentate negli audit testuali, non nuova certificazione normativa.','Promesse digitali e dati editoriali comuni aperti; nessuna prova fisica o anteprima esterna KDP.']}
 save(A/f'VOL-{v}-production-visual-checkpoint.json',ledger)
 print(v,c['pages'],len(direct),len(transferred))
