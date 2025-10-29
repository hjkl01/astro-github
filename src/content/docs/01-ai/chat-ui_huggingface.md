
---
title: chat-ui
---


# Hugging Face Chat UI

项目地址: https://github.com/huggingface/chat-ui

## 主要特性

- **多模型支持**：可与任意 Hugging Face Hub 上的对话模型配合使用（LLM、Seq2Seq、ChatGLM 等）。
- **实时交互**：WebSocket + SSE 实现低延迟流式回复。
- **多轮对话**：自动管理上下文，支持会话重置与历史记录查看。
- **多语言**：前端支持多语言切换，后端可自定义语言模型。
- **可扩展插件**：通过插件机制可添加自定义功能（如检索增强、工具调用等）。
- **轻量部署**：基于 FastAPI + React，Docker 化，支持单机或多实例部署。

## 核心功能

| 功能 | 说明 |
|------|------|
| **对话接口** | 通过 `/v1/chat/completions` 接口提交用户消息，返回模型回复。 |
| **模型管理** | 在 `config.yaml` 中配置可用模型及其参数；支持动态切换。 |
| **前端 UI** | 响应式聊天窗口，支持滚动加载历史、复制/下载答案、撤回消息。 |
| **安全控制** | 基于 API Key 或 JWT 进行访问控制，支持速率限制。 |
| **日志与监控** | 统一日志记录，支持 Prometheus 指标导出。 |

## 快速使用

### 1. 克隆仓库

```bash
git clone https://github.com/huggingface/chat-ui.git
cd chat-ui
```

### 2. 配置模型

编辑 `config.yaml`，填写 Hugging Face 模型路径或 Hugging Face Hub ID，例如：

```yaml
model_id: "gpt-4o-mini"
base_url: "https://api-inference.huggingface.co/models"
api_key: "YOUR_HF_API_KEY"
```

### 3. 启动服务

```bash
# 直接运行（需要 Python 3.10+）
python -m uvicorn app.main:app --reload
```

或使用 Docker：

```bash
docker build -t chat-ui .
docker run -p 8000:8000 --env HF_TOKEN=YOUR_HF_API_KEY chat-ui
```

### 4. 访问前端

浏览器访问 `http://localhost:8000`，即可使用聊天界面。

### 5. 调用 API

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
     -H "Authorization: Bearer YOUR_HF_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
           "model": "gpt-4o-mini",
           "messages": [
             {"role": "user", "content": "你好，天气怎么样？"}
           ],
           "stream": false
         }'
```

## 进一步扩展

- **自定义插件**：在 `app/plugins` 目录创建插件，按接口规范实现后自动加载。  
- **多实例部署**：使用 `docker-compose` 或 Kubernetes 部署多实例，配合 Nginx 负载均衡。  
- **前端主题**：在 `src/components` 处替换 CSS 或使用 Tailwind 进行主题定制。

---

> 以上即为 Hugging Face Chat UI 的核心特性与使用方法。祝开发愉快！