#!/usr/bin/env python3
"""
Code Line Counter - Benchmark Edition
Single-threaded baseline version for performance comparison

Usage:
    python code_counter_benchmark.py [path]
    
Arguments:
    path    Optional path to analyze (default: current directory)
"""

import os
import sys
import time
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
    """Count non-empty lines in a file efficiently"""
    try:
        line_count = 0
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            # Read file line by line instead of loading all lines into memory
            for line in f:
                if line.strip():  # Count non-empty lines
                    line_count += 1
        return line_count
    except (IOError, OSError, UnicodeDecodeError):
        # Skip files that can't be read
        return 0


def get_file_extension(file_path):
    """Get lowercase file extension"""
    return file_path.suffix.lower()


def count_lines_in_directory(directory_path):
    """Count lines of code in the specified directory (single-threaded)"""
    start_time = time.time()
    
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
        return None, None, None, None, None
    
    if not root_path.is_dir():
        print(f"Error: Path '{directory_path}' is not a directory.")
        return None, None, None, None, None
    
    print(f"📊 Benchmark counting lines of code in: {root_path}")
    print()
    
    # Walk through all files recursively (single-threaded)
    processed_files = 0
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
                processed_files += 1
                
                # Progress indicator for large projects
                if processed_files % 1000 == 0:
                    print(f"Processed {processed_files:,} files...")
    
    end_time = time.time()
    analysis_time = end_time - start_time
    
    return total_lines, extension_counts, file_counts, root_path, analysis_time


def display_results(total_lines, extension_counts, file_counts, root_path, analysis_time):
    """Display the counting results"""
    print()
    print("=" * 70)
    print("📊 BENCHMARK CODE ANALYSIS RESULTS")
    print("=" * 70)
    print(f"📁 Directory: {root_path}")
    print()
    print(f"📊 Total Lines: {total_lines:,}")
    print(f"📁 Total Files: {sum(file_counts.values()):,}")
    print(f"⏱️  Analysis Time: {analysis_time:.3f} seconds")
    
    # Calculate performance metrics
    total_files = sum(file_counts.values())
    if analysis_time > 0:
        files_per_sec = total_files / analysis_time
        lines_per_sec = total_lines / analysis_time
        print(f"📈 Performance: {files_per_sec:,.0f} files/sec, {lines_per_sec:,.0f} lines/sec")
    
    print()
    
    # Sort by line count (descending)
    sorted_extensions = sorted(extension_counts.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_extensions:
        print("📋 Breakdown by File Type:")
        print("-" * 50)
        for ext, lines in sorted_extensions:
            files = file_counts[ext]
            percentage = (lines / total_lines * 100) if total_lines > 0 else 0
            avg_lines = lines / files if files > 0 else 0
            print(f"{ext:>8}: {lines:>8,} lines ({files:>4} files) [{percentage:>5.1f}%] avg: {avg_lines:>6.1f}")
    else:
        print("No supported code files found.")
    
    print()
    print("=" * 70)
    print("💡 For high-performance analysis of large repositories, try: python code_counter_turbo.py")


def show_usage_examples():
    """Show usage examples"""
    print("📊 Benchmark Usage Examples:")
    print("  python code_counter_benchmark.py                    # Count lines in current directory")
    print("  python code_counter_benchmark.py /path/to/project   # Count lines in specified directory")
    print("  python code_counter_benchmark.py ../other-project   # Count lines in relative path")
    print("  python code_counter_benchmark.py --help             # Show detailed help")
    print("  💡 For high-performance analysis, use code_counter_turbo.py")
    print()


def main():
    """Main function to count lines of code"""
    parser = argparse.ArgumentParser(
        description='📊 Code Line Counter - Benchmark Edition (single-threaded baseline for comparison)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📊 Benchmark Examples:
    python code_counter_benchmark.py              # Count lines in current directory
    python code_counter_benchmark.py /path/to/project    # Count lines in specified directory
    python code_counter_benchmark.py ../other-project   # Count lines in relative path
    
🚀 For high-performance analysis:
    python code_counter_turbo.py /path/to/large-repo     # Use turbo edition for large repositories
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
    result = count_lines_in_directory(args.path)
    
    # Display results if successful
    if result[0] is not None:
        display_results(*result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n📊 Benchmark analysis cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)