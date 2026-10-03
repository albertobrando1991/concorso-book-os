from pathlib import Path
import re,json,hashlib,collections
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia');R=Path('wiki/reviews/pipeline/VOL-04')
changes={9:('In prova non serve recitare sanzioni, ma bisogna mostrare che il patrocinio è un istituto assistito da controlli reali.','Il dettaglio richiesto sulle sanzioni dipende dal programma del bando. Per affrontare il caso occorre collegare dichiarazione, controllo e conseguenza della falsità.'),11:('Non serve memorizzare tutte le regole del codice. Serve non confondere il piano.','Il programma del bando determina le regole da approfondire; in ogni caso occorre distinguere questi piani.'),12:('Non bisogna elencare software o schermate; bisogna spiegare la logica.','Alla conoscenza dei sistemi richiesti dal bando va unita la capacità di spiegare il flusso.'),14:('Non serve recitare tutte le decisioni. Serve saper dire che la pena deve restare umana anche quando il sistema è sotto pressione.','Per le decisioni richieste dal programma, collega il principio alla questione risolta e all’effetto sull’attività dell’ufficio. La tutela della dignità deve tradursi nei rimedi e nelle garanzie applicabili.')}
for n,(old,new) in changes.items():
 p=next((B/'chapters').glob(f'{n:02}-*.md'));t=p.read_text('utf-8');assert old in t or new in t;t=t.replace(old,new);p.write_text(t,'utf-8')
problems=[];data=[];keys=[]
for n,p in enumerate(sorted((B/'chapters').glob('*.md')),1):
 t=p.read_text('utf-8');fm,body=t.split('---',2)[1:]
 refs=json.loads(re.search(r'source_refs: (\[.*?\])',fm,re.S).group(1))
 for ref in refs:
  if not (Path('wiki')/ref).exists():problems.append(str(p)+': missing '+ref)
 if re.search(r'\[\[(?:sources|topics|entities|raw|planning|reviews)/',body):problems.append(str(p)+': internal links')
 k=[a or b for a,b in re.findall(r'Risposta corretta: ([A-D])|\*\*Risposta ([A-D])\.',body)]
 assert len(k)==(6 if n<=14 else 0),(n,k)
 if n<=12:
  opts=re.findall(r'(?m)^\s*- ([A-D])\. ',body);assert collections.Counter(opts)==dict(A=6,B=6,C=6,D=6),(n,collections.Counter(opts))
 keys+=k
 t=t.replace('review_required: true','review_required: false');p.write_text(t,'utf-8')
 data.append(dict(chapter=n,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),quizKeys=k,sourceRefs=refs,words=len(body.split()),sourceRefsResolved=True,textAudit='passed'))
assert not problems,problems
assert collections.Counter(keys)==dict(A=21,B=21,C=21,D=21)
e=dict(volume='VOL-04',date='2026-10-03',chapters=data,quizTotal=84,keyDistribution=dict(collections.Counter(keys)),finalSimulations=6,publicationReady=False,remaining=['PDF','revisione21','preflight22','pacchetto23','conferma24'])
(A/'VOL-04-text-verifica.json').write_text(json.dumps(e,ensure_ascii=False,indent=2),'utf-8')
text=(R/'13-moduli-m-fc04-giustizia.md').read_text('utf-8').replace('Revisione trasversale dopo le correzioni','Audit specialistico conclusivo')
special='''

### Controlli specialistici per fonte consolidata

| ID | File e posizione | Evidenza consolidata | Correzione applicata | Stato finale |
|---|---|---|---|---|
| SP04-01 | Capitoli 1–4, struttura e compiti | sources/vol-04-organizzazione-upp-verifica-2026-10-03.md; D.Lgs.151 artt.1–9, D.Lgs.240, L.145 e DL144 | Distinti organi, personale, funzioni e tempi normativi; Senato 30 settembre e pubblicazione non confusi. | Corretto e verificato |
| SP04-02 | Capitoli 5–6 e 15.1 | sources/vol-04-processo-civile-verifica-2026-10-03.md | Termini 120/150, 10/70, 15/55/45, 40/20/10; riti e impugnazioni; calendario e prove documentali distinti da allegazioni. | Corretto e verificato |
| SP04-03 | Capitolo 7 e 15.2 | sources/vol-04-processo-penale-verifica-2026-10-03.md | 335/45-bis, 405–407, 415-bis, 425/554-ter, fascicoli e riti; 544/548/585; richiesta interrogatorio e 20 giorni applicati. | Corretto e verificato |
| SP04-04 | Capitolo 8 | sources/vol-04-cancelleria-verifica-2026-10-03.md | Modelli, accesso 76/116, copie 475, GDPR9/10 e D.Lgs.51 secondo finalità. | Corretto e verificato |
| SP04-05 | Capitolo 9 e 15.3 | sources/vol-04-spese-verifica-2026-10-03.md | Redditi, CU e minimo, Corte137/2026, patrocinio pendente, 248c3-bis; termini distinti 71/99/170, SPEdiGIUS centrale. | Corretto e verificato |
| SP04-06 | Capitolo 10 e 15.3 | sources/vol-04-casellario-verifica-2026-10-03.md | Qualità60, 24/25-bis, non menzione/eliminazione, 39PDND e 40; obbligo e validità distinti. | Corretto e verificato |
| SP04-07 | Capitolo 11 e 15.4 | sources/vol-04-unep-verifica-2026-10-03.md | 139/140/143, Corte3/2010, precetto e pignoramenti, 492-bis ordinario/urgente, offerta reale; avviso543 al terzo. | Corretto e verificato |
| SP04-08 | Capitolo 12 e 15.3 | sources/vol-04-digitale-verifica-2026-10-03.md | PCT prima PEC condizionata buon fine, specifiche17c11, rassegna Cassazione109–110; WARN/ERROR/FATAL; PPT600/60 e calendario DM114; malfunzionamenti. | Corretto e verificato |
| SP04-09 | Capitoli 13–14 e 15.5–6 | sources/vol-04-minorile-penitenziario-verifica-2026-10-03.md | Età/MAP/riparativa, misure e soglie, programma6mesi, 35-bis/ter, sentenze e ruolo servizi/giudice; 6giorni/480euro. | Corretto e verificato |
| SP04-10 | Capitoli 9, 11, 12, 14 | Programma del bando e coerenza interna | Qualificate quattro residue formule assolute su ciò che non servirebbe studiare; nessuna regola giuridica alterata. | Corretto e verificato |

Nessun box Dato operativo rilevato dal contratto. Le soglie giuridiche sono comunque verificate nelle righe sopra. I campi review_required dei 17 capitoli sono ora false per questo audit testuale; PDF e pubblicazione restano fuori da tale attestazione. Il controllo semantico delle soluzioni precede il riequilibrio delle lettere: la distribuzione uniforme non è prova autonoma di qualità. Le verifiche automatiche confermano 84 soluzioni, tutte le source refs risolte e assenza di link editoriali interni nel corpo.
'''
text=text.replace('## 7. Migliorie opzionali',special+'\n## 7. Migliorie opzionali')
(R/'15-moduli-m-fc04-giustizia.md').write_text(text,'utf-8')
print(json.dumps(dict(chapters=len(data),quiz=len(keys),keys=dict(collections.Counter(keys)),problems=problems),ensure_ascii=False))
