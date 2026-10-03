import subprocess,json
from pathlib import Path
A=Path(__file__).parent;rows=[]
for n in range(1,15):
 p=subprocess.run(['node','node_modules/tsx/dist/cli.mjs','scripts/pipeline/cli.ts','gate','VOL-09','--step','10','--module','M-TR02','--chapter',f'{n:02}','--json'],capture_output=True,encoding='utf8')
 d=json.loads(p.stdout[p.stdout.index('{'):]);rows.append(d)
 print(n,d['ok'],d['result']['blockers'],d['result']['warnings'],flush=True)
(A/'VOL-09-gates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
