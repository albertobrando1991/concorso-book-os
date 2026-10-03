from pathlib import Path
import json
idx=Path('wiki/index.md');s=idx.read_text(encoding='utf8');refs=[]
for p in sorted(Path('wiki/sources').glob('vol-09-*-2026-10-03.md')):
 ref='sources/'+p.stem;refs.append(ref)
 if '[['+ref+']]' not in s:s+='- [['+ref+']] — Verifica e integrazioni VOL-09, ottobre 2026.\n'
idx.write_text(s,encoding='utf8')
entity=Path('wiki/entities/codice-dei-contratti-pubblici.md');s=entity.read_text(encoding='utf8')
missing=[r for r in refs if '[['+r+']]' not in s]
if missing:s+='\n## Verifiche editoriali del 3 ottobre 2026\n\n'+'\n'.join('- [['+r+']]' for r in missing)+'\n'
entity.write_text(s,encoding='utf8')
with Path('wiki/log.md').open('a',encoding='utf8') as f:f.write('''
## 3 ottobre 2026 — Completamento applicazione rilievi testuali VOL-09

Interventi registrati su tutti i 38 rilievi testuali del volume: fonti normative primarie, chiusura PNRR, tracciabilità/antifrode, DNSH/CAM, dieci simulazioni svolte, piano30/60/90 e kit cartaceo. Acquisiti tre bandi specialistici ufficiali; verificati direttamente commi449/450 e510/512/516 mediante paginazione Normattiva. Eliminata la promessa di appendici autonome inesistenti, con strumenti effettivi e destinazioni nel corpo. Formato2: 14capitoli,73nuclei, tutti sopra600parole e senza warning di densità dopo riequilibrio; il controllo quantitativo non sostituisce quello sostanziale. Matrice, audit15, freeze e nuovi PDF restano da chiudere. VOL01: 49/51testo,19figure corrette; frontespizi e verifica servizi digitali pendenti. Agenti: VOL03/07/08/10 testo verificato e congelato, nuovi PDF pendenti; VOL02/06 in corso; VOL11 preso in carico da review_vol03 dopo10; VOL04/05/12 ancora da correggere. Nessun via libera alla pubblicazione.
''')
metrics=json.loads(Path('artifacts/correzioni-collana-2026-10-02/vol09-density.json').read_text(encoding='utf8'))
print({'indexedSources':len(refs),'nuclei':sum(len(r['metrics']['nuclei']) for r in metrics),'words':sum(r['metrics']['chapterWords'] for r in metrics)})
