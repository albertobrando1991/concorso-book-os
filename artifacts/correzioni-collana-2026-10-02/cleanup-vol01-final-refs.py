from pathlib import Path
import json,re
base=Path('wiki/books/il-metodo-bando/chapters')
archive=[]
for slug in ['scegliere-moduli-integrativi','appendice-e-schema-universale-risposta-orale','appendice-f-matrice-materie-profili']:
 p=base/(slug+'.md');t=p.read_text(encoding='utf8')
 if '## Riferimenti consolidati' not in t:continue
 body,refs=t.split('## Riferimenti consolidati',1)
 archive.append({'file':p.as_posix(),'removed':refs})
 keep=[l for l in refs.splitlines() if '[[books/il-metodo-bando/chapters/' in l]
 t=body.rstrip()+ ('\n\n## Per continuare\n\n'+'\n'.join(keep) if keep else '')+'\n'
 if slug.startswith('appendice-f'):
  t=t.replace('Se non tagli nulla, non hai ancora scelto. Hai solo aggiunto.','Riduci duplicazioni e approfondimenti estranei al programma. Mantieni una copertura essenziale di tutte le materie richieste dal bando: scegliere le priorità non significa eliminarne alcune.')
  t=t.replace('Quale contenuto taglio per liberare tempo?','Quale duplicazione o approfondimento fuori programma elimino?')
 p.write_text(t,encoding='utf8')
if archive:
 Path('artifacts/correzioni-collana-2026-10-02/vol01-riferimenti-interni-residui-rimossi.json').write_text(json.dumps(archive,ensure_ascii=False,indent=2),encoding='utf8')
print({'cleaned':len(archive)})
