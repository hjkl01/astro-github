---
title: grequests
---

# grequests 项目

**项目地址:** [https://github.com/spyoungtech/grequests](https://github.com/spyoungtech/grequests)

## 主要特性
grequests 是一个基于 Python 的异步 HTTP 请求库，它是 gevent 和 requests 的结合体。主要特性包括：
- **异步请求处理**：利用 gevent 的绿色线程实现高并发 HTTP 请求，支持同时发送多个请求而无需阻塞，提高效率。
- **兼容 requests API**：API 设计与 Python 的 requests 库高度兼容，便于从 requests 迁移到异步模式。
- **轻量级**：无需复杂的配置，即可实现批量请求，适合爬虫、API 测试等场景。
- **支持会话管理**：内置 Session 支持，方便处理 cookies、认证等状态信息。
- **异常处理**：提供内置的错误处理机制，如超时、重试等。

## 主要功能
- **批量发送请求**：支持 GET、POST、PUT、DELETE 等 HTTP 方法的异步执行。
- **事件驱动**：通过 gevent 的协程机制，实现非阻塞 I/O 操作。
- **结果收集**：可轻松获取所有请求的响应结果，支持回调函数处理。
- **集成 gevent 池**：使用线程池或事件循环管理并发请求数量，避免资源耗尽。

## 用法示例
安装依赖：`pip install grequests`

### 基本用法
```python
import grequests

# 创建多个异步请求
urls = ['http://httpbin.org/html', 'http://httpbin.org/html', 'http://httpbin.org/html']
requests = [grequests.get(url) for url in urls]

# 发送请求并等待结果
responses = grequests.map(requests)

# 处理响应
for response in responses:
    print(response.text[:100])  # 输出前100字符
```

### 使用 Session
```python
import grequests

session = grequests.Session()
urls = ['http://httpbin.org/get', 'http://httpbin.org/post']
requests = [session.get(url) for url in urls]
responses = grequests.map(requests, size=10)  # 并发大小为10
```

### 带回调的用法
```python
import grequests

def exception_handler(request, exception):
    print(f"请求失败: {exception}")

urls = ['http://httpbin.org/get', 'http://nonexistent-site.com']
requests = (grequests.get(u, hooks={'response': print('成功')} ) for u in urls)
responses = grequests.map(requests, exception_handler=exception_handler)
```

更多详情请参考项目 README。