"""Focused scorer calibration for C2 manifest evidence-register rows."""
import argparse, json, re
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--case',type=Path,required=True)
a=p.parse_args()
case=json.loads(a.case.read_text())
provenance=case.get('provenance')
if provenance not in {'description','excerpt'}:
 print('UNSCORED: ambiguous or missing input provenance');raise SystemExit(2)
rows=[r for r in case['report'].splitlines() if r.startswith('|') and 'manifest' in r.lower()]
if not rows:
 print('UNSCORED: no manifest row');raise SystemExit(2)
if provenance=='excerpt':
 print('PASS: supplied-excerpt label is not a description upgrade; other evidence fields require separate review');raise SystemExit(0)
if any(re.search(r'(?<![A-Z])VERIFIED(?![A-Z])',r) for r in rows):
 print('FAIL: description upgraded to VERIFIED');raise SystemExit(1)
print('PASS: no evidence upgrade');raise SystemExit(0)
