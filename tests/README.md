# Minimal offline CLI smoke

Run with the already available Python interpreter:

```powershell
py -3.12 -B tests/test_demo_cli.py
```

The test executes the repository's **actual** `demo.py`, then checks exit
status, stderr and the two produced output lines. It uses the Python standard
library only: no pip, network, browser, Docker or external service.

Scope is deliberately tiny because `demo.py` itself only prints two lines.
**A PASS verifies only this CLI smoke; it is not whole-project QA.**
Draft PR: an exact-HEAD Windows Runner execution is still required.
