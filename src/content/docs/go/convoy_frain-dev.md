---
title: convoy
---

# Convoy

## 项目地址

[GitHub 项目地址](https://github.com/frain-dev/convoy)

- 网站：https://getconvoy.io
- 论坛：[Convoy Community](https://community.getconvoy.io)
- 文档：https://docs.getconvoy.io
- 部署：[安装 Convoy](https://docs.getconvoy.io/deployment/install-convoy/docker)
- Slack：[加入社区](https://join.slack.com/t/convoy-community/shared_invite/zt-xiuuoj0m-yPp~ylfYMCV9s038QL0IUQ)

## 项目简介

Convoy 是一个开源的高性能 Webhooks 网关，用于安全地摄取、持久化、调试、交付和管理数百万事件。它具有丰富的功能，如重试、速率限制、静态 IP、断路器、滚动密钥等。

Convoy 提供以下关键功能：

- **Webhooks 网关**：作为 Webhooks 网关，Convoy 位于网络边缘，从微服务流式传输 Webhooks，并将它们发送到用户以及从提供商接收 Webhooks 并路由到所需服务。这样，您的内部系统永远不会暴露在公共互联网上。
- **可扩展性**：Convoy 充当 Webhooks 的专用消息队列，并被设计为水平可扩展。它包括几个组件，如 `API 服务器`、`workers`、`scheduler` 和 `socket server`，这些组件可以独立扩展以适应需求。
- **安全性**：Convoy 为 Webhooks 提供几种安全功能，如有效负载签名以确保消息完整性、用于认证 Webhook 端点的承载令牌认证，以及具有严格防火墙规则的环境中的静态 IP。
- **扇出**：Convoy 能够根据事件类型或有效负载结构将事件路由到多个端点。
- **速率限制**：虽然 Convoy 能够以巨大的速率摄取事件，但它以可配置的速率限制对端点的交付。
- **重试和批量重试**：Convoy 支持两种重试算法；恒定时间和指数退避与抖动。当自动重试不足时，Convoy 为连续失败处理重试事件的端点提供批量重试。
- **面向客户的仪表板**：Convoy 允许您生成嵌入到应用程序中的面向客户的 Webhooks 仪表板。在这个仪表板上，用户可以调试 Webhooks、重试事件、添加端点并配置每个端点的订阅。
- **端点故障通知**：当端点连续失败处理事件时，Convoy 会禁用端点并发送通知。支持两种类型的通知：电子邮件和 Slack 通知。

## 主要功能

Convoy 的核心功能围绕事件管理和消息处理展开：

- **事件端点管理**：创建和管理端点，用于接收和发送事件，支持 webhook 验证和重放。
- **队列与消费者**：配置队列以处理异步消息，支持消费者组和负载均衡。
- **事件历史与重放**：存储事件历史记录，并允许重放过去的事件以实现数据一致性。
- **集成与扩展**：内置模板和预设集成，便于连接第三方服务，如数据库、云存储和通知系统。
- **仪表板**：Web-based 仪表板，提供可视化界面用于配置、监控和管理资源。
- **批量处理**：支持批量事件导入和处理，适用于大规模数据场景。

## 用法

### 安装

1. **使用 Docker**（推荐快速启动）：

   ```
   docker run -d -p 5005:5005 -p 5006:5006 --name convoy frain-dev/convoy:latest
   ```

   默认访问 API：`http://localhost:5005`，仪表板：`http://localhost:5006`。

2. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/frain-dev/convoy.git`
   - 安装依赖：使用 Go 1.18+，运行 `go mod tidy`。
   - 构建：`make build`。
   - 配置：编辑 `config/config.yaml` 文件，设置数据库（支持 PostgreSQL、MongoDB）和 Redis。
   - 运行：`./convoy server`。

### 基本用法

1. **启动服务**：确保数据库和 Redis 已运行，然后启动 Convoy。
2. **创建端点**（通过 API 或仪表板）：
   - API 示例（使用 curl）：
     ```
     curl -X POST http://localhost:5005/api/v1/endpoints \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "My Endpoint",
       "url": "https://example.com/webhook",
       "secret": "my-secret-key"
     }'
     ```
3. **发送事件**：
   ```
   curl -X POST http://localhost:5005/api/v1/projects/<project-id>/events \
   -H "Authorization: Bearer <your-jwt-token>" \
   -H "Content-Type: application/json" \
   -d '{
     "event_type": "user.signup",
     "data": {"user_id": 123}
   }'
   ```
4. **管理队列**：在仪表板中创建队列，配置消费者并监控消息流。
5. **CLI 用法**：安装 CLI 后，使用 `convoy create endpoint --title "Test" --url "https://test.com"` 等命令。

详细文档请参考项目仓库的 [README](https://github.com/frain-dev/convoy/blob/main/README.md) 和 [API 文档](https://docs.convoy.dev)。

## 贡献

感谢您对贡献的兴趣！请在贡献之前参考 [CONTRIBUTING.md](https://github.com/frain-dev/convoy/blob/main/CONTRIBUTING.md)。对于 Convoy 仪表板的贡献，请参考 [web/ui](https://github.com/frain-dev/convoy/tree/main/web/ui) 目录。

## 许可证

[Elastic License v2.0](https://github.com/frain-dev/convoy/blob/main/LICENSE)
