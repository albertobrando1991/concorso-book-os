from pathlib import Path
base=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane/chapters')
replacements={
'08-': {
'l’ente e in grado':'l’ente è in grado','La spesa e ammissibile':'La spesa è ammissibile','La catena minima e:':'La catena minima è:','Il ciclo e:':'Il ciclo è:',
'La domanda da commissario e spesso':'La domanda da commissario è spesso','una fase rilevante e stata':'una fase rilevante è stata','la prima domanda da farsi e:':'la prima domanda da farsi è:',
'il progetto e identificato':'il progetto è identificato','la risorsa e iscritta':'la risorsa è iscritta','il capitolo e coerente':'il capitolo è coerente','di spesa e allineato':'di spesa è allineato',
'la regola e semplice':'la regola è semplice','Il progetto e tracciabile':'Il progetto è tracciabile','probabilmente e incompleta':'probabilmente è incompleta','un Comune e soggetto':'un Comune è soggetto',
'procedurale e documentato':'procedurale è documentato','ReGiS e solo':'ReGiS è solo','cos’e':'cos’è','L’errore tipico e scrivere':'L’errore tipico è scrivere','La frase e povera':'La frase è povera',
'chi e amministrazione':'chi è amministrazione','chi e soggetto':'chi è soggetto','la fattura e pagata':'la fattura è pagata','artt.5,9,20,22 e24':'artt. 5, 9, 20, 22 e 24','art.17.':'art. 17.',
'Decreto-legge77/2021, artt.8–9':'Decreto-legge 77/2021, artt. 8–9','COM(2025)310':'COM(2025) 310','verso il2026':'verso il 2026','PCM–MEF/RGS16aprile2026':'PCM–MEF/RGS 16 aprile 2026'},
'01-': {'usera’':'userà'},
'05-': {'quali documenti prova':'quali documenti provano','a che cosa serva':'a che cosa serve'},
'06-': {'Ambiguitàà':'Ambiguità','Ambiguita':'Ambiguità'},
'11-': {'eseguira':'eseguirà','in se,':'in sé,','in se.':'in sé.','gestione e coerente':'gestione è coerente'}
}
for prefix, changes in replacements.items():
 p=next(base.glob(prefix+'*')); text=p.read_text(encoding='utf-8')
 for old,new in changes.items():
  if old in text: text=text.replace(old,new)
 p.write_text(text,encoding='utf-8')
p=next(base.glob('12-*')); text=p.read_text(encoding='utf-8'); text='\n'.join(line.rstrip() for line in text.splitlines())+'\n';p.write_text(text,encoding='utf-8')
