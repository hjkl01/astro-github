---
title: Ventoy
---

# Ventoy 项目

## 项目地址
[https://github.com/ventoy/Ventoy](https://github.com/ventoy/Ventoy)

## 主要特性
Ventoy 是一个开源的多系统启动工具，支持 Windows、Linux、macOS 等操作系统。它无需反复格式化 U 盘，只需一次安装 Ventoy，即可轻松管理多个 ISO 文件。核心特性包括：
- **无需格式化 U 盘**：安装后，U 盘分区保持不变，直接复制 ISO 文件即可启动。
- **支持多种格式**：兼容 ISO、WIM、IMG、VHD(x)、EFI 等文件格式。
- **跨平台兼容**：支持 UEFI 和 Legacy BIOS 模式，适用于 x86 和 ARM 架构。
- **插件系统**：内置插件支持，如主题自定义、文件注入、密码保护等。
- **安全与稳定性**：开源项目，代码透明，支持 Secure Boot，无需额外驱动。

## 主要功能
- **多 ISO 启动**：将多个 ISO 文件复制到 Ventoy U 盘，即可从菜单中选择启动，支持 Windows、Linux、VMware、Chromium OS 等上百种系统。
- **持久化模式**：可选启用数据持久化功能，安装系统后数据不会丢失。
- **树状菜单**：ISO 文件可按文件夹组织，支持多级目录浏览。
- **USB 直通**：在虚拟机环境中可直通 U 盘启动。
- **ARM 支持**：适用于 Raspberry Pi 等 ARM 设备。

## 用法
1. **下载与安装**：
   - 从 GitHub 发布页下载最新 Ventoy 版本（有 Windows、Linux 安装程序）。
   - 插入 U 盘，运行 Ventoy2Disk.exe（Windows）或 ventoy2disk.sh（Linux），选择 U 盘并点击“Install”安装。安装过程会创建两个分区：一个 exFAT 分区用于存放 ISO 文件。

2. **准备 ISO 文件**：
   - 将 ISO 文件直接复制到 U 盘的 exFAT 分区（无需解压）。

3. **启动系统**：
   - 重启电脑，进入 BIOS 设置将 U 盘设为第一启动项。
   - 启动后进入 Ventoy 菜单，选择所需的 ISO 文件启动即可。
   - 支持热插拔：启动后可随时插入/移除 U 盘。

注意：安装前备份 U 盘数据，确保 U 盘容量至少 8GB。更多详情请参考项目 Wiki。