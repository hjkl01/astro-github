---
title: fastapi-starter
---

# FastAPI Starter 项目

## 项目地址
[GitHub 项目地址](https://github.com/gaganpreet/fastapi-starter)

## 主要特性
- **现代 FastAPI 框架**：基于 FastAPI 构建，提供高性能的异步 API 开发体验，支持自动生成 OpenAPI 文档。
- **依赖注入系统**：内置依赖管理，支持数据库连接、认证和配置注入，简化代码组织。
- **数据库集成**：使用 SQLAlchemy ORM，支持 PostgreSQL 或 SQLite 等数据库，包含迁移工具 Alembic。
- **认证与授权**：集成 JWT 或 OAuth2，支持用户注册、登录和角色-based 访问控制。
- **测试支持**：内置 Pytest 配置，包含单元测试和集成测试模板，便于 CI/CD 集成。
- **环境配置**：使用 Pydantic 模型管理开发、生产环境变量，支持 Docker 部署。
- **API 文档**：自动生成 Swagger UI 和 ReDoc 接口文档，便于前端开发和调试。

## 主要功能
- **用户管理**：提供 CRUD 操作接口，包括用户创建、查询、更新和删除。
- **API 路由**：预定义 RESTful 路由，支持 GET、POST、PUT、DELETE 等 HTTP 方法。
- **错误处理**：全局异常处理器，统一返回 JSON 格式的错误响应。
- **日志记录**：集成 logging 模块，支持结构化日志输出。
- **CORS 支持**：配置跨域资源共享，适用于前后端分离应用。
- **健康检查**：内置健康端点，用于监控应用状态。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/gaganpreet/fastapi-starter.git
   cd fastapi-starter
   ```

2. **安装依赖**：
   ```
   pip install -r requirements.txt
   ```

3. **配置环境**：
   - 复制 `.env.example` 为 `.env`，并编辑数据库 URL、密钥等配置。
   - 示例：`DATABASE_URL=postgresql://user:password@localhost/dbname`

4. **运行迁移**（如果使用数据库）：
   ```
   alembic upgrade head
   ```

5. **启动应用**：
   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **访问 API**：
   - Swagger UI: http://localhost:8000/docs
   - 测试端点：如 `/users/` 用于用户管理。

项目适合快速构建生产级 FastAPI 应用，可根据需求扩展模块。