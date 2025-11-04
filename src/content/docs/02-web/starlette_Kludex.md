
---
title: starlette
---


# Kludex/starlette

**项目地址**: https://github.com/Kludex/starlette

## 主要特性

- **ASGI 兼容**：完全基于 ASGI 协议，支持异步请求处理。
- **简单路由**：使用 `Route` 或 `APIRouter` 定义路由，支持路径参数、查询参数、请求体解析。
- **中间件支持**：内置 `CORSMiddleware`、`GZipMiddleware`、`HTTPSRedirectMiddleware` 等常用中间件，也可自定义。
- **多种响应类型**：提供 `JSONResponse`、`HTMLResponse`、`PlainTextResponse`、`RedirectResponse` 等响应类。
- **静态文件**：`StaticFiles` 组件可直接提供静态资源服务。
- **错误处理**：自定义异常处理器，支持统一返回错误信息。
- **依赖注入**：通过 `Depends` 实现轻量级依赖注入。

## 核心功能

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse

async def hello(request):
    return JSONResponse({"message": "Hello, world!"})

app = Starlette(
    debug=True,
    routes=[
        Route("/hello", hello, methods=["GET"]),
    ],
)
```

- **应用实例**：`Starlette` 类是核心应用对象，负责路由匹配、请求分发。
- **路由**：`Route` 类用于声明单一路由；`APIRouter` 可以批量注册路由并分组。
- **请求解析**：`Request` 对象提供 `json()`、`form()`、`query_params` 等方法。
- **中间件**：使用 `app.add_middleware(MiddlewareClass, **options)` 添加中间件。
- **静态文件**：`app.mount("/static", StaticFiles(directory="static"))`。

## 快速使用

1. **安装**

```bash
pip install kludex-starlette
```

2. **创建应用**

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse

async def homepage(request):
    return PlainTextResponse("Welcome to Kludex Starlette!")

app = Starlette(debug=True, routes=[Route("/", homepage)])
```

3. **运行**

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

4. **使用中间件**

```python
from starlette.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

5. **静态文件服务**

```python
from starlette.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
```

6. **错误处理**

```python
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)
```

## 文档与支持

- 官方文档：提供完整的 API 说明、路由配置、响应、异常处理等章节。
- 社区支持：GitHub Issues、Pull Requests 用于功能请求与 Bug 修复。

> 以上内容基于 Kludex/starlette 项目的核心特性与常用用法，适合快速搭建异步 Web 服务。