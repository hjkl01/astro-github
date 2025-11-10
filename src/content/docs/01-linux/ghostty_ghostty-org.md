---
title: ghostty
---

# Ghostty 项目介绍

**项目地址**: [https://github.com/ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)

## 主要特性
- **现代化终端模拟器**：专为高性能和跨平台优化设计。
- **GPU 加速渲染**：利用硬件加速提供更流畅的输出和更低的延迟。
- **多平台支持**：支持 macOS、Linux，并计划提供 Windows 版本。
- **高度可配置**：通过配置文件定制界面、主题、快捷键和行为。
- **分屏与标签页**：在同一窗口中方便切换和管理多个会话。
- **符合终端标准**：兼容常见终端协议和应用。
- **快速启动速度**：优化启动流程，减少延迟。

## 功能简介
- **主题与配色方案**：支持自定义配色，包括透明度与背景纹理。
- **字体与字形渲染**：可选择多种字体，支持 ligatures 及高 DPI 显示。
- **输入法与剪贴板支持**：方便在终端中输入多语言文字及复制粘贴。
- **终端行为控制**：控制光标样式、滚动历史记录长度等。
- **插件与扩展**：通过脚本及扩展机制增强功能。

## 用法示例
1. **安装**
   ```bash
   git clone https://github.com/ghostty-org/ghostty.git
   cd ghostty
   # 根据系统进行编译安装
   make install
   ```

2. **运行**
   ```bash
   ghostty
   ```

3. **配置**
   编辑配置文件（如 `~/.config/ghostty/config`）：
   ```conf
   font=JetBrains Mono
   theme=dracula
   enable_gpu=true
   ```
