---
title: centrifugo
---

# Centrifugo 项目

## 项目地址

[GitHub 项目地址](https://github.com/centrifugal/centrifugo)

## 主要特性

Centrifugo 是一个开源的实时消息服务器，专为现代 Web 和移动应用设计。它支持实时通信协议，如 WebSocket、HTTP 流和长轮询，提供高性能、低延迟的消息传递。主要特性包括：

- **实时消息推送**：支持发布/订阅（Pub/Sub）模式，允许服务器向客户端实时推送消息。
- **多种传输协议**：内置 WebSocket 支持，同时兼容 HTTP 流和长轮询，确保在不同网络环境下的兼容性。
- **高可扩展性**：可水平扩展，支持集群模式，使用 Redis 或其他后端存储来管理连接和通道。
- **客户端 SDK**：提供多种语言的客户端库，包括 JavaScript、iOS、Android 等，便于集成到 Web 和移动应用中。
- **安全性**：支持 JWT（JSON Web Token）认证、TLS 加密，以及细粒度的访问控制。
- **轻量级**：基于 Go 语言开发，资源占用低，适合部署在各种环境中。

## 主要功能

- **连接管理**：处理客户端连接、断线重连和心跳检测。
- **频道订阅**：客户端可以订阅特定频道，接收相关消息，支持命名空间和权限控制。
- **消息广播**：服务器 API 允许从后端服务向指定频道或用户广播消息。
- **历史消息**：可选支持消息历史记录和恢复功能，通过后端存储实现。
- **代理模式**：可以与现有后端（如 Node.js、Python）集成，通过代理将消息路由到 Centrifugo。
- **监控与调试**：内置 Admin UI 和 API，用于监控连接状态、消息流量和调试问题。
- **多租户支持**：通过多实例或配置隔离不同应用或用户组。

## 用法

### 安装

1. **二进制安装**（推荐生产环境）：
   - 从 GitHub Releases 下载预编译二进制文件。
   - 解压并运行：`./centrifugo`（需配置 config.json）。

2. **Docker 安装**：

   ```
   docker run -d -p 8000:8000 centrifugo/centrifugo
   ```

3. **从源代码构建**：
   - 安装 Go 环境。
   - 克隆仓库：`git clone https://github.com/centrifugal/centrifugo.git`。
   - 构建：`go build`。

### 配置

创建一个 `config.json` 文件，例如：

```json
{
  "token_hmac_secret_key": "your-secret-key",
  "api_key": "your-api-key",
  "admin": true,
  "admin_secret": "admin-secret",
  "allowed_origins": ["http://localhost:3000"],
  "proxy_connect_endpoint": "http://backend/connect"
}
```

- `token_hmac_secret_key`：用于客户端 JWT 令牌签名。
- `api_key`：保护 API 端点的密钥。

### 运行

- 启动服务器：`./centrifugo -c config.json`。
- 默认监听端口：8000（WebSocket 和 HTTP）。

### 客户端集成（JavaScript 示例）

1. 引入 SDK：`<script src="https://cdn.jsdelivr.net/npm/@centrifugal/centrifugo@latest/centrifugo.js"></script>`。
2. 连接和订阅：

   ```javascript
   const centrifugo = new Centrifugo(
     'ws://localhost:8000/connection/websocket'
   );
   centrifugo.setToken('your-jwt-token');
   centrifugo.connect();

   const channel = centrifugo.newSubscription('chat');
   channel.on('publication', function (msg) {
     console.log('收到消息:', msg.data);
   });
   channel.subscribe();
   ```

3. 发布消息（从后端 API）：
   - 使用 HTTP POST 到 `/api` 端点：
     ```
     curl -H "Authorization: apikey your-api-key" \
          -d '{"method": "publish", "params": {"channel": "chat", "data": {"msg": "Hello"}}}'
          http://localhost:8000/api
     ```

### 高级用法

- **集群部署**：配置 Redis 作为引擎：`"engine": "redis", "redis": {"address": "redis://localhost:6379"}`。
- **Admin UI**：访问 `http://localhost:8000`，使用 admin_secret 登录查看实时统计。
- **文档参考**：详见项目 README 和官方文档（https://centrifugal.dev/docs）。

## 文档

- [Centrifugo 官方文档站点](https://centrifugal.dev)
- [安装说明](https://centrifugal.dev/docs/getting-started/installation)
- [入门教程](https://centrifugal.dev/docs/getting-started/quickstart)
- [设计概述和惯用用法](https://centrifugal.dev/docs/getting-started/design)
- [使用 Centrifugo 构建 WebSocket 聊天/信使应用](https://centrifugal.dev/docs/tutorial/intro) 教程
- [Centrifugal 博客](https://centrifugal.dev/blog)
- [FAQ](https://centrifugal.dev/docs/faq)

## 加入社区

- [Telegram](https://t.me/joinchat/ABFVWBE0AhkyyhREoaboXQ)
- [Discord](https://discord.gg/tYgADKx)
- [Twitter](https://twitter.com/centrifugalabs)

## 为什么选择 Centrifugo

Centrifugo 的核心理念很简单——它是基于现代实时传输的 PUB/SUB 服务器：

![协议 PUB/SUB](https://centrifugal.dev/img/protocol_pub_sub.png?v=2)

困难的部分是使这个概念生产就绪、高效、灵活并可从不同应用环境访问。Centrifugo 是一个成熟的解决方案，已经帮助许多项目添加实时功能并扩展到许多并发连接。Centrifugo 提供了一套在该领域其他开源解决方案中不可用的功能：

- 高效的实时传输：WebSocket、HTTP-streaming、Server-Sent Events、GRPC、WebTransport
- 内置可扩展性与 Redis（或 Redis Cluster，或 Redis 兼容存储——例如 AWS Elasticache、Valkey、KeyDB、DragonflyDB 等）、或 Nats。
- 简单的 HTTP 和 GRPC 服务器 API，用于从应用后端与 Centrifugo 通信
- 异步 PostgreSQL 和 Kafka 消费者，支持事务性 outbox 和 CDC 模式
- 灵活的连接认证机制：JWT 和代理式（通过从 Centrifugo 到后端的请求）
- 通过单个连接的频道订阅多路复用
- 不同类型的订阅：客户端侧和服务器侧
- 各种频道权限策略，频道命名空间概念
- 频道中的热消息历史，具有自动重新连接时的消息恢复，缓存恢复模式（订阅时立即交付最新发布）
- 基于 Fossil 算法的频道中的增量压缩
- 频道在线存在信息，具有加入/离开通知
- 通过实时连接向后端发送 RPC 调用的方式
- 由几个官方 SDK 包装的严格有效的客户端协议
- JSON 和二进制 Protobuf 消息传输，具有优化的序列化和内置批处理
- 美丽的嵌入式管理 Web UI
- 通过暴露的大量 Prometheus 指标和官方 Grafana 仪表板提供出色的可观测性
- 等等，访问 [Centrifugo 文档站点](https://centrifugal.dev)

## 支持

此仓库由 [packagecloud.io](https://packagecloud.io/) 托管。

<a href="https://packagecloud.io/"><img height="46" width="158" alt="Private NPM registry and Maven, RPM, DEB, PyPi and RubyGem Repository · packagecloud" src="https://packagecloud.io/images/packagecloud-badge.png" /></a>

也感谢 [JetBrains](https://www.jetbrains.com/) 支持 OSS（此处大部分代码在 Goland 中编写）：

<a href="https://www.jetbrains.com/"><img height="140" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains logo"></a>

此项目适用于聊天应用、实时通知、协作工具等场景，提供可靠的实时通信基础设施。
