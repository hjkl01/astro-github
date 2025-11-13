---
title: webdis
---

# Webdis 项目

## 项目地址
[https://github.com/nicolasff/webdis](https://github.com/nicolasff/webdis)

## 主要特性
Webdis 是一个将 Redis 数据库转换为 HTTP 服务器的开源工具。它基于 Redis 的 HTTP 协议实现，允许通过 Web 接口直接访问和操作 Redis 数据。主要特性包括：
- **HTTP 接口支持**：提供 RESTful API，支持 GET、POST 等 HTTP 方法来执行 Redis 命令。
- **JSON 响应**：所有 Redis 操作返回 JSON 格式的数据，便于前端或脚本集成。
- **跨域支持 (CORS)**：内置 CORS 支持，适合 Web 应用直接调用。
- **安全配置**：支持 Redis 认证、SSL/TLS 加密，以及访问控制列表 (ACL)。
- **轻量级**：无需额外依赖，直接运行在 Redis 之上，资源占用低。
- **实时监控**：支持 Redis 的 MONITOR 命令，实现实时事件流。

## 主要功能
- **命令执行**：通过 HTTP 请求执行 Redis 命令，例如 GET/SET 键值对、LIST 操作、HASH 处理等。
- **Pub/Sub 支持**：实现 Redis 的发布/订阅模式，通过 WebSocket 或长轮询订阅消息。
- **批量操作**：支持多命令管道 (PIPELINE) 以提高性能。
- **错误处理**：统一返回 HTTP 状态码和 JSON 错误信息，便于调试。
- **配置灵活**：可自定义端口、主机、认证等参数，支持生产环境部署。

## 用法
1. **安装与运行**：
   - 克隆仓库：`git clone https://github.com/nicolasff/webdis.git`
   - 确保 Redis 已安装并运行。
   - 编译（如果需要）：使用 Makefile 或直接运行二进制文件。
   - 启动：`./webdis --port=7379 --address=0.0.0.0`（默认连接本地 Redis）。

2. **基本用法**：
   - **键值操作**：`GET /keys/mykey`（获取键值），`POST /keys/mykey`（设置键值，body 为 JSON）。
   - **列表操作**：`POST /lists/mylist/push`（添加元素）。
   - **Pub/Sub**：`GET /subscribe/channel`（订阅频道）。
   - **认证**：添加 HTTP Basic Auth 或在配置中指定 Redis 密码。

3. **示例**：
   - 设置键：`curl -X POST -d '{"value": "hello"}' http://localhost:7379/keys/greeting`
   - 获取键：`curl http://localhost:7379/keys/greeting` 返回 `{"value": "hello"}`。

更多细节请参考项目 README。