
---
title: slack-mcp-server
---

# Slack MCP Server (korotovsky)

**GitHub 地址**: <https://github.com/korotovsky/slack-mcp-server>

---

## 项目简介
`slack-mcp-server` 是一个用 Node.js 编写的轻量级服务器，专门用于接收并转发 Slack 事件、Slash Command 和 Interactivity 交互，满足需要在自建后端与 Slack 进行实时通信的场景。它实现了 Slack 官方的签名验证、事件回调、命令处理、以及可扩展的业务逻辑插件。

---

## 主要特性

| 特性 | 描述 |
|------|------|
| **事件订阅** | 监听 `message`, `reaction_added`, `app_mention` 等事件，并可通过插件进行自定义处理。 |
| **Slash Command** | 支持自定义命令 `/mycmd`，并在服务器端解析参数与回复。 |
| **Interactivity** | 处理按钮、选择菜单、模态窗口等交互事件。 |
| **签名校验** | 使用 `SLACK_SIGNING_SECRET` 自动校验请求签名，保证安全。 |
| **插件化架构** | 通过 `plugins/` 目录可以轻松添加/移除业务逻辑。 |
| **Docker 化** | 提供 `Dockerfile` 与 `docker-compose.yml`，一键部署。 |
| **日志与监控** | 基于 `winston` 的日志系统，支持 `stdout` 与 `stderr` 输出。 |
| **环境配置** | 通过 `.env` 文件或环境变量配置 Slack 相关凭证与服务器选项。 |

---

## 功能模块

- `src/index.js` – 入口文件，创建 Express 服务器并挂载路由。
- `src/routes/events.js` – 处理 Slack 事件回调。
- `src/routes/commands.js` – 处理 Slash Command。
- `src/routes/interactivity.js` – 处理交互事件。
- `src/plugins/` – 插件目录，每个插件导出 `handleEvent`, `handleCommand`, `handleInteractivity`。
- `src/middleware/verifySignature.js` – Slack 请求签名验证中间件。
- `src/config.js` – 环境变量读取与默认值。

---

## 安装与运行

```bash
# 克隆仓库
git clone https://github.com/korotovsky/slack-mcp-server.git
cd slack-mcp-server

# 安装依赖
npm install

# 创建 .env 文件
cp .env.example .env
# 根据提示填入 SLACK_SIGNING_SECRET, SLACK_BOT_TOKEN 等

# 启动服务器
npm start
```

### Docker 部署

```bash
docker build -t slack-mcp-server .
docker run -d -p 3000:3000 \
  -e SLACK_SIGNING_SECRET=xxxx \
  -e SLACK_BOT_TOKEN=xxxx \
  slack-mcp-server
```

---

## 用法示例

### 1. 事件处理插件

```js
// src/plugins/logger.js
module.exports = {
  handleEvent: ({ event }) => {
    console.log('收到事件:', event.type, event);
  },
};
```

### 2. Slash Command 示例

```js
// src/plugins/echo.js
module.exports = {
  handleCommand: ({ command, text }) => {
    if (command === '/echo') {
      return { text: `你说的是: ${text}` };
    }
  },
};
```

### 3. Interactivity 示例

```js
// src/plugins/button.js
module.exports = {
  handleInteractivity: ({ payload }) => {
    if (payload.actions[0].action_id === 'button_click') {
      return { text: '按钮已点击！' };
    }
  },
};
```

---

## 配置

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `PORT` | 服务器监听端口 | `3000` |
| `SLACK_SIGNING_SECRET` | Slack 签名密钥 | 必填 |
| `SLACK_BOT_TOKEN` | Slack Bot Token | 必填 |
| `LOG_LEVEL` | 日志等级 | `info` |

---

## 贡献

欢迎提交 PR、issue 或者提供插件。请遵循项目的代码规范和提交信息格式。

---

## 许可证

MIT © 2024 korotovsky

---