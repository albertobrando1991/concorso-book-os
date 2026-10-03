import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-digitale-esempi-correzioni-2026-10-03.md';u.REF=ref
s='informatica-pa-digitale-competenze-digitali';t=u.read(s)
t=u.replace(t,r'C: \Utenti\Mario\Documenti\relazione.docx',r'C:\Users\Mario\Documents\relazione.docx')
t=u.replace(t,'`C: ` identifica l’unità', '`C:` identifica l’unità')
t=u.replace(t,'`Utenti`, `Mario` e `Documenti` sono cartelle', '`Users`, `Mario` e `Documents` sono cartelle dell’esempio')
t=u.replace(t,'| Termine | Significato | Errore da evitare |', 'Il percorso mostrato è **assoluto**: parte dalla radice dell’unità. `Documenti\\relazione.docx` è invece un esempio di percorso **relativo**, interpretato rispetto alla cartella corrente. I nomi delle cartelle dipendono dall’installazione: un percorso sintatticamente corretto non garantisce che quel file esista.\n\n| Termine | Significato | Errore da evitare |')
t=u.replace(t,'https: //www.comune.example.it/servizi/anagrafe', 'https://www.example.com/servizi/anagrafe')
t=u.replace(t,'In un concorso, se una domanda chiede cosa indica `https`', 'L’indirizzo è un esempio sintattico: non identifica un servizio comunale da usare. In un concorso, se una domanda chiede cosa indica `https`')
t=t.replace('A1: A10','A1:A10')
t=u.replace(t,'### Fogli elettronici: Excel e programmi equivalenti','''### Stampa unione: un modello, più destinatari

La stampa unione combina un documento principale con una tabella di dati. Ogni riga produce un documento personalizzato; i nomi delle colonne diventano campi da inserire nel modello.

| Nome | Cognome | Ora |
|---|---|---|
| Anna | Bianchi | 09:00 |
| Luca | Verdi | 09:30 |

Con il modello `Gentile «Nome» «Cognome», la convocazione è alle «Ora».`, il primo documento sarà: “Gentile Anna Bianchi, la convocazione è alle 09:00.” Il secondo riporterà Luca Verdi e 09:30. Prepara il modello, collega l’elenco, inserisci i campi, controlla l’anteprima per ciascun record e completa l’unione. Non basta digitare manualmente i segnaposto: il programma deve riconoscerli come campi collegati all’origine dati.

**Errore tipico:** ordinare una sola colonna separandola dalle altre, associando nome e orario di persone diverse. Mantieni integre le righe e controlla destinatari, valori e risultato prima di stampare o inviare.

### Fogli elettronici: Excel e programmi equivalenti''')
t=u.replace(t,'### Presentazioni: PowerPoint e programmi equivalenti','''### Laboratorio: formule e riferimenti

Inserisci 10 in B2, 20 in B3 e 30 in B4; in E1 inserisci `10%`. In C2 scrivi `=B2*$E$1` e copia fino a C4: ottieni **1, 2, 3**. Il riferimento B2 diventa B3 e B4; `$E$1` resta fisso. Se scrivessi `=B2*E1`, la copia verso il basso leggerebbe E2 ed E3, che nell’esempio sono vuote: il risultato non rappresenterebbe più il 10%.

Un riferimento **misto** blocca una sola coordinata: `$B2` blocca la colonna B, `B$2` blocca la riga 2. Copiando da C2 a D3, `=B2` diventa `=C3`, `=$B2` diventa `=$B3`, `=B$2` diventa `=C$2`, `=$B$2` resta invariato.

Con i dati di B2:B4, le funzioni nella versione italiana restituiscono:

| Formula | Risultato | Funzione |
|---|---:|---|
| `=SOMMA(B2:B4)` | 60 | Totale |
| `=MEDIA(B2:B4)` | 20 | Media aritmetica |
| `=MIN(B2:B4)` | 10 | Valore minimo |
| `=MAX(B2:B4)` | 30 | Valore massimo |
| `=CONTA.NUMERI(B2:B4)` | 3 | Celle numeriche |
| `=SE(B2>=20;"Sì";"No")` | No | Scelta in base a una condizione |

Nomi delle funzioni e separatori dipendono dalla lingua e dalle impostazioni del programma; qui si usano nomi italiani e punto e virgola fra gli argomenti. Un filtro mostra le righe che soddisfano un criterio senza cancellare le altre; un ordinamento ne cambia la sequenza. Quando ordini una tabella, includi tutte le colonne dei record.

**Verifica:** copiando la formula condizionale da C2 a C3, quale cella viene confrontata con 20 e quale risultato si ottiene? **Soluzione:** B3, perché il riferimento è relativo; 20 è maggiore o uguale a 20, quindi il risultato è “Sì”.

### Presentazioni: PowerPoint e programmi equivalenti''')
t=u.replace(t,'## 8. Programmazione, linguaggi, HTML, XML e algoritmi','''### Chiave esterna, collegamento e ordinamento

Una **chiave esterna** è un campo, o insieme di campi, vincolato a valori presenti in una chiave della tabella collegata. Mantiene l’integrità referenziale: per esempio impedisce di assegnare un dipendente a un ufficio inesistente. Non è necessariamente univoca: più dipendenti possono appartenere allo stesso ufficio.

Considera queste due tabelle fittizie. `IdUfficio` è chiave primaria di Uffici; in Dipendenti è chiave esterna. `IdDipendente` è la chiave primaria di Dipendenti.

| Uffici.IdUfficio | NomeUfficio |
|---|---|
| 10 | Anagrafe |
| 20 | Tributi |

| IdDipendente | Cognome | IdUfficio |
|---|---|---|
| 1 | Verdi | 10 |
| 2 | Bianchi | 10 |
| 3 | Neri | 20 |

La seguente query collega le righe corrispondenti, seleziona Anagrafe e ordina i cognomi:

```sql
SELECT d.Cognome, u.NomeUfficio
FROM Dipendenti AS d
JOIN Uffici AS u
  ON d.IdUfficio = u.IdUfficio
WHERE u.NomeUfficio = 'Anagrafe'
ORDER BY d.Cognome ASC;
```

`JOIN ... ON` combina i dati usando la condizione indicata; `d` e `u` sono abbreviazioni delle tabelle. `WHERE` filtra, `ORDER BY` ordina: `ASC` crescente, `DESC` decrescente. Il risultato è **Bianchi — Anagrafe**, poi **Verdi — Anagrafe**. Senza `ORDER BY` non si può presumere l’ordine dei risultati. Il collegamento tramite JOIN e il vincolo di chiave esterna hanno funzioni diverse: la query può essere scritta anche senza un vincolo dichiarato, ma questo non rende automaticamente coerenti i dati.

**Verifica:** è ammesso inserire nella tabella Dipendenti un nuovo record con IdUfficio 99 se il vincolo è attivo e Uffici contiene solo 10 e 20? **Soluzione:** no, perché manca la riga richiamata; prima occorre una scelta di dati coerente, non disattivare il controllo per aggirare l’errore. Cambiando `ASC` in `DESC`, i due risultati del caso diventano Verdi e Bianchi.

## 8. Programmazione, linguaggi, HTML, XML e algoritmi''')
t=u.replace(t,'Nei concorsi va distinto da una semplice scansione, da una copia informale e da un file privo di requisiti.', 'Può nascere digitale oppure derivare da un originale analogico. La scansione di un atto cartaceo può essere una copia per immagine su supporto informatico: rientra nella categoria documentale, ma non equivale automaticamente a un originale sottoscritto digitalmente. Validità, conformità della copia ed efficacia probatoria richiedono una valutazione distinta secondo gli artt. 20–22 del CAD.')
t=u.replace(t,'Il **domicilio digitale** è l’indirizzo elettronico eletto presso un servizio qualificato, utilizzabile per comunicazioni aventi valore legale secondo la disciplina applicabile.', 'Il **domicilio digitale** è eletto presso una PEC oppure presso un servizio elettronico di recapito certificato qualificato ai sensi di eIDAS (art. 1 CAD). Un indirizzo email ordinario non costituisce domicilio digitale.')
a=t.index('Caratteristiche essenziali:',t.index('### Open data'));b=t.index('\n## 17. Cloud',a)
t=t[:a]+'''L’art. 1, comma 1, lettera l-ter), CAD richiede congiuntamente:

- riuso da parte di chiunque, anche commerciale e in forma disaggregata, consentito da licenza o norma;
- accessibilità mediante tecnologie informatiche, formato aperto, elaborabilità automatica e metadati;
- gratuità oppure costi marginali di riproduzione/divulgazione, salve le eccezioni del d.lgs. 36/2006.

Aggiornamento e qualità rendono il dato utile; privacy, segreti e sicurezza possono limitarne la pubblicazione. Una tabella solo fotografata in un PDF non soddisfa, per il semplice fatto di essere online, l’elaborabilità automatica richiesta. Il formato aperto è necessario ma non basta: occorre verificare anche le altre condizioni.\n''' +t[b:]
u.save(s,t,['V01-25','V01-26','V01-27','V01-28','V01-29'],ref)

s='appendice-a-glossario-essenziale-pa';t=u.read(s)
t=u.replace(t,'| Documento informatico | Documento formato, gestito o conservato in formato digitale secondo regole tecniche e giuridiche. | Non è una semplice scansione senza regole. |','| Documento informatico | Documento elettronico che rappresenta atti, fatti o dati giuridicamente rilevanti. | Comprende anche copie informatiche: natura del documento ed efficacia probatoria sono questioni distinte. |')
t=u.replace(t,'| Domicilio digitale | Indirizzo elettronico usato per comunicazioni aventi valore secondo la disciplina digitale. | Non coincide sempre con una casella email ordinaria. |','| Domicilio digitale | Indirizzo eletto presso PEC o recapito certificato qualificato per comunicazioni legali. | L’email ordinaria non è domicilio digitale. |')
t=u.replace(t,'| Open data | Dati pubblici resi disponibili in formato aperto e riutilizzabile, quando possibile. | Non ogni dato pubblicato è automaticamente open data. |','| Open data | Dati con riuso consentito, formato aperto, elaborabilità automatica, metadati e condizioni economiche previste dal CAD. | I requisiti sono congiunti; pubblicare un file online non basta. |')
t=u.replace(t,'Supporta e sorveglia il rispetto della disciplina privacy; non decide sempre finalità e mezzi.', 'Informa, consiglia e sorveglia; finalità e mezzi competono al titolare. Altri incarichi del RPD non devono creare conflitto di interessi.')
t=u.replace(t,'| Performance | Misurazione e valutazione di risultati, servizi, organizzazione e contributo individuale. |', '| Performance | Prestazione e risultati dell’organizzazione o del singolo rispetto agli obiettivi. |')
u.save(s,t,['V01-26','V01-27','V01-28','V01-45','V01-47'],ref)
s='appendice-b-100-parole-chiave-concorsi';t=u.read(s)
t=u.replace(t,'| 42 | Documento informatico | Documento formato e gestito digitalmente secondo regole tecniche e giuridiche. | “Il documento informatico non è una semplice scansione.” |','| 42 | Documento informatico | Rappresentazione elettronica di atti, fatti o dati giuridicamente rilevanti. | “Anche una copia da carta può essere informatica; la sua efficacia va verificata.” |')
t=u.replace(t,'Indirizzo elettronico eletto per comunicazioni aventi valore legale.', 'Indirizzo eletto presso PEC o recapito certificato qualificato.')
t=u.replace(t,'Informazioni riferite a una persona identificata o identificabile.', 'Informazioni relative a una persona fisica identificata o identificabile.')
t=u.replace(t,'| 37 | Performance | Misurazione di risultati organizzativi e individuali. | “La performance serve a valutare se l’azione pubblica produce risultati.” |','| 37 | Performance | Prestazione e risultati organizzativi o individuali rispetto agli obiettivi. | “La misurazione e la valutazione della performance verificano i risultati raggiunti.” |')
t=t.replace('“La chiarezza facilita','“La chiarezza facilita')
u.save(s,t,['V01-26','V01-27','V01-47'],ref)
for topic in ['pa-digitale','informatica','competenze-digitali']:
 p=Path('wiki/topics')/(topic+'.md')
 with p.open('a',encoding='utf8') as out:out.write('\n\n## Correzioni consolidate del 3 ottobre 2026\n\n[[sources/vol-01-digitale-esempi-correzioni-2026-10-03]] corregge la tassonomia documentale, domicilio e open data; aggiunge esempi originali Office/SQL nel capitolo 10 e coordina i glossari.\n')
u.record()
