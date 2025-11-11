---
title: teleport
---

# Teleport

Teleport 是一个开源工具，用于提供基础设施的连接性、认证、访问控制和审计。它旨在简化对云和本地基础设施的安全访问。

## 功能

- **单点登录 (SSO)**: 支持为所有云基础设施设置 SSO（开源版本仅支持 GitHub SSO）。
- **安全访问保护**: 使用 mTLS 端点和短期证书保护对云和本地服务的访问。
- **隧道建立**: 提供隧道以访问 NAT 和防火墙后面的服务。
- **审计日志**: 提供会话记录和重放的审计日志，支持多种协议。
- **统一 RBAC**: 统一角色-based 访问控制，并通过访问请求强制执行最小权限原则。
- **支持协议和服务**:
  - SSH 节点
  - Kubernetes 集群
  - 数据库 (PostgreSQL, MongoDB, CockroachDB, MySQL)
  - 内部 Web 应用
  - Windows 主机
  - 网络服务器

## 用法

### 安装和运行

要设置单实例 Teleport 集群，请按照[入门指南](https://goteleport.com/docs/admin-guides/deploy-a-cluster/linux-demo/)操作。然后，您可以向 Teleport 集群注册服务器、Kubernetes 集群和其他基础设施。

您也可以开始使用 Teleport Enterprise Cloud，这是一个托管的 Teleport 部署，可以更轻松地启用对基础设施的安全访问。

[注册免费试用](https://goteleport.com/signup) Teleport Enterprise Cloud。

按照指南[注册您的第一个服务器](https://goteleport.com/docs/get-started/)与 Teleport Enterprise Cloud。

### Docker

如果您希望在 Docker 容器中部署 Teleport，请参阅[安装指南](https://goteleport.com/docs/installation/#running-teleport-on-docker)。

### 构建 Teleport

Teleport 包含用 Go 编写的守护进程二进制文件和用 TypeScript 编写的 Web UI。

要构建，请克隆仓库并运行 `make full`。

更多详细信息，请参阅[构建说明](https://github.com/gravitational/teleport#building-teleport)。

### 架构和文档

- 架构: [https://goteleport.com/docs/reference/architecture/](https://goteleport.com/docs/reference/architecture/)
- 入门: [https://goteleport.com/docs/get-started/](https://goteleport.com/docs/get-started/)
- 文档: [https://goteleport.com/docs/](https://goteleport.com/docs/)
