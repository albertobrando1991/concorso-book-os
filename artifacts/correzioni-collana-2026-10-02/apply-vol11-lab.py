from pathlib import Path
exec(Path('artifacts/correzioni-collana-2026-10-02/apply-vol11-pc.py').read_text(encoding='utf8').split("p=next(B.glob('10-")[0])
S='sources/vol-11-energia-sostenibilita-verifica-2026-10-03'
p=next(B.glob('14-*.md'));t=p.read_text(encoding='utf8')
# Move method blocks before the units they had interrupted, preserving all prose.
for number in [1,3,5,8]:
 pat=rf'(### Simulazione {number} — [^\n]+\n\n)(.*?)(?=\*\*Consegna\.\*\*)'
 t=re.sub(pat,lambda m:m[2]+m[1],t,count=1,flags=re.S)
a=t.index('### Da sapere in 5 righe');b=t.index('Una risposta forte parte dalla consegna',a)
block=t[a:b].replace('### Da sapere in 5 righe\n\n','');t=t[:a]+block+'### Da sapere in 5 righe\n\n'+t[b:]
t=t.replace('Ho evitato soglie non presenti?','Ho distinto fatti mancanti e soglie normative da conoscere?')
t=t.replace('Energia, clima, DNSH e CAM chiedono metodo più che calcolo.','Energia, clima, DNSH e CAM richiedono metodo e calcoli coerenti con i dati disponibili.')
t=t.replace('Se mancano soglie, competenze regionali o titolo autorizzativo, il candidato deve:','Se mancano il limite specifico del titolo autorizzativo e gli elementi necessari a individuare la competenza regionale, il candidato deve:')
t=t.replace('**Risposta corretta: C.** Commento: dichiarare il limite informativo è parte della soluzione, non una rinuncia.','**Risposta corretta: C.** Commento: i fatti e gli atti specifici mancanti richiedono istruttoria; le regole normative note e applicabili vanno invece utilizzate, anche quando la traccia non le ricopia.')
t=add(t,14,1,'''### Dato mancante o regola da conoscere?

Non inventare la concentrazione misurata, la classificazione acustica locale o il contenuto di un'autorizzazione assente. È diverso applicare una regola nazionale studiata: il pagamento ridotto dell'art. 16 della L. 689/1981 o i minimi delle fasi di allertamento non diventano «dati mancanti» solo perché la traccia non li trascrive. Quando i fatti sono sufficienti, prendi posizione, esegui il calcolo e indica il criterio. Quando non lo sono, formula una conclusione condizionata e l'accertamento preciso necessario.''')
def replace_output(t,n,x):
 a=t.index(f'### Simulazione {n} —');b=t.index('**Risposta/output modello.**',a);e=t.index('**Griglia di correzione.**',b)
 return t[:b]+'**Risposta/output modello.**\n\n'+x.strip()+'\n\n'+t[e:]
t=replace_output(t,6,'''| Ramo | Dato da acquisire/verificare | Operazione e prova |
|---|---|---|
| Emissioni | Titolo, punti emissivi, limiti e condizioni di esercizio | Organo competente: sopralluogo, campionamento pertinente e verbale |
| Aria ambiente | Serie di rete, rappresentatività, meteo e possibili sorgenti | Valutazione tecnica separata dal solo dato al camino |
| Rumore | Classe, ricettori, periodo, ambientale/residuo e condizioni di misura | Tecnico competente: misure e rapporto con metodo e strumenti |
| Segnalazioni | Data, ora, luogo e descrizione circostanziata | Ufficio: registro degli esposti e collegamento ai controlli |
| Esito | Dati validati e disposizione applicabile | Autorità competente: valutazione motivata, eventuali atti e successivo controllo |

**Nota al responsabile.** Le segnalazioni orientano il controllo ma non provano da sole il superamento. Il titolo va letto per ogni punto emissivo; aria ambiente e rumore richiedono criteri distinti. **Integrazione della traccia:** ricettore esterno in classe III, periodo diurno, Leq validato e confrontabile 62 dB(A), limite di immissione applicabile 60, escluse discipline speciali. Lo scostamento è **2 dB**. Non è il differenziale interno e non qualifica da solo un reato. Si conserva il rapporto di prova e si procede secondo autorità, norma e responsabilità accertate.''')
t=t.replace('**Griglia di correzione.** 2 punti per distinzione emissione/aria/rumore; 2 per qualità del dato; 1 per titolo; 1 per verbale.','**Griglia di correzione.** 1 punto per tabella e nota entrambe presenti; 1 per separazione dei tre rami; 1 per calcolo 62 − 60; 1 per qualità del dato; 1 per responsabilità; 1 per prova e seguito. Totale 6.')
t=replace_output(t,8,'''| Priorità/azione | Output e indicatore | Responsabile e termine didattico |
|---|---|---|
| 1. Definire perimetro | Inventario di edifici, usi e vettori inclusi | Ufficio tecnico, giorno 2 |
| 2. Riconciliare i due POD | Due associazioni documentate a contratti e contatori | Patrimonio e gestore, giorno 5 |
| 3. Misurare la superficie mancante | m² utili e documento di rilievo | Tecnico incaricato, giorno 7 |
| 4. Costruire baseline | kWh normalizzati, orari e comfort del triennio | Referente energia, giorno 10 |
| 5. Ridurre il fabbisogno | Misure di regolazione; kWh evitati a pari servizio | Gestore edificio, giorno 15 |
| 6. Istruire fotovoltaico | Copertura, potenza, titolo, rete e produzione stimata | Ufficio tecnico e progettista, giorno 20 |
| 7. Istruire CER | Soggetto, partecipanti, cabina e calcolo orario | Referente del progetto, giorno 25 |
| 8. Approvare monitoraggio | Responsabili, costi, kWh, fattore CO₂e e verifica trimestrale | Dirigente, giorno 30 |

I termini sono un programma del caso, non termini legali. Non si inventano consumi dei POD ignoti; si documenta la riconciliazione. La produzione viene dimensionata sul fabbisogno residuo; i benefici CER restano subordinati ai requisiti del servizio e del sostegno.''')
t=t.replace('**Griglia di correzione.** 2 punti per baseline; 2 per priorità; 1 per CER non automatica; 1 per indicatori.','**Griglia di correzione.** 1 punto per otto righe effettive; 1 per baseline; 1 per ordine efficienza/produzione; 1 per CER istruita; 1 per indicatori; 1 per responsabili e termini. Totale 6.')
t=replace_output(t,10,'''**Nota al dirigente — aggiornamento didattico delle 10:00.** Il piano comunale prevede interdizione del sottopasso se è osservato allagamento: il presidio lo conferma alle 9:50. Si attiva subito la funzione competente per chiusura e percorso alternativo, con riscontro dell'avvenuta interdizione, senza attendere uno stato di emergenza nazionale. Le segnalazioni ambientali sono registrate separatamente e ancora da validare.

| Azione | Assegnazione | Termine e verifica |
|---|---|---|
| Sottopasso e assistenza | Funzione comunale viabilità/PC secondo piano | Subito; conferma chiusura e percorso sicuro entro le 10:15 |
| Rifiuti trascinati | Servizio ambiente con operatori abilitati | Sopralluogo entro le 11:00; origine, flussi e filiera documentati |
| Scarico e depuratore | Ufficio competente e gestore, raccordo organo tecnico | Acquisire titolo, schema e condizioni entro le 11:30; campioni se pertinenti |
| Odori | Ufficio ambiente e supporto tecnico | Registro localizzato e confronto con esercizio; primo quadro alle 12:00 |
| Materiali della palestra | RUP e direzione lavori | Prima dell'accettazione/posa: confronto requisiti e prove della variante |
| Comunicazione | Funzione informazione del piano | Avviso viabilità alle 10:15; nuovo aggiornamento alle 12:00 |

Gli orari sono priorità operative della simulazione. Non attribuiamo al depuratore l'origine di ogni odore né responsabilità senza prova. La palestra non è utilizzabile per assistenza solo perché è comunale: è in cantiere e servono condizioni di sicurezza e disponibilità. Alle 12:00 il dirigente riceve stato delle azioni, dati validati, richieste di supporto e questioni aperte.''')
t=t.replace('**Vincolo.** 25 righe, 20 minuti.','**Vincolo.** Nota di massimo 12 righe più tabella di 6 azioni, 20 minuti: 3 per analisi, 10 per nota/tabella, 4 per controlli di competenza e prova, 3 per revisione.')
t=t.replace('**Griglia di correzione.** 2 punti per priorità PC; 2 per separazione dei fatti AMB; 1 per DNSH/CAM; 1 per dati mancanti; 1 per output e tracciabilità; 1 per tono proporzionato.','**Griglia di correzione.** 2 punti per sicurezza e piano; 2 per rami ambientali separati; 1 per variante CAM/DNSH; 1 per fatti e incertezze; 1 per responsabili e termini; 1 per formato e verifica. Totale 8; esercizio da ripetere se manca una priorità di sicurezza anche con punteggio complessivo sufficiente.')
append='''## Appendice A — Protezione civile operativa

Questa scheda accompagna i capitoli 10–11. Si compila con il piano locale, senza sostituirlo.

| Campo | Modello compilato per Vallechiara |
|---|---|
| Scenario e validità | Ramo A: allerta idrogeologica Z-4 dalle 18:00 alle 12:00; ruscellamento osservato alle 15:20 |
| Centro e funzioni | COC secondo piano; tecnica, viabilità, assistenza, informazione; nominativi e sostituti dal piano |
| Fase | Almeno attenzione per arancione; innalzamento motivato dalle osservazioni |
| Aree | Piazza alta: attesa; palestra verificata: assistenza; piazzale sicuro: ammassamento |
| Persone e servizi | Frazione nord e RSA; autonomia elettrica da verificare |
| Comunicazione | Canali comunali e raccordo regionale; nessuna attesa di IT-alert meteo |
| Prossimo controllo | Presidio ogni 30 minuti; registrare ora, fonte, azione ed esito |

Per usare la scheda in altro territorio, sostituisci ogni dato fittizio con quello del piano e verifica sicurezza e accessibilità delle aree. Nel ramo industriale si applica il raccordo PEE, non la stessa sequenza meteo.

## Appendice B — Clima, energia e indicatori

| Indicatore | Formula e esempio | Condizione di utilizzo |
|---|---|---|
| Risparmio energetico | 120.000 − 90.000 = 30.000 kWh/anno | Stesso perimetro e servizio, dati normalizzati |
| Riduzione percentuale | 30.000/120.000 × 100 = 25% | Baseline documentata |
| Ritorno semplice | 36.000/6.000 = 6 anni | Beneficio netto annuo; non sostituisce LCC |
| CO₂e evitata | 30.000 × 0,25 = 7,5 t/anno | Fattore illustrativo; sostituire con quello pertinente |
| Condivisione CER | min(80,50)+min(20,70)=70 kWh | Misure orarie e configurazione ammissibile |
| Avanzamento | Azioni completate/azioni programmate | Misura il processo, non le emissioni |

Il PNIEC orienta le politiche energia-clima; il PNACC l'adattamento. Nel rapporto locale separa risultato fisico, spesa, avanzamento e comfort. Per i titoli FER usa la sequenza allegati A/B/C e vincoli del capitolo 12; per gli incentivi verifica il meccanismo specifico.

## Appendice C — Ambiente negli enti locali

| Caso ricevuto dall'ufficio | Prima verifica | Documento e seguito |
|---|---|---|
| Liquido in caditoia | Collegamento, origine, ricettore e titolo | Schema idraulico, verbale e raccordo con autorità competente |
| Materiali di manutenzione | Origine, classificazione e produttore | Schede dei flussi, EER/HP, filiera e tracciabilità |
| Rumore notturno | Ricettore, classe, periodo e metodo | Piano di misura e rapporto; confronto pertinente |
| Superamento CSC | Rappresentatività, comunicazioni e prevenzione | Procedimento di caratterizzazione/analisi di rischio |
| Modifica impianto | Titolo esistente e natura della modifica | Istruttoria sul regime e sugli assensi necessari |
| Inadempimento accertato | Norma, autorità, responsabilità e termini | Atto motivato, notifiche e verifica del seguito |

L'ufficio comunale non assume ogni competenza ambientale per il solo fatto di ricevere l'esposto. Indica sempre quale legge, delega o titolo individua il decisore e quale organo svolge il controllo tecnico.

## Appendice D — Registri, piattaforme e dati

| Strumento o fonte | A cosa serve | Che cosa non dimostra da solo |
|---|---|---|
| Registro cronologico | Documentare movimenti secondo obblighi e tempi applicabili | Autorizzazione alla gestione |
| FIR / RENTRI | Tracciare il trasporto e gli adempimenti digitali; per iscritti FIR digitale dal 16 settembre 2026 | Corretta classificazione del rifiuto |
| MUD | Comunicazione annuale nei soggetti e flussi previsti | Regolarità di ogni trasporto |
| SNPA / ARPA / APPA | Dati, metodi e rapporti tecnici istituzionali | Violazione specifica senza confronto e contesto |
| GSE / ARERA | Regole, misure e servizi energetici secondo competenze | Titolo per costruire l'impianto |
| Cataloghi e portali territoriali | Localizzare dataset, piani e versioni | Attualità di una copia senza data |

Scheda minima del dato: **ente — documento/dataset — versione — data di acquisizione — unità — periodo — territorio — metodo — limite — impiego nella decisione**. Esempio: serie PM10 annuale; 38 superamenti giornalieri e media annua 32 µg/m³ producono due giudizi distinti rispetto a 35 giorni e 40 µg/m³, nei presupposti del capitolo 08.

## Appendice E — Toolkit 30/60/90 e simulazioni

Scegli uno dei calendari alternativi del capitolo 01: 30 giorni con 2 ore al giorno; 60 giorni con 90 minuti; 90 giorni con un'ora. Non sono durate cumulative. Distribuisci il tempo secondo il profilo e conserva una prova settimanale corretta; il criterio didattico è almeno cinque risposte corrette su sei, più caso con passaggi essenziali presenti.

**Decoder compilato, bando fittizio EN.** Prova: quesito e caso in 60 minuti. Programma: FER, CER, efficienza, DNSH/CAM e principi ambientali. Priorità: capitoli 12–13; supporto 02–04 e 08; laboratorio 14. Output: matrice energia e nota variante. Vincolo: non attribuire incentivi senza requisiti. Le materie comuni si recuperano nei capitoli indicati del volume base secondo la mappa del proprio bando.

**Diario compilato.** Errore: condivisa CER calcolata sui totali giornalieri, 100 kWh. Causa: ignorata la simultaneità. Regola: somma dei minimi orari, 70. Correzione: rifare il caso con tre ore; richiamo a 24 ore, 7 e 21 giorni. Esito: annotare calcolo e motivazione, non soltanto «corretto».

**Scheda procedimento.** Oggetto → fatto qualificato → norma/versione → autorità → domanda e documenti → termine con decorrenza/sospensioni → atto → comunicazione → controllo. Esempio PAS: l'efficacia richiede la pubblicazione prevista nel Bollettino regionale; il mero trascorrere di 30 giorni non basta a descrivere tutti i casi.

**Verbale minimo.** Data, ora, luogo, operatori e ruolo; oggetto e titolo; operazioni e metodo; dati osservati; documenti acquisiti; dichiarazioni distinte dai fatti; allegati; limiti; firme e trasmissioni. Per un campione aggiungi identificazione, custodia e collegamento al rapporto di prova.

**Checklist della consegna.** Ho rispettato formato e tempo? Ho applicato le regole note? Ho distinto fatti mancanti e ipotesi? Ogni azione ha responsabile e termine? Ogni conclusione ha una prova? Ho indicato la successiva verifica? Usa le simulazioni 6, 8 e 10 per esercitare rispettivamente tabella più nota, otto righe e prova integrata.

'''
t=t.replace('## Riferimenti normativi e professionali essenziali',append+'## Riferimenti normativi e professionali essenziali')
save(p,t)
for n in [8]:
 p=next(B.glob(f'{n:02d}-*.md'));t=p.read_text(encoding='utf8');t=t.replace('Alla data di verifica di questo capitolo, 13 agosto 2026, il termine non è ancora scaduto:','Alla data di aggiornamento del 3 ottobre 2026, il termine non è ancora scaduto:').replace(' Il text freeze dovrà verificare gli atti italiani sopravvenuti.',' Lo stato degli atti italiani è distinto dalle scadenze europee, come indicato nel quadro aggiornato di questo nucleo.');p.write_text(t,encoding='utf8')
print('Laboratorio, appendici A–E e note al lettore aggiornati.')
