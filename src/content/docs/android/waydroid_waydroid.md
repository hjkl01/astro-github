---
title: waydroid
---

# Waydroid 项目

## 项目地址
[https://github.com/waydroid/waydroid](https://github.com/waydroid/waydroid)

## 主要特性
Waydroid 是一个基于 Linux 的容器化 Android 环境工具，它允许用户在 Linux 桌面系统（如 Ubuntu、Fedora 等）上运行完整的 Android 系统。主要特性包括：
- **容器化运行**：使用 LXC（Linux Containers）技术隔离 Android 环境，与主机系统无缝集成，而非虚拟机模拟。
- **原生性能**：提供接近原生的 Android 体验，支持硬件加速和 GPU 渲染，适合游戏和应用运行。
- **开源免费**：基于 AOSP（Android Open Source Project），支持自定义 ROM 和模块扩展。
- **桌面集成**：Android 应用可以作为独立窗口在 Linux 桌面运行，支持 Wayland 和 X11 显示协议。
- **多架构支持**：兼容 x86_64 和 ARM64 架构，便于在不同硬件上部署。

## 主要功能
- **运行 Android 应用**：安装并运行 APK 文件，支持 Google Play 服务（需手动配置）。
- **完整 Android 系统**：提供模拟器般的完整 Android OS，包括设置、通知和多任务管理。
- **会话管理**：支持全屏模式或窗口化模式，允许在主机上切换 Android 会话。
- **自定义配置**：可调整分辨率、内存分配和输入设备，支持触摸屏和键盘/鼠标输入。
- **兼容性扩展**：集成 Weston 合成器，实现平滑的图形渲染和多窗口支持。

## 用法
1. **安装依赖**：确保系统支持 LXC 和 binder（Android IPC 机制）。在 Ubuntu 上运行：
   ```
   sudo apt update
   sudo apt install curl ca-certificates
   ```
   添加 Waydroid 仓库并安装：
   ```
   curl https://repo.waydro.id/waydroid.gpg | sudo apt-key add -
   echo "deb https://repo.waydro.id/ focal main" | sudo tee /etc/apt/sources.list.d/waydroid.list
   sudo apt update
   sudo apt install waydroid
   ```

2. **初始化**：下载并初始化 Android 镜像（推荐使用 Vanilla 或 GApps 版本）：
   ```
   sudo waydroid init
   ```
   对于带 Google 服务的版本：
   ```
   sudo waydroid init -s GAPPS
   ```

3. **启动**：运行 Waydroid 会话：
   ```
   waydroid show-full-ui  # 全屏模式
   ```
   或启动特定应用：
   ```
   waydroid app launch com.example.app
   ```

4. **安装应用**：使用 ADB 工具安装 APK：
   ```
   waydroid app install /path/to/app.apk
   ```

5. **停止和卸载**：停止会话：
   ```
   waydroid session stop
   ```
   完全卸载：
   ```
   sudo waydroid container stop
   sudo waydroid uninstall
   ```

详细文档请参考项目 README 和 Wiki。注意：需 root 权限，且在某些发行版上可能需额外内核模块。