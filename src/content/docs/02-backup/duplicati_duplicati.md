---
title: duplicati
---

# Duplicati 项目

**GitHub 项目地址:** [https://github.com/duplicati/duplicati](https://github.com/duplicati/duplicati)

## 主要特性
Duplicati 是一个免费开源的备份软件，支持加密、增量备份和去重功能。它采用零知识加密，确保备份数据在传输和存储过程中高度安全。主要特性包括：
- **加密备份**：使用 AES-256 加密，所有备份数据在本地加密后上传，避免云存储提供商访问明文。
- **增量备份**：仅备份文件变更部分，支持版本控制和恢复特定时间点的文件。
- **去重和压缩**：自动检测重复数据块，减少存储空间占用，并压缩备份文件以优化传输。
- **跨平台支持**：兼容 Windows、macOS 和 Linux，支持命令行和图形界面。
- **多种存储后端**：集成云服务如 Google Drive、OneDrive、Dropbox、Amazon S3，以及本地磁盘、FTP 等。
- **自动化调度**：内置任务调度器，支持定时备份和自动清理旧版本。
- **开源与免费**：基于 GPL 许可，用户可自由修改和分发。

## 主要功能
Duplicati 的核心功能聚焦于可靠的数据备份和恢复：
- **备份创建**：选择源文件夹或文件，配置目标存储位置，进行完整或增量备份。
- **数据恢复**：从备份中恢复单个文件、文件夹或整个数据集，支持时间点恢复。
- **备份管理**：监控备份进度、错误日志，并设置保留策略（如保留最近 N 个版本）。
- **安全传输**：使用 HTTPS 或 SFTP 等协议，确保数据在网络中安全传输。
- **移动设备支持**：通过 Web 界面或 API 实现远程管理，适用于 NAS 或服务器环境。
- **高级选项**：支持排除文件模式、带宽限制、并行上传，以及 WebDAV 和 SSH 存储。

## 用法指南
Duplicati 的使用简单直观，支持图形界面（GUI）和命令行（CLI）。以下是基本用法步骤：

### 1. 安装
- 从 GitHub 下载最新版本（Windows/macOS 安装包或源代码）。
- 对于 Linux，使用包管理器如 `apt install duplicati` 或从源代码编译。
- 启动后，默认访问 Web 界面：http://localhost:8200。

### 2. 配置备份任务（GUI）
- 打开 Duplicati，点击“添加备份” > “配置新备份”。
- **源数据**：选择要备份的文件夹或文件，支持过滤器排除临时文件等。
- **目标存储**：选择存储类型（如 Google Drive），输入凭证和路径。
- **加密和设置**：设置密码（推荐强密码），启用加密；配置保留策略（如保留 30 天内每天备份）。
- **调度**：设置备份频率（如每天凌晨），并测试连接。
- 点击“运行现在”开始首次完整备份。

### 3. 恢复数据
- 在 Web 界面，选择备份任务 > “恢复”。
- 浏览备份版本，选择文件或文件夹。
- 指定恢复位置（原位置或新位置），点击“恢复”执行。

### 4. 命令行用法（CLI）
- 使用 `Duplicati.CommandLine.exe`（Windows）或 `duplicati-cli`（Linux）。
- 示例：备份命令  
  ```
  Duplicati.CommandLine.Backup.exe "C:\MyFiles" "s3://mybucket/backups" --passphrase="yourpassword" --dblock-size=100mb
  ```
- 恢复命令  
  ```
  Duplicati.CommandLine.Restore.exe "s3://mybucket/backups" --passphrase="yourpassword" --restore-path="C:\Restore"
  ```
- 更多选项参考官方文档：运行 `Duplicati.CommandLine.Backup.exe help`。

### 注意事项
- 首次备份可能耗时较长，后续增量备份更快。
- 定期检查备份完整性（内置验证功能）。
- 对于大型数据集，建议分批备份以避免超时。
- 详细文档和社区支持可在 GitHub Wiki 中找到。