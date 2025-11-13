---
title: rust-analyzer
---

# rust-analyzer

## 项目简介

rust-analyzer 是一个为 Rust 编程语言提供 IDE 功能的语言服务器。它实现了 [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)，可以与支持 LSP 的编辑器（如 VS Code、Vim、Emacs、Zed 等）集成使用。

## 主要功能

- **代码导航**：支持跳转到定义（go-to-definition）、查找所有引用（find-all-references）等功能。
- **重构**：提供各种代码重构工具，帮助改进代码结构。
- **代码补全**：智能代码补全，提升编写 Rust 代码的效率。
- **格式化**：集成 rustfmt，支持代码格式化。
- **诊断**：集成 rustc 和 clippy，提供编译错误和代码质量检查。

内部结构上，rust-analyzer 是一组用于分析 Rust 代码的库。更多架构信息请参考 [Architecture](https://rust-analyzer.github.io/book/contributing/architecture.html)。

## 使用方法

1. **安装**：请参考官方安装指南 [https://rust-analyzer.github.io/book/installation.html](https://rust-analyzer.github.io/book/installation.html)。
2. **配置编辑器**：在支持 LSP 的编辑器中配置 rust-analyzer 作为语言服务器。
3. **开始使用**：打开 Rust 项目，享受 IDE 功能如代码补全、错误检查等。

## 文档和资源

- **官方文档**：[https://rust-analyzer.github.io/book/](https://rust-analyzer.github.io/book/)
- **贡献指南**：查看 [CONTRIBUTING.md](https://github.com/rust-lang/rust-analyzer/blob/master/CONTRIBUTING.md)
- **社区**：在 Rust 论坛的 "IDEs and Editors" 类别提问：[https://users.rust-lang.org/c/ide/14](https://users.rust-lang.org/c/ide/14)
- **开发讨论**：加入 Zulip 上的 rust-analyzer 工作组：[https://rust-lang.zulipchat.com/#narrow/stream/185405-t-compiler.2Frust-analyzer](https://rust-lang.zulipchat.com/#narrow/stream/185405-t-compiler.2Frust-analyzer)

## 许可证

rust-analyzer 采用 MIT 和 Apache License (Version 2.0) 双许可证。
