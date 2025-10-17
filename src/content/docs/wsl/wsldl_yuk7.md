
---
title: wsldl
---

# WSLDL 项目描述

## 项目地址
[https://github.com/yuk7/wsldl](https://github.com/yuk7/wsldl)

## 主要特性
WSLDL（WSL Distribution Launcher）是一个开源工具，用于简化Windows Subsystem for Linux (WSL) 的发行版管理和启动。它的主要特性包括：
- **一键安装WSL发行版**：支持从Microsoft Store或其他来源快速下载和安装各种Linux发行版，如Ubuntu、Debian等，而无需手动操作。
- **自定义启动器**：允许用户创建自定义的WSL发行版启动器，支持参数配置、环境变量设置和快捷方式创建。
- **多发行版管理**：轻松切换和管理多个WSL发行版，支持导出/导入发行版配置。
- **集成Windows工具**：无缝集成Windows的命令提示符、PowerShell和桌面快捷方式，便于开发者使用。
- **轻量级设计**：纯脚本实现（基于PowerShell），无需额外依赖，适用于Windows 10/11系统。
- **开源免费**：MIT许可，社区维护，支持贡献和自定义扩展。

## 主要功能
- **安装与配置WSL**：自动检测并启用WSL功能，下载并安装指定Linux发行版。
- **启动与运行**：通过生成的启动器直接运行WSL发行版，支持GUI应用（如X11转发）和命令行交互。
- **备份与迁移**：导出WSL发行版为.tar文件，便于备份、迁移或分享。
- **更新管理**：检查并更新WSL内核和发行版版本。
- **故障排除**：内置诊断工具，帮助解决WSL常见问题，如网络配置或权限错误。

## 用法
1. **下载与安装**：
   - 从GitHub仓库克隆或下载发布版本（ZIP文件）。
   - 解压后运行`install.ps1`脚本（以管理员权限执行PowerShell）：
     ```
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     .\install.ps1
     ```

2. **安装WSL发行版**：
   - 运行`wsldl.exe`（或通过PowerShell调用）。
   - 在GUI界面选择发行版（如Ubuntu 20.04），点击“Install”下载并安装。
   - 命令行用法示例：
     ```
     wsldl install Ubuntu-20.04
     ```

3. **启动发行版**：
   - 使用生成的桌面快捷方式或命令：
     ```
     wsldl run Ubuntu-20.04
     ```
   - 支持参数，如`wsldl run Ubuntu-20.04 --user root`（以root用户启动）。

4. **高级用法**：
   - **导出发行版**：`wsl --export Ubuntu-20.04 backup.tar`
   - **导入发行版**：`wsl --import MyUbuntu C:\WSL\MyUbuntu backup.tar`
   - **自定义启动器**：编辑`wsldl.json`配置文件添加环境变量或启动命令。
   - 更新工具：运行`wsldl update`检查最新版本。

更多细节请参考仓库的README.md文件。确保系统已启用虚拟化（BIOS设置）和WSL功能（通过`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`）。