# File Documentation: run_10.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_10.py`
- **Size**: 881 bytes (881 characters)
- **Lines**: 37
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from collections import Counter
import heapq

def _iter_tokens(s):
    # Stream tokens: lowercase ASCII [a-z0-9]+; others are separators
    buf = []
    append = buf.append
    for ch in s:
        c = ch.lower()
        if ('a' <= c <= 'z') or ('0' <= c <= '9'):
            append(c)
        elif buf:
            yield ''.join(buf)
            buf.clear()
    if buf:
        yield ''.join(buf)

def _compute_top_k(s, k):
    if not isinstance(k, int) or k <= 0:
        return []
    counts = Counter()
    for tok in _iter_tokens(s):
        counts[tok] += 1
    # Sort by count desc, then token asc
    return heapq.nsmallest(k, counts.items(), key=lambda kv: (-kv[1], kv[0]))

# Use provided globals; fall back to safe defaults if missing
try:
    _text = text
except NameError:
    _text = ""
try:
    _k = k
except NameError:
    _k = 0

top_k = _compute_top_k(_text, _k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_tokens(s)`
- `_compute_top_k(s, k)`

### Dependencies/Imports

- `collections`
- `heapq`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_10.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_10.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_10.py`*
