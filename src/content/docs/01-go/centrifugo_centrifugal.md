
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
   const centrifugo = new Centrifugo('ws://localhost:8000/connection/websocket');
   centrifugo.setToken('your-jwt-token');
   centrifugo.connect();

   const channel = centrifugo.newSubscription('chat');
   channel.on('publication', function(msg) {
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

此项目适用于聊天应用、实时通知、协作工具等场景，提供可靠的实时通信基础设施。