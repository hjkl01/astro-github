---
title: WuKongIM
---

# WuKongIM 项目

## 项目地址
[GitHub 项目地址](https://github.com/WuKongIM/WuKongIM)

## 主要特性
WuKongIM 是一个高性能、分布式即时通讯（IM）服务器框架，基于 Go 语言开发，支持大规模用户并发和低延迟消息传递。主要特性包括：
- **高性能架构**：采用分布式设计，支持水平扩展，单节点可处理数十万并发连接。
- **多协议支持**：兼容 WebSocket、TCP 等协议，便于客户端集成。
- **消息可靠性**：提供消息持久化、离线消息推送和重连机制，确保消息不丢失。
- **安全性**：内置 TLS 加密、用户认证和权限控制，支持 OAuth 和 JWT。
- **可扩展性**：模块化设计，支持自定义插件，如群聊、文件传输和音视频通话扩展。
- **监控与运维**：集成 Prometheus 和 Grafana，支持实时监控和日志管理。

## 主要功能
- **用户管理**：注册、登录、好友关系和群组管理。
- **消息传递**：支持单聊、群聊、系统消息和广播推送。
- **离线与在线状态**：实时在线状态同步和离线消息存储。
- **多端同步**：支持多设备登录和消息同步。
- **推送服务**：集成第三方推送（如 APNs、FCM）实现移动端通知。
- **API 接口**：提供 RESTful API 和 SDK，便于前后端集成。

## 用法
### 1. 安装与部署
- **环境要求**：Go 1.16+，Redis（用于缓存），MySQL（用于存储）。
- **克隆项目**：
  ```
  git clone https://github.com/WuKongIM/WuKongIM.git
  cd WuKongIM
  ```
- **构建**：
  ```
  go mod tidy
  go build -o wukongim cmd/server/main.go
  ```
- **配置**：编辑 `config/config.yaml` 文件，设置数据库连接、端口等参数。
- **启动服务器**：
  ```
  ./wukongim start
  ```

### 2. 客户端集成
- **Go SDK**：导入 `github.com/WuKongIM/WuKongIM/pkg/client`，示例：
  ```go
  import "github.com/WuKongIM/WuKongIM/pkg/client"

  conn, err := client.NewConn("ws://localhost:3000")
  if err != nil {
      // 处理错误
  }
  conn.SendMessage("hello")
  ```
- **Web/移动端**：使用 WebSocket 连接服务器地址，支持 JavaScript、iOS 和 Android SDK。
- **API 调用**：通过 HTTP POST 请求，如发送消息 API：`/api/v1/message/send`。

### 3. 扩展与自定义
- 添加插件：在 `plugins` 目录下实现接口，重新构建服务器。
- 集群部署：使用 Docker Compose 或 Kubernetes 扩展多节点，支持负载均衡。

详细文档见项目 README 和 `docs` 目录。