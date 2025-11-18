# File Documentation: run_21.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_21.py`
- **Size**: 717 bytes (717 characters)
- **Lines**: 24
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from collections import Counter
from heapq import nsmallest

def _iter_tokens(s):
    # Yield lowercase ASCII [a-z0-9]+ tokens; non-matching chars are separators
    pattern = re.compile(r"[a-z0-9]+", flags=re.ASCII | re.IGNORECASE)
    for m in pattern.finditer(s):
        yield m.group(0).lower()

def compute_top_k(s, k_value):
    k_int = int(k_value)
    if k_int <= 0:
        return []
    counts = Counter()
    for tok in _iter_tokens(s):
        counts[tok] += 1
    if not counts:
        return []
    # Sort by count desc, then token asc; take top k
    return nsmallest(k_int, counts.items(), key=lambda t: (-t[1], t[0]))

# Expose result as a convenient global
top_k = compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_tokens(s)`
- `compute_top_k(s, k_value)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_21.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_21.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_21.py`*
