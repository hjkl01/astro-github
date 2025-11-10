---
title: awesome-adb
---

# Awesome ADB 项目

## 项目地址
[GitHub 项目地址](https://github.com/mzlogin/awesome-adb)

## 主要特性
Awesome ADB 是一个开源资源集合，专注于 Android Debug Bridge (ADB) 工具的实用技巧、命令和扩展。它汇集了 ADB 在 Android 开发、调试和自动化方面的最佳实践和资源，帮助用户高效利用 ADB 进行设备管理和测试。项目以列表形式组织内容，便于快速参考和学习。

## 主要功能
- **ADB 命令参考**：提供 ADB 的核心命令列表，包括设备连接、文件传输、应用安装、日志捕获等常用操作。
- **高级技巧**：涵盖屏幕截图、录屏、模拟输入、性能监控等高级功能，支持无线 ADB 和多设备管理。
- **自动化脚本**：介绍使用 ADB 结合脚本（如 shell 或 Python）实现自动化测试和任务。
- **资源链接**：收集官方文档、教程、工具扩展（如 scrcpy、ADB over WiFi）和社区贡献的实用示例。
- **兼容性支持**：适用于 Android 设备调试、逆向工程和开发环境搭建，兼容多种操作系统（Windows、macOS、Linux）。

## 用法
1. **克隆仓库**：使用 Git 命令 `git clone https://github.com/mzlogin/awesome-adb.git` 下载项目。
2. **浏览内容**：打开 README.md 文件，查看分类列表（如基础命令、高级用法）。
3. **应用命令**：安装 ADB 工具后，直接在终端运行示例命令，例如：
   - 列出设备：`adb devices`
   - 安装 APK：`adb install app.apk`
   - 推送文件：`adb push file.txt /sdcard/`
4. **扩展使用**：根据资源链接，探索无线调试（`adb tcpip 5555`）或集成到 IDE（如 Android Studio）中进行开发调试。
5. **贡献**：用户可 fork 项目，添加新资源或命令，并提交 pull request 以完善集合。