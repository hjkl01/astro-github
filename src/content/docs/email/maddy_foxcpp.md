---
title: maddy
---

# maddy 项目概述

## 项目地址

[https://github.com/foxcpp/maddy](https://github.com/foxcpp/maddy)

## 主要特性

maddy 是一个用 Go 语言编写的自托管 SMTP 服务器，旨在提供简单、高性能的电子邮件服务解决方案。它支持完整的 SMTP 协议栈，包括 MTA（邮件传输代理）和 MDA（邮件投递代理）功能。主要特性包括：

- **模块化设计**：允许用户自定义邮件处理管道，支持插件式扩展。
- **高性能**：基于 Go 的并发模型，实现高效的邮件处理和队列管理。
- **安全支持**：集成 TLS/SSL 加密、DKIM 签名、SPF/DMARC 检查，以及反垃圾邮件过滤。
- **数据库集成**：支持 SQLite、PostgreSQL 和 MySQL 等后端，用于用户认证和邮件存储。
- **Web 管理界面**：提供可选的 Web UI 用于配置和管理。
- **兼容性强**：符合 RFC 标准，支持 IMAP 和 POP3 代理（通过外部集成）。注意：IMAP 存储是 "beta" 版本，如果需要稳定且功能丰富的实现，建议使用 Dovecot。

## 主要功能

maddy 的核心功能聚焦于电子邮件服务器的完整生命周期管理：

- **邮件接收与发送**：处理 SMTP 入站/出站邮件，支持虚拟域和用户别名。
- **认证与授权**：内置 SASL 认证，支持 LDAP、OAuth 等外部认证源。
- **邮件存储**：将邮件存储在 Maildir 格式或数据库中，便于与 Dovecot 等 IMAP 服务器集成。
- **队列管理**：自动重试失败的邮件投递，并提供监控工具。
- **日志与监控**：详细的日志记录，支持 Prometheus 指标导出，用于性能监控。
- **反滥用机制**：内置速率限制、灰名单和内容过滤，防范垃圾邮件和 DDoS 攻击。

## 用法

### 安装

1. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/foxcpp/maddy.git`
   - 进入目录：`cd maddy`
   - 构建：`go build`

2. **使用预编译二进制**：
   - 从 GitHub Releases 下载适用于你的平台的二进制文件。
   - 解压并放置到系统路径中。

### 配置与运行

1. **基本配置**：
   - 创建配置文件 `maddy.conf`（TOML 格式），示例：

     ```
     hostname example.com
     domain example.com

     [smtp.tcp.in]
     listen :25
     ```

   - 配置用户认证、TLS 证书等细节。

2. **运行服务器**：
   - 命令行启动：`./maddy -config maddy.conf`
   - 使用 systemd 服务：安装后启用并启动服务。

3. **高级用法**：
   - **添加域**：在配置中定义虚拟域和用户映射。
   - **集成 IMAP**：配置 maddy 与 Dovecot 配合，提供完整邮件服务。
   - **测试**：使用 `swaks` 或 `telnet` 测试 SMTP 连接。
   - **监控**：访问 `/metrics` 端点查看 Prometheus 数据。

更多细节请参考项目文档：https://maddy.email/reference/configuration/
