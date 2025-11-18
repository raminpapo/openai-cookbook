# File Documentation: utils.py

## File Metadata
- **Path**: `examples/partners/temporal_agents_with_knowledge_graphs/utils.py`
- **Size**: 1,200 bytes (1,200 characters)
- **Lines**: 48
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import re
from datetime import UTC, datetime

from dateutil.parser import parse


def parse_date_str(value: str | datetime | None) -> datetime | None:
    """Parse a date string into a datetime object.

    If the value is a 4-digit year, it returns January 1 of that year in UTC.
    Otherwise, it attempts to parse the date string using dateutil.parser.parse.
    If the resulting datetime has no timezone, it defaults to UTC.
    """
    if not value:
        return None

    if isinstance(value, datetime):
        return value

    try:
        # Year Handling
        if re.fullmatch(r"\d{4}", value.strip()):
            year = int(value.strip())
            return datetime(year, 1, 1, tzinfo=UTC)

        #  General Handing
        dt: datetime = parse(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=UTC)
        return dt

    except Exception:
        return None


def safe_iso(dt: datetime | None) -> str | None:
    """Return the ISO format of a datetime object.

    If the datetime is None, it returns None.
    """
    if isinstance(dt, str):
        dt = parse_date_str(dt)

    if isinstance(dt, datetime):
        return dt.isoformat()

    return None

```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `datetime`
- `dateutil.parser`
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
python examples/partners/temporal_agents_with_knowledge_graphs/utils.py

# Run tests (if this is a test file)
pytest examples/partners/temporal_agents_with_knowledge_graphs/utils.py
```

---

*Documentation generated for `examples/partners/temporal_agents_with_knowledge_graphs/utils.py`*
