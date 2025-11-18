# File Documentation: run_12.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_12.py`
- **Size**: 744 bytes (744 characters)
- **Lines**: 29
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from collections import Counter
from heapq import nsmallest

def _compute_top_k(text: str, k: int):
    # Tokens: ASCII [a-z0-9]+ after lowercasing
    pat = re.compile(r'[A-Za-z0-9]+', flags=re.ASCII)
    freq = Counter()
    for m in pat.finditer(text):
        freq[m.group(0).lower()] += 1

    items = list(freq.items())
    if not items:
        return []

    t = max(0, min(int(k), len(items)))
    if t == 0:
        return []

    key = lambda it: (-it[1], it[0])  # count desc, token asc
    if t < len(items):
        return nsmallest(t, items, key=key)
    return sorted(items, key=key)

try:
    top_k = _compute_top_k(text, k)
except NameError:
    # If text or k are not defined, expose an empty result.
    top_k = []
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `_compute_top_k(text: str, k: int)`

### Dependencies/Imports

- `collections`
- `heapq`
- `re`

---

## Performance & Security Notes

- Ensure proper error handling is implemented
- Review for potential security vulnerabilities (SQL injection, XSS, etc.)
- Consider performance implications of loops and recursive functions

---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

```bash
# Run this file
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_12.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_12.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_12.py`*
