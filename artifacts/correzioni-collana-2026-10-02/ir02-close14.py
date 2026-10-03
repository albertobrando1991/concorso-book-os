from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir02-universita-afam');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
for p in (B/'chapters').glob('*.md'):
 t=p.read_text(encoding='utf8').replace("Si'",'Sì').replace("si'",'sì').replace("purche'",'purché').replace("affinche'",'affinché')
 t=t.replace('secondo la fonte MUR consolidata','come indicato dal MUR').replace('Il riferimento consolidato comprende','Il quadro normativo comprende').replace('requisiti specifici non consolidati','requisiti specifici non verificati')
 p.write_text(t,encoding='utf8')
p=Path('wiki/sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05.md');t=p.read_text(encoding='utf8').replace('[[entities/ministero-cultura]]','[[entities/ministero-universita-ricerca]]');p.write_text(t,encoding='utf8')
evidence={1:'Quattro profili e decoder; confine nazionale/locale.',2:'Organi L. 240, ruoli e composizioni; caso proposta/approvazione di bilancio.',3:'Titoli e CFU, 6×25=150 ore; PQA/NdV/CPDS e documenti AVA3.',4:'Rinuncia/decadenza/interruzione/sospensione; borsa ER.GO, due indicatori e requisiti ulteriori.',5:'Documento, protocollo, fascicolo, accesso e servizio; caso con sequenza e confini di competenza.',6:'Documenti D.Lgs. 18 e D.I. 34/2025; tre assestamenti e bilancio quadrato a 215.000.',7:'Ciclo del progetto; costi effettivi/unitari/forfait/lump sum, esercizi 3.360 e 2.000; variazioni.',8:'PRIN/Horizon/PNRR distinti; DNSH obbligatorio, milestone/target e utenti verificabili 112 su 120.',9:'REICAT/ISBD/UNIMARC/SBNMARC; authority/soggetto/classificazione/collocazione, record e ILL/DD.',10:'Tirocinio curriculare con soggetti e atti; Learning Agreement e transcript, caso 18/12 crediti.',11:'AFAM statale/non statale, otto organi, CFA e titoli; 8×25=200 ore.',12:'Quattro prove con dati, consegna, documento risolto e griglia 10 punti; errori critici.'}
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8');t=re.sub(r'^status:.*$','status: coverage_reconciled',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
t=re.sub(r'`Completo` attesta[^\n]+','`Completo` è riferito al testo effettivo nel perimetro assegnato, riscontrato il 3 ottobre 2026. La tabella delle evidenze collega i nuclei a teoria, applicazione e verifica; non certifica ogni bando né la pubblicabilità del PDF.',t)
t=t.split('\n## Blocker ordinati')[0]+'\n## Riconciliazione sul testo corrente\n\n| Capitolo e nuclei | Evidenza didattica | Verifiche |\n| --- | --- | --- |\n'
for n,s in evidence.items():
 pcap=next((B/'chapters').glob(f'{n:02}-*.md'));body=pcap.read_text(encoding='utf8').split('\n---\n',1)[1];q=len(re.findall(r'\*\*Quiz \d+',body));t+=f'| {n:02}, N-IR02-{n:02}-01–05 | {s} | Q:{q} C:1 E:1, risolti nel capitolo |\n'
t+='''
La checklist dimensionale riguarda definizione, funzione, fonti, elementi, distinzioni, conseguenze, esempio, prova, errore e verifica: i primi cinque nuclei di ciascun capitolo distribuiscono queste dimensioni; i casi aggiunti rendono operativi i concetti prima trattati solo in termini generali. I conteggi reali in `M-IR02-surface-counts.json` rilevano 60 nuclei, tutti sopra 600 parole; la lunghezza non è usata come prova autonoma di completezza.

Fonti aggiuntive: [[sources/contabilita-economico-patrimoniale-universita-enti-pubblici]], [[sources/grant-management-horizon-pnrr-2026-08-23]], [[sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05]], [[sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24]]. Esempi locali o inventati sono dichiarati. L'audit specialistico e il PDF aggiornato sono passaggi distinti; la correzione dell'export IR02/09 viene verificata nel ciclo del renderer.
''';p.write_text(t,encoding='utf8')
p=B/'index.md';t=p.read_text(encoding='utf8').replace('M-IR02 - Universita e AFAM','M-IR02 — Università e AFAM').replace('text_frozen','correction-in-progress').replace('text_freeze','editorial_revision').replace('testi completi, in revisione trasversale del modulo.','correzioni testuali applicate; audit specialistico e nuovo PDF da completare.').replace('source notes consolidate e review umana','fonti consolidate e audit specialistico; la conferma umana riguarda il pacchetto finale');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
p=Path('wiki/books/volumi/vol-06-scuola-universita-ricerca-cultura/planning/01-indice-analitico.md');t=p.read_text(encoding='utf8').replace('Appendici: 4.600 parole. Target: 32.400 parole.','Apparati effettivi nei capitoli: bilancio numerico e forme di costo nei 06–08; record bibliografico e servizi nel 09; mobilità e tirocinio nel 10; quattro simulazioni con rubriche nel 12. Nessuna appendice separata promessa. Il target progettuale storico di 32.400 parole non è una misura del testo corrente.');p.write_text(t,encoding='utf8')
p=Path('wiki/topics/m-ir02-universita-afam-fonti-e-profili.md');t=p.read_text(encoding='utf8')+'''
## Correzioni verificate il 3 ottobre 2026

Organi universitari, CFU/titoli, AVA3, carriere e beneficio ER.GO sono spiegati nei capitoli 02–04 con fonti ufficiali. D.I. 34/2025 e AGA artt. 5–6 alimentano i casi numerici e di grant nei 06–08. Standard catalografici e accessi nel 09, accordo/transcript e tirocinio nel 10, organi/CFA e istituzioni statali/non statali nel 11; quattro output risolti nel 12. Matrice collegata ai nuclei effettivi. Fonti: [[sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24]], [[sources/contabilita-economico-patrimoniale-universita-enti-pubblici]], [[sources/grant-management-horizon-pnrr-2026-08-23]], [[sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05]]. Nessuna attestazione sul PDF aggiornato.
''';p.write_text(t,encoding='utf8')
p=R/'14-moduli-m-ir02-universita-afam.md';arc=C/'archive/pre-correzioni-14-m-ir02.md'
if not arc.exists():arc.write_bytes(p.read_bytes())
rows=[('V06-09','02–04','Governance, CFU, AVA, carriere e DSU completati.'),('V06-10 quota IR02','06–08','Bilancio numerico, quattro forme di finanziamento, milestone e target.'),('V06-11 quota IR02','09','Standard catalografici, authority, soggetti, record e ILL/DD.'),('V06-12','10','Mobilità e tirocinio con attori, documenti e casi.'),('V06-13/14','11','AFAM statale/non statale, organi e titoli; rimossa bozza duplicata.'),('V06-15/16','12','Quiz corretto e regola budget resa coerente con flessibilità del grant.'),('V06-24 quota IR02','12','Quattro prove chiuse, documenti risolti e rubrica.'),('V06-33/35 quota IR02','Tutti','Superficie, fonti leggibili, matrice e promesse di apparati riallineate.'),('V06-34','09–10','Bibliografia separata dai titoli H2.')]
p.write_text('''# M-IR02 — Correzioni del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i rilievi universitari dell'audit integrale e le quote pertinenti dei rilievi trasversali. Le altre quote restano aperte nel registro di volume.

## 2. Checklist

Autonomia, copertura, definizioni, fonti, casi, calcoli, quesiti, coerenza delle promesse, superficie e metadati. L'impaginato aggiornato resta da controllare.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(f'| {i} | {pos} | Testo e didattica | Media | {s} | Delta inserito e raccordato alle fonti | Corretto |' for i,pos,s in rows)+'''

## 4. Osservazioni per capitolo

'''+ '\n\n'.join(f'{n:02}: {s}' for n,s in evidence.items())+'''

## 5. Coerenza globale

Matrice corrente raccordata ai 60 nuclei e ai casi. Frontmatter conserva le dipendenze; il corpo offre riferimenti leggibili. Archiviate le note interne, eliminata la bozza duplicata AFAM. Gli apparati sono nei capitoli, senza appendici inesistenti.

## 6. Fonti

Consolidati L. 240 art. 2; D.M. 270 artt. 3/5/7; D.P.R. 132 artt. 4–8 e 212 artt. 3/6/8; D.Lgs. 18 art. 1; D.I. 34/2025 nelle pagine dichiarate; ANVUR AVA3 e bando ER.GO art. 7; AGA artt. 5–6; REICAT/ICCU, IFLA e BNCF nelle parti dichiarate; linee guida Erasmus KA131 e procedura UniBo. Nuovi contenuti scritti dopo il consolidamento.

## 7. Suggerimenti facoltativi

Nessun ulteriore ampliamento necessario per i rilievi assegnati al modulo.

## 8. Priorità

Audit specialistico, text freeze, rigenerazione e controllo PDF. Verificare nel nuovo impaginato anche il ripristino dei cinque nuclei di IR02/09 effettuato nel renderer.

## 9. Pubblicabilità

Non attestata; gli altri moduli di VOL06 e i controlli PDF sono ancora in corso.

## 10. Limiti

Baseline di lettura integrale precedente; ora riesame dei delta e raccordi, non nuova lettura integrale dichiarata delle parti invariate. Riscontri esterni selettivi, con sezioni e copie indicate nelle fonti. Valori ipotetici distinti dalle soglie normative. Nessun controllo di ogni regolamento locale o di ogni pagina dei manuali tecnici.
''',encoding='utf8')
print('IR02 raccordi e report14 completati')
