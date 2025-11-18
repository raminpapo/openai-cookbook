# File Documentation: run_09.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_09.py`
- **Size**: 1,234 bytes (1,234 characters)
- **Lines**: 40
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from heapq import nsmallest

def _count_tokens(s):
    # Scan once, building ASCII [a-z0-9]+ tokens in lowercase.
    counts = {}
    buf = []  # token buffer
    append = buf.append  # local for speed
    get = counts.get
    for ch in s:
        o = ord(ch)
        if 48 <= o <= 57:          # '0'-'9'
            append(ch)
        elif 65 <= o <= 90:        # 'A'-'Z' -> lower
            append(chr(o + 32))
        elif 97 <= o <= 122:       # 'a'-'z'
            append(ch)
        else:
            if buf:
                tok = "".join(buf)
                counts[tok] = get(tok, 0) + 1
                buf.clear()
    if buf:
        tok = "".join(buf)
        counts[tok] = get(tok, 0) + 1
        buf.clear()
    return counts

def _select_top_k(counts, k):
    # Sort by count desc, then token asc; pick up to k unique tokens.
    if not counts or k <= 0:
        return []
    n = min(k, len(counts))
    items = counts.items()
    # nsmallest with key (-count, token) gives desired order
    top = nsmallest(n, items, key=lambda kv: (-kv[1], kv[0]))
    return list(top)

# Expect globals: text (str), k (int)
# Build top_k as required: list of (token, count) tuples.
top_k = _select_top_k(_count_tokens(text), int(k))
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_count_tokens(s)`
- `_select_top_k(counts, k)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_09.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_09.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_09.py`*
