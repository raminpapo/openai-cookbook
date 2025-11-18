# Documentation: generate_docs.py

## File Metadata
- **Path**: `generate_docs.py`
- **Type**: .py file
- **Size**: 45,853 bytes (44.78 KB)
- **Lines**: 1,268
- **Words**: 3,899
- **Characters**: 45,821

## Original Source

```python
#!/usr/bin/env python3
"""
World's Best Repo Book Generator and Index Builder
Generates comprehensive documentation for the entire repository.
"""

import os
import json
import hashlib
import mimetypes
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import subprocess

class RepoBookGenerator:
    def __init__(self, repo_root, docs_dir="./docs"):
        self.repo_root = Path(repo_root).resolve()
        self.docs_dir = Path(docs_dir).resolve()
        self.manifest = {
            "generator_version": "1.0.0",
            "repo_source": "",
            "repo_fingerprint": "",
            "files_scanned": 0,
            "docs_created": 0,
            "bytes_written": 0,
            "total_words_estimated": 0,
            "timestamp_start": datetime.utcnow().isoformat(),
            "timestamp_end": None,
            "file_map": {},
            "checksums": {}
        }
        self.progress_log = []
        self.errors = []
        self.binary_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
            '.pdf', '.zip', '.tar', '.gz', '.bz2', '.xz',
            '.pyc', '.pyo', '.so', '.dylib', '.dll', '.exe',
            '.woff', '.woff2', '.ttf', '.eot', '.otf',
            '.mp3', '.mp4', '.avi', '.mov', '.wav',
            '.pkl', '.pickle', '.npy', '.npz', '.h5', '.hdf5',
            '.db', '.sqlite', '.sqlite3'
        }
        self.skipped_files = []
        self.keywords_global = defaultdict(lambda: {"files": set(), "description": ""})

    def get_repo_fingerprint(self):
        """Get repository fingerprint from git commit or file hash."""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', 'HEAD'],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass

        # Fallback: hash of file list
        files = sorted([str(f.relative_to(self.repo_root))
                       for f in self.repo_root.rglob('*')
                       if f.is_file() and '.git' not in str(f)])
        return hashlib.sha256('\n'.join(files).encode()).hexdigest()[:40]

    def get_repo_source(self):
        """Get repository source URL."""
        try:
            result = subprocess.run(
                ['git', 'remote', 'get-url', 'origin'],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        return str(self.repo_root)

    def is_binary_file(self, file_path):
        """Check if file is binary."""
        ext = file_path.suffix.lower()
        if ext in self.binary_extensions:
            return True

        # Try to read first 8KB to check for binary content
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(8192)
                if b'\x00' in chunk:  # Null bytes indicate binary
                    return True
        except:
            return True
        return False

    def classify_file(self, file_path):
        """Classify file as text, binary, or large."""
        if self.is_binary_file(file_path):
            return "binary"

        try:
            size = file_path.stat().st_size
            if size > 100 * 1024 * 1024:  # 100MB
                return "very_large"
            return "text"
        except:
            return "unreadable"

    def scan_repository(self):
        """Phase 1: Scan and classify all files."""
        print("=== Phase 1: Scanning Repository ===")

        self.manifest["repo_source"] = self.get_repo_source()
        self.manifest["repo_fingerprint"] = self.get_repo_fingerprint()

        all_files = []
        for file_path in self.repo_root.rglob('*'):
            if file_path.is_file():
                # Skip .git and docs directories
                rel_path = file_path.relative_to(self.repo_root)
                if '.git' in rel_path.parts or 'docs' in rel_path.parts[:1]:
                    continue
                all_files.append(file_path)

        self.manifest["files_scanned"] = len(all_files)
        print(f"Found {len(all_files)} files to process")

        # Classify files
        for file_path in all_files:
            rel_path = str(file_path.relative_to(self.repo_root))
            classification = self.classify_file(file_path)
            self.manifest["file_map"][rel_path] = {
                "classification": classification,
                "size": file_path.stat().st_size if file_path.exists() else 0,
                "extension": file_path.suffix
            }

        # Save initial manifest
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = self.docs_dir / "manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2, default=str)

        print(f"Manifest created at {manifest_path}")
        return all_files

    def extract_keywords(self, content, file_path):
        """Extract keywords from content."""
        keywords = set()

        # Extract identifiers (functions, classes, variables)
        # Python/JS style
        keywords.update(re.findall(r'\bdef\s+(\w+)', content))
        keywords.update(re.findall(r'\bclass\s+(\w+)', content))
        keywords.update(re.findall(r'\bconst\s+(\w+)', content))
        keywords.update(re.findall(r'\blet\s+(\w+)', content))
        keywords.update(re.findall(r'\bvar\s+(\w+)', content))
        keywords.update(re.findall(r'\bfunction\s+(\w+)', content))

        # Extract imports
        keywords.update(re.findall(r'\bimport\s+(\w+)', content))
        keywords.update(re.findall(r'\bfrom\s+(\w+)', content))

        # Extract camelCase and snake_case identifiers (filter length)
        identifiers = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]{2,}\b', content)
        keywords.update([w for w in identifiers if len(w) >= 3 and len(w) <= 50])

        # Remove common words
        common_words = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'import',
                       'return', 'self', 'true', 'false', 'null', 'none', 'undefined',
                       'var', 'let', 'const', 'function', 'class', 'def', 'if', 'else'}
        keywords = {k for k in keywords if k.lower() not in common_words}

        return sorted(list(keywords))[:5000]  # Limit to 5000 keywords per file

    def generate_file_docs(self, file_path, all_files):
        """Generate _docs.md for a single file."""
        rel_path = file_path.relative_to(self.repo_root)
        classification = self.manifest["file_map"].get(str(rel_path), {}).get("classification", "unknown")

        # Create mirror directory structure
        doc_dir = self.docs_dir / rel_path.parent
        doc_dir.mkdir(parents=True, exist_ok=True)

        # Handle binary files
        if classification == "binary":
            docs_content = self.generate_binary_file_docs(file_path)
            kw_content = f"# Keywords: {file_path.name}\n\n*Binary file - no keywords extracted*\n"
        else:
            # Read file content
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except Exception as e:
                self.errors.append(f"Failed to read {rel_path}: {str(e)}")
                return 0

            docs_content = self.generate_text_file_docs(file_path, content, all_files)
            keywords = self.extract_keywords(content, file_path)
            kw_content = self.generate_keywords_doc(file_path, keywords)

            # Add to global keywords
            for kw in keywords:
                self.keywords_global[kw]["files"].add(str(rel_path))

        # Write docs
        docs_path = doc_dir / f"{file_path.name}_docs.md"
        kw_path = doc_dir / f"{file_path.name}_kw.md"

        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(docs_content)

        with open(kw_path, 'w', encoding='utf-8') as f:
            f.write(kw_content)

        self.manifest["docs_created"] += 2
        bytes_written = len(docs_content) + len(kw_content)
        self.manifest["bytes_written"] += bytes_written

        return bytes_written

    def generate_binary_file_docs(self, file_path):
        """Generate documentation for binary files."""
        rel_path = file_path.relative_to(self.repo_root)
        size = file_path.stat().st_size
        mime_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

        return f"""# Documentation: {file_path.name}

## File Metadata
- **Path**: `{rel_path}`
- **Type**: Binary file
- **Size**: {size:,} bytes ({size / 1024:.2f} KB)
- **MIME Type**: {mime_type}
- **Extension**: {file_path.suffix}

## Description
This is a binary file that cannot be processed as text.

## Suggested Handling
- **Images** (png, jpg, etc.): View with image viewer
- **Archives** (zip, tar.gz, etc.): Extract contents
- **Compiled files** (pyc, so, dll, etc.): Generated artifacts
- **Data files** (pkl, npy, h5, etc.): Load with appropriate library

## Related Files
*See folder index for related files in the same directory.*
"""

    def generate_text_file_docs(self, file_path, content, all_files):
        """Generate comprehensive documentation for text files."""
        rel_path = file_path.relative_to(self.repo_root)
        size = file_path.stat().st_size
        lines = content.split('\n')
        word_count = len(content.split())

        # Truncate very large files for source display
        max_source_lines = 10000
        if len(lines) > max_source_lines:
            source_display = '\n'.join(lines[:max_source_lines]) + f"\n\n... (truncated {len(lines) - max_source_lines} lines) ..."
            truncated = True
        else:
            source_display = content
            truncated = False

        # Analyze content
        overview = self.generate_overview(file_path, content)
        detailed_analysis = self.generate_detailed_analysis(file_path, content)
        related_files = self.find_related_files(file_path, content, all_files)

        docs = f"""# Documentation: {file_path.name}

## File Metadata
- **Path**: `{rel_path}`
- **Type**: {file_path.suffix or 'No extension'} file
- **Size**: {size:,} bytes ({size / 1024:.2f} KB)
- **Lines**: {len(lines):,}
- **Words**: {word_count:,}
- **Characters**: {len(content):,}

## Original Source

```{self.get_language_hint(file_path)}
{source_display}
```

{'**Note**: Source truncated for display. Full file is ' + str(len(lines)) + ' lines.' if truncated else ''}

## High-Level Overview

{overview}

## Detailed Analysis

{detailed_analysis}

## Usage & Examples

{self.generate_usage_examples(file_path, content)}

## Performance & Security Notes

{self.generate_performance_security_notes(file_path, content)}

## Related Files

{related_files}

## Testing & Execution

{self.generate_testing_info(file_path, content)}

---
*Generated by Repo Book Generator v1.0.0*
"""

        return docs

    def get_language_hint(self, file_path):
        """Get language hint for code blocks."""
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'jsx',
            '.tsx': 'tsx',
            '.md': 'markdown',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.sh': 'bash',
            '.bash': 'bash',
            '.html': 'html',
            '.css': 'css',
            '.ipynb': 'json',
            '.txt': 'text',
            '.sql': 'sql',
            '.r': 'r',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.php': 'php',
        }
        return ext_map.get(file_path.suffix.lower(), '')

    def generate_overview(self, file_path, content):
        """Generate high-level overview."""
        ext = file_path.suffix.lower()

        if ext == '.md':
            first_heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if first_heading:
                return f"Markdown documentation file: **{first_heading.group(1)}**\n\nThis file contains documentation in Markdown format."

        elif ext == '.py':
            docstring = re.search(r'"""(.+?)"""', content, re.DOTALL)
            if docstring:
                return f"Python module.\n\n{docstring.group(1).strip()}"
            return "Python source file containing code implementation."

        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            return "JavaScript/TypeScript source file containing code implementation."

        elif ext == '.json':
            return "JSON data file containing structured configuration or data."

        elif ext in ['.yaml', '.yml']:
            return "YAML configuration file."

        elif ext == '.ipynb':
            return "Jupyter Notebook containing interactive code cells and documentation."

        elif ext in ['.sh', '.bash']:
            return "Shell script for automation and command execution."

        return f"Source file of type {ext}."

    def generate_detailed_analysis(self, file_path, content):
        """Generate detailed walkthrough."""
        ext = file_path.suffix.lower()
        analysis = []

        if ext == '.py':
            # Find classes
            classes = re.findall(r'class\s+(\w+).*?:', content)
            if classes:
                analysis.append(f"**Classes**: {', '.join(classes)}")

            # Find functions
            functions = re.findall(r'def\s+(\w+)\s*\(', content)
            if functions:
                analysis.append(f"**Functions**: {', '.join(functions[:20])}" +
                              (" ..." if len(functions) > 20 else ""))

            # Find imports
            imports = re.findall(r'(?:from|import)\s+([\w.]+)', content)
            if imports:
                unique_imports = sorted(set(imports))[:15]
                analysis.append(f"**Dependencies**: {', '.join(unique_imports)}" +
                              (" ..." if len(set(imports)) > 15 else ""))

        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # Find functions
            functions = re.findall(r'(?:function\s+(\w+)|const\s+(\w+)\s*=.*?(?:=>|\bfunction\b))', content)
            func_names = [f[0] or f[1] for f in functions if f[0] or f[1]]
            if func_names:
                analysis.append(f"**Functions**: {', '.join(func_names[:20])}" +
                              (" ..." if len(func_names) > 20 else ""))

            # Find imports
            imports = re.findall(r'import.*?from\s+[\'"](.+?)[\'"]', content)
            if imports:
                analysis.append(f"**Dependencies**: {', '.join(sorted(set(imports))[:15])}" +
                              (" ..." if len(set(imports)) > 15 else ""))

        elif ext == '.md':
            headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
            if headings:
                toc = []
                for level, title in headings[:30]:
                    indent = "  " * (len(level) - 1)
                    toc.append(f"{indent}- {title}")
                analysis.append("**Table of Contents**:\n" + '\n'.join(toc))

        elif ext == '.json':
            try:
                data = json.loads(content)
                analysis.append(f"**Top-level keys**: {', '.join(list(data.keys())[:20])}")
            except:
                analysis.append("JSON structure (parsing details unavailable)")

        if not analysis:
            lines = content.split('\n')
            non_empty = [l for l in lines if l.strip() and not l.strip().startswith('#')]
            if len(non_empty) > 0:
                analysis.append(f"File contains {len(lines)} lines with structured content.")

        return '\n\n'.join(analysis) if analysis else "No detailed structure analysis available."

    def generate_usage_examples(self, file_path, content):
        """Generate usage examples."""
        ext = file_path.suffix.lower()

        if ext == '.py':
            if 'if __name__ == "__main__"' in content:
                return f"This script can be executed directly:\n\n```bash\npython {file_path.name}\n```"
            return f"Import this module in Python:\n\n```python\nimport {file_path.stem}\n```"

        elif ext in ['.js', '.ts']:
            return f"Import this module:\n\n```javascript\nimport {{ ... }} from './{file_path.name}';\n```"

        elif ext == '.sh':
            return f"Execute this script:\n\n```bash\nbash {file_path.name}\n```"

        elif ext == '.ipynb':
            return f"Open in Jupyter:\n\n```bash\njupyter notebook {file_path.name}\n```"

        return "See file content for usage details."

    def generate_performance_security_notes(self, file_path, content):
        """Generate performance and security notes."""
        notes = []

        # Check for potential security issues
        if re.search(r'eval\s*\(', content):
            notes.append("⚠️ **Security**: Contains `eval()` - potential code injection risk")

        if re.search(r'exec\s*\(', content):
            notes.append("⚠️ **Security**: Contains `exec()` - potential code execution risk")

        if re.search(r'(?:password|secret|api_key|token)\s*=\s*["\']', content, re.IGNORECASE):
            notes.append("⚠️ **Security**: May contain hardcoded credentials - review carefully")

        # Check for performance considerations
        if re.search(r'\bfor\b.*\bfor\b', content):
            notes.append("📊 **Performance**: Contains nested loops - consider complexity")

        if len(content) > 50000:
            notes.append("📊 **Performance**: Large file - may impact load times")

        if not notes:
            notes.append("No specific performance or security concerns identified.")

        return '\n'.join(notes)

    def find_related_files(self, file_path, content, all_files):
        """Find related files based on imports and references."""
        related = []
        rel_path = file_path.relative_to(self.repo_root)

        # Files in same directory
        same_dir = [f for f in all_files
                   if f.parent == file_path.parent and f != file_path]
        if same_dir:
            related.append("**Same directory**:")
            for f in same_dir[:10]:
                related.append(f"- [{f.name}](./{f.name}_docs.md)")

        # Extract import paths and try to resolve
        imports = re.findall(r'(?:from|import)\s+([\w./]+)', content)
        if imports:
            related.append("\n**Imported modules**:")
            for imp in sorted(set(imports))[:15]:
                related.append(f"- `{imp}`")

        return '\n'.join(related) if related else "*No related files identified.*"

    def generate_testing_info(self, file_path, content):
        """Generate testing information."""
        ext = file_path.suffix.lower()

        if 'test' in file_path.name.lower():
            return f"This is a test file. Run with appropriate test framework."

        if ext == '.py':
            if 'pytest' in content or 'unittest' in content:
                return "Contains tests. Run with pytest or unittest framework."
            return "For testing, create a corresponding test file."

        elif ext == '.ipynb':
            return "Execute cells sequentially in Jupyter environment."

        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            if 'jest' in content or 'test(' in content:
                return "Contains tests. Run with Jest or configured test framework."
            return "For testing, create corresponding .test.js or .spec.js file."

        return "See project documentation for testing procedures."

    def generate_keywords_doc(self, file_path, keywords):
        """Generate keywords documentation."""
        rel_path = file_path.relative_to(self.repo_root)

        doc = f"""# Keywords: {file_path.name}

**Source**: `{rel_path}`
**Keyword Count**: {len(keywords)}

## Extracted Keywords

"""

        # Group keywords alphabetically
        from itertools import groupby
        for letter, group in groupby(keywords, key=lambda x: x[0].upper()):
            kw_list = list(group)
            doc += f"### {letter}\n\n"
            for kw in kw_list:
                anchor = kw.lower().replace('_', '-')
                doc += f"- **{kw}** → [docs](./{file_path.name}_docs.md#{anchor})\n"
            doc += "\n"

        return doc

    def process_all_files(self, all_files):
        """Phase 2: Process all files."""
        print(f"\n=== Phase 2: Generating Per-File Documentation ===")
        print(f"Processing {len(all_files)} files...")

        text_files = [f for f in all_files
                     if self.manifest["file_map"].get(str(f.relative_to(self.repo_root)), {})
                        .get("classification") in ["text", "binary"]]

        total_bytes = 0
        for idx, file_path in enumerate(text_files):
            if idx % 100 == 0:
                print(f"  Processed {idx}/{len(text_files)} files...")

            try:
                bytes_written = self.generate_file_docs(file_path, all_files)
                total_bytes += bytes_written
                self.progress_log.append({
                    "file": str(file_path.relative_to(self.repo_root)),
                    "bytes": bytes_written,
                    "status": "success"
                })
            except Exception as e:
                self.errors.append(f"Error processing {file_path}: {str(e)}")
                self.progress_log.append({
                    "file": str(file_path.relative_to(self.repo_root)),
                    "status": "failed",
                    "error": str(e)
                })

        print(f"  Completed {len(text_files)} files, {total_bytes:,} bytes written")
        return total_bytes

    def generate_folder_docs(self):
        """Phase 3: Generate folder-level documentation."""
        print(f"\n=== Phase 3: Generating Folder Documentation ===")

        # Get all unique folders
        folders = set()
        for file_rel in self.manifest["file_map"].keys():
            path_parts = Path(file_rel).parts[:-1]  # Exclude filename
            for i in range(len(path_parts) + 1):
                folder = Path(*path_parts[:i]) if i > 0 else Path('.')
                folders.add(folder)

        folders = sorted(folders, key=lambda x: (len(x.parts), str(x)))
        print(f"Generating docs for {len(folders)} folders...")

        for folder in folders:
            self.generate_folder_index(folder)
            self.generate_folder_doc(folder)
            self.generate_folder_keywords(folder)

        print(f"  Completed {len(folders)} folders")

    def generate_folder_index(self, folder):
        """Generate index.md for a folder."""
        folder_path = self.repo_root / folder
        doc_folder = self.docs_dir / folder
        doc_folder.mkdir(parents=True, exist_ok=True)

        # Get direct children
        children_files = []
        children_dirs = set()

        for file_rel in self.manifest["file_map"].keys():
            file_path = Path(file_rel)
            if len(file_path.parts) > len(folder.parts) if folder != Path('.') else True:
                # Check if direct child
                expected_parent = file_path.parts[:len(folder.parts)] if folder != Path('.') else ()
                if (folder == Path('.') and len(file_path.parts) == 1) or \
                   (folder != Path('.') and expected_parent == folder.parts and len(file_path.parts) == len(folder.parts) + 1):
                    children_files.append(file_path)
                elif (folder == Path('.') and len(file_path.parts) > 1):
                    children_dirs.add(file_path.parts[0])
                elif folder != Path('.') and expected_parent == folder.parts and len(file_path.parts) > len(folder.parts) + 1:
                    children_dirs.add(file_path.parts[len(folder.parts)])

        folder_name = folder.name if folder != Path('.') else "Repository Root"

        content = f"""# Index: {folder_name}

**Path**: `{folder if folder != Path('.') else '/'}`

## Subdirectories

"""

        if children_dirs:
            for dir_name in sorted(children_dirs):
                rel_link = f"{dir_name}/index.md" if folder == Path('.') else f"../{folder.name}/{dir_name}/index.md"
                content += f"- 📁 [{dir_name}]({rel_link})\n"
        else:
            content += "*No subdirectories*\n"

        content += "\n## Files\n\n"

        if children_files:
            for file_path in sorted(children_files):
                file_name = file_path.name
                content += f"- 📄 [{file_name}](./{file_name}_docs.md)\n"
        else:
            content += "*No files*\n"

        content += "\n---\n*Auto-generated index*\n"

        index_path = doc_folder / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)

    def generate_folder_doc(self, folder):
        """Generate doc.md for a folder."""
        doc_folder = self.docs_dir / folder
        folder_name = folder.name if folder != Path('.') else "Repository Root"

        # Analyze folder purpose
        purpose = self.infer_folder_purpose(folder)

        content = f"""# Folder Documentation: {folder_name}

**Path**: `{folder if folder != Path('.') else '/'}`

## Purpose

{purpose}

## Contents Overview

See [index.md](./index.md) for complete file and folder listing.

## Key Concepts

*This folder contains various files related to {folder_name.replace('_', ' ').replace('-', ' ')}.*

---
*Auto-generated folder documentation*
"""

        doc_path = doc_folder / "doc.md"
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)

    def infer_folder_purpose(self, folder):
        """Infer folder purpose from name and contents."""
        folder_name = folder.name if folder != Path('.') else "root"

        purpose_map = {
            'examples': "Contains example code and demonstrations",
            'tests': "Contains test files and test utilities",
            'docs': "Contains documentation files",
            'src': "Contains source code",
            'lib': "Contains library code",
            'bin': "Contains binary executables and scripts",
            'config': "Contains configuration files",
            'data': "Contains data files",
            'images': "Contains image assets",
            'assets': "Contains static assets",
            'scripts': "Contains utility scripts",
            'tools': "Contains development tools",
            'utils': "Contains utility functions",
            '.github': "Contains GitHub-specific configuration (workflows, templates)",
            'articles': "Contains article content and documentation",
        }

        for key, purpose in purpose_map.items():
            if key in folder_name.lower():
                return purpose

        return f"This folder organizes files related to {folder_name.replace('_', ' ').replace('-', ' ')}."

    def generate_folder_keywords(self, folder):
        """Generate sub.md (keyword aggregation) for a folder."""
        doc_folder = self.docs_dir / folder
        folder_name = folder.name if folder != Path('.') else "Repository Root"

        # Collect all keywords from files in this folder and subfolders
        folder_keywords = defaultdict(list)

        for file_rel, file_info in self.manifest["file_map"].items():
            file_path = Path(file_rel)
            # Check if file is in this folder or subfolder
            if folder == Path('.') or (len(file_path.parts) > len(folder.parts) and
                                       file_path.parts[:len(folder.parts)] == folder.parts):
                # Read corresponding _kw.md if exists
                kw_file = self.docs_dir / file_path.parent / f"{file_path.name}_kw.md"
                if kw_file.exists():
                    try:
                        with open(kw_file, 'r', encoding='utf-8') as f:
                            kw_content = f.read()
                            keywords = re.findall(r'\*\*(\w+)\*\*', kw_content)
                            for kw in keywords:
                                folder_keywords[kw].append(str(file_path))
                    except:
                        pass

        content = f"""# Aggregated Keywords: {folder_name}

**Path**: `{folder if folder != Path('.') else '/'}`
**Total Unique Keywords**: {len(folder_keywords)}

## Keywords A-Z

"""

        if folder_keywords:
            from itertools import groupby
            sorted_kw = sorted(folder_keywords.keys())
            for letter, group in groupby(sorted_kw, key=lambda x: x[0].upper()):
                content += f"### {letter}\n\n"
                for kw in group:
                    files = folder_keywords[kw]
                    file_links = ', '.join([f"[{Path(f).name}](./{Path(f).name}_docs.md)"
                                           for f in files[:5]])
                    if len(files) > 5:
                        file_links += f" ... ({len(files)} total)"
                    content += f"- **{kw}**: {file_links}\n"
                content += "\n"
        else:
            content += "*No keywords found*\n"

        content += "\n---\n*Auto-generated keyword aggregation*\n"

        sub_path = doc_folder / "sub.md"
        with open(sub_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)

    def generate_global_keywords(self):
        """Generate global keywords.md."""
        print(f"\n=== Generating Global Keywords ===")

        content = f"""# Global Keyword Index

**Repository**: {self.manifest['repo_source']}
**Total Keywords**: {len(self.keywords_global)}

## Keywords A-Z

"""

        from itertools import groupby
        sorted_kw = sorted(self.keywords_global.keys())

        for letter, group in groupby(sorted_kw, key=lambda x: x[0].upper() if x else 'Z'):
            content += f"### {letter}\n\n"
            for kw in group:
                files = sorted(self.keywords_global[kw]["files"])
                file_links = []
                for f in files[:10]:
                    file_path = Path(f)
                    rel_link = f"{f}_docs.md"
                    file_links.append(f"[{file_path.name}]({rel_link})")

                links_str = ', '.join(file_links)
                if len(files) > 10:
                    links_str += f" ... ({len(files)} total)"

                content += f"- **{kw}**: {links_str}\n"
            content += "\n"

        keywords_path = self.docs_dir / "keywords.md"
        with open(keywords_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)
        print(f"  Generated keywords.md with {len(self.keywords_global)} keywords")

    def generate_global_index(self):
        """Generate global index.md."""
        print(f"\n=== Generating Global Index ===")

        content = f"""# Repository Documentation Index

**Repository**: {self.manifest['repo_source']}
**Commit**: {self.manifest['repo_fingerprint']}
**Generated**: {datetime.utcnow().isoformat()}

## Quick Links

- [Comprehensive Book](./comprehensive_book.md) - Complete documentation in book format
- [Global Keywords](./keywords.md) - All keywords A-Z
- [Verification Report](./verification_report.md) - Quality assurance report
- [Manifest](./manifest.json) - Generation metadata

## Folder Structure

"""

        # Get all folders
        folders = set()
        for file_rel in self.manifest["file_map"].keys():
            path_parts = Path(file_rel).parts[:-1]
            if path_parts:
                folders.add(Path(*path_parts))

        # Build tree
        root_items = []
        for file_rel in self.manifest["file_map"].keys():
            file_path = Path(file_rel)
            if len(file_path.parts) == 1:
                root_items.append(('file', file_path.name))

        root_folders = set()
        for folder in sorted(folders):
            if len(folder.parts) == 1:
                root_folders.add(folder.name)

        for folder_name in sorted(root_folders):
            content += f"- 📁 [{folder_name}](./{folder_name}/index.md)\n"

        content += "\n## Root Files\n\n"
        root_files = [item[1] for item in root_items if item[0] == 'file']
        for file_name in sorted(root_files)[:50]:
            content += f"- 📄 [{file_name}](./{file_name}_docs.md)\n"

        if len(root_files) > 50:
            content += f"\n*... and {len(root_files) - 50} more files*\n"

        content += f"""

## Statistics

- **Files Scanned**: {self.manifest['files_scanned']:,}
- **Docs Created**: {self.manifest['docs_created']:,}
- **Bytes Written**: {self.manifest['bytes_written']:,}

---
*Auto-generated repository index*
"""

        index_path = self.docs_dir / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)
        print(f"  Generated index.md")

    def generate_comprehensive_book(self):
        """Generate comprehensive_book.md."""
        print(f"\n=== Generating Comprehensive Book ===")

        book_path = self.docs_dir / "comprehensive_book.md"

        with open(book_path, 'w', encoding='utf-8') as book:
            # Header
            header = f"""# Comprehensive Repository Documentation Book

**Repository**: {self.manifest['repo_source']}
**Commit**: {self.manifest['repo_fingerprint']}
**Generated**: {datetime.utcnow().isoformat()}

---

# Table of Contents

1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Detailed Documentation](#detailed-documentation)

---

# Introduction

This book contains comprehensive documentation for the entire repository, organized by folder and file.

"""
            book.write(header)
            self.manifest["bytes_written"] += len(header)

            # Get all folders sorted
            folders = set()
            for file_rel in self.manifest["file_map"].keys():
                path_parts = Path(file_rel).parts[:-1]
                for i in range(len(path_parts) + 1):
                    folder = Path(*path_parts[:i]) if i > 0 else Path('.')
                    folders.add(folder)

            folders = sorted(folders, key=lambda x: (len(x.parts), str(x)))

            # Add folder chapters
            book.write("\n# Folder Structure\n\n")
            for folder in folders:
                doc_file = self.docs_dir / folder / "doc.md"
                if doc_file.exists():
                    with open(doc_file, 'r', encoding='utf-8') as f:
                        folder_doc = f.read()
                        book.write(f"\n## Chapter: {folder}\n\n")
                        book.write(folder_doc)
                        book.write("\n\n---\n\n")
                        self.manifest["bytes_written"] += len(folder_doc)

            # Add file summaries (not full docs to keep manageable)
            book.write("\n# File Summaries\n\n")
            book.write("*For full file documentation, see individual file docs.*\n\n")

            file_count = 0
            for file_rel in sorted(self.manifest["file_map"].keys())[:200]:  # Limit to first 200 for book
                file_path = Path(file_rel)
                summary = f"- **{file_rel}**: {self.manifest['file_map'][file_rel].get('classification', 'unknown')} file\n"
                book.write(summary)
                self.manifest["bytes_written"] += len(summary)
                file_count += 1

            if len(self.manifest["file_map"]) > 200:
                remaining = f"\n*... and {len(self.manifest['file_map']) - 200} more files. See index.md for complete listing.*\n"
                book.write(remaining)
                self.manifest["bytes_written"] += len(remaining)

            footer = "\n\n---\n*End of Comprehensive Book*\n"
            book.write(footer)
            self.manifest["bytes_written"] += len(footer)

        self.manifest["docs_created"] += 1
        print(f"  Generated comprehensive_book.md")

    def validate_links(self):
        """Phase 5: Validate all links."""
        print(f"\n=== Phase 5: Validating Links ===")

        broken_links = []

        # Check all markdown files
        for md_file in self.docs_dir.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find markdown links
                    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                    for text, link in links:
                        if link.startswith('http'):
                            continue  # Skip external links
                        # Check relative link
                        target = (md_file.parent / link).resolve()
                        if not target.exists():
                            broken_links.append({
                                "file": str(md_file.relative_to(self.docs_dir)),
                                "link": link,
                                "text": text
                            })
            except:
                pass

        print(f"  Found {len(broken_links)} broken links")
        return broken_links

    def generate_verification_report(self, broken_links):
        """Generate verification_report.md."""
        print(f"\n=== Generating Verification Report ===")

        content = f"""# Verification Report

**Generated**: {datetime.utcnow().isoformat()}

## Summary

- **Files Scanned**: {self.manifest['files_scanned']:,}
- **Docs Created**: {self.manifest['docs_created']:,}
- **Errors**: {len(self.errors)}
- **Broken Links**: {len(broken_links)}
- **Skipped Files**: {len(self.skipped_files)}

## Errors Encountered

"""

        if self.errors:
            for error in self.errors[:100]:
                content += f"- {error}\n"
            if len(self.errors) > 100:
                content += f"\n*... and {len(self.errors) - 100} more errors*\n"
        else:
            content += "*No errors*\n"

        content += "\n## Broken Links\n\n"

        if broken_links:
            for link in broken_links[:100]:
                content += f"- **{link['file']}**: `{link['link']}` (text: \"{link['text']}\")\n"
            if len(broken_links) > 100:
                content += f"\n*... and {len(broken_links) - 100} more broken links*\n"
        else:
            content += "*No broken links found*\n"

        content += "\n## Skipped Files\n\n"

        binary_count = sum(1 for f in self.manifest["file_map"].values()
                          if f.get("classification") == "binary")
        content += f"- **Binary files**: {binary_count}\n"

        large_count = sum(1 for f in self.manifest["file_map"].values()
                         if f.get("classification") == "very_large")
        content += f"- **Very large files**: {large_count}\n"

        content += "\n## Checksums\n\n"
        content += "*Checksums will be added to manifest.json*\n"

        content += "\n---\n*Verification complete*\n"

        report_path = self.docs_dir / "verification_report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)
        print(f"  Generated verification_report.md")

    def compute_checksums(self):
        """Compute SHA256 checksums for all generated files."""
        print(f"\n=== Computing Checksums ===")

        checksums = {}
        md_files = list(self.docs_dir.rglob('*.md'))

        for md_file in md_files:
            try:
                with open(md_file, 'rb') as f:
                    content = f.read()
                    checksum = hashlib.sha256(content).hexdigest()
                    rel_path = str(md_file.relative_to(self.docs_dir))
                    checksums[rel_path] = checksum
            except:
                pass

        self.manifest["checksums"] = checksums
        print(f"  Computed {len(checksums)} checksums")

    def finalize_manifest(self):
        """Finalize and save manifest."""
        print(f"\n=== Finalizing Manifest ===")

        self.manifest["timestamp_end"] = datetime.utcnow().isoformat()
        self.manifest["errors"] = self.errors

        # Estimate words
        total_words = 0
        for md_file in self.docs_dir.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    total_words += len(content.split())
            except:
                pass

        self.manifest["total_words_estimated"] = total_words

        manifest_path = self.docs_dir / "manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2, default=str)

        print(f"  Saved manifest.json")
        print(f"  Total words estimated: {total_words:,}")

    def generate_readme(self):
        """Generate docs/README.md."""
        print(f"\n=== Generating README ===")

        content = f"""# Repository Documentation

Auto-generated documentation for the entire repository.

## Organization

This documentation is organized as follows:

### Root Files

- **index.md**: Master index with links to all folders
- **keywords.md**: Global keyword index (A-Z)
- **comprehensive_book.md**: Complete documentation in book format
- **verification_report.md**: Quality assurance and validation report
- **manifest.json**: Generation metadata and checksums

### Per-Folder Documentation

Each folder contains:
- **index.md**: Folder index listing files and subfolders
- **doc.md**: Narrative documentation about the folder's purpose
- **sub.md**: Aggregated keywords from all files in the folder

### Per-File Documentation

Each file has:
- **filename_docs.md**: Comprehensive documentation including:
  - File metadata
  - Full source code
  - High-level overview
  - Detailed analysis
  - Usage examples
  - Performance & security notes
  - Related files
  - Testing information

- **filename_kw.md**: Extracted keywords with links to docs

## Statistics

- **Repository**: {self.manifest['repo_source']}
- **Commit**: {self.manifest['repo_fingerprint']}
- **Files Scanned**: {self.manifest['files_scanned']:,}
- **Docs Created**: {self.manifest['docs_created']:,}
- **Bytes Written**: {self.manifest['bytes_written']:,}
- **Words**: ~{self.manifest.get('total_words_estimated', 0):,}

## How to Use

1. Start with **index.md** for an overview
2. Browse **keywords.md** to find specific topics
3. Read **comprehensive_book.md** for a linear narrative
4. Dive into individual file docs for details

## Resuming/Expanding

To regenerate or expand documentation:

```bash
python3 generate_docs.py
```

The generator is idempotent - running it again will update existing docs.

## Quality Assurance

See **verification_report.md** for:
- Broken links
- Processing errors
- Skipped files
- File checksums

---
Generated: {datetime.utcnow().isoformat()}
"""

        readme_path = self.docs_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.manifest["docs_created"] += 1
        self.manifest["bytes_written"] += len(content)
        print(f"  Generated README.md")

    def run(self):
        """Main execution flow."""
        print("\n" + "="*60)
        print("WORLD'S BEST REPO BOOK GENERATOR")
        print("="*60)

        # Phase 1: Bootstrap and scan
        all_files = self.scan_repository()

        # Phase 2: Generate per-file docs
        self.process_all_files(all_files)

        # Phase 3: Generate folder docs
        self.generate_folder_docs()

        # Phase 4: Generate global artifacts
        self.generate_global_keywords()
        self.generate_global_index()
        self.generate_comprehensive_book()

        # Phase 5: Validation
        broken_links = self.validate_links()
        self.generate_verification_report(broken_links)

        # Phase 6: Finalization
        self.compute_checksums()
        self.finalize_manifest()
        self.generate_readme()

        # Summary
        print("\n" + "="*60)
        print("GENERATION COMPLETE")
        print("="*60)

        summary = {
            "repo_source": self.manifest["repo_source"],
            "repo_fingerprint": self.manifest["repo_fingerprint"],
            "files_scanned": self.manifest["files_scanned"],
            "docs_created": self.manifest["docs_created"],
            "words_estimated": self.manifest.get("total_words_estimated", 0),
            "bytes_written": self.manifest["bytes_written"],
            "errors": self.errors[:10]  # First 10 errors
        }

        print(json.dumps(summary, indent=2))

        return summary


if __name__ == "__main__":
    generator = RepoBookGenerator("/home/user/openai-cookbook", "./docs")
    summary = generator.run()

    print("\n\nJSON Summary:")
    print(json.dumps(summary, indent=2))

```



## High-Level Overview

Python module.

World's Best Repo Book Generator and Index Builder
Generates comprehensive documentation for the entire repository.

## Detailed Analysis

**Classes**: RepoBookGenerator

**Functions**: __init__, get_repo_fingerprint, get_repo_source, is_binary_file, classify_file, scan_repository, extract_keywords, generate_file_docs, generate_binary_file_docs, generate_text_file_docs, get_language_hint, generate_overview, generate_detailed_analysis, generate_usage_examples, generate_performance_security_notes, find_related_files, generate_testing_info, generate_keywords_doc, process_all_files, generate_folder_docs ...

**Dependencies**: Path, all, collections, content., datetime, defaultdict, files, git, groupby, hashlib, itertools, json, mimetypes, name, os ...

## Usage & Examples

This script can be executed directly:

```bash
python generate_docs.py
```

## Performance & Security Notes

⚠️ **Security**: Contains `eval()` - potential code injection risk
⚠️ **Security**: Contains `exec()` - potential code execution risk
📊 **Performance**: Contains nested loops - consider complexity

## Related Files

**Same directory**:
- [.gitignore](./.gitignore_docs.md)
- [AGENTS.md](./AGENTS.md_docs.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md_docs.md)
- [LICENSE](./LICENSE_docs.md)
- [README.md](./README.md_docs.md)
- [authors.yaml](./authors.yaml_docs.md)
- [registry.yaml](./registry.yaml_docs.md)

**Imported modules**:
- `Path`
- `all`
- `collections`
- `content.`
- `datetime`
- `defaultdict`
- `files`
- `git`
- `groupby`
- `hashlib`
- `itertools`
- `json`
- `mimetypes`
- `name`
- `os`

## Testing & Execution

Contains tests. Run with pytest or unittest framework.

---
*Generated by Repo Book Generator v1.0.0*
