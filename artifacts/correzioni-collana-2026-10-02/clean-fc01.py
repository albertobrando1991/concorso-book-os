from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc01-ministeri/chapters');A=Path('artifacts/correzioni-collana-2026-10-02');archive=[]
refs={1:'D.Lgs. 165/2001; D.Lgs. 300/1999; D.P.R. 487/1994; CCNL del comparto applicabile e bando della procedura.',2:'D.P.R. 487/1994; bando, allegati e avvisi dell’amministrazione procedente; portale inPA.',3:'D.Lgs. 165/2001; CCNL Funzioni Centrali 9 maggio 2022 e rinnovi successivi, incluso il definitivo 6 agosto 2026; CCNL autonomo PCM quando applicabile.',4:'Costituzione, artt. 92–95; L. 400/1988; D.Lgs. 300/1999 e D.Lgs. 165/2001.',5:'L. 400/1988; D.Lgs. 303/1999, artt. 7–8; atti organizzativi della PCM e contratto del comparto autonomo.',6:'D.Lgs. 300/1999, artt. 3–6; D.Lgs. 165/2001; regolamento di organizzazione dell’amministrazione interessata.',7:'R.D. 1611/1933; R.D. 1612/1933; L. 103/1979; art. 25 c.p.c.; documentazione istituzionale dell’Avvocatura dello Stato.'}
for p in sorted(B.glob('*.md')):
 s=p.read_text(encoding='utf8');num=int(p.name[:2])
 if num in refs:
  matches=list(re.finditer(r'(?m)^## Riferimenti consolidati\s*$',s));assert len(matches)==1,p
  i=matches[0].start();archive.append({'path':p.as_posix(),'text':s[i:]});s=s[:i]+'## Riferimenti normativi e istituzionali\n\n'+refs[num]+'\n'
 s=s.replace('Le fonti ARAN consolidate distinguono','I contratti ARAN distinguono')
 s=s.replace('fonte primaria consolidata','fonte primaria')
 s=s.replace('[[books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato]]','[[books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato#11. Governo|VOL-01, Costituzione e ordinamento dello Stato, Governo]]')
 s=s.replace('[[books/il-metodo-bando/chapters/pubblico-impiego-e-organizzazione-pa]]','[[books/il-metodo-bando/chapters/pubblico-impiego-e-organizzazione-pa#Dirigenza e distinzione tra politica e amministrazione|VOL-01, Pubblico impiego, Dirigenza e distinzione tra politica e amministrazione]]')
 s=s.replace('[[books/il-metodo-bando/chapters/trasparenza-anticorruzione-privacy]]','[[books/il-metodo-bando/chapters/trasparenza-anticorruzione-privacy#6. Limiti all’accesso e bilanciamento|VOL-01, Trasparenza, anticorruzione e privacy, Limiti all’accesso e bilanciamento]]')
 s=s.replace('| N — Norma e bisogno | Quale dovere e quale interesse sono in gioco? | vincoli della scelta |','| N — Nuclei | Quali doveri e concetti distinguono le alternative? | regole della scelta |')
 s=s.replace('| D — Decisione | Quale azione affronta il problema senza eccedere? | alternativa preferibile |','| D — Diario | Quale errore di valutazione devo correggere? | causa, regola e nuova prova |')
 s=s.replace('82. Ricostruisci fatto, funzione, competenza, termine, regola, azione ed evidenza: la risposta deve rendere controllabili questi passaggi.','82. Ricostruisci fatto, interesse coinvolto, funzione competente, regola, azione, controllo ed evidenza: sono le sette domande della griglia del capitolo 11.')
 fm,body=s.split('---',2)[1:]
 for k,v in [('status','revised_draft'),('draft_stage','revision-in-progress'),('review_required','true'),('updated_at','2026-10-03')]:fm=re.sub(r'^'+k+':.*$',k+': '+v,fm,flags=re.M)
 fm=fm.replace('"text-frozen"','"revision-in-progress"')
 p.write_text('---'+fm+'---'+body,encoding='utf8')
(A/'VOL-03-FC01-staff-tail-archive.json').write_text(json.dumps(archive,ensure_ascii=False,indent=2),encoding='utf8')
print('7 apparati staff archiviati; riferimenti pubblici e rinvii aggiornati; BANDO e criterio 82 allineati.')
