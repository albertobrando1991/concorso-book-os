from pathlib import Path
import json,re,hashlib
mod=Path('wiki/books/moduli/m-fl04-polizia-locale');art=Path('artifacts/correzioni-collana-2026-10-02')
matrix=(mod/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf-8');files=sorted((mod/'chapters').glob('*.md'));assert len(files)==15
missing=[]
for p in files:
 assigned=set(re.findall('N-FL04-'+p.name[:2]+r'-\d+',matrix));existing=set(re.findall(r'N-FL04-\d+-\d+',p.read_text(encoding='utf-8')));missing+=sorted(assigned-existing)
assert not missing,missing
records=[{'file':p.as_posix(),'state':'text-freeze','date':'2026-10-03','sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
(art/'M-FL04-freeze.json').write_text(json.dumps({'module':'M-FL04','cutoff':'2026-10-03','files':records,'pdfChecked':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=mod/'planning/10-text-freeze-manifest.md';backup=art/'M-FL04-freeze-prima-correzioni.md'
if manifest.exists() and not backup.exists():backup.write_bytes(manifest.read_bytes())
lines=['---','id: m-fl04-text-freeze-manifest','type: text_freeze_manifest','title: "Text freeze — M-FL04"','status: frozen','module_code: M-FL04','freeze_date: 2026-10-03','updated_at: 2026-10-03','review_required: false','canonical: true','---','','# Text freeze — M-FL04','','Quindici capitoli presenti; nuclei della matrice e indice coerenti. Rilievi V02-39–51 e parti PL di 17/20/38/53/54 corretti; il V02-20 mantiene il distinto intervento sulla simulazione del volume. Controllati 61 wikilink e 90 quiz, con verifiche editoriali documentate nel report 15. Humanizer e audit specialistico dei passaggi modificati completati. Gate 14 e 15 passati senza blocker o warning. Cut-off 3 ottobre 2026; fonti, ambiti e limiti nel manifest M-FL04-source-review.json. Questa verifica manuale del freeze non simula il gate automatico non implementato. Il PDF successivo resta da produrre e verificare.','','| File | Stato | Data | SHA-256 |','|---|---|---|---|']
for x in records:lines.append(f"| {Path(x['file']).name} | {x['state']} | {x['date']} | `{x['sha256']}` |")
manifest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
sp=art/'VOL-02-changes.json';s=json.loads(sp.read_text(encoding='utf-8'))
for fid in [f'V02-{i:02d}' for i in range(39,52)]+['V02-17','V02-38','V02-53','V02-54']:s['changes'][fid]['status']='Applicato e riesaminato; gate 15 M-FL04 superato'
s['limitations']=['Tutti i quattro moduli corretti e audit15 superati; restano apparati e simulazione del volume.','PDF da rigenerare e verificare; superamento limite KDP del precedente volume richiede distribuzione in tomi, non riduzione dei font.','Nessun commit, push o pubblicazione; conferma finale24 distinta dalle verifiche tecniche.']
sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'chapters':15,'missingNuclei':missing}))
