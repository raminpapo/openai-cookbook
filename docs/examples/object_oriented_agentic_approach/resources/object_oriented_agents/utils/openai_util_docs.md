# File Documentation: openai_util.py

## File Metadata
- **Path**: `examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/openai_util.py`
- **Size**: 959 bytes (959 characters)
- **Lines**: 36
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
# object_oriented_agents/utils/openai_util.py

from typing import List, Dict, Any
from .logger import get_logger
from ..services.openai_factory import OpenAIClientFactory

logger = get_logger("OpenAIUtils")

def call_openai_chat_completion(
    model: str,
    messages: List[Dict[str, str]],
    tools: List[Dict[str, Any]] = None,
    openai_client=None,
    api_key: str = None
) -> Any:
    """
    A utility function to call OpenAI's chat completion.
    If openai_client is provided, use it, otherwise create a new one.
    """
    if openai_client is None:
        openai_client = OpenAIClientFactory.create_client(api_key=api_key)

    kwargs = {
        "model": model,
        "messages": messages,
    }

    if tools:
        kwargs["tools"] = tools

    try:
        response = openai_client.chat.completions.create(**kwargs)
        return response
    except Exception as e:
        logger.error(f"OpenAI call failed: {str(e)}")
        raise e
```

---

## High-Level Overview

This is a Python source file.

---

## Detailed Walkthrough

### Dependencies/Imports

- `..services.openai_factory`
- `.logger`
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
python examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/openai_util.py

# Run tests (if this is a test file)
pytest examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/openai_util.py
```

---

*Documentation generated for `examples/object_oriented_agentic_approach/resources/object_oriented_agents/utils/openai_util.py`*
