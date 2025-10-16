
---
title: structlog
---

# structlog 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/hynek/structlog)

## 主要特性
structlog 是一个 Python 日志库，旨在提供结构化日志记录功能。它基于标准 Python 日志模块（logging），但增强了日志的结构化和可读性。主要特性包括：
- **结构化日志**：允许将日志消息以键值对形式记录，便于后续解析和分析，而不是传统的纯文本日志。
- **上下文管理**：支持日志上下文的自动绑定（如请求 ID、用户 ID），确保日志在分布式系统中保持一致性。
- **高性能**：使用高效的日志处理器，减少序列化和格式化的开销，支持异步日志。
- **可扩展性**：模块化设计，支持自定义处理器（如 JSON 格式化、控制台彩色输出），并与第三方库（如 Twisted、asyncio）集成。
- **兼容性**：完全兼容标准 logging 模块，无需修改现有代码即可逐步迁移。
- **无外部依赖**：核心功能不依赖第三方库，安装简单（pip install structlog）。

## 主要功能
- **日志绑定**：通过 `bind()` 方法为日志记录器添加上下文数据，例如：
  ```python
  import structlog
  logger = structlog.get_logger()
  logger = logger.bind(user="alice", action="login")
  ```
- **日志级别支持**：标准日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL），并支持事件字典格式。
- **处理器链**：自定义日志处理流程，如添加时间戳、过滤敏感信息或输出到文件/控制台。
- **JSON 和人类可读输出**：内置支持 JSON 序列化，便于机器解析；同时提供彩色、格式化的控制台输出。
- **异常处理**：自动捕获和结构化异常信息，包括堆栈跟踪。
- **配置灵活**：通过配置文件或代码动态配置日志行为，支持多输出目标。

## 用法示例
### 基本安装和使用
1. 安装：`pip install structlog`
2. 简单日志记录：
   ```python
   import structlog

   structlog.configure(
       processors=[
           structlog.processors.TimeStamper(fmt="iso"),
           structlog.processors.JSONRenderer()
       ],
       logger_factory=structlog.stdlib.LoggerFactory(),
   )

   logger = structlog.get_logger()
   logger.info("event", key="value", count=42)
   # 输出示例：{"event": "event", "key": "value", "count": 42, "timestamp": "2023-..."}
   ```

### 高级用法：上下文绑定
```python
logger = structlog.get_logger().bind(request_id="req-123")
logger.info("Processing request", status="pending")
logger.error("Request failed", exc_info=True)
```
这会自动在所有日志中包含 `request_id` 字段。

### 配置控制台输出
```python
structlog.configure(
    processors=[
        structlog.dev.ConsoleRenderer(colors=True),
    ],
)
```
输出彩色、易读的结构化日志。

更多细节请参考项目文档：https://www.structlog.org/en/stable/