# File Documentation: macro.py

## File Metadata
- **Path**: `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/macro.py`
- **Size**: 711 bytes (711 characters)
- **Lines**: 18
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from agents import Agent, WebSearchTool, ModelSettings
from tools import get_fred_series
from utils import load_prompt, DISCLAIMER

default_model = "gpt-4.1"
default_search_context = "medium"
RECENT_DAYS = 45

def build_macro_agent():
    tool_retry_instructions = load_prompt("tool_retry_prompt.md")
    macro_prompt = load_prompt("macro_base.md", RECENT_DAYS=RECENT_DAYS)
    return Agent(
        name="Macro Analysis Agent",
        instructions=(macro_prompt + DISCLAIMER + tool_retry_instructions),
        tools=[WebSearchTool(search_context_size=default_search_context), get_fred_series],
        model=default_model,
        model_settings=ModelSettings(parallel_tool_calls=True, temperature=0),
    ) 
```

---

## High-Level Overview

This is a Python source file and 1 function(s).

---

## Detailed Walkthrough

### Functions

- `build_macro_agent()`

### Dependencies/Imports

- `agents`
- `tools`
- `utils`

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
python examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/macro.py

# Run tests (if this is a test file)
pytest examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/macro.py
```

---

*Documentation generated for `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/macro.py`*
