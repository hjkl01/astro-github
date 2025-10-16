
---
title: flask-graphql
---

# Flask-GraphQL 项目

**项目地址:** [https://github.com/graphql-python/flask-graphql](https://github.com/graphql-python/flask-graphql)

## 主要特性

- **GraphQL 集成**: 将 GraphQL 服务器无缝集成到 Flask 应用中，支持查询和变异操作。
- **Schema 定义**: 使用 Python 的 GraphQL 库（如 Graphene）定义 schema，支持类型系统、解析器和订阅。
- **灵活的端点配置**: 允许自定义 GraphQL 端点路径、支持 POST 和 GET 请求。
- **错误处理和调试**: 内置错误处理机制，支持 GraphQL 标准的错误格式，并在开发模式下提供详细的调试信息。
- **中间件支持**: 兼容 Flask 的中间件系统，便于添加认证、日志等功能。
- **兼容性**: 与 Python 3.x 和 Flask 框架兼容，支持异步操作（需额外配置）。

## 主要功能

- **GraphQL 执行**: 处理 GraphQL 查询、变异和订阅，提供实时数据响应。
- **Schema 验证**: 自动验证输入数据，确保类型安全。
- **上下文传递**: 支持在解析器中访问 Flask 请求上下文，如用户会话和 HTTP 头。
- **批处理支持**: 处理批量查询，提高性能。
- **工具集成**: 与 GraphQL Playground 或 GraphiQL 集成，便于开发时测试和可视化查询。

## 用法

1. **安装**:
   ```
   pip install flask-graphql
   ```

2. **基本设置**（假设使用 Graphene 定义 schema）:
   ```python
   from flask import Flask
   from flask_graphql import GraphQLView
   from graphene import ObjectType, String, Schema
   from graphene_flask import FlaskGraphQL  # 示例依赖

   # 定义 schema
   class Query(ObjectType):
       hello = String(description='A typical hello world')

       def resolve_hello(self, info):
           return 'World'

   schema = Schema(query=Query)

   # 创建 Flask 应用
   app = Flask(__name__)
   app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
   ```

3. **运行应用**:
   ```
   if __name__ == '__main__':
       app.run(debug=True)
   ```
   访问 `http://localhost:5000/graphql` 以使用 GraphiQL 测试查询。

4. **高级用法**:
   - **自定义上下文**: 在 `GraphQLView` 中传入 `get_context` 函数访问 Flask 请求。
   - **认证**: 使用 Flask 的 `@login_required` 或自定义中间件保护端点。
   - **订阅**: 对于实时订阅，需结合 Flask-SocketIO 或类似库实现 WebSocket 支持。

更多细节请参考项目文档和示例。