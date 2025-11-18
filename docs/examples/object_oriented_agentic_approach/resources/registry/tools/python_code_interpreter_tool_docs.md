# File Documentation: python_code_interpreter_tool.py

## File Metadata
- **Path**: `examples/object_oriented_agentic_approach/resources/registry/tools/python_code_interpreter_tool.py`
- **Size**: 2,307 bytes (2,307 characters)
- **Lines**: 66
- **Extension**: `.py`
- **Classification**: text

---

## Original Source

```python
import subprocess
from typing import Tuple, Dict, Any

from ...object_oriented_agents.utils.logger import get_logger
from ...object_oriented_agents.core_classes.tool_interface import ToolInterface

class PythonExecTool(ToolInterface):
    """
    A Tool that executes Python code securely in a container.
    """

    def get_definition(self) -> Dict[str, Any]:
        """
        Return the JSON/dict definition of the tool's function
        in the format expected by the OpenAI function calling API.
        """
        return {
            "function": {
                "name": "execute_python_code",
                "description": "Executes Python code securely in a container. Python version 3.10 is installed in the container. pandas, numpy, matplotlib, seaborn, and scikit-learn are installed in the container.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "python_code": {
                            "type": "string",
                            "description": "The Python code to execute"
                        }
                    },
                    "required": ["python_code"]
                }
            }
        }

    def run(self, arguments: Dict[str, Any]) -> str:
        """
        Execute the Python code in a Docker container and return the output.
        """
        python_code = arguments["python_code"]
        python_code_stripped = python_code.strip('"""')

        output, errors = self._run_code_in_container(python_code_stripped)
        if errors:
            return f"[Error]\n{errors}"

        return output

    @staticmethod
    def _run_code_in_container(code: str, container_name: str = "sandbox") -> Tuple[str, str]:
        """
        Helper function that actually runs Python code inside a Docker container named `sandbox` (by default).
        """
        cmd = [
            "docker", "exec", "-i",
            container_name,
            "python", "-c", "import sys; exec(sys.stdin.read())"
        ]

        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = process.communicate(code)
        return out, err
```

---

## High-Level Overview

This is a Python source file containing 1 class(es).

---

## Detailed Walkthrough

### Classes

- `PythonExecTool`

### Dependencies/Imports

- `...object_oriented_agents.core_classes.tool_interface`
- `...object_oriented_agents.utils.logger`
- `subprocess`
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
python examples/object_oriented_agentic_approach/resources/registry/tools/python_code_interpreter_tool.py

# Run tests (if this is a test file)
pytest examples/object_oriented_agentic_approach/resources/registry/tools/python_code_interpreter_tool.py
```

---

*Documentation generated for `examples/object_oriented_agentic_approach/resources/registry/tools/python_code_interpreter_tool.py`*
