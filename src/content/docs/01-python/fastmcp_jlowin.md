---
title: fastmcp
---

# fastmcp

## 项目简介

FastMCP 是用于构建 Model Context Protocol (MCP) 服务器和客户端的 Python 框架。它提供了快速、Pythonic 的方式来开发 MCP 应用程序，支持工具、资源、提示等核心概念，并包含企业级认证、部署工具和完整的生态系统。

## 主要功能

- **MCP 服务器构建**：使用装饰器快速定义工具、资源和提示。
- **客户端支持**：提供完整的客户端库，支持多种传输协议（Stdio、SSE、HTTP）。
- **企业级认证**：内置支持 Google、GitHub、Azure、Auth0 等 OAuth 提供商。
- **部署选项**：支持本地运行、FastMCP Cloud 部署或自托管。
- **高级特性**：代理服务器、服务器组合、OpenAPI/FastAPI 集成等。
- **测试和开发工具**：内置测试框架和开发工具。

## 安装

使用 uv 安装（推荐）：

```bash
uv pip install fastmcp
```

或使用 pip：

```bash
pip install fastmcp
```

## 基本用法

### 创建 MCP 服务器

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### 运行服务器

本地运行：

```bash
fastmcp run server.py
```

或在代码中：

```python
mcp.run()  # 默认使用 STDIO 传输
```

### 使用客户端

```python
from fastmcp import Client

async def main():
    async with Client("server.py") as client:
        tools = await client.list_tools()
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result.content[0].text}")
```

## 核心概念

### 工具 (Tools)

允许 LLM 执行动作，通过装饰 Python 函数实现：

```python
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b
```

### 资源 (Resources)

暴露只读数据源：

```python
@mcp.resource("config://version")
def get_version():
    return "2.0.1"
```

### 提示 (Prompts)

定义可重用的消息模板：

```python
@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"
```

### 上下文 (Context)

在函数中访问会话能力：

```python
from fastmcp import Context

@mcp.tool
async def process_data(uri: str, ctx: Context):
    await ctx.info(f"Processing {uri}...")
    data = await ctx.read_resource(uri)
    summary = await ctx.sample(f"Summarize: {data.content[:500]}")
    return summary.text
```

## 认证

添加企业级认证只需几行代码：

```python
from fastmcp.server.auth.providers.google import GoogleProvider

auth = GoogleProvider(client_id="...", client_secret="...", base_url="https://myserver.com")
mcp = FastMCP("Protected Server", auth=auth)
```

## 部署

- **开发**：`fastmcp run server.py`
- **生产**：部署到 [FastMCP Cloud](https://fastmcp.cloud)
- **自托管**：`mcp.run(transport="http", host="0.0.0.0", port=8000)`

## 更多信息

完整文档：https://gofastmcp.com

社区：https://discord.gg/uu8dJCgttd
