
---
title: apscheduler
---

# APScheduler 项目

## 项目地址
[https://github.com/agronholm/apscheduler](https://github.com/agronholm/apscheduler)

## 主要特性
APScheduler (Advanced Python Scheduler) 是一个 Python 库，用于在后台调度任务。它支持多种调度方式，包括基于日期、间隔或 cron 表达式，类似于 Unix 的 cron 服务，但可以完全在 Python 应用中运行。主要特性包括：
- **多种调度器**：支持阻塞式（BlockingScheduler）、后台（BackgroundScheduler）和异步（AsyncIOScheduler）等调度器类型。
- **任务存储**：可将任务持久化到数据库（如 SQLAlchemy、MongoDB）或文件（JSON、YAML），确保任务在重启后恢复。
- **灵活的触发器**：Date（单次日期触发）、Interval（固定间隔）、Cron（cron 表达式）和结合触发器（Combined）。
- **线程安全**：多线程环境下可靠运行，支持任务优先级和最大实例限制。
- **插件支持**：集成 Tornado、Twisted 等框架的调度器。
- **轻量级**：纯 Python 实现，无外部依赖（可选依赖如 SQLAlchemy 用于持久化）。

## 主要功能
- **任务调度**：添加、修改、暂停、恢复和删除定时任务。
- **事件监听**：通过事件系统监听任务执行、错误等事件。
- **时区支持**：内置时区处理，支持 UTC 和本地时间。
- **错误处理**：任务执行失败时可配置重试或日志记录。
- **依赖管理**：任务可依赖其他任务，支持链式执行。

## 用法示例
安装：`pip install apscheduler`

### 基本用法（阻塞式调度器）
```python
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def my_job(text):
    print(f"任务执行: {text}，时间: {datetime.now()}")

scheduler = BlockingScheduler()
scheduler.add_job(my_job, 'interval', seconds=5, args=['Hello World'])
scheduler.start()  # 启动调度器，阻塞运行
```

### 后台调度器（非阻塞）
```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(my_job, 'cron', hour=0, minute=0)  # 每天午夜执行
scheduler.start()
# 继续其他代码...
```

### Cron 触发器示例
```python
scheduler.add_job(my_job, 'cron', day_of_week='mon-fri', hour=17, minute=30)  # 工作日17:30执行
```

更多用法请参考官方文档：https://apscheduler.readthedocs.io/