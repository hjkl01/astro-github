
---
title: iRedMail
---

# iRedMail 项目

## 项目地址
[https://github.com/iredmail/iRedMail](https://github.com/iredmail/iRedMail)

## 主要特性
iRedMail 是一个开源的邮件服务器解决方案，旨在为用户提供一个简单、高效的邮件系统部署工具。它支持多种流行的邮件服务器组件，包括 Postfix（SMTP）、Dovecot（IMAP/POP3）、SpamAssassin（反垃圾邮件）和 ClamAV（病毒扫描）。主要特性包括：
- **易于安装**：一键式安装脚本，支持多种 Linux 和 BSD 操作系统（如 Ubuntu、CentOS、Debian 等），无需手动配置复杂组件。
- **安全性高**：内置 SSL/TLS 支持、DKIM 签名、DMARC 验证，以及防火墙集成，确保邮件传输安全。
- **模块化设计**：支持多种后端存储，如 MySQL、PostgreSQL 或 OpenLDAP，用于用户管理和邮件存储。
- **Web 管理界面**：集成 Roundcube 或 iRedAdmin，提供用户友好的 Webmail 和管理员面板，便于管理用户、域名和别名。
- **反垃圾和病毒防护**：集成 Amavisd-new、SpamAssassin 和 ClamAV，提供强大的过滤机制。
- **开源免费**：基于 GPL 许可，用户可以自由修改和扩展。

## 主要功能
- **邮件发送与接收**：支持 SMTP/IMAP/POP3 协议，实现完整的邮件服务，包括多域名管理和用户认证。
- **用户管理**：通过 Web 界面或命令行添加/删除用户、设置配额和权限。
- **备份与恢复**：内置工具支持邮件数据备份和灾难恢复。
- **扩展支持**：兼容 Sieve 过滤规则、CalDAV/CardDAV（日历和联系人同步），以及与第三方工具的集成。
- **监控与日志**：提供详细的日志记录和性能监控，便于故障排查。

## 用法
1. **系统要求**：确保服务器运行支持的 Linux/BSD 发行版，具有 root 权限和足够的磁盘空间（至少 5GB）。
2. **下载与安装**：
   - 从 GitHub 克隆仓库：`git clone https://github.com/iredmail/iRedMail.git`
   - 进入目录：`cd iRedMail`
   - 运行安装脚本：`bash iRedMail.sh`（脚本会引导你选择组件、后端数据库等配置）。
3. **配置**：
   - 安装过程中，设置主机名、域名、数据库密码等。
   - 安装完成后，通过 Web 界面（默认 https://your-server/iredadmin）登录管理员面板（用户名：postmaster@your-domain，密码在安装时设置）。
4. **管理与使用**：
   - 用户通过 Webmail（如 Roundcube）登录收发邮件：https://your-server/mail。
   - 添加域名和用户：在 iRedAdmin 面板中操作。
   - 更新系统：定期运行 `iRedMail.tips` 获取更新提示，或手动升级组件。
5. **故障排除**：查看 `/var/log/` 中的日志文件，或参考官方文档（https://docs.iredmail.org/）。

更多详情请参考项目 README 和官方文档。