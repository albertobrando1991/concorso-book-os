from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir01-scuola');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/correzioni-collana-2026-10-02/archive');R.mkdir(exist_ok=True)
refs={1:'D.P.R. 275/1999; CCNL Istruzione e Ricerca; D.M. 205 e 206/2023 e bandi della procedura scelta.',2:'L. 62/2000; D.P.R. 275/1999; ordinamenti del primo e secondo ciclo; documentazione MIM sul sistema di istruzione.',3:'D.Lgs. 297/1994, artt. 5, 7, 8, 10 e 37; D.Lgs. 165/2001, art. 25; D.I. 129/2018.',4:'D.P.R. 275/1999, art. 3; D.P.R. 80/2013; documentazione INVALSI per il Sistema nazionale di valutazione, ciclo 2025–2028.',5:'D.P.R. 445/2000; D.Lgs. 82/2005 e Linee guida AgID sulla gestione documentale; Regolamento (UE) 2016/679; procedure di iscrizione e trasferimento della scuola.',6:'CCNL Scuola 29 novembre 2007, art. 53, per la disciplina compatibile; CCNL Istruzione e Ricerca 18 gennaio 2024, art. 55 e classificazione ATA; CCNL 23 dicembre 2025, artt. 1, 5, 6 e 11.',7:'D.I. 28 agosto 2018, n. 129, in particolare artt. 5, 12–17 e 23; istruzioni annuali MIM per gli eventuali differimenti.',8:'D.I. 129/2018, artt. 30–33; D.Lgs. 36/2023 e correttivi; Regolamento (UE) 2021/241, art. 5; guida MEF al DNSH e istruzioni della misura PNRR.',9:'D.Lgs. 165/2001, art. 25; D.P.R. 275/1999; D.M. 194/2022 e bando della procedura dirigenziale pertinente.',10:'D.Lgs. 81/2008, in particolare artt. 17, 18 e 20; CCNL Istruzione e Ricerca 23 dicembre 2025, artt. 5, 6, 8 e 11; DVR e piano di emergenza dell’istituto.',11:'D.M. 205 e 206/2023, allegati A; D.Lgs. 66/2017, art. 7; L. 104/1992, art. 15; D.L. 170/2026, art. 1; D.I. 182/2020 e 153/2023; L. 170/2010, D.M. 5669/2011 e Linee guida DSA, §§ 3–3.1. Per i modelli: Piaget, Vygotskij, Skinner, Bandura; Wood, Bruner e Ross, The role of tutoring in problem solving (1976).',12:'D.Lgs. 62/2017 e L. 150/2024; O.M. 3 del 9 gennaio 2025 e Allegato A; Commissione europea, JRC, quadro DigCompEdu; D.M. 205 e 206/2023.',13:'D.M. 205 e 206/2023, allegati A e bando della procedura pertinente; O.M. 3/2025; Commissione europea, JRC, DigCompEdu. Lezione e rubrica sono esempi didattici originali.'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');front,body=t.split('\n---\n',1);n=int(p.name[:2]);arc=R/f'M-IR01-{p.name}'
 if not arc.exists():arc.write_text(t,encoding='utf8')
 body=re.split(r'\n## (?:Note di review|Riferimenti consolidati)\b',body)[0].rstrip()
 body=re.sub(r'\[\[(?:sources|topics|entities|raw|planning|reviews)/[^\]]+\]\]','',body)
 def booklink(m):
  target,label=m.group(1),m.group(2)
  if label:return label
  path=Path('wiki')/(target+'.md')
  if path.exists():
   match=re.search(r'^title:\s*[\"\']?(.*?)[\"\']?$',path.read_text(encoding='utf8'),re.M)
   if match:return '«'+match.group(1)+'»'
  return target.rsplit('/',1)[-1].replace('-',' ')
 body=re.sub(r'\[\[(books/[^\]|]+)(?:\|([^\]]+))?\]\]',booklink,body)
 def accent(m):
  w=m.group(1);lo=w.lower();last='é' if lo in ['perche','poiche','ne'] else {'a':'à','e':'è','i':'ì','o':'ò','u':'ù'}[lo[-1]]
  return w[:-1]+(last.upper() if w.isupper() else last)
 body=re.sub(r"\b([A-Za-z]+)'(?=[ ,.;:?!\n])",accent,body)
 body=body.replace('Nel corpus M-IR01','Nei bandi esaminati').replace('Nel corpus iniziale','Nei bandi esaminati').replace('La fonte consolidata sul PNRR presenta','Le istruzioni MEF presentano').replace('La fonte richiama il principio','La disciplina richiama il principio')
 body=body.replace('la source note','il riferimento normativo').replace('La source note','Il riferimento normativo')
 body=re.sub(r' +\n','\n',body);body=re.sub(r' {2,}',' ',body)
 if n==1:
  body=body.replace("La disciplina specifica non viene compressa in questo modulo: è un verticale da affiancare al percorso comune.","I capitoli 11–13 coprono il nucleo pedagogico e progettuale comune e una lezione svolta. Per il programma disciplinare si usa l’allegato A al D.M. 205/2023 o al D.M. 206/2023 pertinente alla classe o al posto, integrato dal bando della procedura: non è promessa in questo modulo un’appendice per ogni disciplina.")
  body=body.replace('Se il bando richiede ICT avanzato, appalti complessi o una disciplina specialistica, il rinvio deve essere scritto nel tuo piano e non riempito con studio casuale.','Per informatica specialistica il percorso di collana è VOL-10; per appalti pubblici VOL-09, modulo M-TR02; per la disciplina docente la destinazione è il programma ministeriale identificato nel paragrafo precedente. Segna nel piano solo le sezioni richieste dal tuo bando.')
 if n==13:body=body.replace('innesto nel verticale disciplinare','programma della classe o del posto e contenuto della lezione')
 body+='\n\n## Riferimenti normativi e professionali\n\n'+refs[n]+'\n'
 front=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',front,flags=re.M)
 p.write_text(front+'\n---\n'+body,encoding='utf8')
 stats.append({'path':str(p).replace('\\','/'),'words':len(re.findall(r"\b[\w’]+\b",body)),'staffLinks':bool(re.search(r'\[\[(sources|topics|entities|raw|planning|reviews)/',body)),'legacyFormat':True})
(A/'M-IR01-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(stats,ensure_ascii=False))
