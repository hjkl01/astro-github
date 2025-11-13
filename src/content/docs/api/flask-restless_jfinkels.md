---
title: flask-restless
---

# Flask-Restless 项目

## 项目地址
[GitHub 项目地址](https://github.com/jfinkels/flask-restless)

## 主要特性
Flask-Restless 是一个 Flask 扩展，用于快速生成 RESTful API。它基于 SQLAlchemy ORM 模型自动创建 API 端点，支持 CRUD 操作（创建、读取、更新、删除）。主要特性包括：
- **自动 API 生成**：无需手动编写路由，直接从 SQLAlchemy 模型生成完整的 REST API。
- **支持 HATEOAS**：API 响应包含超媒体链接，便于客户端导航。
- **自定义处理器**：允许开发者通过预处理器和后处理器自定义请求和响应逻辑。
- **分页和过滤**：内置支持查询分页、排序和过滤功能。
- **认证与授权**：集成 Flask-Principal 或其他认证系统，支持 API 访问控制。
- **兼容 Flask**：无缝集成 Flask 应用，轻量级且易扩展。

## 主要功能
- **CRUD 操作**：自动提供 GET（列表/详情）、POST（创建）、PUT/PATCH（更新）和 DELETE（删除）端点。
- **查询优化**：支持复杂查询，如关联模型的嵌套查询和条件过滤。
- **错误处理**：标准化 HTTP 错误响应，便于调试。
- **版本支持**：兼容 Flask 1.x 和 SQLAlchemy 1.x，支持 Python 2.7+ 和 3.x。
- **扩展性**：可与 Flask-RESTful 等其他扩展结合使用。

## 用法
1. **安装**：
   ```
   pip install flask-restless
   ```

2. **初始化**（在 Flask 应用中）：
   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_restless import APIManager

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
   db = SQLAlchemy(app)

   # 定义模型
   class Person(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(50))

   manager = APIManager(app, flask_sqlalchemy_db=db)
   manager.create_api(Person, methods=['GET', 'POST', 'PUT', 'DELETE'])
   ```

3. **运行应用**：
   - 启动 Flask 服务器后，访问 `/api/person` 即可使用生成的 API。
   - 示例请求：`GET /api/person` 获取人员列表；`POST /api/person` 创建新人员（JSON body: `{"name": "Alice"}`）。

4. **自定义**：
   - 添加预处理器：`manager.create_api(Person, preprocessors=dict(POST=[custom_preprocessor]))`。
   - 更多配置详见项目文档。