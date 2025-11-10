---
title: mailcow-dockerized
---

# mailcow: dockerized

**GitHub项目地址:** [https://github.com/mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized)

## 主要特性
mailcow: dockerized 是一个基于 Docker 的开源邮件服务器套件，集成了多个开源组件，提供完整的邮件服务解决方案。其主要特性包括：
- **全面的邮件功能**：支持 SMTP、IMAP、POP3 协议，提供邮件发送、接收、存储和检索。
- **Web 界面管理**：内置 SoGo 或 Roundcube 等 Webmail 客户端，以及管理员仪表板，便于用户和管理员管理邮箱、域名、别名和过滤规则。
- **安全性增强**：集成 SpamAssassin 防垃圾邮件、ClamAV 病毒扫描、DKIM/DMARC/SPF 支持，以及 TLS/SSL 加密，确保邮件传输安全。
- **自动化管理**：支持自动配置、备份和恢复，易于扩展和管理多个域名和用户。
- **开源与模块化**：使用 Docker 容器化部署，易于安装、更新和维护，支持自定义配置。
- **其他特性**：包括 ActiveSync 支持（移动设备同步）、LDAP 集成、邮件归档和监控工具。

## 功能
- **邮件服务器核心**：Postfix（SMTP）、Dovecot（IMAP/POP3）和 Fetchmail（邮件拉取）。
- **反垃圾与安全**：Rspamd（高级垃圾过滤）、Fail2Ban（入侵防护）和 Let's Encrypt（自动 SSL 证书）。
- **用户管理**：支持无限域名、邮箱别名、共享邮箱和配额管理。
- **集成工具**：Web 界面用于用户自助服务，API 支持自动化操作。
- **监控与日志**：内置日志查看器和性能监控，兼容 Prometheus 等工具。

## 用法
1. **系统要求**：需要 Docker 和 Docker Compose（推荐 Ubuntu/Debian 系统，至少 2GB RAM）。
2. **安装步骤**：
   - 克隆仓库：`git clone https://github.com/mailcow/mailcow-dockerized.git`
   - 进入目录：`cd mailcow-dockerized`
   - 生成配置：`./generate_config.sh`
   - 编辑 `mailcow.conf` 文件（设置主机名、时区等）。
   - 启动服务：`docker-compose pull && docker-compose up -d`
3. **访问界面**：通过浏览器访问 `https://your-mail-server/admin`（管理员面板）和 `https://your-mail-server`（Webmail）。
4. **管理与维护**：
   - 添加域名/用户：在管理员面板中配置。
   - 更新：`./update.sh`
   - 备份：使用内置工具或 Docker 卷备份。
   - 停止/重启：`docker-compose down` 或 `docker-compose restart`。
更多详情请参考仓库的 [文档](https://docs.mailcow.email)。