---
title: FastAPI
---

## 功能介绍

FastAPI 是一个现代、高性能的 Web 框架，用于使用 Python 构建 API。它基于标准的 Python 类型提示，提供了快速开发、生产就绪的 API 解决方案。

### 主要特性

- **高性能**：性能与 NodeJS 和 Go 相当，基于 Starlette 和 Pydantic。
- **快速编码**：通过类型提示减少代码重复，提高开发速度。
- **减少错误**：自动数据验证和类型检查，减少开发者错误。
- **直观**：优秀的编辑器支持，包括自动补全和类型检查。
- **易学**：基于标准 Python，无需学习新语法。
- **健壮**：自动生成交互式 API 文档，支持 OpenAPI 和 JSON Schema。
- **基于标准**：完全兼容 OpenAPI 和 JSON Schema 标准。

## 用法

### 安装

```bash
pip install "fastapi[standard]"
```

### 基本示例

创建 `main.py` 文件：

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

```bash
fastapi dev main.py
```

应用将在 `http://127.0.0.1:8000` 启动。

### API 文档

- 交互式文档：`http://127.0.0.1:8000/docs` (Swagger UI)
- 替代文档：`http://127.0.0.1:8000/redoc` (ReDoc)

### 高级用法

支持请求体、查询参数、路径参数、依赖注入、认证等。更多示例请参考官方文档。
