
---
title: pspg
---

# PSPG 项目

**GitHub 项目地址**: [https://github.com/okbob/pspg](https://github.com/okbob/pspg)

## 主要特性
PSPG（PostgreSQL Pager）是一个开源工具，专为 PostgreSQL 数据库设计，用于高效浏览和导航大型查询结果集。它类似于 `less` 命令，但针对 SQL 输出进行了优化。主要特性包括：
- **交互式分页浏览**：支持上下滚动、搜索和过滤查询结果，支持数百万行数据的快速加载和显示。
- **高效性能**：使用 C 语言编写，内存占用低，支持实时排序、过滤和聚合操作，而无需重新执行查询。
- **颜色高亮和格式化**：自动高亮 SQL 输出，支持自定义颜色主题、列对齐和数值格式化（如货币、日期）。
- **键盘快捷键**：丰富的快捷键支持，包括搜索（`/search`）、正则表达式过滤、标记行和导出子集。
- **多平台支持**：兼容 Linux、macOS 和 Windows，支持终端和 SSH 环境。
- **扩展性**：可与 `psql` 集成，作为 PostgreSQL 的默认分页器；支持 CSV/TSV 导入和导出。

## 主要功能
- **查询结果导航**：加载 `\pset pager on` 后的 SQL 输出，支持水平/垂直滚动、跳到特定行或列。
- **数据操作**：内置排序（按列升/降序）、过滤（基于条件或正则）、聚合统计（如求和、平均值）。
- **搜索与高亮**：全文搜索、行/列高亮，支持忽略大小写和多模式匹配。
- **自定义配置**：通过配置文件（`~/.pspgconf`）设置主题、默认行为和快捷键。
- **导出功能**：将当前视图导出为 CSV、SQL INSERT 语句或剪贴板。
- **其他**：支持多窗口模式、冻结列、数值编辑预览，以及与 `pgcli` 等工具的集成。

## 用法
### 安装
- **从源代码编译**（推荐）：
  1. 克隆仓库：`git clone https://github.com/okbob/pspg.git`
  2. 进入目录：`cd pspg`
  3. 配置并编译：`./configure && make && sudo make install`
  - 依赖：PostgreSQL 开发库（`libpq`）、ncurses 和 readline。

- **预编译包**：
  - Ubuntu/Debian：`sudo apt install pspg`
  - Homebrew（macOS）：`brew install pspg`
  - Windows：通过 MSYS2 或预构建二进制文件。

### 基本用法
1. **独立模式**（直接浏览文件或查询）：
   - 浏览 SQL 输出文件：`pspg output.sql`
   - 从 PostgreSQL 查询：`psql -c "SELECT * FROM large_table;" | pspg`

2. **与 psql 集成**：
   - 在 `psql` 中启用：`\pset pager always` 或设置环境变量 `PSPG_PAGER=pspg`。
   - 示例：在 `psql` 中运行查询 `SELECT * FROM users LIMIT 1000000;`，结果将自动通过 PSPG 分页显示。
   - 退出 PSPG：按 `q`。

3. **命令行选项**：
   - `-s <size>`：设置初始窗口大小。
   - `-X`：禁用 X11 颜色（纯终端模式）。
   - `-f <config>`：指定配置文件。
   - 示例：`pspg -s 100x50 large_result.csv`

4. **交互命令**（在 PSPG 内）：
   - `h`：显示帮助。
   - `Enter` 或 `j/k`：上下移动。
   - `F`：全屏模式。
   - `/`：搜索模式。
   - `:`：执行命令，如 `:sort col1`（排序）或 `:filter value > 100`（过滤）。

更多详情请参考项目 README 或运行 `pspg --help`。