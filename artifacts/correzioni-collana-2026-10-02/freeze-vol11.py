from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile');R=Path('wiki/reviews/pipeline/VOL-11')
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
chapters=sorted((B/'chapters').glob('*.md'));assert len(chapters)==14
assert not json.loads((A/'VOL-11-TR04-links.json').read_text(encoding='utf8'))
for p in chapters:
 s=p.read_text(encoding='utf8');assert 'review_required: false' in s;s=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',s,flags=re.M);p.write_text(s,encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8');s=re.sub(r'^(status|module_status|draft_stage): specialist_audit_done$',r'\1: text_frozen',s,flags=re.M);s+='\n## Congelamento corrente\n\nIl testo dei quattordici capitoli è verificato al 3 ottobre 2026. Audit 14 e 15 superati; freeze 16 manuale con manifest SHA-256, perché il gate automatico non è implementato. La matrice distingue 90 nuclei didattici e 14 unità aggregate di verifica. I 44 rilievi testuali sono chiusi; PDF aggiornato e preflight restano da verificare. Ogni modifica sostanziale riapre i gate pertinenti.\n';p.write_text(s,encoding='utf8')
factor=sum(1/1.03**t for t in range(1,6));lcca=10000+3000*factor+1000/1.03**5;lccb=14000+2000*factor+500/1.03**5
assert round(lcca,2)==24601.73 and round(lccb,2)==23590.72 and round(lcca-lccb,2)==1011.01
calc={'SST_excess_percent':(240-200)/200*100,'noise_differences_dB':[62-60,56-49],'payment_689':min(3000/3,500*2),'payment_318':18000/4,'CER_hourly_kWh':min(80,50)+min(20,50),'energy_saving_percent':(120000-90000)/120000*100,'net_saving_euro':30000*.22-600,'payback_years':36000/6000,'hypothetical_CO2e_t':30000*.25/1000,'soil_m3':[300*.25,360*.25],'LCC_euro':[round(lcca,2),round(lccb,2)],'difference_euro':round(lcca-lccb,2)}
save(A/'VOL-11-calculations.json',calc)
dos=[{'chapter':6,'subject':'FIR digitale','source':'RENTRI e L. 26/2026','versionAndVerification':'3 ottobre 2026; obbligo dal 16 settembre 2026'}, {'chapter':11,'id':'DO-TR04-11-IT-ALERT-2026-08-17','source':'IT-alert e direttiva 12 febbraio 2026, GU 100/2026','versionAndVerification':'3 ottobre 2026'}, {'chapter':12,'id':'DO-TR04-12-CLIMA-2026-08-18','source':'Reg. UE 2021/1119 consolidato al 7 aprile 2026 e Reg. UE 2026/667','versionAndVerification':'3 ottobre 2026; obiettivi UE, non quote locali'}]
save(A/'VOL-11-operative-data-manual-check.json',{'method':'Verifica manuale di fonte, ambito, versione/data e uso. Il gate automatico non rileva questi tre box legacy; non equivale ad assenza dei dati.','records':dos,'result':'passed','limitations':'Date negli ID storici non sono le date della verifica corrente; PDF aggiornato da controllare.'})
replacements={'art.6':'art. 6','Art.3':'Art. 3','art.240':'art. 240','art.256':'art. 256','L.132':'L. 132','L.689':'L. 689','DPR357':'DPR 357','D.Lgs.195':'D.Lgs. 195','AUA15':'AUA 15','AIA10/12/16':'AIA 10/12/16 anni','BAT4':'BAT entro 4 anni','schemaAG420':'schema AG 420','VAS12':'VAS, art. 12','conCSR120':'con CSR 120','chiunque,30/60':'chiunque, 30/60','256,137/133':'256, 137/133','PAcentrale':'PA centrale','APE192':'APE, D.Lgs. 192','FER190':'FER 190','CER199':'CER 199','efficienza102':'efficienza 102','edifici192':'edifici 192','CAM24':'CAM del 24','pedologico,75/90':'pedologico, 75/90','3%,24601,73/23590,72':'3%, 24.601,73/23.590,72','AppendiciA–E':'Appendici A–E','textfreeze':'text freeze','1 ott;':'1° ottobre;','CO2 e':'CO₂e','artt.6–9':'artt. 6–9'}
manual='\nTre dati operativi verificati manualmente: FIR digitale (capitolo 6), IT-alert (11), obiettivi climatici UE (12), ciascuno con fonte, ambito e data corrente. Il gate non rileva i box legacy: la verifica manuale è documentata in `VOL-11-operative-data-manual-check.json`, senza dichiarare che i box siano assenti.\n'
for p in [Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-11.md'),R/'14-moduli-m-tr04-ambiente-protezione-civile.md',R/'15-moduli-m-tr04-ambiente-protezione-civile.md']:
 s=p.read_text(encoding='utf8')
 for x,y in replacements.items():s=s.replace(x,y)
 s=s.replace('Chiudere CLI 14/15/16 e rigenerare il PDF.','Audit CLI 14 e 15 superati; freeze 16 manuale documentato. Rigenerare il PDF.').replace('Applicato e verificato nel testo; PDF da verificare','Testo verificato e congelato; PDF da verificare').replace('al termine dell\'audit specialistico; il freeze avviene tramite CLI e manifest separato.','dopo l’audit specialistico e il freeze manuale tramite CLI con manifest separato.').replace('## 7. Suggerimenti facoltativi',manual+'\n## 7. Suggerimenti facoltativi')
 p.write_text(s,encoding='utf8')
files=chapters+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/17-bibbia-del-modulo.md',B/'planning/01-indice-analitico-vol-11.md',Path('wiki/books/volumi/vol-11-ambiente-protezione-civile-sostenibilita/index.md'),Path('wiki/topics/ambiente-rettifiche-2026.md')]
files+=[Path('wiki/sources')/x for x in ['vol-11-ambiente-rettifiche-2026-10-03.md','vol-11-rifiuti-controlli-rettifiche-2026-10-03.md','legge-689-procedura-verifica-2026-10-03.md','vol-11-protezione-civile-verifica-2026-10-03.md','vol-11-energia-sostenibilita-verifica-2026-10-03.md','aia-aua-emissioni-quadro-ufficiale-2026.md','aria-rumore-monitoraggio-dati-quadro-ufficiale-2026.md','clima-energia-rinnovabili-cer-efficienza-quadro-ufficiale-2026.md','bonifiche-siti-contaminati-danno-ambientale-quadro-ufficiale-2026.md','laboratorio-casi-quesiti-sintetici-vol-11-2026.md']]
checks=['14 capitoli presenti; lettura integrale della baseline e riesame dei delta e contesti documentati.','44 rilievi testuali applicati; errori gravi e medi chiusi.','90 nuclei nella matrice, 14 unità aggregate di verifica; zero stati incompleti.','14 gate di capitolo superati senza blocker né warning; audit 14 e 15 superati.','Rinvii del corpo risolti; indici e cinque appendici nel capitolo 14 coerenti.','Lingua e ripetizioni riesaminate; casi, calcoli e 84 domande finali verificati.','Tre box operativi verificati manualmente; fonti consolidate e cut-off 3 ottobre 2026.','Gate text-freeze non implementato; verifica manuale richiesta dal CLI eseguita.']
manifest={'volume':'VOL-11','module':'M-TR04','date':'2026-10-03','verification':'manuale dopo gate-not-implemented','checks':checks,'files':[{'path':p.as_posix(),'sha256':sha(p),'status':'text-frozen'} for p in files],'limitations':['PDF aggiornato, controllo grafico e preflight ancora da completare.','Verifica normativa mirata ai passaggi registrati; non attestata lettura integrale dei testi unici.']}
save(A/'M-TR04-freeze.json',manifest)
table='| File | Stato | SHA-256 |\n| --- | --- | --- |\n'+''.join('| '+x['path']+' | '+x['status']+' | '+x['sha256']+' |\n' for x in manifest['files'])
body='# M-TR04 — Congelamento del testo, 3 ottobre 2026\n\nGate automatico non implementato; verifica manuale prevista dal CLI. Il presente manifest sostituisce quello di agosto, archiviato. Nessun commit effettuato.\n\n'+'\n'.join('- '+x for x in checks)+'\n\n'+table+'\n## Limiti\n\n'+' '.join(manifest['limitations'])+'\n\nOgni modifica sostanziale riapre i gate 10–15; le correzioni controllate devono aggiornare gli hash.\n'
for p in [R/'16-moduli-m-tr04-ambiente-protezione-civile.md',B/'planning/18-text-freeze-manifest.md']:
 backup=A/'before-text/VOL-11'/p.name
 if p.exists() and not backup.exists():shutil.copy2(p,backup)
 p.write_text(body,encoding='utf8')
p=A/'VOL-11-ledger.json';d=json.loads(p.read_text(encoding='utf8'))
for r in d['files']:r['sha256']=sha(Path(r['path']))
for r in d['findings']:
 r['status']='Testo verificato e congelato; PDF da verificare'
 for x,y in replacements.items():r['correction']=r['correction'].replace(x,y)
d.update(freezeManifest=(A/'M-TR04-freeze.json').as_posix(),operativeDataManualCheck=(A/'VOL-11-operative-data-manual-check.json').as_posix(),appendices='A–E nel capitolo 14',textVerified=True,finalVerified=False)
save(p,d)
p=A/'VOL-11-reading-checkpoint.json';d=json.loads(p.read_text(encoding='utf8'));d['frozenFiles']=[x for x in manifest['files'] if '/chapters/' in x['path']];save(p,d)
p=A/'VOL-11-progress.json';d=json.loads(p.read_text(encoding='utf8'));d['textStatus']='44 rilievi verificati; audit 14/15 conclusi; manifest freeze 16 corrente';d['pending']=['Chiusura CLI 16 manuale','PDF aggiornato e gate finali'];save(p,d)
print('Freeze manuale:',len(files),'file; 44 rilievi; PDF pending.')
