
---
title: convoy
---

# Convoy 项目

## 项目地址
[GitHub 项目地址](https://github.com/frain-dev/convoy)

## 主要特性
Convoy 是一个开源的消息队列和事件驱动架构平台，专为现代应用程序设计。它提供高可用性、可扩展性和易用性，支持多种消息协议和集成方式。主要特性包括：
- **多协议支持**：兼容 HTTP、Webhooks、Kafka、RabbitMQ 等多种消息源和目标。
- **事件路由与过滤**：允许用户定义路由规则、事件过滤器和转换器，实现智能消息分发。
- **高可用性和容错**：内置重试机制、死信队列和监控，支持分布式部署。
- **插件系统**：可扩展的插件架构，支持自定义集成，如 Slack、Discord 等通知服务。
- **API 和 CLI**：提供 RESTful API 和命令行工具，便于管理和自动化。
- **安全性**：支持 JWT 认证、签名验证和 TLS 加密，确保消息传输安全。
- **监控与日志**：集成 Prometheus 和 Grafana，支持实时监控和详细日志记录。

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