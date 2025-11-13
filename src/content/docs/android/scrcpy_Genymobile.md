---
title: scrcpy
---

# Scrcpy 项目

**GitHub 项目地址:** [https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)

## 主要特性
Scrcpy 是一个开源工具，用于通过 USB 或 TCP/IP 将 Android 设备屏幕镜像到计算机上，并支持设备控制。主要特性包括：
- **高性能镜像**：使用硬件加速，提供低延迟的屏幕显示，支持高达 1920x1080 分辨率和 60 FPS。
- **无根要求**：无需 root 权限即可运行，支持 Android 5.0 及以上版本。
- **无线和有线连接**：支持 USB 连接和无线 ADB（TCP/IP）连接。
- **音频支持**：从 Android 11 开始，支持设备音频转发到计算机。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 系统。
- **轻量级**：客户端体积小，仅需设备端安装 ADB 服务器，无需在设备上安装额外应用。
- **录制功能**：可录制屏幕视频或保存音频。
- **自定义控制**：支持键盘和鼠标控制设备，支持游戏手柄和多显示器。

## 主要功能
- **屏幕镜像**：实时显示 Android 设备屏幕到计算机窗口。
- **设备控制**：通过计算机的键盘、鼠标或触摸模拟控制设备，包括点击、滑动、输入文本等。
- **文件传输**：支持从计算机向设备推送文件。
- **剪贴板同步**：设备和计算机间剪贴板内容同步。
- **视频录制**：记录镜像屏幕为 MP4 文件，支持指定分辨率和比特率。
- **音频转发**：将设备音频输出到计算机扬声器。
- **多实例支持**：同时连接多个设备。

## 用法
### 安装
1. **前提条件**：安装 ADB（Android Debug Bridge），通常通过 Android SDK Platform-Tools 获取。确保设备启用 USB 调试（设置 > 关于手机 > 多次点击版本号 > 开发者选项 > USB 调试）。
2. **下载 Scrcpy**：从 GitHub Releases 页面下载对应平台的预编译二进制文件，或通过包管理器安装（如 Homebrew on macOS: `brew install scrcpy`）。
3. **Linux 用户**：可能需安装依赖，如 SDL2 和 FFmpeg。

### 基本用法
1. **USB 连接**：
   - 连接设备到计算机。
   - 运行命令：`scrcpy`（默认启动镜像和控制）。

2. **无线连接**：
   - 先通过 USB 启用 TCP/IP：`adb tcpip 5555`。
   - 断开 USB，运行：`adb connect <设备IP>:5555`。
   - 然后：`scrcpy -s <设备IP>:5555`。

3. **常用选项**：
   - `--record=file.mp4`：录制视频。
   - `--audio-codec=opus`：启用音频（Android 11+）。
   - `--max-size=1024`：限制最大分辨率。
   - `--bit-rate=2M`：设置比特率。
   - `--turn-screen-off`：关闭设备屏幕以节省电量。
   - `-s <serial>`：指定设备序列号（多设备时）。

4. **高级用法**：
   - 推送文件：`scrcpy --push file.txt /sdcard/`。
   - 查看帮助：`scrcpy --help`。

详细文档和故障排除请参考 GitHub 仓库的 README。