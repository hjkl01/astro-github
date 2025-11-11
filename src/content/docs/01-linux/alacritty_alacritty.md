---
title: alacritty
---

# Alacritty 项目

## 项目地址

[GitHub 项目地址](https://github.com/alacritty/alacritty)

## 主要特性

- **跨平台终端模拟器**：支持 BSD、Linux、macOS 和 Windows，使用 OpenGL 渲染。
- **高性能**：GPU 加速，快速响应和流畅的文本渲染。
- **可配置性**：通过 TOML 配置文件自定义外观、行为和快捷键。
- **现代功能**：支持 Unicode、TrueType 字体、滚动缓冲区和搜索。
- **轻量级**：无依赖复杂图形界面，专注于终端模拟。

## 主要功能

- **文本渲染**：高质量的 GPU 加速文本显示，支持多种字体和颜色。
- **快捷键绑定**：可自定义键盘快捷键，用于复制、粘贴、搜索等操作。
- **滚动和搜索**：无限滚动缓冲区，支持正则表达式搜索历史。
- **多显示器支持**：在多屏幕环境中无缝工作。
- **Vi 模式**：内置 Vi 风格的编辑模式，便于导航和编辑命令。
- **Hints**：终端 hints 允许在不启动 vi 模式的情况下轻松与可见文本交互。
- **Selection expansion**：在进行选择后，可以使用右键鼠标扩展选择。
- **Opening URLs with the mouse**：可以使用鼠标单击打开 URL。
- **Multi-Window**：Alacritty 支持从同一实例运行多个终端模拟器。

## Requirements

- At least OpenGL ES 2.0
- [Windows] ConPTY support (Windows 10 version 1809 or higher)

## 用法

1. **安装**：
   - 从 [GitHub Releases](https://github.com/alacritty/alacritty/releases) 下载预编译二进制文件。
   - 或使用包管理器：`sudo apt install alacritty`（Ubuntu/Debian），`brew install alacritty`（macOS）。

2. **启动**：
   - 在终端输入 `alacritty` 启动。
   - 或从应用菜单启动。

3. **配置**：
   - 配置文件位于 `~/.config/alacritty/alacritty.toml`。
   - 示例配置：

     ```toml
     [font]
     size = 12.0

     [colors]
     primary = { background = "#000000", foreground = "#ffffff" }
     ```

4. **快捷键**：
   - `Ctrl+Shift+C`：复制
   - `Ctrl+Shift+V`：粘贴
   - `Ctrl+Shift+Space`：进入搜索模式

更多细节请参考 GitHub 仓库的 README 文件和 [官方文档](https://alacritty.org/)。
