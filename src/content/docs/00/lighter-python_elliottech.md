
---
title: lighter-python
---

# lighter-python（elliottech）

> 项目地址: <https://github.com/elliottech/lighter-python>

Lightweight Python SDK 用于与 **Lighter Cloud** 的 RESTful/WS 接口交互。它通过简洁的 API、自动重试、异步支持以及丰富的错误处理，让开发者可以快速构建与设备、事件、配置管理相关的业务流程。

---

## ✨ 主要特性

| 特性 | 描述 |
|------|------|
| **简洁直观的接口** | 只需几行代码即可完成验证、设备 CRUD、事件订阅等操作。 |
| **同步/异步双模式** | 内置 `asyncio` 支持，按需选择 `sync` 或 `async` 调用。 |
| **自动重试 & 请求限流** | 对网络异常自动重试，支持自定义重试策略，避免瞬时流量激增导致服务拒绝。 |
| **统一错误处理** | 抛可辨识的错误类型（`AuthenticationError`、`NotFoundError` 等）并提供友好提示。 |
| **日志与监控** | 默认集成 `logging`，可自定义日志级别与格式，支持链路跟踪。 |
| **易于配置** | 通过环境变量或显式参数加载 `api_token`、`base_url` 等配置信息。 |
| **兼容性好** | 只依赖 `requests`（同步）/`httpx`（异步），最低 Python 3.8。 |

---

## 📦 安装

```bash
pip install lighter-python
```

或直接从源码安装：

```bash
git clone https://github.com/elliottech/lighter-python.git
cd lighter-python
pip install .
```

---

## 🚀 快速上手

### 1. 同步模式

```python
from lighter import LighterClient

# 通过环境变量读取 token，或显式传递
client = LighterClient()

# 获取设备列表
devices = client.list_devices()
print(devices)

# 读取单个设备信息
device = client.get_device("device-id-123")
print(device)

# 发送事件
client.publish_event(device_id="device-id-123", event="temperature", data={"value": 22.5})
```

### 2. 异步模式

```python
import asyncio
from lighter import AsyncLighterClient

async def main():
    async with AsyncLighterClient() as client:
        devices = await client.list_devices()
        print(devices)

        await client.publish_event(
            device_id="device-id-123",
            event="humidity",
            data={"value": 55}
        )

asyncio.run(main())
```

---

## 📚 主要 API 参考

| 方法 | 说明 | 备注 |
|------|------|------|
| `list_devices()` / `list_devices_async()` | 获取所有设备列表 | 支持分页 |
| `get_device(device_id)` | 查询单个设备 | 返回 `Device` 对象 |
| `create_device(name, *args)` | 创建新设备 | 捕获 `ConflictError` |
| `update_device(device_id, **kwargs)` | 更新设备信息 | 精细字段更新 |
| `delete_device(device_id)` | 删除设备 | 确认删除后再执行 |
| `publish_event(device_id, event, data)` | 事件上报 | 支持批量事件 |
| `subscribe_events(callback, **filters)` | 订阅实时事件 | 通过 WebSocket 实现 |
| `set_config(device_id, config)` | 设置设备配置 | 自动序列化 |
| `get_config(device_id)` | 获取设备配置 | 解析为 `dict` |

> 所有异步方法均以 `async_` 或 `_async` 结尾，适配协程调用。

---

## 🛠️ 配置与环境

- **API Token**：使用 `LIGHTER_API_TOKEN` 环境变量或在客户端构造器中显式传递。
- **Base URL**：默认 `https://api.lighter.com`，可通过 `LIGHTER_BASE_URL` 或参数 `base_url` 指定（用于测试环境）。
- **重试策略**：`retry_max`（最大重试次数），`retry_backoff`（指数回退时间，单位秒）可自定义。
- **日志**：将 `LIGHTER_LOG_LEVEL` 设置为 `DEBUG`、`INFO` 等，可在 import 后配置。

```python
import os
os.environ["LIGHTER_LOG_LEVEL"] = "DEBUG"
```

---

## 📦 贡献与支持

- 上行 PR：欢迎提交功能改进和 bug 修复。
- issue：请详细描述重现步骤或错误信息。
- 文档：保持 README 与代码注释同步。

---

**项目地址**: [https://github.com/elliottech/lighter-python](https://github.com/elliottech/lighter-python)