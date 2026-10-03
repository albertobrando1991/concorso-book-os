import json, pathlib, hashlib, sys
sys.stdout.reconfigure(encoding='utf-8')
root = pathlib.Path(__file__).resolve().parents[2]
out = root/'artifacts/review-integrale-2026-10-02'
volume = sys.argv[1]
reader = json.loads((root/f'artifacts/review-collana-2026-10-02/{volume}-reader.json').read_text(encoding='utf8'))
ledger = out/f'{volume}-ledger.json'
if not ledger.exists():
    ledger.write_text(json.dumps({'volume':volume,'chapters':[{'file':'wiki/'+c['file'], 'sha256':hashlib.sha256((root/'wiki'/c['file']).read_bytes()).hexdigest(),'readComplete':False,'quizReview':'pending','externalClaimsChecked':[],'findings':[],'limitations':['Controllo esterno non universale.']} for c in reader]},ensure_ascii=False,indent=2),encoding='utf8')
if len(sys.argv)<3:
    for i,c in enumerate(reader):
        p=root/'wiki'/c['file'];t=p.read_text(encoding='utf8');print(i+1,len(t),len(t.splitlines()),c['title'])
else:
    c=reader[int(sys.argv[2])-1];p=root/'wiki'/c['file'];lines=p.read_text(encoding='utf8').splitlines()
    first=int(sys.argv[3]) if len(sys.argv)>3 else 1
    last=int(sys.argv[4]) if len(sys.argv)>4 else len(lines)
    print(str(p.relative_to(root)),hashlib.sha256(p.read_bytes()).hexdigest(),f'LINES {first}-{min(last,len(lines))}/{len(lines)}')
    print('\n'.join(f'{n}: {lines[n-1]}' for n in range(first,min(last,len(lines))+1)))
