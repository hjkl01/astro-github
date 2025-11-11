---
title: WingetUI
---

# UniGetUI 项目

## 项目地址

[GitHub 项目地址](https://github.com/marticliment/UniGetUI)

## 主要特性

UniGetUI (formerly WingetUI) 是一个开源的图形用户界面（GUI）工具，为 Windows 10 和 11 上最常见的 CLI 包管理器设计，如 WinGet、Scoop、Chocolatey、Pip、Npm、.NET Tool、PowerShell Gallery 等。它允许用户轻松下载、安装、更新和卸载任何发布在支持的包管理器上的软件。主要特性包括：

- **多包管理器支持**：整合 WinGet、Scoop、Chocolatey、Pip、Npm 等包管理器。
- **用户友好界面**：直观的 GUI，支持一键安装、更新和卸载，无需命令行。
- **批量操作**：选择多个包同时执行安装、更新或卸载。
- **包发现与过滤**：搜索和过滤包，查看详细元数据。
- **自动更新**：自动更新包，或通知可用更新，支持跳过版本。
- **自定义安装**：为每个包选择不同安装选项，保存设置。
- **导出/导入**：导出包列表到文件，导入到另一台机器。
- **开源与多语言**：支持多种语言，包括中文。

## 主要功能

- **安装软件**：搜索并安装支持的包管理器中的软件。
- **更新软件**：扫描并更新已安装软件，支持批量。
- **卸载软件**：移除已安装的软件。
- **包管理**：导出导入包列表，备份设置。
- **通知与小部件**：系统托盘显示更新，集成 Dev Home 小部件。
- **日志与调试**：详细日志，便于排查问题。
- **主题支持**：浅色/深色模式。

## 用法

1. **安装**：
   - Microsoft Store：搜索 UniGetUI。
   - WinGet：`winget install --exact --id MartiCliment.UniGetUI --source winget`
   - Scoop：`scoop bucket add extras; scoop install extras/unigetui`
   - Chocolatey：`choco install wingetui`
   - 或下载安装程序从 Releases。

2. **启动应用**：
   - 运行 UniGetUI，可能需要管理员权限。

3. **基本操作**：
   - **发现包**：搜索包，查看详情，安装。
   - **更新**：检查更新，批量更新。
   - **已安装**：管理已安装包，卸载或更新。
   - **设置**：配置包管理器、更新检查等。

4. **注意事项**：
   - 支持的包管理器需单独安装（如 WinGet 默认在 Win10/11）。
   - 包来自第三方，使用风险自负。
   - 如遇问题，检查 Wiki 或 Issues。

此工具适合需要管理多个包管理器的用户，提升软件管理效率。
