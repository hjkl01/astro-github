---
title: lapce
---

# Lapce

## 简介

Lapce 是一个用纯 Rust 编写的闪电般快速且强大的代码编辑器。它的 UI 基于 [Floem](https://github.com/lapce/floem)，设计灵感来源于 [Xi-Editor](https://github.com/xi-editor/xi-editor) 的 Rope Science 技术，实现超快计算，并使用 [wgpu](https://github.com/gfx-rs/wgpu) 进行渲染。

## 功能特性

- **内置 LSP 支持**：提供智能代码功能，如自动补全、诊断和代码操作。
- **模态编辑**：原生支持 Vim-like 模态编辑，可切换。
- **远程开发**：内置远程开发支持，类似于 VSCode Remote Development，提供本地体验的同时利用远程系统的全部功能。
- **插件系统**：支持使用可编译为 WASI 格式的编程语言（如 C、Rust、AssemblyScript）编写插件。
- **内置终端**：无需离开编辑器即可在工作区执行命令。

## 安装

你可以从 [GitHub Releases](https://github.com/lapce/lapce/releases) 下载适用于 Windows、Linux 和 macOS 的预构建版本，或使用包管理器安装。详细安装指南请参考 [官方文档](https://docs.lapce.dev/)。

### 从源码编译

如果需要从源码编译，请参考 [构建指南](https://github.com/lapce/lapce/blob/master/docs/building-from-source.md)。

## 使用方法

1. **启动 Lapce**：下载并安装后，运行 Lapce。
2. **打开项目**：使用文件菜单或命令打开文件夹作为工作区。
3. **编辑代码**：享受快速的代码编辑体验，支持 LSP 提供的智能功能。
4. **模态编辑**：如果启用 Vim 模式，使用 `i` 进入插入模式，`Esc` 返回正常模式。
5. **远程开发**：配置远程环境以在远程系统上开发。
6. **插件**：从插件市场安装插件以扩展功能。
7. **终端**：使用内置终端执行命令。

更多详细用法请参考 [Lapce 文档](https://docs.lapce.dev/)。

## 贡献

Lapce 是开源项目，欢迎贡献。贡献指南请见 [CONTRIBUTING.md](https://github.com/lapce/lapce/blob/master/CONTRIBUTING.md)。

## 反馈与联系

- Discord: [https://discord.gg/n8tGJ6Rn6D](https://discord.gg/n8tGJ6Rn6D)
- Reddit: [https://www.reddit.com/r/lapce/](https://www.reddit.com/r/lapce/)
- Matrix: [https://matrix.to/#/#lapce-editor:matrix.org](https://matrix.to/#/#lapce-editor:matrix.org)

## 许可证

Lapce 基于 Apache License Version 2.0 许可证开源。
