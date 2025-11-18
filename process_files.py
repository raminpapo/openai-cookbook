#!/usr/bin/env python3
"""
File-by-file documentation generator
Processes each file and generates comprehensive documentation
"""

import os
import json
import re
import hashlib
from pathlib import Path
from collections import defaultdict, Counter
import keyword
import string

class FileDocGenerator:
    def __init__(self, repo_path=".", output_dir="./docs"):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()

        # Load file tree
        with open(self.output_dir / "file_tree.json", 'r') as f:
            self.file_tree = json.load(f)

        self.processed_files = 0
        self.created_docs = 0

    def extract_keywords(self, content, file_ext):
        """Extract keywords from file content"""
        keywords = set()

        # Common programming keywords
        programming_keywords = {
            'function', 'class', 'def', 'import', 'from', 'const', 'let', 'var',
            'async', 'await', 'return', 'if', 'else', 'for', 'while', 'try', 'except',
            'catch', 'finally', 'throw', 'raise', 'public', 'private', 'protected'
        }

        # Extract identifiers (alphanumeric + underscore sequences)
        identifiers = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]{2,}\b', content)

        # Filter and collect keywords
        for identifier in identifiers:
            # Skip Python keywords
            if keyword.iskeyword(identifier):
                continue
            # Skip very common words
            if identifier.lower() in {'the', 'and', 'for', 'that', 'this', 'with'}:
                continue
            # Skip single letters
            if len(identifier) < 2:
                continue

            keywords.add(identifier)

        # Extract function/class names (common patterns)
        # Python/JS: def function_name, class ClassName
        func_pattern = r'(?:def|function|class|const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        for match in re.finditer(func_pattern, content):
            keywords.add(match.group(1))

        # Extract import statements
        import_pattern = r'(?:import|from)\s+([a-zA-Z_][a-zA-Z0-9_.]*)'
        for match in re.finditer(import_pattern, content):
            keywords.add(match.group(1))

        return sorted(list(keywords))[:500]  # Limit to top 500

    def analyze_file_content(self, file_path, content):
        """Analyze file content and extract structure"""
        analysis = {
            "functions": [],
            "classes": [],
            "imports": [],
            "variables": [],
            "comments": []
        }

        ext = file_path.suffix.lower()

        # Python analysis
        if ext == '.py':
            # Functions
            for match in re.finditer(r'^\s*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\):', content, re.MULTILINE):
                analysis["functions"].append({
                    "name": match.group(1),
                    "params": match.group(2).strip()
                })

            # Classes
            for match in re.finditer(r'^\s*class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*(?:\([^)]*\))?:', content, re.MULTILINE):
                analysis["classes"].append(match.group(1))

            # Imports
            for match in re.finditer(r'^\s*(?:import|from)\s+([^\s]+)', content, re.MULTILINE):
                analysis["imports"].append(match.group(1))

        # JavaScript/TypeScript analysis
        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # Functions
            for match in re.finditer(r'(?:function|const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*[=:]?\s*(?:async\s*)?\([^)]*\)', content):
                analysis["functions"].append({"name": match.group(1)})

            # Classes
            for match in re.finditer(r'class\s+([a-zA-Z_$][a-zA-Z0-9_$]*)', content):
                analysis["classes"].append(match.group(1))

            # Imports
            for match in re.finditer(r'(?:import|from)\s+["\']([^"\']+)["\']', content):
                analysis["imports"].append(match.group(1))

        # Markdown analysis
        elif ext == '.md':
            # Extract headers
            headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
            analysis["headers"] = headers[:50]  # Limit to first 50

            # Extract code blocks
            code_blocks = re.findall(r'```(\w+)?', content)
            analysis["code_languages"] = list(set(code_blocks))

        return analysis

    def generate_file_docs(self, rel_path):
        """Generate comprehensive documentation for a single file"""
        file_info = self.file_tree[rel_path]
        file_path = self.repo_path / rel_path
        path_obj = Path(rel_path)

        # Create output directory
        out_dir = self.output_dir / path_obj.parent
        out_dir.mkdir(parents=True, exist_ok=True)

        file_stem = path_obj.stem if path_obj.stem else path_obj.name
        docs_file = out_dir / f"{file_stem}_docs.md"
        kw_file = out_dir / f"{file_stem}_kw.md"

        # Handle binary files
        if file_info["classification"] == "binary":
            docs_content = f"""# File Documentation: {path_obj.name}

## File Metadata
- **Path**: `{rel_path}`
- **Size**: {file_info['size']:,} bytes
- **Type**: Binary file
- **Classification**: {file_info['classification']}

## Description
This is a binary file and cannot be displayed as text. The file should be accessed directly from the repository.

## Suggested Handling
- For images: View using an image viewer
- For archives: Extract using appropriate archive tools
- For compiled files: This is a compiled binary

## Related Files
(See folder index for related files)
"""
            with open(docs_file, 'w', encoding='utf-8') as f:
                f.write(docs_content)

            kw_content = f"""# Keywords: {path_obj.name}

## File Information
- **Path**: `{rel_path}`
- **Type**: Binary file

Binary files do not contain extractable keywords.
"""
            with open(kw_file, 'w', encoding='utf-8') as f:
                f.write(kw_content)

            return 2  # Created 2 files

        # Handle text files
        elif file_info["classification"] == "text":
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()

                # Truncate if extremely large
                original_size = len(content)
                max_size = 2_000_000  # 2MB of text
                truncated = False
                if len(content) > max_size:
                    content = content[:max_size]
                    truncated = True

                # Extract keywords
                keywords = self.extract_keywords(content, path_obj.suffix)

                # Analyze content
                analysis = self.analyze_file_content(path_obj, content)

                # Generate documentation
                docs_content = self.create_docs_content(
                    rel_path, path_obj, file_info, content,
                    analysis, original_size, truncated
                )

                with open(docs_file, 'w', encoding='utf-8') as f:
                    f.write(docs_content)

                # Generate keywords file
                kw_content = self.create_keywords_content(
                    rel_path, path_obj, keywords, analysis
                )

                with open(kw_file, 'w', encoding='utf-8') as f:
                    f.write(kw_content)

                return 2  # Created 2 files

            except Exception as e:
                error_content = f"""# File Documentation: {path_obj.name}

## Error
Failed to process this file: {str(e)}

## File Metadata
- **Path**: `{rel_path}`
- **Size**: {file_info['size']:,} bytes
"""
                with open(docs_file, 'w', encoding='utf-8') as f:
                    f.write(error_content)
                return 1

        return 0

    def create_docs_content(self, rel_path, path_obj, file_info, content, analysis, original_size, truncated):
        """Create comprehensive documentation content"""
        lines = content.split('\n')
        num_lines = len(lines)

        docs = f"""# File Documentation: {path_obj.name}

## File Metadata
- **Path**: `{rel_path}`
- **Size**: {file_info['size']:,} bytes ({original_size:,} characters)
- **Lines**: {num_lines:,}
- **Extension**: `{path_obj.suffix or 'none'}`
- **Classification**: {file_info['classification']}

---

## Original Source

"""

        if truncated:
            docs += f"**Note**: This file is very large ({original_size:,} characters). Showing first {len(content):,} characters.\n\n"

        # Determine language for syntax highlighting
        lang_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.jsx': 'jsx', '.tsx': 'tsx', '.java': 'java', '.c': 'c',
            '.cpp': 'cpp', '.h': 'c', '.hpp': 'cpp', '.cs': 'csharp',
            '.rb': 'ruby', '.go': 'go', '.rs': 'rust', '.php': 'php',
            '.swift': 'swift', '.kt': 'kotlin', '.scala': 'scala',
            '.sh': 'bash', '.bash': 'bash', '.zsh': 'zsh',
            '.sql': 'sql', '.html': 'html', '.css': 'css', '.scss': 'scss',
            '.json': 'json', '.yaml': 'yaml', '.yml': 'yaml', '.xml': 'xml',
            '.md': 'markdown', '.txt': 'text', '.toml': 'toml',
            '.ini': 'ini', '.cfg': 'ini', '.conf': 'conf'
        }
        lang = lang_map.get(path_obj.suffix.lower(), '')

        docs += f"```{lang}\n{content}\n```\n\n"

        docs += "---\n\n## High-Level Overview\n\n"

        # Add overview based on file type
        if path_obj.suffix == '.py':
            docs += f"This is a Python source file"
            if analysis['classes']:
                docs += f" containing {len(analysis['classes'])} class(es)"
            if analysis['functions']:
                docs += f" and {len(analysis['functions'])} function(s)"
            docs += ".\n\n"
        elif path_obj.suffix in ['.js', '.ts', '.jsx', '.tsx']:
            docs += f"This is a {'TypeScript' if 't' in path_obj.suffix else 'JavaScript'} source file.\n\n"
        elif path_obj.suffix == '.md':
            docs += "This is a Markdown documentation file.\n\n"
            if 'headers' in analysis and analysis['headers']:
                docs += f"Contains {len(analysis['headers'])} section(s).\n\n"
        elif path_obj.suffix in ['.json', '.yaml', '.yml']:
            docs += "This is a configuration/data file.\n\n"
        else:
            docs += f"This is a text file with extension `{path_obj.suffix or 'none'}`.\n\n"

        docs += "---\n\n## Detailed Walkthrough\n\n"

        # Add detailed analysis
        if analysis['classes']:
            docs += "### Classes\n\n"
            for cls in analysis['classes'][:50]:  # Limit to 50
                docs += f"- `{cls}`\n"
            docs += "\n"

        if analysis['functions']:
            docs += "### Functions\n\n"
            for func in analysis['functions'][:100]:  # Limit to 100
                if isinstance(func, dict):
                    params = func.get('params', '')
                    docs += f"- `{func['name']}({params})`\n"
                else:
                    docs += f"- `{func}`\n"
            docs += "\n"

        if analysis['imports']:
            docs += "### Dependencies/Imports\n\n"
            for imp in sorted(set(analysis['imports']))[:50]:  # Limit to 50
                docs += f"- `{imp}`\n"
            docs += "\n"

        if 'headers' in analysis and analysis['headers']:
            docs += "### Document Structure\n\n"
            for header in analysis['headers']:
                docs += f"- {header}\n"
            docs += "\n"

        docs += """---

## Performance & Security Notes

"""

        # Add file-specific notes
        if path_obj.suffix == '.py':
            docs += "- Ensure proper error handling is implemented\n"
            docs += "- Review for potential security vulnerabilities (SQL injection, XSS, etc.)\n"
            docs += "- Consider performance implications of loops and recursive functions\n"
        elif 'test' in str(rel_path).lower():
            docs += "- This appears to be a test file\n"
            docs += "- Ensure tests are comprehensive and cover edge cases\n"
        elif path_obj.suffix in ['.json', '.yaml', '.yml']:
            docs += "- Verify that sensitive data is not committed to version control\n"
            docs += "- Validate configuration values\n"

        docs += """
---

## Related Files

See the folder index for related files in the same directory.

---

## Tests / How to Run

"""

        if path_obj.suffix == '.py':
            docs += "```bash\n# Run this file\npython " + str(rel_path) + "\n\n# Run tests (if this is a test file)\npytest " + str(rel_path) + "\n```\n"
        elif path_obj.suffix in ['.js', '.ts']:
            docs += "```bash\n# Run with Node.js\nnode " + str(rel_path) + "\n```\n"
        elif path_obj.suffix == '.md':
            docs += "This is a documentation file. View it in a Markdown viewer or on GitHub.\n"
        else:
            docs += "Refer to the project README for instructions on how to use this file.\n"

        docs += f"\n---\n\n*Documentation generated for `{rel_path}`*\n"

        return docs

    def create_keywords_content(self, rel_path, path_obj, keywords, analysis):
        """Create keywords documentation"""
        kw_content = f"""# Keywords Index: {path_obj.name}

## File Information
- **Path**: `{rel_path}`
- **Total Keywords**: {len(keywords)}

---

## Keywords (A-Z)

"""

        # Group keywords by first letter
        grouped = defaultdict(list)
        for kw in keywords:
            first_letter = kw[0].upper()
            grouped[first_letter].append(kw)

        for letter in sorted(grouped.keys()):
            kw_content += f"### {letter}\n\n"
            for kw in sorted(grouped[letter])[:50]:  # Limit per letter
                # Create anchor link to docs
                docs_file = f"{path_obj.stem}_docs.md"
                kw_content += f"- **{kw}** - See [{docs_file}]({docs_file})\n"
            kw_content += "\n"

        kw_content += "---\n\n"

        # Add notable symbols
        if analysis['classes']:
            kw_content += "## Classes\n\n"
            for cls in sorted(set(analysis['classes']))[:30]:
                kw_content += f"- `{cls}`\n"
            kw_content += "\n"

        if analysis['functions']:
            kw_content += "## Functions\n\n"
            func_names = []
            for func in analysis['functions']:
                if isinstance(func, dict):
                    func_names.append(func['name'])
                else:
                    func_names.append(func)

            for func in sorted(set(func_names))[:30]:
                kw_content += f"- `{func}`\n"
            kw_content += "\n"

        return kw_content

    def process_all_files(self, limit=None):
        """Process all text files in the repository"""
        files_to_process = [f for f in self.file_tree.keys()]

        if limit:
            files_to_process = files_to_process[:limit]

        total = len(files_to_process)
        print(f"Processing {total} files...")

        for i, rel_path in enumerate(files_to_process, 1):
            if i % 100 == 0:
                print(f"Progress: {i}/{total} files processed")

            try:
                created = self.generate_file_docs(rel_path)
                self.created_docs += created
                self.processed_files += 1
            except Exception as e:
                print(f"Error processing {rel_path}: {e}")

        print(f"\nCompleted! Processed {self.processed_files} files, created {self.created_docs} documentation files")
        return self.processed_files, self.created_docs

def main():
    generator = FileDocGenerator()
    processed, created = generator.process_all_files()

    print(f"\nSummary:")
    print(f"  Files processed: {processed}")
    print(f"  Docs created: {created}")

    return processed, created

if __name__ == "__main__":
    main()
