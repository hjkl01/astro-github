---
title: kombu
---

# Kombu 项目

**项目地址:** [https://github.com/celery/kombu](https://github.com/celery/kombu)

## 主要特性
Kombu 是一个 Python 消息传递库，用于构建异步和分布式任务处理系统。它是 Celery 的核心依赖，支持多种消息代理（如 RabbitMQ、Redis、Amazon SQS 等），提供高性能的序列化、路由和连接管理。Kombu 强调简单性、可扩展性和可靠性，支持 AMQP 协议的实现，并允许自定义扩展。

## 主要功能
- **消息代理支持**: 兼容多种后端，包括 RabbitMQ、Redis、SQS、Apache ActiveMQ 等，实现统一的 API 接口。
- **生产者和消费者**: 支持消息的生产（发送）和消费（接收），包括队列声明、绑定和路由键配置。
- **序列化与反序列化**: 内置 JSON、Pickle 等序列化器，支持自定义格式，确保消息在不同系统间的兼容。
- **连接管理和池化**: 提供连接池、自动重连和心跳机制，提高系统的稳定性和性能。
- **异步支持**: 与 gevent、eventlet 等异步框架集成，支持非阻塞 I/O 操作。
- **错误处理和重试**: 内置异常处理、死信队列和重试逻辑，适用于分布式环境。
- **监控与调试**: 提供日志记录、事件追踪和虚拟主机支持，便于运维和调试。

## 用法示例
Kombu 的用法简单，通过建立连接、创建生产者/消费者来处理消息。以下是基本示例（需安装 Kombu: `pip install kombu`）：

### 基本连接和发送消息
```python
from kombu import Connection, Producer, Queue

# 连接 RabbitMQ
with Connection('amqp://guest:guest@localhost:5672//') as connection:
    producer = Producer(connection)
    producer.publish('Hello, Kombu!', exchange='', routing_key='test_queue')

# 声明队列
queue = Queue('test_queue')
```

### 消费消息
```python
from kombu import Consumer

def callback(body, message):
    print(body)
    message.ack()

with Connection('amqp://guest:guest@localhost:5672//') as connection:
    with Consumer(connection, queues='test_queue', callbacks=[callback]):
        connection.drain_events()
```

更多用法请参考官方文档：https://kombu.readthedocs.io/。Kombu 常与 Celery 结合使用，实现分布式任务队列。