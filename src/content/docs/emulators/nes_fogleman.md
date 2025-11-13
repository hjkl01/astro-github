---
title: nes
---

# NES 项目

## 项目地址

[https://github.com/fogleman/nes](https://github.com/fogleman/nes)

## 概述

这是一个用 Go 语言编写的 NES（Nintendo Entertainment System）模拟器。它允许在现代计算机上运行经典的 NES 游戏。

## 主要特性

- **纯 Go 实现**：使用 Go 语言编写，无需外部依赖。
- **跨平台支持**：支持 Windows、macOS 和 Linux。
- **音频支持**：集成音频播放，使用 PortAudio。
- **图形渲染**：使用 OpenGL 和 GLFW 进行图形渲染。
- **游戏库管理**：支持从目录或单个文件加载游戏，并提供菜单界面。

## 功能

- **游戏加载**：支持从目录或指定文件加载 NES ROM。
- **菜单界面**：自动生成游戏封面和菜单。
- **控制器支持**：支持键盘和游戏手柄输入。
- **保存状态**：支持游戏进度保存和加载。
- **调试功能**：提供基本的调试信息。

## 用法

1. **安装依赖**：
   - 安装 Go 语言环境。
   - 安装 PortAudio（用于音频）。

2. **克隆和构建**：

   ```bash
   go get github.com/fogleman/nes
   ```

3. **运行**：
   - 从目录运行：`nes /path/to/roms/`
   - 运行特定游戏：`nes /path/to/game.nes`

4. **控制**：
   - 方向键：移动
   - Z：A 按钮
   - X：B 按钮
   - Enter：开始
   - 右 Shift：选择
   - R：重置

## 贡献

欢迎提交 Issue 和 Pull Request 以改进模拟器。

---
