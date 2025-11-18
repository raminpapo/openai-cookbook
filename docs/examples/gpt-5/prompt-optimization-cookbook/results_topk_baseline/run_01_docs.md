# File Documentation: run_01.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_01.py`
- **Size**: 806 bytes (806 characters)
- **Lines**: 34
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq

def compute_top_k(text: str, k: int):
    # Tokenize: lowercase, ASCII [a-z0-9]+; others are separators
    if not text or k <= 0:
        return []
    s = text.lower()
    pattern = re.compile(r'[a-z0-9]+', re.ASCII)

    counts = {}
    get = counts.get
    for m in pattern.finditer(s):
        t = m.group(0)
        counts[t] = get(t, 0) + 1

    n = min(k, len(counts))
    if n <= 0:
        return []
    # Sort by count desc, then token asc
    return heapq.nsmallest(n, counts.items(), key=lambda it: (-it[1], it[0]))

def _to_int(v):
    try:
        return int(v)
    except Exception:
        return 0

# Use provided globals; expose only top_k
_text = globals().get('text', '')
_k = _to_int(globals().get('k', 0))
top_k = compute_top_k(_text, _k)

__all__ = ['top_k']
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `compute_top_k(text: str, k: int)`
- `_to_int(v)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_01.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_01.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_01.py`*
