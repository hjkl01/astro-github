---
title: KernelSU
---

# KernelSU 项目介绍

## 项目地址
[KernelSU](https://github.com/tiann/KernelSU)

## 主要特性
KernelSU 是一个基于内核的 Android root 解决方案，类似于 Magisk，但专注于内核级修改。它通过在 Android 内核中集成一个小型的 root 管理器，实现无系统修改的 root 访问。主要特性包括：
- **内核级 root**：直接在内核中注入 root 权限，避免修改系统分区，支持 A/B 分区设备。
- **模块支持**：类似于 Magisk 的模块系统，允许用户安装和管理 root 模块，而不影响系统文件。
- **SELinux 兼容**：保持 SELinux 的 enforcing 模式，确保安全性。
- **无系统修改**：安装后无需修改 boot.img 或 recovery，支持 OTA 更新。
- **开源与免费**：基于 GPL 许可，完全开源，用户可以自定义内核。
- **多架构支持**：兼容 ARM64 等主流 Android 设备架构。
- **隐藏 root**：内置 root 隐藏功能，可绕过部分检测（如银行 app）。

## 主要功能
- **Root 管理**：提供 root 权限授予界面，允许用户选择性授权 app 的 root 访问。
- **模块安装**：支持从 GitHub 等来源下载和安装模块，实现自定义功能如 Xposed、AdBlock 等。
- **内核补丁**：自动应用内核补丁以启用 root，支持自定义内核构建。
- **设备兼容性**：适用于 Android 12+ 版本的设备，特别是 Pixel、OnePlus 等支持 GKI（Generic Kernel Image）的设备。
- **调试工具**：内置日志和调试功能，便于开发者排查问题。
- **无痕安装**：安装过程不留下痕迹，支持卸载恢复原状。

## 用法
1. **准备设备**：
   - 确保设备已解锁 bootloader（需通过 fastboot 命令）。
   - 备份重要数据。
   - 下载支持你设备的 KernelSU 预编译内核（从 GitHub Releases 页面获取）。

2. **安装 KernelSU**：
   - 将下载的 boot.img（已集成 KernelSU）通过 fastboot 刷入：`fastboot flash boot boot.img`。
   - 重启设备：`fastboot reboot`。
   - 首次启动后，安装 KernelSU Manager APK（从 GitHub 下载）。

3. **使用 KernelSU Manager**：
   - 打开 app，授予 root 权限。
   - 在“模块” tab 中浏览并安装模块，重启生效。
   - 在“超级用户” tab 中管理 app 的 root 访问权限。
   - 若需自定义，参考 GitHub 的构建指南编译自己的内核。

4. **卸载**：
   - 刷入原版 boot.img：`fastboot flash boot stock_boot.img`。
   - 删除 Manager APK，重启设备。

注意：安装 root 可能导致设备保修失效，并有安全风险。请在了解风险后操作。更多细节请参考项目 README。