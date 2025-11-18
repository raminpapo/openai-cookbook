# File Documentation: run_23.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_23.py`
- **Size**: 1,201 bytes (1,201 characters)
- **Lines**: 43
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import heapq

def _iter_tokens_ascii_lower(s):
    # Stream tokens: ASCII [a-z0-9]+, lowercase letters; non-matching chars are separators.
    buf = []
    append = buf.append
    for ch in s:
        o = ord(ch)
        if 65 <= o <= 90:           # 'A'-'Z' -> lower
            append(chr(o + 32))
        elif 97 <= o <= 122 or 48 <= o <= 57:  # 'a'-'z' or '0'-'9'
            append(ch)
        else:
            if buf:
                yield ''.join(buf)
                buf.clear()
    if buf:
        yield ''.join(buf)

def _top_k_tokens(s, k):
    if not s or k <= 0:
        return []
    counts = {}
    for tok in _iter_tokens_ascii_lower(s):
        counts[tok] = counts.get(tok, 0) + 1
    if not counts:
        return []
    m = k if k < len(counts) else len(counts)
    # Sort by count desc, then token asc -> key (-count, token); nsmallest returns sorted ascending by key.
    return heapq.nsmallest(m, counts.items(), key=lambda it: (-it[1], it[0]))

# Use provided globals `text` and `k`; fall back to empty values if missing.
try:
    _text, _k = text, k
except NameError:
    _text, _k = "", 0

try:
    _k = int(_k)
except Exception:
    _k = 0

top_k = _top_k_tokens(_text, _k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_tokens_ascii_lower(s)`
- `_top_k_tokens(s, k)`

### Dependencies/Imports

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_23.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_23.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_23.py`*
