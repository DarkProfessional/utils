# **Utils**
Non-specific useful scripts or modules

# **Scripts Documentation**

---

## *print_contents_with_patterns.py*

## Overview

This script traverses a specified directory and its subdirectories, printing the relative file paths and contents of all files found. It includes options to ignore specific subdirectories or file patterns and to require files to match specified patterns. These options provide flexibility in focusing on relevant files and excluding irrelevant ones.

## Prerequisites

- Python 3.x installed on your system.
- Basic familiarity with running Python scripts from the command line.

## Usage

\```bash
python print_contents_with_patterns.py <directory> [options]
\```

### Positional Arguments

- `directory`: The root directory to start processing. The script will print paths and contents of files within this directory and its subdirectories.

### Optional Arguments

- `--ignore <subdirectory>`: A list of subdirectories to ignore. Paths should be relative to the `directory`.
- `--ignore-patterns <patterns>`: A list of glob patterns for file paths to ignore. Patterns should match the relative file path from the `directory`.
- `--require-patterns <patterns>`: A list of glob patterns that file paths must match to be included. This is strictly enforced, and only files matching at least one of these patterns will be processed.

### Flags

- `--help`: Show the help message and exit.

## Examples

**Ignore Specific Subdirectories:**
\```sh
python print_contents_with_patterns.py /path/to/directory --ignore dir1 dir2
\```

**Ignore Files Matching Specific Patterns:**
\```sh
python print_contents_with_patterns.py /path/to/directory --ignore-patterns "*.log" "*.tmp"
\```

**Require Files to Match Specific Patterns:**
\```sh
python print_contents_with_patterns.py /path/to/directory --require-patterns "*.py" "*.md"
\```

## Features

- **Directory Traversal**: Recursively processes files in the specified directory and its subdirectories.
- **Ignore Subdirectories**: Skips specified subdirectories to focus on relevant areas.
- **Pattern Filtering**: Supports glob pattern matching to ignore files or require files to match certain patterns.
- **Mutual Exclusivity**: `--ignore-patterns` and `--require-patterns` cannot be used together, ensuring clear and predictable script behavior.

## Notes

- The script assumes files are text-readable and uses UTF-8 encoding for reading file contents. Adjust the encoding in the script if necessary.
- Pattern matching uses glob syntax, allowing for flexible and powerful file selection criteria.

## Conclusion

This script offers a versatile tool for exploring file systems, tailoring file and directory processing according to specific needs, whether it be excluding logs and temporary files, focusing on specific file types, or ignoring irrelevant subdirectories.

---
