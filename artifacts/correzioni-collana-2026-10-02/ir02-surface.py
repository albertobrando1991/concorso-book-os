from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir02-universita-afam');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/correzioni-collana-2026-10-02/archive');R.mkdir(exist_ok=True)
refs={1:'L. 168/1989; L. 240/2010; L. 508/1999; D.M. 270/2004; D.P.R. 132/2003 e 212/2005. Bando e atti della procedura individuano profilo e programma.',2:'L. 168/1989; L. 240/2010, art. 2; statuto e regolamenti dell’ateneo pertinente.',3:'D.M. 270/2004, artt. 3, 5 e 7; D.M. 1154/2021; ANVUR, AVA3, requisiti con note del 13 febbraio 2023, ambito C.',4:'D.Lgs. 68/2012; regolamenti di carriera dell’ateneo; Università di Bologna, informazioni su interruzione, sospensione e decadenza; ER.GO, bando benefici 2026/2027, art. 7, pagina 35.',5:'D.P.R. 445/2000; D.Lgs. 82/2005 e Linee guida AgID sulla gestione documentale; L. 241/1990 e D.Lgs. 33/2013 per le rispettive forme di accesso; Regolamento (UE) 2016/679.',6:'D.Lgs. 18/2012, art. 1; D.I. MUR-MEF 34 del 15 gennaio 2025, principi contabili e schemi universitari; regolamento di amministrazione, finanza e contabilità dell’ateneo.',7:'Regolamento (UE) 2021/695; Commissione europea, Annotated Grant Agreement, versione 2.0 del 1° aprile 2025, artt. 5–6; call e grant agreement del progetto.',8:'Regolamenti (UE) 2021/695 e 2021/241; Commissione europea, Annotated Grant Agreement, artt. 5–6; MUR, Si.Ge.Co. e linee guida della misura; bando PRIN e manuale della specifica edizione; istruzioni MEF sul DNSH.',9:'ICCU, REICAT, introduzione 0.4.3, e documentazione SBNMARC; IFLA, ISBD; BNCF, Nuovo soggettario; carta dei servizi e licenze della biblioteca; policy del repository istituzionale.',10:'Commissione europea, Guidelines on how to use the Erasmus+ Learning Agreement for Studies, KA131; Università di Bologna, pagina Tirocini, consultata il 3 ottobre 2026; regolamenti e accordi dell’istituzione interessata.',11:'L. 508/1999; D.P.R. 132/2003, artt. 4–8; D.P.R. 212/2005, artt. 3, 6 e 8, testo vigente; statuto e regolamenti dell’istituzione.',12:'Fonti dei capitoli 02–11. Le quattro tracce sono esercizi originali: le clausole e i dati forniti delimitano il caso e non costituiscono nuove regole generali.'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');front,body=t.split('\n---\n',1);n=int(p.name[:2]);arc=R/f'M-IR02-{p.name}'
 if not arc.exists():arc.write_text(t,encoding='utf8')
 body=re.split(r'\n## Note di review\b',body)[0].rstrip()
 body=re.sub(r'\[\[(?:sources|topics|entities|raw|planning|reviews)/[^\]]+\]\]','',body)
 replacements={
 'Il quadro nazionale richiamato dalle fonti consolidate comprende':'Il quadro nazionale comprende',
 'se la fonte consolidata non lo sostiene':'senza un fondamento nella disciplina applicabile',
 'Nel corpus consolidato compaiono procedure':'Nei bandi di settore compaiono procedure',
 'un altro bando del corpus':'un altro bando',
 'Il corpus dei bandi rappresentativi':'Il confronto fra bandi',
 'un corpus di bandi':'un insieme di bandi',
 'Il corpus aiuta':'Il confronto aiuta',
 'Il D.M. 1154/2021 e il sistema ANVUR/AVA sono indicati dalle fonti consolidate come riferimenti':'Il D.M. 1154/2021 e il sistema ANVUR/AVA costituiscono riferimenti',
 'versioni operative non consolidate':'versioni operative non verificate',
 'La fonte consolidata consente di affermare il principio, non di inventare la descrizione di una misura concreta.':'La descrizione della misura è stabilita dai suoi atti: non si ricava per analogia da un altro finanziamento.',
 'La fonte consolidata collega il principio':'La disciplina collega il principio',
 'Alcune fonti consolidate nascono per contesti regionali o locali e sono utili per i concetti generali di ReGiS, DNSH, monitoraggio, rendicontazione e controlli. Non autorizzano però a descrivere procedure, uffici o competenze universitarie per analogia.':'Le istruzioni rivolte a regioni o enti locali non attribuiscono per analogia le stesse procedure e competenze agli uffici universitari.'}
 for old,new in replacements.items():body=body.replace(old,new)
 def accent(m):
  w=m[1];lo=w.lower();last='é' if lo in ['perche','poiche','ne'] else {'a':'à','e':'è','i':'ì','o':'ò','u':'ù'}[lo[-1]]
  return w[:-1]+(last.upper() if w.isupper() else last)
 body=re.sub(r"\b((?:[A-Za-z]*)(?:ita|ta)|perche|poiche|piu|gia|puo|cio|cosi|e)'(?=[ ,.;:?!\n])",accent,body,flags=re.I)
 if n not in [9,10]:body+='\n\n## Riferimenti normativi e professionali\n\n'+refs[n]+'\n'
 else:body+='\n\n'+refs[n]+'\n'
 extra=[]
 if n in [7,8,12]:extra.append('sources/grant-management-horizon-pnrr-2026-08-23')
 if n==12:extra+=['sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05']
 for key in ['source_refs','last_compiled_from']:
  for src in extra:
   m=re.search(rf'^{key}: \[(.*)\]$',front,re.M)
   if m and src not in m[1]:front=front[:m.start()]+f'{key}: [{m[1]}, "{src}"]'+front[m.end():]
 front=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',front,flags=re.M).replace('draft_stage: text_frozen','draft_stage: correction-in-progress').replace('review_required: false','review_required: true')
 p.write_text(front+'\n---\n'+body,encoding='utf8')
 chunks=re.split(r'^### (N-IR02-\d+-\d+[^\n]*)\n',body,flags=re.M)
 nuclei=[]
 for i in range(1,len(chunks),2):nuclei.append({'id':chunks[i].split(' · ')[0],'words':len(re.findall(r'\b[\w’]+\b',chunks[i+1].split('\n## ')[0]))})
 stats.append({'path':str(p).replace('\\','/'),'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'staffLinks':bool(re.search(r'\[\[(sources|topics|entities|raw|planning|reviews)/',body))})
(A/'M-IR02-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'chapters':len(stats),'words':sum(x['words'] for x in stats),'shortNuclei':[x for f in stats for x in f['nuclei'] if x['words']<600]},ensure_ascii=False))
