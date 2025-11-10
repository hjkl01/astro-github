---
title: Gopher64
---

# gopher64

## 功能

gopher64 是一个高度兼容的 Nintendo 64 (N64) 模拟器，使用 Rust 编写。它提供了以下主要功能：

- **高度兼容性**：支持运行 N64 游戏 ROM 文件
- **Netplay 支持**：通过云托管服务器或自建服务器实现在线多人游戏
- **Portable 模式**：创建 `portable.txt` 文件以将所有游戏数据保存在可执行文件同一目录
- **跨平台支持**：提供 Windows 和 Linux 版本
- **图形和音频模拟**：基于 parallel-rdp 和其他组件实现高质量的图形和音频渲染

## 用法

### 下载和安装

- **Windows**：从 [GitHub Releases](https://github.com/gopher64/gopher64/releases/latest/download/gopher64-windows-x86_64.exe) 下载可执行文件
- **Linux**：通过 [Flathub](https://flathub.org/apps/io.github.gopher64.gopher64) 安装 Flatpak 版本

### 运行游戏

1. 下载 N64 ROM 文件（.z64 格式）
2. 运行模拟器：`./gopher64 /path/to/rom.z64`
3. 对于 Flatpak 版本，使用：`flatpak run --filesystem=host:ro io.github.gopher64.gopher64 /path/to/rom.z64`

### 控制设置

- **键盘控制**：参考 [默认键盘设置](https://github.com/gopher64/gopher64/wiki/Default-Keyboard-Setup)
- **游戏手柄**：参考 [默认游戏手柄设置](https://github.com/gopher64/gopher64/wiki/Default-Gamepad-Setup)

### Netplay

gopher64 支持通过服务器进行在线多人游戏：

- 使用云托管服务器
- 或在 LAN 上自建服务器（参考 [gopher64-netplay-server](https://github.com/gopher64/gopher64-netplay-server)）

### 构建从源码

1. 安装 SDL3 依赖（Linux）：参考 [SDL3 Linux 构建依赖](https://wiki.libsdl.org/SDL3/README-linux#build-dependencies)
2. 安装 Rust：参考 [Rust 安装指南](https://www.rust-lang.org/tools/install)
3. 克隆仓库：`git clone --recursive https://github.com/gopher64/gopher64.git`
4. 进入目录：`cd gopher64`
5. 构建：`cargo build --release`
6. 运行：`./target/release/gopher64 /path/to/rom.z64`

## 许可证

gopher64 基于 GPLv3 许可证发布。部分代码改编自 mupen64plus 和 ares 项目。

## 社区

- **Wiki**：[GitHub Wiki](https://github.com/gopher64/gopher64/wiki)
- **Discord**：[Discord 服务器](https://discord.gg/9RGXq8W8JQ)
