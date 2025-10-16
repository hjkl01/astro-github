
---
title: rclone
---

# Rclone 项目

## 项目地址
[https://github.com/rclone/rclone](https://github.com/rclone/rclone)

## 主要特性
Rclone 是一个开源的命令行工具，用于管理和同步文件到各种云存储提供商。它支持超过 70 种云存储服务，包括 Google Drive、Amazon S3、Dropbox、OneDrive 等。核心特性包括：
- **高效同步**：支持增量同步，仅传输文件变更部分，节省带宽和时间。
- **加密支持**：内置文件加密和解密功能，使用 AES-256 加密保护数据隐私。
- **多线程传输**：通过并行上传/下载加速大文件传输。
- **挂载功能**：可以将云存储挂载为本地文件系统，像本地驱动器一样访问。
- **跨平台兼容**：支持 Linux、Windows、macOS 和 FreeBSD 等操作系统。
- **过滤和排除**：允许通过规则过滤文件，支持正则表达式和路径排除。
- **校验和验证**：自动校验文件完整性，确保传输无误。

## 主要功能
- **复制和同步文件**：从本地或云端复制文件，支持单向同步（source 到 dest）或双向镜像。
- **列出和浏览**：浏览云存储目录，列出文件列表。
- **删除和移动**：安全删除或移动文件，支持回收站模拟。
- **服务器模式**：作为 Web GUI 或 REST API 服务器运行，提供图形化界面。
- **缓存和优化**：内置缓存机制优化性能，支持 VFS（虚拟文件系统）挂载。
- **授权管理**：通过 OAuth 等方式处理云存储认证，支持服务账户。

## 用法
Rclone 通过命令行操作，首先需安装并配置远程存储。基本用法如下：

### 安装
- 下载二进制文件：从 GitHub Releases 下载适合系统的版本。
- Linux 示例：`curl https://rclone.org/install.sh | sudo bash`
- Windows：下载 .exe 文件并添加到 PATH。

### 配置
运行 `rclone config` 交互式配置远程存储：
```
rclone config
```
- 选择存储类型（如 "drive" for Google Drive）。
- 输入认证信息（如 API 密钥）。
- 配置完成后，远程名为 "remote"（可自定义）。

### 基本命令示例
- **同步本地到云端**：`rclone sync /local/path remote:/cloud/path`
- **复制文件**：`rclone copy /local/file.txt remote:/cloud/dir/`
- **列出文件**：`rclone ls remote:/path`
- **挂载云存储**：`rclone mount remote:/path /local/mountpoint`
- **加密传输**：先配置加密远程 `rclone config`，然后使用加密路径如 `rclone sync local: encrypted-remote:/path`
- **查看帮助**：`rclone --help` 或 `rclone command --help`（如 `rclone sync --help`）。

更多细节参考官方文档：https://rclone.org/docs/。使用时注意权限和配额限制。