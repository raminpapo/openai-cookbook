# File Documentation: run_17.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_17.py`
- **Size**: 787 bytes (787 characters)
- **Lines**: 26
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq

# Compile once for speed; ASCII-only tokens
_TOKEN_RE = re.compile(r'[A-Za-z0-9]+')

def _compute_top_k(src_text: str, k: int):
    # k <= 0 yields empty result
    if not isinstance(k, int) or k <= 0:
        return []

    counts = {}
    # One pass: iterate matches without building an intermediate list
    for m in _TOKEN_RE.finditer(src_text):
        tok = m.group(0).lower()  # lowercase per token
        counts[tok] = counts.get(tok, 0) + 1

    if not counts:
        return []

    top_n = k if k < len(counts) else len(counts)
    # Sort by count desc, then token asc using a key on (-count, token)
    return heapq.nsmallest(top_n, counts.items(), key=lambda kv: (-kv[1], kv[0]))

# Expose the requested global result
top_k = _compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `_compute_top_k(src_text: str, k: int)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_17.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_17.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_17.py`*
