from pathlib import Path
import re
B=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters')
p=B/'08-governo-esecuzione.md';t=p.read_text(encoding='utf8')
t=t.replace('N-TR02-08-05','N-TR02-08-06').replace('N-TR02-08-04','N-TR02-08-05')
t=t.replace('### Penali e premi: un calcolo verificabile','## N-TR02-08-04 · Prezzi, pagamenti e chiusura\n\n### Penali e premi: un calcolo verificabile')
t=t.replace('## N-TR02-08-03 · Gestione operativa','## N-TR02-08-03 · Subappalto, modifiche e sospensioni')
p.write_text(t,encoding='utf8')
p=B/'13-project-management-pubblico.md';t=p.read_text(encoding='utf8')
t=t.replace('## N-TR02-13-05 · Simulazione 2 - WBS confusa con organigramma','## N-TR02-13-06 · Laboratorio di verifica del progetto')
t=t.replace('### Soluzione completa: sportello digitale in nove giorni','## N-TR02-13-05 · WBS e calendario: soluzione completa\n\n### Soluzione completa: sportello digitale in nove giorni')
t=t.replace('concentrare il test in una finestra ridotta','organizzare le risorse per eseguire i test nella finestra disponibile, conservando tutte le verifiche obbligatorie')
p.write_text(t,encoding='utf8')
p=B/'14-laboratorio-atti-casi-simulazioni.md';t=p.read_text(encoding='utf8')
t=t.replace('### Kit cartaceo: trovare e riutilizzare gli strumenti','## N-TR02-14-06 · Kit cartaceo per atti, controlli e aggiornamenti\n\n### Kit cartaceo: trovare e riutilizzare gli strumenti')
t=t.replace('Un Comune acquista arredi interni per 90.000 euro netti. Nell’ipotesi non esistono convenzioni obbligatorie o vincoli di aggregazione pertinenti; la categoria è disponibile sul MePA.','Un’università acquista arredi interni per 90.000 euro netti. La verifica documentata non individua convenzioni, accordi quadro o altri strumenti centralizzati obbligatori disponibili e idonei; la categoria è presente sul MePA. L’università è esclusa dallo specifico regime merceologico dei soggetti aggregatori dell’articolo 9, comma 3, del DL 66/2014, ma resta soggetta agli altri obblighi d’acquisto applicabili.')
t=t.replace('Per il Comune l’acquisto di beni e servizi da 5.000 euro e sotto la soglia UE','Per l’università, nell’ambito delle altre amministrazioni pubbliche del comma 450, l’acquisto di beni e servizi da 5.000 euro e sotto la soglia UE')
p.write_text(t,encoding='utf8')
# Typographic spacing only in visible prose; preserve identifiers, URLs and image paths.
for p in B.glob('*.md'):
 t=p.read_text(encoding='utf8');head,body=t.split('---',2)[1:];lines=[]
 for line in body.splitlines():
  if not (line.startswith('## N-') or '![' in line or 'http' in line or '`' in line or re.search(r'N-TR02-\d\d-\d\d',line)):
   line=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)|(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',line)
   line=re.sub(r'\bcap\.?\s+(\d+)',r'capitolo \1',line,flags=re.I)
   line=re.sub(r'(?<=[,;])(?=[A-Za-zÀ-ÿ0-9])',' ',line)
  lines.append(line)
 p.write_text('---'+head+'---'+'\n'.join(lines)+'\n',encoding='utf8')
s=Path('wiki/sources/vol-09-laboratorio-soluzioni-verificate-2026-10-03.md');t=s.read_text(encoding='utf8').replace('2. Arredi 90.000, nessuna convenzione obbligatoria/merceologia aggregata applicabile nell\'ipotesi, strumenti di mercato elettronico disponibili.','2. Università, arredi 90.000; verifica documentata dell’assenza di convenzioni/AQ/altri strumenti centralizzati obbligatori disponibili e idonei, mercato elettronico disponibile. Esclusione università dallo specifico regime art.9c3 DL66/2014 (arredi ora categoria DPCM2026), non dagli altri obblighi.');s.write_text(t,encoding='utf8')
s=Path('wiki/sources/vol-09-consip-strumenti-obblighi-2026-10-03.md');t=s.read_text(encoding='utf8')
t+='''
## Completamento acquisizione diretta — 3 ottobre 2026

Letti integralmente su Normattiva i commi 449 e 450 della legge 296/2006 e 510, 512 e 516 della legge 208/2015. Raw validi: `l296-obblighi-block-20261003.html`, `l208-obblighi-block-20261003.html`, nel folder raw comune. Manifest con URL e SHA256: `artifacts/correzioni-collana-2026-10-02/obblighi-commi-manifest.json`. La paginazione caricaArticolo, con sessione originata dall’URN e progressivo5/6, ha risolto la precedente acquisizione del solo inizio dell’articolo1. I vecchi file con c449/c512 nel nome non provano la presenza del relativo comma.

Il comma449 comprende scuole e università fra i soggetti obbligati alle convenzioni. Il comma450 le esclude dalla prima frase relativa alle amministrazioni statali e mantiene ambiti differenziati: non ricavarne esonero generale dall’acquisto digitale. Per le altre PA e authority, da5.000 sottoUE, MePA, altri mercati elettronici o sistema telematico regionale. Deroga510 per inidoneità della convenzione dovuta a mancanza di caratteristiche essenziali: autorizzazione del vertice e trasmissione alla Corte dei conti. ICT512/516: strumenti Consip/aggregatori per beni disponibili, deroga per indisponibilità/inidoneità o necessità e urgenza per continuità; autorizzazione motivata e comunicazione ANAC/AgID.

Caso laboratorio90.000 di arredi assegnato a università, non Comune: evita di ignorare il nuovo obbligo merceologico del DPCM2026 per enti locali oltre40.000. L’esclusione universitaria dall’art.9c3 non elimina il comma449 o gli altri strumenti obbligatori: l’ipotesi rende esplicita la verifica di indisponibilità.
''';s.write_text(t,encoding='utf8')
print('Riequilibrati nuclei 8/13/14, chiarita università nel caso arredi, spaziatura del testo e acquisizione normativa completate.')
