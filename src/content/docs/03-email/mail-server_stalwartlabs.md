---
title: mail-server
---

# Stalwart Mail Server 项目

## 项目地址
[GitHub 项目地址](https://github.com/stalwartlabs/mail-server)

## 主要特性
Stalwart Mail Server 是一个开源的全功能邮件服务器，采用 Rust 语言开发，强调安全性、可扩展性和高性能。其核心特性包括：
- **多协议支持**：兼容 SMTP、IMAP、POP3、ManageSieve 等标准邮件协议，支持 TLS/SSL 加密。
- **内置 Web 管理界面**：提供直观的 Web UI 用于配置和管理服务器，无需命令行操作。
- **现代架构**：使用事件驱动的异步框架（如 Tokio），支持高并发处理和低资源消耗。
- **数据存储灵活**：支持多种后端存储，如 RocksDB、SQLite、PostgreSQL、MySQL 等，便于集成现有系统。
- **安全增强**：内置反垃圾邮件（SpamAssassin 集成）、反病毒扫描、DKIM/SPF/DMARC 支持，以及细粒度访问控制（ACL）。
- **可扩展性**：模块化设计，支持插件扩展和 Webhooks，用于自定义工作流。
- **跨平台**：可在 Linux、macOS 和 Windows 上运行，支持 Docker 部署。

## 主要功能
- **邮件路由与投递**：智能路由规则，支持虚拟域、别名和重定向；自动处理退信和队列管理。
- **用户管理**：支持 LDAP/Active Directory 集成、多租户环境，以及基于角色的权限控制。
- **搜索与索引**：内置全文搜索功能，使用 Tantivy 引擎，实现快速邮件检索。
- **备份与恢复**：自动快照和导出工具，确保数据完整性。
- **监控与日志**：详细的审计日志、Prometheus 指标集成，便于监控服务器健康状态。
- **移动友好**：优化了 IMAP 支持，与主流邮件客户端（如 Outlook、Thunderbird）无缝兼容。

## 用法
### 安装
1. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/stalwartlabs/mail-server.git`
   - 安装 Rust：通过 rustup 安装。
   - 构建：`cargo build --release`
   - 配置：编辑 `config.toml` 文件，设置域名、存储路径等。

2. **Docker 部署**（推荐）：
   - 拉取镜像：`docker pull stalwartlabs/mail-server:latest`
   - 运行：`docker run -d -p 25:25 -p 143:143 -p 993:993 -v /path/to/config:/opt/stalwart-mail-server/etc stalwartlabs/mail-server`
   - 访问 Web UI：通过 `https://your-server:8080` 配置。

### 配置与运行
- **基本配置**：在 `config.toml` 中定义服务器主机名、TLS 证书路径、数据库连接等。
- **启动服务器**：运行 `./target/release/stalwart-mail-server` 或使用 systemd 服务。
- **添加域与用户**：通过 Web UI 或 CLI 工具（如 `stalwart-cli`）创建虚拟域和用户账户。
- **测试**：使用工具如 `swaks` 发送测试邮件，验证 SMTP/IMAP 连接。
- **高级用法**：集成外部服务（如 PostgreSQL 用于存储），启用 Webhooks 处理事件；参考官方文档进行自定义脚本开发。

更多细节请参考项目 README 和文档。