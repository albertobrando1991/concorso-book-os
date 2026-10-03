from pathlib import Path
import json,hashlib
A=Path(__file__).parent;D=A/'vol01-native';p=A/'M-PA01-freeze.json';d=json.loads(p.read_text(encoding='utf8'));changes=[]
for old in sorted((D/'before').glob('*.md')):
 current=Path('wiki/books/il-metodo-bando/chapters')/old.name
 changes.append({'path':current.as_posix(),'before':hashlib.sha256(old.read_bytes()).hexdigest(),'after':hashlib.sha256(current.read_bytes()).hexdigest()})
d['controlledNativePrintCorrections']={'date':'2026-10-03','changes':changes,'nativeSchemas':133,'protectedImages':19,'ledger':(A/'VOL-01-native-ledger.json').as_posix(),'verification':(A/'VOL-01-native-verifica.json').as_posix(),'description':'133 schemi testuali convertiti in tabelle e sequenze native; relazioni preservate e allineate al testo corrente; titoletti H3. Due raccordi testuali corretti. Asset originali e 19 immagini protette invariati. Verifica PDF in corso, nessuna pubblicabilità finale.'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print(len(changes))
