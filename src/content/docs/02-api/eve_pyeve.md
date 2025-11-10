---
title: eve
---

# EVE 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/pyeve/eve)

## 主要特性
EVE 是一个基于 Python 的开源框架，主要用于构建 RESTful API 服务。它是 Flask 的扩展，专注于快速开发和部署 API。核心特性包括：
- **资源导向设计**：支持资源（Resource）作为 API 的核心单元，便于定义和管理数据模型。
- **内置认证与授权**：集成多种认证机制，如 Basic Auth、OAuth 和 JWT，支持角色-based 访问控制。
- **数据验证与序列化**：自动处理输入验证、输出格式化和分页，支持多种数据格式（如 JSON、XML）。
- **MongoDB 原生支持**：无缝集成 MongoDB 作为后端数据库，但也可扩展到其他存储。
- **扩展性强**：模块化设计，支持自定义钩子（Hooks）和扩展插件，便于集成第三方服务。
- **轻量级与高效**：基于 Flask，启动快速，适合微服务架构。

## 主要功能
- **API 端点管理**：自动生成 CRUD 操作的 RESTful 端点，包括 GET、POST、PUT、DELETE 等。
- **领域驱动设计**：支持领域（Domain）概念，用于复杂业务逻辑的封装。
- **错误处理与日志**：内置异常处理、HTTP 状态码响应和日志记录。
- **测试支持**：提供测试客户端和工具，便于单元测试和集成测试。
- **部署友好**：支持 WSGI 服务器部署，如 Gunicorn 或 uWSGI。

## 用法
1. **安装**：
   使用 pip 安装：`pip install eve`。确保安装 Flask 和 MongoDB（如果使用）。

2. **基本配置**：
   创建一个 Python 文件（如 `app.py`）：
   ```python
   from eve import Eve
   app = Eve()
   if __name__ == '__main__':
       app.run()
   ```

3. **定义资源**：
   在 `settings.py` 中配置资源：
   ```python
   # settings.py
   DOMAIN = {
       'people': {
           'schema': {
               'name': {'type': 'string'},
               'age': {'type': 'integer'},
           }
       }
   }
   ```
   这将自动创建 `/people` 端点，支持 CRUD 操作。

4. **运行与测试**：
   - 运行应用：`python app.py`。
   - 测试 API：使用 curl 或 Postman，例如 `curl -X GET http://localhost:5000/people`。
   - 连接 MongoDB：设置 `MONGO_URI` 在 settings 中。

5. **高级用法**：
   - 添加认证：在 settings 中配置 `AUTH` 字段。
   - 自定义钩子：使用 `@app.route` 或 Eve 的钩子函数扩展逻辑。
   - 更多细节参考官方文档：项目 README 或 [Eve 文档](https://docs.python-eve.org/)。

此项目适合快速构建数据驱动的 API 服务，社区活跃，适用于 Web 开发和后端服务。