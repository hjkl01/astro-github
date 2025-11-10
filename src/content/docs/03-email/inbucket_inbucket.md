---
title: inbucket
---

# Inbucket 项目

**项目地址：** [https://github.com/inbucket/inbucket](https://github.com/inbucket/inbucket)

## 主要特性
Inbucket 是一个开源的临时电子邮件服务项目，设计用于测试和开发环境。它模拟了一个邮件服务器，能够接收和存储电子邮件，而无需实际发送或存储在真实邮件系统中。主要特性包括：
- **临时邮箱支持**：为测试目的提供临时邮箱地址，邮件在指定时间内自动过期。
- **Web 界面**：内置 Web UI，允许用户通过浏览器查看、搜索和删除收到的邮件。
- **SMTP 服务器**：实现完整的 SMTP 协议，支持接收来自任何客户端的邮件。
- **POP3 支持**：可选的 POP3 服务器，用于从客户端拉取邮件。
- **内存存储**：默认使用内存存储邮件数据，重启后数据丢失（可配置持久化）。
- **轻量级和易部署**：Go 语言编写，单二进制文件，支持 Docker 部署，便于集成到 CI/CD 管道。
- **自定义配置**：支持 YAML 配置，包括域名、过期时间、存储路径等。
- **安全性**：默认监听本地端口，适合开发环境；可配置 TLS 支持。

## 主要功能
- **接收邮件**：监听 SMTP 端口（默认 2500），接收任意发件人发送到 Inbucket 域名的邮件（如 user@inbucket.local）。
- **查看和管理邮件**：通过 Web 界面（默认端口 9000）浏览收件箱、阅读邮件内容（包括附件）、搜索邮件。
- **自动清理**：邮件和收件箱可设置过期时间（如 24 小时），自动删除以节省资源。
- **测试集成**：常用于自动化测试、API 验证等场景，模拟用户注册确认邮件等流程。
- **监控和日志**：提供详细日志输出，支持监控邮件流量。

## 用法
### 安装与运行
1. **下载二进制文件**：从 GitHub Releases 下载适合平台的二进制文件（如 inbucket.exe for Windows）。
2. **使用 Docker（推荐）**：
   ```
   docker run -p 9000:9000 -p 2500:2500 inbucket/inbucket:latest
   ```
   这将启动 Web UI（http://localhost:9000）和 SMTP 服务器（端口 2500）。

3. **直接运行**：
   ```
   ./inbucket
   ```
   默认配置下，访问 http://localhost:9000 查看界面。

### 配置
创建 `inbucket.yml` 文件自定义设置，例如：
```yaml
inbucket:
  defaultMailboxExpiration: 24h  # 收件箱过期时间
  defaultMessageExpiration: 24h  # 邮件过期时间
smtp:
  hostname: inbucket.local  # 域名
http:
  listen: 0.0.0.0:9000  # Web 端口
```
运行时指定配置：`./inbucket -config=inbucket.yml`。

### 使用示例
1. 启动服务后，在 Web 界面生成临时邮箱（如 test@example.com）。
2. 从外部应用或工具发送邮件到该地址（SMTP 服务器需指向 localhost:2500）。
3. 在 Web 界面刷新收件箱，查看收到的邮件内容、头部和附件。
4. 用于测试：集成到 Selenium 或 Postman 中验证邮件发送功能。

更多细节请参考项目 README。