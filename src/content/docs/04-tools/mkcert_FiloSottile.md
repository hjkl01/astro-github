---
title: mkcert
---

# mkcert 项目

**GitHub 项目地址:** [https://github.com/FiloSottile/mkcert](https://github.com/FiloSottile/mkcert)

## 主要特性
mkcert 是一个简单、跨平台的工具，用于生成本地证书颁发机构 (CA) 和本地 SSL/TLS 证书。它无需复杂的配置或外部依赖，主要特性包括：
- **零配置**：一键安装本地 CA，并自动信任它，避免浏览器证书警告。
- **跨平台支持**：兼容 macOS、Windows、Linux 等系统。
- **安全简单**：生成的证书仅用于本地开发环境，支持 HTTPS、HTTP/2 等协议。
- **开源免费**：由 Google 工程师 FiloSottile 维护，使用 Go 语言编写，易于构建和分发。

## 主要功能
- **生成本地 CA**：创建自签名根证书，用于本地信任。
- **颁发证书**：为特定域名（如 localhost、127.0.0.1 或自定义域名）快速生成证书和私钥。
- **自动安装**：在支持的系统上自动将 CA 添加到系统信任存储中。
- **支持 IP 和域名**：可为 IP 地址或多个域名生成证书。
- **无外部依赖**：内置所有必要功能，不需要安装 OpenSSL 或其他工具。

## 用法
### 安装
1. **macOS**：使用 Homebrew 安装 `brew install mkcert`。
2. **Windows**：从 GitHub Releases 下载二进制文件，或使用 Chocolatey `choco install mkcert`。
3. **Linux**：下载二进制文件并使其可执行，或从源代码构建（需要 Go 环境）。
4. **其他平台**：从 [GitHub Releases](https://github.com/FiloSottile/mkcert/releases) 下载对应版本。

安装后，运行 `mkcert -install` 来安装本地 CA（仅需执行一次）。

### 基本用法
- **生成证书**：`mkcert example.com` 或 `mkcert localhost 127.0.0.1 ::1`，这将生成 `example.com+2.pem`（证书）和 `example.com+2-key.pem`（私钥）。
- **查看版本**：`mkcert -version`。
- **卸载 CA**：`mkcert -uninstall`。
- **示例**：为本地开发服务器生成证书：
  ```
  mkcert localhost 127.0.0.1
  ```
  然后在服务器中使用生成的 PEM 文件配置 HTTPS。

更多细节请参考项目 README。