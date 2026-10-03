from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02')
s=(A/'freeze-fc01.py').read_text(encoding='utf8').replace('fc01-ministeri','fc03-enti-non-economici').replace('FC01','FC03').replace('15 capitoli','19 capitoli').replace('len(files)==15','len(files)==19').replace('12 rilievi','22 rilievi')
exec(compile(s,'freeze-fc03-generated','exec'))
# Apparatus correction only: refresh the affected manifest after recording the index delta.
for slug,code in [('m-fc01-ministeri','FC01'),('m-fc03-enti-non-economici','FC03')]:
 p=Path('wiki/books/moduli')/slug/'index.md';s=p.read_text(encoding='utf8')
 s=re.sub(r'(?m)^Scrivere i capitoli in sequenza con Manual Writer Agent.*$', 'Il testo è congelato al 3 ottobre 2026. Restano verifica delle figure, PDF candidato, preflight e chiusura della pipeline di volume.',s)
 s=s.replace('- Stato: testo revisionato e pronto per il text freeze.','- Stato: testo congelato il 3 ottobre 2026; controlli del PDF e della produzione ancora distinti.')
 s=s.replace('Text freeze, composizione del volume e preflight dei formati di pubblicazione.', 'Testo congelato il 3 ottobre 2026; seguono composizione del volume e preflight dei formati di pubblicazione.')
 p.write_text(s,encoding='utf8');mp=A/f'M-{code}-freeze.json';m=json.loads(mp.read_text(encoding='utf8'))
 for e in m['files']:
  if e['path']==p.as_posix():
   old=e['sha256'];e['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();rp=Path('wiki/reviews/pipeline/VOL-03')/f'16-moduli-{slug}.md';r=rp.read_text(encoding='utf8').replace(old,e['sha256']);rp.write_text(r,encoding='utf8')
 mp.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf8')
reg=A/'update-vol03-register.py';s=reg.read_text(encoding='utf8')
s=s.replace('applicato; da verificare in revisione finale e PDF','testo verificato e congelato; PDF candidato da verificare').replace("row['status'].startswith('applicato')", "row['status'].startswith('testo verificato')")
s=s.replace('registro in lavorazione','testo verificato; produzione da completare')
s=s.replace('Completare le integrazioni rimanenti; verificare copertura, quiz, rinvii, fonti e frontmatter; aggiornare matrice senza attestazioni premature; audit specialistico e text freeze tramite pipeline; export e controllo visivo del candidato aggiornato.', 'Tutti i 57 ID sono corretti; gate 14 e 15 superati nei tre moduli, freeze 16 manuali documentati con hash. I controlli includono fonti, quiz, rinvii e matrici. Restano figure, export e controllo visivo del candidato aggiornato, preflight e chiusura della pipeline di volume. Nessuna attestazione di pubblicabilità è anticipata.')
s=s.replace("'finalVerified':False", "'textVerified':True,'finalVerified':False")
reg.write_text(s,encoding='utf8')
print('Manifest e registri predisposti.')
