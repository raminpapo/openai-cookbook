# Documentation: file_access_tool.py

## File Metadata
- **Path**: `examples/object_oriented_agentic_approach/resources/registry/tools/file_access_tool.py`
- **Type**: .py file
- **Size**: 4,593 bytes (4.49 KB)
- **Lines**: 105
- **Words**: 366
- **Characters**: 4,593

## Original Source

```python
from typing import Dict, Any
import pandas as pd
import subprocess
import os

from ...object_oriented_agents.utils.logger import get_logger
from ...object_oriented_agents.core_classes.tool_interface import ToolInterface

class FileAccessTool(ToolInterface):
    """
    A tool to read CSV files and copy them to a Docker container.
    """

    def __init__(self, logger=None):
        self.logger = logger or get_logger(self.__class__.__name__)

    def get_definition(self) -> Dict[str, Any]:
        self.logger.debug("Returning tool definition for safe_file_access")
        return {
            "function": {
                "name": "safe_file_access",
                "description": (
                    "Read the contents of a file in a secure manner "
                    "and transfer it to the Python code interpreter docker container"
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filename": {
                            "type": "string",
                            "description": "Name of the file to read"
                        }
                    },
                    "required": ["filename"]
                }
            }
        }

    def run(self, arguments: Dict[str, Any]) -> str:
        filename = arguments["filename"]
        self.logger.debug(f"Running safe_file_access with filename: {filename}")
        
        return self.safe_file_access(filename)

    def safe_file_access(self, filename: str) -> str:
        if not filename.endswith('.csv'):
            error_msg = "Error: The file is not a CSV file."
            self.logger.warning(f"{error_msg} - Filename provided: {filename}")
            return error_msg

        # Ensure the path is correct
        if not os.path.dirname(filename):
        
            filename = os.path.join('./resources/data', filename)
        
        self.logger.debug(f"Attempting to read file at path: {filename}")
        try:
            df = pd.read_csv(filename)
            self.logger.debug(f"File '{filename}' loaded successfully.")
            copy_output = self.copy_file_to_container(filename)
            head_str = df.head(15).to_string()
            return f"{copy_output}\nThe file content for the first 15 rows is:\n{head_str}"
        except FileNotFoundError:
            error_msg = f"Error: The file '{filename}' was not found."
            self.logger.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error while reading the CSV file: {str(e)}"
            self.logger.error(error_msg, exc_info=True)
            return error_msg

    def copy_file_to_container(self, local_file_name: str, container_name: str = "sandbox") -> str:
        container_home_path = "/home/sandboxuser"
        self.logger.debug(f"Copying '{local_file_name}' to container '{container_name}'.")

        if not os.path.isfile(local_file_name):
            error_msg = f"The local file '{local_file_name}' does not exist."
            self.logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        # Check if container is running
        check_container_cmd = ["docker", "inspect", "-f", "{{.State.Running}}", container_name]
        result = subprocess.run(check_container_cmd, capture_output=True, text=True)
        if result.returncode != 0 or result.stdout.strip() != "true":
            error_msg = f"The container '{container_name}' is not running."
            self.logger.error(error_msg)
            raise RuntimeError(error_msg)

        # Copy the file into the container
        container_path = f"{container_name}:{container_home_path}/{os.path.basename(local_file_name)}"
        self.logger.debug(f"Running command: docker cp {local_file_name} {container_path}")
        subprocess.run(["docker", "cp", local_file_name, container_path], check=True)

        # Verify the file was copied
        verify_cmd = ["docker", "exec", container_name, "test", "-f",
                      f"{container_home_path}/{os.path.basename(local_file_name)}"]
        verify_result = subprocess.run(verify_cmd, capture_output=True, text=True)
        if verify_result.returncode != 0:
            error_msg = f"Failed to verify the file '{local_file_name}' in the container '{container_name}'."
            self.logger.error(error_msg)
            raise RuntimeError(error_msg)

        success_msg = f"Copied {local_file_name} into {container_name}:{container_home_path}/."
        self.logger.debug(success_msg)
        return success_msg
```



## High-Level Overview

Python module.

A tool to read CSV files and copy them to a Docker container.

## Detailed Analysis

**Classes**: FileAccessTool

**Functions**: __init__, get_definition, run, safe_file_access, copy_file_to_container

**Dependencies**: ...object_oriented_agents.core_classes.tool_interface, ...object_oriented_agents.utils.logger, Dict, ToolInterface, get_logger, os, pandas, subprocess, typing

## Usage & Examples

Import this module in Python:

```python
import file_access_tool
```

## Performance & Security Notes

No specific performance or security concerns identified.

## Related Files

**Same directory**:
- [python_code_interpreter_tool.py](./python_code_interpreter_tool.py_docs.md)

**Imported modules**:
- `...object_oriented_agents.core_classes.tool_interface`
- `...object_oriented_agents.utils.logger`
- `Dict`
- `ToolInterface`
- `get_logger`
- `os`
- `pandas`
- `subprocess`
- `typing`

## Testing & Execution

For testing, create a corresponding test file.

---
*Generated by Repo Book Generator v1.0.0*
