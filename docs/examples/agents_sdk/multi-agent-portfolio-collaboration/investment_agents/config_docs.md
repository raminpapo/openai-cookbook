# File Documentation: config.py

## File Metadata
- **Path**: `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/config.py`
- **Size**: 970 bytes (970 characters)
- **Lines**: 31
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from dataclasses import dataclass
from investment_agents.fundamental import build_fundamental_agent
from investment_agents.macro import build_macro_agent
from investment_agents.quant import build_quant_agent
from investment_agents.editor import build_editor_agent, build_memo_edit_tool
from investment_agents.pm import build_head_pm_agent, SpecialistRequestInput
import asyncio

@dataclass
class InvestmentAgentsBundle:
    head_pm: object
    fundamental: object
    macro: object
    quant: object


def build_investment_agents() -> InvestmentAgentsBundle:
    fundamental = build_fundamental_agent()
    macro = build_macro_agent()
    quant = build_quant_agent()
    editor = build_editor_agent()
    memo_edit_tool = build_memo_edit_tool(editor)
    head_pm = build_head_pm_agent(fundamental, macro, quant, memo_edit_tool)
    return InvestmentAgentsBundle(
        head_pm=head_pm,
        fundamental=fundamental,
        macro=macro,
        quant=quant,
    )


```

---

## High-Level Overview

This is a Python source file containing 1 class(es).

---

## Detailed Walkthrough

### Classes

- `InvestmentAgentsBundle`

### Dependencies/Imports

- `asyncio`
- `dataclasses`
- `investment_agents.editor`
- `investment_agents.fundamental`
- `investment_agents.macro`
- `investment_agents.pm`
- `investment_agents.quant`

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
python examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/config.py

# Run tests (if this is a test file)
pytest examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/config.py
```

---

*Documentation generated for `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/config.py`*
