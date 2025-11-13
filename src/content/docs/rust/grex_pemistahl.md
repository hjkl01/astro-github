---
title: grex
---

# grex 项目概述

## 项目地址
[https://github.com/pemistahl/grex](https://github.com/pemistahl/grex)

## 主要特性
- **命令行工具**：grex 是一个高效的命令行工具，用于从正则表达式（regex）生成基于样本的正则表达式，支持多种编程语言的语法。
- **多语言支持**：兼容 Perl、PCRE2、JavaScript、Python、Ruby 和 Go 等语言的正则表达式语法，确保生成的表达式在不同环境中通用。
- **样本驱动生成**：基于提供的字符串样本自动推断和生成简洁的正则表达式，减少手动编写复杂正则的负担。
- **优化与简洁**：生成的正则表达式经过优化，力求简短且高效，支持捕获组和非捕获组的处理。
- **跨平台兼容**：编写于 Rust 语言，支持 Windows、macOS 和 Linux 等操作系统，安装简单且性能出色。
- **开源许可**：采用 MIT 许可，免费开源，欢迎贡献和扩展。

## 主要功能
- **从样本生成正则**：输入一组示例字符串，grex 会分析模式并输出匹配这些样本的正则表达式。
- **自定义选项**：支持指定语言类型、捕获组模式、输出格式等选项，以适应不同需求。
- **验证与测试**：生成的正则可直接用于匹配样本，并支持在多种引擎中验证。
- **批量处理**：可处理多个样本文件或输入流，适合自动化脚本和数据处理任务。
- **错误处理**：提供详细的错误反馈，帮助用户调试样本或选项。

## 用法
### 安装
通过 Cargo（Rust 包管理器）安装：
```
cargo install grex
```

或者从 GitHub Releases 下载预编译二进制文件。

### 基本用法
1. **简单生成**：
   ```
   grex "pattern1" "pattern2" ...
   ```
   示例：
   ```
   grex "John Doe" "Jane Smith" "Bob Johnson"
   ```
   输出：一个匹配这些名字模式的正则表达式，如 `^[A-Z][a-z]+ [A-Z][a-z]+$`。

2. **指定语言**：
   ```
   grex --language pcre2 "sample1" "sample2"
   ```
   支持的语言：`perl`、`pcre2`、`javascript`、`python`、`ruby`、`go`。

3. **从文件读取样本**：
   ```
   grex --file samples.txt
   ```

4. **高级选项**：
   - `--capture`：启用捕获组。
   - `--non-capturing`：使用非捕获组。
   - `--with-flag`：添加正则标志（如 `i` 表示忽略大小写）。
   - `--json`：以 JSON 格式输出结果。

更多细节请参考项目 README：https://github.com/pemistahl/grex/blob/master/README.md。