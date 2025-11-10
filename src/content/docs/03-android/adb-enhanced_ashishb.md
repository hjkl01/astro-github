---
title: adb-enhanced
---

# adb-enhanced 项目

## 项目地址
[https://github.com/ashishb/adb-enhanced](https://github.com/ashishb/adb-enhanced)

## 主要特性
adb-enhanced 是一个增强版的 Android Debug Bridge (ADB) 工具集，旨在简化 Android 设备开发和测试流程。它基于标准 ADB 命令扩展，提供更便捷的交互方式。主要特性包括：
- **自动化脚本支持**：内置脚本引擎，支持快速执行常见 ADB 操作，如设备连接、应用安装和日志捕获。
- **增强命令**：扩展了原生 ADB 命令，例如一键截屏、录屏、设备信息查询和性能监控。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统，无需额外配置。
- **用户友好界面**：提供命令行界面 (CLI) 和可选的 GUI 模式，便于初学者使用。
- **安全与稳定性**：集成设备授权管理，避免常见连接问题，并支持批量设备操作。

## 主要功能
- **设备管理**：自动检测连接设备，支持多设备并行操作，包括重启、卸载应用和文件传输。
- **调试工具**：实时日志查看、CPU/内存监控、应用崩溃分析。
- **媒体处理**：快速截取屏幕、录制视频，并支持直接拉取到本地。
- **高级功能**：模拟输入事件（如点击、滑动）、网络模拟和应用性能基准测试。
- **集成扩展**：可与 Android Studio 或其他 IDE 结合使用，提升开发效率。

## 用法
1. **安装**：
   - 下载最新 release 从 GitHub 项目页面。
   - 解压后，确保 ADB 已安装（项目会自动检测并使用系统 ADB）。
   - 在终端运行 `adb-enhanced --help` 检查安装。

2. **基本用法**：
   - 连接设备：`adb-enhanced connect`（自动处理 USB 调试授权）。
   - 安装 APK：`adb-enhanced install path/to/app.apk`。
   - 截屏：`adb-enhanced screenshot output.png`。
   - 查看日志：`adb-enhanced logcat | grep "error"`。
   - 多设备：使用 `--device-id` 指定设备，例如 `adb-enhanced reboot -d device123`。

3. **高级用法**：
   - 运行脚本：创建 JSON 配置文件定义操作序列，然后执行 `adb-enhanced run script.json`。
   - GUI 模式：`adb-enhanced gui` 启动图形界面，选择功能进行操作。
   - 自定义命令：编辑 `config.yaml` 文件添加个性化快捷方式。

更多详情请参考项目 README 和示例文件夹。