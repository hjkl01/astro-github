
---
title: msdl
---

# msdl 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/massgravel/msdl)

## 主要特性
msdl 是一个开源的 Microsoft Store 下载工具，主要用于从 Microsoft Store 下载应用包。它具有以下核心特性：
- **支持多种下载方式**：可以从 Microsoft Store 直接下载 .appx、.msix 等应用包，支持离线安装。
- **无需 Microsoft 账户**：无需登录 Microsoft 账户即可下载公开应用。
- **命令行界面**：简洁的 CLI 工具，便于脚本化和自动化使用。
- **支持代理和自定义设置**：允许配置 HTTP 代理、用户代理字符串等，以绕过网络限制。
- **批量下载**：支持通过 URL 或应用 ID 批量处理下载任务。
- **开源免费**：基于 MIT 许可，代码透明，可自由修改和分发。

## 主要功能
- **下载应用**：通过应用的产品 ID 或 Store URL 下载安装包，支持指定版本和架构（x64、ARM 等）。
- **提取和安装**：下载后可自动提取包内容，或直接用于 sideloading 安装。
- **查询应用信息**：内置功能可查询应用的元数据，如名称、版本和大小。
- **错误处理**：提供详细的日志和错误反馈，帮助诊断下载问题。
- **跨平台兼容**：主要针对 Windows，但可通过 WSL 或其他环境在 Linux 上运行。

## 用法
msdl 是一个命令行工具，首先需要从 GitHub 下载并编译（使用 Go 语言构建），或使用预编译二进制文件。基本用法如下：

### 安装
1. 安装 Go 环境（如果需要编译）。
2. 克隆仓库：`git clone https://github.com/massgravel/msdl.git`
3. 构建：`go build -o msdl.exe`

### 基本命令
- **下载应用**：
  ```
  msdl -productid 9WZDNCRFJ3Q2 下载应用（替换为实际产品 ID）
  ```
  或使用 Store URL：
  ```
  msdl https://www.microsoft.com/store/productId/9WZDNCRFJ3Q2
  ```

- **指定选项**：
  - `-arch x64`：指定架构（默认 auto）。
  - `-ver latest`：指定版本（默认最新）。
  - `-proxy http://proxy.example.com:8080`：设置代理。
  - `-ua "自定义 User-Agent"`：自定义用户代理。

- **查询应用**：
  ```
  msdl -query 9WZDNCRFJ3Q2
  ```

- **帮助**：
  ```
  msdl -h
  ```

更多高级用法请参考项目 README 文件。注意：下载的应用仅限个人使用，遵守 Microsoft 服务条款。