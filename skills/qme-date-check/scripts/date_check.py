#!/usr/bin/env python3
"""Date arithmetic checks for a QME draft. Standard library only.

Usage: python3 date_check.py DRAFT [--today YYYY-MM-DD] [--json]

DRAFT is a .txt/.md file or a .docx (python-docx if installed, else zip
fallback). Prints a findings table. Exit code 0 always; findings are for
the physician, not a build gate.
"""
import json
import re
import sys
import zipfile
from collections import defaultdict
from datetime import date
from typing import Dict, List, Optional, Tuple

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}
MONTHS.update({k[:3]: v for k, v in list(MONTHS.items())})
MONTHS["sept"] = 9
MONTH_RE = r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
FULL_DATE_RE = re.compile(
    rf"\b({MONTH_RE})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+((?:19|20)\d{{2}})\b|\b(\d{{1,2}})/(\d{{1,2}})/((?:19|20)?\d{{2}})\b",
    re.IGNORECASE)
MONTH_YEAR_RE = re.compile(rf"\b({MONTH_RE})\.?\s+((?:19|20)\d{{2}})\b", re.IGNORECASE)
YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\b")
AGE_RE = re.compile(r"\b(?:Mr|Ms|Mrs|Dr)\.?\s+[A-Z][\w'-]+\s+is\s+(?:a|an)\s+(\d{2})[- ]year[- ]old\b|\b(\d{2})[- ]year[- ]old\s+(?:woman|man|female|male|applicant|evaluee|patient|worker)\b|\bDOB:[^\n]*?\((\d{2})\)", re.IGNORECASE)
DOB_RE = re.compile(r"(?:DOB|date of birth)\s*:?\s*(?:is\s+)?([^\n.;]+)", re.IGNORECASE)
EVAL_DATE_RE = re.compile(r"date of (?:re-?)?evaluation\s*:?\s*([^\n]+)", re.IGNORECASE)
DOI_RE = re.compile(r"date of injury\s*(?:is|was|:)?\s*(?:on\s+)?([^\n.;]{4,40})", re.IGNORECASE)
DOI_SENTENCE_RE = re.compile(r"(?:injur(?:y|ed)|incident|accident)[^.\n]{0,80}?\bon\s+([^.\n]{4,30}\d{4})", re.IGNORECASE)
LDW_RE = re.compile(r"last (?:day (?:of )?work(?:ed)?|worked|date worked|day on the job)\s*(?:was|is|:|on)?\s*(?:on\s+)?([^.\n;]{4,40})", re.IGNORECASE)
DATE_TOKEN = rf"(?:{MONTH_RE}\.?\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}|\d{{1,2}}/\d{{1,2}}/\d{{2,4}})"
TERM_RE = re.compile(rf"(?:terminated|separated|resigned|laid off|stopped working|left (?:her|his|their) (?:job|employment|position)|went off work|has not worked since|last worked)[^.\n]{{0,60}}?({DATE_TOKEN})", re.IGNORECASE)
TTD_RE = re.compile(rf"(?:temporar(?:il)?y (?:total(?:ly)?|partial(?:ly)?) disab\w+|TTD|TPD)[^.\n]{{0,80}}?(?:from|since|beginning|as of|starting|effective)\s+({DATE_TOKEN})", re.IGNORECASE)
DURATION_RE = re.compile(r"\b(?:for|over)\s+(?:the (?:past|last)\s+)?(\d{1,2}|[a-z]+)\s+years?\b[^.\n]{0,40}?\b(?:since|from|beginning(?: in)?)\s+((?:19|20)\d{2})\b|\b(?:since|from|beginning(?: in)?)\s+((?:19|20)\d{2})\b[^.\n]{0,40}?\b(?:for|over)\s+(?:the (?:past|last)\s+)?(\d{1,2}|[a-z]+)\s+years?\b", re.IGNORECASE)
RELATIVE_RE = re.compile(r"\b(?:after|before|since|following|prior to|until|from|through|between)\b", re.IGNORECASE)
WORD_NUMS = {w: i for i, w in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"])}

HEADER_RE = re.compile(r"^\s*(?:=+\s*)?([A-Z][A-Z0-9 ,'&/()\-\.]{3,}?)(?:\s+as (?:reported|described) by [^=]*?)?(?:\s*\(\d+ words\))?\s*:?\s*(?:=+)?\s*$")
IDENTIFYING = ("IDENTIFYING DATA", "IDENTIFYING INFORMATION")
DOI_HOME_SECTIONS = ("IDENTIFYING DATA", "HISTORY OF INJURY", "REVIEW OF RECORDS", "DISCUSSION", "CAUSATION", "DISABILITY", "IMPAIRMENT", "APPORTIONMENT", "OCCUPATIONAL HISTORY", "CURRENT COMPLAINTS", "SUMMARY", "DIAGNOS", "DECLARATION", "BILLING", "PRIOR INDUSTRIAL")
TERMINATION_SECTIONS = ("IDENTIFYING DATA", "HISTORY OF INJURY", "OCCUPATIONAL HISTORY", "DISABILITY", "DISCUSSION", "CURRENT COMPLAINTS", "SOCIAL HISTORY")


def read_draft(path: str) -> str:
    if path.lower().endswith(".docx"):
        try:
            import docx  # type: ignore
            return "\n".join(p.text for p in docx.Document(path).paragraphs)
        except ImportError:
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml").decode("utf8", "ignore")
            xml = re.sub(r"</w:p>", "\n", xml)
            return re.sub(r"<[^>]+>", "", xml)
    with open(path, encoding="utf8", errors="ignore") as f:
        return f.read()


def split_sections(text: str) -> List[Tuple[str, str]]:
    sections: List[Tuple[str, List[str]]] = [("FRONT MATTER", [])]
    for line in text.splitlines():
        m = HEADER_RE.match(line)
        stripped = line.strip()
        if m and stripped and stripped.upper() == stripped and not FULL_DATE_RE.search(stripped) and len(stripped) < 90:
            sections.append((m.group(1).strip().rstrip(":"), []))
        else:
            sections[-1][1].append(line)
    return [(h, "\n".join(b)) for h, b in sections]


def parse_full_date(s: str) -> Optional[date]:
    m = FULL_DATE_RE.search(s)
    if not m:
        return None
    try:
        if m.group(1):
            mon = MONTHS[m.group(1).lower().rstrip(".")[:4] if m.group(1).lower().startswith("sept") else m.group(1).lower()[:3]]
            return date(int(m.group(3)), mon, int(m.group(2)))
        y = int(m.group(6))
        y = y + (2000 if y < 50 else 1900) if y < 100 else y
        return date(y, int(m.group(4)), int(m.group(5)))
    except (ValueError, KeyError):
        return None


def all_full_dates(text: str) -> List[Tuple[date, str]]:
    out = []
    for m in FULL_DATE_RE.finditer(text):
        d = parse_full_date(m.group(0))
        if d:
            out.append((d, excerpt(text, m.start(), m.end())))
    return out


def excerpt(text: str, start: int, end: int, width: int = 70) -> str:
    a = max(0, start - width)
    b = min(len(text), end + width)
    return ("..." if a else "") + text[a:b].replace("\n", " ").strip() + ("..." if b < len(text) else "")


ABBREV_RE = re.compile(r"\b(?:Mr|Ms|Mrs|Dr|Jr|Sr|St|vs|No|Inc|Ltd|[A-Z])\.$")


def _is_abbrev_period(text: str, i: int) -> bool:
    """True when the period at text[i] ends an honorific or initial, not a sentence."""
    return bool(ABBREV_RE.search(text[max(0, i - 4):i + 1]))


def sentence_around(text: str, pos: int) -> str:
    a = text.rfind(".", 0, pos)
    while a >= 0 and _is_abbrev_period(text, a):
        a = text.rfind(".", 0, a)
    a = max(a, text.rfind("\n", 0, pos)) + 1
    b = text.find(".", pos)
    while b >= 0 and _is_abbrev_period(text, b):
        b = text.find(".", b + 1)
    b = len(text) if b < 0 else b + 1
    return text[a:b].strip()


class Finding(dict):
    pass


def finding(check: str, what: str, a_sec: str, a_txt: str, b_sec: str = "", b_txt: str = "") -> Finding:
    return Finding(check=check, finding=what, location_a=a_sec, quote_a=a_txt, location_b=b_sec, quote_b=b_txt)


def first_in(sections, names, regex):
    for h, body in sections:
        if any(n in h.upper() for n in names):
            m = regex.search(body)
            if m:
                return h, m
    return None, None


def canonical_date(sections, names, regex):
    h, m = first_in(sections, names, regex)
    if m:
        d = parse_full_date(m.group(1))
        if d:
            return h, d, sentence_around(sections[[s[0] for s in sections].index(h)][1], m.start())
    return None, None, None


def check_same_fact(sections, label, names, regex, check_id) -> List[Finding]:
    out = []
    home, canon, canon_sent = canonical_date(sections, names, regex)
    if not canon:
        return out
    for h, body in sections:
        if h == home:
            continue
        for m in regex.finditer(body):
            d = parse_full_date(m.group(1))
            if d and d != canon:
                out.append(finding(check_id, f"{label} stated two ways: {canon} and {d}.", home, canon_sent, h, sentence_around(body, m.start())))
    return out


def check_month_year_collision(sections) -> List[Finding]:
    out, seen = [], defaultdict(list)
    for h, body in sections:
        for d, ex in all_full_dates(body):
            seen[(d.month, d.day)].append((d.year, h, ex))
    for (mo, da), hits in seen.items():
        years = sorted({y for y, _, _ in hits})
        for y1, y2 in zip(years, years[1:]):
            if y2 - y1 == 1:
                a = next(x for x in hits if x[0] == y1)
                b = next(x for x in hits if x[0] == y2)
                if a[1] != b[1]:
                    out.append(finding("f6_month_year_collision", f"Same month and day in adjacent years: {mo}/{da}/{y1} and {mo}/{da}/{y2}.", a[1], a[2], b[1], b[2]))
    return out


def check_age(sections, text, today: date) -> List[Finding]:
    out = []
    dob = None
    m = DOB_RE.search(text)
    if m:
        dob = parse_full_date(m.group(1))
    ev = None
    m = EVAL_DATE_RE.search(text)
    if m:
        ev = parse_full_date(m.group(1))
    ref = ev or today
    ages = []
    for h, body in sections:
        for m in AGE_RE.finditer(body):
            age = int(next(g for g in m.groups() if g))
            ages.append((age, h, sentence_around(body, m.start())))
    if dob and ages:
        expected = ref.year - dob.year - ((ref.month, ref.day) < (dob.month, dob.day))
        for age, h, sent in ages:
            if abs(age - expected) > 1:
                out.append(finding("f6_age_year_math", f"Age {age} stated; DOB {dob} gives {expected} as of {ref}.", h, sent, "DOB", m.group(0) if (m := DOB_RE.search(text)) else ""))
    distinct = sorted({a for a, _, _ in ages})
    if len(distinct) > 1 and distinct[-1] - distinct[0] > 1:
        lo = next(x for x in ages if x[0] == distinct[0])
        hi = next(x for x in ages if x[0] == distinct[-1])
        out.append(finding("f6_age_year_math", f"Age stated as both {lo[0]} and {hi[0]}.", lo[1], lo[2], hi[1], hi[2]))
    for h, body in sections:
        for m in DURATION_RE.finditer(body):
            n = m.group(1) or m.group(4)
            y = int(m.group(2) or m.group(3))
            n = int(n) if n.isdigit() else WORD_NUMS.get(n.lower())
            if n is None:
                continue
            if abs((ref.year - y) - n) > 1:
                out.append(finding("f6_age_year_math", f"'{n} years' since {y} does not match {ref.year - y} years as of {ref.year}.", h, sentence_around(body, m.start())))
    return out


def check_anchor_year_offset(sections, anchors) -> List[Finding]:
    out = []
    for label, (home, canon, sent) in anchors.items():
        if not canon:
            continue
        for h, body in sections:
            for d, ex in all_full_dates(body):
                if d.month == canon.month and d.day == canon.day and d.year != canon.year:
                    out.append(finding("f6_anchor_year_offset", f"{d} shares month and day with the {label} {canon} but the year differs.", home, sent, h, ex))
    return out


def check_doi_routing(sections, doi) -> List[Finding]:
    out = []
    home, canon, _ = doi
    if not canon:
        return out
    for h, body in sections:
        if any(n in h.upper() for n in DOI_HOME_SECTIONS) or h == "FRONT MATTER":
            continue
        for m in FULL_DATE_RE.finditer(body):
            if parse_full_date(m.group(0)) == canon:
                sent = sentence_around(body, m.start())
                if not RELATIVE_RE.search(sent[: max(0, sent.find(m.group(0)))]):
                    out.append(finding("f6_doi_section_routing", f"Date of injury {canon} restated in {h}.", h, sent))
    return out


def check_ttd(sections, ldw) -> List[Finding]:
    out = []
    home, canon, sent = ldw
    if not canon:
        for h, body in sections:
            m = TERM_RE.search(body)
            if m:
                canon = parse_full_date(m.group(1)); home = h; sent = sentence_around(body, m.start()); break
    if not canon:
        return out
    for h, body in sections:
        for m in TTD_RE.finditer(body):
            d = parse_full_date(m.group(1))
            if d and d < canon:
                out.append(finding("f6_ttd_predates_ldw", f"Disability begins {d}, before the last day worked {canon}.", h, sentence_around(body, m.start()), home, sent))
    return out


def check_termination_spread(sections) -> List[Finding]:
    hits = []
    for h, body in sections:
        if not any(n in h.upper() for n in TERMINATION_SECTIONS):
            continue
        for m in TERM_RE.finditer(body):
            d = parse_full_date(m.group(1))
            if d:
                hits.append((d, h, sentence_around(body, m.start())))
    out = []
    if len(hits) > 1:
        lo, hi = min(hits), max(hits)
        if (hi[0] - lo[0]).days > 7 and lo[1] != hi[1]:
            out.append(finding("f6_termination_date_spread", f"Last-worked or termination dates {(hi[0] - lo[0]).days} days apart: {lo[0]} and {hi[0]}.", lo[1], lo[2], hi[1], hi[2]))
    return out


def check_future(sections, today: date) -> List[Finding]:
    out = []
    for h, body in sections:
        for d, ex in all_full_dates(body):
            if d > today:
                out.append(finding("f6_future_year", f"{d} is after today ({today}).", h, ex))
        spans = [(m.start(), m.end()) for m in FULL_DATE_RE.finditer(body)]
        for m in YEAR_RE.finditer(body):
            if int(m.group(1)) > today.year and not any(a <= m.start() < b for a, b in spans):
                out.append(finding("f6_future_year", f"Year {m.group(1)} is after today ({today}).", h, sentence_around(body, m.start())))
    return out



def run(text: str, today: date) -> List[Finding]:
    sections = split_sections(text)
    doi = canonical_date(sections, IDENTIFYING, DOI_RE)
    if not doi[1]:
        doi = canonical_date(sections, IDENTIFYING, DOI_SENTENCE_RE)
    ldw = canonical_date(sections, IDENTIFYING, LDW_RE)
    findings: List[Finding] = []
    findings += check_same_fact(sections, "Date of injury", IDENTIFYING, DOI_RE, "f1_doi")
    findings += check_same_fact(sections, "Last day worked", IDENTIFYING, LDW_RE, "f1_last_day_worked")
    findings += check_month_year_collision(sections)
    findings += check_age(sections, text, today)
    findings += check_anchor_year_offset(sections, {"date of injury": doi, "last day worked": ldw})
    findings += check_doi_routing(sections, doi)
    findings += check_ttd(sections, ldw)
    findings += check_termination_spread(sections)
    findings += check_future(sections, today)
    seen, uniq = set(), []
    for f in findings:
        key = (f["check"], f["finding"], f["location_a"], f["location_b"])
        if key not in seen:
            seen.add(key); uniq.append(f)
    return uniq


def main(argv: List[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__); return 0
    today = date.today()
    as_json = "--json" in argv
    if "--today" in argv:
        today = date.fromisoformat(argv[argv.index("--today") + 1])
    text = read_draft(argv[1])
    findings = run(text, today)
    if as_json:
        print(json.dumps(findings, indent=2, default=str)); return 0
    print(f"Date check: {argv[1]}  (today = {today})")
    print(f"{len(findings)} finding(s)\n")
    if not findings:
        print("No date findings. This covers the ten checks listed in SKILL.md and nothing else.")
    for i, f in enumerate(findings, 1):
        print(f"{i}. [{f['check']}] {f['finding']}")
        print(f"   A: {f['location_a']}: \"{f['quote_a']}\"")
        if f["location_b"]:
            print(f"   B: {f['location_b']}: \"{f['quote_b']}\"")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
