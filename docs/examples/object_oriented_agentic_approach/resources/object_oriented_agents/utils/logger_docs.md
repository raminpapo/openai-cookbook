# File Documentation: logger.py

## File Metadata
- **Path**: `examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/logger.py`
- **Size**: 882 bytes (882 characters)
- **Lines**: 28
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
# object_oriented_agents/utils/logger.py
import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO, formatter: Optional[logging.Formatter] = None) -> logging.Logger:
    """
    Return a logger instance with a given name and logging level.
    If no formatter is provided, a default formatter will be used.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # Use a default formatter if none is provided
        if formatter is None:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        ch.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(ch)

    return logger
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `logging`
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
python examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/logger.py

# Run tests (if this is a test file)
pytest examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/logger.py
```

---

*Documentation generated for `examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/logger.py`*
