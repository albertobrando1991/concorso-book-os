from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters')
data=json.loads((A/'fc03-verifiche.json').read_text(encoding='utf8'));ledger=[]
for i,p in enumerate(sorted(B.glob('*.md')),1):
 s=p.read_text(encoding='utf8');key=f'{i:02d}';d=data[key];assert len(d['quiz'])==6
 a=s.index('### ▣ Verifica');s=s[:a]+'### ▣ Verifica\n\nRispondi senza consultare le soluzioni. Per ogni risposta indica la regola e applicala ai fatti; tempo indicativo: dodici minuti.\n\n'
 for n,(q,ans) in enumerate(d['quiz'],1):s+=f'**Quiz {n}.** {q}\n\n'
 s+='### Caso ragionato di chiusura\n\n'+d['caso'][0]+'\n\n### Soluzioni commentate\n\n'
 for n,(q,ans) in enumerate(d['quiz'],1):
  s+=f'**{n}. Risposta corretta:** {ans}\n\n';ledger.append({'chapter':key,'question':n,'text':q,'answer':ans,'format':'risposta aperta','review':'controllata sul nucleo e sui fatti'})
 s+='**Soluzione del caso.** '+d['caso'][1]+'\n'
 p.write_text(s,encoding='utf8')
assert len(ledger)==114
(A/'VOL-03-FC03-quiz-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print('114 domande, 19 casi e soluzioni installati.')
