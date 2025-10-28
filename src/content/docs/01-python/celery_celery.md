
---
title: celery
---

# Celery 项目

**GitHub 项目地址:** [https://github.com/celery/celery](https://github.com/celery/celery)

## 主要特性
Celery 是一个开源的分布式任务队列系统，专为 Python 设计。它支持异步任务处理、分布式执行和高可用性。主要特性包括：
- **异步任务执行**：允许将耗时任务从主程序中分离出来，后台异步运行，提高应用响应速度。
- **分布式支持**：可以跨多台机器和多个进程/线程执行任务，支持水平扩展。
- **多种消息代理**：兼容 RabbitMQ、Redis、Amazon SQS 等作为消息 broker。
- **结果存储**：支持将任务结果持久化到数据库、缓存或文件系统中。
- **监控与管理**：内置 Flower 工具用于实时监控任务状态、性能和错误。
- **定时任务**：类似于 cron 的调度功能，支持周期性任务执行。
- **错误处理与重试**：自动重试失败任务，支持自定义重试策略。
- **高性能**：基于事件驱动架构，支持 gevent 和 eventlet 等并发模型。

## 主要功能
Celery 的核心功能围绕任务队列展开：
- **任务定义**：使用装饰器（如 `@app.task`）将 Python 函数定义为可分发任务。
- **任务调度**：通过 `delay()` 或 `apply_async()` 方法异步调用任务，支持参数传递、延迟执行和优先级设置。
- **工作进程管理**：启动 worker 进程（`celery -A tasks worker`）来消费和执行队列中的任务。
- **任务链与组合**：支持任务链（chord）、组（group）和画布（canvas）来构建复杂工作流。
- **信号与事件**：提供任务事件钩子，用于日志记录、审计或外部集成。
- **安全机制**：支持任务签名和访问控制，防止未授权执行。

## 用法
### 安装
```bash
pip install celery
# 对于 Redis broker
pip install celery[redis]
# 对于 RabbitMQ broker
pip install celery[librabbitmq]
```

### 基本用法示例
1. **创建 Celery 应用**：
   ```python
   from celery import Celery

   app = Celery('tasks', broker='redis://localhost:6379/0')
   ```

2. **定义任务**：
   ```python
   @app.task
   def add(x, y):
       return x + y
   ```

3. **调用任务**：
   ```python
   result = add.delay(4, 5)  # 异步调用
   print(result.get())  # 获取结果（阻塞）
   ```

4. **启动 Worker**：
   ```bash
   celery -A tasks worker --loglevel=info
   ```

5. **启动调度器（Beat）**（用于定时任务）：
   ```bash
   celery -A tasks beat --loglevel=info
   ```

更多高级用法请参考官方文档：http://docs.celeryproject.org/。