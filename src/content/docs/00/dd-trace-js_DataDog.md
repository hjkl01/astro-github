
---
title: dd-trace-js
---


# dd-trace-js（DataDog 分布式追踪库）

**项目地址**: https://github.com/DataDog/dd-trace-js

## 主要特性

- **自动化 Instrumentation**  
  通过 Node.js 的 `async_hooks`，dd-trace-js 能够自动为多数流行框架（Express, Koa, Hapi, Fastify, gRPC 以及数据库驱动）注入追踪逻辑。

- **支持多种后端**  
  内置支持 DataDog Agent（透过环境变量配置）和 OpenTelemetry（通过导出在 `api` 里）两种后端。

- **丰富的 Span API**  
  - `tracer.trace(name,)`  
  - `tracer.scope().activate(span, callback)`  
  - `tracer.scope().active()`  
  - `tracer.setData(key, value)`、`tracer.setTag(key, value)`  

- **上下文传播**  
  自动将追踪上下文从 HTTP 请求、gRPC 调用、Redis/PubSub 以及共享内存等渠道传递。

- **高性能、低侵入**  
  采用轻量级实现，最小化对业务代码的改动，并通过 `dd-trace` 官方 Docker 镜像提供即装即用。

- **配置灵活**  
  - 小程序式配置（`require('dd-trace').init(...)`）
  - 环境变量覆盖（`DD_ENV`, `DD_SERVICE`, `DD_VERSION`, `DD_LOGS_INJECTION`, `DD_TRACE_DEBUG` 等）
  - `package.json` 中的 `tracer` 脚本

- **搭配 DogStatsD 使用**  
  自动在 Span 结束时记下耗时、错误信息，Datum 通过 DogStatsD 发送。

## 核心功能

| 功能 | 说明 |
|------|------|
| **Trace Collection** | 对每个请求或事务创建 **Span**，自动记录栈、耗时、错误等信息 |
| **Tagging & Logging** | 通过 `setTag`, `setData` 添加业务标签，支持自定义 span 日志 |
| **Error Capture** | 自动捕获异常并关联到当前 Span；不捕获时可手动 `span.setStatus(500)` |
| **Distributed Context** | 通过 HTTP Header、Metadata（gRPC）或其他渠道传播 trace context |
| **Service Mapping** | 自动为 Express/Koa 等框架生成服务调用堆栈，把内部调用映射为子 Span |
| **Metrics Export** | 内建 metrics 收集（如: `request_duration_ms`, `db_query_duration_ms`）可直接导向 DataDog |
| **Sampling** | 内置采样器，可自定义 `sampleRate`, `traceRate`，或通过外部策略（如 OpenTelemetry 采样器） |

## 用法示例

### 1. 安装

```bash
npm install dd-trace
```

### 2. 初始化（放在入口文件最前面，确保所有模块被 Instrumented）

```js
// app.js
const tracer = require('dd-trace').init({
  // 可选参数
  service: 'my-node-service',
  env: process.env.NODE_ENV,
  version: '1.0.0',
  tags: { 'team': 'backend' },
  // 采样率 0.5（50%），可根据业务需求覆盖
  sampleRate: 0.5
});
```

### 3. Express 自动 Instrumentation

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello DataDog Tray!');
});

app.listen(3000, () => console.log('🚀 Server listening on 3000'));
```

在请求期间会自动创建外部 Span（HTTP），内部请求也会创建子 Span。

### 4. 手动创建 Span

```js
const { tracer } = require('dd-trace');

function doSomething() {
  return tracer.trace('doSomething', span => {
    span.setTag('operation', 'cleanup');
    // ...业务逻辑
    if (someCondition) {
      span.setError(new Error('something bad'));
    }
  });
}
```

### 5. 与第三方库共用

库的自动 instrumentation 通过 `autoInstrumentation`：

```js
const tracer = require('dd-trace').init();
tracer.use('express'); // 可选，手动声明
```

已集成 Redis、MongoDB、Mongoose、Mysql、Postgres 等。

### 6. 配置环境变量

| 变量 | 含义 | 默认 |
|------|------|------|
| `DD_AGENT_HOST` | DataDog Agent 主机 | `localhost` |
| `DD_TRACE_AGENT_PORT` | 端口 | `8126` |
| `DD_SERVICE` | Service 名 | 自动推断 |
| `DD_ENV` | 环境 | `undefined` |
| `DD_VERSION` | 版本 | `undefined` |
| `DD_TRACE_DEBUG` | 打印调试 | `false` |
| `DD_LOGS_INJECTION` | 注入日志上下文 | `false` |

### 7. 与容器/云无缝集成

- Docker: 使用官方 `datter/dd-trace` 镜像或自建镜像，放置 `DD_AGENT_HOST=host.docker.internal`
- Kubernetes: 使用 DataDog Agent DaemonSet，Service/端点直接写入 `- DD_AGENT_HOST=datadog-agent`

## 开发与调试

- **开启调试**：`DD_TRACE_DEBUG=true`  
- **打印 Trace**：`tracer.trace(...)` 里 `console.log(span.context().toTraceId())`
- **自定义日志采样**：`tracer.setTraceFilter(() => true)` 或 `tracer.setErrorFilter(...)`

## 贡献

- Fork → Clone → `npm install` → `npm test`  
- 代码规范使用 Prettier 与 ESLint。  
- Pull Request 需通过 CI：`npm run lint && npm run test`

## 参考

- 官方文档: https://docs.datadoghq.com/tracing/setup/nodejs
- OpenTelemetry 兼容：`npm install @opentelemetry/api`
- 示例仓库: https://github.com/DataDog/dd-trace-js/tree/master/examples

---

**项目地址**: https://github.com/DataDog/dd-trace-js
