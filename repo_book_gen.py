#!/usr/bin/env python3
"""
World's Best Repo Book Generator and Index Builder
Generates comprehensive documentation for an entire repository
"""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

class RepoBookGenerator:
    def __init__(self, repo_path=".", output_dir="./docs"):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.progress_log = self.output_dir / ".progress.log"
        self.checkpoint_file = self.output_dir / ".checkpoint.json"

        self.manifest = {
            "generator_version": "1.0.0",
            "repo_source": str(self.repo_path),
            "repo_fingerprint": "",
            "commit_sha": "",
            "file_count": 0,
            "docs_count": 0,
            "bytes_written": 0,
            "timestamp_start": datetime.utcnow().isoformat(),
            "timestamp_end": "",
            "files": {},
            "checksums": {}
        }

        self.stats = {
            "files_scanned": 0,
            "docs_created": 0,
            "words_estimated": 0,
            "bytes_written": 0,
            "errors": []
        }

        self.file_tree = {}
        self.all_keywords = defaultdict(list)

    def compute_repo_fingerprint(self):
        """Compute a fingerprint of the repository"""
        # Try to get git commit SHA
        try:
            import subprocess
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass

        # Fallback: hash of all file paths and sizes
        hasher = hashlib.sha256()
        files = sorted(self.repo_path.rglob("*"))
        for f in files:
            if f.is_file() and not any(p in f.parts for p in ['.git', 'docs']):
                rel = f.relative_to(self.repo_path)
                hasher.update(str(rel).encode())
                hasher.update(str(f.stat().st_size).encode())
        return hasher.hexdigest()

    def classify_file(self, file_path):
        """Classify a file as text, binary, or large"""
        try:
            size = file_path.stat().st_size

            # Very large files
            if size > 100 * 1024 * 1024:  # >100MB
                return "large_blob"

            # Binary detection
            mime_type, _ = mimetypes.guess_type(str(file_path))
            binary_extensions = {
                '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
                '.pdf', '.zip', '.tar', '.gz', '.bz2', '.xz',
                '.exe', '.dll', '.so', '.dylib',
                '.pyc', '.pyo', '.pyd',
                '.whl', '.egg',
                '.pkl', '.pickle',
                '.db', '.sqlite', '.sqlite3'
            }

            if file_path.suffix.lower() in binary_extensions:
                return "binary"

            # Try to read as text
            try:
                with open(file_path, 'r', encoding='utf-8', errors='strict') as f:
                    f.read(1024)  # Try reading first 1KB
                return "text"
            except (UnicodeDecodeError, UnicodeError):
                return "binary"

        except Exception as e:
            return "error"

    def scan_repository(self):
        """Scan and classify all files in the repository"""
        print("Scanning repository...")

        for item in self.repo_path.rglob("*"):
            # Skip .git and docs directories
            if any(p in item.parts for p in ['.git', 'docs']):
                continue

            if item.is_file():
                rel_path = item.relative_to(self.repo_path)
                classification = self.classify_file(item)

                self.file_tree[str(rel_path)] = {
                    "path": str(rel_path),
                    "size": item.stat().st_size,
                    "classification": classification,
                    "docs_created": False
                }
                self.stats["files_scanned"] += 1

        self.manifest["file_count"] = self.stats["files_scanned"]
        self.manifest["files"] = self.file_tree
        print(f"Scanned {self.stats['files_scanned']} files")

    def save_manifest(self):
        """Save the manifest to disk"""
        manifest_path = self.output_dir / "manifest.json"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2)
        print(f"Manifest saved to {manifest_path}")

    def get_file_list(self):
        """Get list of files grouped by directory"""
        files_by_dir = defaultdict(list)
        for file_info in self.file_tree.values():
            file_path = Path(file_info["path"])
            dir_path = str(file_path.parent) if file_path.parent != Path('.') else "."
            files_by_dir[dir_path].append(file_info)
        return files_by_dir

    def get_directory_tree(self):
        """Get all directories in the repository"""
        dirs = set()
        for file_path in self.file_tree.keys():
            path = Path(file_path)
            while path.parent != Path('.'):
                dirs.add(str(path.parent))
                path = path.parent
        return sorted(dirs)

def main():
    generator = RepoBookGenerator()

    # Step 1: Bootstrap
    print("Step 1: Bootstrap")
    generator.manifest["repo_fingerprint"] = generator.compute_repo_fingerprint()
    generator.manifest["commit_sha"] = generator.manifest["repo_fingerprint"]

    # Step 2: Scan
    print("\nStep 2: Scan repository")
    generator.output_dir.mkdir(exist_ok=True)
    generator.scan_repository()
    generator.save_manifest()

    # Export file tree for processing
    file_tree_path = generator.output_dir / "file_tree.json"
    with open(file_tree_path, 'w', encoding='utf-8') as f:
        json.dump(generator.file_tree, f, indent=2)

    print(f"\nBootstrap complete!")
    print(f"Files to process: {generator.stats['files_scanned']}")
    print(f"File tree saved to: {file_tree_path}")

    return generator

if __name__ == "__main__":
    main()
