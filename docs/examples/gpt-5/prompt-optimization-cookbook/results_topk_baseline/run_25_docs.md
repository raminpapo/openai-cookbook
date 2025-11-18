# File Documentation: run_25.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_25.py`
- **Size**: 1,351 bytes (1,351 characters)
- **Lines**: 52
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import heapq
from collections import Counter

# Expects globals: text (str) and k (int)
# Produces: top_k -> list[tuple[str, int]]

def _count_tokens_ascii_lower(s: str) -> Counter:
    # One-pass ASCII [a-z0-9]+ tokenizer with on-the-fly lowercasing
    cnt = Counter()
    buf = []  # current token buffer

    for ch in s:
        if ch.isascii():
            o = ord(ch)
            # Fast ASCII lowercase
            if 65 <= o <= 90:  # 'A'-'Z'
                o += 32
                c = chr(o)
            else:
                c = ch

            oc = ord(c)
            if 97 <= oc <= 122 or 48 <= oc <= 57:  # 'a'-'z' or '0'-'9'
                buf.append(c)
                continue

        if buf:
            token = ''.join(buf)
            cnt[token] += 1
            buf.clear()

    if buf:
        token = ''.join(buf)
        cnt[token] += 1

    return cnt


# Build frequency map
_counts = _count_tokens_ascii_lower(text)

# Determine k safely
_unique = len(_counts)
_k = int(k) if isinstance(k, int) or (isinstance(k, bool) is False and str(k).lstrip("-").isdigit()) else 0
_k = max(0, min(_k, _unique))

# Top-K sorted by count desc, then token asc
if _k == 0:
    top_k = []
else:
    # nsmallest on (-count, token) yields count desc, token asc
    top_k = heapq.nsmallest(_k, _counts.items(), key=lambda it: (-it[1], it[0]))
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `collections`
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_25.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_25.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_25.py`*
