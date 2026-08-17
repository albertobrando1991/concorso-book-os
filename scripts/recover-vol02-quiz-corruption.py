#!/usr/bin/env python3
"""Recover the 107 quiz blocks corrupted by rebalance-vol02-quizzes.py's original
"**" boundary bug (see repair-vol02-quiz-corruption.py's docstring for the
mechanism). Rather than patch already-corrupted text, this rebuilds each
affected quiz block from scratch: original (git HEAD) text -> typography
normalization (same fix_body used everywhere else in VOL-02) -> corrected
relabeling logic, reusing the SAME target letter the corrupted block already
shows in its (never-corrupted) "Risposta corretta: X" line, so the corpus-wide
A/B/C/D balance achieved earlier is preserved exactly.

Only touched quiz blocks are replaced; everything else in each file (all the
other prior fixes already applied) is left exactly as it is on disk.
"""

from __future__ import annotations

import glob
import importlib.util
import re
import subprocess

QUIZ_SPLIT = re.compile(r"(?=^#{3,4} Quiz)", re.M)
ANSWER_RE = re.compile(r"Risposta corretta:?\s*\*?\*?\s*([A-D])\.?")
# Line format now also accepts an optional markdown list marker ("- ") before
# the letter, e.g. "- A. text" -- a real format used by some quizzes that
# otherwise fell through to (and broke) the inline parser.
LINE_OPTION_RE = re.compile(r"^([ \t]*(?:[-*]\s+)?)([A-D])([.)])(\s*)(.+)$", re.M)
INLINE_SPLIT_RE = re.compile(r"([A-D])([.)])(\s+)")
LETTERS4 = ["A", "B", "C", "D"]
LETTERS3 = ["A", "B", "C"]

typo_spec = importlib.util.spec_from_file_location("typo", "scripts/fix-vol02-quotes-apostrophes.py")
typo = importlib.util.module_from_spec(typo_spec)
typo_spec.loader.exec_module(typo)


def parse_line_options(question_part: str):
    matches = list(LINE_OPTION_RE.finditer(question_part))
    if len(matches) not in (3, 4):
        return None
    expected = LETTERS4 if len(matches) == 4 else LETTERS3
    if [m.group(2) for m in matches] != expected:
        return None
    return {m.group(2): m for m in matches}


def rebuild_line_options(question_part: str, options: dict, mapping: dict) -> str:
    letters = LETTERS4 if len(options) == 4 else LETTERS3
    ordered = sorted(options.values(), key=lambda m: m.start())
    span_start = ordered[0].start()
    span_end = ordered[-1].end()
    gaps = [question_part[a.end() : b.start()] for a, b in zip(ordered, ordered[1:])]
    by_new_letter = {mapping[m.group(2)]: m for m in ordered}
    lines = []
    for letter in letters:
        m = by_new_letter[letter]
        prefix, sep, spacing, text = m.group(1), m.group(3), m.group(4), m.group(5)
        lines.append(f"{prefix}{letter}{sep}{spacing}{text}")
    replacement = lines[0]
    for gap, line in zip(gaps, lines[1:]):
        replacement += gap + line
    return question_part[:span_start] + replacement + question_part[span_end:]


def parse_inline_options(question_part: str):
    parts = INLINE_SPLIT_RE.split(question_part)
    pre = parts[0]
    entries = []
    i = 1
    while i + 3 < len(parts):
        entries.append((parts[i], parts[i + 1], parts[i + 2], parts[i + 3]))
        i += 4
    if len(entries) not in (3, 4):
        return None
    expected = LETTERS4 if len(entries) == 4 else LETTERS3
    if [e[0] for e in entries] != expected:
        return None
    return pre, entries


def rebuild_inline_options(pre: str, entries: list, mapping: dict) -> str:
    # Each captured option "text" naturally includes its own trailing
    # separator up to the next letter marker (e.g. "...istruttoria; "),
    # EXCEPT the option that was originally last, whose text has no such
    # separator (nothing followed it but "Risposta corretta"). If that
    # option lands in a non-last position after remapping, it needs a
    # space inserted so it does not run straight into the next letter.
    letters = LETTERS4 if len(entries) == 4 else LETTERS3
    by_new_letter = {mapping[e[0]]: e for e in entries}
    out = pre
    for position, letter in enumerate(letters):
        _, sep, spacing, text = by_new_letter[letter]
        if position < len(letters) - 1 and text and not text[-1].isspace():
            text += " "
        out += f"{letter}{sep}{spacing}{text}"
    return out


def split_question_and_rest(block: str):
    """Like the original script, but correctly excludes the "**" bold-open
    marker that always precedes "Risposta corretta" from the option region."""
    m = ANSWER_RE.search(block)
    if not m:
        return None, None, None
    question_part = block[: m.start()]
    rest = block[m.start() :]
    # Strip the bold-open marker AND any whitespace around it (typically a
    # blank line) that precedes "Risposta corretta" -- all of it belongs to
    # the answer line, not to whichever option happens to be captured last.
    tail = re.search(r"\s*\*\*\s*$", question_part)
    if tail:
        rest = question_part[tail.start() :] + rest
        question_part = question_part[: tail.start()]
    return question_part, rest, m


def option_texts(question_part: str):
    line_options = parse_line_options(question_part)
    if line_options is not None:
        return {letter: m.group(5) for letter, m in line_options.items()}
    parsed = parse_inline_options(question_part)
    if parsed is None:
        return None
    _, entries = parsed
    return {letter: text for letter, _, _, text in entries}


def make_mapping(letters: list, target_correct_letter: str, correct_old_letter: str, old_order: list) -> dict:
    # Deterministic: keep the other options in their original relative order,
    # placed into the remaining new-letter slots in letter order.
    remaining_new = [l for l in letters if l != target_correct_letter]
    remaining_old = [l for l in old_order if l != correct_old_letter]
    mapping = {correct_old_letter: target_correct_letter}
    for old, new in zip(remaining_old, remaining_new):
        mapping[old] = new
    return mapping


def rebuild_quiz(clean_block: str, target_correct_letter: str) -> str:
    question_part, rest, m = split_question_and_rest(clean_block)
    if question_part is None:
        raise AssertionError("nessun marcatore di risposta nel blocco sorgente")
    correct_old_letter = m.group(1)
    original_texts = option_texts(question_part)
    if original_texts is None:
        raise AssertionError("impossibile analizzare le opzioni del blocco sorgente")
    letters = LETTERS4 if len(original_texts) == 4 else LETTERS3
    original_correct_text = original_texts[correct_old_letter]

    line_options = parse_line_options(question_part)
    old_order = letters
    mapping = make_mapping(letters, target_correct_letter, correct_old_letter, old_order)

    if line_options is not None:
        new_question_part = rebuild_line_options(question_part, line_options, mapping)
    else:
        pre, entries = parse_inline_options(question_part)
        new_question_part = rebuild_inline_options(pre, entries, mapping)

    new_rest = ANSWER_RE.sub(
        lambda mm: mm.group(0)[: mm.start(1) - mm.start(0)] + mapping[correct_old_letter] + mm.group(0)[mm.end(1) - mm.start(0) :],
        rest,
        count=1,
    )
    new_block = new_question_part + new_rest

    # verification
    q2, r2, m2 = split_question_and_rest(new_block)
    if q2 is None:
        raise AssertionError("verifica: nessun marcatore di risposta dopo la ricostruzione")
    new_texts = option_texts(q2)
    if new_texts is None:
        raise AssertionError("verifica: opzioni non analizzabili dopo la ricostruzione")
    # A trailing separator space may have been added to whichever option was
    # originally last (see rebuild_inline_options) if it no longer ends the
    # list; that single added space is not a content change.
    if sorted(t.rstrip() for t in new_texts.values()) != sorted(t.rstrip() for t in original_texts.values()):
        raise AssertionError("verifica: testi delle opzioni alterati")
    if new_texts.get(m2.group(1), "").rstrip() != original_correct_text.rstrip():
        raise AssertionError("verifica: la risposta corretta non punta al testo originale")
    if m2.group(1) != target_correct_letter:
        raise AssertionError("verifica: lettera target non applicata")

    return new_block


def is_corrupted(block: str) -> bool:
    q, _, m = split_question_and_rest(block)
    if q is None:
        return False
    # A bold-wrapped question stem (very common, e.g. "**Qual e ...?**") also
    # starts with "\n\n**" before any option appears -- that is NOT
    # corruption. Only look for "\n\n**" occurring AFTER the first real
    # option marker, with more option markers still following it: that is
    # the actual corruption signature (the bold-open that belongs right
    # before "Risposta corretta" landed in the middle of the option list).
    first_option = re.search(r"[A-D][.)]\s", q)
    if not first_option:
        return False
    tail = q[first_option.start() :]
    idx = tail.find("\n\n**")
    if idx == -1:
        return False
    return bool(re.search(r"[A-D][.)]\s", tail[idx + 4 :]))


def main() -> None:
    files = sorted(glob.glob("wiki/books/moduli/m-fl0*/chapters/*.md"))
    total_recovered = 0
    total_files = 0

    for f in files:
        current = open(f, encoding="utf-8").read()
        current_blocks = QUIZ_SPLIT.split(current)
        corrupted_indices = [i for i in range(1, len(current_blocks)) if is_corrupted(current_blocks[i])]
        if not corrupted_indices:
            continue

        gitpath = f.replace("\\", "/")
        head = subprocess.run(
            ["git", "show", f"HEAD:{gitpath}"], capture_output=True, text=True, encoding="utf-8", check=True
        ).stdout
        head_blocks = QUIZ_SPLIT.split(head)
        if len(head_blocks) != len(current_blocks):
            raise AssertionError(f"disallineamento blocchi HEAD/attuale in {f}")

        recovered_in_file = 0
        for i in corrupted_indices:
            target_letter_match = ANSWER_RE.search(current_blocks[i])
            if not target_letter_match:
                raise AssertionError(f"nessuna lettera target leggibile in {f} blocco {i}")
            target_letter = target_letter_match.group(1)

            clean_block = typo.fix_body(head_blocks[i])
            new_block = rebuild_quiz(clean_block, target_letter)
            current_blocks[i] = new_block
            recovered_in_file += 1

        open(f, "w", encoding="utf-8", newline="\n").write("".join(current_blocks))
        total_recovered += recovered_in_file
        total_files += 1
        print(f"{f}: {recovered_in_file} quiz recuperati")

    print(f"\nTOTALE: {total_recovered} quiz recuperati in {total_files} file")


if __name__ == "__main__":
    main()
