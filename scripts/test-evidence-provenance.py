"""Replay the real scoring symptom against explicit provenance fixtures."""
from pathlib import Path
import json, subprocess, sys, unittest
root=Path(__file__).resolve().parents[1]
class ProvenanceScoring(unittest.TestCase):
 def test_calibration(self):
  for case in sorted((root/'evals/qme-env-audit/provenance-regression').glob('*.json')):
   with self.subTest(case=case.name):
    expected=json.loads(case.read_text())['expected_exit']
    result=subprocess.run([sys.executable,str(root/'scripts/check-evidence-provenance.py'),'--case',str(case)],capture_output=True,text=True)
    self.assertEqual(expected,result.returncode,result.stdout+result.stderr)
if __name__=='__main__':unittest.main()
