# File Documentation: run_18.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_18.py`
- **Size**: 715 bytes (715 characters)
- **Lines**: 22
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from heapq import nsmallest

# Token generator: ASCII [a-z0-9]+, lowercased, streaming via re.finditer
def _iter_tokens_ascii_lower(s: str):
    for m in re.finditer(r'[A-Za-z0-9]+', s):
        yield m.group(0).lower()

def _compute_top_k(s: str, k: int):
    if not s or k <= 0:
        return []
    counts = {}
    for tok in _iter_tokens_ascii_lower(s):
        counts[tok] = counts.get(tok, 0) + 1
    if not counts:
        return []
    kk = k if k < len(counts) else len(counts)
    # Select and sort by count desc, then token asc
    return [(t, c) for t, c in nsmallest(kk, counts.items(), key=lambda it: (-it[1], it[0]))]

# Expose result as a convenient global
top_k = _compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_tokens_ascii_lower(s: str)`
- `_compute_top_k(s: str, k: int)`

### Dependencies/Imports

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_18.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_18.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_18.py`*
