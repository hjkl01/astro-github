---
title: Warpgate
---

## 功能介绍

Warpgate 是一个智能且完全透明的 SSH、HTTPS、MySQL 和 PostgreSQL 堡垒主机，无需客户端应用程序或 SSH 包装器。

### 主要特性

- **部署简单**：将其设置在 DMZ 中，添加用户账户并轻松分配给网络中的特定主机和 URL。
- **会话记录**：记录每个会话，您可以通过内置的管理 Web UI 查看（实时）和重播。
- **透明转发**：不是跳板主机，而是以对客户端完全透明的方式将连接直接转发到目标。
- **安全认证**：原生支持 2FA（TOTP）和 SSO（OpenID Connect）。
- **轻量高效**：单二进制文件，无依赖项，使用 100% 安全的 Rust 编写。
- **协议支持**：支持 SSH、HTTPS、MySQL 和 PostgreSQL 协议。

### 与其他工具的区别

Warpgate 与跳板主机、VPN 或 Teleport 等工具不同，它提供精确的 1:1 用户到服务分配，无需自定义客户端，支持命令级审计和完整会话记录。

## 用法指南

### 安装和下载

- **二进制文件**：从 [GitHub Releases](https://github.com/warp-tech/warpgate/releases) 下载最新的稳定版或测试版。
- **夜间构建**：从 [Nightly Builds](https://nightly.link/warp-tech/warpgate/workflows/build/main) 获取最新构建。
- **Docker**：参考 [Docker 入门指南](https://warpgate.null.page/getting-started-on-docker/)。

### 快速开始

1. 下载并安装 Warpgate 二进制文件。
2. 运行 `warpgate setup` 命令以交互式生成配置文件，包括端口绑定。
3. 启动 Warpgate 服务。
4. 通过 Web 管理界面（默认端口通常为 8888）添加用户和目标主机。
5. 用户可以使用标准客户端（如 SSH 客户端）连接到 Warpgate，格式为 `username@warpgate-host`，然后选择目标。

### 配置示例

- **SSH 连接**：用户通过 `ssh user@warpgate.example.com` 连接，Warpgate 会提示选择目标主机。
- **HTTPS 代理**：通过浏览器访问 Warpgate 的 HTTPS 端口，选择目标 URL 进行代理。
- **数据库连接**：使用 MySQL 或 PostgreSQL 客户端连接到 Warpgate 的相应端口，Warpgate 会透明地转发到目标数据库。

### 管理界面

- 访问内置 Web UI 查看实时会话、会话记录、日志和用户管理。
- 支持用户和目标的精确分配，确保安全访问控制。

### 高级用法

- **SSO 集成**：配置 OpenID Connect 以实现单点登录。
- **会话审计**：所有会话都会被记录，支持命令级审计和重播。
- **Docker 部署**：使用 Docker Compose 快速部署完整环境。

更多详细信息，请参考官方文档：[Warpgate 文档](https://warpgate.null.page)。
