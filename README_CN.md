# 🚀 超高速代码行数统计工具 - Turbo版

[English Version 英文版本](README.md) | [性能分析报告](PERFORMANCE_COMPARISON.md)

**⚡ 比传统代码统计工具快8.7倍！** 这个超级优化的Python工具能以惊人的速度统计各种编程语言的代码行数。

## 🎯 快速开始

### Turbo版本（大型项目推荐）
```bash
# 超高速多进程分析（默认模式）
python code_counter_turbo.py /path/to/large-project

# 小型项目使用线程模式（启动更快）
python code_counter_turbo.py --threads /path/to/project

# 超大仓库自定义工作进程数
python code_counter_turbo.py --workers 16 /path/to/huge-repo

# 当前目录分析（显示使用示例）
python code_counter_turbo.py
```

### 基准版本（对比测试 & 小型项目）
```bash
# 单线程基准版本
python code_counter_benchmark.py /path/to/project
```

## ⚡ 性能对比

| 项目规模 | Turbo版 | 标准版 | 性能提升 |
|----------|---------|--------|----------|
| **大型** (17K+ 文件) | **6.95秒** | 60.74秒 | **快8.7倍** ⚡ |
| **中型** (1K 文件) | **~1.5秒** | ~8秒 | **快5.3倍** ⚡ |
| **小型** (<100 文件) | 0.3秒 | 0.1秒 | 建议用基准版 |

💡 **性能建议**: 1000+文件用Turbo版，小项目用基准版。

## 🚀 Turbo版特性

- **🔥 超高速处理**: 多进程并行，自动检测CPU核心数
- **🧠 智能优化**: 内存映射、字节级操作、智能预筛选
- **⚡ 灵活模式**: 进程模式（最高速度）或线程模式（快速启动）
- **📊 实时指标**: 性能监控，显示文件/秒和行数/秒
- **🎯 智能扫描**: 预筛选二进制文件，优化目录遍历
- **📈 增强报告**: 百分比分解、平均值和性能提示

## 🔧 基准版特性

- **🌍 跨平台支持**: 适用于Windows、macOS和Linux
- **🔍 递归扫描**: 分析目录及所有子目录中的文件
- **🌐 多语言支持**: 支持30+种编程语言和文件类型
- **🚫 智能过滤**: 自动排除常见目录：
  - `.git`, `.vscode`, `node_modules`, `__pycache__`
  - `venv`, `env`, `bin`, `obj`, `target`, `build`, `dist`
  - `logs`, `.idea`, `.vs`, `coverage`, `.cache`
- **📏 精确统计**: 只统计非空的实际代码行
- **📊 详细统计**: 总行数、文件数和按类型分类的统计
- **🛠 用户友好**: 显示使用示例和实用提示

## 📁 支持的文件类型

- **Python**: `.py`
- **C/C++**: `.c`, `.cpp`, `.h`, `.hpp`, `.cxx`, `.cc`
- **C#**: `.cs`
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
- **Web前端**: `.html`, `.css`, `.scss`, `.sass`, `.less`, `.vue`
- **Java**: `.java`
- **数据库**: `.sql`
- **配置文件**: `.json`, `.yaml`, `.yml`, `.xml`
- **脚本**: `.sh`, `.ps1`
- **现代语言**: `.go`, `.rs`, `.swift`, `.kt`, `.scala`, `.dart`, `.zig`, `.nim`
- **其他**: `.php`, `.rb`, `.m`, `.mm`, `.r`, `.pl`, `.lua`, `.hx`

## 📋 输出示例

### Turbo版输出示例
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

### 基准版输出示例
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

## 🎯 版本选择指南

### 🚀 使用Turbo版的场景：
- **大型代码仓库**（1000+文件）
- **时间敏感**（CI/CD流水线）
- **大型代码库的定期分析**
- **性能比启动时间更重要**

### 📋 使用基准版的场景：
- **性能对比测试**（与Turbo版对比）
- **小型项目**（<100文件）
- **单个目录的快速检查**
- **基准测量**
- **简单的一次性分析**

## 🛠 安装和系统要求

- **Python 3.6+**（无需额外依赖）
- **多核CPU**（Turbo版推荐）
- **跨平台**: Windows、macOS、Linux

只需下载脚本文件即可，无需额外安装！

## 📊 性能深度分析

详细的性能分析、基准测试和优化技术，请参见[性能对比分析](PERFORMANCE_COMPARISON.md)。

**Turbo版的核心优化：**
- 🔧 **多进程处理**: 绕过Python GIL限制
- 🗃️ **内存映射**: 高效的大文件处理
- ⚡ **字节级操作**: 最小化Python对象开销
- 🎯 **智能预筛选**: 跳过二进制文件和大型数据文件
- 📦 **优化批处理**: 在工作进程间平衡负载

## 🤖 使用场景示例

### 开发场景
```bash
# 项目代码统计
python code_counter_turbo.py ./src

# 多项目对比
python code_counter_turbo.py ../project-a
python code_counter_turbo.py ../project-b

# CI/CD流水线（快速分析）
python code_counter_turbo.py --threads .
```

### 大型仓库分析
```bash
# 企业级代码库
python code_counter_turbo.py --workers 32 /path/to/enterprise-repo

# 开源项目分析
python code_counter_turbo.py /path/to/large-open-source-project

# 性能测试
time python code_counter_turbo.py /path/to/test-repo
```

## 🚀 进阶使用技巧

### 性能调优
- **CPU密集型**: 使用默认进程模式，设置workers为CPU核心数
- **I/O密集型**: 使用`--threads`模式，可设置更多workers
- **超大仓库**: 逐步增加workers数量找到最佳性能点

### 脚本集成
```bash
# 批量分析脚本
for dir in project1 project2 project3; do
    echo "Analyzing $dir..."
    python code_counter_turbo.py $dir
done
```

## 🤝 贡献指南

欢迎贡献改进、添加语言支持或性能优化！

## 📄 开源协议

开源项目 - 可自由使用和修改！

---

⭐ **如果这个工具对您有帮助，请给个Star！**