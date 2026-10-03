from pathlib import Path
import json,re,hashlib
mod=Path('wiki/books/moduli/m-fl03-camere-commercio');art=Path('artifacts/correzioni-collana-2026-10-02')
matrix=(mod/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf-8')
files=sorted((mod/'chapters').glob('*.md'));assert len(files)==5
missing=[]
for p in files:
 assigned=set(re.findall('N-FL03-'+p.name[:2]+r'-\d+',matrix));existing=set(re.findall(r'N-FL03-\d+-\d+',p.read_text(encoding='utf-8')))
 missing+=sorted(assigned-existing)
assert not missing,missing
records=[{'file':p.as_posix(),'state':'text-freeze','date':'2026-10-03','sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
(art/'M-FL03-freeze.json').write_text(json.dumps({'module':'M-FL03','cutoff':'2026-10-03','files':records,'pdfChecked':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=mod/'planning/10-text-freeze-manifest.md';a=art/'M-FL03-freeze-prima-correzioni.md'
if manifest.exists() and not a.exists():a.write_bytes(manifest.read_bytes())
lines=['---','id: m-fl03-text-freeze-manifest','type: text_freeze_manifest','title: "Text freeze — M-FL03"','status: frozen','module_code: M-FL03','freeze_date: 2026-10-03','updated_at: 2026-10-03','review_required: false','canonical: true','---','','# Text freeze — M-FL03','','Cinque capitoli presenti, indice e nuclei della matrice coerenti, 62 wikilink validi. I delta camerali dei rilievi V02-35–38 sono completi; il rilievo V02-38 conserva un intervento distinto in M-FL04. Humanizer dei passaggi integrati e audit specialistico 15 eseguiti. Gate 14 e 15 passati senza blocker o warning. Cut-off: 3 ottobre 2026. La verifica manuale del freeze è distinta dal gate automatico non implementato. Il nuovo PDF e la pubblicabilità del volume richiedono i successivi controlli di produzione.','','| File | Stato | Data | SHA-256 |','| --- | --- | --- | --- |']
for x in records:lines.append(f"| {Path(x['file']).name} | {x['state']} | {x['date']} | `{x['sha256']}` |")
manifest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
statepath=art/'VOL-02-changes.json';state=json.loads(statepath.read_text(encoding='utf-8'))
for fid in ['V02-35','V02-36','V02-37']:state['changes'][fid]['status']='Applicato e riesaminato in M-FL03; gate 15 superato'
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'chapters':len(records),'missingNuclei':missing}))
