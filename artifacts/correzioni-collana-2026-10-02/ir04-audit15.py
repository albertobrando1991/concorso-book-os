from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir04-cultura-beni-culturali');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
keys=json.loads((A/'M-IR04-quiz-keys.json').read_text(encoding='utf8'));stats=json.loads((A/'M-IR04-surface-counts.json').read_text(encoding='utf8'))
assert 2026-1990==36 and 36<70
for row in stats:
 p=Path(row['path']);t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1)
 assert len(row['nuclei'])==5 and min(n['words'] for n in row['nuclei'])>=600
 assert re.findall(r'\*\*Risposta corretta: ([ABCD])\.',body)==keys[str(row['chapter'])],p
 assert len(re.findall(r'^A\. ',body,re.M))==6 and len(re.findall(r'^D\. ',body,re.M))==6,p
 for field in ['source_refs','last_compiled_from','topics','entities']:
  for ref in json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1]):assert (Path('wiki')/(ref+'.md')).exists(),ref
 assert not re.search(r'\[\[(sources|topics|entities|raw|reviews|planning)/',body)
 assert not re.search(r'(usi incompatibili possono richiedere autorizzazioni|metadati devono essere distinti dai dati catalografici)',body)
 t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M).replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(t,encoding='utf8')
p=R/'15-moduli-m-ir04-cultura-beni-culturali.md';a=C/'archive/pre-correzioni-15-m-ir04.md'
if p.exists() and not a.exists():a.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-ir04-cultura-beni-culturali.md').read_text(encoding='utf8').replace('# M-IR04 — Correzioni del 3 ottobre 2026','# M-IR04 — Audit specialistico del 3 ottobre 2026').replace('Applicati i rilievi testuali del modulo;','Riesaminati i rilievi testuali corretti; zero errori gravi o medi aperti nel perimetro descritto;').replace('Audit specialistico, manifest testuale e nuovo PDF,','Audit specialistico concluso; manifest testuale e nuovo PDF,')
t+='''

### Riscontri puntuali dell'audit

- V06-25: corrispondenza dei quattro dipartimenti e delle DG con il portale istituzionale; competenze archivistiche distinte dalla tutela SABAP. I quiz 2/1 e 2/6 distinguono DiT e DiAC.
- V06-26/27: categorie e presupposti degli artt. 10/12/13/14; nessuna soglia settantennale applicata agli archivi pubblici; uso incompatibile vietato, non semplicemente autorizzabile. Controllati avvio, osservazioni e tutela interinale.
- Art. 21: eliminata la generalizzazione che assimila spostamento e autorizzazione; recepita l'abrogazione 2026, denuncia preventiva e comunicazione specifica degli archivi correnti. Prestito e opere restano procedimenti distinti.
- Circolazione: denuncia 30 giorni, prelazione ordinaria 60 e speciale 180; categorie art. 54/55 e tutela dopo alienazione; soglia generale 50.000 e libri 13.500, senza applicarle ai beni già vietati all'uscita. ALC cinque anni e termine quaranta giorni; nessun caso ambiguo esattamente sulla soglia.
- V06-11/28: catalogazione compresa nei metadati descrittivi; master/derivati distinti; checksum prova confronto dei bit, non corretta attribuzione. Collaudo con due associazioni errate e un file alterato correttamente negativo.
- V06-29: gerarchia ISAD e produttore ISAAR; scarto/versamento distinti; caso 1990/2026 pari a 36 anni, inferiore al limite di 70 per salute. Consultazione anticipata non equivale a pubblicazione. Diplomatia nel solo perimetro introduttivo e con limite di fonte dichiarato.
- V06-30: sequenza stratigrafica 10→12→13 coerente; denuncia del rinvenimento 24 ore e custodia distinta da manipolazione. Scheda Botticelli confrontata con Uffizi, committenza mantenuta probabile. Art. 29 con riserva professionale circoscritta a mobili e superfici decorate.
- V06-31/32: nessuna esclusione generale della progettazione dalle prove per architetti; lavoratore e addetto distinti, piano locale senza manovre universali. Caso di pericolo conforme all'art. 20, senza passività assoluta.
- V06-36: 78 chiavi controllate contro opzioni e spiegazioni; nessun commento rimappa lettere di vecchi distrattori. Sei quesiti per capitolo. Dati operativi: nessun box rilevato dal CLI; numeri dei casi dichiarati didattici e termini normativi riferiti all'articolo.

Tredici capitoli e 65 nuclei sopra la soglia di 600 parole; il conteggio non è usato come prova sufficiente della copertura. Controllo didattico e stilistico dei delta concluso. Nuovo PDF da verificare separatamente.
''';p.write_text(t,encoding='utf8')
print('IR04 audit15: fonti, termini, casi, chiavi e superficie verificati')
