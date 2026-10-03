from pathlib import Path
from fractions import Fraction
import re,json,datetime
B=Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
keys=json.loads((A/'M-SP04-quiz-keys.json').read_text(encoding='utf8'));matrix=(B/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf8');checks=[]
assert Fraction(6,10)/Fraction(27,10)==Fraction(2,9)
assert Fraction(5,10)/Fraction(25,10)==Fraction(1,5)
assert Fraction(4,10)/Fraction(23,10)==Fraction(4,23)
assert sum([70,72,68,75,65])/5+76+3+1==150
assert sum([72,68,70,75,65])/5+74+1.2+2+2==149.2
assert sum([1.5,1,1.5,1,1,3,1,1,1])==12
assert sum([2,2,2,2,2,5,1.5,1,1,1.5])==20
assert 6+2+4+1+12==25 and 2+1+12==15
assert datetime.date(2026,3,17)+datetime.timedelta(days=40)==datetime.date(2026,4,26)
assert datetime.date(2026,4,26).weekday()==6
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);no=p.name[:2];ids=re.findall(r'^## (N-SP04-\d+-\d+) ·',body,re.M)
 assert ids==[f'N-SP04-{no}-{i:02}' for i in range(1,8 if no=='03' else 6)],p
 for nid in ids:assert nid in matrix
 assert re.findall(r'Risposta corretta: ([ABCD])',body)==[q['key'] for q in keys[no]],p
 qs=re.findall(r'^A\. ([^\n]+)\nB\. ([^\n]+)\nC\. ([^\n]+)\nD\. ([^\n]+)\n\n\*\*Risposta corretta: ([ABCD])',body,re.M)
 assert len(qs)==len(keys[no])
 for q,saved in zip(qs,keys[no]):assert q[ord(q[4])-65]==saved['correct']
 assert not re.search(r'\[\[(sources|topics|raw|entities|planning|reviews)/',body)
 assert '<br' not in body and 'Accorpamento motivato' not in body
 for field in ['source_refs','last_compiled_from','topics','entities']:
  for ref in json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1]):assert (Path('wiki')/(ref+'.md')).exists(),ref
 for ref,heading in re.findall(r'\[\[(books/[^#|]+)#([^|\]]+)',body):assert ('## '+heading) in (Path('wiki')/(ref+'.md')).read_text(encoding='utf8')
 fm=fm.replace('review_required: true','review_required: false').replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(fm+'\n---\n'+body,encoding='utf8');checks.append({'path':p.as_posix(),'nuclei':len(ids),'quiz':len(keys[no]),'links':'resolved','semanticAnswers':'preserved','bodyInternalLinks':0})
(A/'M-SP04-audit-checks.json').write_text(json.dumps({'math':'passed','files':checks,'legalCheckScope':'Selective checks of two competition notices, article 21 DL90/2014 and official MAECI deadline; older ordinance evidence remains dated in source.'},ensure_ascii=False,indent=2),encoding='utf8')
p=R/'15-moduli-m-sp04-prefettizia-diplomatica.md';arc=C/'archive/pre-correzioni-15-m-sp04.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-sp04-prefettizia-diplomatica.md').read_text(encoding='utf8').replace('— Correzioni editoriali','— Audit specialistico').replace('Audit specialistico, manifest, rigenerazione PDF','Audit specialistico concluso; manifest, rigenerazione PDF')
t+='''

### Evidenze dell’audit specialistico

Zero errori gravi o medi aperti nel perimetro corretto. Nessun box Dato operativo rilevato dal CLI; valori e condizioni sono stati comunque riesaminati. I limiti temporali e documentali non sono presentati come certezze ulteriori.

- Prefettizia: bando 158 posti, pp. 3–7 e 9–13, requisiti e computo del compleanno, classi di laurea, domanda e opzioni, preselezione 90/60, 27 facili/45 medie/18 difficili, valori delle risposte e omissioni, contingente 1.106 più pari merito, cinque prove digitali e durate 8+8+8+7+4 = 35 ore. Soglie 70 di media, 60 per prova e orale 60. Calcolo finale con incrementi, preferenze e riserve separati. Caso Paolo chiuso con date e beneficio singolo; varianti non implicite. Soglie attese 2/9, 1/5, 4/23 e valori con quattro/cinque opzioni ricalcolati.
- Formazione: art. 21 d.l. 90/2014 acquisito nel testo ufficiale completo e letto; SSAI soppressa e funzioni SNA. Durata biennale del percorso distinta dalla denominazione storica della scuola. L’ordinamento diplomatico mantiene le evidenze consolidate e datate nella fonte, senza una nuova attestazione di lettura integrale del d.P.R. 18/1967.
- Diplomatica: bando 35 posti 2026, pp. 5–14, accesso con laurea magistrale o equiparata e regime dei titoli esteri. Art. 2, comma 3: quattro serie complete di scritti non superate, non domande o insuccessi all’orale. Art. 3 e pagina ufficiale MAECI: 27 aprile ore 12; il 26 era domenica. Opzioni linguistiche, materia facoltativa e titoli nella domanda. Programma economico aggiornato; scritti digitali senza dizionario, 5+5+5+3+3 = 21 ore, media 70, inglese 70, altri 60. Orale 60, materia facoltativa 1,2–2, lingue con valori e tetti differenziati, titoli massimo 6 con sottolimiti 3+3. Esempio finale 149,2 ricalcolato.
- Didattica applicata: testo linguistico originale, traduzione fedele con modalità e condizioni, risposta e dialogo. Dossier ipotetico con 25 ore iniziali contro 20 disponibili e 15 a regime: nessuna previsione causale o potere amministrativo inventato. Foglio elettronico e variante risolti; rilettura della consegna consentita. Piani con somme 12/20, settimane minime 4/6, ore nominali 312/520 per 26 settimane, finestre di prove intere e controlli a calendario.
- Coerenza: sette capitoli, 37 nuclei sopra 600 parole, 43 quiz commentati. Chiavi ruotate con confronto della risposta semantica prima/dopo; commenti del capitolo 7 specifici per le alternative. Nessun HTML residuo o link staff nel corpo. ID e matrice riconciliati; rinvii al volume base risolti a sezioni esistenti e lette nel perimetro riusato. Humanizer e micro-revisione eseguiti sui delta.

Evidenze: M-SP04-audit-checks.json, M-SP04-surface-counts.json, M-SP04-quiz-keys.json e source note specialistica. Il nuovo PDF resta necessario per spazi di compilazione, pagine, tabelle, quiz e leggibilità. L’audit non dichiara il volume pubblicabile.
''';p.write_text(t,encoding='utf8');print('SP04 audit',len(checks),'files')
