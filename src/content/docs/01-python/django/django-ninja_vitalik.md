---
title: django-ninja
---

# Django Ninja 项目

## 项目地址
[https://github.com/vitalik/django-ninja](https://github.com/vitalik/django-ninja)

## 主要特性
Django Ninja 是一个快速、高性能的 Python Web 框架，用于构建 RESTful API。它基于 Django 和 FastAPI 的理念，提供类型提示支持、自动文档生成和高效的异步处理。主要特性包括：
- **类型提示支持**：使用 Pydantic 模型进行请求/响应验证，确保 API 的类型安全性和数据完整性。
- **自动 OpenAPI 文档**：内置 Swagger UI 和 ReDoc 支持，一键生成交互式 API 文档。
- **高性能**：基于 ASGI（如 Uvicorn），支持异步操作，性能媲美 FastAPI。
- **与 Django 集成**：无缝集成 Django 的 ORM、认证和中间件，无需额外配置。
- **简洁语法**：使用装饰器（如 `@api_get`、`@api_post`）定义路由，代码简短易读。
- **依赖注入**：支持依赖注入机制，便于处理认证、日志等跨切面逻辑。
- **测试友好**：内置测试客户端，支持 pytest 等工具进行 API 测试。

## 主要功能
- **API 路由定义**：快速创建 GET、POST、PUT、DELETE 等 HTTP 方法的端点。
- **请求/响应处理**：自动解析 JSON、表单数据，支持文件上传和分页。
- **认证与授权**：集成 Django 的认证系统，支持 JWT、OAuth 等。
- **错误处理**：统一异常处理机制，提供自定义错误响应。
- **WebSocket 支持**：可选扩展支持实时通信。
- **多语言支持**：易于国际化 API 响应。

## 用法
1. **安装**：
   ```
   pip install django-ninja
   ```

2. **基本配置**：
   在 Django 的 `urls.py` 中添加：
   ```python
   from ninja import NinjaAPI
   from django.urls import path

   api = NinjaAPI()

   @api.get("/hello")
   def hello(request):
       return {"message": "Hello World"}

   urlpatterns = [
       path("api/", api.urls),
   ]
   ```

3. **定义模型和端点**：
   使用 Pydantic 模型：
   ```python
   from ninja import Schema

   class Item(Schema):
       name: str
       price: float

   @api.post("/items")
   def create_item(request, payload: Item):
       # 处理逻辑
       return payload
   ```

4. **运行和文档**：
   - 启动服务器：`python manage.py runserver`。
   - 访问 `/api/docs` 查看 Swagger 文档。

更多细节请参考官方文档和 GitHub 示例。