# File Documentation: run_04.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_04.py`
- **Size**: 798 bytes (798 characters)
- **Lines**: 23
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq

def compute_top_k(s: str, k_value: int):
    # Count tokens: ASCII [A-Za-z0-9]+, case-insensitive, stored lowercase
    counts = {}
    for m in re.finditer(r'[A-Za-z0-9]+', s):
        tok = m.group(0).lower()
        counts[tok] = counts.get(tok, 0) + 1

    n = max(0, int(k_value))
    if n == 0 or not counts:
        return []

    # Sort by count desc, then token asc using a key tuple
    key = lambda item: (-item[1], item[0])
    # Use nsmallest with the composite key to avoid sorting the whole list when k << unique
    top_items = heapq.nsmallest(n, counts.items(), key=key)
    # Ensure exact order (nsmallest returns sorted by key already)
    return [(tok, cnt) for tok, cnt in top_items]

# Expect globals: text (str), k (int)
top_k = compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `compute_top_k(s: str, k_value: int)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_04.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_04.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_04.py`*
