from pathlib import Path
import json
base=Path('artifacts/review-integrale-2026-10-02')
figures=json.loads((base/'figures/manifest.json').read_text(encoding='utf-8'))
mapping={9:['P01-12','V01-01'],20:['P01-04'],38:['P01-05'],44:['P01-06'],45:['P01-07'],51:['P01-11'],55:['P01-06'],65:['P01-08'],80:['P01-10'],87:['P01-10'],90:['V01-34'],93:['P01-10'],101:['P01-10'],107:['P01-10'],118:['P01-10'],124:['P01-09'],139:['P01-06'],146:['P01-12','V01-42'],147:['P01-10']}
for f in figures:
 f['visuallyInspected']=True
 f['inspection']='contact sheet at original resolution, four figures per sheet'
 f['findings']=mapping.get(f['n'],[])
 f['limitations']=['No physical print proof; QR access workflow not tested' if f['n']==1 else 'Print-size readability also depends on final layout']
(base/'figures/visual-review.json').write_text(json.dumps(figures,ensure_ascii=False,indent=2),encoding='utf-8')
reviews=[{'volume':'VOL-01','pages':592,'panoramicCoverage':'all 25 contact sheets','detailPages':[7,21,55,135,300,460,578],'report':'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-01.md'}, {'volume':'VOL-06','pages':530,'panoramicCoverage':'all 23 contact sheets','detailPages':[6,47,88,179,184,199,361,453],'report':'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-06.md'}, {'volume':'VOL-10','pages':100,'panoramicCoverage':'all 5 contact sheets','detailPages':[24,28,42,58,64,98],'report':'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-10.md'}]
(base/'pdf/root-visual-review.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
reviews.append({'volume':'VOL-03','pages':738,'panoramicCoverage':'all 31 contact sheets','detailPages':[6,161,177,435,459],'report':'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-03.md'})
reviews.append({'volume':'VOL-07','pages':394,'panoramicCoverage':'all 17 contact sheets','detailPages':[6,8,86,139,169,232,353,394],'report':'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-07.md'})
(base/'pdf/root-visual-review.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8')
for volume in ['VOL-03','VOL-05']:
 folder=base/('figures-'+volume)
 rows=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
 for f in rows:
  f['visuallyInspected']=True
  f['inspection']='contact sheet at original resolution, four figures per sheet'
  f['report']='wiki/reviews/audit-integrale-2026-10-02/'+('PDF-VOL-03.md' if volume=='VOL-03' else 'FIGURE-VOL-05.md')
  f['limitations']=['No physical print proof; print-size readability depends on final layout']
 (folder/'visual-review.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded actual visual coverage:',len(figures),'assets;',sum(x['pages'] for x in reviews),'PDF pages in panorama')
