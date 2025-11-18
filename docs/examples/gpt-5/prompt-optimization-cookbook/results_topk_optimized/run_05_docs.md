# File Documentation: run_05.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_optimized/run_05.py`
- **Size**: 1,326 bytes (1,326 characters)
- **Lines**: 43
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
import heapq
from collections import Counter
from typing import List, Tuple, Iterable

_TOKEN = re.compile(r"[a-z0-9]+", flags=re.ASCII | re.IGNORECASE)

def _tokens(s: str) -> Iterable[str]:
    for m in _TOKEN.finditer(s):
        yield m.group(0).lower()

def top_k_tokens(text: str, k: int) -> List[Tuple[str, int]]:
    if not isinstance(k, int) or k <= 0:
        return []
    cnt = Counter()
    for t in _tokens(text):
        cnt[t] += 1
    u = len(cnt)
    if u == 0:
        return []
    key = lambda kv: (-kv[1], kv[0])  # sort by count desc, then token asc

    if k >= u:
        return sorted(cnt.items(), key=key)
    # Sort all only when k >= 0.3 * u
    if 10 * k >= 3 * u:
        return sorted(cnt.items(), key=key)[:k]
    # Exact selection with bounded memory
    return heapq.nsmallest(k, cnt.items(), key=key)

# Use provided globals if available; optional demo otherwise
try:
    text; k  # type: ignore[name-defined]
except NameError:
    if __name__ == "__main__":
        demo_text = "A a b b b c1 C1 c1 -- d! d? e"
        demo_k = 3
        top_k = top_k_tokens(demo_text, demo_k)
        print(top_k)
else:
    top_k = top_k_tokens(text, k)  # type: ignore[name-defined]

# Complexity: counting O(N tokens); selection O(U log k) when k < 0.3U, else O(U log U). Extra space O(U + k).
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `collections`
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_optimized/run_05.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_optimized/run_05.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_optimized/run_05.py`*
