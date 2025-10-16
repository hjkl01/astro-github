
---
title: flask-restful
---

# Flask-RESTful 项目

**项目地址:** [https://github.com/flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)

## 主要特性
Flask-RESTful 是一个轻量级的 Python 扩展库，专为 Flask 框架设计，用于快速构建 RESTful API。它提供简洁的接口来定义 API 资源，支持 HTTP 方法（如 GET、POST、PUT、DELETE），并自动处理请求解析、响应序列化和错误处理。主要特性包括：
- **资源导向设计**：将 API 端点抽象为资源类，便于组织代码。
- **参数解析**：内置支持查询参数、表单数据和 JSON 输入的解析器（使用 argparse 或 marshmallow）。
- **响应处理**：自动生成 JSON 响应，支持自定义错误消息和状态码。
- **安全性与验证**：集成输入验证、认证和授权机制。
- **易扩展**：兼容 Flask 的生态，支持蓝图（Blueprints）和自定义错误处理器。
- **轻量高效**：不引入过多依赖，适合中小型 API 项目。

## 主要功能
- **资源定义**：通过 `Resource` 类定义 API 端点，支持单个资源（`@api.resource`）或资源列表。
- **HTTP 方法支持**：实现 `get`、`post`、`put`、`delete`、`patch` 等方法。
- **请求/响应处理**：自动处理 `request` 对象，生成标准 HTTP 响应（如 200 OK、404 Not Found）。
- **错误管理**：内置异常处理器，如 `ApiError`，便于统一错误响应。
- **分页与过滤**：支持查询参数驱动的分页、排序和过滤功能。
- **文档生成**：易于集成 Swagger 或其他 API 文档工具。

## 用法示例
### 安装
```bash
pip install flask-restful
```

### 基本用法
1. **初始化 API**：
   ```python
   from flask import Flask
   from flask_restful import Api, Resource, reqparse

   app = Flask(__name__)
   api = Api(app)
   ```

2. **定义资源**：
   ```python
   class HelloWorld(Resource):
       def get(self):
           return {'hello': 'world'}

       def post(self):
           parser = reqparse.RequestParser()
           parser.add_argument('name', type=str)
           args = parser.parse_args()
           return {'you': args['name']}, 201

   api.add_resource(HelloWorld, '/hello')
   ```

3. **运行应用**：
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

   - 访问 `GET /hello`：返回 `{"hello": "world"}`。
   - 访问 `POST /hello`（带 JSON `{"name": "user"}`）：返回 `{"you": "user"}`（状态码 201）。

更多高级用法详见项目文档，包括认证集成和自定义格式化。