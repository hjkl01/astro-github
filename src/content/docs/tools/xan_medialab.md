---
title: xan
---

# xan

xan 是一个用 Rust 编写的命令行工具，专为处理大型 CSV 文件而设计。它能够快速、内存高效地处理 CSV 数据，支持并行计算，并提供丰富的命令来执行各种数据操作。

## 功能

xan 提供了全面的 CSV 处理功能，包括：

- **数据探索与可视化**：查看文件头、预览数据、绘制直方图、散点图、热力图等
- **搜索与过滤**：基于模式搜索、表达式过滤、行切片等
- **排序与去重**：排序数据、去除重复行
- **聚合分析**：频率统计、描述性统计、分组聚合等
- **数据转换**：选择列、添加新列、转换数据类型、格式转换等
- **文件合并**：连接、合并多个 CSV 文件
- **高级功能**：支持表达式语言进行复杂计算、并行处理、矩阵和网络分析等

xan 支持多种文件格式，包括 CSV、TSV、NDJSON、VCF、GTF 等生物信息学格式，以及压缩文件。

## 用法

xan 的基本用法是通过命令行执行各种子命令，每个命令都有丰富的选项。数据可以通过管道流式处理，支持标准输入输出。

### 基本示例

```bash
# 查看文件头
xan headers data.csv

# 预览数据
xan view data.csv

# 过滤数据
xan filter 'column > 100' data.csv

# 排序数据
xan sort -s column data.csv

# 选择列
xan select col1,col2 data.csv

# 频率统计
xan frequency -s category data.csv | xan hist

# 分组聚合
xan groupby category 'sum(value)' data.csv
```

### 表达式语言

xan 内置了一个强大的表达式语言，支持：

- 数学运算、字符串操作、日期处理
- 条件判断、循环、正则表达式
- 自定义函数和聚合函数
- 并行计算支持

```bash
# 添加计算列
xan map 'col1 + col2 as sum' data.csv

# 复杂过滤
xan filter 'regex_match(pattern, text_column)' data.csv

# 自定义聚合
xan agg 'mean(numeric_col), count(*)' data.csv
```

## 安装

### Cargo

```bash
cargo install xan --locked
```

### 其他安装方式

- **Scoop (Windows)**: `scoop bucket add extras && scoop install xan`
- **Homebrew (macOS)**: `brew install xan`
- **Arch Linux**: `pacman -S xan`
- **NetBSD**: `pkgin install xan`
- **Nix**: `nix-shell -p xan`
- **Pixi**: `pixi global install xan`

也提供预编译二进制文件下载。

## 特点

- **高性能**：使用 SIMD CSV 解析器，支持并行处理
- **内存高效**：针对大型文件优化，最小化内存使用
- **灵活**：支持多种输入格式和数据转换
- **可组合**：命令可以通过管道组合使用
- **跨平台**：支持 Linux、macOS、Windows

xan 特别适合数据科学家、社会科学家和任何需要处理大型 CSV 数据集的用户。
