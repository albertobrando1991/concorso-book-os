---
id: source-cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie
type: source
title: "Rischio cyber, vulnerabilità, sviluppo sicuro e supply chain — fonti primarie"
status: processed
domain: "cybersecurity specialistica"
topics: ["cybersecurity", "risk assessment", "vulnerabilità", "secure software", "software supply chain"]
entities: ["NIST", "OWASP", "CVE", "CWE", "FIRST", "CISA"]
source_refs: ["sources/sicurezza-informatica-privacy-nis2-pa", "sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.92
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "cyber-risk", "vulnerability", "secure-software", "supply-chain"]
source_type: official_frameworks_standards_and_documentation
source_url: "https://www.nist.gov/cyberframework"
source_date: 2026-07-29
authority_level: alta
---

# Rischio cyber, vulnerabilità, sviluppo sicuro e supply chain — fonti primarie

## Uso

Nota consolidata per il capitolo 8 di VOL-08. Sostiene il linguaggio del rischio, le funzioni di governo della cybersecurity, il ciclo di gestione delle vulnerabilità, lo sviluppo sicuro e la trasparenza della software supply chain. Le fonti internazionali sono riferimenti tecnici: non creano da sole obblighi per la PA italiana.

## Fonti primarie

- **NIST Cybersecurity Framework 2.0**, <https://www.nist.gov/cyberframework>. Organizza gli outcome nelle funzioni Govern, Identify, Protect, Detect, Respond e Recover; gli outcome non costituiscono una checklist prescrittiva.
- **NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments**, <https://csrc.nist.gov/pubs/sp/800/30/r1/final>. Guida la preparazione, conduzione e manutenzione del risk assessment.
- **NIST SP 800-218 — Secure Software Development Framework 1.1**, <https://csrc.nist.gov/pubs/sp/800/218/final>. Integra pratiche di sicurezza nel ciclo di sviluppo per ridurre vulnerabilità, impatto e ricorrenza delle cause.
- **OWASP Top 10:2025**, <https://owasp.org/Top10/2025/>. Documento di awareness sui rischi delle applicazioni web; non è una certificazione né una lista esaustiva.
- **CVE Program**, <https://www.cve.org/>. Identifica, definisce e cataloga vulnerabilità pubblicamente note mediante record e identificativi comuni.
- **CWE — Common Weakness Enumeration**, <https://cwe.mitre.org/>. Elenca debolezze software e hardware che possono condurre a vulnerabilità.
- **CVSS v4.0 Specification**, FIRST, <https://www.first.org/cvss/specification-document>. Framework aperto per comunicare caratteristiche e gravità delle vulnerabilità mediante metriche Base, Threat, Environmental e Supplemental.
- **CISA, SBOM FAQ e risorse Software Bill of Materials**, <https://www.cisa.gov/sbom>. Definisce la SBOM come record formale dei componenti software e delle relazioni di supply chain.
- **CISA, Securing the Software Supply Chain: Recommended Practices for SBOM Consumption**, <https://www.cisa.gov/sites/default/files/2024-08/SECURING_THE_SOFTWARE_SUPPLY_CHAIN_RECOMMENDED_PRACTICES_FOR_SOFTWARE_BILL_OF_MATERIALS_CONSUMPTION-508.pdf>. Collega trasparenza delle dipendenze e gestione del rischio.

## Decisioni editoriali

- Distinguere asset, minaccia, vulnerabilità, evento, impatto e rischio.
- Presentare la risk matrix come strumento di priorità basato su scale dichiarate, non come misurazione assoluta.
- Distinguere rischio inerente e residuo e associare ogni trattamento a responsabile, scadenza ed evidenza.
- Usare il CSF 2.0 come mappa di outcome, senza convertirlo in sequenza rigida.
- Prioritizzare le vulnerabilità con il contesto: CVSS comunica gravità, ma non sostituisce esposizione, sfruttabilità, criticità dell’asset e controlli.
- Distinguere CVE, specifica vulnerabilità; CWE, classe di debolezza; CVSS, sistema di scoring.
- Integrare sicurezza lungo tutto il ciclo di sviluppo.
- Trattare OWASP Top 10 come documento di awareness.
- Presentare la SBOM come inventario: migliora visibilità ma non dimostra da sola sicurezza o assenza di vulnerabilità.

## Limiti e review

- Scale e formule del rischio variano fra metodi: il capitolo usa una matrice didattica dichiarata, non una tassonomia obbligatoria.
- Le categorie OWASP cambiano nel tempo; verificare l’edizione vigente al text freeze.
- CVSS 4.0 è la specifica corrente consultata, ma molti record e strumenti possono esporre versioni precedenti.
- Threat modeling, controlli compensativi, SAST/DAST e penetration test richiedono review application security.
- Quadro ACN e NIS2, procedure e termini restano da verificare su fonti ufficiali italiane.

## Collegamenti

- [[sources/sicurezza-informatica-privacy-nis2-pa]]
- [[topics/sicurezza-informatica]]
- [[entities/agenzia-cybersicurezza-nazionale]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/08-cybersecurity-rischio-controlli-vulnerabilita]]
