---
title: Rustlings
---

# Rustlings

Rustlings 是一个帮助你熟悉阅读和编写 Rust 代码的小型练习集合。它是与阅读 [Rust 官方书籍](https://doc.rust-lang.org/book) 并行推荐的工具。

## 功能

- **练习集合**：提供一系列按主题排序的小型练习，帮助你逐步掌握 Rust 的语法、概念和工具。
- **编译错误修复**：大多数练习包含编译错误，你需要修复它们。
- **测试通过**：一些练习包含需要通过的测试。
- **提示系统**：内置提示系统，帮助你在遇到困难时获得指导。
- **交互式列表**：提供交互式练习列表，可以查看进度、跳过或重置练习。
- **自动检测**：在 watch 模式下，自动检测文件变化并重新运行练习。

## 用法

### 安装

1. 确保安装了最新版本的 Rust（包括 Cargo）：访问 [www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) 进行安装。
   - Linux：确保安装了 `gcc`（Debian: `sudo apt install gcc`，Fedora: `sudo dnf install gcc`）。
   - MacOS：确保安装了 Xcode 和开发者工具：`xcode-select --install`。

2. 安装 Rustlings：
   ```bash
   cargo install rustlings
   ```
   如果安装失败，尝试 `rustup update` 更新 Rust，或使用 `--locked` 标志：`cargo install rustlings --locked`。

### 初始化

运行以下命令初始化 `rustlings/` 目录：

```bash
rustlings init
```

### 开始练习

进入目录并启动 Rustlings：

```bash
cd rustlings
rustlings
```

这将启动 watch 模式，按照预定义顺序引导你完成练习。每次修改 `exercises/` 目录中的文件时，会自动重新运行当前练习。

### 其他命令

- 查看练习列表：`l`
- 手动运行练习：`r`（如果文件变化检测失败）
- 获取提示：`h`
- 继续到其他练习：`c`
- 重置练习：`r`（在列表中选择）

### 推荐环境

- **编辑器**：VS Code + rust-analyzer 插件，或任何支持 rust-analyzer 的编辑器。
- **终端**：现代终端（Linux/Mac 默认终端，Windows 推荐 Windows Terminal）。

完成 Rustlings 后，可以通过构建自己的项目、贡献到 Rustlings 或参与其他开源项目来继续练习 Rust 技能。
