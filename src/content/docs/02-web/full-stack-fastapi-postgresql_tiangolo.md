---
title: full-stack-fastapi-postgresql
---

# Full Stack FastAPI PostgreSQL 项目

## 项目地址
[GitHub 项目地址](https://github.com/tiangolo/full-stack-fastapi-postgresql)

## 主要特性
- **全栈架构**：基于 FastAPI 后端、PostgreSQL 数据库和现代前端框架（如 React 或 Vue.js）的完整全栈应用模板，提供从 API 到 UI 的端到端解决方案。
- **高性能 API**：利用 FastAPI 的异步特性，支持快速开发和高效的 Web API，包括自动生成的 OpenAPI 文档和 Swagger UI。
- **数据库集成**：使用 SQLAlchemy ORM 与 PostgreSQL 数据库无缝集成，支持复杂查询、事务和数据迁移（通过 Alembic）。
- **认证与授权**：内置 JWT 令牌认证系统，支持用户注册、登录和基于角色的访问控制（RBAC）。
- **现代前端**：前端采用 TypeScript 和流行框架构建，提供响应式设计、状态管理和实时更新功能。
- **容器化部署**：支持 Docker 和 Docker Compose，便于本地开发、测试和生产部署，包括多容器环境（如后端、数据库和前端）。
- **测试与 CI/CD**：集成 Pytest 测试框架、覆盖率工具，以及 GitHub Actions 用于持续集成。
- **安全性**：包含 CORS 配置、输入验证、HTTPS 支持和常见安全最佳实践。

## 主要功能
- **用户管理**：用户注册、登录、注销，以及个人资料编辑和密码重置。
- **CRUD 操作**：对核心实体（如用户、项目或任务）进行创建、读取、更新和删除操作，通过 RESTful API 实现。
- **实时通信**：可选集成 WebSocket 支持，用于实时通知或聊天功能。
- **文件上传**：支持图像或文件上传，使用云存储或本地存储。
- **后台任务**：使用 Celery 和 Redis 处理异步任务，如邮件发送或数据处理。
- **API 文档**：自动生成交互式 API 文档，便于开发和调试。
- **监控与日志**：集成日志记录和性能监控工具。

## 用法
1. **克隆仓库**：
   ```
   git clone https://github.com/tiangolo/full-stack-fastapi-postgresql.git
   cd full-stack-fastapi-postgresql
   ```

2. **安装依赖**：
   - 后端：创建虚拟环境，安装 `requirements.txt` 中的依赖（如 `pip install -r requirements.txt`）。
   - 前端：使用 npm 或 yarn 安装（如 `npm install`）。
   - 数据库：确保 PostgreSQL 已安装，或使用 Docker。

3. **配置环境**：
   - 复制 `.env.example` 为 `.env`，并配置数据库 URL、密钥等变量（如 `DATABASE_URL=postgresql://user:password@localhost/dbname`）。

4. **运行应用**：
   - 使用 Docker：`docker-compose up -d`（自动启动后端、数据库和前端）。
   - 手动运行：
     - 启动数据库：`docker run -d -p 5432:5432 --name db -e POSTGRES_PASSWORD=password postgres:13`。
     - 运行后端：`uvicorn app.main:app --reload`（访问 `http://localhost:8000`）。
     - 运行前端：`npm run dev`（访问 `http://localhost:3000`）。

5. **数据库迁移**：
   - 初始化 Alembic：`alembic init alembic`。
   - 生成迁移：`alembic revision --autogenerate -m "Initial migration"`。
   - 应用迁移：`alembic upgrade head`。

6. **测试**：
   - 运行测试：`pytest`。
   - 检查覆盖率：`pytest --cov`。

7. **部署**：
   - 使用 Docker Compose 或 Kubernetes 部署到云平台（如 Heroku、AWS 或 Vercel）。
   - 配置生产环境变量，确保安全密钥和数据库连接正确。

此项目适合快速构建生产级 Web 应用，提供可扩展的模板以自定义需求。