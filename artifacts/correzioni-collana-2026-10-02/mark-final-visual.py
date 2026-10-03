from pathlib import Path
import json,sys
p=Path(__file__).parent/'VOL-01-native-final-pdf-visual-ledger.json';rows=json.loads(p.read_text(encoding='utf8'))
for number in map(int,sys.argv[1:]):
 rows[number-1]['visualReviewed']=True
 rows[number-1]['review']='Pagina intera esaminata: schemi leggibili, raccordi coerenti, tabelle e immagini senza tagli o sovrapposizioni.'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(sum(r['visualReviewed'] for r in rows))
