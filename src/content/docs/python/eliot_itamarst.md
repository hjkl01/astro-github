---
title: eliot
---

# Eliot 项目

**GitHub 项目地址:** [https://github.com/itamarst/eliot](https://github.com/itamarst/eliot)

## 主要特性
Eliot 是一个 Python 日志记录库，专注于结构化日志输出和可观测性。它不是传统的日志系统，而是强调事件驱动的日志记录，帮助开发者追踪分布式系统中的因果关系和调试复杂问题。主要特性包括：
- **结构化日志**：所有日志条目都是 JSON 格式的结构化数据，便于解析和分析。
- **因果追踪**：支持任务（Task）和动作（Action）的概念，自动记录事件的层次结构和时间序列，便于重现问题流程。
- **分布式系统支持**：设计用于微服务或异步应用，能处理跨进程或跨机器的日志关联。
- **低开销**：最小化日志记录的性能影响，支持异步写入。
- **可扩展性**：易于集成到现有 Python 项目中，支持自定义处理器和输出格式。

## 主要功能
- **事件记录**：通过 `eliot.log_call` 等装饰器记录函数调用和返回值，支持参数和异常的自动捕获。
- **任务管理**：每个任务有唯一 ID，可嵌套子任务，实现日志的树状结构。
- **输出处理器**：内置文件、控制台和网络处理器，支持将日志发送到外部系统如 ELK Stack。
- **搜索与分析**：生成的日志易于使用工具如 jq 或 Elasticsearch 查询。
- **测试支持**：提供测试工具来验证日志输出，而不依赖实际 I/O。

## 用法
### 安装
```bash
pip install eliot
```

### 基本用法示例
1. **简单日志记录**：
   ```python
   from eliot import MessageLog
   logger = MessageLog().writer()

   logger.message("user.login", {"user_id": 123})
   ```

2. **结构化函数调用**：
   ```python
   from eliot import log_call

   @log_call
   def process_user(user_id):
       # 函数逻辑
       return {"status": "success"}

   # 调用时自动记录输入/输出
   result = process_user(123)
   ```

3. **任务上下文**：
   ```python
   from eliot import start_task

   with start_task(logger, "app.startup"):
       # 在任务上下文中记录子事件
       logger.message("init.db", {"db": "postgres"})
   ```

4. **配置输出**：
   ```python
   from eliot import FileWriter, TreeLogger

   tree = TreeLogger()
   writer = FileWriter("app.log")
   tree.add_writer(writer)

   # 使用 tree 作为 logger
   tree.message("event", {"key": "value"})
   ```

更多细节请参考项目文档和示例代码。Eliot 适合需要高可观测性的 Python 应用开发。