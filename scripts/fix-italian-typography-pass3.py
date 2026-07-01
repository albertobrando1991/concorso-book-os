#!/usr/bin/env python3
"""Third pass: remaining accents, yes/no sì, and wiki slug path repair."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "wiki" / "books" / "il-metodo-bando" / "chapters"

APOSTROPHES = "'\u2019\u02bc\u0060\u00b4"

EXTRA_WORDS = {
    "dira": "dirà",
    "Dira": "Dirà",
    "finira": "finirà",
    "Finira": "Finirà",
    "servira": "servirà",
    "Servira": "Servirà",
    "Invalidita": "Invalidità",
    "invalidita": "invalidità",
}

# Only de-accent paths in wiki metadata/link segments (filenames use ASCII slugs).
WIKI_PATH_PREFIXES = (
    "sources/",
    "topics/",
    "entities/",
    "wiki/sources/",
    "wiki/topics/",
    "wiki/entities/",
    "reviews/",
)


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def deaccent_wiki_paths(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        segment = match.group(0)
        for prefix in WIKI_PATH_PREFIXES:
            if prefix in segment:
                # De-accent only the path portion after the prefix up to .md
                idx = segment.index(prefix)
                head = segment[: idx + len(prefix)]
                tail = segment[idx + len(prefix) :]
                return head + strip_accents(tail)
        return segment

    # YAML arrays and markdown wiki links
    text = re.sub(
        r"(?:sources|topics|entities|reviews|wiki/sources|wiki/topics|wiki/entities)/[a-zA-Z0-9._\-àèéìòù]+(?:\.md)?",
        repl,
        text,
    )
    return text


def fix_yes_si(text: str) -> str:
    # Affirmative "sì" in common workbook patterns (not reflexive "si").
    text = re.sub(r"\bse si\b", "se sì", text)
    text = re.sub(r"\be se si\b", "e se sì", text)
    text = re.sub(r"\bsi / no\b", "sì / no", text)
    text = re.sub(r"\| si \|", "| sì |", text)
    text = re.sub(r"\| Si \|", "| Sì |", text)
    text = re.sub(r"\bsi, ", "sì, ", text)
    text = re.sub(r"\bSi, ", "Sì, ", text)
    return text


def fix_ce_apostrophe(text: str) -> str:
    # c'e -> c'è but not c'entra / c'è already fixed
    return re.sub(rf"\bc[{APOSTROPHES}]e\b", "c'è", text)


def fix_chapter_ids(text: str) -> str:
    # Keep machine ids ASCII-only
    text = re.sub(
        r"^(id: chapter-[^\n]+)$",
        lambda m: f"id: {strip_accents(m.group(1).removeprefix('id: '))}",
        text,
        flags=re.MULTILINE,
    )
    return text


def fix_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original

    text = fix_ce_apostrophe(text)
    for old, new in EXTRA_WORDS.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)

    text = fix_yes_si(text)
    text = deaccent_wiki_paths(text)
    text = fix_chapter_ids(text)

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def iter_targets(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.md")) if target.is_dir() else []


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, default=CHAPTERS)
    args = parser.parse_args()
    changed = sum(fix_file(p) for p in iter_targets(args.path))
    print(f"pass3 changed {changed} files in {args.path}")


if __name__ == "__main__":
    main()