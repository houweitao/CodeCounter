#!/usr/bin/env python3
"""
Cross-platform code line counter
Counts non-empty lines in various programming language files

Usage:
    python code_counter.py [path]
    
Arguments:
    path    Optional path to analyze (default: current directory)
"""

import os
import sys
import time
import argparse
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading


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

def should_skip_path(file_path, skip_dirs):
    """Optimized function to check if a path should be skipped"""
    # Check if any part of the path contains skip directories
    for part in file_path.parts:
        if part in skip_dirs:
            return True
    return False


def collect_files_to_process(root_path, extensions, skip_dirs):
    """Collect all files that need to be processed"""
    files_to_process = []
    total_files_found = 0
    
    print("Scanning files...")
    
    for file_path in root_path.rglob('*'):
        total_files_found += 1
        if total_files_found % 10000 == 0:
            print(f"Scanned {total_files_found:,} files...")
        
        # Skip if it's not a file
        if not file_path.is_file():
            continue
            
        # Skip if path contains any skip directories
        if should_skip_path(file_path, skip_dirs):
            continue
            
        # Get file extension
        extension = get_file_extension(file_path)
        
        # Only process supported extensions
        if extension in extensions:
            files_to_process.append((file_path, extension))
    
    print(f"Found {len(files_to_process):,} code files to analyze (scanned {total_files_found:,} total files)")
    return files_to_process


def process_file_batch(file_batch):
    """Process a batch of files and return results"""
    batch_lines = 0
    batch_extension_counts = defaultdict(int)
    batch_file_counts = defaultdict(int)
    
    for file_path, extension in file_batch:
        line_count = count_lines_in_file(file_path)
        if line_count > 0:
            batch_lines += line_count
            batch_extension_counts[extension] += line_count
            batch_file_counts[extension] += 1
    
    return batch_lines, batch_extension_counts, batch_file_counts


def count_lines_in_directory(directory_path, max_workers=None):
    """Count lines of code in the specified directory using parallel processing"""
    start_time = time.time()
    
    # Supported file extensions
    extensions = {
        '.py', '.cs', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c',
        '.h', '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.scala', '.sh',
        '.ps1', '.sql', '.xml', '.json', '.yaml', '.yml', '.jsx', '.tsx',
        '.vue', '.scss', '.sass', '.less', '.m', '.mm', '.r', '.pl', '.lua'
    }
    
    # Directories to skip
    skip_dirs = {
        '.git', '.vscode', 'node_modules', '__pycache__', '.pytest_cache',
        'venv', 'env', 'bin', 'obj', 'target', 'build', 'dist', '.idea',
        '.vs', 'coverage', '.nyc_output', 'logs'
    }
    
    # Convert to Path object and resolve
    root_path = Path(directory_path).resolve()
    
    if not root_path.exists():
        print(f"Error: Path '{directory_path}' does not exist.")
        return None, None, None, None, None
    
    if not root_path.is_dir():
        print(f"Error: Path '{directory_path}' is not a directory.")
        return None, None, None, None, None
    
    print(f"Counting lines of code in: {root_path}")
    print()
    
    # Collect all files to process
    files_to_process = collect_files_to_process(root_path, extensions, skip_dirs)
    
    if not files_to_process:
        end_time = time.time()
        analysis_time = end_time - start_time
        return 0, defaultdict(int), defaultdict(int), root_path, analysis_time
    
    # Initialize counters
    total_lines = 0
    extension_counts = defaultdict(int)
    file_counts = defaultdict(int)
    
    # Process files in parallel
    if max_workers is None:
        max_workers = min(32, (os.cpu_count() or 1) + 4)
    
    # Split files into batches for better load balancing
    batch_size = max(1, len(files_to_process) // (max_workers * 4))
    file_batches = [files_to_process[i:i + batch_size]
                   for i in range(0, len(files_to_process), batch_size)]
    
    print(f"Processing {len(files_to_process):,} files using {max_workers} threads...")
    
    processed_files = 0
    lock = threading.Lock()
    
    def update_progress():
        nonlocal processed_files
        with lock:
            processed_files += 1
            if processed_files % 1000 == 0 or processed_files == len(file_batches):
                progress = (processed_files / len(file_batches)) * 100
                print(f"Progress: {progress:.1f}% ({processed_files}/{len(file_batches)} batches)")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all batches
        future_to_batch = {executor.submit(process_file_batch, batch): batch
                          for batch in file_batches}
        
        # Collect results as they complete
        for future in as_completed(future_to_batch):
            try:
                batch_lines, batch_extension_counts, batch_file_counts = future.result()
                
                # Merge results
                total_lines += batch_lines
                for ext, count in batch_extension_counts.items():
                    extension_counts[ext] += count
                for ext, count in batch_file_counts.items():
                    file_counts[ext] += count
                
                update_progress()
                
            except Exception as exc:
                print(f"Batch processing generated an exception: {exc}")
    
    end_time = time.time()
    analysis_time = end_time - start_time
    
    print()
    return total_lines, extension_counts, file_counts, root_path, analysis_time
    return total_lines, extension_counts, file_counts, root_path


def display_results(total_lines, extension_counts, file_counts, root_path, analysis_time):
    """Display the counting results"""
    print("=" * 60)
    print("Code Lines Statistics")
    print("=" * 60)
    print(f"Directory: {root_path}")
    print()
    print(f"Total Lines: {total_lines:,}")
    print(f"Total Files: {sum(file_counts.values()):,}")
    print(f"Analysis Time: {analysis_time:.3f} seconds")
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
    print("  python code_counter.py                    # Count lines in current directory")
    print("  python code_counter.py /path/to/project   # Count lines in specified directory")
    print("  python code_counter.py ../other-project   # Count lines in relative path")
    print("  python code_counter.py --help             # Show detailed help")
    print()


def main():
    """Main function to count lines of code"""
    parser = argparse.ArgumentParser(
        description='Count lines of code in various programming language files (optimized for large repositories)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python code_counter.py              # Count lines in current directory
    python code_counter.py /path/to/project    # Count lines in specified directory
    python code_counter.py ../other-project   # Count lines in relative path
    python code_counter.py --threads 8 /path/to/large-repo  # Use 8 threads for large repositories
        """
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to analyze (default: current directory)'
    )
    parser.add_argument(
        '--threads',
        type=int,
        default=None,
        help='Number of threads to use for parallel processing (default: auto-detect)'
    )
    
    args = parser.parse_args()
    
    # Show usage examples when using default path (current directory)
    if args.path == '.':
        show_usage_examples()
    
    # Count lines in the specified directory
    total_lines, extension_counts, file_counts, root_path, analysis_time = count_lines_in_directory(args.path, args.threads)
    
    # Display results if successful
    if total_lines is not None:
        display_results(total_lines, extension_counts, file_counts, root_path, analysis_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)