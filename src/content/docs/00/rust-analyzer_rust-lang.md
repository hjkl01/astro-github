
---
title: rust-analyzer
---


# Rust Analyzer

**项目地址**  
<https://github.com/rust-lang/rust-analyzer>

## 项目简介
Rust Analyzer 是 Rust 语言的一个跨平台语言服务器（Language Server Protocol, LSP），为 IDE 提供高效、实时的代码分析、补全、跳转、重构等功能。它旨在通过分析 Rust 代码的语义信息，提升编辑体验与开发效率。

## 主要特性

| 特性 | 说明 |
|------|------|
| **即时补全** | 语义层面的智能补全，支持宏、模块、trait、generic 等多种 Rust 语法结构。 |
| **跳转至定义/引用** | 通过快速跳转到实现、定义、引用及实现文档，极大提升代码阅读速度。 |
| **类型信息** | 右侧悬浮提示显示变量、函数返回值等类型信息，支持自定义生成方式。 |
| **代码导航** | 快速跳转到项目内外部 Crate，支持 Cargo 依赖。 |
| **错误检查** | 语法错误、编译错误、未使用变量等问题实时提示，并支持错误定位与修复。 |
| **重构** | 支持重命名、提取方法、移动文件等多种重构操作。 |
| **Hover 文档** | 显示宏展开、Crate 文档注释、标准库文档等信息。 |
| **多语言支持** | 通过 LSP 可与 VS Code、Neovim、Emacs、IntelliJ 等 IDE 集成。 |

## 功能详解

### 1. 代码补全  
提供基于语义信息的补全，完全避免仅基于文本匹配导致的不一致。可在输入中通过 `Ctrl+Space` 调出。

### 2. 跳转功能  
- **跳转到定义** (`F12` 或 `Ctrl+Click`)  
- **跳转到实现** (`Ctrl+Shift+Click`)  
- **显示引用** (`Shift+F12`)  
- **跳转到文档** (`Ctrl+K Ctrl+I`)  

### 3. 代码诊断  
实时检测错误并在编辑器中下划线标注。支持快速修复建议，按 `Ctrl+.` 可弹出修复列表。

### 4. 重构工具  
- **重命名变量/函数** (`F2` 或 `Ctrl+R Ctrl+R`)  
- **提取函数** (`Alt+F8`)  
- **移动文件/模块** (`Ctrl+Shift+M`)  

### 5. 类型信息与查看  
悬停鼠标或使用快捷键查看当前光标位置的完整类型定义。

## 使用方法

### 1. 安装

- **VS Code**  
  1. 打开 Extensions Marketplace  
  2. 搜索 `rust-analyzer` 并安装  
  3. 在 `settings.json` 中设置 `rust-analyzer.checkOnSave.command: clippy` 可启用 Clippy 检查  

- **Neovim**（使用 LSP 客户端）  
  ```lua
  require'lspconfig'.rust_analyzer.setup {
      settings = {
          ["rust-analyzer"] = {
              diagnostics = { enable = true }
          }
      }
  }
  ```

- **其它 IDE**  
  启动 Rust Analyzer 作为 LSP 服务器，配置对应插件（如 JetBrains 的 Rust plugin）即可。

### 2. 基本操作

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+Space` | 补全 |
| `F12` | 跳转到定义 |
| `Shift+F12` | 查看引用 |
| `Ctrl+.` 状态栏错误修复 |
| `Ctrl+R Ctrl+R` | 重命名 |
| `Alt+F8` | 提取函数 |

> **提示**  
> 通过 `rust-analyzer` 的配置文件 `settings.toml` 可自定义详细行为：  
> ```toml
> [rust-analyzer]
> cargo-watch = true
> lens.enable = true
> diagnostics = { enableExperimental = true }
> ```  

### 3. 与 Cargo 集成

Rust Analyzer 会自动加载项目的 `Cargo.toml`、`Cargo.lock`，并对依赖进行索引。  
- 执行 `cargo metadata` 也会被自动同步。  
- 通过 `rust-analyzer.checkOnSave.command` 可以在保存时触发编译诊断。

## 常见问题

| 问题 | 解决办法 |
|------|----------|
| **补全不工作** | 确认 `rust-analyzer.cargo.loadOutDirsFromCheck` 设置为 `true` 或完整的 `Cargo.toml` 目录。 |
| **编译错误提示不完整** | 更新到最新 LSP 服务器与 IDE 插件，或在 `settings.toml` 换用更丰富的诊断选项。 |
| **重构失败** | 确认工作区已正确识别为 Rust 项目，且文件 not part of any crate。 |

## 进一步阅读

- 官方文档: <https://rust-analyzer.github.io/>  
- 常见配置: <https://rust-analyzer.github.io/manual.html#settings>

> **注**  
> 本文件仅记录核心功能与使用，更多高级设置请参阅官方文档。  

```

（将以上内容保存为 `src/content/docs/00/rust-analyzer_rust-lang.md`）