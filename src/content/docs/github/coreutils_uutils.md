
---
title: coreutils
---


# uutils/coreutils

<uutils/coreutils> 是一套基于 Rust 重新实现 `coreutils` 的工具集合，旨在提供与 GNU coreutils 完全兼容的命令行工具，同时保持安全、高效和可维护性。它支持多平台（Linux、macOS、Windows）并实现了大多数传统 Unix 工具的功能。

---

## 主要特性

- **完全兼容**：与 GNU coreutils 的行为保持一致，能够无缝替换系统自带工具。
- **跨平台**：在 Linux、macOS、Windows 以及其他支持 Rust 的平台上均可运行。
- **模块化**：每个工具都实现为单独的 crate，代码结构清晰，易于维护。
- **强类型 & 内存安全**：利用 Rust 的类型系统和所有权机制，降低运行时错误。
- **现代化的构建工具**：使用 Cargo 进行依赖管理、编译和发布，便于集成与 CI/CD。

---

## 主要功能

| 工具 | 简述 |
|------|------|
| `cat` | 读取并输出文件内容 |
| `chmod` | 更改文件权限 |
| `echo` | 输出文本字符串 |
| `head` | 显示文件或输入流的前 N 行 |
| `ls` | 列出目录内容 |
| `mv` | 移动/重命名文件 |
| `sed` | 流编辑器，支持正则替换 |
| `sort` | 对文本进行排序 |
| `tee` | 将标准输入复制到文件并输出 |
| `touch` | 修改时间戳或创建文件 |
| `uname` | 显示系统信息 |
| … | 其它典型 Unix 工具（如 `awk`, `cut`, `date`, `du`, `find`, `grep`, `head`, `tail`, `wc` 等） |

> 上表为常见工具示例，完整列表请参阅仓库 README。

---

## 用法

### 安装

```bash
cargo install uutils-coreutils
```

> 也可以使用 `cargo install` 直接从 GitHub 安装，或者通过发行版的包管理器（如 `brew`, `apt`, `winget`）获取对应平台的二进制文件。

### 运行

安装后，工具将在 `$PATH` 中可用。示例：

```bash
# 列出当前目录内容
ls

# 输出文件内容
cat README.md

# 显示前 20 行
head -n 20 file.txt

# 更改权限
chmod 755 script.sh

# 替换文本
sed 's/foo/bar/g' input.txt > output.txt
```

### 组合使用

uutils 的工具支持标准管道，充分利用 Unix 典型的“少量职责、组合可重组”原则：

```bash
# 列出所有 .rs 文件并压缩
ls *.rs | tar -czf rust_files.tar.gz
```

---

## 贡献与开发

- **代码仓库**: `https://github.com/uutils/coreutils`
- **文档与 issue 跟踪**: 使用 GitHub Issues
- **测试**: `cargo test` 运行全部测试
- **请遵循**: Rust 项目标准代码风格，使用 `rustfmt` 和 Clippy

---

## 参考链接

- 官方 GitHub 地址: [https://github.com/uutils/coreutils](https://github.com/uutils/coreutils)
- 文档与使用手册: 在仓库根目录的 `README.md` 与每个工具的子目录中说明

```

