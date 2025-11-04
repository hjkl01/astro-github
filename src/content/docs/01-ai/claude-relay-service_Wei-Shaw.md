
---
title: claude-relay-service
---


# Claude Relay Service
仓库地址: <https://github.com/Wei-Shaw/claude-relay-service>

## 项目简介
Claude Relay Service 为 Claude AI 提供一个轻量级的 HTTP 代理服务，旨在解决同源策略、访问受限及网络延迟等问题。它通过在本地或服务器上部署 API 接口，将前端请求转发至 Claude 服务器，并返回响应，简化了与 Claude 的集成过程。

## 主要功能
- **HTTP/HTTPS 隧道**：将前端请求安全地转发到 Claude 服务器，支持 TLS 加密。
- **请求缓存**：可选的缓存层，减少对 Claude API 的重复调用，提高性能。
- **API 速率限制**：内置速率限制，防止过度调用导致服务被封禁。
- **WebSocket 支持**：提供实时聊天功能的 WebSocket 接口。
- **可配置性**：支持环境变量或配置文件方式设置 Claude API 密钥、代理地址等参数。
- **日志与监控**：记录请求日志，支持自定义日志格式与输出。

## 用法

### 1. 环境准备
```bash
# 克隆项目
git clone https://github.com/Wei-Shaw/claude-relay-service.git

# 进入目录
cd claude-relay-service
```

### 2. 配置
编辑 `.env.example` 并重命名为 `.env`，配置以下参数：
```dotenv
CLAUDE_API_KEY=YOUR_CLAUDE_API_KEY
CLAUDE_ENDPOINT=https://api.anthropic.com/v1/messages
PORT=8080
```

### 3. 运行
```bash
# 直接运行（Node.js 环境）
node server.js

# 或使用 Docker
docker build -t claude-relay .
docker run -p 8080:8080 -e CLAUDE_API_KEY=YOUR_KEY claude-relay
```

### 4. API 使用示例
```bash
curl -X POST http://localhost:8080/message \
     -H "Content-Type: application/json" \
     -d '{"prompt":"Hello Claude"}'
```

返回示例（JSON）：
```json
{
  "id": "msg_12345",
  "content": "Hello, how can I help you today?"
}
```

### 5. WebSocket 示例
```javascript
const ws = new WebSocket('ws://localhost:8080/ws');

ws.onopen = () => ws.send(JSON.stringify({ prompt: 'Hi Claude' }));
ws.onmessage = (e) => console.log('Claude says:', e.data);
```

## 目录结构
```
claude-relay-service/
├── src/
│   ├── server.js          # 主入口
│   ├── routes/
│   │   └── message.js    # HTTP 端点
│   └── websocket.js      # WebSocket 处理
├── config/
│   └── config.js         # 配置读取
├── logs/                  # 日志存储
├── Dockerfile
└── README.md
```

## 贡献
欢迎提出 Issue、Pull Request 以及添加新功能或修复 bug。

---

> **提示**: 若使用代理访问 Claude，请在环境变量中配置 `HTTPS_PROXY` 或 `HTTP_PROXY`。