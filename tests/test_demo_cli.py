"""Tiny but real CLI smoke: execute the original demo and check its observable output.

This is deliberately *not* claimed as a complete regression or business test.
No dependency, network, account, or installed package beyond Python stdlib.
"""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo.py"


class DemoCliSmoke(unittest.TestCase):
    def test_demo_prints_the_documented_two_lines_without_error(self):
        with tempfile.TemporaryDirectory(prefix="my-training-qa-") as folder:
            env = os.environ.copy()
            env["PYTHONNOUSERSITE"] = "1"
            result = subprocess.run(
                [sys.executable, "-B", str(DEMO)],
                cwd=folder,
                env=env,
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout.splitlines(), ["Hello", "welcome"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
