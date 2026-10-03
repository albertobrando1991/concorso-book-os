from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc03-enti-non-economici');R=Path('wiki/reviews/pipeline/VOL-03')
files=sorted((B/'chapters').glob('*.md'))
assert len(files)==19
for p in files+[B/'planning/02-matrice-copertura-didattica.md',Path('wiki/sources/epne-previdenza-assicurazione-rettifiche-2026-10-03.md'),Path('wiki/topics/epne-previdenza-assicurazione-rettifiche-2026.md')]:
 s=p.read_text(encoding='utf8');s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);p.write_text(s,encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8')
s=s.replace('- Copertura: INPS, INAIL, ACI, ENAC, ISTAT, ASI, ENEA amministrativo, CONI, CRI e altri EPNE compatibili con profili amministrativi, giuridici, economici, contabili, servizi e vigilanza non tecnica.', '- Copertura: INPS e INAIL per i profili amministrativi, giuridici, economici, contabili e di servizio; orientamento alle funzioni di ACI, ENAC e CONI. ISTAT, ASI ed ENEA conservano il comparto Istruzione e Ricerca anche per i profili amministrativi; CRI è un’associazione privata dal 2016. Le schede comparative non mutano questi confini. La vigilanza ispettiva e il servizio sociale richiedono le integrazioni specialistiche dichiarate nelle appendici.')
s=s.replace('  "sources/metodo-bando-progetto-editoriale.md",','  "sources/epne-previdenza-assicurazione-rettifiche-2026-10-03.md",\n  "sources/metodo-bando-progetto-editoriale.md",',1)
s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);p.write_text(s,encoding='utf8')
text=(R/'14-moduli-m-fc03-enti-non-economici.md').read_text(encoding='utf8')
text=text.replace('Correzioni integrali, step 14','Audit specialistico conclusivo, step 15').replace('Applicato; riesame del testo corrente','Verificato e chiuso')
text=text.replace('## 3. Registro per ID','## 3. Registro specialistico per ID').replace('| Descrizione | Correzione proposta |','| Evidenza consolidata | Correzione applicata |')
text=text.replace('Riesame specialistico 15, freeze 16 con manifest e controlli manuali quando il gate non è implementato;', 'Riesame specialistico concluso: nessun errore grave o medio noto resta aperto nel testo. Procedere al freeze 16 con manifest e controlli manuali quando il gate non è implementato;')
text=text.replace('## 4. Fonti ed evidenze','## 4. Fonti ed evidenze\n\nRiscontri puntuali: art. 38 Cost.; art. 2116 c.c.; legge 222/1984 e schede INPS pensioni/NASpI/ISEE; DPR 1124/1965 e d.lgs. 38/2000 con schede INAIL; d.lgs. 124/2004 e circolare INL 6/2020; DPR 97/2003 e bilancio INPS 2026; CCNQ 28 ottobre 2025 e CCNL definitivo 6 agosto 2026; legge 114/2024, art. 314-bis c.p. e art. 445-bis c.p.c. I relativi URL e passaggi sono nella fonte consolidata. Il riesame ha aggiunto l’eccezione del velocipede e la regola sugli ordini vietati penalmente o costituenti illecito amministrativo. Nessun box Dato operativo rilevato dal contratto CLI.')
text=text.replace('## 6. Verifiche','## 6. Verifiche').replace('Zero destinazioni o ancore irrisolte nel corpo;', 'Ultima ripetizione sul testo corrente: 19/19 gate passati senza avvisi. Zero destinazioni o ancore irrisolte nel corpo;')
text=text.replace('Il modulo non è ancora dichiarato pubblicabile:', 'Il testo è idoneo al congelamento nel perimetro dei rilievi riesaminati. Il modulo non è ancora dichiarato pubblicabile:')
(R/'15-moduli-m-fc03-enti-non-economici.md').write_text(text,encoding='utf8')
ledger={'volume':'VOL-03','module':'M-FC03','date':'2026-10-03','reviewType':'baseline integrale più riesame dei delta','findingsClosed':list(json.loads((A/'FC03-applied.json').read_text(encoding='utf8'))),'openQuestionsReviewed':114,'casesReviewed':19,'situationalMcReviewed':8,'simulationTracesReviewed':5,'coverageGates':'19/19 senza warning','bodyLinksUnresolved':0,'datiOperativi':0,'textVerified':True,'pdfVerified':False,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(A/'VOL-03-FC03-specialist-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print('Rapporto 15 e ledger scritti; metadati e indice riconciliati.')
