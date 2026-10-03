from pathlib import Path
import re
root=Path.cwd();base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali'
def append(rel,title,text):
 p=root/rel;s=p.read_text(encoding='utf-8')
 if title not in s:s+='\n## '+title+'\n\n'+text+'\n'
 s=re.sub(r'updated_at: [^\n]+','updated_at: 2026-10-03',s,count=1);p.write_text(s,encoding='utf-8')
append('wiki/sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17.md','Rettifica sul fermo del 3 ottobre 2026','Art. 86 D.P.R. 602/1973: divieto di circolazione, non divieto assoluto di alienazione; preavviso 30 giorni e prova della strumentalità. Sospensione del fermo dopo integrale e tempestivo prima rata nelle condizioni previste, cancellazione dopo saldo. Fonte primaria riletta: [AdER, procedure cautelari](https://www.agenziaentrateriscossione.gov.it/it/Per-saperne-di-piu/le-procedure/procedurecautelari/). Capitolo 07 e topic riscossione allineati.')
append('wiki/sources/catasto-cartografia-estimo-pubblicita-immobiliare-aggiornamento-2026-07-18.md','Integrazione estimativa del 3 ottobre 2026',"Tre esempi didattici FC02/10 esplicitano dati e ipotesi: comparazione 85 × 2.000 = 170.000; capitalizzazione perpetua 8.000 / 0,04 = 200.000; costo terreno 60.000 + fabbricato 160.000 × 0,75 = 180.000. Sono esercizi, non stime ufficiali né valori OMI. Metodo comparativo e capitalizzazione riscontrati nella [guida AE](https://www1.agenziaentrate.gov.it/web_app_entrate/guida_acquisto_casa.html); formula del costo definita nel testo come ipotesi didattica. L'art. 2808 c.c. attribuisce all'iscrizione efficacia costitutiva, non soltanto eventuale; fonte civile consolidata collegata al capitolo.")
append('wiki/topics/catasto-pubblicita-immobiliare-concorsi.md','Integrazione del 3 ottobre 2026','FC02/10 contiene tre calcoli con ipotesi, controllo del risultato e limite delle quotazioni OMI. Iscrizione ipotecaria costitutiva ai sensi dell’art. 2808 c.c.; si distinguono titolo e formalità. Fonti: [[sources/catasto-cartografia-estimo-pubblicita-immobiliare-aggiornamento-2026-07-18]], [[sources/diritto-civile-obbligazioni-contratti-m-fc02-2026-07-17]].')
for code in ['10']:
 p=next((base/'chapters').glob(code+'-*.md'));s=p.read_text(encoding='utf-8');s=s.replace('source_refs: [','source_refs: ["sources/diritto-civile-obbligazioni-contratti-m-fc02-2026-07-17.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/diritto-civile-obbligazioni-contratti-m-fc02-2026-07-17.md", ',1);p.write_text(s,encoding='utf-8')
anchors={'#IVA: operazioni, soggetti, detrazione e adempimenti':'#N-FC02-04-04 · IVA: operazioni, soggetti, detrazione e adempimenti','#Presupposto e soggetto passivo':'#N-FC02-04-02 · Presupposto, soggetti e obbligazione tributaria','#Livello 3 - Quadro UE fiscale, IVA e dogane':'#N-FC02-04-05 · Quadro UE fiscale, IVA e dogane'}
for p in (base/'chapters').glob('*.md'):
 s=p.read_text(encoding='utf-8')
 for a,b in anchors.items():s=s.replace(a,b)
 p.write_text(s,encoding='utf-8')
p=base/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf-8');s=s.replace('status: final','status: review-in-progress').replace('review_required: false','review_required: true');s=re.sub(r'updated_at: [^\n]+','updated_at: 2026-10-03',s,count=1)
s=s.replace('processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18','processo-tributario-regime-2026-rettifica-2026-10-03')
marker='## Delta della revisione integrale del 3 ottobre 2026'
if marker not in s:s+='''
## Delta della revisione integrale del 3 ottobre 2026

Le righe precedenti conservano il censimento storico. La revisione corrente integra le lacune sotto riportate; lo stato «integrato» attesta testo ed esercizi presenti, non approvazione normativa finale né pubblicabilità. Sono ancora da eseguire i gate 15–16 e il controllo dell’export candidato.

| Nucleo | Collocazione verificabile | Teoria e applicazione aggiunte | Fonte | Stato corrente |
| --- | --- | --- | --- | --- |
| Organi fiscali | cap. 03, Organi | Collegio dei revisori, Direttore e Comitato, con funzioni distinte | D.Lgs. 300/1999, art. 67 | integrato; controllo finale pendente |
| Metodi di accertamento | cap. 05, I metodi di accertamento | Cinque metodi, presupposti e scelta guidata | D.P.R. 600/1973, artt. 38–41 | integrato; controllo finale pendente |
| Garanzie e TCF | cap. 05, contraddittorio/autotutela/TCF | 60 giorni, limiti dell’autotutela, accesso 2026 e caso | L. 212/2000; D.Lgs. 128/2015 | integrato; controllo finale pendente |
| Sanzioni e reati | cap. 05a, soglie e termini | Imputazione agli enti, soglie cumulative, consumazione e due casi numerici | D.Lgs. 472/1997 e 74/2000, con D.Lgs. 87/2024 | integrato; controllo finale pendente |
| Processo | cap. 05b, regime 2026, termini e difesa | D.Lgs. 546/1992, ricorso/costituzione/appelli, 3.000 euro e calendario | Fonte rettifica processo 3 ottobre; TU dal 2027 | integrato; controllo finale pendente |
| Redditi e dichiarazioni | cap. 06, Determinazione e periodo | Cassa/competenza, pensioni, 12 gennaio, calcolo e 90 giorni | TUIR e D.P.R. 322/1998 | integrato; controllo finale pendente |
| Fermo | cap. 07, Fermo: preavviso, circolazione e tutele | Effetto corretto, strumentalità e caso | art. 86 D.P.R. 602/1973; AdER | integrato; controllo finale pendente |
| Dogane e accise | capp. 08–09 e glossario 14 | A.TR/origine, art. 173, vigilanza, destinatario registrato, EMCS a imposta assolta | CDU; direttiva 2020/262; note ADM | integrato; controllo finale pendente |
| Estimo e ipoteca | cap. 10, Tre calcoli estimativi | Comparazione, capitalizzazione e costo con risultati; iscrizione costitutiva | Fonte estimativa e codice civile art. 2808 | integrato; controllo finale pendente |
| Valutazioni di bilancio | cap. 11, immobilizzazioni/rimanenze/indici | Terreni, finanziarie, minore costo/realizzo, due margini | OIC 13/16/24 e codice civile | integrato; controllo finale pendente |
| Civile e società | cap. 12, sez. 4, 7 e 11 | Delegazione/espromissione/accollo, patologie, sei tipi societari e casi | codice civile e source notes pertinenti | integrato; controllo finale pendente |
| Metodo e apparati | capp. 01–14 | D = Diario; riferimenti pubblici; rimozione note staff archiviate; ancore corrette | Audit integrale e snapshot | integrato; controllo finale pendente |
'''
p.write_text(s,encoding='utf-8')
# Persist corrected register descriptions before further modules.
p=root/'artifacts/correzioni-collana-2026-10-02/update-vol03-register.py';s=p.read_text(encoding='utf-8');where='rows=[]';add="applied.update("+repr({28:'FC02/05a: soglie, condizioni, consumazione, calendario e imputazione sanzioni agli enti.',29:'FC02/05: cinque metodi, 60 giorni di contraddittorio, limiti autotutela e TCF 2026.',30:'FC02/06: criteri reddituali, pensioni, cassa allargata, calcolo e 90 giorni.',43:'FC02/07: fermo, circolazione, preavviso e strumentalità.',45:'FC02/13: tre etichette di svolgimento richiuse.',47:'FC02/13: D = Diario e relativa applicazione.',52:'FC02: accenti e apostrofi, Sara/stabilita/necessita e frase sui controlli corretti in contesto.',54:'FC02: apparati staff archiviati, bibliografia leggibile, rinvii alla produzione sostituiti da istruzioni di studio; tre ancore corrette.'})+")\n"
if add not in s:s=s.replace(where,add+where,1)
p.write_text(s,encoding='utf-8')
print('Fonti, ancore e matrice FC02 consolidate; registro aggiornabile')
