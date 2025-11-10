---
title: open-im-server
---

以下为直接存入文件 **src/content/docs/00/open-im-server_openimsdk.md** 的 Markdown 内容。  
（请将此内容复制到对应文件即可，文件路径已按需求提供。）

```markdown
# open-im-server (OpenIM SDK)

**项目地址**: https://github.com/openimsdk/open-im-server

## 概述
OpenIM Server 是一套基于 Go 开发的企业级即时通讯后台服务，提供高性能、高可扩展性的聊天、群组、文件、推送、离线消息等核心业务能力。它以“轻量、可插拔、可扩展”为设计理念，支持多协议（WebSocket、gRPC）接入，便于快速构建跨终端通信应用。

## 核心特性
| 特性 | 说明 |
|------|------|
| **实时消息** | 支持点对点与群组实时消息推送，使用 WebSocket、gRPC 双通道互斥 |
| **离线消息** | 消息持久化存储，用户离线后可在上线时同步未读消息 |
| **多用户在线状态** | 实时在线监测与推送，提供 presence 服务 |
| **群组与讨论组** | 支持多种群组类型、成员管理、消息撤回、表情点踩、禁言、踢人等操作 |
| **文件与图片上传** | 内置文件上传接口，可自定义存储后端（对象存储、云文件系统） |
| **推送通知** | 集成 Firebase、JPush、华为推送，支持自定义消息 & 业务类型 |
| **自定义业务字段** | 支持自定义扩展字段，满足业务变更需求 |
| **分布式部署** | 支持多实例部署，配合 Nginx + Redis 集群实现高可用 |
| **鉴权 & 加密** | JWT Token、TLS 加密传输；可结合鉴权服务 (CAS, OAuth) |

## 架构亮点
- **微服务化**：每个业务域（消息、群组、文件、推送、鉴权）可单独部署、水平扩容  
- **协议统一**：利用 Protobuf + gRPC 做服务间通信；WebSocket 作为前端实时通道  
- **可插拔存储**：支持 MySQL、PostgreSQL、MongoDB 等数据库，缓存使用 Redis 或 Memorystore  
- **弹性伸缩**：与 Kubernetes 集成，借助 HPA、Service Mesh（Istio）实现灰度发布与弹性伸缩  

## 快速入门

### 1. 克隆代码
```bash
git clone https://github.com/openimsdk/open-im-server.git
cd open-im-server
```

### 2. 编译
```bash
make build
```

### 3. 配置环境
编辑 `config.yaml`，配置数据库连接、Redis、存储等信息。

```yaml
Server:
  Port: 7888
  JwtSecretKey: "YOUR_SECRET"

Database:
  User: "root"
  Pass: "password"
  Host: "127.0.0.1:3306"
  Name: "open_im"

Redis:
  Host: "127.0.0.1:6379"
```

### 4. 启动
```bash
./build/open-im-server
```

访问 `http://localhost:7888` 可进行 API 调用或使用前端 SDK 连接。

### 5. Docker 部署
```bash
docker pull registry.cn-beijing.aliyuncs.com/openimsdk/open-im-server:v1.0
docker run -d -p 7888:7888 -v ./config.yaml:/app/config.yaml openimsdk/open-im-server:v1.0
```

## API 文档
- gRPC 接口请查看 `/proto` 目录下的 .proto 文件，启动后可以使用 `protoc` 生成对应 SDK。
- HTTP 接口可通过 Swagger UI 访问 `http://<host>:<port>/swagger`

## 贡献指南
1. Fork 本仓库  
2. 创建 Feature/bugfix 分支  
3. 通过 GitHub Pull Requests 提交
4. 代码规范请参照 `golangci-lint` 规则

## 许可证
本项目基于 MIT 许可证发布，详情见 LICENSE 文件。

``` 
