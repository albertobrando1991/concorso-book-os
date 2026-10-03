from pathlib import Path
import json,re
A=Path(__file__).parent;D=A/'vol01-native';B=Path('wiki/books/il-metodo-bando/chapters');inv=json.loads((A/'VOL-01-native-inventory.json').read_text(encoding='utf8'));n=0
for r in inv:
 p=D/(r['id']+'.md');rep=p.read_text(encoding='utf8').strip();ch=B/r['chapter'];s=ch.read_text(encoding='utf8');pos=s.index(rep)+len(rep);tail=s[pos:];m=re.match(r'\s*\*Schema (\d+\.\d+)\s*[-–—]\s*(.*?)\*',tail)
 assert m,r['id'];number,description=m.groups();lines=rep.splitlines();assert lines[0].startswith('### ')
 first='### Schema '+number+' — '+lines[0][4:];new=first+'\n\n'+description+'\n'+rep[len(lines[0]):]
 s=s[:pos-len(rep)]+new+tail[m.end():];ch.write_text(s,encoding='utf8');p.write_text(new+'\n',encoding='utf8');n+=1
print(n)
