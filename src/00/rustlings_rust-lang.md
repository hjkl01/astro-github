# Rustlings

## 项目简介

Rustlings 是由 Rust 官方维护的一个项目，提供了一系列小练习，帮助用户熟悉阅读和编写 Rust 代码。它被推荐与阅读 [官方 Rust 书籍](https://doc.rust-lang.org/book) 并行使用。

## 主要功能

- **练习导向学习**：通过修复代码中的错误或编写代码来学习 Rust 概念。
- **自动检查**：使用 watch 模式自动检测文件变化并重新运行练习。
- **逐步指导**：练习按主题排序，每个主题有 README 文件提供资源。
- **社区支持**：提供 Q&A 讨论区和社区练习扩展。

## 安装和使用

### 安装 Rust

首先确保安装了最新版本的 Rust（包括 Cargo）。访问 [www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install) 获取安装指令。

- Linux：确保安装了 `gcc`（Debian: `sudo apt install gcc`，Fedora: `sudo dnf install gcc`）。
- MacOS：安装 Xcode 开发者工具：`xcode-select --install`。

### 安装 Rustlings

```bash
cargo install rustlings
```

如果安装失败，尝试 `rustup update` 更新 Rust，或使用 `--locked` 标志。

### 初始化

```bash
rustlings init
cd rustlings
rustlings
```

这将启动 watch 模式，引导你完成练习。

### 练习流程

- 练习位于 `exercises/<topic>` 目录。
- 修复代码中的 `TODO` 或 `todo!()` 标记。
- 运行测试以验证练习完成。
- 在 watch 模式中输入 `h` 获取提示，`l` 查看练习列表。

## 推荐环境

- **编辑器**：VS Code + rust-analyzer 插件。
- **终端**：现代终端，如 Windows Terminal。

## 更多资源

- 官方网站：[rustlings.rust-lang.org](https://rustlings.rust-lang.org)
- GitHub 仓库：[github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings)
- 社区练习：[rustlings.rust-lang.org/community-exercises/](https://rustlings.rust-lang.org/community-exercises/)
