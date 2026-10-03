from pathlib import Path
import json, hashlib, shutil
A=Path(__file__).parent
D=Path('delivery/VOL-04/candidate-2026-10-03')
p=Path('wiki/reviews/pipeline/VOL-04/22-vol-04.md')
shutil.copy2(p,D/'reports'/p.name)
readme=D/'README.md'
t=readme.read_text('utf8')
marker='\n## Preflight locale\n'
if marker not in t:
 t+=marker+'\nBuild, typecheck e 52 test mirati superati. Il [rapporto 22](reports/22-vol-04.md) riporta anche i controlli non superati o non eseguiti. Lo step 22 resta aperto; nessuna accettazione manuale del gate.\n'
readme.write_text(t,'utf8')
manifest=D/'package-manifest.json'
data=json.loads(manifest.read_text('utf8'))
data['files']=[dict(path=f.relative_to(D).as_posix(),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(D.rglob('*')) if f.is_file() and f.name!='package-manifest.json']
manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf8')
p=Path('delivery/COLLANA-REVISIONATA-2026-10-03.md')
t=p.read_text('utf8').replace('Per il preflight software vedere il rapporto corrente di Giustizia e le limitazioni della working tree:', 'Build, typecheck e 52 test mirati sono superati. Per il preflight software completo vedere il [rapporto 22 di Giustizia](VOL-04/candidate-2026-10-03/reports/22-vol-04.md) e le limitazioni della working tree:')
p.write_text(t,'utf8')
for name,section in [
 ('wiki/index.md','\n## Consegna revisionata della collana, 3 ottobre 2026\n\n- [Indice dei dodici pacchetti locali](../delivery/COLLANA-REVISIONATA-2026-10-03.md).\n- [[reviews/correzioni-collana-2026-10-02/registro-applicazione-consolidato-2026-10-03]] — 582 rilievi riconciliati, 577 verificati, 4 parziali e 1 facoltativo aperto; nessun via libera globale.\n'),
 ('wiki/log.md','\n## 2026-10-03 — Consegna degli interni revisionati della collana\n\nApplicate e verificate 577 correzioni sui 582 rilievi originari (501 testuali e 76 di produzione); quattro parziali e una miglioria non bloccante restano esplicite. Tredici rilievi aggiuntivi registrati separatamente. Dodici pacchetti locali con PDF e manifest, VOL-02 in due tomi. Copertura panoramica dei candidati e dettagli mirati documentati nei registri visuali. Build finale, typecheck e 52 test mirati superati; diff globale e test source graph con limiti documentati. VOL-04 ha superato 21, ma 22 resta aperto senza accettazione manuale. Dati digitali/editoriali, copertine, verifiche di stampa e conferma 24 non conclusi. Nessuna pubblicazione, commit o push. Indice: delivery/COLLANA-REVISIONATA-2026-10-03.md. I precedenti eventi di avanzamento sono storici e vengono aggiornati da questo riscontro.\n')]:
 p=Path(name)
 with p.open('a',encoding='utf8') as f:f.write(section)
print('Rapporto preflight, manifest04, indice e log aggiornati.')
