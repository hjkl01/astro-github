---
title: vhs
---

# Charmbracelet VHS 项目

## 项目地址
[https://github.com/charmbracelet/vhs](https://github.com/charmbracelet/vhs)

## 主要特性
- **终端录制工具**：VHS 是一个专为终端设计的录制工具，能够捕获终端会话并生成高质量的视频文件，支持多种输出格式。
- **高保真输出**：支持录制终端的精确视觉效果，包括颜色、字体和动画，确保录制的视频与实际终端显示一致。
- **轻量级与高效**：基于 Go 语言开发，轻量级且高效，适合开发者在命令行环境中快速录制教程、演示或调试过程。
- **跨平台支持**：兼容 macOS、Linux 和 Windows 系统，便于在不同环境中使用。
- **自定义选项**：提供丰富的配置选项，如帧率调整、主题支持和水印添加，增强录制灵活性。

## 主要功能
- **会话录制**：实时捕获终端输入输出，包括命令执行过程和交互界面。
- **视频导出**：将录制内容导出为 MP4、GIF 等常见视频格式，便于分享或嵌入文档。
- **帧率与分辨率控制**：允许用户自定义录制帧率和分辨率，以优化文件大小和质量。
- **暂停/恢复**：支持在录制过程中暂停和恢复操作，适合长时间会话。
- **集成脚本**：可与 shell 脚本结合，实现自动化录制流程。

## 用法
1. **安装**：
   - 通过 Go 安装：`go install github.com/charmbracelet/vhs@latest`
   - 或从 GitHub Releases 下载预编译二进制文件。

2. **基本录制**：
   - 启动录制：`vhs record output.mp4`
   - 在终端中执行命令或交互。
   - 按 Ctrl+C 停止录制，自动生成视频文件。

3. **高级选项**：
   - 指定帧率：`vhs record -fps 30 output.mp4`
   - 添加主题：`vhs record -theme dark output.mp4`
   - 录制 GIF：`vhs record -format gif output.gif`

更多详细用法请参考项目 README 文档。