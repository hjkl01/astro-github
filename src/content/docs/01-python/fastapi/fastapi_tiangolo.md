---
title: fastapi
---

## 功能介绍

FastAPI 是一个现代、快速（高性能）的 Web 框架，用于使用 Python 构建 API。它基于标准的 Python 类型提示。

### 主要特性

- **快速**：非常高的性能，与 NodeJS 和 Go 相当（感谢 Starlette 和 Pydantic）。这是最快的 Python 框架之一。
- **快速编码**：将开发功能的速度提高 200% 到 300%。\*
- **更少错误**：减少约 40% 的人为（开发者）错误。\*
- **直观**：出色的编辑器支持。处处都有补全。更少调试时间。
- **简单**：设计易于使用和学习。更少阅读文档的时间。
- **简短**：最小化代码重复。从每个参数声明中获得多个功能。更少错误。
- **健壮**：获得生产就绪的代码。具有自动交互式文档。
- **基于标准**：基于（并完全兼容）API 的开放标准：OpenAPI（以前称为 Swagger）和 JSON Schema。

\* 基于内部开发团队测试的估计，在构建生产应用程序时。

## 安装

创建一个虚拟环境并激活，然后安装 FastAPI：

```bash
pip install "fastapi[standard]"
```

注意：确保将 `"fastapi[standard]"` 放在引号中，以确保在所有终端中正常工作。

## 用法示例

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

使用以下命令运行服务器：

```bash
fastapi dev main.py
```

这将启动开发服务器，默认情况下启用自动重载以进行本地开发。

### 检查 API

打开浏览器访问 http://127.0.0.1:8000/items/5?q=somequery，您将看到 JSON 响应。

### 交互式 API 文档

访问 http://127.0.0.1:8000/docs 查看自动交互式 API 文档（由 Swagger UI 提供）。

或者访问 http://127.0.0.1:8000/redoc 查看替代文档（由 ReDoc 提供）。

## 高级示例

修改 `main.py` 以接收 PUT 请求的主体：

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

现在，API 文档将自动更新以反映新的参数和主体。

## 性能

独立的 TechEmpower 基准测试显示，在 Uvicorn 下运行的 FastAPI 应用程序是[最快的 Python 框架之一](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)，仅次于 Starlette 和 Uvicorn 本身（FastAPI 内部使用）。

## 依赖

FastAPI 依赖于 Pydantic 和 Starlette。

### 标准依赖

当您使用 `pip install "fastapi[standard]"` 安装 FastAPI 时，它带有标准可选依赖组：

- `uvicorn`：用于加载和服务的服务器。
- `fastapi-cli[standard]`：提供 `fastapi` 命令。

## 许可证

该项目根据 MIT 许可证的条款获得许可。
