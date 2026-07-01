#!/usr/bin/env python3
"""Restore Italian accents and light punctuation hygiene in book chapter markdown."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "wiki" / "books" / "il-metodo-bando" / "chapters"

# Nouns/adjectives in -ita → -ità (explicit whitelist; avoids verbs like limita, merita).
ITA_TO_ITA_ACCENT = {
    "abilita": "abilità",
    "accessibilita": "accessibilità",
    "affidabilita": "affidabilità",
    "ambiguita": "ambiguità",
    "ammissibilita": "ammissibilità",
    "annullabilita": "annullabilità",
    "antichita": "antichità",
    "attivita": "attività",
    "autorita": "autorità",
    "capacita": "capacità",
    "collettivita": "collettività",
    "comodita": "comodità",
    "compatibilita": "compatibilità",
    "comprensibilita": "comprensibilità",
    "comunita": "comunità",
    "conoscibilita": "conoscibilità",
    "contabilita": "contabilità",
    "continuita": "continuità",
    "controllabilita": "controllabilità",
    "criticita": "criticità",
    "curiosita": "curiosità",
    "disabilita": "disabilità",
    "disponibilita": "disponibilità",
    "facilita": "facilità",
    "familiarita": "familiarità",
    "finalita": "finalità",
    "formalita": "formalità",
    "fruibilita": "fruibilità",
    "genericita": "genericità",
    "identita": "identità",
    "idoneita": "idoneità",
    "imparzialita": "imparzialità",
    "incompatibilita": "incompatibilità",
    "inconferibilita": "inconferibilità",
    "irregolarita": "irregolarità",
    "legalita": "legalità",
    "leggibilita": "leggibilità",
    "legittimita": "legittimità",
    "lucidita": "lucidità",
    "modalita": "modalità",
    "necessita": "necessità",
    "neutralita": "neutralità",
    "novita": "novità",
    "nullita": "nullità",
    "opacita": "opacità",
    "opportunita": "opportunità",
    "parita": "parità",
    "passivita": "passività",
    "penalita": "penalità",
    "pluralita": "pluralità",
    "possibilita": "possibilità",
    "priorita": "priorità",
    "probabilita": "probabilità",
    "produttivita": "produttività",
    "profondita": "profondità",
    "proporzionalita": "proporzionalità",
    "pubblicita": "pubblicità",
    "qualita": "qualità",
    "quantita": "quantità",
    "regolarita": "regolarità",
    "reperibilita": "reperibilità",
    "responsabilita": "responsabilità",
    "riconducibilita": "riconducibilità",
    "rigidita": "rigidità",
    "rintracciabilita": "rintracciabilità",
    "sanita": "sanità",
    "sostenibilita": "sostenibilità",
    "stabilita": "stabilità",
    "superficialita": "superficialità",
    "tecnicita": "tecnicità",
    "tracciabilita": "tracciabilità",
    "trasferibilita": "trasferibilità",
    "universita": "università",
    "usabilita": "usabilità",
    "utilita": "utilità",
    "validita": "validità",
    "velocita": "velocità",
    "verificabilita": "verificabilità",
    "viziosita": "viziosità",
    "interoperabilita": "interoperabilità",
    "intensita": "intensità",
    "difficolta": "difficoltà",
    "gravita": "gravità",
    "societa": "società",
    "specialita": "specialità",
    "semplicita": "semplicità",
    "complessita": "complessità",
    "chiarezza": "chiarezza",
    "rilevanza": "rilevanza",
    "sicche": "sicché",
}

APOSTROPHES = "'\u2019\u02bc\u0060\u00b4"

WORD_REPLACEMENTS = {
    "piu": "più",
    "pero": "però",
    "cosi": "così",
    "gia": "già",
    "perche": "perché",
    "puo": "può",
    "cio": "ciò",
    "cioe": "cioè",
    "finche": "finché",
    "affinche": "affinché",
    "poiche": "poiché",
    "percio": "perciò",
    "sara": "sarà",
    "fara": "farà",
    "verra": "verrà",
    "dara": "darà",
    "avra": "avrà",
    "potra": "potrà",
    "dovra": "dovrà",
    "andra": "andrà",
    "avro": "avrò",
    "saro": "sarò",
    "faro": "farò",
    "potro": "potrò",
    "dovro": "dovrò",
    "andro": "andrò",
    "e": "è",  # applied only via apostrophe / phrase rules below
}

APOSTROPHE_PHRASES = [
    (r"\bC'e'\b", "C'è"),
    (r"\bc'e'\b", "c'è"),
    (r"\bL'e'\b", "L'è"),
    (r"\bl'e'\b", "l'è"),
    (r"\bQuell'e'\b", "Quell'è"),
    (r"\bquell'e'\b", "quell'è"),
    (r"\bDov'e'\b", "Dov'è"),
    (r"\bdov'e'\b", "dov'è"),
    (r"\bCom'e'\b", "Com'è"),
    (r"\bcom'e'\b", "com'è"),
    (r"\bQual'e'\b", "Qual'è"),
    (r"\bqual'e'\b", "qual'è"),
    (r"\bN'e'\b", "N'è"),
    (r"\bn'e'\b", "n'è"),
    (r"\bS'e'\b", "S'è"),
    (r"\bs'e'\b", "s'è"),
    (r"\bD'e'\b", "D'è"),
    (r"\bd'e'\b", "d'è"),
    (r"\bE'\b", "È"),
    (r"\be'\b", "è"),
    (r"\bpiu'\b", "più"),
    (r"\bpero'\b", "però"),
    (r"\bcosi'\b", "così"),
    (r"\bgia'\b", "già"),
    (r"\bperche'\b", "perché"),
    (r"\bpuo'\b", "può"),
    (r"\bcio'\b", "ciò"),
    (r"\bPerche'\b", "Perché"),
    (r"\bperche'\b", "perché"),
]

CAPITALIZED_WORDS = {
    "Perche": "Perché",
    "Piu": "Più",
    "Pero": "Però",
    "Cosi": "Così",
    "Gia": "Già",
    "Puo": "Può",
    "Cio": "Ciò",
    "Cioe": "Cioè",
    "Sara": "Sarà",
    "Fara": "Farà",
    "Verra": "Verrà",
    "Dara": "Darà",
    "Avra": "Avrà",
    "Potra": "Potrà",
    "Dovra": "Dovrà",
    "Andra": "Andrà",
}

# -ita whitelist with capitalized forms
for lower, accented in list(ITA_TO_ITA_ACCENT.items()):
    CAPITALIZED_WORDS[lower.capitalize()] = accented[0].upper() + accented[1:]


def build_word_patterns() -> list[tuple[re.Pattern[str], str]]:
    patterns: list[tuple[re.Pattern[str], str]] = []

    for old, new in WORD_REPLACEMENTS.items():
        if old == "e":
            continue
        patterns.append((re.compile(rf"\b{re.escape(old)}\b", re.IGNORECASE), new))

    for old, new in ITA_TO_ITA_ACCENT.items():
        patterns.append((re.compile(rf"\b{re.escape(old)}\b", re.IGNORECASE), new))

    for old, new in CAPITALIZED_WORDS.items():
        patterns.append((re.compile(rf"\b{re.escape(old)}\b"), new))

    for pattern, repl in APOSTROPHE_PHRASES:
        patterns.append((re.compile(pattern), repl))

    patterns.append((re.compile(rf"\bqual e[{APOSTROPHES}]?\b", re.IGNORECASE), "qual è"))
    patterns.append((re.compile(r"\bcio che\b", re.IGNORECASE), "ciò che"))
    patterns.append((re.compile(r"\bcio che\b", re.IGNORECASE), "ciò che"))

    return patterns


PATTERNS = build_word_patterns()


def fix_punctuation(text: str) -> str:
    # Do not alter ISO-8601 timestamps in YAML frontmatter.
    text = re.sub(
        r"(\d{4}-\d{2}-\d{2}T\d{2}): (\d{2}): (\d{2})\+(\d{2}): (\d{2})",
        r"\1:\2:\3+\4:\5",
        text,
    )
    text = re.sub(r" +([,;!?])", r"\1", text)
    text = re.sub(r" +\.(?!\.)(?!\d)", r".", text)
    text = re.sub(r"([,;!?])([^\s\]\)|\n])", r"\1 \2", text)
    text = re.sub(r" {2,}", " ", text)
    return text


def fix_text(text: str) -> str:
    for pattern, repl in PATTERNS:
        if pattern.flags & re.IGNORECASE:
            text = pattern.sub(lambda m, r=repl: r if m.group(0).islower() else r, text)
        else:
            text = pattern.sub(repl, text)
    return fix_punctuation(text)


def process_file(path: Path, dry_run: bool = False) -> int:
    original = path.read_text(encoding="utf-8")
    updated = fix_text(original)
    if updated != original:
        if not dry_run:
            path.write_text(updated, encoding="utf-8", newline="\n")
        return 1
    return 0


def iter_targets(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    flat = sorted(target.glob("*.md"))
    if flat:
        return flat
    return sorted(target.rglob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    changed = 0
    for path in iter_targets(args.dir):
        changed += process_file(path, dry_run=args.dry_run)

    mode = "would change" if args.dry_run else "changed"
    print(f"{mode} {changed} files in {args.dir}")


if __name__ == "__main__":
    main()