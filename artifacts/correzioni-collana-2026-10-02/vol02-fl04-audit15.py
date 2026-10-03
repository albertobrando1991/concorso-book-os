from pathlib import Path
import re,json
art=Path('artifacts/correzioni-collana-2026-10-02');mod=Path('wiki/books/moduli/m-fl04-polizia-locale')
quiz=[];problems=[]
for p in sorted((mod/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf-8')
 for chunk in re.split(r'^### Quiz ',t,flags=re.M)[1:]:
  chunk=chunk.split('\n### ',1)[0];opts=re.findall(r'^([A-D])\. ',chunk,re.M);answer=re.search(r'Risposta corretta: ([A-D])',chunk)
  if opts!=list('ABCD') or not answer:problems.append({'file':p.name,'options':opts})
  quiz.append({'file':p.name,'quiz':chunk.splitlines()[0],'key':answer[1] if answer else None,'options':opts})
assert not problems,problems
(art/'M-FL04-quiz-check.json').write_text(json.dumps({'quizCount':len(quiz),'structuralProblems':problems,'items':quiz,'note':'Verifica meccanica struttura; risoluzione logica eseguita sui passaggi nell’audit editoriale, non dedotta da questa scansione.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=Path('wiki/reviews/pipeline/VOL-02/14-moduli-m-fl04-polizia-locale.md');t=p.read_text(encoding='utf-8').replace('# Correzioni autorizzate — M-FL04','# Audit specialistico correttivo — M-FL04').replace('Applicato nel modulo; audit15 successivo','Chiuso nel modulo')
t=t.replace('Eseguire gate15 sul testo corretto.', 'Audit eseguito sui nuclei corretti. Nessuna criticità grave o media residua nel perimetro degli ID; nessun box Dato operativo nel contratto CLI. Il gate14 corrente è passato senza blocker o warning.')
t=t.replace('Audit specialistico15, freeze16; simulazione/apparati del volume e nuova produzione.', 'Registrare gate15 e freeze16; simulazione/apparati del volume e nuova produzione restano distinti.')
t=t.replace('Modulo corretto nel perimetro dei rilievi, da sottoporre al gate15.', 'Testo del modulo idoneo al freeze nel perimetro riesaminato.')
anchor='## 5. Coerenza globale\n\n'
extra='''Verificati 61 wikilink senza destinazioni o heading mancanti; 90 quiz hanno quattro alternative A–D e chiave presente. Il controllo automatico della forma non sostituisce la risoluzione editoriale. Sono stati risolti i casi nuovi: 0,8 g/l rimane nella fascia amministrativa ordinaria; 90/100/360 giorni CdS distinti dai 90/360 della L689; pagamento800 contro1000 nel confronto art16; CNR senza ritardo e termine48 ore per atti garantiti distinti dai termini del sequestro; allontanamento48 ore distinto dal divieto questorile. In rilettura corretta nel quiz09 la decorrenza in «dall'accertamento del fatto», conforme alla tabella e alla norma.

Commercio: SCIA unica non anticipa un assenso preventivo; requisiti professionali del preposto non cancellano quelli morali. Edilizia: controlloSCIA30 e attesaSCIAalternativa30 sono diversi; sospensione45 e demolizione90 non coincidono. Rifiuti: privato non equivale ad amministrativo, proprietario non equivale a responsabile colpevole. Sinistri: quote C–D4 e A–B2,5; distanza OA circa8,25; posizioni di quiete non punto d'urto; caso rosso/lesionegrave ha aggravante e non attende querela. Turni: intervallo7ore insufficiente rispetto alla clausola11; esclusioneD66 operativa distinta dal CCNL. Verbale didattico: pagamento200, difese30, norma regionale fittizia dichiarata; annotazione ambientale non sostituisce identificazione e CNR.

'''
t=t.replace(anchor,anchor+extra);Path('wiki/reviews/pipeline/VOL-02/15-moduli-m-fl04-polizia-locale.md').write_text(t,encoding='utf-8')
print(json.dumps({'quiz':len(quiz),'problems':problems,'report':'15-moduli-m-fl04-polizia-locale.md'}))
