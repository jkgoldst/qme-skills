#!/usr/bin/env python3
"""Check every GAF / WPI pair in a QME draft against the 2005 PDRS table.

Usage: python3 gaf_wpi_check.py DRAFT   (DRAFT is .docx, .txt, or .md)
Stdlib only. Prints the findings memo to stdout.
"""
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

CITATION = ("2005 Schedule for Rating Permanent Disabilities, Section 1, "
            "GAF-to-WPI conversion table, p. 1-16")

GAF_TO_WPI = {
    1: 90, 2: 89, 3: 89, 4: 88, 5: 87, 6: 87, 7: 86, 8: 85, 9: 84, 10: 84,
    11: 83, 12: 82, 13: 82, 14: 81, 15: 80, 16: 80, 17: 79, 18: 78, 19: 78, 20: 77,
    21: 76, 22: 76, 23: 75, 24: 74, 25: 73, 26: 73, 27: 72, 28: 71, 29: 71, 30: 70,
    31: 69, 32: 67, 33: 65, 34: 63, 35: 61, 36: 59, 37: 57, 38: 55, 39: 53, 40: 51,
    41: 48, 42: 46, 43: 44, 44: 42, 45: 40, 46: 38, 47: 36, 48: 34, 49: 32, 50: 30,
    51: 29, 52: 27, 53: 26, 54: 24, 55: 23, 56: 21, 57: 20, 58: 18, 59: 17, 60: 15,
    61: 14, 62: 12, 63: 11, 64: 9, 65: 8, 66: 6, 67: 5, 68: 3, 69: 2, 70: 0,
}
for _g in range(71, 101):
    GAF_TO_WPI[_g] = 0
assert len(GAF_TO_WPI) == 100

IN_SCOPE = ("IMPAIRMENT", "DIAGNOSIS", "DISCUSSION", "DISABILITY", "CONCLUSION", "SUMMARY")
BOUNDARY_SCORES = (68, 69, 70, 71, 72)
PAIR_REACH_SENTENCES = 3

GAF_RE = re.compile(
    r"\b(?:Global\s+Assessment\s+of\s+Functioning\s*(?:\(GAF\))?|GAF)\s+"
    r"(?:score\s+of\s+|score\s+|rating\s+of\s+|of\s+)(\d{1,3})\b",
    re.IGNORECASE,
)
WPI_RE = re.compile(
    r"(?:Whole\s+Person\s+Impairment|WPI)[^.%\n]{0,60}?"
    r"(\d{1,3}(?:\.\d+)?)\s*(?:[-–]\s*(\d{1,3}(?:\.\d+)?))?\s*(?:%|percent)",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(r"\[PHYSICIAN:[^\]]*\]", re.IGNORECASE)
HEADING_RE = re.compile(r"^\s*(?:=+\s*)?(?:#+\s*)?([A-Z][A-Z0-9 ,/&()':.-]{3,}?)(?:\s*\(\d+ words\))?\s*(?:=+)?\s*$")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
ABBREV_RE = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|M\.D|Ph\.D|No|vs|approx)\.$", re.IGNORECASE)


def read_draft(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf8", "ignore")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return path.read_text(errors="ignore")


def split_sections(text: str):
    sections, name, buf = [], "DRAFT", []
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m and line.strip().upper() == line.strip() and len(line.strip()) < 90:
            if buf:
                sections.append((name, "\n".join(buf)))
            name, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if buf:
        sections.append((name, "\n".join(buf)))
    return sections


def in_scope(name: str) -> bool:
    return name == "DRAFT" or any(k in name.upper() for k in IN_SCOPE)


def sentences(content: str):
    content = PLACEHOLDER_RE.sub(" ", content).replace("\n", " ")
    out = []
    for piece in SENTENCE_RE.split(content):
        piece = piece.strip()
        if not piece:
            continue
        if out and ABBREV_RE.search(out[-1]):
            out[-1] = out[-1] + " " + piece
        else:
            out.append(piece)
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    path = Path(argv[1])
    secs = split_sections(read_draft(path))
    findings, consistent, unchecked = [], [], []
    seen_unchecked = set()
    pending = []  # (kind, section, sentence, gaf, wpi_lo, wpi_hi)
    paired_gafs, paired_wpis = set(), set()

    for name, content in secs:
        sents = sentences(content)
        gafs, wpis = [], []
        for i, s in enumerate(sents):
            gm = GAF_RE.findall(s)
            if len(gm) > 1:
                if (name, s) not in seen_unchecked:
                    seen_unchecked.add((name, s))
                    unchecked.append((name, s, "two GAF scores in one sentence"))
            elif len(gm) == 1 and 1 <= int(gm[0]) <= 100:
                gafs.append((i, int(gm[0]), s))
            for wm in WPI_RE.finditer(s):
                lo = float(wm.group(1))
                hi = float(wm.group(2)) if wm.group(2) else lo
                wpis.append((i, min(lo, hi), max(lo, hi), s))
        if not in_scope(name):
            for i, s in [(i, s) for i, _, s in gafs] + [(i, s) for i, _, _, s in wpis]:
                if (name, s) not in seen_unchecked:
                    seen_unchecked.add((name, s))
                    unchecked.append((name, s, "outside the rated sections; another evaluator's score"))
            continue

        used_w, used_g = set(), set()
        # same-sentence pairs first, then nearest within reach
        for pass_reach in (0, PAIR_REACH_SENTENCES):
            for gi_idx, (gi, g, gs) in enumerate(gafs):
                if gi_idx in used_g:
                    continue
                partner = None
                for wi, (i, lo, hi, ws) in enumerate(wpis):
                    if wi in used_w or abs(i - gi) > pass_reach:
                        continue
                    if partner is None or abs(i - gi) < abs(wpis[partner][0] - gi):
                        partner = wi
                if partner is None:
                    continue
                used_w.add(partner)
                used_g.add(gi_idx)
                i, lo, hi, ws = wpis[partner]
                expected = GAF_TO_WPI[g]
                quote = gs if ws == gs else f"{gs} [...] {ws}"
                stated = f"{lo:g}%" if lo == hi else f"{lo:g}-{hi:g}%"
                paired_gafs.add(g)
                paired_wpis.add((lo, hi))
                if lo <= expected <= hi:
                    consistent.append((name, g, stated, expected))
                else:
                    findings.append(("MISMATCH", name, quote,
                                     f"Stated: GAF {g}, WPI {stated}. Table: GAF {g} converts to {expected}% WPI."))
        boundary_seen = set()
        for gi_idx, (gi, g, gs) in enumerate(gafs):
            if g in BOUNDARY_SCORES and (name, g) not in boundary_seen:
                boundary_seen.add((name, g))
                nb = " and ".join(f"GAF {n} to {GAF_TO_WPI[n]}%" for n in (g - 1, g + 1) if n in GAF_TO_WPI)
                findings.append(("BOUNDARY", name, gs,
                                 f"Stated: GAF {g}, which converts to {GAF_TO_WPI[g]}%. One point of change gives {nb}. Confirm {g} is the intended score."))
            if gi_idx not in used_g:
                pending.append(("GAF", name, gs, g, None, None))
        for wi, (i, lo, hi, ws) in enumerate(wpis):
            if wi not in used_w:
                pending.append(("WPI", name, ws, None, lo, hi))

    # a lone score that restates a pair made elsewhere is a restatement, not an orphan
    for kind, name, s, g, lo, hi in pending:
        if kind == "GAF":
            if g in paired_gafs:
                consistent.append((name, g, "restated, no WPI", GAF_TO_WPI[g]))
            else:
                findings.append(("ORPHAN", name, s, f"GAF {g} stated with no WPI within reach; table value {GAF_TO_WPI[g]}%."))
        else:
            stated = f"{lo:g}%" if lo == hi else f"{lo:g}-{hi:g}%"
            if (lo, hi) in paired_wpis:
                consistent.append((name, "restated, no GAF", stated, "n/a"))
            else:
                findings.append(("ORPHAN", name, s, f"WPI {stated} stated with no GAF within reach."))

    if not findings and not consistent and not unchecked:
        print("No GAF or WPI stated; nothing to check.")
        return 0

    print(f"# GAF to WPI check: {path.name}\n")
    print(f"Checked {date.today().isoformat()} against the {CITATION}. Lookup by script (gaf_wpi_check.py).\n")
    print("## Findings\n")
    if not findings:
        print("None.\n")
    for n, (kind, sec, quote, detail) in enumerate(findings, 1):
        print(f"### {n}. {kind}, {sec}\n\n> \"{quote}\"\n\n{detail}\n")
    print("## Pairs checked and consistent\n")
    for sec, g, stated, expected in consistent:
        if expected == "n/a":
            print(f"- {sec}: WPI {stated} ({g}).")
        elif stated.startswith("restated"):
            print(f"- {sec}: GAF {g} ({stated}); table {expected}%.")
        else:
            print(f"- {sec}: GAF {g}, WPI {stated}; table {expected}%.")
    if not consistent:
        print("- none")
    print("\n## Not checked\n")
    for sec, s, why in unchecked:
        print(f"- {sec}: \"{s}\" ({why}).")
    if not unchecked:
        print("- none")
    kinds = {k: sum(1 for f in findings if f[0] == k) for k in ("MISMATCH", "BOUNDARY", "ORPHAN")}
    print(f"\n## Count\n\n{len(findings)} finding{"" if len(findings) == 1 else "s"} ({kinds['MISMATCH']} mismatch, {kinds['BOUNDARY']} boundary, "
          f"{kinds['ORPHAN']} orphan); {len(consistent)} pairs consistent; {len(unchecked)} mentions not checked.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
