#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


CLASS_PATTERNS = {
    ".py": [re.compile(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".js": [re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".jsx": [re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".ts": [re.compile(r"^\s*(?:export\s+)?(?:abstract\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".tsx": [re.compile(r"^\s*(?:export\s+)?(?:abstract\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".java": [re.compile(r"^\s*(?:public\s+)?(?:abstract\s+|final\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".kt": [re.compile(r"^\s*(?:public\s+)?(?:data\s+|sealed\s+|open\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".cs": [re.compile(r"^\s*(?:public|internal|private|protected)?\s*(?:abstract\s+|sealed\s+|partial\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".php": [re.compile(r"^\s*(?:abstract\s+|final\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\b")],
    ".rb": [re.compile(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_:]*)\b")],
}

HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"command failed: {' '.join(cmd)}")
    return result.stdout


def inside_git_repo():
    try:
        run(["git", "rev-parse", "--show-toplevel"])
    except RuntimeError:
        return False
    return True


def build_diff_args(base_ref, cached):
    diff_args = ["git", "diff"]
    if cached:
        diff_args.append("--cached")
    if base_ref:
        diff_args.append(base_ref)
    return diff_args


def parse_numstat(output):
    files = []
    total_added = 0
    total_deleted = 0

    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added_text, deleted_text, path = parts[0], parts[1], parts[2]
        added = 0 if added_text == "-" else int(added_text)
        deleted = 0 if deleted_text == "-" else int(deleted_text)
        files.append({"path": path, "added": added, "deleted": deleted})
        total_added += added
        total_deleted += deleted

    return files, total_added, total_deleted


def changed_line_ranges(diff_text):
    ranges = []
    for line in diff_text.splitlines():
        match = HUNK_RE.match(line)
        if not match:
            continue
        start = int(match.group(1))
        count = int(match.group(2) or "1")
        if count == 0:
            continue
        ranges.append((start, start + count - 1))
    return ranges


def extract_class_lines(file_path):
    suffix = file_path.suffix.lower()
    patterns = CLASS_PATTERNS.get(suffix)
    if not patterns or not file_path.exists():
        return []

    class_lines = []
    try:
        for lineno, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern in patterns:
                match = pattern.match(line)
                if match:
                    class_lines.append((lineno, match.group(1)))
                    break
    except UnicodeDecodeError:
        return []

    return class_lines


def classes_for_changed_ranges(file_path, ranges):
    class_lines = extract_class_lines(file_path)
    if not class_lines or not ranges:
        return []

    classes = set()
    for start, end in ranges:
        for line_no in range(start, end + 1):
            nearest = None
            for class_lineno, class_name in class_lines:
                if class_lineno <= line_no:
                    nearest = class_name
                else:
                    break
            if nearest:
                classes.add(nearest)
    return sorted(classes)


def main():
    parser = argparse.ArgumentParser(description="Collect task change statistics from git diff.")
    parser.add_argument("--base", help="Optional base ref for git diff, such as HEAD~1 or origin/main.")
    parser.add_argument("--cached", action="store_true", help="Use staged changes instead of working tree changes.")
    args = parser.parse_args()

    if not inside_git_repo():
        print("error: current directory is not a git repository", file=sys.stderr)
        return 2

    diff_args = build_diff_args(args.base, args.cached)
    numstat_output = run(diff_args + ["--numstat"])
    files, total_added, total_deleted = parse_numstat(numstat_output)

    print(f"files_changed: {len(files)}")
    print(f"lines_added: {total_added}")
    print(f"lines_deleted: {total_deleted}")
    print(f"lines_changed: {total_added + total_deleted}")
    print("changed_files:")

    for item in files:
        path = item["path"]
        file_path = Path(path)
        diff_text = run(diff_args + ["-U0", "--", path])
        ranges = changed_line_ranges(diff_text)
        classes = classes_for_changed_ranges(file_path, ranges)
        class_text = ", ".join(classes) if classes else "-"
        print(
            f"- {path} | +{item['added']} -{item['deleted']} | classes: {class_text}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
