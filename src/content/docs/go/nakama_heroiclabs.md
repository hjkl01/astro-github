
---
title: nakama
---

# Nakama 项目

## 项目地址
[GitHub 项目地址](https://github.com/heroiclabs/nakama)

## 主要特性
Nakama 是一个开源的分布式服务器框架，专为构建实时多人游戏和社交应用而设计。它提供高性能、可扩展的架构，支持多种游戏引擎和平台。主要特性包括：
- **实时通信**：支持 WebSocket 和 gRPC，实现低延迟的多人互动，如聊天、匹配和同步。
- **用户管理**：内置用户认证、会话管理和权限控制，支持社交登录（Google、Facebook 等）。
- **存储系统**：灵活的键值存储和关系数据库集成，用于保存用户数据、游戏状态和资产。
- **匹配系统**：智能匹配算法，支持自定义匹配规则和大厅功能。
- **社交功能**：朋友系统、群组、排行榜和通知推送。
- **可扩展性**：支持水平扩展，使用 Lua 或 TypeScript 编写自定义逻辑；集成 Redis、PostgreSQL 等后端。
- **跨平台支持**：兼容 Unity、Unreal Engine、Godot 等游戏引擎，以及 Web 和移动应用。
- **安全与监控**：内置加密、API 网关和日志系统，便于运维。

## 主要功能
- **认证与授权**：通过 JWT 令牌处理用户登录和访问控制。
- **实时多人游戏**：处理位置同步、动作广播和回合制逻辑。
- **数据持久化**：存储领导板、库存和进度，支持 ACID 事务。
- **通知与推送**：集成 FCM 和 APNs 发送实时通知。
- **分析与洞察**：内置指标收集和事件日志，用于游戏分析。
- **插件扩展**：通过模块化设计添加自定义功能，如支付集成或 AI 服务。

## 用法
1. **安装与部署**：
   - 从 GitHub 克隆仓库：`git clone https://github.com/heroiclabs/nakama.git`。
   - 使用 Docker 快速启动：运行 `docker run --rm -it -p 7350:7350 heroiclabs/nakama:latest`。
   - 或构建二进制文件：安装 Go 环境，运行 `make build`。

2. **配置**：
   - 编辑 `nakama.yml` 文件设置数据库（PostgreSQL）、缓存（Redis）和服务器参数。
   - 示例配置：指定端口、API 密钥和模块路径。

3. **开发自定义逻辑**：
   - 使用 Lua 或 TypeScript 编写 RPC 函数，例如在 `lua` 目录下创建脚本处理匹配逻辑。
   - 示例 Lua 脚本：
     ```lua
     local nk = require("nakama")

     nk.register_rpc("hello", function(context, payload)
         return nk.json_encode({message = "Hello from Nakama!"})
     end)
     ```

4. **客户端集成**：
   - 使用官方 SDK（如 Unity、JavaScript）：安装后初始化客户端 `client = new NakamaClient("http://localhost:7350");`。
   - 示例：认证用户 `session = await client.authenticateDeviceAsync(deviceId);`，然后调用 RPC `result = await client.rpcAsync(session, "hello");`。

5. **运行与测试**：
   - 启动服务器：`./nakama`。
   - 使用 Postman 或 SDK 测试 API 端点，如 `/v2/account` 获取用户账户。
   - 监控：通过控制台日志或集成 Prometheus。

Nakama 适用于从小型独立游戏到大型多人在线游戏的开发，文档详见项目 Wiki。