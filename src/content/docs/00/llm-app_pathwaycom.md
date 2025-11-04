
---
title: llm-app
---


# Pathway LLM App

**项目地址:** https://github.com/pathwaycom/llm-app

## 主要特性

| 特色 | 说明 |
|------|------|
| 简易聊天界面 | 通过 Streamlit 提供实时交互的前端页面 |
| 多 LLM 支持 | 默认支持 OpenAI（gpt‑3.5‑turbo、gpt‑4 等），可按需切换 |
| 环境变量配置 | 所有关键配置（API Key、模型、端口等）均通过 `.env` 统一管理 |
| Docker 化 | 一键 `docker compose up` 即可完成本地或云端部署 |
| FastAPI 后端 | 提供 `/api/chat` 接口，支持 WebSocket 或 HTTP 请求 |
| 对话记忆 | 使用 LangChain 的 `ConversationBufferMemory` 自动维护上下文 |
| 日志记录 | 所有请求与响应均写入 `logs/llm_app.log`，便于排查 |

## 功能说明

- **后端 API (`src/app.py`)**  
  - `POST /api/chat`：接收 JSON 格式的 `{"message": "用户提问"}`，返回 `{"response": "LLM 回复"}`。  
  - 通过 `config.py` 读取系统提示、模型、温度等参数。  
  - 内置错误处理，返回友好的错误信息。  

- **前端页面 (`src/frontend/main.py`)**  
  - 采用 Streamlit，展示多轮对话。  
  - 支持文件上传（可扩展为文档检索）。  
  - 自动刷新聊天记录，实时显示 LLM 输出。  

- **配置 (`src/config.py`)**  
  - `SYSTEM_PROMPT`: 系统级提示词。  
  - `MODEL`: LLM 模型名称。  
  - `TEMPERATURE`: 采样温度。  
  - `MAX_TOKENS`: 单轮最大 token 数。  

- **日志 (`logs/llm_app.log`)**  
  - 记录每一次请求、响应、异常。  

## 用法

### 1. 克隆仓库

```bash
git clone https://github.com/pathwaycom/llm-app.git
cd llm-app
```

### 2. 配置环境变量

在项目根目录创建 `.env`（示例）：

```dotenv
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXX
LLM_MODEL=gpt-3.5-turbo
PORT=8000
```

> **Tip**：若使用其他 LLM 提供商，只需修改 `LLM_MODEL` 或在 `config.py` 中加入对应参数。

### 3. 本地运行（可选）

```bash
# 安装依赖
pip install -r requirements.txt

# 启动后端
uvicorn src.app:app --reload

# 启动前端（另起一个终端）
streamlit run src/frontend/main.py
```

访问 `http://localhost:8501` 即可使用前端页面。

### 4. Docker 部署

```bash
docker compose up -d
```

- **后端**：`http://localhost:8000/api/chat`  
- **前端**：`http://localhost:8501`

### 5. API 调用示例

```bash
curl -X POST http://localhost:8000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"你好"}'
```

返回：

```json
{
  "response": "你好！有什么可以帮您的吗？"
}
```

### 6. 自定义系统提示

编辑 `src/config.py`：

```python
SYSTEM_PROMPT = "You are a helpful assistant."
```

### 7. 查看日志

日志文件位于 `logs/llm_app.log`，可直接打开或使用 `tail -f` 监控。

---

> 进一步细节请参阅仓库根目录下的 `README.md`。祝使用愉快！
