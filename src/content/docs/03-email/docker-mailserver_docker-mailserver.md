---
title: docker-mailserver
---

# Docker Mailserver 项目

## 项目地址
[GitHub 项目地址](https://github.com/docker-mailserver/docker-mailserver)

## 主要特性
- **完整邮件服务器解决方案**：基于 Docker 容器，提供一个全功能的邮件服务器，支持 SMTP、IMAP、POP3 等协议，适合自托管邮件服务。
- **易于部署和管理**：使用 Docker Compose 一键部署，支持环境变量配置和 Docker 卷持久化数据，简化了传统邮件服务器的复杂安装过程。
- **安全性增强**：内置 Fail2Ban 防暴力破解、DKIM/SPF/DMARC 签名验证、TLS/SSL 支持，以及自动证书管理（兼容 Let's Encrypt）。
- **模块化设计**：包括 Postfix（SMTP）、Dovecot（IMAP/POP3）、Amavis（反病毒/反垃圾邮件）、Rspamd（高级垃圾邮件过滤）等组件，可根据需求自定义。
- **监控与日志**：集成 Watchdog 监控容器健康，支持 syslog 日志输出，便于调试和监控。
- **社区支持**：活跃的开源社区，提供详细文档、示例配置和持续更新，支持多语言和多平台（x86_64、ARM）。

## 主要功能
- **邮件收发**：处理邮件发送、接收和中继，支持虚拟用户和域名管理。
- **反垃圾与反病毒**：集成 ClamAV 病毒扫描和 SpamAssassin/Rspamd 垃圾邮件过滤，提高邮件安全性。
- **用户认证**：支持 LDAP、SASL 等外部认证，或内置用户管理。
- **Web 管理**：可选集成 Roundcube Webmail 或 Adminer 数据库管理。
- **备份与恢复**：数据持久化到 Docker 卷，支持邮件队列管理和备份。
- **扩展性**：可添加自定义脚本、环境变量调整功能，如自定义 DNS 设置或黑白名单。

## 用法
1. **前提准备**：
   - 安装 Docker 和 Docker Compose。
   - 准备域名和 DNS 记录（MX、A、TXT 等）。

2. **快速部署**：
   - 克隆仓库：`git clone https://github.com/docker-mailserver/docker-mailserver`。
   - 编辑 `docker-compose.yml` 和 `.env` 文件，配置域名、邮箱用户等（例如，`POSTFIX_MYNETWORKS` 设置允许网络）。
   - 启动容器：`docker compose up -d`。

3. **用户管理**：
   - 添加用户：`docker compose exec mailserver setup email add user@domain.com`（设置密码）。
   - 查看用户：`docker compose exec mailserver setup email list`。

4. **配置调整**：
   - 通过环境变量自定义（如 `ENABLE_FAIL2BAN=1` 启用 Fail2Ban）。
   - 生成 DKIM 密钥：`docker compose exec mailserver setup config dkim`。
   - 重启服务：`docker compose restart`。

5. **测试与维护**：
   - 测试邮件发送：使用 `mail` 命令或外部客户端（如 Thunderbird）。
   - 查看日志：`docker compose logs mailserver`。
   - 更新：拉取最新镜像并重启容器。

详细用法请参考项目文档中的 [Usage](https://docker-mailserver.github.io/docker-mailserver/latest/) 部分。