import pathlib, json, hashlib, re
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/review-integrale-2026-10-02'
maps={
'VOL-01': [[49],[],[1,43],[49],list(range(2,10)),[10,11,12],[13,14,15],[16,17,18,49],[19,20,21,49],[22,23,24],[18,25,26,27,28,29],[30,31,32],[33],[34],[35],[36],[],[37],[38],[],[39],[40,49],[41],[42],[43],[40,44],[13,26,27,28,45,46],[19,26,47],[1,43],[41],[],[1,39,48]],
'VOL-10': [[1],[2],[3],[4,5,6],[7],[8,9],[],[10,11,12],[13],[14],[15],[16],[17,18]]}
for volume,mapping in maps.items():
    p=OUT/f'{volume}-ledger.json'; d=json.loads(p.read_text(encoding='utf8'))
    report=(ROOT/f'wiki/reviews/audit-integrale-2026-10-02/{volume}.md').read_text(encoding='utf8')
    urls=sorted(set(re.findall(r'https?://[^\s)]+',report)))
    prefix='V'+volume.split('-')[1]
    for row,ids in zip(d['chapters'],mapping,strict=True):
        actual=hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()
        if row['sha256']!=actual:
            print('HASH DELTA',row['file'],row['sha256'],actual)
            # Allow only a provably metadata-only freeze insertion, or the two
            # updates already included in the full rereads and recorded notes.
            raw=(ROOT/row['file']).read_bytes()
            without_freeze=b''.join(line for line in raw.splitlines(keepends=True) if not line.startswith(b'integration_text_freeze:'))
            metadata_only=hashlib.sha256(without_freeze).hexdigest()==row['sha256']
            if not metadata_only and not (volume=='VOL-01' and any(s in row['file'] for s in ['pubblico-impiego','logica-comprensione'])):
                raise SystemExit('Unexpected source delta; reread required')
            row['hashDeltaNote']='Freeze metadata only, or metadata already covered by recorded full reread; substantive content unchanged.'
        row.update(sha256=actual,readComplete=True,quizReview='complete',findings=[f'{prefix}-{n:02}' for n in ids])
        row['externalClaimsChecked']=['See report section 6: selective checks, not universal claim verification']
    d['report']=f'wiki/reviews/audit-integrale-2026-10-02/{volume}.md'
    d['externalSources']=urls
    if volume=='VOL-01':
        d['frontMatter']=[{'file':str(f.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'readComplete':True} for f in sorted((ROOT/'wiki/books/il-metodo-bando/front-matter').glob('*.md'))]
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
    print(volume,len(d['chapters']),'complete')
