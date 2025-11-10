---
title: winget-cli
---

# Microsoft Winget CLI

**GitHub项目地址:** [https://github.com/microsoft/winget-cli](https://github.com/microsoft/winget-cli)

## 主要特性
Winget CLI 是 Microsoft 开发的 Windows 包管理器工具，具有以下核心特性：
- **跨平台支持**：专为 Windows 10（版本 1809 或更高）和 Windows 11 设计，支持命令行操作。
- **开源与社区驱动**：基于 MIT 许可开源，允许社区贡献软件包和改进工具。
- **安全与可靠**：通过 Microsoft Store 分发，确保软件来源可靠；支持数字签名验证，减少恶意软件风险。
- **轻量级集成**：无需额外安装，直接通过 Microsoft Store 或 GitHub Releases 获取，支持系统级集成。
- **多源支持**：默认使用 Microsoft 的 Winget 源，但可添加自定义源以扩展软件仓库。

## 主要功能
Winget CLI 提供丰富的包管理功能，类似于 Linux 的 apt 或 macOS 的 Homebrew，主要包括：
- **搜索与发现**：搜索软件包、查看详细信息和可用版本。
- **安装与卸载**：从仓库安装软件，支持静默安装和自定义参数；轻松卸载已安装应用。
- **升级与管理**：检查并升级已安装软件，列出所有已安装包。
- **源管理**：添加、移除或切换软件源，支持 YAML 配置。
- **导出与导入**：导出已安装软件列表为 JSON 文件，便于在多机迁移。
- **哈希验证**：验证下载包的完整性，确保安全。
- **高级选项**：支持代理设置、日志记录和架构指定（x64、ARM 等）。

## 用法
Winget CLI 通过命令行使用，基本语法为 `winget <命令> [选项]`。以下是常见用法示例（在 PowerShell 或命令提示符中运行）：

### 安装 Winget
- 通过 Microsoft Store 搜索 "App Installer" 并安装（包含 Winget）。
- 或从 GitHub Releases 下载最新 .msixbundle 文件安装。

### 基本命令示例
- **搜索软件**：  
  `winget search <软件名>`  
  示例：`winget search vscode`（搜索 Visual Studio Code）。

- **安装软件**：  
  `winget install <包ID>`  
  示例：`winget install Microsoft.VisualStudioCode`（安装 VS Code，支持 `--silent` 静默模式）。

- **卸载软件**：  
  `winget uninstall <包ID>`  
  示例：`winget uninstall Microsoft.VisualStudioCode`。

- **升级软件**：  
  `winget upgrade`（列出所有可升级包）；  
  `winget upgrade <包ID>`（升级指定包）。

- **列出已安装**：  
  `winget list`（显示所有已安装应用）。

- **添加源**：  
  `winget source add --name <源名> --arg <URL>`  
  示例：添加自定义源。

更多详细用法，请参考项目文档或运行 `winget --help` 查看帮助。Winget 适用于 IT 管理员、开发者及日常用户简化软件管理。