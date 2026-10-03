from pathlib import Path
import json,hashlib,shutil
W=Path('wiki/reviews/correzioni-collana-2026-10-02');D=Path('delivery/VOL-03/candidate-2026-10-03');p=W/'VOL-03.md';t=p.read_text(encoding='utf8');t=t.replace('testo verificato e congelato; PDF candidato da verificare','testo verificato e congelato; PDF verificato nella copertura dichiarata; dipendenze comuni aperte');t=t.replace('Restano figure, export e controllo visivo del candidato aggiornato, preflight e chiusura della pipeline di volume.','Figure, export e controllo visivo del candidato aggiornato sono conclusi nella copertura del rapporto PDF-VOL-03; restano dipendenze comuni, preflight finale e chiusura della pipeline di volume.');p.write_text(t,encoding='utf8');shutil.copy2(p,D/'reports/VOL-03.md')
m=D/'package-manifest.json';d=json.loads(m.read_text(encoding='utf8'))
for r in d['files']:
 q=D/r['path'];r['sha256']=hashlib.sha256(q.read_bytes()).hexdigest()
 if 'bytes' in r:r['bytes']=q.stat().st_size
m.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Report03 e copia pacchetto allineati; PDF e master immutati.')
