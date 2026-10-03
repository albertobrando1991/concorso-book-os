from pathlib import Path
import hashlib,shutil,re,json
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
p=Path('wiki/sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24.md');t=p.read_text(encoding='utf8')
t=t.replace('updated_at: 2026-08-23','updated_at: 2026-10-03').replace('review_required: true','review_required: false').replace('D.M. 154/2017, D.P.C.M. 57/2024 e atti MiC','D.Lgs. 42/2004, art. 29; D.P.C.M. 57/2024 e atti MiC')
t+='''
## Verifica selettiva del 3 ottobre 2026 — Codice vigente

Letti integralmente gli articoli 10, 12, 13, 14, 20, 21, 29, 41, 54, 55, 59, 60, 61, 65, 68, 90, 91, 122 e 123 del D.Lgs. 42/2004 tramite i permalink Normattiva puntuali `https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2004-01-22;42~art65!vig=` (sostituire il numero dopo art). Non si attesta il controllo integrale del Codice.

- Art. 10: distinguere soggetti pubblici e persone giuridiche private senza fine di lucro, categorie culturali ex lege del comma 2 e categorie del comma 3 oggetto di dichiarazione. Soglia autore non vivente/oltre settant'anni per comma 1 e comma 3 lettere a/e; non applicarla indiscriminatamente agli archivi pubblici del comma 2. Specifica soglia cinquantennale per comma 3 d-bis.
- Artt. 12–14: tutela interinale per cose con requisiti dell'art. 12; verifica positiva equivale a dichiarazione; negativa esclude il regime culturale, con controllo distinto di altri interessi alla demanialità. Termine verifica 90 giorni e intervento sostitutivo nei successivi 30 secondo commi 10–10-ter. Dichiarazione: avvio del soprintendente, comunicazione, osservazioni per almeno 30 giorni; effetti cautelari tipizzati, dichiarazione ministeriale. Non serve dichiarazione per i beni dell'art. 10, comma 2.
- Artt. 20–21: usi incompatibili o pregiudizievoli vietati. L. 17 marzo 2026, n. 40 ha abrogato art. 21, comma 1, lettera b: lo spostamento segue ora denuncia preventiva e potere di prescrizioni del soprintendente entro 30 giorni; archivi correnti pubblici hanno comunicazione ex comma 3. Rimozione/demolizione, smembramento di collezioni e scarto restano nei rispettivi regimi autorizzatori; opere/lavori ex comma 4 richiedono autorizzazione. Mutamento d'uso comunicato per le finalità dell'art. 20.
- Art. 29: conservazione mediante studio, prevenzione, manutenzione e restauro coordinati e programmati; restauro e manutenzione dei beni mobili e superfici decorate riservati ai restauratori qualificati, ferme le regole professionali per beni architettonici.
- Artt. 54–55: inalienabilità delle categorie indicate, con eccezioni tipizzate anche per trasferimenti fra enti territoriali; alienazione di altri immobili culturali demaniali autorizzabile alle condizioni di legge, senza cessazione della tutela.
- Artt. 59–61: denuncia trasferimenti entro 30 giorni; detenzione da denunciare limitatamente ai mobili. Prelazione su alienazione onerosa/conferimento, non su qualsiasi donazione o successione. Termine ordinario 60 giorni; 180 in caso di denuncia tardiva, omessa o incompleta dalla conoscenza di tutti gli elementi prescritti.
- Artt. 65 e 68: divieti di uscita definitiva, categorie autorizzate e dichiarazioni di non assoggettamento distinti. Nel testo vigente la soglia generale è 50.000 euro, quella dei libri 13.500; categorie senza soglia e archivi/documenti privati richiedono analisi propria. Non proporre esempi al valore esattamente pari alla soglia, poiché il testo usa superiore/inferiore. Attestato di libera circolazione valido cinque anni, rilascio/diniego entro 40 giorni dalla presentazione della cosa. SUE conferma dal maggio 2026 DVAL50_MILA e DVAL13.500_LIBRI: https://sue.cultura.gov.it/SUE/FE/SUE/pageHome.aspx .
- Artt. 41, 122–123: versamento degli archivi statali per affari esauriti da oltre 30 anni, con eccezioni e versamento anticipato tipizzati; scarto autorizzato prima del versamento. Consultabilità ordinaria, limiti 50/40/70 anni secondo categoria documentale; autorizzazione anticipata per studio storico del Ministero dell'interno non libera indiscriminatamente i documenti né equivale a pubblicazione dei dati personali.
- Artt. 90–91: ritrovamento fortuito denunciato entro 24 ore a soprintendente, sindaco o autorità di pubblica sicurezza; conservazione temporanea in sito, rimozione dei mobili solo quando la custodia altrimenti non sia assicurabile. Cose ritrovate nel sottosuolo/fondali appartengono allo Stato secondo il regime demaniale o patrimoniale pertinente.

## Organizzazione e standard — parti effettivamente consultate

MiC, https://cultura.gov.it/dipartimenti e https://cultura.gov.it/organizzazione : assetto D.P.C.M. 57/2024 e D.M. 270/2024, quattro dipartimenti DiAG, DiT, DiVA, DiAC e rispettive direzioni generali. DGA, https://archivi.cultura.gov.it/istituti-archivistici , pagina aggiornata 16 febbraio 2026: Archivi di Stato conservano e tutelano archivi statali; soprintendenze archivistiche e bibliografiche tutelano archivi pubblici non statali, privati dichiarati e beni librari non statali. Evitare trasferimento automatico delle competenze SABAP al settore archivistico o bibliografico.

ICAR: https://icar.cultura.gov.it/standard/standard-internazionali/isad-g e https://icar.cultura.gov.it/standard/standard-internazionali/isaar-cpf . ISAD(G), seconda edizione, traduzione in Rassegna degli Archivi di Stato, https://icar.cultura.gov.it/fileadmin/risorse/docu_standard/RAS_2003_1.pdf : letti i quattro principi nei fogli PDF 85 e 87 (pagine a stampa 87 e 89), non l'intero fascicolo di 430 pagine. Descrizione dal generale al particolare, pertinenza al livello, collegamento gerarchico e non ripetizione; ISAAR(CPF) descrive separatamente enti/persone/famiglie produttori. Un authority record non sostituisce l'inventario dei documenti.

ICDP, Linee guida digitalizzazione, versione 1 giugno 2022: https://docs.italia.it/italia/icdp/icdp-pnd-digitalizzazione-docs/it/v1.0-giugno-2022/index.html . Letti §3.1, §4.1, §4.7 e §9: master e derivati hanno scopi diversi; dati catalografici sono metadati descrittivi; metadati tecnici, strutturali, diritti e conservazione integrano la descrizione. Checksum rileva cambiamenti dei bit, non certifica da solo autenticità storica o correttezza catalografica; controlli durante il progetto e al collaudo. Versione datata esplicitamente, non presentata come norma nuova del 2026.

Biblioteche: riuso della nota consolidata [[sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05]] per REICAT, ISBD, UNIMARC/SBNMARC, authority, soggettazione/classificazione, ILL e DD. Applicazione IR04 con nuovo caso originale.

Università di Bologna, materiale didattico Archeologia dell'architettura: https://site.unibo.it/scuola-superiore-citta-territorio/it/didattica/architettura-e-museografia-per-l-archeologica-di-emergenza/emerafpresentazione.pdf/@@download/file/EMERAFpresentazione.pdf . Consultate pagine PDF 25, 32 e 46–51: US materiale/negativa; rapporti di taglio, riempimento e appoggio; cronologia relativa distinta da datazione assoluta. Non è una procedura di scavo né un manuale integralmente verificato.

Uffizi, scheda Nascita di Venere di Daniela Parenti: https://www.uffizi.it/opere/nascita-di-venere . Scheda e testo letti: Botticelli, circa 1485, tempera su tela, 172,5 × 278,5 cm, inventario 1890 n. 878; approdo di Venere, rimandi classici; committenza medicea probabile, non documentata con certezza dalla sola scheda. Il caso didattico distingue dato catalografico, osservazione formale e ipotesi interpretativa.

Sicurezza: D.Lgs. 81/2008, art. 20 corrente letto integralmente, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81~art20!vig= . Cura della sicurezza secondo formazione, istruzioni e mezzi; segnalazione immediata, intervento urgente entro competenze e possibilità, divieto di manovre estranee o pericolose. Il piano locale assegna gli incarichi agli addetti; il capitolo non inventa soglie di affollamento o procedure universali.

## Collegamenti

[[topics/m-ir04-cultura-fonti-e-profili]]; [[entities/ministero-cultura]]; [[books/moduli/m-ir04-cultura-beni-culturali/index]].

## Evidenze immutabili acquisite

'''
names=[f'dlgs42-art{x}-current.html' for x in [10,12,13,14,20,21,29,41,54,55,59,60,61,65,68,90,91,122,123]]+['dlgs81-art20-current.html','mic-dipartimenti-20261003.html','mic-organizzazione-20261003.html','uffizi-venere-20261003.html','icar-isad.html','icar-isaar.html','isad-g-2003.pdf','mic-sue-20261003.html']
for n in names:
 a=A/n
 if not a.exists() or a.stat().st_size<100:continue
 raw=R/n
 if not raw.exists():shutil.copyfile(a,raw)
 t+=f'- `{raw.as_posix()}` — SHA256 `{hashlib.sha256(raw.read_bytes()).hexdigest()}`.\n'
t+='\nLe fonti web non scaricate restano tracciate con URL, sezioni e data; nessuna acquisizione locale completa è dichiarata per esse. Le verifiche normative sono selettive e non certificano ogni disciplina speciale.\n'
p.write_text(t,encoding='utf8')
print('Source IR04 consolidata')
