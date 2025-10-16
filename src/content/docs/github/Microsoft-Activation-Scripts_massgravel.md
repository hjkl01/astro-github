
---
title: Microsoft-Activation-Scripts
---

# Microsoft Activation Scripts 项目

## 项目地址
[https://github.com/massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)

## 主要特性
- **开源激活工具**：提供多种Microsoft产品激活方法，包括Windows操作系统和Office套件，支持KMS、HWID、Online KMS等多种激活模式。
- **多平台支持**：兼容Windows、Office及其他Microsoft软件的激活需求，适用于个人和企业环境。
- **自动化脚本**：基于PowerShell脚本实现一键激活，减少手动操作，提高效率。
- **安全性与合法性**：脚本使用公开的KMS服务器和官方方法激活，强调合法使用，避免盗版风险。
- **更新维护**：定期更新以兼容最新Microsoft版本，支持Windows 10/11和Office 2016-2021等。

## 主要功能
- **Windows激活**：支持HWID（硬件ID）永久激活、KMS在线/离线激活，适用于LTSC、IoT等版本。
- **Office激活**：提供Ohook、KMS等方法激活Office产品，包括 Visio、Project 等扩展组件。
- **诊断工具**：内置检查激活状态、服务器连接测试和故障排除功能。
- **自定义选项**：允许用户选择激活服务器、设置激活期限，并支持批量激活。
- **无痕运行**：脚本设计为临时运行，不修改系统文件，确保可逆性。

## 用法
1. **下载项目**：从GitHub仓库克隆或下载ZIP文件，解压到本地文件夹。
2. **运行脚本**：
   - 以管理员权限打开PowerShell。
   - 导航到脚本目录，执行 `irm https://massgrave.dev/get | iex`（在线方式）或直接运行本地MAS_AIO.cmd文件。
3. **选择模式**：
   - 运行后，选择激活类型（如Windows、Office）。
   - 挑选具体方法（e.g., HWID for permanent activation）。
   - 确认并执行，脚本会自动处理激活过程。
4. **验证**：激活完成后，使用 `slmgr /xpr` 命令检查状态，或在设置中查看激活信息。
5. **注意事项**：确保网络连接稳定，使用官方Microsoft产品；若遇问题，参考仓库的Wiki或Issues页面。建议备份系统前操作。