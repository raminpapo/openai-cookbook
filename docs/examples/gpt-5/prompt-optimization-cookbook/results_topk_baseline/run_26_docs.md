# File Documentation: run_26.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_26.py`
- **Size**: 1,210 bytes (1,210 characters)
- **Lines**: 49
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from heapq import nsmallest

def _counts_from_text(s: str):
    # One-pass ASCII tokenizer: [a-z0-9]+ after lowercasing A-Z only
    counts = {}
    buf = []
    append = buf.append
    clear = buf.clear
    get = counts.get
    for ch in s:
        oc = ord(ch)
        if 48 <= oc <= 57:          # 0-9
            append(ch)
        elif 65 <= oc <= 90:        # A-Z -> a-z
            append(chr(oc + 32))
        elif 97 <= oc <= 122:       # a-z
            append(ch)
        else:
            if buf:
                tok = ''.join(buf)
                counts[tok] = get(tok, 0) + 1
                clear()
    if buf:
        tok = ''.join(buf)
        counts[tok] = get(tok, 0) + 1
    return counts

def _top_k_from_counts(counts, k: int):
    if k <= 0 or not counts:
        return []
    # Sort by count desc, then token asc; do k-selection to avoid full sort
    return list(nsmallest(k, counts.items(), key=lambda it: (-it[1], it[0])))

# Use provided globals `text` (str) and `k` (int)
try:
    _text = text
    _k = k
except NameError:
    _text = ""
    _k = 0

try:
    _k = int(_k)
except Exception:
    _k = 0
if _k < 0:
    _k = 0

top_k = _top_k_from_counts(_counts_from_text(_text), _k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_counts_from_text(s: str)`
- `_top_k_from_counts(counts, k: int)`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_26.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_26.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_26.py`*
