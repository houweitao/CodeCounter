#!/usr/bin/env python3
"""
Ultra-fast code line counter - Turbo Edition
Optimized for maximum speed on large repositories
"""

import os
import sys
import time
import argparse
import mmap
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import multiprocessing as mp


def count_lines_fast_bytes(file_path):
    """Ultra-fast line counting using byte-level operations"""
    try:
        with open(file_path, 'rb') as f:
            # Get file size first
            f.seek(0, 2)  # Seek to end
            file_size = f.tell()
            
            if file_size == 0:
                return 0
            
            # For very small files, use simple approach
            if file_size < 1024:
                f.seek(0)
                content = f.read()
                lines = content.split(b'\n')
                return sum(1 for line in lines if line.strip())
            
            # For larger files, use memory mapping
            f.seek(0)
            try:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    line_count = 0
                    buffer_size = 64 * 1024  # 64KB buffer
                    
                    pos = 0
                    current_line = b''
                    
                    while pos < file_size:
                        # Read chunk
                        chunk_size = min(buffer_size, file_size - pos)
                        chunk = mm[pos:pos + chunk_size]
                        pos += chunk_size
                        
                        # Process chunk
                        lines = (current_line + chunk).split(b'\n')
                        current_line = lines[-1]  # Save incomplete line
                        
                        # Count non-empty lines
                        for i in range(len(lines) - 1):
                            if lines[i].strip():
                                line_count += 1
                    
                    # Handle last line
                    if current_line.strip():
                        line_count += 1
                    
                    return line_count
                    
            except (OSError, ValueError):
                # Fallback to regular reading
                f.seek(0)
                return sum(1 for line in f if line.strip())
                
    except Exception:
        return 0


def is_text_file_fast(file_path, sample_size=512):
    """Fast text file detection"""
    try:
        with open(file_path, 'rb') as f:
            sample = f.read(sample_size)
            if not sample:
                return True
            
            # Check for null bytes (binary indicator)
            if b'\x00' in sample:
                return False
            
            # Quick ASCII ratio check
            ascii_count = sum(1 for b in sample if b < 128)
            return (ascii_count / len(sample)) > 0.8
    except:
        return False


def process_file_batch_turbo(args):
    """Process a batch of files with maximum speed"""
    file_batch, extensions = args
    
    batch_lines = 0
    batch_extension_counts = defaultdict(int)
    batch_file_counts = defaultdict(int)
    
    for file_path, extension in file_batch:
        try:
            # Quick size check
            file_size = file_path.stat().st_size
            
            # Skip empty files
            if file_size == 0:
                continue
                
            # Skip very large files (likely binary/data)
            if file_size > 50 * 1024 * 1024:  # 50MB
                continue
            
            # Fast text file check for medium files
            if file_size > 10240 and not is_text_file_fast(file_path):
                continue
            
            # Count lines using optimized method
            line_count = count_lines_fast_bytes(file_path)
            
            if line_count > 0:
                batch_lines += line_count
                batch_extension_counts[extension] += line_count
                batch_file_counts[extension] += 1
                
        except Exception:
            continue
    
    return batch_lines, dict(batch_extension_counts), dict(batch_file_counts)


def collect_files_turbo(root_path, extensions, skip_dirs):
    """Ultra-fast file collection with pre-filtering"""
    files_to_process = []
    
    print("Scanning files...")
    start_scan = time.time()
    
    # Use os.walk for faster directory traversal
    for root, dirs, files in os.walk(root_path):
        # Filter directories in-place to avoid traversing them
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        root_path_obj = Path(root)
        
        for filename in files:
            file_path = root_path_obj / filename
            
            # Quick extension check
            if '.' not in filename:
                continue
                
            ext = '.' + filename.split('.')[-1].lower()
            if ext not in extensions:
                continue
            
            # Quick file size check to skip very large files early
            try:
                if file_path.stat().st_size > 100 * 1024 * 1024:  # 100MB
                    continue
            except:
                continue
                
            files_to_process.append((file_path, ext))
    
    scan_time = time.time() - start_scan
    print(f"Scanned {len(files_to_process):,} code files in {scan_time:.3f}s")
    
    return files_to_process


def show_usage_examples_turbo():
    """Show turbo usage examples"""
    print("🚀 Turbo Usage Examples:")
    print("  python code_counter_turbo.py                        # Turbo count in current directory")
    print("  python code_counter_turbo.py /path/to/large-repo    # Turbo count in specified directory")
    print("  python code_counter_turbo.py --threads ../project   # Use threads instead of processes")
    print("  python code_counter_turbo.py --workers 16 /path     # Use custom number of workers")
    print("  python code_counter_turbo.py --help                 # Show detailed help")
    print()


def count_lines_turbo(directory_path, max_workers=None, use_processes=True, show_examples=False):
    """Turbo-charged line counting with maximum optimization"""
    start_time = time.time()
    
    # Supported extensions
    extensions = {
        '.py', '.cs', '.js', '.ts', '.html', '.css', '.java', '.cpp', '.c',
        '.h', '.hpp', '.cxx', '.cc', '.php', '.rb', '.go', '.rs', '.swift',
        '.kt', '.scala', '.sh', '.ps1', '.sql', '.xml', '.json', '.yaml',
        '.yml', '.jsx', '.tsx', '.vue', '.scss', '.sass', '.less', '.m',
        '.mm', '.r', '.pl', '.lua', '.dart', '.zig', '.nim', '.hx'
    }
    
    # Directories to skip
    skip_dirs = {
        '.git', '.svn', '.hg', '.vscode', '.idea', '.vs', 'node_modules',
        '__pycache__', '.pytest_cache', 'venv', 'env', '.env', 'bin', 'obj',
        'target', 'build', 'dist', 'coverage', '.nyc_output', 'logs', 'tmp',
        '.cache', 'vendor', 'third_party', 'external', '.gradle'
    }
    
    root_path = Path(directory_path).resolve()
    
    if not root_path.exists() or not root_path.is_dir():
        return None, None, None, None, None
    
    print(f"🚀 Turbo counting lines of code in: {root_path}")
    print()
    
    # Show usage examples when using default path (current directory)
    if show_examples:
        show_usage_examples_turbo()
    
    # Collect files
    files_to_process = collect_files_turbo(root_path, extensions, skip_dirs)
    
    if not files_to_process:
        print("⚠️  No supported code files found.")
        return 0, defaultdict(int), defaultdict(int), root_path, time.time() - start_time
    
    # Determine optimal worker count
    if max_workers is None:
        cpu_count = os.cpu_count() or 1
        if use_processes:
            max_workers = cpu_count
        else:
            max_workers = min(32, cpu_count * 2)
    
    # Create optimized batches
    if use_processes:
        # Larger batches for processes to reduce IPC overhead
        batch_size = max(10, len(files_to_process) // (max_workers * 2))
    else:
        # Smaller batches for threads for better load balancing
        batch_size = max(5, len(files_to_process) // (max_workers * 4))
    
    batches = []
    for i in range(0, len(files_to_process), batch_size):
        batch = files_to_process[i:i + batch_size]
        batches.append((batch, extensions))
    
    print(f"Processing {len(files_to_process):,} files in {len(batches)} batches using {max_workers} {'processes' if use_processes else 'threads'}...")
    
    # Process files
    total_lines = 0
    extension_counts = defaultdict(int)
    file_counts = defaultdict(int)
    
    executor_class = ProcessPoolExecutor if use_processes else ThreadPoolExecutor
    
    with executor_class(max_workers=max_workers) as executor:
        # Submit all batches
        future_to_batch = {
            executor.submit(process_file_batch_turbo, batch_args): i 
            for i, batch_args in enumerate(batches)
        }
        
        completed = 0
        for future in as_completed(future_to_batch):
            try:
                batch_lines, batch_ext_counts, batch_file_counts = future.result()
                
                total_lines += batch_lines
                for ext, count in batch_ext_counts.items():
                    extension_counts[ext] += count
                for ext, count in batch_file_counts.items():
                    file_counts[ext] += count
                
                completed += 1
                if completed % max(1, len(batches) // 20) == 0 or completed == len(batches):
                    progress = (completed / len(batches)) * 100
                    print(f"Progress: {progress:.1f}% ({completed}/{len(batches)} batches)")
                    
            except Exception as e:
                print(f"Batch processing error: {e}")
    
    analysis_time = time.time() - start_time
    return total_lines, extension_counts, file_counts, root_path, analysis_time


def display_results_turbo(total_lines, extension_counts, file_counts, root_path, analysis_time):
    """Display results with performance metrics"""
    print()
    print("=" * 70)
    print("🚀 TURBO CODE ANALYSIS RESULTS 🚀")
    print("=" * 70)
    print(f"📁 Directory: {root_path}")
    print(f"⏱️  Analysis Time: {analysis_time:.3f} seconds")
    
    total_files = sum(file_counts.values())
    if analysis_time > 0:
        files_per_sec = total_files / analysis_time
        lines_per_sec = total_lines / analysis_time
        print(f"⚡ Performance: {files_per_sec:,.0f} files/sec, {lines_per_sec:,.0f} lines/sec")
    
    print()
    print(f"📊 Total Lines: {total_lines:,}")
    print(f"📁 Total Files: {total_files:,}")
    print()
    
    if extension_counts:
        print("📈 Breakdown by File Type:")
        print("-" * 50)
        sorted_extensions = sorted(extension_counts.items(), key=lambda x: x[1], reverse=True)
        for ext, lines in sorted_extensions:
            files = file_counts[ext]
            avg_lines = lines / files if files > 0 else 0
            percentage = (lines / total_lines * 100) if total_lines > 0 else 0
            print(f"{ext:>8}: {lines:>10,} lines ({files:>5} files) [{percentage:>5.1f}%] avg: {avg_lines:>6.1f}")
    else:
        print("⚠️  No supported code files found.")
    
    print()
    print("=" * 70)
    print("💡 Tip: Use --threads for smaller projects, default (processes) for large repos")
    print("📖 See PERFORMANCE_COMPARISON.md for detailed benchmarks")


def main():
    parser = argparse.ArgumentParser(
        description='🚀 Ultra-fast code line counter - Turbo Edition (optimized for large repositories)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🚀 Turbo Examples:
    python code_counter_turbo.py              # Turbo count in current directory
    python code_counter_turbo.py /path/to/large-repo    # Turbo count in specified directory
    python code_counter_turbo.py --threads ../project   # Use threads (faster startup)
    python code_counter_turbo.py --workers 16 /huge-repo # Use 16 workers for massive repos
    
💡 Performance Tips:
    - Use default (processes) for large repositories (1000+ files)
    - Use --threads for smaller projects (faster startup, less overhead)
    - Adjust --workers based on your CPU cores for optimal performance
        """
    )
    parser.add_argument('path', nargs='?', default='.', help='Path to analyze (default: current directory)')
    parser.add_argument('--workers', type=int, default=None, help='Number of workers (default: auto-detect based on CPU cores)')
    parser.add_argument('--threads', action='store_true', help='Use threads instead of processes (better for smaller projects)')
    
    args = parser.parse_args()
    
    # Show usage examples when using default path (current directory)
    show_examples = args.path == '.'
    
    use_processes = not args.threads
    result = count_lines_turbo(args.path, args.workers, use_processes, show_examples)
    
    if result[0] is not None:
        display_results_turbo(*result)
    else:
        print("❌ Analysis failed. Please check the path and try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚡ Turbo analysis cancelled!")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Error: {e}")
        sys.exit(1)