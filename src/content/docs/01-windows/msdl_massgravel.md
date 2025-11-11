---
title: Microsoft Activation Scripts
---

# Microsoft Activation Scripts (MAS) 项目

## 项目地址

[GitHub 项目地址](https://github.com/massgravel/Microsoft-Activation-Scripts)

## 主要特性

Microsoft Activation Scripts (MAS) 是一个开源的 Windows 和 Office 激活器，采用 HWID、Ohook、TSforge、KMS38 和在线 KMS 激活方法，并提供高级故障排除功能。主要特性包括：

- **多种激活方法**：支持 HWID、KMS38、在线 KMS 等激活方式，适用于不同场景。
- **Windows 和 Office 支持**：可激活 Windows 10/11 和 Office 2016-2021 等版本。
- **开源透明**：代码公开，便于审查和修改。
- **高级故障排除**：内置诊断工具，帮助解决激活问题。
- **免费无广告**：完全免费，无恶意软件。

## 主要功能

- **激活 Windows**：使用 HWID、KMS38 或在线 KMS 永久激活 Windows。
- **激活 Office**：支持 Office 2016-2021 的激活，包括零售和批量许可证。
- **扩展更新 (ESU)**：激活 Windows 7/8.1/Server 2012 R2 的扩展安全更新。
- **故障排除**：检查激活状态、修复常见问题、生成日志。
- **跨平台兼容**：主要针对 Windows，支持 PowerShell 脚本。

## 用法

MAS 提供 PowerShell 脚本激活，无需下载文件。基本用法如下：

### 方法 1 - PowerShell（推荐）

1. 打开 PowerShell。
2. 复制并运行以下命令：
   ```
   irm https://get.activated.win | iex
   ```
   或国内服务器：
   ```
   iex ((New-Object Net.WebClient).DownloadString('https://get.activated.win'))
   ```
3. 选择激活选项，绿色高亮为推荐。

### 方法 2 - 传统方式

1. 下载 MAS_AIO.cmd 从 Releases。
2. 运行脚本，选择激活选项。

注意：使用风险自负，确保来源可靠。更多细节请参考项目 README。
