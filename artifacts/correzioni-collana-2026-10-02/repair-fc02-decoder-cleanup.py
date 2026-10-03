from pathlib import Path
import re,json
root=Path.cwd();art=root/'artifacts/correzioni-collana-2026-10-02';base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters';p=next(base.glob('02-*.md'))
namespace={};script=(art/'clean-vol03-fc02.py').read_text(encoding='utf-8');exec(script[:script.index('for p in sorted(base.glob')],namespace)
language=namespace['language'];original=(art/'before-text/VOL-03'/p.name).read_text(encoding='utf-8');current=p.read_text(encoding='utf-8');body=original.split('---',2)[-1]
body=re.sub(r'(?ms)^### Riferimenti consolidati\n.*?(?=^## Dal bando al piano di studio)', '', body)
m=list(re.finditer(r'(?m)^### Riferimenti consolidati',body))[-1];tail=body[m.start():];body=body[:m.start()].rstrip()+'\n\n## Riferimenti essenziali\n\n'+namespace['biblio']['02']+'\n'
chunks=re.split(r'(\[\[[^\]]+\]\]|\]\([^\n)]+\))',body)
for i in range(0,len(chunks),2):chunks[i]=language(chunks[i])
body=''.join(chunks);fm=current.split('---',2)[1];p.write_text('---'+fm+'---'+body,encoding='utf-8')
archive=json.loads((art/'VOL-03-FC02-staff-tail-archive.json').read_text(encoding='utf-8'))
for r in archive:
 if r['file'].endswith(p.name):r['removedStaffTail']=tail;r['note']='Il corpo fra i due blocchi Riferimenti è stato conservato; corretta la rimozione transitoria rilevata dal controllo dei rinvii.'
(art/'VOL-03-FC02-staff-tail-archive.json').write_text(json.dumps(archive,ensure_ascii=False,indent=2),encoding='utf-8')
p=next(base.glob('14-*.md'));s=p.read_text(encoding='utf-8').replace("#Il presupposto d'imposta",'#N-FC02-04-02 · Presupposto, soggetti e obbligazione tributaria');p.write_text(s,encoding='utf-8')
print('Decoder ripristinato:',len(body.splitlines()),'righe del corpo; rimozione limitata ai blocchi staff')
