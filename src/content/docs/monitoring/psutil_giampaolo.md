
---
title: psutil
---

# psutil 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/giampaolo/psutil)

## 主要特性
psutil（Python system and process utilities）是一个跨平台的Python库，用于检索有关运行系统进程和资源利用率（CPU、内存、磁盘、网络等）的信息。它是一个纯Python库，支持Python 2.6、2.7和3.x版本。主要特性包括：
- **跨平台支持**：兼容Linux、Windows、macOS、FreeBSD、OpenBSD以及Sun Solaris等操作系统。
- **进程管理**：提供详细的进程信息检索，如进程ID、状态、CPU使用率、内存使用、打开的文件和线程等。
- **系统监控**：实时监控系统整体资源，包括CPU负载、内存使用、磁盘I/O、网络I/O和传感器温度。
- **轻量级和高效**：纯Python实现，依赖少量系统调用，性能高效，适用于脚本、监控工具和系统管理应用。
- **易于扩展**：支持自定义传感器和插件，社区活跃，常用于DevOps、性能分析和自动化脚本。

## 主要功能
psutil的核心功能围绕进程和系统资源监控展开：
- **进程功能**：
  - 获取进程列表：`psutil.process_iter()` 返回所有进程迭代器。
  - 进程信息：通过`psutil.Process(pid)` 获取单个进程的属性，如`name()`（进程名）、`cpu_percent()`（CPU使用率）、`memory_info()`（内存信息）和`connections()`（网络连接）。
  - 进程控制：支持终止进程`terminate()`、杀死进程`kill()` 和设置进程优先级。
- **系统功能**：
  - CPU监控：`psutil.cpu_percent()` 获取系统CPU使用率，`psutil.cpu_times()` 获取详细CPU时间统计。
  - 内存监控：`psutil.virtual_memory()` 返回内存使用详情，包括总内存、可用内存和使用百分比。
  - 磁盘监控：`psutil.disk_usage(path)` 获取磁盘使用情况，`psutil.disk_io_counters()` 监控I/O活动。
  - 网络监控：`psutil.net_io_counters()` 获取网络I/O统计，`psutil.net_connections()` 列出网络连接。
  - 用户和环境：`psutil.users()` 获取登录用户，`psutil.boot_time()` 获取系统启动时间。
- **其他功能**：支持传感器读取（如温度）、电池状态和环境变量管理。

## 用法示例
安装psutil：使用pip安装 `pip install psutil`。

### 基本用法
```python
import psutil

# 获取系统CPU使用率
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU使用率: {cpu_percent}%")

# 获取当前进程信息
current_process = psutil.Process()
print(f"进程名: {current_process.name()}")
print(f"内存使用: {current_process.memory_info().rss / 1024 / 1024:.2f} MB")

# 迭代所有进程
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try:
        print(f"PID: {proc.info['pid']}, 名称: {proc.info['name']}, CPU: {proc.info['cpu_percent']}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# 系统内存信息
memory = psutil.virtual_memory()
print(f"总内存: {memory.total / (1024**3):.2f} GB, 使用率: {memory.percent}%")
```

psutil适合用于系统监控脚本、性能基准测试和资源管理工具。通过其API，可以轻松构建自定义监控解决方案。更多细节请参考官方文档。