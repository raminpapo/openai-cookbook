# File Documentation: run_08.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_08.py`
- **Size**: 802 bytes (802 characters)
- **Lines**: 31
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq
from typing import List, Tuple, Dict

# Expects globals: text (str) and k (int)

_token_re = re.compile(r'[a-z0-9]+')

def compute_top_k(src: str, top_n: int) -> List[Tuple[str, int]]:
    # Lowercase once, stream tokens via finditer to avoid building a full token list
    counts: Dict[str, int] = {}
    for m in _token_re.finditer(src.lower()):
        t = m.group(0)
        counts[t] = counts.get(t, 0) + 1

    if not counts:
        return []

    try:
        n = int(top_n)
    except Exception:
        n = 0
    if n <= 0:
        return []

    n = min(n, len(counts))
    # Smallest by (-count, token) => count desc, token asc
    return heapq.nsmallest(n, counts.items(), key=lambda kv: (-kv[1], kv[0]))

# Produce the required global
top_k = compute_top_k(text, k)
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_08.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_08.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_08.py`*
