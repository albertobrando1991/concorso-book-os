from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent
p=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters/14-laboratorio-atti-casi-simulazioni.md')
old=p.read_bytes();text=old.decode('utf8');nl='\r\n' if '\r\n' in text else '\n'
needle='**Controlli svolti, documenti ed esiti:** __________+'+nl+'**Risorse, impegno e riferimenti contabili:** __________'
replacement='**Controlli svolti, documenti ed esiti:** __________'+nl+nl+'**Risorse, impegno e riferimenti contabili:** __________'
assert text.count(needle)==1
freeze=A/'M-TR02-freeze.json';f=json.loads(freeze.read_text(encoding='utf8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
assert all(sha(Path(r['path']).read_bytes())==r['sha256'] for r in f['files'])
shutil.copy2(freeze,A/'M-TR02-freeze-before-final-form.json')
(A/'VOL-09-cap14-before-final-form.md').write_bytes(old)
new=text.replace(needle,replacement).encode('utf8');p.write_bytes(new)
delta={'id':'P09-07','path':str(p),'beforeSha256':sha(old),'afterSha256':sha(new),'before':needle,'after':replacement,'evidence':'PDF release p.266: literal plus and merged fields. Two original labels retained as separate paragraphs; no normative content altered.'}
(A/'VOL-09-final-form-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),encoding='utf8')
for step in ['14','15']:
 r=Path(f'wiki/reviews/pipeline/VOL-09/{step}-moduli-m-tr02-appalti-pnrr-fondi-ue.md')
 with r.open('a',encoding='utf8') as out:out.write('\n\n### Delta di produzione P09-07 — 3 ottobre 2026\n\nSeparati i campi «Controlli svolti, documenti ed esiti» e «Risorse, impegno e riferimenti contabili» nella scheda del capitolo 14; rimosso il segno + residuo che li univa. Confronto esatto prima/dopo in `artifacts/correzioni-collana-2026-10-02/VOL-09-final-form-delta.json`. Nessuna modifica a norme, fonti, quiz o casi. Il controllo del nuovo PDF resta da svolgere.\n')
print(json.dumps(delta,ensure_ascii=False))
