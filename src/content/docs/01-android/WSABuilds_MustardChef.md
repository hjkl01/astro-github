---
title: WSABuilds
---

## 项目简介

WSABuilds 是一个开源项目，由 MustardChef 开发，用于在 Windows 10 和 Windows 11 PC 上运行 Windows Subsystem for Android (WSA)。该项目提供预构建的 WSA 二进制文件，集成了 Google Play Store (MindTheGapps) 和/或 Magisk 或 KernelSU (root 解决方案)。

## 主要功能

- **预构建 WSA 镜像**：提供多种 WSA 版本的预构建镜像，支持 Windows 10 和 Windows 11。
- **Google Apps 集成**：可选集成 Google Play Store 和 Google Play Services (GMS)，允许安装和运行 Google 应用。
- **Root 解决方案**：支持 Magisk 或 KernelSU，提供 root 访问权限，用于高级定制和模块安装。
- **多架构支持**：支持 x64 和 ARM64 架构。
- **长期支持 (LTS)**：对特定 WSA 版本提供长期支持，包括 Magisk 和 KernelSU 的更新。
- **备份和恢复**：支持用户数据的备份和恢复。
- **应用兼容性**：提供详细的应用兼容性列表，包括游戏和应用的测试状态。

## 使用方法

### 系统要求

- **操作系统**：Windows 11 (Build 22000.526 或更高) 或 Windows 10 (22H2 10.0.19045.2311 或更高)。
- **处理器**：支持虚拟化的 x86_64 或 ARM64 CPU。
- **RAM**：至少 8GB (推荐 16GB)。
- **存储**：至少 10GB 可用空间，推荐使用 SSD。
- **虚拟化**：BIOS/UEFI 中启用虚拟化，并启用 Windows 虚拟机平台和 Hyper-V。

### 安装步骤

1. **下载构建**：
   - 访问 [WSABuilds Releases](https://github.com/MustardChef/WSABuilds/releases) 页面。
   - 根据您的 Windows 版本 (10 或 11) 和架构 (x64 或 ARM64) 下载相应的 .7z 文件。
   - 选择是否包含 GApps (Google Apps) 或 NoGApps 版本。

2. **提取文件**：
   - 使用 7-Zip 或类似工具提取 .7z 文件。
   - 将提取的文件夹重命名为 `WSA`。
   - 删除 .7z 文件。

3. **安装 WSA**：
   - 打开提取的 `WSA` 文件夹。
   - 双击运行 `Run.bat` 文件。
   - 如果是首次安装，可能会弹出诊断信息窗口，点击确定。
   - 安装完成后，WSA 将自动启动。

4. **更新**：
   - 要更新到新版本，下载最新构建，提取到现有 WSA 文件夹中，替换文件，然后重新运行 `Run.bat`。

### 卸载

- 搜索并卸载 "Windows Subsystem for Android Settings"。
- 删除提取的 WSA 文件夹。

### 备份和恢复

- **备份**：复制 `%LOCALAPPDATA%\Packages\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\LocalCache\userdata.vhdx` 文件。
- **恢复**：在重新安装后，将备份的 VHDX 文件复制回相同位置。

### 故障排除

- 如果安装失败，检查虚拟化设置和 Windows 功能。
- 常见问题包括路径过长、权限问题或 GPU 兼容性。
- 参考项目的 [FAQ](https://github.com/MustardChef/WSABuilds/blob/master/Documentation/WSABuilds/FAQ.md) 和 [Issues](https://github.com/MustardChef/WSABuilds/issues) 页面。

## 注意事项

- 该项目不隶属于 Microsoft 或 Google，是非官方的第三方修改。
- 使用 root 功能时请谨慎，可能影响安全性。
- 某些应用可能不兼容，建议检查兼容性列表。
- 项目遵循 AGPL-3.0 许可证。
