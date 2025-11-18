# File Documentation: run_24.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_24.py`
- **Size**: 1,195 bytes (1,195 characters)
- **Lines**: 42
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from typing import List, Tuple, Dict

def compute_top_k(s: str, k: int) -> List[Tuple[str, int]]:
    # Tokenize: lowercase letters, digits; others are separators
    counts: Dict[str, int] = {}
    buf: List[str] = []

    append = buf.append
    get = counts.get

    for c in s:
        oc = ord(c)
        if 48 <= oc <= 57:  # '0'-'9'
            append(c)
        elif 65 <= oc <= 90:  # 'A'-'Z' -> to lowercase
            append(chr(oc + 32))
        elif 97 <= oc <= 122:  # 'a'-'z'
            append(c)
        else:
            if buf:
                tok = ''.join(buf)
                counts[tok] = (get(tok) or 0) + 1
                buf.clear()
    if buf:
        tok = ''.join(buf)
        counts[tok] = (get(tok) or 0) + 1

    if k <= 0 or not counts:
        return []

    items = counts.items()
    items_sorted = sorted(items, key=lambda it: (-it[1], it[0]))
    return items_sorted[:min(k, len(items_sorted))]

# Produce the required global `top_k` using provided globals `text` and `k`
try:
    _text = text  # provided externally
    _k = k        # provided externally
except NameError:
    top_k: List[Tuple[str, int]] = []
else:
    top_k = compute_top_k(_text, _k)
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_24.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_24.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_24.py`*
