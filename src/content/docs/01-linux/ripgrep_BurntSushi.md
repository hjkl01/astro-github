---
title: ripgrep
---

---

## title: ripgrep

# ripgrep

ripgrep 是一个快速、行导向的搜索工具，它递归搜索当前目录中的正则表达式模式，默认情况下尊重 gitignore 规则并跳过隐藏/二进制文件。

## 功能

- 极致速度：使用 Rust 编写，搜索速度极快。
- 递归搜索：自动遍历目录。
- 正则表达式：支持 PCRE 风格的正则表达式。
- 忽略规则：自动读取 .gitignore 等。
- 多文件类型：支持按类型过滤。
- 并行处理：利用多核 CPU。
- 输出丰富：支持行号、高亮等。

## 用法

1. 安装：从 GitHub Releases 下载，或使用 cargo install ripgrep。
2. 运行：rg "pattern"
3. 选项：rg -n "pattern" 显示行号。

## 许可证

ripgrep 根据 MIT 许可证或 Apache License, Version 2.0 发布。
