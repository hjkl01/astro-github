---
title: fastapi-cache
---

# FastAPI-Cache 项目

## 项目地址
[https://github.com/long2ice/fastapi-cache](https://github.com/long2ice/fastapi-cache)

## 主要特性
- **简单易用**：提供简洁的装饰器和依赖注入方式，支持一键缓存 FastAPI 路由和函数结果。
- **多存储后端支持**：兼容 Redis、Memcached、文件系统等多种缓存后端，便于在不同环境中部署。
- **灵活配置**：支持自定义缓存键生成、过期时间、序列化方式，以及缓存失效机制。
- **异步支持**：完全兼容 FastAPI 的异步特性，确保高性能和非阻塞操作。
- **轻量级**：基于 FastAPI 生态，无需额外依赖，易于集成到现有项目中。

## 主要功能
- **路由缓存**：通过 `@cache` 装饰器自动缓存 HTTP 响应，支持 GET、POST 等方法。
- **函数缓存**：使用 `cache` 依赖注入或装饰器缓存任意函数的返回值。
- **缓存管理**：提供清除缓存、设置 TTL（生存时间）、键值查询等操作。
- **序列化/反序列化**：内置 JSON 支持，可扩展自定义序列化器处理复杂数据。
- **集成监控**：可选集成日志和指标，监控缓存命中率和性能。

## 用法示例
### 安装
```bash
pip install fastapi-cache2[redis]  # 以 Redis 为例
```

### 基本配置
在 FastAPI 应用中初始化：
```python
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
```

### 路由缓存
```python
@app.get("/items/{item_id}")
@cache(expire=60)  # 缓存 60 秒
async def get_item(item_id: int):
    return {"item_id": item_id, "data": "expensive_operation"}
```

### 函数缓存（依赖注入）
```python
from fastapi_cache.decorator import cache

@cache(expire=300)
async def expensive_function(key: str):
    # 模拟耗时操作
    return f"Result for {key}"
```

### 清除缓存
```python
from fastapi_cache import FastAPICache

@app.post("/clear-cache")
async def clear_cache():
    await FastAPICache.clear()
    return {"message": "Cache cleared"}
```

更多细节请参考项目文档和示例代码。