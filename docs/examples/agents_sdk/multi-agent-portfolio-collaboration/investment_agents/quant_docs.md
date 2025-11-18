# File Documentation: quant.py

## File Metadata
- **Path**: `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/quant.py`
- **Size**: 1,082 bytes (1,082 characters)
- **Lines**: 27
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from agents import Agent, ModelSettings
from tools import run_code_interpreter, get_fred_series, read_file, list_output_files
from utils import load_prompt, DISCLAIMER, repo_path
from pathlib import Path

default_model = "gpt-4.1"

def build_quant_agent():
    tool_retry_instructions = load_prompt("tool_retry_prompt.md")
    quant_prompt = load_prompt("quant_base.md")
    # Set up the Yahoo Finance MCP server
    from agents.mcp import MCPServerStdio
    server_path = str(repo_path("mcp/yahoo_finance_server.py"))
    yahoo_mcp_server = MCPServerStdio(
        params={"command": "python", "args": [server_path]},
        client_session_timeout_seconds=300,
        cache_tools_list=True,
    )
    
    return Agent(
        name="Quantitative Analysis Agent",
        instructions=(quant_prompt + DISCLAIMER + tool_retry_instructions),
        mcp_servers=[yahoo_mcp_server],
        tools=[run_code_interpreter, get_fred_series, read_file, list_output_files],
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

- `build_quant_agent()`

### Dependencies/Imports

- `agents`
- `agents.mcp`
- `pathlib`
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
python examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/quant.py

# Run tests (if this is a test file)
pytest examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/quant.py
```

---

*Documentation generated for `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/quant.py`*
