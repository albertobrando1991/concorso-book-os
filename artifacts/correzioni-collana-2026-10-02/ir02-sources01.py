from pathlib import Path
import re,shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
names=['l240-art2-current.html','dm270-art3-current.html','dm270-art5-current.html','dm270-art7-current.html','dpr132-art4-current.html','dpr132-art6-current.html','dpr132-art7-current.html','dpr212-art3-current.html','dpr212-art6-current.html','dpr212-art8-current.html','anvur-ava3-requisiti.pdf','ergo-bando-2026-2027.pdf']
for name in names:
 if not (R/name).exists():shutil.copyfile(A/name,R/name)
p=Path('wiki/sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24.md');t=p.read_text();t+='''
## Riscontri puntuali del 3 ottobre 2026

Letti integralmente i consolidati L.240/2010 art.2, D.M.270/2004 artt.3/5/7, DPR132/2003 artt.4/6/7, DPR212/2005 artt.3/6/8. ANVUR AVA3, requisiti con note 13 febbraio2023, pagine19–20 (ambitoC) lette per ruoli, monitoraggio e documenti. ER.GO2026/2027 letto selettivamente, pagine13–14,25–26,35 e56; non attestata lettura di tutte le338pagine.

### Università

La L.240 art.2 si riferisce alle università statali: rettore (rappresentanza, indirizzo e proposta), senato (didattica/ricerca e pareri), CdA (strategia, sostenibilità e approvazione bilancio), direttore generale (gestione), revisori (controllo contabile), nucleo di valutazione (qualità/efficacia). Rettore6anni non rinnovabili; senato massimo35, almeno2/3 docenti e almeno1/3 di questi direttori di dipartimento; CdA massimo11, con almeno3esterni se11,2semeno. Dipartimenti integrano ricerca e didattica; CPDS monitorano offerta e servizi. Non trasformare statuti locali in deroga libera ai vincoli di legge.

D.M.270:1CFU=25ore complessive, variazioni ministeriali entro20%;60CFU annui medi; laurea180, magistrale120, masteralmeno60; masterI/II successivi rispettivamente a laurea/magistrale, non sinonimo di LM. I crediti misurano carico, non voto; acquisizione con verifica; riconoscimento alla struttura ricevente con criteri predeterminati. Cicli unici seguono ordinamenti pertinenti, senza sommare meccanicamente180+120 per ogni corso.

AVA3: PQA supporta metodologicamente e organizza processi; NdV valuta sistema ed efficacia; CPDS monitorano e formulano indicazioni; CdS/dipartimenti svolgono autovalutazione e miglioramento. Scheda di Monitoraggio Annuale, Riesame ciclico, SUA-CdS, relazioni CPDS e opinioni studenti sono evidenze differenti, non documenti intercambiabili. Accreditamento ministeriale e valutazione ANVUR distinti dalla gestione interna.

Esempio locale di carriera verificato sul portale UniBo: rinuncia formale irrevocabile chiude la carriera; interruzione e sospensione non equivalgono, la sospensione richiede le condizioni ammesse; decadenza è perdita della possibilità di proseguire secondo termini/regole applicabili. Nel caso UniBo gli anni di sospensione non contano per la decadenza, quelli di interruzione sì. Le soglie temporali non vengono universalizzate. URL: https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/lasciare-e-riprendere-gli-studi/lasciare-riprendere-gli-studi ; https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/lasciare-e-riprendere-gli-studi/decadenza-dallo-status-di-studente .

ER.GO, bando benefici2026/2027, art.7 p.35: borsa ISEE25.000 e ISPE50.000; vanno soddisfatti entrambi, oltre alle altre condizioni. Un solo indicatore favorevole non basta. L’esempio numerico nel capitolo è originale e isolato al requisito economico; non dichiara assegnata la borsa. Fonte https://www.er-go.it/cosa-fare-per/bandi-di-concorso/leggi-il-bando/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf/@@display-file/file/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf .

### AFAM

Il sistema comprende istituzioni statali e istituzioni non statali autorizzate/accreditate; formazione terziaria artistica, musicale e coreutica distinta ma parallela all’università. DPR132: presidente, direttore, CdA, consiglio accademico, revisori, nucleo, collegio professori, consulta studenti. Direttore responsabile didattico/scientifico/artistico; CdA5componenti ordinari, possibili2aggiuntivi nei casi previsti, approva bilancio e gestione. Non assimilare direttore AFAM a direttore generale universitario.

DPR212 vigente: diplomaI almeno180CFA, II almeno120, IIciclounico almeno300; master/perfezionamento almeno60; CFA25ore (variazioni ministeriali20%),60annui tempo pieno,36tempo parziale. Il titolo del terzo ciclo è ora diploma accademico di dottorato di ricerca, equiparato al dottorato universitario. La norma include istituzioni non statali accreditate; non dichiarare ogni istituzione AFAM ente pubblico. I dettagli di ammissione, scuole e titoli seguono i decreti pertinenti, senza generalizzazione da un conservatorio.

URL primari dei consolidati: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2010-12-30;240~art2!vig= ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto:2004-10-22;270~art5!vig= ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2003-02-28;132~art4!vig= ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2005-07-08;212~art3!vig= . ANVUR: https://www.anvur.it/sites/default/files/2025-02/AVA3_Requisiti-con-NOTE_2023_02_13.pdf .

Copie raw e hash:
'''
for name in names:t+=f'- `raw/correzioni-collana-2026-10-02/{name}` SHA256 {hashlib.sha256((R/name).read_bytes()).hexdigest()}.\n'
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8');print('IR02 fonti01 consolidate')
