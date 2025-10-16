
---
title: rq
---

# rq 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/rq/rq)

## 主要特性
rq 是一个轻量级的 Python 任务队列库，基于 Redis 实现。它具有以下主要特性：
- **简单易用**：无需复杂配置，即可快速集成到 Python 项目中，支持异步任务执行。
- **分布式支持**：利用 Redis 作为后端，支持多 worker 进程和多机器分布式任务处理。
- **任务持久化**：任务结果自动存储在 Redis 中，支持任务重试、失败处理和结果检索。
- **灵活调度**：支持延迟任务、定时任务和依赖任务。
- **高性能**：基于 gevent 或标准线程模型，实现高效的并发任务执行。
- **监控与日志**：内置任务监控工具和日志记录，便于调试和运维。

## 主要功能
- **任务队列管理**：创建、添加、执行和管理任务队列。
- **Worker 进程**：启动 worker 进程来消费和执行队列中的任务。
- **结果存储**：任务执行结果持久化，支持查询和过期机制。
- **异常处理**：自动重试失败任务，并支持自定义异常处理器。
- **CLI 工具**：提供命令行接口，用于队列监控、worker 管理和任务调度。

## 用法
### 安装
使用 pip 安装：
```
pip install rq
```

### 基本用法示例
1. **添加任务**：
   ```python
   from rq import Queue
   from redis import Redis

   redis_conn = Redis()
   q = Queue(connection=redis_conn)

   def hello(name):
       return f"Hello {name}!"

   job = q.enqueue(hello, "World")  # 添加任务到默认队列
   ```

2. **启动 Worker**：
   在终端运行：
   ```
   rq worker
   ```
   这将启动一个 worker 进程来执行队列中的任务。

3. **获取结果**：
   ```python
   result = job.result  # 获取任务结果
   print(result)  # 输出: Hello World!
   ```

4. **高级用法**：
   - 指定队列：`q = Queue('high', connection=redis_conn)`
   - 延迟任务：`q.enqueue_in(timedelta(minutes=5), hello, "Delayed")`
   - 更多细节请参考 [官方文档](https://python-rq.org/)。