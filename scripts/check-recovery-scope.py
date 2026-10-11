"""Focused symptom check; PASS means only this exact unsupported absence was not found."""
import argparse,re,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('report',type=Path);a=p.parse_args()
s=a.report.read_text()
pattern=re.compile(r'\bno recovery (?:or incident(?:-response)? )?runbooks?\b',re.I)
expanded=re.compile(r'recovery[^.\n]{0,220}(?:and (?:any )?incident response (?:currently )?rest on[^.\n]{0,80}undocumented capability|both[^.\n]{0,60}undocumented)',re.I)
hits=[line for line in s.splitlines() if pattern.search(line) or expanded.search(line)]
if hits:
 print('FAIL: recovery documentation absence asserted although only restore test and incident-response runbook are absent')
 for line in hits:print(line)
 sys.exit(1)
if not s.strip():print('UNSCORED: empty report');sys.exit(2)
print('PASS: targeted recovery-runbook expansion not found; other claims require review')
