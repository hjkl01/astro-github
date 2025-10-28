
---
title: core
---

# Dovecot Core 项目

## 项目地址
[https://github.com/dovecot/core](https://github.com/dovecot/core)

## 主要特性
Dovecot Core 是开源邮件服务器 Dovecot 的核心组件，主要用于处理 IMAP 和 POP3 协议。它以高性能、安全性和可靠性著称，支持多种认证机制、插件扩展和虚拟用户管理。核心特性包括：
- **高性能**：支持数百万用户并发访问，高效的邮件索引和缓存机制。
- **安全性**：内置 SSL/TLS 支持、SASL 认证、邮件加密和权限控制，防范常见邮件服务器漏洞。
- **模块化设计**：易于扩展，通过插件支持 LDAP、SQL 等后端存储。
- **跨平台兼容**：支持 Linux、BSD 和其他 Unix-like 系统。
- **邮件协议支持**：完整实现 IMAP4rev1、POP3、ManageSieve 等协议。

## 主要功能
- **邮件存储管理**：支持 Maildir、mbox 等格式，提供邮件分箱、搜索和 quota 控制。
- **用户认证**：集成 PAM、LDAP、数据库等认证方式，支持虚拟域和用户。
- **协议处理**：处理 IMAP/POP3 客户端连接，实现邮件同步、推送通知（IMAP IDLE）。
- **插件系统**：内置插件如 ACL（访问控制列表）、Quota（配额管理）和 Pigeonhole（Sieve 脚本过滤）。
- **日志和监控**：详细的日志记录、统计信息和集成监控工具。
- **高可用性**：支持邮件复制、故障转移和负载均衡。

## 用法
1. **安装**：
   - 在 Linux 系统上，使用包管理器安装，例如 Ubuntu/Debian：`sudo apt install dovecot-core`。
   - 或从源码编译：克隆仓库 `git clone https://github.com/dovecot/core.git`，然后运行 `./autogen.sh && ./configure && make && sudo make install`。

2. **配置**：
   - 主配置文件位于 `/etc/dovecot/dovecot.conf`。
   - 编辑协议设置（如 `protocols = imap pop3`）、认证（`auth_mechanisms = plain login`）和邮件位置（`mail_location = maildir:~/Maildir`）。
   - 示例配置邮件存储：添加 `mailbox Drafts { special_use = \Drafts }` 以支持标准文件夹。

3. **启动和运行**：
   - 启动服务：`sudo systemctl start dovecot`。
   - 测试连接：使用 telnet 或邮件客户端（如 Thunderbird）连接 IMAP 端口 143（明文）或 993（SSL）。
   - 管理：使用 `doveadm` 命令行工具进行用户管理、邮件备份等，例如 `doveadm user username` 查看用户信息。

4. **扩展**：
   - 安装插件：如 `dovecot-sieve` 用于邮件过滤。
   - 集成后端：配置 SQL（如 MySQL）存储用户数据，通过 `passdb` 和 `userdb` 指令。

更多细节参考官方文档：https://doc.dovecot.org/。