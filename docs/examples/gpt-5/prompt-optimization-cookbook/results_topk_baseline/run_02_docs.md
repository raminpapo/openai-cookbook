# File Documentation: run_02.py

## File Metadata
- **Path**: `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_02.py`
- **Size**: 759 bytes (759 characters)
- **Lines**: 25
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from typing import List, Tuple, Dict

def compute_top_k(text: str, k: int) -> List[Tuple[str, int]]:
    # Tokens are ASCII [a-z0-9]+; lowercase; others are separators.
    if not isinstance(text, str) or not isinstance(k, int) or k <= 0:
        return []

    pattern = re.compile(r'[a-z0-9]+', re.ASCII | re.IGNORECASE)
    counts: Dict[str, int] = {}
    get = counts.get

    for m in pattern.finditer(text):
        tok = m.group(0).lower()
        counts[tok] = (get(tok) or 0) + 1

    if not counts:
        return []

    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    limit = min(k, len(items))
    return items[:limit]

# Expose the result as a convenient global.
top_k: List[Tuple[str, int]] = compute_top_k(text, k)
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

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
python examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_02.py

# Run tests (if this is a test file)
pytest examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_02.py
```

---

*Documentation generated for `examples/gpt-5/prompt-optimization-cookbook/results_topk_baseline/run_02.py`*
