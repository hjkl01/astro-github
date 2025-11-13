---
title: strawberry
---

# Strawberry GraphQL 项目

## 项目地址
[GitHub 项目地址](https://github.com/strawberry-graphql/strawberry)

## 主要特性
Strawberry 是一个 Python 库，用于构建 GraphQL API。它基于 Python 类型提示（type hints），提供类型安全的 GraphQL 实现。主要特性包括：
- **类型安全**：利用 Python 的类型系统（如 dataclasses、Pydantic 模型）定义 GraphQL schema，避免手动编写 schema 文件。
- **现代 Python 支持**：兼容 Python 3.7+，集成 asyncio 和 ASGI（如 Starlette、FastAPI），支持异步查询。
- **灵活扩展**：支持自定义标量类型、接口、联合类型和订阅（subscriptions）。
- **工具集成**：内置 GraphiQL 界面、代码生成和验证工具，易于调试和开发。
- **性能优化**：高效的解析和执行引擎，支持缓存和批处理。
- **社区驱动**：开源项目，活跃维护，兼容 Strawberry 生态中的插件和扩展。

## 主要功能
- **Schema 定义**：通过装饰器（如 `@strawberry.type` 和 `@strawberry.field`）快速定义查询（Query）、变异（Mutation）和订阅（Subscription）。
- **查询执行**：支持 GraphQL 查询解析、验证和执行，包括实时订阅。
- **集成支持**：无缝集成 FastAPI、Django 和 Flask 等框架，提供 HTTP/2 和 WebSocket 支持。
- **错误处理**：内置错误类型和扩展机制，确保 API 的鲁棒性。
- **测试工具**：提供 schema 验证和查询测试功能，便于单元测试。
- **国际化**：支持多语言 schema 定义和国际化消息。

## 用法
### 安装
```bash
pip install strawberry-graphql
```

### 基本用法示例
1. **定义 Schema**：
   ```python
   import strawberry

   @strawberry.type
   class User:
       name: str
       age: int

   @strawberry.type
   class Query:
       @strawberry.field
       def user(self) -> User:
           return User(name="Alice", age=30)

   schema = strawberry.Schema(query=Query)
   ```

2. **集成到 ASGI 应用**（如 FastAPI）：
   ```python
   from fastapi import FastAPI
   from strawberry.asgi import GraphQL

   app = FastAPI()
   graphql_app = GraphQL(schema)

   app.mount("/graphql", graphql_app)
   ```

3. **运行查询**：
   - 使用 GraphiQL 界面：在 `/graphql` 端点访问，输入查询如 `{ user { name age } }`。
   - 程序化执行：
     ```python
     from strawberry.schema import execute

     result = execute(schema, query="{ user { name age } }")
     print(result.data)  # {'user': {'name': 'Alice', 'age': 30}}
     ```

更多高级用法详见官方文档：https://strawberry.rocks/