from pathlib import Path
import json,re
A=Path(__file__).parent;D=A/'vol01-native';B=Path('wiki/books/il-metodo-bando/chapters');inv=json.loads((A/'VOL-01-native-inventory.json').read_text(encoding='utf8'));n=0
for r in inv:
 p=D/(r['id']+'.md');s=p.read_text(encoding='utf8');lines=s.splitlines();first=lines[0];assert first.startswith('**') and first.endswith('**'),(r['id'],first)
 updated='### '+first[2:-2]+s[len(first):];chapter=B/r['chapter'];c=chapter.read_text(encoding='utf8');assert c.count(s.strip())==1,r['id'];chapter.write_text(c.replace(s.strip(),updated.strip()),encoding='utf8');p.write_text(updated,encoding='utf8');n+=1
print(n)
