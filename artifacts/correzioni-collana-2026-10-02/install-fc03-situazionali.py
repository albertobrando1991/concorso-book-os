from pathlib import Path
import json,re
A=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters/12-quesiti-situazionali-epne.md')
s=p.read_text(encoding='utf8');a=s.index('### Simulazione guidata');b=s.index('### Come leggere le opzioni in prova',a)
data=json.loads((A/'fc03-situazionali.json').read_text(encoding='utf8'));text='### Simulazione situazionale: otto quesiti\n\nScegli la condotta più efficace. Le soluzioni sono dopo l’intera batteria; le alternative possono essere incomplete senza essere tutte illecite.\n\n';solutions=[]
for i,row in enumerate(data):
 q,right,*rest=row;wrong=rest[:3];comment=rest[3];pos=i%4;opts=wrong[:];opts.insert(pos,right)
 text+=f'### Quesito {i+1}\n\n{q}\n\n'+ '\n'.join(f'{chr(65+j)}. {x}' for j,x in enumerate(opts))+'\n\n'
 solutions.append(f'**Quesito {i+1}. Risposta più efficace: {chr(65+pos)}.** {comment}')
text+='### Soluzioni della simulazione situazionale\n\n'+'\n\n'.join(solutions)+'\n\n';s=s[:a]+text+s[b:];p.write_text(s,encoding='utf8')
print('Otto situazionali sostituiti, chiavi A/B/C/D due volte ciascuna.')
