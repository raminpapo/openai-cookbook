# File Documentation: supply_chain_guardrails.py

## File Metadata
- **Path**: `examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/supply_chain_guardrails.py`
- **Size**: 1,182 bytes (1,182 characters)
- **Lines**: 37
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
"""
Output guardrail that blocks answers not related to supply-chain topics.
"""
from __future__ import annotations

from pydantic import BaseModel
from agents import Agent, Runner, GuardrailFunctionOutput
from agents import output_guardrail
from agents.run_context import RunContextWrapper

class SupplyChainCheckOutput(BaseModel):
    reasoning: str
    is_supply_chain: bool


guardrail_agent = Agent(
    name="Supply-chain check",
    instructions=(
        "Check if the text is within the domain of supply-chain analytics and operations "
        "Return JSON strictly matching the SupplyChainCheckOutput schema"
    ),
    output_type=SupplyChainCheckOutput,
)


@output_guardrail
async def supply_chain_guardrail(
    ctx: RunContextWrapper, agent: Agent, output
) -> GuardrailFunctionOutput:
    """Output guardrail that blocks non-supply-chain answers"""
    text = output if isinstance(output, str) else getattr(output, "response", str(output))
    result = await Runner.run(guardrail_agent, text, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_supply_chain,
    )

```

---

## High-Level Overview

This is a Python source file containing 1 class(es).

---

## Detailed Walkthrough

### Classes

- `SupplyChainCheckOutput`

### Dependencies/Imports

- `__future__`
- `agents`
- `agents.run_context`
- `pydantic`

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
python examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/supply_chain_guardrails.py

# Run tests (if this is a test file)
pytest examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/supply_chain_guardrails.py
```

---

*Documentation generated for `examples/mcp/building-a-supply-chain-copilot-with-agent-sdk-and-databricks-mcp/supply_chain_guardrails.py`*
