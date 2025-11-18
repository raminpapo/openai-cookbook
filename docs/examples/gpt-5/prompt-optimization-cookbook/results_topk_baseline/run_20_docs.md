# File Documentation: run_20.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_20.py`
- **Size**: 1,096 bytes (1,096 characters)
- **Lines**: 36
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from heapq import nsmallest

def _count_tokens_ascii(text: str):
    # One-pass ASCII [a-z0-9]+ tokenizer (lowercasing A-Z); others are separators.
    counts = {}
    buf = []
    append = buf.append
    get = counts.get
    def commit():
        if buf:
            tok = ''.join(buf)
            counts[tok] = get(tok, 0) + 1
            buf.clear()

    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:          # 'A'-'Z' -> lower
            append(chr(o + 32))
        elif 97 <= o <= 122:       # 'a'-'z'
            append(ch)
        elif 48 <= o <= 57:        # '0'-'9'
            append(ch)
        else:
            commit()
    commit()
    return counts

def _top_k_from_counts(counts, k: int):
    if k <= 0 or not counts:
        return []
    # Sort by count desc, then token asc using nsmallest with key (-count, token)
    return nsmallest(k, counts.items(), key=lambda kv: (-kv[1], kv[0]))

# Expect globals: text (str) and k (int) to be provided by the environment.
# Produce the required global `top_k`.
top_k = _top_k_from_counts(_count_tokens_ascii(text), k)
```

---

## High-Level Overview

This is a Python source file and 3 function(s).

---

## Detailed Walkthrough

### Functions

- `_count_tokens_ascii(text: str)`
- `commit()`
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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_20.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_20.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_20.py`*
