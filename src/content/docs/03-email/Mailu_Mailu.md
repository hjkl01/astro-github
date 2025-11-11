---
title: Mailu
---

# Mailu 项目

## 项目地址

[https://github.com/Mailu/Mailu](https://github.com/Mailu/Mailu)

## 主要特性

Mailu 是一个开源的电子邮件服务器解决方案，基于 Docker 容器化技术设计，旨在提供简单、安全且易于管理的邮件服务。它支持完整的邮件服务器功能，包括 SMTP、IMAP 和 POP3 协议，适用于个人或小型团队使用。主要特性包括：

- **容器化部署**：使用 Docker Compose 快速搭建和运行，避免复杂的手动配置。
- **安全优先**：内置反垃圾邮件（SpamAssassin）、反病毒（ClamAV）功能，支持 DKIM、DMARC 和 SPF 验证，防范邮件滥用。
- **用户友好**：提供 Web 管理界面（Admin），允许管理员轻松管理用户、域名和别名。
- **模块化设计**：核心组件包括 Postfix（SMTP）、Dovecot（IMAP/POP3）、Roundcube（Webmail）等，支持扩展插件。
- **多域名支持**：可处理多个域名和虚拟用户，无需为每个域名单独配置服务器。
- **自动更新**：支持一键更新 Docker 镜像，保持系统安全和最新。
- **高级邮件功能**：支持别名、域名别名、自定义路由、全文搜索邮件附件。
- **Web 访问**：多个 Webmail 和管理界面。
- **用户功能**：别名、自动回复、自动转发、获取账户、managesieve。
- **管理员功能**：全局管理员、公告、按域委托、配额。
- **自由**：所有 FOSS 组件，无跟踪器。

## 主要功能

- **邮件发送与接收**：通过 SMTP 服务器可靠发送邮件，支持 TLS/SSL 加密；IMAP/POP3 允许客户端（如 Outlook、Thunderbird）访问收件箱。
- **Web 邮件客户端**：集成 Roundcube，提供浏览器访问邮件的功能，无需额外安装。
- **管理员工具**：Web 界面管理用户账户、设置别名、监控日志和配置反垃圾规则。
- **备份与恢复**：内置工具支持邮件数据备份，易于迁移或恢复。
- **集成服务**：可选集成 Fail2Ban（入侵防护）、Redis（缓存）和 LetsEncrypt（免费 SSL 证书）。

## 用法

1. **环境准备**：确保系统安装 Docker 和 Docker Compose（推荐 Linux 主机，如 Ubuntu）。克隆仓库：`git clone https://github.com/Mailu/Mailu.git`。
2. **配置**：编辑 `mailu.env` 和 `docker-compose.yml` 文件，设置域名、密码等参数。生成初始配置：运行 `./setup` 脚本。
3. **启动服务**：在项目目录执行 `docker-compose up -d`，服务将在端口 25（SMTP）、993（IMAP）、995（POP3）和 80/443（Web）上运行。
4. **访问界面**：通过浏览器访问 `https://your-domain/admin` 登录管理员面板（默认凭证在配置中设置），添加域名和用户。
5. **客户端配置**：在邮件客户端中设置服务器地址（your-domain）、端口和认证信息。
6. **维护**：定期运行 `docker-compose pull && docker-compose up -d` 更新；使用 `docker-compose logs` 查看日志。详细文档见仓库的 `doc/` 目录。
