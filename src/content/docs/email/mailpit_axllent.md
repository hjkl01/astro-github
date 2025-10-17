
---
title: mailpit
---

# Mailpit 项目

**GitHub 项目地址:** [https://github.com/axllent/mailpit](https://github.com/axllent/mailpit)

## 主要特性
Mailpit 是一个现代化的电子邮件测试服务器和Web 界面工具，专为开发者和测试人员设计。它模拟 SMTP 服务器，用于捕获和查看应用程序发送的电子邮件，而无需实际发送到真实收件人。主要特性包括：
- **轻量级 SMTP 服务器**：支持 SMTP 协议（端口 1025），可以拦截和存储所有传入的电子邮件。
- **Web 界面**：内置 Web UI（默认端口 8025），提供直观的邮件查看、搜索和调试功能，支持实时预览 HTML、纯文本和附件。
- **内存存储**：电子邮件默认存储在内存中，支持持久化到 SQLite 数据库（可选），便于开发环境快速重置。
- **API 支持**：提供 RESTful API 接口，用于程序化访问和自动化测试。
- **跨平台兼容**：支持 Linux、macOS 和 Windows，易于部署和集成到 CI/CD 管道。
- **安全性与配置**：支持自定义域名、认证选项，以及 Docker 容器化部署，适合生产级开发测试。

## 主要功能
- **邮件捕获与显示**：捕获所有发送的邮件，并以线程形式展示，支持过滤、搜索和导出。
- **附件处理**：自动解析和下载邮件附件，包括图像和文件。
- **调试工具**：实时查看邮件头、源代码和渲染效果，帮助诊断邮件格式问题。
- **集成友好**：可与流行框架（如 Rails、Django、Laravel）无缝集成，用于单元测试和端到端测试。
- **监控与日志**：内置日志记录和性能监控，确保开发过程中的邮件测试高效可靠。

## 用法
### 快速启动
1. **下载与安装**：从 GitHub Releases 下载二进制文件，或使用 Docker：
   ```
   docker run -p 1025:1025 -p 8025:8025 axllent/mailpit
   ```
   这将启动 SMTP 服务器（端口 1025）和 Web UI（端口 8025）。

2. **配置应用程序**：在你的应用中将 SMTP 设置指向 Mailpit：
   - 主机：localhost（或容器 IP）
   - 端口：1025
   - 无需认证（默认）。

3. **访问 Web 界面**：打开浏览器访问 `http://localhost:8025`，即可查看捕获的邮件。

### 高级用法
- **持久化存储**：运行时添加标志 `-storage sqlite3` 以使用 SQLite 数据库保存邮件。
- **自定义配置**：使用命令行参数如 `-smtp bind=:1025` 修改端口，或 `-web bind=:8025` 调整 Web 界面。
- **API 示例**：通过 `GET /api/v1/message` 获取邮件列表，支持 JSON 响应。
- **Docker Compose 示例**：
  ```
  version: '3'
  services:
    mailpit:
      image: axllent/mailpit
      ports:
        - "1025:1025"
        - "8025:8025"
      volumes:
        - ./data:/data  # 用于持久化
  ```
  运行 `docker-compose up` 启动。

更多细节请参考项目 README。