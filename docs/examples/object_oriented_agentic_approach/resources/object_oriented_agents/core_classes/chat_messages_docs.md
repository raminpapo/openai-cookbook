# File Documentation: chat_messages.py

## File Metadata
- **Path**: `examples/object_oriented_agentic_approach/resources/object_oriented_agents/core_classes/chat_messages.py`
- **Size**: 811 bytes (811 characters)
- **Lines**: 23
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
# object_oriented_agents/core_classes/chat_messages.py
from typing import List, Dict

class ChatMessages:
    """
    Stores all messages in a conversation (developer, user, assistant).
    """

    def __init__(self, developer_prompt: str):
        self.messages: List[Dict[str, str]] = []
        self.add_developer_message(developer_prompt)

    def add_developer_message(self, content: str) -> None:
        self.messages.append({"role": "developer", "content": content})

    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})

    def get_messages(self) -> List[Dict[str, str]]:
        return self.messages
```

---

## High-Level Overview

This is a Python source file containing 1 class(es) and 1 function(s).

---

## Detailed Walkthrough

### Classes

- `ChatMessages`

### Functions

- `__init__(self, developer_prompt: str)`

### Dependencies/Imports

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
python examples/object_oriented_agentic_approach/resources/object_oriented_agents/core_classes/chat_messages.py

# Run tests (if this is a test file)
pytest examples/object_oriented_agentic_approach/resources/object_oriented_agents/core_classes/chat_messages.py
```

---

*Documentation generated for `examples/object_oriented_agentic_approach/resources/object_oriented_agents/core_classes/chat_messages.py`*
