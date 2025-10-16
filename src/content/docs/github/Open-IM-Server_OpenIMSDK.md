
---
title: Open-IM-Server
---

# Open-IM-Server 项目

## 项目地址
[GitHub 项目地址](https://github.com/OpenIMSDK/Open-IM-Server)

## 主要特性
Open-IM-Server 是一个开源的即时通讯（IM）服务器项目，基于 Go 语言开发，支持高并发和分布式部署。主要特性包括：
- **多协议支持**：兼容 WebSocket、TCP 和 HTTP 等多种通信协议，便于客户端接入。
- **端到端加密**：提供消息加密功能，确保通信安全。
- **实时消息推送**：支持在线消息、离线消息和群组消息的实时传输。
- **用户管理**：内置用户注册、认证和权限控制，支持 OAuth 和 JWT 令牌。
- **群组与社交功能**：支持创建群组、好友关系、音视频通话集成。
- **高可用性**：支持集群部署、负载均衡和数据库分片，适用于大规模用户场景。
- **开源与可扩展**：模块化设计，便于二次开发和集成第三方服务。

## 主要功能
- **消息功能**：文本、图片、文件、表情等消息类型，支持消息撤回、已读回执和消息搜索。
- **用户系统**：用户在线状态管理、好友列表、黑名单功能。
- **群组管理**：群组创建、加入、退出、@ 提及和群公告。
- **音视频支持**：集成 WebRTC 或其他 SDK，实现一对一/多人音视频通话。
- **推送通知**：集成第三方推送服务（如 APNs、FCM），处理离线消息。
- **数据存储**：支持 MySQL、Redis 和 MongoDB 等后端存储，持久化消息和用户数据。
- **管理后台**：提供 Web 界面用于监控服务器状态、用户管理和日志查看。

## 用法
1. **环境准备**：
   - 安装 Go 1.18+、Git 和数据库（MySQL/Redis）。
   - 克隆仓库：`git clone https://github.com/OpenIMSDK/Open-IM-Server.git`。

2. **配置**：
   - 编辑 `config/config.yaml` 文件，设置数据库连接、服务器端口、密钥等参数。
   - 生成配置文件：运行 `./build.sh` 或使用 Makefile。

3. **构建与启动**：
   - 构建项目：`make build`（生成二进制文件）。
   - 启动服务器：`./openim-server`（默认监听 10002 端口）。
   - 对于生产环境，使用 Docker：`docker-compose up -d`（需配置 docker-compose.yml）。

4. **客户端集成**：
   - 使用 OpenIM SDK（支持 iOS、Android、Web、Flutter 等）连接服务器。
   - 示例：初始化 SDK，调用登录 API（如 `login` 方法），然后发送消息（如 `sendMsg`）。

5. **测试与部署**：
   - 使用 Postman 测试 REST API（如 `/user/login`）。
   - 部署时推荐使用 Kubernetes 或云服务，确保防火墙开放必要端口。
   - 详细文档参考项目 Wiki 或官方教程。

更多细节请查看项目 README 和 docs 目录。