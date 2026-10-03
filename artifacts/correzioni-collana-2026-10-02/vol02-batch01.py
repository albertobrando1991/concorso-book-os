from pathlib import Path
import json,re
base=Path('wiki/books/moduli/m-fl01-comuni-unioni/chapters')
for n,source,topic in [(1,'vol-02-verifica-tuel-atti-statuti-2026-10-02','vol-02-statuti-atti-comunali-correzioni-2026-10-02'),(2,'vol-02-verifica-tuel-atti-statuti-2026-10-02','vol-02-statuti-atti-comunali-correzioni-2026-10-02'),(4,'vol-02-verifica-tuel-atti-statuti-2026-10-02','vol-02-statuti-atti-comunali-correzioni-2026-10-02'),(13,'vol-02-edilizia-somma-urgenza-verifica-2026-10-02','vol-02-titoli-edilizi-e-somma-urgenza')]:
 p=next(base.glob(f'{n:02d}-*.md'));s=p.read_text(encoding='utf8')
 s=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-02',s,flags=re.M)
 s=re.sub(r'^review_required:.*$', 'review_required: true',s,flags=re.M)
 for key,refs in [('source_refs',[f'sources/{source}.md']),('last_compiled_from',[f'wiki/sources/{source}.md',f'wiki/topics/{topic}.md'])]:
  for ref in refs:
   s=re.sub(rf'^({key}: \[)(.*)(\])$',lambda m:m[1]+m[2]+(', '+json.dumps(ref) if ref not in m[2] else '')+m[3],s,flags=re.M)
 if n==13:
  replacements={
  'A, C e D saltano l’istruttoria, la competenza e le garanzie del procedimento.':'A attribuisce automaticamente al verbalizzante il potere di demolizione; B considera provato ciò che è soltanto segnalato; D sostituisce la Polizia locale alla valutazione dell’ufficio competente.',
  'fabbisogno, programmazione, progettazione tecnica, copertura, RUP, affidamento':'fabbisogno e nomina del RUP al primo atto di avvio, programmazione, progettazione tecnica, copertura, affidamento',
  'fabbisogno, programmazione, progettazione, copertura, RUP, affidamento':'fabbisogno e nomina del RUP al primo atto di avvio, programmazione, progettazione, copertura, affidamento',
  '22 e 23 (interventi subordinati a SCIA).':'20 (procedimento e silenzio-assenso, come modificato dalla L. 182/2025, art. 40), 22 e 23 (SCIA ordinaria e alternativa).',
  'per ciclo dei lavori pubblici, RUP, affidamento, esecuzione e verifica.':'in particolare artt. 15 e 140, per ciclo dei lavori pubblici, RUP, affidamento, somma urgenza, esecuzione e verifica; TUEL artt. 191, comma 3, e 194 per riconoscimento e copertura della spesa.'}
  for a,b in replacements.items():
   if a not in s:raise ValueError(a)
   s=s.replace(a,b)
 p.write_text(s,encoding='utf8')
statepath=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');state=json.loads(statepath.read_text(encoding='utf8'))
updates={
'V02-03':([1],'Separate presidenza Giunta e Consiglio; art.54 per ufficiale del Governo.','Confronto artt.39/50/54; riesame normativo complessivo ancora aperto.','applicato'),
'V02-04':([2,4],'Eccezione Giunta per regolamento uffici e servizi coordinata fra teoria, tabelle e risposte.','Raccordo TUEL48c3 nella nota fonte; rilettura dei passaggi modificati.','applicato'),
'V02-05':([2],'Procedura statutaria con quorum, due votazioni, pubblicazione, esempio13componenti e verifica; caso tardività/soccorso risolto.','Fonti DAIT e CdS129/2021; esempio9voti contro7 e distinzione requisito/documento.','applicato'),
'V02-06':([4],'Presupposti pareri49, visto183c7, pubblicazione124/esecutività134; caso riflessi indiretti.','Note fonti Camera/DAIT; esempio1200entrate perse e800spese. Computo calendario controverso non automatizzato.','applicato'),
'V02-16':([13],'Riscritti i sei commenti incongruenti; Q3 coordinata con silenzio-assenso.','Risoluzione analitica alternative: C,A,D,C,D,A,A; verifica testo dei distrattori e ruoloRUP.','applicato'),
'V02-17':([13],'Titolo espresso/silenzio-assenso, SCIA22 e alternativa23 distinti; integrazione L182/2025 sui vincoli.','Fonte e topic dedicati; esempio assensi già validi. Resta applicazione FL04/11.','parziale'),
'V02-18':([13],'Caso tetto biforcato fra manutenzione e somma urgenza, verbale, perizia, riconoscimento e copertura.','MEF art140 in vigore20luglio2025 e TUEL191; controllati presupposti,10/20/30giorni e separabilità rifacimento.','applicato')}
for fid,(ns,change,evidence,status) in updates.items():state['changes'][fid]={'files':[str(next(base.glob(f'{n:02d}-*.md'))).replace('\\','/') for n in ns],'change':change,'evidence':evidence,'status':status}
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
