import subprocess,json
from pathlib import Path
A=Path('artifacts/correzioni-collana-2026-10-02');results=[]
for n in range(1,14):
 r=subprocess.run(['node','node_modules/tsx/dist/cli.mjs','scripts/pipeline/cli.ts','gate','VOL-08','--step','10','--module','M-TR01','--chapter',f'{n:02d}','--json'],capture_output=True,encoding='utf8')
 d=json.loads(r.stdout[r.stdout.index('{'):]);results.append(d);print(n,d['ok'],[x['code']+': '+x['message'] for x in d['result']['blockers']],[x['code'] for x in d['result']['warnings']],flush=True)
(A/'VOL-08-TR01-gates.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
