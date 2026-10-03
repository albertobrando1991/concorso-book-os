from pathlib import Path
import json,sys
p=Path(__file__).parent/'VOL-01-native-pdf-visual-ledger.json';d=json.loads(p.read_text(encoding='utf8'))
for arg in sys.argv[1:]:
 i=int(arg)-1;d[i]['visualReviewed']=True;d[i]['review']='Pagina intera esaminata: leggibilità, margini, tabelle, raccordi e asset. Eccezioni nel report di volume.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print(sum(r['visualReviewed'] for r in d))
