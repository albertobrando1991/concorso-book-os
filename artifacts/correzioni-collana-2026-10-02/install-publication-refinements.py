from pathlib import Path
import json,hashlib,shutil,datetime
A=Path(__file__).parent;Q=A/'publication-refinement-qa';W=Path('wiki/reviews/correzioni-collana-2026-10-02');C=Path('delivery/copertine-2026-10-03')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text('utf8'))
packages=load(A/'registro-package-verification.json')['volumes'];covers=load(A/'cover-qa/cover-manifest.json')
refinements={n:load(Q/f'VOL-{n}-verification.json') for n in ['01','06','09','10']}
assert all(r['visualReviewed'] for r in refinements.values())
assert all(c['visualReviewed'] for c in covers)
notes={
 '01':'Le 19 figure sono collocate alla dimensione effettiva di almeno 300 ppi, senza interpolazione delle bitmap e senza ridurre il corpo del testo. Le didascalie restano vicine alle figure. Il ricalcolo mantiene 686 pagine e conserva il contenuto del capitolo 4, con tabella non spezzata e rimando 4.7 aggiornato. Verificate tutte le 25 pagine cambiate; altre 661 identiche nel rendering. Indice completo: 437 destinazioni corrette.',
 '06':'Corretto Universita in Università nel catalogo e nelle sette occorrenze generate (pp. 2, 3, 5, 8, 122, 273, 429). Le altre 610 pagine sono identiche nel rendering; nessun cambiamento del contenuto disciplinare.',
 '09':'Il Gantt di p. 240 è stato renderizzato a 1950 × 1410 pixel dall’originale PDF vettoriale, senza interpolazione del vecchio raster. La risoluzione effettiva supera 370 ppi. Le altre 266 pagine sono identiche nel rendering; dati, calcolo e testo conservati.',
 '10':'La fotografia illustrativa di p. 123 è stata collocata leggermente più piccola, raggiungendo almeno 300 ppi effettivi senza modificare o interpolare il bitmap. Le altre 126 pagine sono identiche nel rendering; testo e dati conservati.'}
for v in packages:
 D=Path(v['manifest']).parent;mf=Path(v['manifest']);data=load(mf);n=v['volume'][-2:]
 if n in refinements:
  r=refinements[n];assert sha(Path(r['pdf']))==r['pdfSha256']
  archive=A/'publication-refinement-before';archive.mkdir(exist_ok=True)
  previous=Path(r['source']);assert sha(previous)==r['sourceSha256']
  if not (archive/f'vol-{n}-interior.pdf').exists():shutil.copy2(previous,archive/f'vol-{n}-interior.pdf')
  target=D/f'vol-{n}-interior-kdp.pdf';shutil.copy2(r['pdf'],target)
  data['pdfSha256']=r['pdfSha256'];data['pdf']=target.relative_to(D).as_posix();data['pages']=r['pages'];data['previousInteriorSha256']=r['sourceSha256']
  sub=D/'publication-refinements';sub.mkdir(exist_ok=True)
  for p in [Q/f'VOL-{n}-verification.json',A/f'vol-{n}-publication-refined-20261003-payload.json',A/f'vol-{n}-publication-refined-20261003-proof-metrics.json',A/'export-publication-refinements.mjs',A/'verify-publication-refinements.py']:
   shutil.copy2(p,sub/p.name)
  for p in Q.glob(f'vol-{n}-page-*.png'):shutil.copy2(p,sub/p.name)
  for p in A.glob(f'vol-{n}-publication-refined-20261003-*-placement.json'):shutil.copy2(p,sub/p.name)
  if n=='01':
   for p in [A/'VOL-01-publication-index-verification.json',A/'normalize-base-orphan.py',A/'VOL-01-orphan-normalization.json']:shutil.copy2(p,sub/p.name)
  if n=='09':
   shutil.copy2(A/'VOL-09-publication-gantt-resolution.json',sub/'VOL-09-publication-gantt-resolution.json')
   shutil.copy2(A/'M-TR02-freeze.json',sub/'M-TR02-freeze.json')
   asset=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/assets/correzioni-2026-10/gantt-sportello-digitale.png')
   shutil.copy2(asset,sub/asset.name)
   shutil.copy2(asset,D/'snapshot'/asset)
   shutil.copy2(A/'M-TR02-freeze.json',D/'reports/M-TR02-freeze.json')
  report=W/f'PDF-VOL-{n}.md';old=report.read_text('utf8');backup=A/f'PDF-VOL-{n}-before-publication-refinement.md'
  if not backup.exists():shutil.copy2(report,backup)
  old=old.replace(r['sourceSha256'],r['pdfSha256'])
  marker='\n### Chiusura tecnica aggiuntiva del 3 ottobre 2026\n'
  assert marker not in old,'Avoid applying this installer twice'
  old+=marker+'\n'+notes[n]+f"\n\nCandidato corrente SHA-256 `{r['pdfSha256']}`. Prova e confronto sono in `publication-refinements/` del pacchetto. Le verifiche anteriori restano evidenze storiche; la verifica del delta completa la copertura del nuovo candidato. Il giudizio sui servizi digitali, i dati editoriali e la pubblicabilità complessiva non cambia.\n"
  report.write_text(old,'utf8');shutil.copy2(report,sub/report.name)
  # Refresh known report copies, preserving their relative locations.
  for p in D.rglob(report.name):
   if p!=sub/report.name:shutil.copy2(report,p)
  readme=D/'README.md';text=readme.read_text('utf8').replace(r['sourceSha256'],r['pdfSha256'])
  text+='\n## Candidato aggiornato per la pubblicabilità\n\n'+f"[Interno corrente](vol-{n}-interior-kdp.pdf), {r['pages']} pagine, SHA-256 `{r['pdfSha256']}`. "+notes[n]+'\n\nPer riprodurre la nuova proiezione usare dalla radice della repository `node artifacts/correzioni-collana-2026-10-02/export-publication-refinements.mjs '+n+'`, con Book Studio sulla porta 3021 e il payload congelato. Le copie in `publication-refinements/` sono evidenze; gli import degli helper originali dipendono dal checkout. I precedenti comandi di export non includono necessariamente questo delta.\n'
  readme.write_text(text,'utf8')
 assigned=[]
 for cover in [c for c in covers if c['volume']==v['volume']]:
  if n in refinements:cover['interior']=str(D/f'vol-{n}-interior-kdp.pdf');cover['interiorSha256']=data['pdfSha256']
  dest=D/'covers'/Path(cover['cover']).name;dest.parent.mkdir(exist_ok=True);shutil.copy2(cover['cover'],dest)
  assigned.append({**cover,'path':dest.relative_to(D).as_posix()})
 data['covers']=assigned;data['publicationApproved']=False
 spec=D/'covers/README.md'
 spec.write_text('# Copertine candidate del 3 ottobre 2026\n\nSono inclusi PDF completi di quarta, dorso e prima, associati agli interni tramite hash nel manifest. Carta bianca, nero, formato 6,69 × 9,61 pollici; dorso calcolato sul conteggio pari KDP. Nessun ISBN o autore inventato.\n\nDati editoriali reali, condizioni digitali e verifica nel canale restano da chiudere. Ogni variazione di pagine, carta o formato impone un ricalcolo. Il panorama della collana e le specifiche sono in delivery/copertine-2026-10-03.\n','utf8')
 readme=D/'README.md';text=readme.read_text('utf8');text+='\n## Copertine disponibili\n\n'+ '\n'.join(f"- [Copertina {c['key']}](covers/{Path(c['cover']).name}) — {c['kdpPages']} pagine per il dorso." for c in assigned)+'\n\nQuesta aggiunta supera le precedenti indicazioni di copertina assente. Restano da allineare i dati editoriali effettivi e la versione dopo la chiusura dei preliminari.\n';readme.write_text(text,'utf8')
 data['files']=[dict(path=p.relative_to(D).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file() and p!=mf]
 mf.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf8')
(A/'cover-qa/cover-manifest.json').write_text(json.dumps(covers,ensure_ascii=False,indent=2)+'\n','utf8')
rows='\n'.join(f"| {c['key']} | [PDF]({Path(c['cover']).name}) | {c['pdfPages']} / {c['kdpPages']} | {c['spineInches']:.6f} | {c['widthInches']:.6f} × {c['heightInches']:.2f} |" for c in covers)
(C/'README.md').write_text('# Copertine della collana — 3 ottobre 2026\n\nTredici copertine complete, una per interno. [Panorama completo](copertine-collana-panorama.pdf). Tutte sono state esaminate visivamente; font incorporati, colori di processo CMYK, nessuna protezione, testo nelle aree sicure e zona barcode libera. I file restano candidati fino all’allineamento dei dati editoriali reali e dei preliminari.\n\n| Volume / tomo | Copertina | Pagine PDF / KDP | Dorso (in) | Tavola (in) |\n|---|---|---:|---:|---|\n'+rows+'\n\nFormato 6,69 × 9,61 in, bianco e nero su carta bianca; bleed copertina 0,125 in. Coefficiente dorso 0,002252 in per pagina, arrotondando al pari il conteggio. Fonte: [KDP, copertina cartacea](https://kdp.amazon.com/en_US/help/topic/G201953020) e [specifiche dei manoscritti](https://kdp.amazon.com/en_US/help/topic/G201857950), consultate il 3 ottobre 2026.\n\nNon sono stati inseriti ISBN, nomi di autori o promesse digitali non confermati. Titoli e marchio riprendono gli interni correnti. Il nome autore effettivo va allineato con i metadati del canale; le copertine non attestano i diritti. Qualsiasi modifica a carta, pagine o formato richiede una nuova verifica. Il panorama è un fascicolo di consultazione: per il caricamento va usato il singolo PDF completo corrispondente. Nessun Print Previewer o ordine di prova effettuato.\n','utf8')
print('Quattro interni aggiornati, tredici copertine associate e dodici manifest riallineati.')
