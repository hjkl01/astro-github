---
title: trio
---

# Trio 项目概述

**项目地址：** [https://github.com/python-trio/trio](https://github.com/python-trio/trio)

## 主要特性
Trio 是一个现代化的 Python 非阻塞异步 I/O 库，旨在提供简单、安全且高效的异步编程体验。其核心特性包括：
- **结构化并发**：通过 Nursery 机制确保所有异步任务正确完成或取消，避免资源泄漏和竞争条件。
- **简化 API**：使用高层次的抽象（如 `trio.run()` 和 `trio.spawn()`），减少 boilerplate 代码，比 asyncio 更易用。
- **取消传播**：内置支持任务取消，确保异步操作可优雅中断。
- **跨平台支持**：兼容 Windows、macOS 和 Linux，支持多种 I/O 操作。
- **测试友好**：提供 Trio 测试工具（如 `trio.testing`），便于编写可靠的异步测试。
- **零依赖**：仅依赖标准库和少量可选依赖，轻量级且易于集成。

Trio 强调正确性和可维护性，适合构建网络服务器、客户端、并发任务等应用。

## 主要功能
Trio 的功能聚焦于异步 I/O 和并发管理：
- **异步 I/O 操作**：支持文件、套接字、子进程、定时器等异步读写（如 `trio.open_file`、`trio.SocketStream`）。
- **任务管理**：通过 `trio.spawn()` 创建子任务，支持等待多个任务（`trio.wait_all`）或任意一个（`trio.wait_any`）。
- **同步原语**：内置异步锁（`trio.Lock`）、事件（`trio.Event`）、通道（`trio.Channel`）等，用于任务间通信和同步。
- **网络功能**：简化 TCP/UDP 连接、HTTP 客户端等（如与 `trio-websockets` 集成）。
- **超时和重试**：`trio.move_on_after()` 和 `trio.retry()` 等工具处理超时和错误重试。
- **低层次支持**：可选集成其他库，如 `trio-asyncio` 用于与 asyncio 兼容。

Trio 不直接处理事件循环，而是通过 `trio.run()` 启动和管理整个异步程序。

## 用法示例
安装 Trio：`pip install trio`

### 基本用法
```python
import trio

async def child_task(name):
    print(f"{name} 开始")
    await trio.sleep(1)
    print(f"{name} 完成")

async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child_task, "任务1")
        nursery.start_soon(child_task, "任务2")
    print("所有任务完成")

trio.run(main)
```
此示例演示了使用 Nursery 启动子任务，并等待它们完成。

### 网络示例
```python
import trio

async def fetch_url(url):
    async with trio.open_tcp_stream("example.com", 80) as stream:
        # 发送 HTTP 请求并读取响应
        await stream.send_all(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        data = await stream.receive_some(1024)
        print(data)

trio.run(fetch_url, "http://example.com")
```
Trio 通过简单流接口处理网络 I/O。

更多细节请参考官方文档：https://trio.readthedocs.io/