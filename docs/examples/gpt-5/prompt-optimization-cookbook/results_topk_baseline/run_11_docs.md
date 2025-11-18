# File Documentation: run_11.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_11.py`
- **Size**: 1,087 bytes (1,087 characters)
- **Lines**: 36
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq

def _compute_top_k(text, k):
    # Tokens: ASCII [A-Za-z0-9]+, lowercased; others are separators.
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    try:
        k = int(k)
    except Exception:
        k = 0
    if k <= 0 or not text:
        return []

    counts = {}
    # Iterate matches without lowercasing the entire text to keep memory low.
    pattern = re.compile(r'[A-Za-z0-9]+', flags=re.ASCII)
    for m in pattern.finditer(text):
        tok = m.group(0).lower()
        counts[tok] = counts.get(tok, 0) + 1

    if not counts:
        return []

    n_unique = len(counts)
    kk = k if k < n_unique else n_unique
    if kk == 0:
        return []

    # Use a heap to avoid sorting the entire map when k << unique tokens.
    # Key: (-count, token) gives count desc, then token asc.
    top = heapq.nsmallest(kk, counts.items(), key=lambda it: (-it[1], it[0]))
    return top

# Expect globals 'text' and 'k'; define top_k for inspection.
top_k = _compute_top_k(globals().get('text', ''), globals().get('k', 0))
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `_compute_top_k(text, k)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_11.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_11.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_11.py`*
