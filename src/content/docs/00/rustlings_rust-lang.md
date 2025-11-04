
---
title: rustlings
---


# Rustlings

> 项目地址: [https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings)

---

## 项目简介
Rustlings 是一个针对 Rust 语言学习者的交互式练习工具。它提供了大量的小型代码片段（练习），让学习者在实际编写与调试代码的过程中掌握 Rust 基础与进阶概念。所有练习均通过命令行工具执行，支持即时反馈与自动评分。

---

## 主要特性

- **交互式练习**：每个练习都在本地文件中，学习者只需编辑文件并运行 `cargo test` 或 `cargo watch` 进行即时验证。
- **覆盖面广**：从基本语法（变量、函数、控制流）到高级主题（所有权、借用、生命周期、并发、宏）。
- **易于安装**：使用 Cargo 一行命令即可安装 `rustlings`。
- **自动生成**：`rustlings new` 可以为新手快速生成练习与测试文件。
- **社区贡献**：任何人都可提交 Pull Request，扩展练习内容。
- **多平台支持**：可在 Windows、macOS、Linux 等多种操作系统上运行。

---

## 功能概览

| 功能 | 描述 |
|------|------|
| `rustlings watch` | 监视练习文件变动，自动执行测试并给出反馈。 |
| `rustlings test` | 仅执行一次测试，适合快速检查。 |
| `rustlings new <name>` | 创建一个新的练习项目，包含源文件与测试文件。 |
| `rustlings list` | 列出所有可用的练习。 |
| `rustlings open` | 将所有练习在默认文本编辑器中打开。 |
| `rustlings help` | 查看命令行帮助信息。 |

---

## 用法示例

1. **安装 Rustlings**

   ```bash
   cargo install rustlings
   ```

2. **初始化练习**

   ```bash
   rustlings init
   ```

   这会在当前目录生成 `rustlings` 目录，包含所有练习文件。

3. **开始练习**

   ```bash
   rustlings watch
   ```

   打开 `rustlings` 目录中的任一 `.rs` 文件，修改代码后保存，命令行会自动跑测试并给出提示。

4. **单次测试**

   ```bash
   rustlings test
   ```

5. **创建新练习**

   ```bash
   rustlings new hello-world
   ```

   这会在 `rustlings` 目录下创建 `hello-world.rs` 与对应的测试文件。

---

## 贡献指南

1. Fork 本仓库并克隆到本地。
2. 创建自己的分支：`git checkout -b feature/your-feature`。
3. 编写或改进练习，确保所有测试通过。
4. 提交 PR 并填写相关说明。

---

## 许可证

该项目遵循 MIT 许可证。详情请查看 [LICENSE](https://github.com/rust-lang/rustlings/blob/master/LICENSE)。

---

*祝你在 Rust 学习路上玩得开心！*

