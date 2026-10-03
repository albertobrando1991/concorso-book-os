from pathlib import Path
import re,shutil
p=Path('wiki/sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04.md');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-source-sp04.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('26 aprile 2026, ore 12.00','27 aprile 2026, ore 12.00')
t=t.replace("dal testo dell'art. 4 comma 3","dal testo dell’art. 2, comma 3")
t=t.replace('Quattro prove scritte portate a termine senza superarle **precludono definitivamente** l\'accesso. È un vincolo che nessun altro concorso del volume presenta in forma così netta e che cambia la natura del piano: ogni tentativo va speso, non provato.','Quattro serie complete di prove scritte portate a termine senza superarle impediscono una nuova ammissione secondo l’art. 2, comma 3, del bando 2026. Non contano automaticamente quattro domande, quattro preselezioni o quattro prove singole; chi supera gli scritti e non supera l’orale non ricade per quel solo esito nella fattispecie. Altri concorsi del volume hanno propri limiti, diversi e da non sovrapporre.')
t=t.replace('percorsi di formazione presso la **Scuola superiore dell\'amministrazione dell\'interno** di durata **minima di due anni**, con tirocinio operativo.','percorso di formazione iniziale **biennale**, con tirocinio operativo. Il riferimento storico alla Scuola superiore dell’amministrazione dell’interno deve essere coordinato con l’art. 21 del d.l. 90/2014, convertito dalla legge 114/2014: la SSAI è soppressa e le sue funzioni di reclutamento e formazione sono attribuite alla SNA.')
t=t.replace('**La prova c) non è una prova di lingua nel senso ordinario:** è una traduzione con vocabolario, in quattro ore. Chiede comprensione scritta e resa in italiano, non conversazione. Chi prepara la lingua come si prepara un esame orale sta allenando la cosa sbagliata.','**La prova c) ha una forma specifica:** traduzione di un testo oppure risposta a un quesito nella lingua prescelta, con vocabolario e quattro ore. Va allenata la forma effettivamente indicata, senza ridurla necessariamente alla traduzione verso l’italiano. La conversazione orale richiede un allenamento distinto.')
t+='''

## Riscontri e correzioni del 3 ottobre 2026

### Originali e perimetro della rilettura

Riletti nel PDF locale prefettizio pp. 3–7 e 9–13 gli artt. 1–3 e 6–14 pertinenti a requisiti, domande, prove, soglie e punteggi. Riletti nel PDF MAECI pp. 5–14 gli artt. 2–14 per requisiti, tentativi, scelte linguistiche, prove, titoli e graduatoria. Controllato anche il bando MAECI online ufficiale. Le clausole sono trattate come regole delle rispettive tornate; i piani non ne presumono la permanenza in procedure future.

### Prefettizia

- Art. 2: 35 anni, superamento alla mezzanotte del compleanno. Elevazione di un anno per figlio vivente; un candidato già oltre il compleanno dei 36 alla scadenza non rientra grazie al solo figlio. Eventuali benefici ulteriori vanno dichiarati nel caso, non inventati nella soluzione. Titoli specifici elencati: l’espressione generica “laurea affine” non basta.
- Art. 9: risposta/omissione vanno confrontate per classe di difficoltà. Con probabilità soggettiva p di correttezza, rispondere supera il valore dell’omissione se p > 2/9 nei facili, p > 1/5 nei medi, p > 4/23 nei difficili. Le formule sono rispettivamente 2,7p − 1,6 > −1; 2,5p − 1,2 > −0,7; 2,3p − 0,6 > −0,2. A parità il valore atteso è uguale. Nessuna garanzia di esito; bisogna conoscere la classe e considerare tempo e incertezza della propria stima.
- Art. 10: cinque scritti digitali; tre da otto ore, caso da sette, lingua da quattro. Totale 35 ore. La prova linguistica può essere traduzione o risposta a quesito: non va ridotta soltanto alla resa in italiano.
- Artt. 12–14: media scritti almeno 70 e ogni prova almeno 60; orale almeno 60. Voto complessivo = media scritti + orale + incrementi spettanti: specializzazione biennale 2,50; dottorato 3; facoltativa linguistica fino a 1,50 se idonea. Titoli dichiarati in domanda alle condizioni dell’art. 3. Preferenze a parità e riserve sono distinte dagli incrementi di punteggio.
- [D.l. 90/2014, art. 21](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-06-24;90~art21!vig=), acquisito in `wiki/raw/correzioni-collana-2026-10-02/dl90-art21-scuole-20261003.html`: testo completo letto. La SSAI è soppressa; le funzioni passano alla SNA. Riscontro istituzionale ulteriore: [SNA, atti generali](https://sna.gov.it/home/amministrazione-trasparente/disposizioni-generali/atti-generali/). Il testo storico del d.lgs. 139/2000 non prova l’esistenza attuale della scuola soppressa.

### Diplomatica

- Art. 2, comma 1, lettera c: laurea magistrale o equiparata, senza elenco ristretto di classi nel bando 2026. Per titoli esteri si distingue equipollenza riconosciuta dall’ateneo ed equivalenza ex art. 38 d.lgs. 165/2001, con ammissione con riserva e onere dei vincitori entro quindici giorni dalla graduatoria secondo la clausola. Non si trasferiscono le classi del bando prefettizio.
- Art. 2, comma 3: quattro serie di scritti terminate senza superamento. Art. 4 non contiene la clausola: il rinvio precedente era errato.
- Art. 3: quaranta giorni dalla pubblicazione; scadenza festiva prorogata al primo giorno non festivo. La [pagina ufficiale MAECI concorsi](https://www.esteri.it/it/trasparenza_comunicazioni_legali/bandi_di_concorso/concorsi/) indica **27 aprile 2026 ore 12.00**, non 26 aprile, che era domenica. È un’ulteriore correzione emersa oltre all’audit iniziale.
- Artt. 7 e 9: economia comprende politica economica, economia internazionale e finanziaria e commercio internazionale. Scritti digitali senza dizionario; inglese almeno 70, altri almeno 60, media dei cinque almeno 70. Non confondere laurea ammessa con programma già coperto dalla laurea.
- Art. 11: una materia orale facoltativa scelta in domanda fra i cinque ambiti; punteggio fino a 2, sufficienza almeno 1,2; aggiunta soltanto se orale obbligatorio superato.
- Art. 12: lingue facoltative dichiarate in domanda, escluse inglese e seconda obbligatoria. Tedesco, russo, turco, arabo, hindi, cinese, giapponese: fino a 4 per lingua, sufficienza 2. Altre: fino a 2, sufficienza 1. Massimo complessivo 7 senza lingue del primo gruppo sufficienti, poi 8/9/10/11 con una/due/tre/quattro o più. Il tedesco scelto come seconda obbligatoria non si riconta come facoltativo.
- Artt. 8 e 13: media dei cinque scritti + orale + bonus facoltativi + titoli. Titoli massimo 6, distinti in massimo 3 per titoli formativi/abilitazioni e massimo 3 per attività internazionale ammessa. Dottorato massimo 2, specializzazione 1,2, abilitazione 1,2, master II livello 1, master I livello 0,5, secondo coerenza e limiti della commissione. Preferenze e riserve non sono punti extra indeterminati.

### Limiti

La precedente indicazione “quesiti non pubblicati al 13 agosto” è un dato storico della fonte, non una verifica aggiornata al 3 ottobre. Il libro insegna il protocollo condizionato alla pubblicazione effettiva; nessun file di banca è inventato o presentato come acquisito. Il corpus normativo storico resta distinto dai riscontri sopra indicati.
'''
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);t=re.sub(r'^checked_at:.*$','checked_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8');print('SP04 source corrected')
