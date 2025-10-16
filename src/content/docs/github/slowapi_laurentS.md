
---
title: slowapi
---

# SlowAPI 项目

## 项目地址
[GitHub 项目地址](https://github.com/laurentS/slowapi)

## 主要特性
SlowAPI 是一个 Python 库，旨在为 FastAPI 应用提供速率限制（Rate Limiting）功能。它基于 `slowapi` 库构建，支持多种后端存储（如内存、Redis），并与 FastAPI 无缝集成。主要特性包括：
- **灵活的速率限制策略**：支持基于 IP、用户 ID 或自定义键的限制，支持固定窗口、滑动窗口等算法。
- **多种后端支持**：内置内存存储，也可轻松集成 Redis 等外部存储，实现分布式速率限制。
- **FastAPI 集成**：提供装饰器和中间件，便于在路由或全局级别应用速率限制。
- **异常处理**：当超过限制时，返回标准的 HTTP 429 响应，并支持自定义错误消息。
- **异步支持**：完全兼容 FastAPI 的异步特性，确保高性能。
- **易于配置**：通过简单的 API 配置限制规则，如每分钟请求数等。

## 主要功能
- **速率限制应用**：在 API 端点上限制请求频率，防止滥用和 DDoS 攻击。
- **存储管理**：支持临时内存存储或持久化存储，适合不同规模的应用。
- **监控与日志**：内置计数器，可记录请求速率，便于调试和监控。
- **自定义键生成**：允许基于请求头、路径参数等生成唯一键，实现精细控制。
- **全局与局部限制**：支持应用级全局限制或特定路由的局部限制。

## 用法
### 安装
```bash
pip install slowapi
```

### 基本用法示例
1. **初始化 Limiter**：
   ```python
   from slowapi import Limiter
   from slowapi.util import get_remote_address
   from fastapi import FastAPI

   limiter = Limiter(key_func=get_remote_address)  # 使用 IP 作为键
   app = FastAPI()
   app.state.limiter = limiter
   ```

2. **应用到路由**：
   ```python
   from slowapi import _rate_limit_exceeded_handler
   from slowapi.errors import RateLimitExceeded

   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

   @app.get("/")
   @limiter.limit("5/minute")  # 每分钟最多 5 个请求
   async def hello(request: Request):
       return {"message": "Hello World"}
   ```

3. **使用 Redis 后端**：
   ```python
   from slowapi.limiter import Limiter
   import redis.asyncio as redis

   redis_client = redis.from_url("redis://localhost")
   limiter = Limiter(key_func=get_remote_address, storage_uri="redis://localhost")
   ```

更多细节请参考项目 README。