---
title: inngest
---


# Inngest 事件与工作流引擎

**GitHub 项目地址:**  
https://github.com/inngest/inngest

## 项目简介  
Inngest 是一个开源、无服务器（serverless）事件/工作流引擎，帮助你在云函数（Lambda、Cloud Functions、Azure Functions 等）里轻松构建可靠的异步工作流。它提供了强大的事件驱动、可靠重试、子工作流、并发控制等功能，并且支持多语言 SDK（Node.js、Python、Go 等）。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **无服务器友好** | 只需部署一个基本的 HTTP 端点即可接收所有事件，兼容 Lambda、Cloud Functions、FaaS 等。 |
| **可靠重试** | 自动指数退避重试，支持用户自定义重试逻辑。 |
| **分布式调度** | 内置分布式锁，天然支持多实例（多进程/多容器），避免重复执行。 |
| **子工作流（Subflows）** | 轻松组合复合工作流，支持并行/串行模式。 |
| **事件补偿 / 纠错** | 通过补偿函数确保完整事务一致性。 |
| **可观察与监控** | 与 OpenTelemetry、Datadog 等集成，提供丰富的指标。 |
| **插件化** | 支持自定义插件（例如定时触发器、消息队列触发器）。 |

## 关键功能  

1. **事件触发**  
   - 通过 HTTP `POST /inngest` 或 SDK 发送 JSON 事件。  
   - 支持自定义 `name`、`payload`、`attributes`。  
2. **工作流声明**  
   - 使用 `inngest` SDK 在 Node.js/Go/Python 中声明 `flow` 或 `subflow`。  
   - 可为每条流添加 `maxRetries`、`schedule`、`concurrency`。  
3. **状态持久化**  
   - 内置使用 AWS DynamoDB、GCP Firestore、PostgreSQL 或自建数据库存储执行状态。  
4. **并发与速率控制**  
   - `maxConcurrent` 与 `rateLimit` 节流，避免资源过载。  
5. **监控与日志**  
   - 每个事件都有唯一 `runId`，可通过 UI 或 API 查询详情。  

## 快速使用示例  

### 1. 安装 SDK (Node.js)

```bash
npm install inngest
```

### 2. 编写一个简单工作流

```ts
import { Inngest } from "inngest";
const inngest = new Inngest();

inngest.createFunction(
  {
    id: "send-welcome-email",
    name: "Send Welcome Email",
    // 触发条件
    events: ["user.created"],
    // 可选：获得事件时使用的 payload
    type:"user.created",
    // 重试次数
    maxRetries: 5,
  },
  async ({ event, logger }) => {
    const { email, name } = event.data;
    logger.info(`Sending welcome email to ${name} (${email})`);
    // …调用邮件服务…
  },
);

export const api = inngest.api(); // 用作 HTTP 端点
```

### 3. 部署为 Lambda（Node.js 14.x）

```bash
node_modules/.bin/inngest build
# 上传给 Lambda
```

### 4. 触发事件（HTTP 端点或 SDK）

```bash
curl -X POST https://<YOUR_DEPLOYMENT>/api \
  -H "Content-Type: application/json" \
  -d '{"name":"user.created","data":{"email":"alice@example.com","name":"Alice"}}'
```

## 如何加入社区  

- **Issue**: 提交 bug 或特性请求。  
- **Pull Requests**: 贡献代码，遵循代码规范。  
- **讨论**: GitHub Discussions 或 Slack 频道。  

> **TIP**：Inngest 官方提供了完整的 SDK 示例、CLI 工具与可视化 Dashboard，建议先查看官方文档（`website/docs`）进一步学习。

---
**项目地址**: <https://github.com/inngest/inngest>
