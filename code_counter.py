#!/usr/bin/env python3
"""
Cross-platform code line counter
Counts non-empty lines in various programming language files

Usage:
    python count_lines.py [path]
    
Arguments:
    path    Optional path to analyze (default: current directory)
"""

import os
import sys
import argparse
from pathlib import Path
from collections import defaultdict


def should_skip_directory(dir_path):
    """Check if directory should be skipped"""
    skip_dirs = {
        '.git', '.vscode', 'node_modules', '__pycache__', '.pytest_cache',
        'venv', 'env', 'bin', 'obj', 'target', 'build', 'dist', '.idea',
        '.vs', 'coverage', '.nyc_output', 'logs'
    }
    return dir_path.name in skip_dirs


def count_lines_in_file(file_path):
    """Count non-empty lines in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            # Count non-empty lines (after stripping whitespace)
            non_empty_lines = [line for line in lines if line.strip()]
            return len(non_empty_lines)
    except (IOError, OSError, UnicodeDecodeError):
        # Skip files that can't be read
        return 0


def get_file_extension(file_path):
    """Get lowercase file extension"""
    return file_path.suffix.lower()


def count_lines_in_directory(directory_path):
    """Count lines of code in the specified directory"""
    # Supported file extensions
    extensions = {
        '.py', '.cs', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c',
        '.h', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.scala', '.sh',
        '.ps1', '.sql', '.xml', '.json', '.yaml', '.yml', '.jsx', '.tsx',
        '.vue', '.scss', '.sass', '.less', '.m', '.mm', '.r', '.pl', '.lua'
    }
    
    total_lines = 0
    extension_counts = defaultdict(int)
    file_counts = defaultdict(int)
    
    # Convert to Path object and resolve
    root_path = Path(directory_path).resolve()
    
    if not root_path.exists():
        print(f"Error: Path '{directory_path}' does not exist.")
        return None, None, None, None
    
    if not root_path.is_dir():
        print(f"Error: Path '{directory_path}' is not a directory.")
        return None, None, None, None
    
    print(f"Counting lines of code in: {root_path}")
    print()
    
    # Walk through all files recursively
    for file_path in root_path.rglob('*'):
        # Skip if it's not a file
        if not file_path.is_file():
            continue
            
        # Skip if any parent directory should be skipped
        if any(should_skip_directory(parent) for parent in file_path.parents):
            continue
            
        # Skip if current directory should be skipped
        if should_skip_directory(file_path.parent):
            continue
            
        # Get file extension
        extension = get_file_extension(file_path)
        
        # Only process supported extensions
        if extension in extensions:
            line_count = count_lines_in_file(file_path)
            if line_count > 0:
                total_lines += line_count
                extension_counts[extension] += line_count
                file_counts[extension] += 1
    
    return total_lines, extension_counts, file_counts, root_path


def display_results(total_lines, extension_counts, file_counts, root_path):
    """Display the counting results"""
    print("=" * 60)
    print("Code Lines Statistics")
    print("=" * 60)
    print(f"Directory: {root_path}")
    print()
    print(f"Total Lines: {total_lines:,}")
    print(f"Total Files: {sum(file_counts.values()):,}")
    print()
    
    # Sort by line count (descending)
    sorted_extensions = sorted(extension_counts.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_extensions:
        print("By File Type:")
        print("-" * 30)
        for ext, lines in sorted_extensions:
            files = file_counts[ext]
            print(f"{ext:>8}: {lines:>8,} lines ({files:>4} files)")
    else:
        print("No supported code files found.")
    
    print()
    print("=" * 60)


def show_usage_examples():
    """Show usage examples"""
    print("Usage Examples:")
    print("  python count_lines.py                    # Count lines in current directory")
    print("  python count_lines.py /path/to/project   # Count lines in specified directory")
    print("  python count_lines.py ../other-project   # Count lines in relative path")
    print("  python count_lines.py --help             # Show detailed help")
    print()


def main():
    """Main function to count lines of code"""
    parser = argparse.ArgumentParser(
        description='Count lines of code in various programming language files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python count_lines.py              # Count lines in current directory
    python count_lines.py /path/to/project    # Count lines in specified directory
    python count_lines.py ../other-project   # Count lines in relative path
        """
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to analyze (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Show usage examples when using default path (current directory)
    if args.path == '.':
        show_usage_examples()
    
    # Count lines in the specified directory
    total_lines, extension_counts, file_counts, root_path = count_lines_in_directory(args.path)
    
    # Display results if successful
    if total_lines is not None:
        display_results(total_lines, extension_counts, file_counts, root_path)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)