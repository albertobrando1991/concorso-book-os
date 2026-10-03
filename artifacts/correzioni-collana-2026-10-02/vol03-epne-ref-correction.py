from pathlib import Path
import json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters/appendice-e-rinvii-ragionati-altri-moduli.md')
old=p.read_text(encoding='utf8');before=hashlib.sha256(p.read_bytes()).hexdigest()
(A/'VOL-03-FC03-appendice-e-before-production.md').write_text(old,encoding='utf8')
changes={
'VOL-06, capitolo 03: Profili':'VOL-06, modulo Enti di ricerca, capitolo «Profili',
'Profili e organizzazione del lavoro negli enti pubblici di ricerca; sezione':'Profili e organizzazione del lavoro negli enti pubblici di ricerca»; sezione',
'VOL-09, capitolo 08: Cybersecurity':'VOL-08, capitolo 08: Cybersecurity',
'VOL-10, capitolo 07: Consip':'VOL-09, capitolo 07: Consip',
'VOL-03, capitolo 01: Mappa':'VOL-03, modulo Agenzie fiscali, capitolo «Mappa',
'Mappa delle Agenzie fiscali e dei profili concorsuali; sezione':'Mappa delle Agenzie fiscali e dei profili concorsuali»; sezione',
'VOL-08, capitolo 01: Le authority':'VOL-05, capitolo 01: Le authority'}
text=old
for a,b in changes.items():assert text.count(a)==1,a;text=text.replace(a,b)
p.write_text(text,encoding='utf8')
evidence={'id':'P03-08','file':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'changes':changes,'evidence':['src/catalog/text-volumes.ts','wiki/books/moduli/architettura-moduli-specialistici.md'],'status':'corrected and checked in source; proof pending'}
(A/'VOL-03-P03-08.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf8')
delta='''

### Delta di produzione P03-08 — 3 ottobre 2026

Corrette le cinque destinazioni nella tabella dell'Appendice E: ICT è VOL-08, appalti VOL-09 e authority VOL-05. Per ricerca e fisco eliminati i numeri locali presentati come numeri del volume: indicati modulo, titolo effettivo e sezione. Il catalogo canonico `src/catalog/text-volumes.ts` e l'architettura del wiki confermano l'associazione; i capitoli e le sezioni esistono. Tutto il restante corpo, quiz e soluzioni è invariato. Evidenza differenziale e hash: `VOL-03-P03-08.json`. Nessuna modifica normativa né nuova promessa di copertura; la verifica tipografica resta separata.

| ID | File | Intervento | Evidenza | Stato |
|---|---|---|---|---|
| P03-08 | FC03 appendice E, Destinazioni disponibili | Cinque rimandi riallineati a codice volume, modulo e titolo | Catalogo canonico, file di destinazione e sezioni | Corretto e verificato nel master |
'''
r=Path('wiki/reviews/pipeline/VOL-03/14-moduli-m-fc03-enti-non-economici.md');r.write_text(r.read_text(encoding='utf8')+delta,encoding='utf8')
(A/'VOL-03-P03-08-report-delta.md').write_text(delta,encoding='utf8')
print(json.dumps(evidence,ensure_ascii=False))
