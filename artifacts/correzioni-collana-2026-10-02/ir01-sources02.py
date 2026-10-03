from pathlib import Path
import json,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/sources/fonti-ufficiali-m-ir01-scuola-2026-07-24.md');t=p.read_text(encoding='utf8');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
t+='''
## Consolidamento sostanziale per le correzioni del 3 ottobre 2026

### Organi e autonomia

Letti integralmente i consolidati Normattiva del D.Lgs. 297/1994 artt. 5, 7, 8, 10 e 37 e D.P.R. 275/1999 art. 3. I richiami storici del testo unico devono essere coordinati con la disciplina successiva: per esempio, predisposizione contabile secondo D.I. 129/2018 e collaboratori del DS secondo art. 25 D.Lgs. 165/2001, non con una riproduzione acritica delle formule del 1994.

Consigli di classe/interclasse/intersezione: docenti e rappresentanze distinte per grado; coordinamento didattico e valutazione nelle composizioni riservate ai docenti. Collegio: docenti in servizio e DS presidente, competenze didattiche, libri di testo e proposte. Consiglio d’istituto: 14 componenti fino a 500 alunni, 19 oltre; rappresentanza studenti nella secondaria superiore in sostituzione di metà di quella genitoriale; presidenza fra i genitori. Giunta: DS, DSGA, docente, ATA, due genitori, di cui uno sostituito da studente nella secondaria superiore. Quorum art. 37 e regole speciali da distinguere.

PTOF triennale e rivedibile annualmente: DS definisce indirizzi, collegio elabora, consiglio approva. SNV D.P.R. 80/2013: autovalutazione, valutazione esterna, miglioramento, rendicontazione. Fonti INVALSI lette: https://www.invalsi.it/valutazione-scuole/valutazione-esterna-scuole/ e https://www.invalsi.it/valutazione-scuole/autovalutazione-scuole/formazione-rav-snv-2025-28/ . Il ciclo corrente richiamato da INVALSI è 2025–2028; non confondere rendicontazione sociale con conto consuntivo contabile.

Quadro dei cicli: primaria cinque anni e secondaria primo grado tre (MIM: https://www.mim.gov.it/ricerca-tag/-/asset_publisher/oHKi7zkjcLkW/content/scuola-secondaria-di-primo-grado). Secondo ciclo: licei, tecnici, professionali e IeFP regionale; descrivere l’ordinario quinquennale senza negare i percorsi quadriennali autorizzati e la filiera 4+2. Non trasferire termini annuali di iscrizione da un anno all’altro.

### Personale e relazioni sindacali

CCNL Comparto Istruzione e ricerca 2022–2024 sottoscritto definitivamente il 23 dicembre 2025: fonte ARAN https://www.aranagenzia.it/wp-content/uploads/2025/12/2025_12_23_CCNL_CIR_2022-2024.pdf ; acquisizione raw `aran-ccnl-istruzione-ricerca-2022-2024.pdf`. Letti art. 1, comma 13 (clausola di continuità delle disposizioni compatibili non sostituite), artt. 5–6 e art. 11 per le relazioni scolastiche. Non presentare il rinnovo come solo economico: l’art. 11 sostituisce il precedente art. 30.

Informazione preventiva scritta; confronto con dialogo ed esito di sintesi, senza accordo necessario; contrattazione sulle sole materie demandate. Art. 11, comma 9, lett. b: confronto su articolazione orario e criteri di assegnazione alle sedi; comma 4, lett. c: contrattazione, fra l’altro, ripartizione risorse/compensi e criteri flessibilità in entrata/uscita ATA. Non equiparare queste due materie solo perché entrambe toccano l’orario.

Piano attività ATA: art. 53, comma 1, CCNL Scuola 29 novembre 2007, letto su ARAN, con raccordo alla vigente disciplina delle relazioni sindacali: DSGA formula la proposta sentito il personale ATA; DS verifica coerenza con offerta formativa ed espleta le relazioni previste, quindi adotta; attuazione puntuale affidata al DSGA. Fonte https://www.aranagenzia.it/documento_pubblico/contratto-collettivo-nazionale-di-lavoro-relativo-al-personale-del-comparto-scuola-per-il-quadriennio-normativo-2006-2009-e-biennio-economico-2006-2007/ . Art. 55 CCNL 18 gennaio 2024 e allegati: DSGA incarico nell’Area Funzionari ed EQ, autonomia operativa entro direttive e obiettivi, sovrintendenza/coordinamento ATA. Nuove aree Collaboratori, Operatori, Assistenti, Funzionari/EQ da distinguere dai singoli profili e dai requisiti del bando.

### Contabilità e inventario

Letti D.I. 129/2018 artt. 12, 13, 15, 16, 17, 30, 31 e 33 consolidati su Normattiva; artt. 5 e 23 letti sulla Gazzetta ufficiale, testo originario. Art. 5: DS predispone con collaborazione DSGA economico-finanziaria, giunta propone entro 30 novembre, consiglio approva entro 31 dicembre; scadenze ordinarie, eventuali differimenti annuali da distinguere. Art. 23: DSGA predispone entro 15 marzo, DS invia ai revisori, parere entro 15 aprile, approvazione consiglio entro 30 aprile.

Accertamento entrata DSGA, riscossione cassiere con reversale; impegno DS e registrazione DSGA, liquidazione DSGA, mandato DS/DSGA, pagamento cassiere. Residui: accertati non riscossi e impegnati non pagati. Il DSGA è consegnatario; inventario distingue proprietà e beni di terzi. Ricognizione almeno quinquennale, rinnovo e rivalutazione almeno decennali. Scarico art. 33 con provvedimento DS e motivazione, denuncia/verbale/relazione secondo causa; non mera cancellazione operativa.

### DS e sicurezza

Art. 25 D.Lgs. 165/2001 letto nel consolidato: gestione unitaria, legale rappresentanza, risorse e risultati, poteri di direzione/coordinamento e relazioni sindacali nel rispetto degli organi collegiali; DSGA con autonomia operativa e direttive di massima. Non riproporre il vecchio meccanismo valutativo come attuale.

Art. 18 D.Lgs. 81/2008, commi 3.1–3.3, letti nel consolidato: responsabilità edilizie dell’amministrazione tenuta alla fornitura/manutenzione; richiesta tempestiva **insieme** alle misure gestionali di competenza condiziona l’esenzione del DS. Pericolo grave e immediato: interdizione/evacuazione e comunicazioni previste, senza attendere istruttoria ordinaria. Rischi strutturali di competenza dell’ente, documento di valutazione congiunta e disciplina attuativa: termine del decreto prorogato al 31 dicembre 2026 dalla L. 26/2026. Il capitolo non deve simulare una procedura attuativa non verificata.

### Limiti del riscontro

Sono verificati gli articoli e i passaggi elencati, non l’intero ordinamento scolastico né tutti gli atti annuali. Le nuove applicazioni numeriche e i casi sono originali e dichiaratamente didattici. Per inclusione e programmi docenti permane la distinta fonte specialistica da completare nei capitoli 11–13.

### Acquisizioni consolidate e tracciabilità

'''
for item in json.loads((A/'ir-sa-norms-fetch.json').read_text(encoding='utf8')):
 name=Path(item['file']).name
 if name.startswith(('dlgs118','dlgs101')):continue
 raw=Path('wiki/raw/correzioni-collana-2026-10-02',name);data=Path(item['file']).read_bytes()
 if not raw.exists():raw.write_bytes(data)
 t+='- '+item['url']+' — raw `'+name+'`, SHA256 `'+hashlib.sha256(data).hexdigest()+'`.\n'
p.write_text(t,encoding='utf8');print('Fonte IR01 consolidata prima della scrittura dei capitoli 02–10.')
