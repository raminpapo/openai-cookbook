# File Documentation: run_22.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_22.py`
- **Size**: 1,012 bytes (1,012 characters)
- **Lines**: 40
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import sys

def _iter_tokens(s: str):
    # Stream tokenizer: ASCII [a-z0-9]+, lowercase; others are separators.
    buf = []
    append = buf.append
    join = ''.join
    for ch in s:
        c = ch.lower()
        if ('a' <= c <= 'z') or ('0' <= c <= '9'):
            append(c)
        else:
            if buf:
                yield join(buf)
                buf.clear()
    if buf:
        yield join(buf)

def _top_k_tokens(s: str, k: int):
    if k <= 0:
        return []
    counts = {}
    get = counts.get
    for tok in _iter_tokens(s):
        counts[tok] = get(tok, 0) + 1
    if not counts:
        return []
    # Sort by count desc, then token asc
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[: min(k, len(items))]

# Expect globals: text (str) and k (int)
try:
    _text = text  # provided by caller
    _k = int(k)
except Exception:
    # If globals not provided, expose empty result for safety.
    top_k = []
else:
    top_k = _top_k_tokens(_text, _k)
```

---

## High-Level Overview

This is a Python source file and 2 function(s).

---

## Detailed Walkthrough

### Functions

- `_iter_tokens(s: str)`
- `_top_k_tokens(s: str, k: int)`

### Dependencies/Imports

- `sys`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_22.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_22.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_22.py`*
