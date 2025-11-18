# File Documentation: run_15.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_15.py`
- **Size**: 1,302 bytes (1,302 characters)
- **Lines**: 41
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
# Computes top_k: the Top-K most frequent ASCII [a-z0-9]+ tokens from the global `text`
# using lowercase tokenization and sorting by count desc, then token asc.

from typing import List, Tuple

def _iter_ascii_tokens(s: str):
    # Stream through s once; yield lowercase ASCII [a-z0-9]+ tokens
    buf = []
    append = buf.append
    for ch in s:
        o = ord(ch)
        if 48 <= o <= 57:         # '0'-'9'
            append(ch)
        elif 97 <= o <= 122:      # 'a'-'z'
            append(ch)
        elif 65 <= o <= 90:       # 'A'-'Z' -> lower
            append(chr(o + 32))
        else:
            if buf:
                yield ''.join(buf)
                buf.clear()
    if buf:
        yield ''.join(buf)

def _compute_top_k(txt: str, k: int) -> List[Tuple[str, int]]:
    if k <= 0:
        return []
    counts = {}
    get = counts.get
    for tok in _iter_ascii_tokens(txt):
        counts[tok] = get(tok, 0) + 1
    if not counts:
        return []
    # Sort by count desc, then token asc; take first k
    items = sorted(counts.items(), key=lambda it: (-it[1], it[0]))
    if k < len(items):
        items = items[:k]
    return items

# Expect globals `text` (str) and `k` (int) to be provided by the caller environment.
top_k: List[Tuple[str, int]] = _compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_ascii_tokens(s: str)`

### Dependencies/Imports

- `typing`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_15.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_15.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_15.py`*
