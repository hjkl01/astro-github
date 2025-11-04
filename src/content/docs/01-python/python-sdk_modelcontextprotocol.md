
---
title: python-sdk
---

以下为 **Python SDK for ModelContextProtocol** 的中文说明，已以 Markdown 格式整理，可直接保存至 `src/content/docs/00/python-sdk_modelcontextprotocol.md`。

```markdown
# Python SDK for ModelContextProtocol

> 项目地址: <https://github.com/modelcontextprotocol/python-sdk>

---

## 1. 简介

`python-sdk` 是 ModelContextProtocol 的官方 Python SDK，旨在帮助开发者轻松与 ModelContextProtocol (MCP) 进行交互。该 SDK 提供统一的客户端接口，封装了请求构造、身份认证、错误处理等细节，使开发者能够专注于业务逻辑。

---

## 2. 安装

```bash
pip install modelcontextprotocol-sdk
```

> **Tip:**  
> - 如果你使用的是 `pipenv` 或 `poetry`，请相应使用 `pipenv install modelcontextprotocol-sdk` 或 `poetry add modelcontextprotocol-sdk`。

---

## 3. 主要特性

| 特性 | 说明 |
|------|------|
| **统一的客户端接口** | `MCPClient` 提供了 `create_context`, `send_request`, `stream_response` 等方法。 |
| **自动身份认证** | 支持 API Key、OAuth2、JWT 等多种认证方式。 |
| **错误处理与重试** | 内置异常层次结构，可在异常中获取 HTTP 状态码与错误信息。支持指数退避重试。 |
| **流式响应** | 通过 `stream_response` 可按需逐步获取大数据或实时推理结果。 |
| **多语言支持** | SDK 内部使用 `httpx`，可在异步和同步两种模式下运行。 |
| **类型安全** | 通过 `pydantic` 定义请求/响应模型，保证数据结构一致。 |

---

## 4. 基本用法

### 4.1 初始化客户端

```python
from modelcontextprotocol import MCPClient

client = MCPClient(
    api_key="YOUR_API_KEY",
    base_url="https://api.modelcontextprotocol.com"
)
```

### 4.2 创建上下文（Context）

```python
context = client.create_context(
    name="my-first-context",
    description="示例上下文",
    data={
        "prompt": "Hello, world!",
        "parameters": {"temperature": 0.7}
    }
)
```

### 4.3 发送推理请求

```python
response = client.send_request(
    context_id=context.id,
    payload={
        "input_text": "请帮我写一段 Python 代码"
    }
)

print("Response:", response.text)
```

### 4.4 流式获取响应

```python
for chunk in client.stream_response(
    context_id=context.id,
    payload={"input_text": "长文本生成示例"}
):
    print(chunk, end="", flush=True)
```

### 4.5 异步使用

```python
import asyncio
from modelcontextprotocol import AsyncMCPClient

async def main():
    async_client = AsyncMCPClient(
        api_key="YOUR_API_KEY",
        base_url="https://api.modelcontextprotocol.com"
    )
    context = await async_client.create_context(
        name="async-context",
        data={"prompt": "async test"}
    )
    resp = await async_client.send_request(
        context_id=context.id,
        payload={"input_text": "异步调用"}
    )
    print(resp.text)

asyncio.run(main())
```

---

## 5. 常见问题（FAQ）

| 题目 | 说明 |
|------|------|
| **如何处理大文件上传？** | 使用 `stream_upload` 或将文件拆分为多块，逐块上传。 |
| **SDK 支持哪些模型？** | 目前支持 `text-davinci`, `image-gen`, `audio-transcribe` 等。详情见文档。 |
| **如果出现 429 或 500 错误怎么办？** | SDK 内置重试策略，若失败会抛出 `MCPError`，可捕获后自行处理。 |

---

## 6. 进一步阅读

- 官方文档: <https://docs.modelcontextprotocol.com/sdk/python>
- 示例代码: <https://github.com/modelcontextprotocol/python-sdk/tree/main/examples>
- 开源协议: MIT

---

> **温馨提示**  
> 本 SDK 仍在快速迭代中，建议关注 GitHub 仓库的更新日志，及时升级以获得最新功能与修复。祝开发愉快！
