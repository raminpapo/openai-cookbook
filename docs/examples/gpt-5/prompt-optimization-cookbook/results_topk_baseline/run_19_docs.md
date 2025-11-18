# File Documentation: run_19.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_19.py`
- **Size**: 1,011 bytes (1,011 characters)
- **Lines**: 36
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from heapq import nsmallest
from typing import List, Tuple, Iterable, Dict


def _iter_tokens(s: str, _pat=re.compile(r'[a-z0-9]+')) -> Iterable[str]:
    # Lowercase, then yield ASCII [a-z0-9]+ sequences
    for m in _pat.finditer(s.lower()):
        yield m.group(0)


def top_k_tokens(s: str, k: int) -> List[Tuple[str, int]]:
    if not isinstance(s, str):
        raise TypeError("text must be a str")
    if not isinstance(k, int):
        raise TypeError("k must be an int")
    if k <= 0:
        return []

    counts: Dict[str, int] = {}
    get = counts.get
    for tok in _iter_tokens(s):
        counts[tok] = get(tok, 0) + 1

    if not counts:
        return []

    # Sort by count desc, then token asc using nsmallest with key (-count, token)
    return nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))


# Expose the result as a convenient global: top_k
try:
    top_k = top_k_tokens(text, k)  # expects globals: text (str), k (int)
except Exception:
    top_k = []
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `heapq`
- `re`
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_19.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_19.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_19.py`*
