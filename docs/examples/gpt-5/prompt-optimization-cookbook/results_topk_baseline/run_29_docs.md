# File Documentation: run_29.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_29.py`
- **Size**: 1,446 bytes (1,446 characters)
- **Lines**: 58
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import heapq

def _iter_tokens(s):
    # Stream tokens: ASCII [a-z0-9]+, lowercase; others are separators
    buf = []
    append = buf.append
    for ch in s:
        o = ord(ch)
        if 48 <= o <= 57:          # '0'-'9'
            append(ch)
        elif 65 <= o <= 90:         # 'A'-'Z' -> to lowercase
            append(chr(o + 32))
        elif 97 <= o <= 122:        # 'a'-'z'
            append(ch)
        else:
            if buf:
                yield ''.join(buf)
                buf.clear()
    if buf:
        yield ''.join(buf)

def _compute_top_k(s, k):
    try:
        k = int(k)
    except Exception:
        k = 0
    if k <= 0 or not s:
        return []

    counts = {}
    for tok in _iter_tokens(s if isinstance(s, str) else str(s)):
        counts[tok] = counts.get(tok, 0) + 1

    if not counts:
        return []

    n_unique = len(counts)
    key = lambda kv: (-kv[1], kv[0])  # sort by count desc, token asc

    if n_unique <= k:
        return sorted(counts.items(), key=key)

    top = heapq.nsmallest(k, counts.items(), key=key)
    top.sort(key=key)
    return top

# Use provided globals `text` and `k`; fall back safely if absent.
try:
    _text = text  # type: ignore[name-defined]
except NameError:
    _text = ""
try:
    _k = k  # type: ignore[name-defined]
except NameError:
    _k = 0

# Exposed result: list of (token, count), sorted by count desc then token asc
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_29.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_29.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_29.py`*
