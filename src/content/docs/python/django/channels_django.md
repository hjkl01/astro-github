---
title: channels
---

# Django Channels 项目

## 项目地址
[GitHub 项目地址](https://github.com/django/channels)

## 主要特性
Django Channels 是 Django 的扩展框架，主要用于处理 WebSocket、HTTP2 和其他异步协议。它将 Django 的 HTTP 处理能力扩展到异步领域，支持实时应用开发。核心特性包括：
- **WebSocket 支持**：允许服务器主动向客户端推送数据，实现实时通信，如聊天室或通知系统。
- **异步消费者**：使用 ASGI（Asynchronous Server Gateway Interface）标准，支持异步视图和消费者，取代传统的 WSGI。
- **协议路由**：通过路由系统处理不同协议的请求，例如 WebSocket、HTTP 等。
- **与 Django 集成**：无缝集成 Django 的模型、认证和 ORM，无需重写现有代码。
- **后台任务**：支持异步任务队列和后台处理，提高性能。
- **多协议支持**：处理 HTTP、WebSocket 和自定义协议。

## 主要功能
- **实时通信**：构建聊天应用、股票报价或协作工具，支持双向通信。
- **长连接管理**：自动处理连接断开、重连和心跳机制。
- **分层架构**：包括应用层（消费者）、协议层（路由）和传输层（服务器），便于扩展。
- **数据库集成**：结合 Django Channels 的 Redis 支持，实现跨进程通信。
- **测试支持**：提供异步测试工具，模拟 WebSocket 连接。

## 用法
### 安装
1. 通过 pip 安装：
   ```
   pip install channels
   ```
2. 在 Django 项目中添加 `channels` 到 `INSTALLED_APPS`：
   ```python
   INSTALLED_APPS = [
       'channels',
       # 其他应用
   ]
   ```

### 配置 ASGI
在 `asgi.py` 文件中配置应用：
```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # WebSocket URL 路由
        ])
    ),
})
```

### 创建消费者
定义异步消费者处理 WebSocket：
```python
# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.send(text_data=json.dumps({'message': message}))
```

### 路由配置
在 `routing.py` 中添加路由：
```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]
```

### 运行服务器
使用 Daphne 或 Uvicorn 运行 ASGI 服务器：
```
daphne -p 8000 myproject.asgi:application
```

### 示例用法
在前端使用 JavaScript 连接 WebSocket：
```javascript
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data.message);
};
chatSocket.send(JSON.stringify({'message': 'Hello!'}));
```

更多细节请参考官方文档：https://channels.readthedocs.io/