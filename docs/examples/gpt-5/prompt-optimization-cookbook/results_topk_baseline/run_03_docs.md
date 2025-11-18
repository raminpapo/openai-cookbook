# File Documentation: run_03.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_03.py`
- **Size**: 1,273 bytes (1,273 characters)
- **Lines**: 45
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import heapq

def _count_tokens(s: str) -> dict:
    # Count ASCII [a-z0-9]+ tokens, lowercasing letters during scan.
    counts = {}
    buf = []
    append = buf.append
    for ch in s:
        o = ord(ch)
        if 48 <= o <= 57:          # 0-9
            append(ch)
        elif 65 <= o <= 90:        # A-Z -> a-z
            append(chr(o + 32))
        elif 97 <= o <= 122:       # a-z
            append(ch)
        else:
            if buf:
                tok = ''.join(buf)
                counts[tok] = counts.get(tok, 0) + 1
                buf.clear()
    if buf:
        tok = ''.join(buf)
        counts[tok] = counts.get(tok, 0) + 1
    return counts

def _top_k_from_counts(counts: dict, k: int):
    if not counts or k <= 0:
        return []
    m = min(k, len(counts))
    # Order: count desc, then token asc -> use nsmallest with key (-count, token)
    return heapq.nsmallest(m, counts.items(), key=lambda it: (-it[1], it[0]))

# Use provided globals text (str) and k (int); fall back safely if absent.
try:
    _text = text  # type: ignore[name-defined]
except NameError:
    _text = ""
try:
    _k = int(k)  # type: ignore[name-defined]
except NameError:
    _k = 0
except Exception:
    _k = 0

top_k = _top_k_from_counts(_count_tokens(_text), _k)
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `_top_k_from_counts(counts: dict, k: int)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_03.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_03.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_03.py`*
