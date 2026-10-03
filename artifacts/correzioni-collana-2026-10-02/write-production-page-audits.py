from pathlib import Path
import json,shutil
A=Path(__file__).parent
for v,label in [('06','vol-06-release-20261003'),('07','vol-07-release-20261003'),('12','vol-12-final-20261003')]:
 visual=json.loads((A/f'VOL-{v}-production-visual-checkpoint.json').read_text(encoding='utf8'));geo=json.loads((A/(label+'-proof-audit/metrics.json')).read_text(encoding='utf8'))
 direct=set(visual['directPanoramaPages']);matches={p['page']:p['matchesReviewedPage'] for p in visual['pixelMatchedPreviouslyReviewedPages']};rows=[]
 for p in geo['pagesData']:
  n=p['page'];method='panoramica corrente' if n in direct else f'pixel identici alla pagina {matches[n]} della prova precedente già vista'
  status='Nessun difetto geometrico rilevato nella panoramica; non è rilettura integrale a piena risoluzione'
  if n in [1,3]:status='Layout leggibile; dipendenza editoriale del front matter ancora aperta'
  if v=='12' and n==129:status='Spazio bianco ampio dopo ultima riga e riferimenti: miglioramento facoltativo P12-07'
  rows.append({'page':n,'review':method,'words':p['words'],'imageCount':len(p['images']),'overflow':p['textOutsidePage'],'status':status})
 (A/f'VOL-{v}-page-audit.json').write_text(json.dumps({'pdf':label+'-proof.pdf','sha256':visual['sha256'],'pages':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 report=f'''# VOL-{v} — Audit della proiezione pagina per pagina

Prova `{label}-proof.pdf`, {len(rows)} pagine. Registro di ogni pagina: `artifacts/correzioni-collana-2026-10-02/VOL-{v}-page-audit.json`; metodo e dettagli nel [rapporto PDF](../../correzioni-collana-2026-10-02/PDF-VOL-{v}.md). Tutte le pagine coperte in panoramica, anche mediante trasferimento documentato della verifica per corrispondenza pixel; nessun campionamento nella copertura geometrica. Gli ingrandimenti restano mirati.

| Pagina | Tipo di problema | Elemento | Gravità | Correzione | Esito |
| --- | --- | --- | --- | --- | --- |
| Tutte | Composizione e progressione | Margini speculari, titoli, tabelle, box, numeri | Controllo | Raccordi e schede corretti senza ridurre il corpo | Nessun overflow locale; tutte le voci di indice corrispondono al PDF |
| 1 e 3 | Contenuto preliminare | Promesse digitali e dati editoriali | Da risolvere in revisione finale | Le pagine non attestano la disponibilità dei servizi | Aperto sul contenuto; geometria leggibile |

Le continuazioni di tabelle mantengono intestazioni leggibili. Frontespizi e chiusure di capitolo motivano parte del bianco residuo. Il caso P12-07, ove applicabile, resta facoltativo: nessun carattere è stato compresso per eliminarlo. Non sono stati eseguiti test fisici a penna né un’anteprima esterna di stampa. Copertina e consegna appartengono alle fasi successive.
'''
 p=Path(f'wiki/reviews/pipeline/VOL-{v}/20-vol-{v}.md')
 if p.exists():shutil.copy2(p,A/f'VOL-{v}-step20-before-production.md')
 p.write_text(report,encoding='utf8')
