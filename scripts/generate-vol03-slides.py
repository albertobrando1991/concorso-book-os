"""Genera i deck HTML VOL-03 dai capitoli wiki (M-FC01, M-FC02, M-FC03)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki" / "books"
SLIDES = ROOT / "slides" / "VOL-03"

MODULES = [
    {
        "code": "M-FC01",
        "book_id": "m-fc01-ministeri",
        "dir": WIKI / "moduli" / "m-fc01-ministeri" / "chapters",
        "files": [
            "01-lavorare-ministeri-funzioni-centrali.md",
            "02-anatomia-bando-ministeriale-ripam.md",
            "03-profili-professionali-ccnl-mansioni.md",
            "04-governo-ministeri-amministrazione-centrale.md",
            "05-presidenza-consiglio-ministri.md",
            "06-organizzazione-interna-ministeri.md",
            "07-avvocatura-stato.md",
            "08-piao-performance-anticorruzione-valore-pubblico.md",
            "09-contabilita-stato-bilancio-ministeriale.md",
            "10-contratti-pubblici-pnrr-amministrazione-digitale.md",
            "11-casi-pratici-ministeriali.md",
            "12-quesiti-situazionali-codice-comportamento.md",
            "13-matrice-materie-piano-30-60-90.md",
            "14-simulazione-finale-diario-errori.md",
            "15-appendici-operative.md",
        ],
    },
    {
        "code": "M-FC02",
        "book_id": "m-fc02-agenzie-fiscali",
        "dir": WIKI / "moduli" / "m-fc02-agenzie-fiscali" / "chapters",
        "files": [
            "01-mappa-agenzie-fiscali-profili-concorsuali.md",
            "02-bando-decoder-fiscale.md",
            "03-ordinamento-organizzazione-ae-adm-ader.md",
            "04-diritto-tributario-teoria-imposta.md",
            "05-accertamento-controlli-compliance-fiscale.md",
            "05a-sanzioni-amministrative-reati-tributari.md",
            "05b-tutela-processo-tributario.md",
            "06-adempimenti-fiscali-redditi-iva-dichiarazioni.md",
            "07-riscossione-nazionale-lavoro-ader.md",
            "08-dogane-procedure-doganali-adm.md",
            "09-accise-giochi-monopoli.md",
            "10-catasto-cartografia-estimo-pubblicita-immobiliare.md",
            "11-contabilita-aziendale-economia-impresa-fisco.md",
            "12-civile-commerciale-applicati-fisco-dogane-riscossione.md",
            "13-casi-pratici-quiz-orale-agenzie-fiscali.md",
            "14-appendici-operative.md",
        ],
    },
    {
        "code": "M-FC03",
        "book_id": "m-fc03-enti-non-economici",
        "dir": WIKI / "moduli" / "m-fc03-enti-non-economici" / "chapters",
        "files": [
            "01-lavorare-enti-pubblici-non-economici.md",
            "02-ordinamento-governance-epne.md",
            "03-inps-previdenza-servizi-prestazioni.md",
            "04-inail-assicurazione-prevenzione-prestazioni.md",
            "05-procedimenti-epne-cittadini-imprese.md",
            "06-bilancio-patrimonio-controlli-epne.md",
            "07-performance-piao-valore-pubblico-epne.md",
            "08-personale-epne-ccnl-funzioni-centrali.md",
            "09-contratti-acquisti-forniture-epne.md",
            "10-bando-decoder-epne.md",
            "11-casi-pratici-epne.md",
            "12-quesiti-situazionali-epne.md",
            "13-piano-30-60-90-inps-inail-epne.md",
            "appendice-a-vigilanza-ispettiva-inps-inail.md",
            "appendice-b-glossario-previdenza-assicurazione-prestazioni.md",
            "appendice-c-schede-rapide-aci-enac-istat-enea-asi-cri.md",
            "appendice-d-errori-tipici-bandi-epne.md",
            "appendice-e-rinvii-ragionati-altri-moduli.md",
            "appendice-f-materie-integrative-inail-ripam.md",
        ],
    },
]

SKIP_H2 = {
    "specifica struttura madre",
    "riferimenti consolidati",
    "riferimenti",
    "note di review",
    "fonti",
    "come usare questo capitolo",
    "diario errori del capitolo",
    "diario dei rischi di perimetro",
    "checklist operativa finale",
}

SPECIAL = (
    "apertura editoriale",
    "obiettivo del capitolo",
    "mappa bando del capitolo",
    "mappa bando",
    "caso guidato",
    "domanda da commissario",
    "domanda-trappola",
    "errore tipico",
    "mini-esercizio",
    "da sapere in 5 righe",
)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def md_inline(s: str) -> str:
    s = re.sub(r"!\[.*?\]\(.*?\)", "", s)
    s = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = s.replace("'", "'").replace("'", "'")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        meta[key] = val
    return meta, body


def split_h2(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"(?m)^## ", body)
    out = []
    for part in parts[1:]:
        lines = part.splitlines()
        title = md_inline(lines[0])
        rest = "\n".join(lines[1:]).strip()
        out.append((title, rest))
    return out


def paragraphs(body: str, n: int = 3, limit: int = 420) -> list[str]:
    chunks = []
    buf: list[str] = []
    for line in body.splitlines():
        if line.strip().startswith("#"):
            if buf:
                chunks.append(" ".join(buf))
                buf = []
            continue
        if line.strip().startswith("|"):
            if buf:
                chunks.append(" ".join(buf))
                buf = []
            continue
        if not line.strip():
            if buf:
                chunks.append(" ".join(buf))
                buf = []
            continue
        if line.strip().startswith(">") or line.strip().startswith("-") or re.match(r"^\d+\.", line.strip()):
            text = md_inline(re.sub(r"^>\s*", "", line.strip()))
            text = re.sub(r"^[-*]\s+", "", text)
            text = re.sub(r"^\d+\.\s+", "", text)
            if text:
                chunks.append(text)
            continue
        buf.append(md_inline(line))
    if buf:
        chunks.append(" ".join(buf))
    cleaned = []
    for c in chunks:
        c = c.strip()
        if len(c) < 40:
            continue
        if c.lower().startswith("figura "):
            continue
        cleaned.append(c[:limit].rsplit(" ", 1)[0] + ("…" if len(c) > limit else "") if len(c) > limit else c)
        if len(cleaned) >= n:
            break
    return cleaned


def parse_table(body: str) -> list[list[str]] | None:
    rows = []
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            if rows:
                break
            continue
        cells = [md_inline(c) for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)
    if len(rows) < 2:
        return None
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    return rows[:7]


def table_html(rows: list[list[str]]) -> str:
    head = "".join(f"<th>{esc(c)}</th>" for c in rows[0])
    body = []
    for row in rows[1:]:
        body.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>")
    return (
        f'<table class="dense reveal d3"><thead><tr>{head}</tr></thead>'
        f"<tbody>{''.join(body)}</tbody></table>"
    )


def cover_title_html(title: str) -> str:
    if len(title) <= 46:
        return esc(title)
    for sep in (": ", " — ", ", "):
        if sep in title:
            a, b = title.split(sep, 1)
            return f"{esc(a)}{sep.strip()}<br>{esc(b)}"
    words = title.split()
    mid = max(3, len(words) // 2)
    return esc(" ".join(words[:mid])) + "<br>" + esc(" ".join(words[mid:]))


def slug_from_file(name: str) -> str:
    stem = Path(name).stem
    stem = re.sub(r"^\d+[a-z]?-", "", stem)
    return stem


def split_h3(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"(?m)^### ", body)
    if len(parts) <= 1:
        return []
    out = []
    for part in parts[1:]:
        lines = part.splitlines()
        title = md_inline(lines[0])
        rest = "\n".join(lines[1:]).strip()
        out.append((title, rest))
    return out


def find_section(sections: list[tuple[str, str]], *keys: str) -> str:
    keys = tuple(k.lower() for k in keys)
    for title, body in sections:
        t = title.lower()
        if any(k in t for k in keys):
            return body
        for h3t, h3b in split_h3(body):
            if any(k in h3t.lower() for k in keys):
                return h3b
    return ""


def is_skipped_title(title: str) -> bool:
    t = title.lower()
    if t in SKIP_H2 or any(t.startswith(s) for s in SKIP_H2):
        return True
    if any(k in t for k in SPECIAL):
        return True
    if "review" in t or t.startswith("note "):
        return True
    if t.startswith("orientamento"):
        return True
    return False


def content_sections(sections: list[tuple[str, str]]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for title, body in sections:
        h3s = split_h3(body)
        nucleo = bool(re.match(r"^N-[A-Z0-9]+-", title, re.I))
        if nucleo or (h3s and len(h3s) >= 4):
            for h3t, h3b in h3s:
                if is_skipped_title(h3t):
                    continue
                if len(paragraphs(h3b, 1, 200)) == 0 and not parse_table(h3b):
                    continue
                out.append((h3t, h3b))
            continue
        if is_skipped_title(title):
            continue
        out.append((title, body))
    return out


def cards_html(items: list[tuple[str, str]], cls: str = "grid-2") -> str:
    bits = []
    delay = 2
    for h, p in items[:4]:
        bits.append(
            f'<div class="card reveal d{delay}"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
        )
        delay += 1
    return f'<div class="{cls}">{"".join(bits)}</div>'


def slide(kind: str, inner: str, foot_left: str, foot_right: str, extra_class: str = "") -> str:
    cls = f"slide {kind} {extra_class}".strip()
    return f"""            <section class="{cls}">
                <div class="pad">
{inner}
                </div>
                <div class="foot"><span>{foot_left}</span><span>{foot_right}</span></div>
            </section>
"""


def build_deck(ch: dict, next_ch: dict | None, total: int) -> str:
    n = ch["n"]
    title = ch["title"]
    module = ch["module"]
    source = ch["source"]
    path = ROOT / source.replace("/", "\\") if "\\" not in source else ROOT / source
    path = ROOT / Path(*source.split("/"))
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    title = meta.get("title") or title
    sections = split_h2(body)
    apertura = find_section(sections, "apertura editoriale")
    obiettivo = find_section(sections, "obiettivo del capitolo")
    bando = find_section(sections, "mappa bando")
    caso = find_section(sections, "caso guidato")
    commissario = find_section(sections, "domanda da commissario")
    trappola = find_section(sections, "domanda-trappola", "trappola")
    errore = find_section(sections, "errore tipico")
    cinque = find_section(sections, "da sapere in 5 righe")
    nuclei = content_sections(sections)

    ap_p = paragraphs(apertura, 2, 500) or paragraphs(obiettivo, 2, 500)
    lead = ap_p[0] if ap_p else f"Questo capitolo insegna {title.lower()} per la prova concorsuale, non come elenco di etichette."
    ob_p = paragraphs(obiettivo, 2, 380)
    bando_table = parse_table(bando)
    caso_p = paragraphs(caso, 3, 360)
    comm_p = paragraphs(commissario, 2, 420)
    trap_p = paragraphs(trappola, 2, 420)
    err_p = paragraphs(errore, 2, 400)
    cinque_p = paragraphs(cinque, 5, 280) or [p[:280] for p in paragraphs(obiettivo, 5, 240)]

    skins = ["ivory", "pearl", "ivory", "pearl"]
    slides: list[str] = []

    # cover
    slides.append(
        f"""            <section class="slide ancora active">
                <img class="brand-logo" src="../../assets/logo.png" alt="Capitale Personale">
                <div class="pad">
                    <p class="kicker reveal">VOL-03 · Capitolo {n}</p>
                    <hr class="gold-rule reveal d1" style="margin: 28px 0 36px;">
                    <p class="cover-sub reveal d1">{esc(module)}</p>
                    <h1 class="h-display cover-title reveal d2">{cover_title_html(title)}</h1>
                    <p class="lead reveal d3" style="margin-top: 36px; max-width: 1200px;">{esc(lead)}</p>
                </div>
                <div class="foot"><span>Capitale Personale</span><span>Il Metodo BANDO</span></div>
            </section>
"""
    )

    # 01 problema
    che = ob_p[0] if ob_p else lead
    serve = ob_p[1] if len(ob_p) > 1 else "Serve a collocare ente, funzione, atto e output di prova prima di aprire il manuale."
    inner = f"""                    <p class="kicker reveal">01 · Il problema in prova</p>
                    <h2 class="h-display section-title reveal d1">Che cos’è, e a che serve</h2>
                    <p class="lead reveal d2">{esc(che)}</p>
                    {cards_html([("Che cos’è", che), ("A che serve in prova", serve)])}"""
    slides.append(slide("ivory", inner, "Capitale Personale · VOL-03", f"02 / {total:02d}"))

    # 02 BANDO
    if bando_table:
        inner = f"""                    <p class="kicker reveal">02 · BANDO</p>
                    <h2 class="h-display section-title reveal d1">Cinque decisioni su questo capitolo</h2>
                    <p class="lead reveal d2">Il metodo non parte dal manuale. Parte dal bando e ricostruisce nuclei, diario e output.</p>
                    {table_html(bando_table)}"""
    else:
        inner = f"""                    <p class="kicker reveal">02 · BANDO</p>
                    <h2 class="h-display section-title reveal d1">Dal bando all’output</h2>
                    <div class="map reveal d2">
                        <div class="node"><h3>Bando</h3><p>Ente, profilo, prove, materie.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Aree</h3><p>Comune, specialistico, rinvii.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Nuclei</h3><p>Istituti che spostano il punteggio.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Output</h3><p>Quiz, caso, orale, atto.</p></div>
                    </div>
                    <div class="note reveal d3"><strong>Nota</strong><p>Se non sai quale output chiede la prova, stai ancora catalogando materie, non preparando una prestazione.</p></div>"""
    slides.append(slide("pearl", inner, "Capitale Personale · VOL-03", f"03 / {total:02d}"))

    # nuclei teaching slides (up to 8)
    used = 0
    for title_s, body_s in nuclei[:9]:
        used += 1
        kind = skins[used % 4]
        ps = paragraphs(body_s, 3, 360)
        tbl = parse_table(body_s)
        h3s = re.findall(r"(?m)^### (.+)$", body_s)
        kicker_n = used + 2
        short = title_s
        if len(short) > 72:
            short = short[:69] + "…"
        parts = [f'                    <p class="kicker reveal">{kicker_n:02d} · Nucleo</p>',
                 f'                    <h2 class="h-display section-title reveal d1">{esc(short)}</h2>']
        if ps:
            parts.append(f'                    <p class="lead reveal d2">{esc(ps[0])}</p>')
        if tbl:
            parts.append("                    " + table_html(tbl))
        elif len(h3s) >= 2:
            cards = []
            bodies = re.split(r"(?m)^### ", body_s)[1:]
            for chunk in bodies[:4]:
                lines = chunk.splitlines()
                h = md_inline(lines[0])
                p = paragraphs("\n".join(lines[1:]), 1, 220)
                cards.append((h, p[0] if p else "Vedi il nesso con la prova: definizione, funzione, limite."))
            parts.append("                    " + cards_html(cards, "grid-2" if len(cards) <= 2 else "grid-2"))
        elif len(ps) >= 2:
            parts.append(
                "                    "
                + cards_html(
                    [
                        ("Come funziona", ps[1] if len(ps) > 1 else ps[0]),
                        ("In prova", ps[2] if len(ps) > 2 else "Collega sempre ente, funzione, atto e output. Non fermarti al nome dell’istituto."),
                    ]
                )
            )
        else:
            parts.append(
                '                    <div class="note reveal d3"><strong>In prova</strong><p>'
                + esc(ps[0] if ps else "Definisci l’istituto, indica la funzione e chiudi con un errore da evitare.")
                + "</p></div>"
            )
        slides.append(slide(kind, "\n".join(parts), "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # mappa di flusso
    inner = f"""                    <p class="kicker reveal">{used+3:02d} · Sequenza</p>
                    <h2 class="h-display section-title reveal d1">Come si ragiona sul fascicolo</h2>
                    <p class="lead reveal d2">Prima la qualificazione, poi il procedimento, poi l’output. Saltare un passaggio produce risposte generiche.</p>
                    <div class="map reveal d3">
                        <div class="node"><h3>Fatto</h3><p>Che cosa è accaduto e quale interesse pubblico è coinvolto.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Fonte</h3><p>Quale regola, atto o bando attribuisce la funzione.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Atto</h3><p>Chi decide, con quale provvedimento, entro quali limiti.</p></div>
                        <div class="arrow">→</div>
                        <div class="node"><h3>Output</h3><p>Quiz, caso, orale: una frase per ciascun passaggio.</p></div>
                    </div>
                    <div class="note reveal d4"><strong>Nota</strong><p>Il nome dell’ente non basta. Servono funzione, atto e prova richiesta.</p></div>"""
    slides.append(slide("pearl", inner, "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # caso
    if caso_p:
        cards = [("Situazione", caso_p[0])]
        if len(caso_p) > 1:
            cards.append(("Ragionamento", caso_p[1]))
        if len(caso_p) > 2:
            cards.append(("Chiusura", caso_p[2]))
        inner = f"""                    <p class="kicker reveal">Caso guidato</p>
                    <h2 class="h-display section-title reveal d1">Un fascicolo, non un riassunto</h2>
                    <p class="lead reveal d2">{esc(caso_p[0])}</p>
                    {cards_html(cards[1:] or [("Metodo", "Identifica ente, funzione, atto, controllo e output.")])}"""
    else:
        inner = """                    <p class="kicker reveal">Caso guidato</p>
                    <h2 class="h-display section-title reveal d1">Parti dal fatto, non dalla materia</h2>
                    <p class="lead reveal d2">Su una traccia, nomi l’ente, la funzione, l’atto e il limite. Poi scegli l’output: quiz, caso o orale.</p>
                    <div class="warn reveal d3"><strong>Errore</strong><p>Elencare istituti senza collocarli in un procedimento produce una risposta da manuale, non da prova.</p></div>"""
    slides.append(slide("ivory", inner, "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # commissario / trappola
    c1 = comm_p[0] if comm_p else "Spiega l’istituto con una definizione operativa e un limite."
    c2 = comm_p[1] if len(comm_p) > 1 else (comm_p[0] if comm_p else "Chiudi con un esempio breve.")
    t1 = trap_p[0] if trap_p else "La trappola è trattare un nome (portale, ente, legge) come se bastasse da solo."
    t2 = trap_p[1] if len(trap_p) > 1 else "Verifica sempre contenuto del bando, funzione e atto."
    inner = f"""                    <p class="kicker reveal">Verifica</p>
                    <h2 class="h-display section-title reveal d1">Due domande da saper spiegare</h2>
                    <div class="grid-2">
                        <div class="card reveal d2">
                            <div class="num">Commissario</div>
                            <h3 style="margin-top:16px;">Che cosa chiede</h3>
                            <p>{esc(c1)}</p>
                            <p>{esc(c2)}</p>
                        </div>
                        <div class="card reveal d3">
                            <div class="num">Trappola</div>
                            <h3 style="margin-top:16px;">Dove si sbaglia</h3>
                            <p>{esc(t1)}</p>
                            <p>{esc(t2)}</p>
                        </div>
                    </div>"""
    slides.append(slide("pearl", inner, "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # errori
    e1 = err_p[0] if err_p else "Studiare il volume come enciclopedia, senza bando e senza output."
    e2 = err_p[1] if len(err_p) > 1 else "Confondere il nome dell’ente con la titolarità della funzione."
    inner = f"""                    <p class="kicker reveal">Errori</p>
                    <h2 class="h-display section-title reveal d1">Distinzioni da tenere ferme</h2>
                    {cards_html([("Errore tipico", e1), ("Correzione", e2)])}
                    <div class="warn reveal d4"><strong>Attenzione</strong><p>Non inventare soglie, importi o termini. I dati mobili si verificano sul bando e sulla fonte ufficiale vigente.</p></div>"""
    slides.append(slide("ivory", inner, "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # cinque regole
    rules = cinque_p[:5]
    while len(rules) < 5:
        rules.append("Collega sempre ente, funzione, atto e output di prova.")
    rule_html = []
    for i, r in enumerate(rules, 2):
        rule_html.append(f'<p class="lead reveal d{i}">{i-1}. {esc(r)}</p>')
    inner = f"""                    <p class="kicker reveal">Da tenere ferme</p>
                    <h2 class="h-display section-title reveal d1">Cinque regole, con il perché</h2>
                    <div class="stack" style="max-width: 1580px;">
                        {''.join(rule_html)}
                    </div>"""
    slides.append(slide("ancora", inner, "Capitale Personale · VOL-03", f"{len(slides)+1:02d} / {total:02d}"))

    # chiusura
    if next_ch:
        nxt_inner = f"""                    <p class="kicker reveal">Prossimo capitolo</p>
                    <hr class="gold-rule reveal d1" style="margin: 28px 0 36px;">
                    <h2 class="h-display reveal d2" style="font-size: 64px; max-width: 1500px;">{esc(next_ch['title'])}</h2>
                    <p class="lead reveal d3" style="max-width: 1100px;">Il capitolo successivo sposta il fascicolo: stessa famiglia, nuovo nucleo da saper usare in prova.</p>"""
        nxt_foot = f"VOL-03 · Capitolo {next_ch['n']}"
    else:
        nxt_inner = """                    <p class="kicker reveal">Dal volume al bando</p>
                    <hr class="gold-rule reveal d1" style="margin: 28px 0 36px;">
                    <h2 class="h-display reveal d2" style="font-size: 64px; max-width: 1500px;">VOL-03 · Fine</h2>
                    <p class="lead reveal d3" style="max-width: 1100px;">Il volume orienta. Il bando decide profondità, prove e priorità. Torna al Metodo BANDO e al nucleo del VOL-01.</p>"""
        nxt_foot = "VOL-03 · Fine"
    slides.append(
        f"""            <section class="slide ancora">
                <img class="brand-logo" src="../../assets/logo.png" alt="Capitale Personale">
                <div class="pad" style="display:flex; flex-direction:column; justify-content:center;">
{nxt_inner}
                </div>
                <div class="foot"><span>Capitale Personale</span><span>{nxt_foot}</span></div>
            </section>
"""
    )

    total_now = len(slides)
    # rewrite sequential NN / total in body feet
    html_slides = []
    for i, block in enumerate(slides):
        if i == 0 or i == total_now - 1:
            html_slides.append(block)
            continue
        block = re.sub(r"<span>\d{2} / \d{2}</span>", f"<span>{i+1:02d} / {total_now:02d}</span>", block, count=1)
        html_slides.append(block)

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOL-03 · Capitolo {n} — {esc(title)}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;1,500&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../../assets/capitale-personale.css">
</head>
<body data-edit-key="cp-vol03-{n}" data-volume="VOL-03" data-chapter="{n}" data-chapter-title="{esc(title)}" data-source="{esc(source)}">
    <div class="edit-hotzone"></div>
    <button class="edit-toggle" id="editToggle" title="Modifica (E)">Modifica</button>
    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">

{''.join(html_slides)}
        </main>
    </div>
    <nav class="deck-controls" aria-label="Avanzamento">
        <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
        <span class="page-count" id="pageCount">01 / {total_now:02d}</span>
    </nav>
    <script src="../../assets/deck.js"></script>
</body>
</html>
"""


def catalog_html(chapters: list[dict]) -> str:
    items = []
    for ch in chapters:
        items.append(
            f'            <li><a href="{ch["folder"]}/index.html"><span class="num">{ch["n"]}</span>'
            f'<span class="title">{esc(ch["folder"][3:])}</span><span class="status">Pronto</span></a></li>'
        )
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOL-03 — Capitoli in ordine · Slide staff</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Playfair+Display:ital,wght@0,600;1,500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/catalog.css">
</head>
<body>
    <header>
        <img src="../assets/logo.png" alt="Capitale Personale">
        <div>
            <p class="kicker">VOL-03 · Indice volume compilato</p>
            <h1>Funzioni centrali, Fisco, Previdenza e Ispettivo</h1>
        </div>
    </header>
    <main>
        <p class="meta"><a href="../index.html" style="color:#D4AF37;text-decoration:none;">← Catalogo</a> · Cartella = numero volume + slug file wiki · 01–50 pronti</p>
        <ol class="chapters">
{chr(10).join(items)}
        </ol>
        <footer>01–15 M-FC01 · 16–31 M-FC02 · 32–50 M-FC03</footer>
    </main>
</body>
</html>
"""


def collect_chapters() -> list[dict]:
    chapters = []
    n = 0
    for mod in MODULES:
        for fname in mod["files"]:
            n += 1
            src = mod["dir"] / fname
            text = src.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(text)
            title = meta.get("title") or Path(fname).stem.replace("-", " ")
            slug = slug_from_file(fname)
            folder = f"{n:02d}-{slug}"
            rel = f"wiki/books/moduli/{mod['book_id']}/chapters/{fname}"
            chapters.append(
                {
                    "n": f"{n:02d}",
                    "module": mod["code"],
                    "title": title,
                    "source": rel,
                    "folder": folder,
                    "book_id": mod["book_id"],
                    "status": "ready",
                }
            )
    return chapters


def main() -> None:
    chapters = collect_chapters()
    SLIDES.mkdir(parents=True, exist_ok=True)
    manifest = {
        "volume": "VOL-03",
        "volume_title": "Funzioni centrali, Fisco, Previdenza e Ispettivo",
        "spec": "wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/planning/00-scheda-pipeline.md",
        "order": "volume compilato: M-FC01, M-FC02, M-FC03",
        "chapters": chapters,
    }
    (SLIDES / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (SLIDES / "index.html").write_text(catalog_html(chapters), encoding="utf-8")

    for i, ch in enumerate(chapters):
        nxt = chapters[i + 1] if i + 1 < len(chapters) else None
        folder = SLIDES / ch["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "capitolo.json").write_text(
            json.dumps(
                {
                    "volume": "VOL-03",
                    "n": ch["n"],
                    "title": ch["title"],
                    "source": ch["source"],
                    "book_id": ch["book_id"],
                    "folder": ch["folder"],
                    "module": ch["module"],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        html = build_deck(ch, nxt, 18)
        (folder / "index.html").write_text(html, encoding="utf-8")
        slides_n = html.count('<section class="slide')
        print(f"VOL-03 {ch['n']}  {slides_n} slide  {ch['folder']}")
    print(f"generati {len(chapters)} deck VOL-03")


if __name__ == "__main__":
    main()
