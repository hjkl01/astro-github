
---
title: transfer.sh
---

# transfer.sh 项目

**GitHub项目地址:** [https://github.com/dutchcoders/transfer.sh](https://github.com/dutchcoders/transfer.sh)

## 主要特性
transfer.sh 是一个开源的命令行工具和服务，用于简化文件传输。它提供了一个临时文件托管服务，支持快速上传和分享文件，而无需复杂的配置。核心特性包括：
- **临时存储**：上传的文件默认在7天后自动删除，确保隐私和存储效率。
- **简单易用**：通过命令行接口（CLI）上传文件，支持各种文件类型（如文本、图片、压缩包等）。
- **支持多种协议**：兼容 HTTPS 和其他标准协议，便于集成到脚本或自动化流程中。
- **开源免费**：基于 Go 语言开发，代码公开，用户可以自托管或使用公共实例。
- **安全性**：文件上传后生成唯一 URL，支持可选的密码保护（通过自托管实现）。
- **跨平台**：CLI 工具支持 Linux、macOS 和 Windows 等操作系统。

## 主要功能
- **文件上传**：将本地文件快速上传到服务器，并返回可分享的下载链接。
- **下载管理**：通过生成的 URL 直接下载文件，支持浏览器或命令行访问。
- **批量处理**：支持管道输入（如从 stdin 上传），适用于日志、输出等场景。
- **自托管选项**：用户可以部署自己的 transfer.sh 实例，避免依赖公共服务器。
- **集成友好**：易于与其他工具结合，如 shell 脚本、CI/CD 管道，用于自动化文件分发。

## 用法
### 安装 CLI 工具
1. **Linux/macOS**：
   ```
   curl --proto '=https' --tlsv1.2 -sSf https://get.transfer.sh | sh
   ```
   或使用 Go 安装：
   ```
   go install github.com/dutchcoders/transfer.sh@latest
   ```

2. **Windows**：下载预编译二进制文件，或使用 Go 安装。

### 基本用法
- **上传单个文件**：
  ```
  curl --upload-file ./hello.txt https://transfer.sh/hello.txt
  ```
  输出示例：`https://transfer.sh/abcdef123/hello.txt`（这是一个临时链接）。

- **使用 CLI 工具上传**：
  ```
  transfer hello.txt
  ```
  它会自动上传并返回下载 URL。

- **从 stdin 上传**（例如，上传命令输出）：
  ```
  echo "Hello World" | transfer
  ```

- **指定服务器**（如果自托管）：
  ```
  transfer -s https://your-server.com file.txt
  ```

- **下载文件**：
  使用生成的 URL 直接在浏览器中打开，或通过 curl：
  ```
  curl -O https://transfer.sh/abcdef123/hello.txt
  ```

更多高级用法和配置，请参考 GitHub 仓库的 README 文档。