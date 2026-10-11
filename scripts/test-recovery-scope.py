"""Calibrate a narrow detector against captured summary-scope failures."""
from pathlib import Path
import subprocess,sys,unittest
root=Path(__file__).resolve().parents[1]
class RecoveryScope(unittest.TestCase):
 def test_captured_cases(self):
  for case in sorted((root/'evals/qme-env-audit/recovery-scope-regression').glob('*.txt')):
   with self.subTest(case=case.name):
    expected=1 if case.stem in {'old-absence','compressed-absence','split-input-absence'} else 0
    r=subprocess.run([sys.executable,str(root/'scripts/check-recovery-scope.py'),str(case)],capture_output=True,text=True)
    self.assertEqual(expected,r.returncode,r.stdout+r.stderr)
if __name__=='__main__':unittest.main()
