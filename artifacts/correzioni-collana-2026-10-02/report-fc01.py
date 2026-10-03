from pathlib import Path
import re,json,hashlib,shutil,collections
B=Path('wiki/books/moduli/m-fc01-ministeri');R=Path('wiki/reviews/pipeline/VOL-03');A=Path('artifacts/correzioni-collana-2026-10-02')
ids=[3,33,34,35,36,37,38,39,40,46,48,50]
reg=json.loads((A/'VOL-03-ledger.json').read_text(encoding='utf8'))
audit={}
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-03.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\| V03-\d{3} \|',line):
  c=[v.strip() for v in line.strip('|').split('|')];audit[c[0]]=c
p=B/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8');arc=A/'before-text/VOL-03'/('FC01-'+p.name)
if not arc.exists():shutil.copy2(p,arc)
s=s.replace('✓ 35 definizioni','✓ definizioni integrate con competenza finanziaria, cassa e residui')
s+='\n## Delta della revisione integrale del 3 ottobre 2026\n\nIl censimento storico è conservato. Le integrazioni correnti correggono le lacune dell’audit integrale; i relativi stati sono documentati nei rapporti 14 e 15 correnti. Non è una nuova attestazione di pubblicabilità del PDF.\n\n| ID | Collocazione | Integrazione verificabile | Verifica | Stato |\n| --- | --- | --- | --- | --- |\n'
for row in reg['findings']:
 if int(row['id'][-3:]) in ids:s+='| '+row['id']+' | '+row['position']+' | '+row['correction']+' | caso, domanda o batteria commentata nel capitolo | integrato, audit 15 corrente |\n'
p.write_text(s,encoding='utf8')
for p in (B/'chapters').glob('*.md'):
 s=p.read_text(encoding='utf8');fm,body=s.split('---',2)[1:]
 if 'ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md' not in fm:fm=fm.replace('source_refs: [','source_refs: ["sources/ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md", ',1)
 if 'sources/aran-ccnl-funzioni-centrali-pcm-2022-2026.md' not in fm:fm=fm.replace('source_refs: [','source_refs: ["sources/aran-ccnl-funzioni-centrali-pcm-2022-2026.md", ',1)
 fm=fm.replace('topics: [','topics: ["ministeri-organizzazione-bilancio-rettifiche-2026", ',1)
 fm=fm.replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md", ',1)
 p.write_text('---'+fm+'---'+body,encoding='utf8')
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |\n'
for row in reg['findings']:
 if int(row['id'][-3:]) in ids:
  c=audit[row['id']];table+='| '+row['id']+' | '+row['position']+' | '+c[2]+' | '+c[3]+' | '+c[4]+' | '+row['correction']+' | Applicato e riesaminato nel testo |\n'
text='''# M-FC01 — Correzioni integrali, step 14, 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i 12 rilievi pertinenti al modulo Ministeri. La revisione integra norme e teoria mancanti, riscrive 60 quiz e fornisce 100 criteri di correzione delle domande aperte. Sono preservati esempi e nuclei legittimi; gli apparati staff dei capitoli 01–07 sono archiviati e sostituiti da riferimenti leggibili.

## 2. Metodo e copertura

Baseline: audit integrale VOL-03, con lettura completa già documentata. Nella correzione sono riletti i blocchi interessati, verificati i claim cruciali su fonti primarie e controllati calcoli, opzioni e commenti. Il testo resta in revisione fino al riesame specialistico e al freeze CLI.

## 3. Registro per ID

'''+table+'''
## 4. Fonti ed evidenze

Nota nuova `ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md`, topic collegato e rettifiche delle note ARAN e contabilità statale. Fonti: RGS, Camera, Gazzetta Ufficiale, MEF, ARAN/testo pubblicato dalla Difesa, Avvocatura e Consip. URL e ambiti sono nelle note. Originali e trasformazioni sono negli artefatti; nessun file raw precedente è modificato.

## 5. Coerenza e autonomia

Allineato BANDO a Bando/Aree/Nuclei/Diario/Output. Le quattro sezioni formali del PIAO sono distinte dalle dimensioni didattiche. Regime generale, eccezioni e casi sono separati; il rinnovo contrattuale del 2026 non rende simultaneamente efficaci tutte le clausole. Il lettore può correggere le cento risposte senza aprire il wiki.

## 6. Verifiche

Sessanta quiz con quattro alternative uniche, una chiave coerente e commento; 15 risposte per ciascuna lettera complessivamente. Nuova verifica del calcolo dei residui: (100−80)+(80−60)=40. Rinvii nel corpo: zero destinazioni/ancore mancanti. Gate didactic-density 08–15 superati; il capitolo 15 conserva due warning non bloccanti per la lunghezza del nucleo con cento soluzioni. I criteri sono divisi in cinque gruppi; resta necessario controllare il PDF, senza diminuire il carattere né eliminare risposte.

## 7. Suggerimenti facoltativi

Nessun suggerimento facoltativo è assunto come condizione di chiusura. Eventuali indici di rinvio più analitici si valuteranno soltanto dopo l'export.

## 8. Priorità

Audit specialistico 15 e congelamento del testo 16, poi controllo delle figure, PDF candidato e preflight di volume. FC03 resta in lavorazione autonoma.

## 9. Giudizio

Le dodici correzioni sono applicate nel manoscritto; nessuna attestazione di pubblicabilità dell'export. I gate conclusivi e la verifica visiva restano distinti.

## 10. Limiti

La verifica normativa è circoscritta ai claim inseriti o corretti; non inventa calendari di bandi, nominativi o documenti futuri. Il corpus storico non è dichiarato integralmente riconfermato. Il controllo testuale non sostituisce il PDF rigenerato.
'''
p=R/'14-moduli-m-fc01-ministeri.md';arc=A/'before-text/VOL-03'/p.name
if p.exists() and not arc.exists():shutil.copy2(p,arc)
p.write_text(text,encoding='utf8')
print('Matrice, frontmatter e rapporto 14 FC01 aggiornati.')
