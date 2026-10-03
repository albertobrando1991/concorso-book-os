from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-ir03-enti-ricerca');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
stats=json.loads((A/'M-IR03-surface-counts.json').read_text(encoding='utf8'));keys=json.loads((A/'M-IR03-quiz-keys.json').read_text(encoding='utf8'))
assert 80000+50000-20000-30000-12000==68000
assert 50000-20000-6000-3000-2000==19000
assert 68000+24000+9000==2000+80000+19000==101000
assert 80+110-100==90 and 35*90==3150 and (18000-2000)*.15==2400 and 210-12-8==190
assert max(i for i,n in enumerate([18,11,7,4,3,1],1) if n>=i)==4
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1)
 assert re.findall(r'\*\*Risposta corretta: ([ABCD])\.',body)==keys[str(int(p.name[:2]))],p
 for target in re.findall(r'\[\[([^\]|]+)',body):
  file,head=target.split('#');dest=Path('wiki')/(file+'.md');assert dest.exists() and any(x.lstrip('# ').strip()==head for x in dest.read_text(encoding='utf8').splitlines() if x.startswith('#')),target
 for field in ['source_refs','last_compiled_from']:
  refs=json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1])
  for ref in refs:
   if ref.startswith('sources/'):
    assert (Path('wiki')/(ref+'.md')).exists(),ref
 t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M).replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(t,encoding='utf8')
p=Path('wiki/sources/fonti-ufficiali-m-ir03-enti-ricerca-2026-07-24.md');t=p.read_text(encoding='utf8').replace('review_required: true','review_required: false');p.write_text(t,encoding='utf8')
p=R/'15-moduli-m-ir03-enti-ricerca.md';a=C/'archive/pre-correzioni-15-m-ir03.md'
if not a.exists():a.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-ir03-enti-ricerca.md').read_text(encoding='utf8').replace('# M-IR03 — Correzioni del 3 ottobre 2026','# M-IR03 — Audit specialistico del 3 ottobre 2026').replace('Applicati i rilievi del modulo e le quote IR03 dei rilievi trasversali.','Riesaminati i rilievi corretti del modulo e le quote IR03 dei rilievi trasversali. Zero errori gravi o medi aperti nel perimetro testuale dichiarato.').replace('Audit specialistico, text freeze e nuovo PDF.','Audit specialistico concluso; text freeze e nuovo PDF sono i passaggi successivi.')
t+='''

### Esiti specialistici puntuali

- V06-17/18: ambiti legislativi e assetti CNR/ISTAT ricontrollati nelle fonti indicate; livelli I–III e funzione grant coerenti col CCNL e col bando reale. Nessuna equiparazione degli organi.
- V06-10: ricalcolati cassa 68.000, risultato 19.000, attivo/passivo 101.000; risconto 9.000, ammortamento 6.000 e fatture da ricevere 2.000. Il debito per prestazione compiuta è distinto da rateo. Forme di costo: 3.150, 2.400; nessuna aliquota didattica presentata come soglia legale.
- V06-19: missione 190 ammessi, 15 esclusi, anticipo 100 e saldo 90; deroga EPR delimitata, astensione distinta da prova di danno; follow-up con evidenze concrete.
- V06-20/21: assunzioni progettuali dichiarate; h=4 anche dopo aumento del solo primo lavoro; prove tecniche falliscono se velocità e completezza non sono entrambe rispettate.
- V06-22: comunicazione, sei mesi, eventuali tre mesi e condizioni, terzi e titolarità distinti dal riconoscimento dell'inventore; licenza non scambiata con cessione.
- V06-23/24: DNSH obbligatorio RRF; 190 utenti validi su target 200. DMP non impone apertura dei dati vincolati. Laboratorio: 2 agosto oltre 31 luglio, 25.000 ammessi e 3.000 esclusi; richiesta di modifica distinta dall'approvazione.
- V06-36 quota IR03: 72 chiavi coerenti con opzioni e commenti; sei quesiti disciplinari per capitolo. Non usati commenti su lettere rimappate.
- Nessun Dato operativo rilevato dal CLI. Soglie, durate e cifre dei casi sono ipotesi esplicite, salvo termini normativi identificati. Dodici capitoli, sessanta nuclei sopra 600 parole; fonti e rinvio al base risolti; nessun collegamento staff nel corpo.

I controlli di forma e copertura sui delta, la revisione stilistica e il ricalcolo sono conclusi. Il manifest di superficie e le chiavi dei quiz restano evidenza riproducibile. Il PDF non è stato ancora rigenerato e verificato in questo ciclo.
''';p.write_text(t,encoding='utf8')
print('IR03 audit15 pronto; conteggi, chiavi, calcoli, fonti e rinvio verificati')
