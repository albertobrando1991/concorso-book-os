#!/usr/bin/env python3
"""Fourth pass: fix è' regression, Si/No tables, and stray accent+apostrophe."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "wiki" / "books" / "il-metodo-bando" / "chapters"

APOSTROPHES = "'\u2019\u02bc\u0060\u00b4"
E_ACCENT_APOSTROPHE = re.compile(rf"è[{APOSTROPHES}]")
E_ACCENT_APOSTROPHE_CAP = re.compile(rf"È[{APOSTROPHES}]")


def fix_file(text: str) -> str:
    # Regression from pass1 qual e + pass2 e' -> qual è'
    text = E_ACCENT_APOSTROPHE_CAP.sub("È", text)
    text = E_ACCENT_APOSTROPHE.sub("è", text)

    # Workbook yes/no columns
    text = re.sub(r"\bSi / No\b", "Sì / No", text)
    text = re.sub(r"\bSi/No\b", "Sì/No", text)

    return text


def process_path(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = fix_file(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def iter_md_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.md")) if target.is_dir() else []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=Path,
        action="append",
        default=[DEFAULT_DIR],
        help="File or directory (recursive for dirs)",
    )
    args = parser.parse_args()

    changed = 0
    seen: set[Path] = set()
    for target in args.path:
        for path in iter_md_files(target):
            if path in seen:
                continue
            seen.add(path)
            if process_path(path.resolve()):
                changed += 1
                try:
                    print(path.resolve().relative_to(ROOT.resolve()))
                except ValueError:
                    print(path)

    print(f"pass4 changed {changed} files")


if __name__ == "__main__":
    main()