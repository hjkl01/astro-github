---
title: postal
---

# Postal 项目

## 项目地址
[https://github.com/postalserver/postal](https://github.com/postalserver/postal)

## 主要特性
Postal 是一个完整的开源邮件服务器解决方案，旨在为开发者提供易于部署和管理的邮件服务。它支持高性能的邮件处理、自动配置和可扩展性。主要特性包括：
- **多租户支持**：允许在单一实例中管理多个邮件域和组织。
- **API 驱动**：提供 RESTful API，用于程序化管理邮件服务器、用户和邮件路由。
- **高可用性**：支持集群部署、负载均衡和故障转移，确保邮件服务的可靠性和扩展性。
- **集成性强**：兼容 SMTP、IMAP 和 POP3 协议，便于与其他邮件客户端和系统集成。
- **监控与日志**：内置详细的日志记录、监控工具和 Web 界面，用于实时跟踪邮件流量和性能。
- **安全性**：支持 SPF、DKIM、DMARC 等邮件认证机制，以及 TLS 加密传输。
- **开源免费**：基于 Ruby on Rails 开发，使用 PostgreSQL 和 Redis 等现代技术栈，完全开源。

## 主要功能
- **邮件发送与接收**：处理传入和传出邮件，支持大规模邮件发送（如营销邮件）。
- **用户管理**：通过 Web 界面或 API 创建和管理邮件用户、别名和域。
- **路由与过滤**：自定义邮件路由规则、垃圾邮件过滤和黑白名单。
- **Webmail 支持**：可选集成 Web 邮件客户端，提供用户自助访问。
- **自动化配置**：自动生成 DNS 记录和证书配置，简化部署过程。
- **扩展插件**：支持自定义插件，用于添加特定功能如 webhook 集成。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/postalserver/postal.git`
   - 安装依赖：使用 Bundler 安装 Ruby  gems，并设置 PostgreSQL 和 Redis。
   - 配置环境：编辑 `config/postal.yml` 文件，设置数据库、主机和 SMTP 设置。
   - 运行初始化：`bundle exec rake postal:install` 生成默认配置。

2. **部署**：
   - 使用 Docker 或直接在服务器上运行：支持 Ubuntu/Debian 等 Linux 系统。
   - 设置 Nginx 或 Apache 作为反向代理。
   - 配置 DNS：为你的域添加 MX、SPF 和 DKIM 记录。

3. **基本操作**：
   - 启动服务器：`bundle exec rails server`。
   - 通过 Web 界面（默认端口 5000）访问：创建组织、添加域和用户。
   - 使用 API：发送邮件示例（使用 curl）：
     ```
     curl -X POST https://your-server.com/api/v1/messages \
     -H "Postal-Token: your-api-token" \
     -F "from=example@domain.com" \
     -F "to=recipient@example.com" \
     -F "subject=Test" \
     -F "html=Hello World"
     ```
   - 管理邮件：通过 API 或界面监控队列、发送报告和处理退信。

更多细节请参考仓库的 [文档](https://github.com/postalserver/postal/wiki)。