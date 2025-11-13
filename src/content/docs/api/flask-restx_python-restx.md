---
title: flask-restx
---

# Flask-RESTX 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/python-restx/flask-restx)

## 主要特性
Flask-RESTX 是 Flask 框架的一个扩展库，专注于构建 RESTful API。它基于 Flask-RESTPlus 发展而来，提供更现代化的 API 开发工具。主要特性包括：
- **自动生成 API 文档**：集成 Swagger UI，支持 OpenAPI 规范，自动生成交互式 API 文档，便于开发和测试。
- **请求/响应解析**：内置支持 JSON、表单数据等格式的输入输出验证，使用 schemas 定义数据模型。
- **命名空间组织**：通过 Namespace 机制组织 API 端点，支持模块化开发。
- **错误处理**：统一的异常处理机制，提供 HTTP 状态码和自定义错误响应。
- **参数支持**：处理查询参数、路径参数和头部参数，支持类型验证和默认值。
- **安全性增强**：支持 API 密钥认证、OAuth 等集成（需结合 Flask 扩展）。
- **兼容性**：完全兼容 Flask 生态，支持 Python 3.6+，易于与现有 Flask 项目集成。

## 主要功能
Flask-RESTX 的核心功能围绕 REST API 的构建和维护：
- **API 路由定义**：使用 `@api.route` 和 `@api.expect` 装饰器快速定义端点，支持 GET、POST、PUT、DELETE 等方法。
- **数据序列化**：通过 `fields` 模块定义模型，实现对象到 JSON 的转换。
- **Swagger 集成**：一键启用 Swagger 界面，自动文档化 API，包括端点描述、参数和响应示例。
- **测试支持**：内置工具用于 API 测试和调试。
- **扩展性**：支持自定义 marshal 格式、错误处理器和资源类继承。

## 用法示例
### 安装
```bash
pip install flask-restx
```

### 基本用法
创建一个简单的 Flask-RESTX 应用：

```python
from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='我的 API', description='一个简单的 REST API 示例')

# 定义命名空间
ns = api.namespace('example', description='示例操作')

# 定义模型
model = api.model('Model', {
    'name': fields.String(required=True),
    'age': fields.Integer
})

@ns.route('/hello')
class HelloWorld(Resource):
    @ns.doc('get_hello')
    def get(self):
        return {'message': 'Hello World!'}

    @ns.expect(model)
    @ns.marshal_with(model)
    def post(self):
        data = api.payload
        return data, 201

if __name__ == '__main__':
    app.run(debug=True)
```

### 运行和访问
- 运行应用后，访问 `http://localhost:5000/` 可看到 Swagger UI 文档。
- 使用文档中的界面测试 API 端点，例如 POST 到 `/example/hello` 发送 JSON 数据。

此项目适合快速开发微服务或 Web API，文档详尽，社区活跃。