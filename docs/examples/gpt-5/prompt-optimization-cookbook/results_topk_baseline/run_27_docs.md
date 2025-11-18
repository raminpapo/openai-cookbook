# File Documentation: run_27.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_27.py`
- **Size**: 1,118 bytes (1,118 characters)
- **Lines**: 47
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from collections import Counter
import heapq

# Expects globals: text (str) and k (int). Produces: top_k = [(token, count), ...]

def _count_tokens(s: str) -> Counter:
    # Single-pass ASCII tokenizer: [a-z0-9]+, lowercased; others are separators
    counts = Counter()
    buf = []
    for ch in s:
        o = ord(ch)
        if 48 <= o <= 57:          # '0'-'9'
            buf.append(ch)
        elif 65 <= o <= 90:        # 'A'-'Z' -> lower
            buf.append(chr(o + 32))
        elif 97 <= o <= 122:       # 'a'-'z'
            buf.append(ch)
        else:
            if buf:
                tok = ''.join(buf)
                counts[tok] += 1
                buf.clear()
    if buf:
        tok = ''.join(buf)
        counts[tok] += 1
    return counts

# Read provided globals safely
try:
    _text = text
except NameError:
    _text = ""

try:
    _k = int(k)
except Exception:
    _k = 0
if _k < 0:
    _k = 0

_counts = _count_tokens(_text)

# Top-K by count desc, then token asc
if _counts and _k:
    top_k = heapq.nsmallest(_k, _counts.items(), key=lambda kv: (-kv[1], kv[0]))
else:
    top_k = []
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_27.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_27.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_27.py`*
