
---
title: certbot
---

# Certbot 项目

**GitHub 项目地址:** [https://github.com/certbot/certbot](https://github.com/certbot/certbot)

## 主要特性
Certbot 是 Let's Encrypt 官方推荐的免费、自动化且开源的证书颁发机构 (CA) 客户端工具。它具有以下主要特性：
- **自动化证书管理**：自动获取、安装和续期 SSL/TLS 证书，支持零配置部署。
- **免费证书**：通过 Let's Encrypt 提供免费的 90 天有效期证书，无需支付费用。
- **安全增强**：支持 HTTP-01 和 DNS-01 验证方式，确保证书安全颁发。
- **多平台兼容**：适用于 Linux、macOS 和 Windows，支持多种 Web 服务器如 Apache、Nginx 和其他自定义服务器。
- **开源与社区支持**：基于 Python 开发，MIT 许可，活跃的社区维护和更新。
- **插件扩展**：内置插件系统，可扩展到更多服务器和环境。

## 主要功能
Certbot 的核心功能围绕 SSL/TLS 证书的生命周期管理：
- **证书获取**：从 Let's Encrypt 获取新证书，支持域名验证和自动安装到 Web 服务器。
- **证书续期**：自动处理证书续期，通常每 60 天检查一次，确保证书不过期。
- **服务器集成**：与 Apache 和 Nginx 无缝集成，能自动修改配置文件以启用 HTTPS。
- **独立模式**：在不修改服务器配置的情况下运行，作为独立服务器处理 HTTPS 流量。
- **测试模式**：提供 staging 环境测试，避免真实证书配额限制。
- **钩子支持**：允许在证书事件（如安装、续期）前后运行自定义脚本，实现自动化工作流。
- **撤销与管理**：支持证书撤销、列出已安装证书和手动管理。

## 用法
Certbot 的安装和使用简单，通常通过命令行操作。以下是基本用法指南（假设已安装 Certbot）：

### 1. 安装 Certbot
- **Ubuntu/Debian**：`sudo apt update && sudo apt install certbot`
- **CentOS/RHEL**：`sudo yum install certbot` 或使用 Snap：`sudo snap install --classic certbot`
- **macOS**：使用 Homebrew：`brew install certbot`
- **其他平台**：参考官方文档或 Snap 包安装：`sudo snap install --classic certbot`

### 2. 获取和安装证书
- **对于 Apache**：`sudo certbot --apache -d example.com -d www.example.com`
  - 这会自动配置 Apache 并获取证书。
- **对于 Nginx**：`sudo certbot --nginx -d example.com -d www.example.com`
  - 自动修改 Nginx 配置启用 HTTPS。
- **独立模式**（无服务器集成）：`sudo certbot certonly --standalone -d example.com`
  - Certbot 作为临时服务器处理验证。

### 3. 证书续期
- 测试续期：`sudo certbot renew --dry-run`
- 自动续期：设置 cron 任务，例如 `sudo crontab -e` 添加 `0 12 * * * /usr/bin/certbot renew --quiet`
- Certbot 默认安装时会添加自动续期钩子。

### 4. 其他常用命令
- **列出证书**：`sudo certbot certificates`
- **删除证书**：`sudo certbot delete --cert-name example.com`
- **使用 DNS 验证**（适用于通配符证书）：`sudo certbot certonly --manual --preferred-challenges dns -d *.example.com`
- **详细帮助**：`certbot --help` 或 `certbot <plugin> --help`（如 `--apache --help`）

更多高级用法和故障排除，请参考官方文档：https://certbot.eff.org/docs/。Certbot 要求域名指向服务器的公网 IP，并开放 80/443 端口。