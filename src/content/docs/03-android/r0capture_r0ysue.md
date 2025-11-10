---
title: r0capture
---

# r0capture 项目

**GitHub 项目地址:** [https://github.com/r0ysue/r0capture](https://github.com/r0ysue/r0capture)

## 主要特性
r0capture 是一个基于 Android 的屏幕捕获和录制工具，专为 root 设备设计。它利用系统底层 API 实现高效的屏幕截图和视频录制，支持多种分辨率和帧率选项。主要特性包括：
- **无水印捕获**：直接从系统表面（Surface）捕获屏幕内容，避免应用层水印或干扰。
- **高性能录制**：支持硬件加速编码，适用于游戏录制、调试和自动化测试。
- **Root 权限优化**：通过 root 访问 MediaProjection 服务，实现更稳定的捕获。
- **自定义参数**：可调整分辨率、比特率、帧率等参数，以适应不同设备和场景。
- **跨设备兼容**：针对 Android 5.0+ 版本优化，支持 ARM 和 x86 架构。

## 主要功能
- **屏幕截图**：实时捕获当前屏幕图像，支持 PNG/JPG 输出。
- **屏幕录制**：录制屏幕视频，支持 H.264 编码，输出 MP4 文件。
- **音频捕获**：可选集成系统音频录制（需额外权限）。
- **自动化脚本支持**：可集成到 ADB 或自动化框架中，用于 UI 测试或逆向工程。
- **日志与调试**：内置日志输出，便于排查捕获问题。

## 用法
### 安装与准备
1. 确保设备已 root，并安装 BusyBox。
2. 从 GitHub 下载 APK 或源代码，编译安装（使用 Android Studio）。
3. 通过 ADB 推送文件：`adb push r0capture /data/local/tmp/`。

### 基本用法
- **启动服务**：运行 APK 或通过 ADB 执行 `./r0capture start`（需在 root shell 中）。
- **截图**：使用命令 `r0capture screenshot /sdcard/screenshot.png` 捕获当前屏幕。
- **录制视频**：`r0capture record -d 10 -o /sdcard/video.mp4`（-d 指定时长秒数，-o 输出路径）。
- **高级选项**：
  - 指定分辨率：`-w 1920 -h 1080`。
  - 设置帧率：`-fps 30`。
  - 比特率：`-bitrate 5000`（单位 kbps）。
- **停止录制**：`r0capture stop` 或 Ctrl+C。
- **示例脚本**：在 shell 中结合 ADB 使用，如 `adb shell su -c '/data/local/tmp/r0capture record -d 60'`。

详细文档请参考项目 README。注意：使用需遵守设备权限和法律规定，仅限合法用途。