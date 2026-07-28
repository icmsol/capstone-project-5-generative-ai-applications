#!/usr/bin/env python3
"""Extract FAR Part 52.2 records from the frozen FAC 2026-01 PDF.

Requires Poppler's pdftotext command. The modeling notebook consumes the
versioned CSV produced by this script; the frozen PDF and checksum are retained
for source verification.
"""
from __future__ import annotations
import argparse
import re
import subprocess
from pathlib import Path
from bisect import bisect_left
import pandas as pd

HEADER_RE = re.compile(r"(?m)^(52\.\d+(?:-\d+)?)\s+([^\n]+)$")

def number_key(number: str) -> tuple[int, int]:
    rest = number.split(".", 1)[1]
    if "-" in rest:
        base, suffix = rest.split("-", 1)
        return int(base), int(suffix)
    return int(rest), -1

def clean_body(body: str) -> str:
    output = []
    for raw in body.replace("\f", "\n").splitlines():
        line = raw.strip()
        if not line:
            output.append("")
            continue
        if "FEDERAL ACQUISITION REGULATION" in line and re.search(r"52\.\d", line):
            continue
        if line.startswith("SUBPART 52.2 - TEXT OF PROVISIONS AND CLAUSES"):
            continue
        if line in {"This page intentionally left blank.",
                    "Subpart 52.2 - Text of Provisions and Clauses"}:
            continue
        if re.fullmatch(r"52\.2-\d+", line):
            continue
        output.append(line)
    cleaned, previous_blank = [], False
    for line in output:
        is_blank = line == ""
        if not (is_blank and previous_blank):
            cleaned.append(line)
        previous_blank = is_blank
    return "\n".join(cleaned).strip()

def longest_increasing_headers(candidates):
    keys = [number_key(item[0]) for item in candidates]
    tails, tail_indices = [], []
    previous = [-1] * len(keys)
    for i, key in enumerate(keys):
        position = bisect_left(tails, key)
        if position == len(tails):
            tails.append(key)
            tail_indices.append(i)
        else:
            tails[position] = key
            tail_indices[position] = i
        if position > 0:
            previous[i] = tail_indices[position - 1]
    index = tail_indices[-1]
    chosen = []
    while index != -1:
        chosen.append(candidates[index])
        index = previous[index]
    return list(reversed(chosen))

def extract(pdf_path: Path, output_csv: Path) -> None:
    text_path = output_csv.with_suffix(".pdftotext.tmp")
    subprocess.run(["pdftotext", "-layout", str(pdf_path), str(text_path)], check=True)
    pages = text_path.read_text(encoding="utf-8", errors="replace").split("\f")
    part_text = "\f".join(pages[1436:2008])

    candidates = []
    for match in HEADER_RE.finditer(part_text):
        number, title = match.group(1), match.group(2).strip()
        if re.fullmatch(r"52\.2-\d+", number):
            continue
        if title == "FEDERAL ACQUISITION REGULATION" or title.startswith("SUBPART "):
            continue
        if number_key(number) <= (253, 1):
            candidates.append((number, title, match.start()))

    part_52_3_boundary = re.search(
        r"(?m)^SUBPART 52\.3 - PROVISION AND CLAUSE MATRIX\b", part_text
    )
    part_52_2_end = (
        part_52_3_boundary.start()
        if part_52_3_boundary
        else len(part_text)
    )

    selected = longest_increasing_headers(candidates)
    rows = []
    for i, (number, _, start) in enumerate(selected):
        end = selected[i + 1][2] if i + 1 < len(selected) else part_52_2_end
        lines = part_text[start:end].splitlines()
        title = lines[0][len(number):].strip()
        title_lines = 1
        while title != "[Reserved]" and not title.endswith("."):
            next_line = lines[title_lines].strip()
            if not next_line or next_line.startswith("As prescribed"):
                break
            title += " " + next_line
            title_lines += 1
        body = clean_body("\n".join(lines[title_lines:]))
        reserved = "[Reserved]" in title
        if reserved or number == "52.200":
            continue
        text = f"{title}\n{body}".strip()
        rows.append({
            "record_id": f"FAR52_{len(rows)+1:04d}",
            "clause_number": number,
            "title": title,
            "family": number.split(".")[1].split("-")[0],
            "word_count": len(re.findall(r"\b[\w’'-]+\b", text)),
            "char_count": len(text),
            "text": text,
        })
    pd.DataFrame(rows).to_csv(output_csv, index=False, encoding="utf-8")
    text_path.unlink(missing_ok=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    extract(args.pdf, args.output_csv)
