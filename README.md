# 🚀 Ultra-Fast Code Line Counter - Turbo Edition

[中文版本 | Chinese Version](README_CN.md) | [Performance Analysis](PERFORMANCE_COMPARISON.md)

**⚡ Up to 8.7x faster** than traditional code counters! This ultra-optimized Python tool counts lines of code in various programming languages with blazing speed.

## 🎯 Quick Start

### Turbo Version (Recommended for large projects)
```bash
# Ultra-fast analysis with multi-processing (default)
python code_counter_turbo.py /path/to/large-project

# For smaller projects, use threads (faster startup)
python code_counter_turbo.py --threads /path/to/project

# Custom worker count for massive repositories
python code_counter_turbo.py --workers 16 /path/to/huge-repo

# Current directory with usage examples
python code_counter_turbo.py
```

### Benchmark Version (For comparison & small projects)
```bash
# Single-threaded baseline version
python code_counter_benchmark.py /path/to/project
```

## ⚡ Performance Comparison

| Project Size | Turbo Edition | Standard Version | Speed Up |
|--------------|---------------|------------------|----------|
| **Large** (17K+ files) | **6.95 seconds** | 60.74 seconds | **8.7x faster** ⚡ |
| **Medium** (1K files) | **~1.5 seconds** | ~8 seconds | **5.3x faster** ⚡ |
| **Small** (<100 files) | 0.3 seconds | 0.1 seconds | Use benchmark |

💡 **Performance tip**: Use Turbo for 1000+ files, benchmark version for comparison & small projects.

## 🚀 Turbo Features

- **🔥 Ultra-fast processing**: Multi-processing with automatic CPU detection
- **🧠 Smart optimization**: Memory mapping, byte-level operations, intelligent pre-filtering
- **⚡ Flexible modes**: Choose between processes (max speed) or threads (fast startup)
- **📊 Real-time metrics**: Performance monitoring with files/sec and lines/sec
- **🎯 Intelligent scanning**: Pre-filters binary files and optimizes directory traversal
- **📈 Enhanced reporting**: Percentage breakdown, averages, and performance tips

## 🔧 Benchmark Version Features

- **🌍 Cross-platform**: Works on Windows, macOS, and Linux
- **🔍 Recursive scanning**: Analyzes all files in directories and subdirectories
- **🌐 Language support**: 30+ programming languages and file types
- **🚫 Smart filtering**: Automatically excludes common directories:
  - `.git`, `.vscode`, `node_modules`, `__pycache__`
  - `venv`, `env`, `bin`, `obj`, `target`, `build`, `dist`
  - `logs`, `.idea`, `.vs`, `coverage`, `.cache`
- **📏 Accurate counting**: Only counts non-empty lines with actual content
- **📊 Detailed statistics**: Total lines, file counts, and breakdown by file type
- **🛠 User-friendly**: Shows usage examples and helpful tips

## 📁 Supported File Types

- **Python**: `.py`
- **C/C++**: `.c`, `.cpp`, `.h`, `.hpp`, `.cxx`, `.cc`
- **C#**: `.cs`
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
- **Web**: `.html`, `.css`, `.scss`, `.sass`, `.less`, `.vue`
- **Java**: `.java`
- **Database**: `.sql`
- **Config**: `.json`, `.yaml`, `.yml`, `.xml`
- **Shell**: `.sh`, `.ps1`
- **Modern**: `.go`, `.rs`, `.swift`, `.kt`, `.scala`, `.dart`, `.zig`, `.nim`
- **Other**: `.php`, `.rb`, `.m`, `.mm`, `.r`, `.pl`, `.lua`, `.hx`

## 📋 Example Output

### Turbo Version Output
```
🚀 Turbo counting lines of code in: /path/to/large-project

Scanning files...
Scanned 17,423 code files in 1.776s
Processing 17,423 files in 41 batches using 20 processes...
Progress: 100.0% (41/41 batches)

======================================================================
🚀 TURBO CODE ANALYSIS RESULTS 🚀
======================================================================
📁 Directory: /path/to/large-project
⏱️  Analysis Time: 6.952 seconds
⚡ Performance: 2,506 files/sec, 510,436 lines/sec

📊 Total Lines: 3,548,511
📁 Total Files: 17,419

📈 Breakdown by File Type:
--------------------------------------------------
     .cs:  1,934,050 lines (11711 files) [ 54.5%] avg:  165.1
   .json:    840,740 lines ( 4934 files) [ 23.7%] avg:  170.4
    .xml:    705,712 lines (  205 files) [ 19.9%] avg: 3442.5

======================================================================
💡 Tip: Use --threads for smaller projects, default (processes) for large repos
📖 See PERFORMANCE_COMPARISON.md for detailed benchmarks
```

### Benchmark Version Output
```
Counting lines of code in: /path/to/project

============================================================
Code Lines Statistics
============================================================
Directory: /path/to/project

Total Lines: 5,875
Total Files: 35
Analysis Time: 0.250 seconds

By File Type:
------------------------------
     .py:    3,908 lines (  31 files)
   .html:    1,839 lines (   2 files)
   .json:       96 lines (   1 files)
    .yml:       32 lines (   1 files)
============================================================
```

## 🎯 When to Use Which Version

### 🚀 Use Turbo Edition When:
- **Large repositories** (1000+ files)
- **Time is critical** (CI/CD pipelines)
- **Regular analysis** of big codebases
- **Performance matters** more than startup time

### 📋 Use Benchmark Version When:
- **Performance comparison** with Turbo edition
- **Small projects** (<100 files)
- **Quick checks** on individual directories
- **Baseline measurements**
- **Simple one-off analysis**

## 🛠 Installation & Requirements

- **Python 3.6+** (no additional dependencies)
- **Multi-core CPU** recommended for Turbo edition
- **Cross-platform**: Windows, macOS, Linux

Simply download the scripts - no additional installation required!

## 📊 Performance Deep Dive

For detailed performance analysis, benchmarks, and optimization techniques, see [PERFORMANCE_COMPARISON.md](PERFORMANCE_COMPARISON.md).

**Key optimizations in Turbo edition:**
- 🔧 **Multi-processing**: Bypass Python GIL limitations
- 🗃️ **Memory mapping**: Efficient large file handling  
- ⚡ **Byte-level operations**: Minimize Python object overhead
- 🎯 **Smart pre-filtering**: Skip binary files and large data files
- 📦 **Optimized batching**: Balance load across workers

## 🤝 Contributing

Feel free to contribute improvements, additional language support, or performance optimizations!

## 📄 License

Open source - feel free to use and modify for your projects.