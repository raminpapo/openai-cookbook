# File Documentation: fundamental.py

## File Metadata
- **Path**: `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/fundamental.py`
- **Size**: 1,100 bytes (1,100 characters)
- **Lines**: 28
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
from agents import Agent, WebSearchTool, ModelSettings
from utils import load_prompt, DISCLAIMER, repo_path
from pathlib import Path

default_model = "gpt-4.1"
default_search_context = "medium"
RECENT_DAYS = 15

def build_fundamental_agent():
    tool_retry_instructions = load_prompt("tool_retry_prompt.md")
    fundamental_prompt = load_prompt("fundamental_base.md", RECENT_DAYS=RECENT_DAYS)
    # Set up the Yahoo Finance MCP server
    from agents.mcp import MCPServerStdio
    server_path = str(repo_path("mcp/yahoo_finance_server.py"))
    yahoo_mcp_server = MCPServerStdio(
        params={"command": "python", "args": [server_path]},
        client_session_timeout_seconds=300,
        cache_tools_list=True,
    )
    
    return Agent(
        name="Fundamental Analysis Agent",
        instructions=(fundamental_prompt + DISCLAIMER + tool_retry_instructions),
        mcp_servers=[yahoo_mcp_server],
        tools=[WebSearchTool(search_context_size=default_search_context)],
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

- `build_fundamental_agent()`

### Dependencies/Imports

- `agents`
- `agents.mcp`
- `pathlib`
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
python examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/fundamental.py

# Run tests (if this is a test file)
pytest examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/fundamental.py
```

---

*Documentation generated for `examples/agents_sdk/multi-agent-portfolio-collaboration/investment_agents/fundamental.py`*
