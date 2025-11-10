---
title: crocodile
---

# Crocodile 项目

**GitHub 项目地址:** [https://github.com/labulakalia/crocodile](https://github.com/labulakalia/crocodile)

## 主要特性
Crocodile 是一个开源的命令行工具，专注于简化文件传输和安全数据交换。其核心特性包括：
- **安全传输**：使用端到端加密，支持 TLS 和自定义密钥，确保数据在传输过程中不被窃取。
- **跨平台支持**：兼容 Windows、macOS 和 Linux 系统，便于多环境使用。
- **简单易用**：无需复杂配置，通过命令行快速启动传输服务，支持 P2P 模式减少服务器依赖。
- **轻量级**：体积小巧，资源占用低，适合开发者和系统管理员日常使用。
- **自定义选项**：支持端口指定、密码保护和传输日志记录，提供灵活的配置。

## 主要功能
- **文件/目录传输**：允许用户安全地将文件或整个目录从一台设备传输到另一台，支持大文件分块传输以提高效率。
- **临时服务器模式**：快速创建一个临时的 HTTP/HTTPS 服务器，用于分享文件链接。
- **集成加密**：内置 AES 加密算法，用户可设置密码保护传输会话。
- **进度监控**：实时显示传输进度、速度和剩余时间。
- **错误处理**：自动重试机制和详细错误日志，帮助诊断传输问题。

## 用法
1. **安装**：
   - 通过 GitHub 仓库克隆项目：`git clone https://github.com/labulakalia/crocodile.git`
   - 进入目录并构建（假设使用 Go 语言）：`go build -o crocodile`
   - 或使用预编译二进制文件直接下载安装。

2. **基本用法**：
   - **启动服务器传输文件**：`./crocodile serve --port 8080 --password yourpass`
     - 这将启动一个本地服务器，用户可以通过生成的 URL 上传/下载文件。
   - **直接传输文件**：`./crocodile send /path/to/file --target host:port --password yourpass`
     - 指定目标主机和端口进行点对点传输。
   - **接收文件**：`./crocodile receive --port 8080 --password yourpass`
     - 监听指定端口，接收传入的文件。

3. **高级选项**：
   - `--dir`：传输整个目录。
   - `--log-level debug`：启用详细日志。
   - 示例：`./crocodile send --dir /myfolder --target 192.168.1.100:8080`

更多详细信息请参考项目 README 文件。