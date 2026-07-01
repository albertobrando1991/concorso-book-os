#!/usr/bin/env python3
"""Second pass: fix regressions and remaining accent patterns."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "wiki" / "books" / "il-metodo-bando" / "chapters"

APOSTROPHES = "'\u2019\u02bc\u0060\u00b4"

# e + any apostrophe variant -> è
E_APOSTROPHE = re.compile(rf"\be[{APOSTROPHES}]", re.IGNORECASE)
E_APOSTROPHE_CAP = re.compile(rf"\bE[{APOSTROPHES}]")

EXTRA_WORDS = {
    "integrita": "integrità",
    "Integrita": "Integrità",
    "adottera": "adotterà",
    "usera": "userà",
    "colleghera": "collegherà",
    "studiera": "studierà",
    "Studiera": "Studierà",
    "accorgera": "accorgerà",
    "succedera": "succederà",
    "insegnera": "insegnerà",
    "risolvera": "risolverà",
    "svolgera": "svolgerà",
}

HEADING_FIXES = {
    "## perché ": "## Perché ",
    "## Perche ": "## Perché ",
}


def fix_iso_timestamps(text: str) -> str:
    # Repair broken YAML timestamps like 2026-06-09T11: 08: 53+02: 00
    text = re.sub(
        r"(\d{4}-\d{2}-\d{2}T\d{2}): (\d{2}): (\d{2})\+(\d{2}): (\d{2})",
        r"\1:\2:\3+\4:\5",
        text,
    )
    text = re.sub(
        r"(\d{4}-\d{2}-\d{2}T\d{2}): (\d{2}): (\d{2})\.(\d+Z)",
        r"\1:\2:\3.\4",
        text,
    )
    text = re.sub(
        r"(\d{4}-\d{2}-\d{2}T\d{2}): (\d{2}): (\d{2})Z",
        r"\1:\2:\3Z",
        text,
    )
    text = re.sub(
        r"(\d{4}-\d{2}-\d{2}T\d{2}): (\d{2}): (\d{2})\.(\d+)\+(\d{2}): (\d{2})",
        r"\1:\2:\3.\4+\5:\6",
        text,
    )
    return text


def fix_markdown_bold_colon(text: str) -> str:
    # **Label: ** -> **Label:**
    text = re.sub(r"\*\*([^*\n]+?): \*\*", r"**\1:**", text)
    return text


def fix_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original

    text = fix_iso_timestamps(text)
    text = E_APOSTROPHE_CAP.sub("È", text)
    text = E_APOSTROPHE.sub("è", text)
    text = re.sub(rf"\bne[{APOSTROPHES}]", "né", text)
    text = re.sub(rf"\bNe[{APOSTROPHES}]", "Né", text)

    for old, new in EXTRA_WORDS.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)

    for old, new in HEADING_FIXES.items():
        text = text.replace(old, new)

    text = fix_markdown_bold_colon(text)

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
    print(f"pass2 changed {changed} files in {args.path}")


if __name__ == "__main__":
    main()