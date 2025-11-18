#!/usr/bin/env python3
"""
Folder-level documentation generator
Creates index.md, doc.md, and sub.md for each folder
"""

import os
import json
from pathlib import Path
from collections import defaultdict

class FolderDocGenerator:
    def __init__(self, repo_path=".", output_dir="./docs"):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()

        # Load file tree
        with open(self.output_dir / "file_tree.json", 'r') as f:
            self.file_tree = json.load(f)

        self.folders_processed = 0
        self.docs_created = 0

    def get_folder_structure(self):
        """Build a folder hierarchy"""
        folders = defaultdict(lambda: {"files": [], "subdirs": set()})

        # Add root
        folders["."] = {"files": [], "subdirs": set()}

        for file_path in self.file_tree.keys():
            path = Path(file_path)
            current = path.parent if path.parent != Path('.') else Path('.')

            # Add file to its directory
            folders[str(current)]["files"].append(str(path))

            # Build folder hierarchy
            parts = list(current.parts) if current != Path('.') else []
            for i in range(len(parts)):
                parent_path = Path(*parts[:i]) if i > 0 else Path('.')
                child_path = Path(*parts[:i+1])
                folders[str(parent_path)]["subdirs"].add(str(child_path))

        return folders

    def create_folder_index(self, folder_path, folder_info):
        """Create index.md for a folder"""
        out_dir = self.output_dir / folder_path
        out_dir.mkdir(parents=True, exist_ok=True)

        index_file = out_dir / "index.md"

        folder_name = Path(folder_path).name if folder_path != "." else "Root"

        content = f"""# Folder Index: {folder_name}

## Location
`{folder_path}`

---

## Contents

"""

        # Add subdirectories
        if folder_info["subdirs"]:
            content += "### Subdirectories\n\n"
            for subdir in sorted(folder_info["subdirs"]):
                subdir_name = Path(subdir).name
                rel_link = Path(subdir).relative_to(Path(folder_path)) if folder_path != "." else subdir
                content += f"- [{subdir_name}]({rel_link}/index.md)\n"
            content += "\n"

        # Add files
        if folder_info["files"]:
            content += "### Files\n\n"
            for file_path in sorted(folder_info["files"]):
                file_name = Path(file_path).name
                file_stem = Path(file_path).stem if Path(file_path).stem else file_name

                # Link to documentation
                if folder_path == ".":
                    doc_link = f"{file_stem}_docs.md"
                else:
                    doc_link = f"{file_stem}_docs.md"

                file_info = self.file_tree.get(file_path, {})
                size = file_info.get('size', 0)
                classification = file_info.get('classification', 'unknown')

                content += f"- **{file_name}** ({size:,} bytes, {classification})\n"
                content += f"  - [Documentation]({doc_link})\n"
                content += f"  - [Keywords]({file_stem}_kw.md)\n"

            content += "\n"

        content += "---\n\n"
        content += f"*Index for `{folder_path}`*\n"

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return 1

    def create_folder_doc(self, folder_path, folder_info):
        """Create doc.md with narrative context for a folder"""
        out_dir = self.output_dir / folder_path
        doc_file = out_dir / "doc.md"

        folder_name = Path(folder_path).name if folder_path != "." else "Root"

        content = f"""# Folder Documentation: {folder_name}

## Overview

**Location**: `{folder_path}`

"""

        # Analyze folder contents
        num_files = len(folder_info["files"])
        num_subdirs = len(folder_info["subdirs"])

        content += f"This folder contains {num_files} file(s) and {num_subdirs} subdirectory(ies).\n\n"

        # Categorize files by type
        file_types = defaultdict(list)
        for file_path in folder_info["files"]:
            ext = Path(file_path).suffix or "no extension"
            file_types[ext].append(Path(file_path).name)

        content += "## File Types\n\n"
        for ext, files in sorted(file_types.items()):
            content += f"### {ext}\n"
            content += f"- {len(files)} file(s)\n"
            for f in sorted(files)[:10]:  # Show first 10
                content += f"  - `{f}`\n"
            if len(files) > 10:
                content += f"  - ... and {len(files) - 10} more\n"
            content += "\n"

        # Add context based on folder name/path
        content += "## Purpose & Context\n\n"

        if 'test' in folder_path.lower():
            content += "This appears to be a test directory containing test files and test utilities.\n\n"
        elif 'doc' in folder_path.lower() or 'documentation' in folder_path.lower():
            content += "This appears to be a documentation directory.\n\n"
        elif 'example' in folder_path.lower():
            content += "This appears to be an examples directory containing sample code and demonstrations.\n\n"
        elif 'src' in folder_path.lower() or 'source' in folder_path.lower():
            content += "This appears to be a source code directory.\n\n"
        elif 'lib' in folder_path.lower():
            content += "This appears to be a library directory containing reusable code modules.\n\n"
        elif 'util' in folder_path.lower():
            content += "This appears to be a utilities directory containing helper functions and tools.\n\n"
        else:
            content += f"This folder is part of the project structure.\n\n"

        content += "## Related Folders\n\n"
        if folder_path != ".":
            parent = str(Path(folder_path).parent) if Path(folder_path).parent != Path('.') else "."
            content += f"- Parent: [{parent}](../{'' if parent == '.' else parent + '/'}index.md)\n"

        for subdir in sorted(folder_info["subdirs"]):
            subdir_name = Path(subdir).name
            rel_path = Path(subdir).relative_to(Path(folder_path)) if folder_path != "." else subdir
            content += f"- Subdirectory: [{subdir_name}]({rel_path}/index.md)\n"

        content += "\n---\n\n"
        content += f"*Documentation for folder `{folder_path}`*\n"

        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return 1

    def create_folder_sub(self, folder_path, folder_info):
        """Create sub.md merging keywords from descendant files"""
        out_dir = self.output_dir / folder_path
        sub_file = out_dir / "sub.md"

        folder_name = Path(folder_path).name if folder_path != "." else "Root"

        content = f"""# Aggregated Keywords: {folder_name}

## Location
`{folder_path}`

This file aggregates keywords from all files in this folder and its subdirectories.

---

## Keywords by File

"""

        # Collect keywords from all _kw.md files in this folder
        keywords_global = defaultdict(set)

        for file_path in sorted(folder_info["files"]):
            file_name = Path(file_path).name
            file_stem = Path(file_path).stem if Path(file_path).stem else file_name

            kw_file = out_dir / f"{file_stem}_kw.md"

            if kw_file.exists():
                content += f"### {file_name}\n\n"
                content += f"See [{file_stem}_kw.md]({file_stem}_kw.md) for detailed keywords.\n\n"

                # Try to extract some keywords
                try:
                    with open(kw_file, 'r', encoding='utf-8') as f:
                        kw_content = f.read()
                        # Simple extraction of bold keywords
                        import re
                        keywords = re.findall(r'\*\*([a-zA-Z_][a-zA-Z0-9_]*)\*\*', kw_content)
                        for kw in keywords[:20]:  # First 20 keywords
                            first_letter = kw[0].upper()
                            keywords_global[first_letter].add(kw)
                except:
                    pass

        content += "\n---\n\n## Alphabetical Index\n\n"

        for letter in sorted(keywords_global.keys()):
            content += f"### {letter}\n\n"
            for kw in sorted(keywords_global[letter]):
                content += f"- {kw}\n"
            content += "\n"

        content += "---\n\n"
        content += f"*Aggregated keywords for folder `{folder_path}`*\n"

        with open(sub_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return 1

    def process_all_folders(self):
        """Process all folders and create documentation"""
        folder_structure = self.get_folder_structure()

        total = len(folder_structure)
        print(f"Processing {total} folders...")

        for i, (folder_path, folder_info) in enumerate(sorted(folder_structure.items()), 1):
            if i % 20 == 0:
                print(f"Progress: {i}/{total} folders processed")

            try:
                # Create index.md
                self.docs_created += self.create_folder_index(folder_path, folder_info)

                # Create doc.md
                self.docs_created += self.create_folder_doc(folder_path, folder_info)

                # Create sub.md
                self.docs_created += self.create_folder_sub(folder_path, folder_info)

                self.folders_processed += 1

            except Exception as e:
                print(f"Error processing folder {folder_path}: {e}")

        print(f"\nCompleted! Processed {self.folders_processed} folders, created {self.docs_created} documentation files")
        return self.folders_processed, self.docs_created

def main():
    generator = FolderDocGenerator()
    processed, created = generator.process_all_folders()

    print(f"\nSummary:")
    print(f"  Folders processed: {processed}")
    print(f"  Docs created: {created}")

    return processed, created

if __name__ == "__main__":
    main()
