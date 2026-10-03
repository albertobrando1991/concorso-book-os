from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli');R=Path('wiki/reviews/pipeline/VOL-07');A=Path('artifacts/correzioni-collana-2026-10-02')
for code,m in [('M-SA01','m-sa01-sanita-amministrativa'),('M-SA04','m-sa04-tecnici-sanitari-prevenzione')]:
 p=B/m/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8')
 s=s.replace('V07-39 apparati e grafico di V07-35 ancora pendenti; la copertura dell’applicazione visiva resta parziale fino al loro inserimento.','V07-39 e il grafico di V07-35 sono inseriti: due confronti visivi con quesiti e soluzioni nel capitolo 03, serie QC nel capitolo 02. La copertura testuale e degli apparati è completa nel perimetro descritto; resa nel nuovo PDF da verificare.')
 s=s.replace('Copertura dei delta testuali applicata; audit specialistico step 15 e nuovo freeze ancora necessari.','Copertura dei delta testuali riesaminata; audit specialistico step 15 passed senza blocker o warning il 3 ottobre. Nuovo freeze documentato nel manifest corrente.')
 s=s.replace('Le correzioni sono applicate, ma audit specialistico, nuovo freeze e PDF devono essere chiusi tramite CLI.','Le correzioni sono applicate e il nuovo audit specialistico è passato; il manifest corrente documenta il freeze. PDF e fasi successive conservano il proprio stato CLI.')
 p.write_text(s,encoding='utf8')
 files=sorted((B/m/'chapters').glob('*.md'));entries=[]
 for p in files:
  t=p.read_text(encoding='utf8');assert 'review_required: false' in t
  body=t.split('---',2)[-1];assert not re.search(r'\[\[(sources|topics|entities|planning|raw|reviews)/',body)
  for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',body):assert (p.parent/image).exists(),image
  entries.append({'path':str(p).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03'})
 manifest={'volume':'VOL-07','module':code,'date':'2026-10-03','verification':'manuale, text-freeze non implementato nel CLI','files':entries,'checks':['Capitoli canonici presenti, indice e titolo coerenti.','Delta specialistici riesaminati; step15 passed senza blocker/warning.','Nessun rinvio staff nel corpo, immagini locali presenti.','Casi, calcoli e soluzioni verificati nei report14/15.','Humanizer e micro-revisione svolti sui delta, fonti e date esplicite.'],'limitations':['Nuovo PDF e controllo visivo ancora necessari.','Packaging Git di due fonti INT resta a cura del coordinamento; i file sono presenti e leggibili.','Test hybrid-pilot richiede aggiornamento aspettative ai due DO; i gate sostanziali densità/copertura sono passed.']}
 (A/f'{code}-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
 p=R/f'16-moduli-{m}.md';arc=R/'archive'/('pre-correzioni-'+p.name)
 if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
 p.write_text(f'# {code} — Manifest di congelamento del testo\n\nVerifica manuale del 3 ottobre 2026; `text-freeze` non implementato. Nessuna attestazione di gate automatico né pubblicabilità del PDF.\n\n'+'\n'.join('- '+x for x in manifest['checks'])+'\n\n| File | Stato | Data | SHA256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+e['path']+' | text-freeze | '+e['date']+' | '+e['sha256']+' |' for e in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
print('Manifest 16 SA01/SA04 preparati; chiusura CLI da eseguire.')
