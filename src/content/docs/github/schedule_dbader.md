
---
title: schedule
---

# schedule 项目

**项目地址:** [https://github.com/dbader/schedule](https://github.com/dbader/schedule)

## 主要特性
- **轻量级任务调度库**: schedule 是一个简单易用的 Python 库，用于在应用程序中调度周期性任务，而无需依赖外部任务队列或 cron 等复杂工具。
- **纯 Python 实现**: 无需额外依赖，支持 Python 3.6+，代码简洁，易于理解和扩展。
- **灵活的调度规则**: 支持基于时间间隔、具体日期、星期、时钟时间等多种调度方式。
- **线程安全**: 任务调度在后台线程中运行，不会阻塞主程序。
- **易于测试和调试**: 提供模拟时钟功能，便于单元测试调度逻辑。

## 主要功能
- **定时执行任务**: 可以调度函数在指定时间或间隔后运行，例如每分钟、每天特定时间或星期几执行。
- **支持多种调度器**: 包括每隔 N 秒/分钟/小时/天/周执行、特定日期执行、在工作日执行等。
- **任务管理**: 支持添加、移除、清除任务，以及检查下一个运行时间。
- **事件驱动**: 通过 run_pending() 方法手动检查和运行待执行任务，或使用 run_continuously() 持续运行调度器。
- **自定义时区支持**: 可配置时区，确保跨时区任务调度准确。

## 用法示例
安装库：
```bash
pip install schedule
```

基本用法：
```python
import schedule
import time

def job():
    print("任务执行！")

# 每 10 秒执行一次
schedule.every(10).seconds.do(job)

# 每天上午 9:30 执行
schedule.every().day.at("09:30").do(job)

# 每个工作日（周一到周五）中午 12:00 执行
schedule.every().monday.at("12:00").do(job)

# 运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)
```

高级用法：
- 使用 `schedule.every().minute.do(job)` 每分钟执行。
- 检查下一个运行时间：`next_run = schedule.next_run()`。
- 移除任务：`schedule.clear()` 清空所有任务。

更多细节请参考项目 README 和文档。