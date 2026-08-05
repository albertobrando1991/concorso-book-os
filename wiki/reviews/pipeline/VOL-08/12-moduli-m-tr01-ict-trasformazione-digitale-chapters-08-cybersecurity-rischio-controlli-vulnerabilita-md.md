# Report editoriale — VOL-08, capitolo 8

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi pubblici.
- Pubblico target: candidati a profili ICT, cybersecurity, infrastrutture e trasformazione digitale nella pubblica amministrazione.
- Perimetro di questa revisione: capitolo 8, matrice di copertura M-TR01, piano di completamento, indice del modulo, matrice aggregata VOL-08, rinvio al VOL-01 e fonti consolidate.
- Stato generale in una frase: capitolo autonomo, chiaro e didatticamente completo, da sottoporre a verifiche tecniche e di aggiornamento circoscritte e da riallineare agli apparati globali prima della pubblicazione.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30: coerenza con indice e struttura; progressione; gerarchia; autonomia del capitolo; rapporto con i capitoli adiacenti; terminologia; completezza e accuratezza delle spiegazioni; errori concettuali, normativi o fattuali; esempi, laboratorio, tabelle e apparato delle fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; layout Markdown; leggibilità e qualità complessiva.

Il punto 27, impaginazione, non è applicabile: non è disponibile un PDF o un file impaginato da ispezionare pagina per pagina.

È stato applicato anche il gate di copertura didattica integrale. Il nucleo «Cybersecurity» sviluppa asset e obiettivi di sicurezza, minacce, vulnerabilità, scenari, valutazione e trattamento del rischio, controlli, threat modeling, vulnerability management, secure SDLC, secure coding e software supply chain. Caso, laboratorio, domanda orale, domanda-trappola e quiz applicano concetti già spiegati. Il rinvio al VOL-01, capitolo 10, § 6, è preciso, verificato e limitato ai prerequisiti.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Indice M-TR01 e matrice aggregata VOL-08 | Struttura vs indice | Media | L’indice del modulo è ancora dichiarato `scaffold` e non elenca i capitoli sviluppati; la matrice aggregata VOL-08 mantiene il capitolo 8 su `parziale`, mentre la matrice canonica M-TR01 e il testo dimostrano copertura completa. | Aggiornare indice, stato del modulo e riga aggregata VOL-08 in uno step trasversale, mantenendo la matrice M-TR01 come evidenza canonica. | Proposto |
| E02 | Processo di assessment; risposta alla domanda da commissario | Accuratezza concettuale | Media | La teoria definisce correttamente il rischio inerente prima dei controlli, ma la risposta orale usa la sequenza «valuterei controlli e rischio inerente», che può suggerire l’ordine inverso. | Riformulare in «stimerei il rischio inerente; valuterei poi controlli e rischio residuo», preservando il resto della risposta. | Proposto |
| E03 | NIST CSF 2.0; NIST SSDF; CVSS 4.0; OWASP Top 10:2025 | Aggiornamento tecnico | Media | Framework, versioni e categorie sono coerenti con la source note consolidata, ma sono contenuti mutevoli e la stessa nota richiede verifica al text freeze. | Ricontrollare edizione, terminologia e URL sulle fonti primarie; registrare data e versione della verifica nella source note. | Da verificare |
| E04 | Threat modeling; gestione delle vulnerabilità | Accuratezza tecnica | Media | STRIDE, validazione dei risultati, priorità, remediation, eccezioni e responsible disclosure sono presentati correttamente a livello didattico, ma richiedono sign-off application security e vulnerability management. | Far validare il blocco da security architect e vulnerability manager; documentare eventuali correzioni nella source note prima del text freeze. | Da verificare |
| E05 | Secure SDLC e secure coding | Accuratezza tecnica | Media | Le pratiche di codice sicuro e le distinzioni fra code review, SAST, DAST, SCA e penetration test sono chiare, ma non coprono differenze operative legate a strumenti, linguaggi e ambienti specifici. | Mantenere il livello trasferibile del capitolo e ottenere una review application security; verificare la profondità richiesta dai bandi del campione. | Da verificare |
| E06 | Software supply chain | Apparato delle fonti e accuratezza tecnica | Media | SBOM, provenienza, attestazioni, pipeline e revoca degli artefatti sono ben distinti, ma provenienza e attestazioni non ricevono una definizione autonoma e richiedono validazione specialistica. | Aggiungere in revisione successiva una definizione essenziale di provenienza e attestazione, supportata da fonte primaria, oppure ridurre la promessa nella checklist. | Proposto |
| E07 | Caso guidato: portale per le domande | Chiarezza didattica | Lieve | Il caso applica correttamente scenario, rischio e trattamento, ma non dichiara esplicitamente che probabilità e impatto usano la matrice qualitativa didattica 3×3 definita nel capitolo. | Aggiungere un richiamo breve alla scala didattica adottata, senza trasformare il livello in una misura assoluta. | Proposto |
| E08 | Tabelle, laboratorio e checklist | Layout | Lieve | Il Markdown è leggibile, ma la tabella del laboratorio e gli elenchi tecnici possono diventare densi nel formato KDP. | Verificare nel master impaginato ritorni a capo, corpo minimo, separazione delle righe e assenza di titoli orfani. | Proposto |

Non sono emersi errori oggettivi gravi, contraddizioni interne, nuclei soltanto nominati, rinvii generici o promesse formative non mantenute. Non sono state applicate correzioni dirette al capitolo in questa fase.

## 4. Osservazioni per capitolo

### Capitolo 8 — Cybersecurity operativa: rischio, controlli e vulnerabilità

- Punti di forza: progressione ordinata da asset e scenari alla valutazione, quindi ai controlli, alle vulnerabilità e alla sicurezza del software; definizioni nette di minaccia, vulnerabilità, evento, impatto, rischio, CVE, CWE e CVSS; distinzione corretta fra rischio inerente e residuo; caso, laboratorio e verifiche coerenti con la teoria; confini chiari con cloud e continuità del capitolo 7, IAM e incident response del capitolo 9 e procurement del capitolo 12.
- Criticità: la risposta orale deve rendere inequivoco l’ordine fra rischio inerente, controlli e residuo; provenienza e attestazioni sono soltanto nominate; framework e tassonomie richiedono sign-off specialistico e verifica di versione; gli apparati globali del modulo e del volume non riflettono ancora lo stato reale del capitolo.

## 5. Coerenza globale

- Terminologia: coerente nei concetti centrali. Gli anglicismi tecnici sono definiti o contestualizzati; provenienza e attestazioni richiedono il chiarimento indicato in E06.
- Struttura vs indice: il titolo coincide con l’indice completo VOL-08, ma l’indice operativo M-TR01 è obsoleto e la matrice aggregata non è sincronizzata, come indicato in E01.
- Promesse dell’introduzione mantenute: sì. Ogni competenza dichiarata dispone di teoria, applicazione e verifica.
- Confini: rispettati. Continuità e backup restano nel capitolo 7; IAM, crittografia, logging e risposta agli incidenti nel capitolo 9; requisiti contrattuali e governo dei fornitori nel capitolo 12.
- Rinvio al VOL-01: preciso e verificato. Il capitolo 10, § 6 del volume base tratta effettivamente password, MFA, phishing, malware, antivirus, firewall, backup, aggiornamenti e quadro NIS2 introduttivo.
- Copertura v4: completa per la riga assegnata al capitolo 8. Non è necessario declassare la matrice M-TR01.

## 6. Contenuto da verificare

- Edizioni e terminologia vigenti di NIST CSF, NIST SSDF, CVSS e OWASP Top 10 al text freeze.
- Quadro ACN, NIS2 e procedure nazionali richiamate dalle source note collegate.
- Tassonomie dei controlli, applicazione di STRIDE e profondità richiesta dai bandi target.
- Ciclo di vulnerability management, criteri di eccezione, remediation e responsible disclosure.
- Confini operativi fra code review, SAST, DAST, SCA e penetration test.
- SBOM, provenienza, attestazioni, verifica e revoca degli artefatti nella software supply chain.
- Resa delle tabelle e della checklist nel master KDP.

## 7. Suggerimenti facoltativi (non errori)

- Aggiungere uno schema visuale che colleghi scenario, rischio inerente, controlli, rischio residuo, trattamento ed evidenza.
- Trasformare il laboratorio in una scheda compilabile su due pagine.
- Inserire nel glossario finale le coppie CVE/CWE/CVSS, SAST/DAST/SCA e threat/vulnerability/risk.
- Affiancare alla SBOM un mini-schema «componente → artefatto → provenienza → attestazione → verifica» dopo consolidamento delle fonti.

## 8. Priorità degli interventi

1. Chiudere le verifiche tecniche e di versione indicate in E03-E06.
2. Rendere inequivoca la sequenza del risk assessment secondo E02.
3. Sincronizzare indice e matrice aggregata secondo E01.
4. Rafforzare il caso e il glossario secondo E07 e i suggerimenti facoltativi.
5. Controllare il master KDP secondo E08.

## 9. Giudizio di pubblicabilità

Pubblicabile dopo intervento medio.

Motivazione: il capitolo è strutturalmente completo, mantiene le promesse formative e non presenta errori gravi aperti. I rilievi E02-E06 sono circoscritti ma riguardano ordine concettuale, aggiornamento di framework e validazione specialistica di contenuti centrali; E01 richiede inoltre l’allineamento degli apparati globali prima della consegna.

## 10. Limiti di questa revisione

La revisione riguarda il Markdown, la matrice M-TR01, il piano, gli indici e le note wiki collegate. Non è stato ispezionato un PDF impaginato. Non è stata eseguita una review umana firmata da esperto ACN/NIS2, cyber risk manager, security architect, vulnerability manager, application security engineer o specialista software supply chain. Non sono stati eseguiti penetration test, scanning, prove di remediation o verifiche su una pipeline reale. Le fonti tecniche sono state valutate attraverso le source note consolidate e richiedono conferma al text freeze.