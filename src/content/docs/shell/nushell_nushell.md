---
title: nushell
---

# Nushell（nu）

**项目地址**  
[https://github.com/nushell/nushell](https://github.com/nushell/nushell)

## 概述

Nushell 是一个新型 shell。

Nushell 从 PowerShell、函数式编程语言和现代 CLI 工具中汲取灵感。与将文件和数据视为原始文本流的传统 shell 不同，Nu 将每个输入视为具有结构的东西。例如，当您列出目录的内容时，您得到的是一个行表，其中每一行代表该目录中的一个项目。这些值可以通过一系列步骤进行管道传输，在一系列称为“管道”的命令中。

## 主要特性

- **结构化数据管道**：命令的输入、输出均为结构化表格/行数据，避免 `grep`/`awk` 之类的文本解析陷阱。
- **可组合的管道语法**：类似 `|` 的管道操作可对列、行进行任意组合，支持自定义函数 (`def`) 与脚本。
- **类型安全**：内置类型系统 (int, float, str, bool, table, list, set, function...) 让错误在编译期被捕获。
- **高可扩展**：可轻松编写自定义插件（Rust、Python、Shell 等），并通过 Cargo 管理依赖。
- **插件支持**：支持插件扩展，遵循结构化数据模型。
- **跨平台**：原生支持 Windows、macOS、Linux，内部使用 Rust 进行高效实现。
- **友好的交互**：交互式提示符、内置命令补全、语法高亮、历史记录等。
- **内置模块**：文件系统、网络、数据库、进程管理等，方便快速调试。
- **功能性数据处理**：使用函数式方法处理数据，避免可变状态。

## 核心功能

- **数据查询**：`open`, `list`, `parse`, `filter`, `sort-by`, `select`, `rename` 等。
- **表格操作**：`into rows`, `into columns`, `flatten`, `pivot`, `group-by`。
- **函数与脚本**：使用 `def` 定义函数，并支持 `mui`（多变体）。
- **执行外部程序**：`system`, `run`, `open` 等。
- **变量与环境**：`env`、`set`, `def-env`。
- **错误处理**：通过 `match`, `try`, `catch` 等机制统一错误处理。
- **插件生态**：例如 `nu-plugin-git`, `nu-plugin-call`, `nu-plugin-cloud` 等。

## 用法

```bash
# 安装（示例）
# 1. 使用 Cargo
cargo install nu

# 2. 预编译二进制
$ wget https://github.com/nushell/nushell/releases/latest/download/nu-<os>-x86_64.tar.gz
$ tar zxvf nu-<os>-x86_64.tar.gz
$ sudo mv nu-<os>-x86_64/nu /usr/local/bin/

# 启动
nu

# 例子：列出当前目录文件并按大小排序
ls | sort-by size

# 读取 JSON 并过滤
cat data.json | from json | where age > 30 | select name, age
```

## 参考资料

- 官方文档：[https://www.nushell.sh/book/](https://www.nushell.sh/book/)
- GitHub wiki: [https://github.com/nushell/nushell/wiki](https://github.com/nushell/nushell/wiki)
- 代码示例与插件市场

---

> **提示**：在编写自定义函数时，建议使用 `--test` 进行单元测试，以保证函数在管道中的正确性。
