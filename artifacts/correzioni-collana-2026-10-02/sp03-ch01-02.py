from pathlib import Path
import re,shutil
B=Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato/chapters');C=Path('wiki/reviews/correzioni-collana-2026-10-02/archive')
for n in [1,2]:
 p=next(B.glob(f'{n:02}-*.md'));a=C/f'pre-correzioni-sp03-{n:02}.md';assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
 if n==1:
  t=t.replace('La magistratura ordinaria richiede di studiare per decidere controversie e questioni penali, civili e amministrative con indipendenza e imparzialità.','La magistratura ordinaria esercita la giurisdizione civile e penale, nelle funzioni giudicanti e requirenti previste dall’ordinamento. Non va confusa con la magistratura amministrativa, percorso professionale escluso da questo modulo. Il diritto amministrativo compare nel concorso ordinario, ma ciò non trasferisce al giudice ordinario la giurisdizione generale del giudice amministrativo. Restano le attribuzioni specifiche e le questioni incidentali previste dalla legge. Indipendenza e imparzialità vanno studiate in rapporto alle funzioni, senza far coincidere ogni magistrato con il solo giudice che decide una controversia.')
  t=re.sub(r'Un ultimo avviso riguarda le fonti\. Un file intitolato.*?(?=\n\n)', 'Per la decisione personale conta il regime applicabile alla pratica, non il nome di un documento. Controlla durata, continuità, periodo universitario computabile e termine della tornata. Se la pratica è ancora in corso al momento dell’invio anticipato, la data decisiva resta quella prevista dal bando: non confondere la scadenza con il giorno in cui hai aperto il modulo. Le dichiarazioni devono rappresentare correttamente il periodo e la data di compimento.',t,flags=re.S)
  t=t.replace('La legge 1035/1966 resta un riferimento storico e ordinamentale nel perimetro verificato, ma non sostituisce il bando contemporaneo su requisiti, prove e qualifica bandita.','Il limite anagrafico si collega al D.P.C.M. 141/2000, art. 1, modificato nel 2011. La legge 1035/1966 resta un riferimento ordinamentale, ma il suo solo art. 1 non dimostra la soglia attuale. Inoltre l’art. 4 del bando esclude chi non abbia conseguito l’idoneità due volte in precedenti esami per procuratore dello Stato: anche questo fascicolo deve contenere gli esiti precedenti.')
  t=t.replace('La verifica anagrafica non si fa con espressioni approssimative come "ho trentacinque anni".','La verifica anagrafica non si fa con espressioni approssimative come "ho trentacinque anni". L’indirizzo richiamato dall’Adunanza plenaria 21/2011 colloca il superamento dal giorno successivo al compleanno: la formula “non superato” non regala un ulteriore anno fino ai trentasei. Occorre inoltre accertare se spetti una specifica elevazione e provarne i presupposti; non è un beneficio automatico.')
  t=t.replace('Per l\'Avvocatura guardi qualifica, limite anagrafico, materie, durata, sede ed eventuale prova anticipata.','Per l’Avvocatura guardi qualifica, limite anagrafico ed eventuali benefici, precedenti non idoneità, materie, durata, sede ed eventuale prova anticipata.')
  t=t.replace('scelta del binario, requisiti, prove, scrittura lunga, ordinamenti, calendario','scelta del binario, requisiti, prove, scrittura lunga, orientamento ordinamentale, calendario')
  t=t.replace('requisiti, prove, scrittura lunga, ordinamenti, calendario','requisiti, prove, scrittura lunga, orientamento ordinamentale, calendario')
  t=t.replace('Manuali o corsi specialistici possono essere necessari per approfondire le materie e allenare temi o atti,','Questo percorso insegna orientamento e metodo, non l’intero programma universitario o professionale delle tre selezioni. Materiali specialistici completi servono a colmare la teoria di materia non sviluppata qui e ad allenare temi o atti,')
 if n==2:
  t=t.replace('Aggiunge almeno una sequenza','Aggiungi almeno una sequenza')
  t=t.replace('La soglia è di almeno sei decimi in ciascuna materia e l\'idoneità richiede anche il punteggio complessivo previsto.','L’art. 8 del bando richiede almeno sei decimi nelle materie orali valutate numericamente; per il colloquio nella lingua straniera prescelta richiede invece un giudizio di sufficienza. Occorre inoltre una votazione complessiva nelle due prove non inferiore a 108 punti e non sono ammesse frazioni. Sono condizioni cumulative: il totale non compensa una materia insufficiente e il colloquio linguistico non aggiunge un voto numerico inventato.')
  marker='### Domanda-trappola\nSe il candidato ottiene un voto molto alto'
  insert='''### Caso di calcolo: totale e soglie separate

Tre scritti valutati 14, 14 e 14 danno 42. Supponi che tutti i gruppi orali valutati numericamente siano almeno sufficienti e sommino 66, e che la lingua abbia giudizio sufficiente: 42 + 66 = 108, quindi le condizioni di punteggio del caso sono soddisfatte. Se gli orali sommano 65, il totale è 107 e manca la soglia complessiva, pur con le singole sufficienze. Se una materia orale vale 5/10, una somma complessiva di 112 non sana l’insufficienza. Infine, lingua insufficiente impedisce l’idoneità anche con 108 o più punti numerici. Prima si controllano tutti i minimi, poi la somma: invertire l’ordine può nascondere un requisito non soddisfatto.

'''
  assert marker in t;t=t.replace(marker,insert+marker)
  t=t.replace('Vuole decidere se presentare domanda, come allenarsi e quali dati registrare.','Nel novembre 2025 vuole decidere se presentare domanda entro il termine, come allenarsi e quali dati registrare. La verifica iniziale usa il bando già pubblicato e gli esiti pregressi; non usa un diario futuro.')
  t=t.replace('Il diario della tornata indica prove scritte nelle giornate del 24, 25 e 26 giugno 2026.','**Secondo momento del caso: marzo 2026.** Marta ha già inviato tempestivamente la domanda. Il diario del 24 febbraio, pubblicato il 10 marzo 2026, indica prove scritte nelle giornate del 24, 25 e 26 giugno 2026.')
  t=t.replace('Secondo passaggio: calendario. Marta registra il dato della tornata:','Secondo passaggio, successivo all’invio: calendario. Nel marzo 2026 Marta aggiorna il piano con il dato della tornata:')
  t=t.replace('Marta può impostare la domanda sulla categoria del laureato se il suo titolo soddisfa il requisito di durata previsto dalla disciplina vigente e dal bando.','La decisione di novembre 2025 permette a Marta di impostare la domanda sulla categoria del laureato se il suo titolo soddisfa i requisiti del bando. L’aggiornamento di marzo 2026 modifica calendario e preparazione materiale, non riapre il termine della candidatura.')
  t+='''

9. Una candidata ha tutti i minimi numerici soddisfatti, 42 punti negli scritti e 66 all’orale, ma lingua insufficiente. È idonea?

A. Sì, perché 108 compensa la lingua.
B. No, perché è necessario anche il giudizio sufficiente nella lingua.
C. Sì, perché la lingua vale sempre zero.
D. No, perché servono sempre più di 108 punti.

**Risposta corretta: B.** L’art. 8 richiede insieme minimi numerici, totale almeno 108 e sufficienza linguistica. A e C cancellano una condizione autonoma; D trasforma il minimo incluso in una soglia strettamente superiore.
'''
 p.write_text(t,encoding='utf8')
print('SP03/01-02 corrected')
