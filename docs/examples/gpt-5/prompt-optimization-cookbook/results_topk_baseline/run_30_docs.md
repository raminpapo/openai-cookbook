# File Documentation: run_30.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_30.py`
- **Size**: 578 bytes (578 characters)
- **Lines**: 18
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from collections import Counter

def compute_top_k(text: str, k: int):
    # Tokens: ASCII [A-Za-z0-9]+, lowercased; other chars are separators
    if not isinstance(text, str) or not isinstance(k, int) or k <= 0:
        return []
    counter = Counter()
    pattern = re.compile(r'[A-Za-z0-9]+')
    for m in pattern.finditer(text):
        counter[m.group(0).lower()] += 1
    if not counter:
        return []
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:min(k, len(items))]

# Exposed result
top_k = compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `compute_top_k(text: str, k: int)`

### Dependencies/Imports

- `collections`
- `re`

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_30.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_30.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_30.py`*
