#!/usr/bin/env python3
"""
Global documentation generator
Creates keywords.md, index.md, and comprehensive_book.md
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import re

class GlobalDocGenerator:
    def __init__(self, repo_path=".", output_dir="./docs"):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()

        # Load file tree
        with open(self.output_dir / "file_tree.json", 'r') as f:
            self.file_tree = json.load(f)

        self.docs_created = 0

    def get_all_folders(self):
        """Get list of all folders"""
        folders = set()
        folders.add(".")

        for file_path in self.file_tree.keys():
            path = Path(file_path)
            current = path.parent

            if current != Path('.'):
                # Add all parent folders
                parts = list(current.parts)
                for i in range(len(parts)):
                    folder = str(Path(*parts[:i+1]))
                    folders.add(folder)

        return sorted(folders)

    def create_global_keywords(self):
        """Create global keywords.md merging all keywords"""
        print("Creating global keywords index...")

        keywords_file = self.output_dir / "keywords.md"

        content = """# Global Keywords Index

This file aggregates all keywords from across the entire repository, organized alphabetically.

---

## Navigation

"""

        # Add alphabet navigation
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            content += f"[{letter}](#{letter.lower()}) "
        content += "\n\n---\n\n"

        # Collect all keywords from all _kw.md files
        all_keywords = defaultdict(list)

        for file_path in self.file_tree.keys():
            path = Path(file_path)
            file_stem = path.stem if path.stem else path.name

            # Find corresponding _kw.md file
            kw_file = self.output_dir / path.parent / f"{file_stem}_kw.md"

            if kw_file.exists():
                try:
                    with open(kw_file, 'r', encoding='utf-8') as f:
                        kw_content = f.read()

                    # Extract keywords (looking for bold keywords)
                    keywords = re.findall(r'\*\*([a-zA-Z_][a-zA-Z0-9_]*)\*\*', kw_content)

                    for kw in keywords:
                        first_letter = kw[0].upper()
                        # Create relative link to the keyword file
                        rel_kw_path = kw_file.relative_to(self.output_dir)
                        all_keywords[first_letter].append((kw, str(rel_kw_path)))

                except Exception as e:
                    pass

        # Write keywords by letter
        for letter in sorted(all_keywords.keys()):
            content += f"## {letter}\n\n"

            # Get unique keywords
            keywords_set = {}
            for kw, kw_file in all_keywords[letter]:
                if kw not in keywords_set:
                    keywords_set[kw] = []
                keywords_set[kw].append(kw_file)

            for kw in sorted(keywords_set.keys())[:200]:  # Limit to 200 per letter
                files = keywords_set[kw]
                if len(files) == 1:
                    content += f"- **{kw}** - [{files[0]}]({files[0]})\n"
                else:
                    content += f"- **{kw}** - Found in {len(files)} file(s)\n"
                    for f in files[:5]:  # Show first 5 files
                        content += f"  - [{f}]({f})\n"
                    if len(files) > 5:
                        content += f"  - ... and {len(files) - 5} more\n"

            content += "\n"

        content += "---\n\n*Global keywords index for the entire repository*\n"

        with open(keywords_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created global keywords index: {keywords_file}")
        return 1

    def create_global_index(self):
        """Create root index.md linking to all folders"""
        print("Creating root index...")

        index_file = self.output_dir / "index.md"

        content = """# Repository Documentation Index

Welcome to the comprehensive documentation for this repository.

---

## Quick Links

- [Global Keywords Index](keywords.md) - Alphabetical index of all keywords
- [Comprehensive Book](comprehensive_book.md) - Complete documentation book
- [Verification Report](verification_report.md) - Validation and verification results
- [Manifest](manifest.json) - Documentation generation metadata

---

## Folder Structure

"""

        folders = self.get_all_folders()

        # Create hierarchical folder listing
        content += "### Root\n\n"
        content += "- [Root Documentation](doc.md)\n"
        content += "- [Root Index](index.md)\n\n"

        # Group folders by depth
        folder_tree = defaultdict(list)
        for folder in folders:
            if folder == ".":
                continue
            depth = len(Path(folder).parts)
            folder_tree[depth].append(folder)

        for depth in sorted(folder_tree.keys()):
            for folder in sorted(folder_tree[depth]):
                indent = "  " * (depth - 1)
                folder_name = Path(folder).name
                content += f"{indent}- [{folder}]({folder}/index.md)\n"

        content += "\n---\n\n## Statistics\n\n"

        # Add statistics
        num_files = len(self.file_tree)
        num_folders = len(folders)

        content += f"- **Total Files**: {num_files:,}\n"
        content += f"- **Total Folders**: {num_folders:,}\n"

        # Count by file type
        file_types = defaultdict(int)
        for file_path in self.file_tree.keys():
            ext = Path(file_path).suffix or "no extension"
            file_types[ext] += 1

        content += f"\n### Files by Type\n\n"
        for ext, count in sorted(file_types.items(), key=lambda x: -x[1])[:20]:
            content += f"- `{ext}`: {count:,} file(s)\n"

        content += "\n---\n\n"
        content += "*Repository documentation generated automatically*\n"

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created root index: {index_file}")
        return 1

    def create_comprehensive_book(self):
        """Create comprehensive_book.md stitching all documentation"""
        print("Creating comprehensive book...")

        book_file = self.output_dir / "comprehensive_book.md"

        content = """# Comprehensive Repository Documentation Book

This book contains comprehensive documentation for the entire repository, organized by folders and files.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Overview](#repository-overview)
3. [Folder Documentation](#folder-documentation)
4. [Appendices](#appendices)

---

## Introduction

This comprehensive book aggregates all documentation generated for this repository. Each section corresponds to a folder in the repository, with summaries of all files contained within.

---

## Repository Overview

"""

        # Add repository statistics
        num_files = len(self.file_tree)
        folders = self.get_all_folders()
        num_folders = len(folders)

        content += f"- **Total Files**: {num_files:,}\n"
        content += f"- **Total Folders**: {num_folders:,}\n\n"

        # Count file types
        file_types = defaultdict(int)
        total_size = 0
        for file_info in self.file_tree.values():
            ext = Path(file_info['path']).suffix or "no extension"
            file_types[ext] += 1
            total_size += file_info.get('size', 0)

        content += f"- **Total Size**: {total_size:,} bytes ({total_size / (1024*1024):.2f} MB)\n\n"

        content += "### File Types Distribution\n\n"
        for ext, count in sorted(file_types.items(), key=lambda x: -x[1])[:30]:
            percentage = (count / num_files) * 100
            content += f"- `{ext}`: {count:,} files ({percentage:.1f}%)\n"

        content += "\n---\n\n## Folder Documentation\n\n"

        # Add each folder's doc.md content
        for i, folder in enumerate(sorted(folders), 1):
            folder_name = Path(folder).name if folder != "." else "Root"
            content += f"### Chapter {i}: {folder_name}\n\n"
            content += f"**Path**: `{folder}`\n\n"

            # Read folder's doc.md if it exists
            doc_file = self.output_dir / folder / "doc.md"
            if doc_file.exists():
                try:
                    with open(doc_file, 'r', encoding='utf-8') as f:
                        doc_content = f.read()

                    # Extract the overview section (skip the title)
                    lines = doc_content.split('\n')
                    # Skip title and add the rest (limit to avoid huge book)
                    overview = '\n'.join(lines[3:50])  # First ~50 lines
                    content += overview + "\n\n"

                except Exception as e:
                    content += f"*Error reading folder documentation: {e}*\n\n"

            content += f"[See full folder documentation]({folder}/doc.md)\n\n"
            content += "---\n\n"

            # Every 50 chapters, add a mini TOC for navigation
            if i % 50 == 0:
                content += "**Progress**: " + f"{i}/{num_folders} folders documented\n\n"

        content += "## Appendices\n\n"
        content += "### A. Global Keywords\n\n"
        content += "See [keywords.md](keywords.md) for the complete alphabetical keyword index.\n\n"

        content += "### B. Verification Report\n\n"
        content += "See [verification_report.md](verification_report.md) for validation results.\n\n"

        content += "### C. Manifest\n\n"
        content += "See [manifest.json](manifest.json) for generation metadata.\n\n"

        content += "---\n\n"
        content += "*End of Comprehensive Documentation Book*\n"

        with open(book_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created comprehensive book: {book_file}")
        return 1

    def process_all(self):
        """Create all global documentation"""
        self.docs_created += self.create_global_keywords()
        self.docs_created += self.create_global_index()
        self.docs_created += self.create_comprehensive_book()

        print(f"\nCompleted! Created {self.docs_created} global documentation files")
        return self.docs_created

def main():
    generator = GlobalDocGenerator()
    created = generator.process_all()

    print(f"\nSummary:")
    print(f"  Global docs created: {created}")

    return created

if __name__ == "__main__":
    main()
