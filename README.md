# Cross-Platform Code Line Counter (Python)

[中文版本 | Chinese Version](README_CN.md)

This is a cross-platform Python script that counts lines of code in various programming language files.

## Usage

Works on Windows, macOS, and Linux with Python 3+:

```bash
# Count lines in current directory (shows usage examples)
python count_lines.py

# Count lines in a specific directory
python count_lines.py /path/to/project

# Count lines in a relative path
python count_lines.py ../other-project

# Show detailed help
python count_lines.py --help
```

Or on Unix-like systems:
```bash
python3 count_lines.py [path]
```

## Features

- **Recursive scanning**: Analyzes all files in the current directory and subdirectories
- **Language support**: Supports 25+ programming languages and file types
- **Smart filtering**: Automatically excludes common directories like:
  - `.git`, `.vscode`, `node_modules`
  - `__pycache__`, `.pytest_cache`, `venv`, `env`
  - `bin`, `obj`, `target`, `build`, `dist`
  - `logs`, `.idea`, `.vs`, `coverage`
- **Non-empty line counting**: Only counts lines with actual content (ignores empty lines)
- **Detailed statistics**: Shows total lines, file counts, and breakdown by file type
- **Flexible path support**: Can analyze any directory via command-line argument
- **User-friendly**: Shows usage examples when run without arguments

## Supported File Extensions

- **Python**: `.py`
- **C/C++**: `.c`, `.cpp`, `.h`
- **C#**: `.cs`
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
- **Web**: `.html`, `.css`, `.scss`, `.sass`, `.less`, `.vue`
- **Java**: `.java`
- **Database**: `.sql`
- **Configuration**: `.json`, `.yaml`, `.yml`, `.xml`
- **Shell**: `.sh`, `.ps1`
- **Other**: `.php`, `.rb`, `.go`, `.rs`, `.swift`, `.kt`, `.scala`, `.m`, `.mm`, `.r`, `.pl`, `.lua`

## Example Output

When running without specifying a path, usage examples are shown:

```
Usage Examples:
  python count_lines.py                    # Count lines in current directory
  python count_lines.py /path/to/project   # Count lines in specified directory
  python count_lines.py ../other-project   # Count lines in relative path
  python count_lines.py --help             # Show detailed help

Counting lines of code in: /path/to/project

============================================================
Code Lines Statistics
============================================================
Directory: /path/to/project

Total Lines: 5,875
Total Files: 35

By File Type:
------------------------------
     .py:    3,908 lines (  31 files)
   .html:    1,839 lines (   2 files)
   .json:       96 lines (   1 files)
    .yml:       32 lines (   1 files)

============================================================
```

When specifying a custom path, only the results are shown:

```
Counting lines of code in: /path/to/project/src

============================================================
Code Lines Statistics
============================================================
Directory: /path/to/project/src

Total Lines: 954
Total Files: 7

By File Type:
------------------------------
     .py:      954 lines (   7 files)

============================================================
```

## Advantages

- **Cross-platform**: Works on Windows, macOS, and Linux
- **Flexible path support**: Can analyze any directory via command-line argument
- **Better error handling**: Gracefully handles encoding issues and unreadable files
- **User-friendly**: Shows usage examples when run without arguments
- **More accurate**: Uses Python's robust file handling
- **Maintainable**: Easy to extend and modify
- **No dependencies**: Uses only Python standard library

## Requirements

- Python 3 or higher
- No additional dependencies required

## Installation

Simply copy the `count_lines.py` script to your project directory and run it. No additional installation required.