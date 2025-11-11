---
title: FastAPI
---

## 功能介绍

FastAPI 是一个现代、快速（高性能）的 Web 框架，用于使用 Python 构建 API。它基于标准的 Python 类型提示。

### 主要特性

- **快速**：非常高性能，与 NodeJS 和 Go 相当（感谢 Starlette 和 Pydantic）。
- **快速编码**：将开发功能的速度提高约 200% 到 300%。
- **更少错误**：减少约 40% 的开发者（人类）诱发错误。
- **直观**：优秀的编辑器支持，到处都有补全。调试时间更少。
- **易用**：设计为易于使用和学习。阅读文档的时间更少。
- **简短**：最小化代码重复。从每个参数声明中获得多个功能。更少错误。
- **健壮**：获得生产就绪代码。具有自动交互式文档。
- **基于标准**：基于（并完全兼容）API 的开放标准：OpenAPI（以前称为 Swagger）和 JSON Schema。

## 安装

创建一个虚拟环境并激活，然后安装 FastAPI：

```bash
pip install "fastapi[standard]"
```

## 基本用法

### 创建应用

创建一个文件 `main.py`：

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

### 运行应用

运行服务器：

```bash
fastapi dev main.py
```

服务器将在 http://127.0.0.1:8000 启动。

### 访问 API

- 打开浏览器访问 http://127.0.0.1:8000/items/5?q=somequery 查看 JSON 响应。
- 访问 http://127.0.0.1:8000/docs 查看交互式 API 文档（Swagger UI）。
- 访问 http://127.0.0.1:8000/redoc 查看替代文档（ReDoc）。

### 高级示例

使用 Pydantic 模型处理请求体：

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

FastAPI 会自动验证数据、生成文档，并提供类型检查和补全支持。
