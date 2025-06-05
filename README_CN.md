# 跨平台代码行数统计工具 (Python)

[英文版本 | English Version](README.md)

这是一个跨平台的 Python 脚本，用于统计各种编程语言文件的代码行数。

## 使用方法

适用于 Windows、macOS 和 Linux，需要 Python 3+：

```bash
# 统计当前目录的代码行数（会显示使用示例）
python code_counter.py

# 统计指定目录的代码行数
python code_counter.py /path/to/project

# 统计相对路径的代码行数
python code_counter.py ../other-project

# 显示详细帮助信息
python code_counter.py --help
```

在类Unix系统上：
```bash
python3 code_counter.py [路径]
```

## 功能特性

- **递归扫描**：分析当前目录及所有子目录中的文件
- **多语言支持**：支持25+种编程语言和文件类型
- **智能过滤**：自动排除常见目录，如：
  - `.git`、`.vscode`、`node_modules`
  - `__pycache__`、`.pytest_cache`、`venv`、`env`
  - `bin`、`obj`、`target`、`build`、`dist`
  - `logs`、`.idea`、`.vs`、`coverage`
- **非空行统计**：只统计有实际内容的行（忽略空行）
- **详细统计信息**：显示总行数、文件数量和按文件类型分类的统计
- **灵活路径支持**：可通过命令行参数分析任意目录
- **用户友好**：无参数运行时显示使用示例

## 支持的文件扩展名

- **Python**: `.py`
- **C/C++**: `.c`, `.cpp`, `.h`
- **C#**: `.cs`
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx`
- **Web前端**: `.html`, `.css`, `.scss`, `.sass`, `.less`, `.vue`
- **Java**: `.java`
- **数据库**: `.sql`
- **配置文件**: `.json`, `.yaml`, `.yml`, `.xml`
- **脚本**: `.sh`, `.ps1`
- **其他**: `.php`, `.rb`, `.go`, `.rs`, `.swift`, `.kt`, `.scala`, `.m`, `.mm`, `.r`, `.pl`, `.lua`

## 输出示例

无参数运行时，会显示使用示例：

```
Usage Examples:
  python code_counter.py                    # Count lines in current directory
  python code_counter.py /path/to/project   # Count lines in specified directory
  python code_counter.py ../other-project   # Count lines in relative path
  python code_counter.py --help             # Show detailed help

Counting lines of code in: /path/to/your/project

============================================================
Code Lines Statistics
============================================================
Directory: /path/to/your/project

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

指定自定义路径时，只显示统计结果：

```
Counting lines of code in: /path/to/your/project/src

============================================================
Code Lines Statistics
============================================================
Directory: /path/to/your/project/src

Total Lines: 954
Total Files: 7

By File Type:
------------------------------
     .py:      954 lines (   7 files)

============================================================
```

## 优势特点

- **跨平台**：适用于 Windows、macOS 和 Linux
- **灵活路径支持**：可通过命令行参数分析任意目录
- **更好的错误处理**：优雅处理编码问题和无法读取的文件
- **用户友好**：无参数运行时显示使用示例
- **更准确**：使用 Python 强大的文件处理能力
- **易于维护**：容易扩展和修改
- **无依赖**：仅使用 Python 标准库

## 系统要求

- Python 3.6 或更高版本
- 无需额外依赖

## 安装使用

将 `code_counter.py` 脚本复制到您的项目目录并运行即可，无需额外安装。

## 常用命令示例

```bash
# 统计当前项目代码行数
python code_counter.py

# 统计源码目录
python code_counter.py src

# 统计测试目录
python code_counter.py test

# 统计上级目录的其他项目
python code_counter.py ../other-project

# 统计绝对路径
python code_counter.py C:\Projects\MyApp