---
title: fastapi-react
---

# FastAPI-React 项目

## 项目地址
[GitHub 项目地址](https://github.com/Buuntu/fastapi-react)

## 主要特性
- **前后端分离架构**：使用 FastAPI 作为后端 API 框架，提供高效、现代的 Python Web 服务；前端采用 React 构建单页应用（SPA），实现响应式用户界面。
- **API 驱动开发**：FastAPI 支持自动生成 OpenAPI 文档，便于 API 测试和集成；内置类型提示和验证，提高代码可靠性和开发效率。
- **实时功能支持**：集成 WebSocket 支持，实现实时数据更新，如聊天或通知系统。
- **认证与授权**：内置 JWT 或 OAuth 支持，确保安全访问控制。
- **数据库集成**：兼容 SQLAlchemy 和 Alembic，支持 PostgreSQL、SQLite 等数据库的 ORM 操作和迁移。
- **部署友好**：支持 Docker 容器化，便于在云平台（如 Heroku、AWS）部署；前端可独立构建为静态文件。

## 主要功能
- **后端 API 服务**：提供 RESTful API 接口，用于数据 CRUD 操作、用户管理、文件上传等。
- **前端交互界面**：React 组件化开发，支持路由（React Router）、状态管理（Redux 或 Context API）和 UI 库（如 Material-UI），实现动态页面渲染。
- **跨域支持**：配置 CORS 允许前后端跨域通信。
- **测试与文档**：FastAPI 自动生成 Swagger UI 和 ReDoc 文档；支持单元测试（Pytest）和前端测试（Jest）。
- **环境配置**：使用 .env 文件管理开发、生产环境变量，如数据库连接和 API 密钥。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/Buuntu/fastapi-react.git
   cd fastapi-react
   ```

2. **安装依赖**：
   - 后端：创建虚拟环境，运行 `pip install -r backend/requirements.txt`。
   - 前端：进入 `frontend` 目录，运行 `npm install` 或 `yarn install`。

3. **运行后端**：
   - 在 `backend` 目录下，运行 `uvicorn main:app --reload`（开发模式）。
   - API 将在 `http://localhost:8000` 启动，访问 `/docs` 查看 Swagger 文档。

4. **运行前端**：
   - 在 `frontend` 目录下，运行 `npm start` 或 `yarn start`。
   - 应用将在 `http://localhost:3000` 启动，前端会自动连接后端 API。

5. **构建与部署**：
   - 前端构建：`npm run build`，生成静态文件可托管于 Nginx 或 CDN。
   - 后端部署：使用 Gunicorn + Uvicorn，或 Docker 镜像：`docker-compose up`。
   - 配置环境变量（如 `DATABASE_URL`）以连接实际数据库。

6. **开发提示**：
   - 修改 API：在 `backend/app` 下编辑路由和模型。
   - 修改 UI：在 `frontend/src` 下调整组件和 API 调用。
   - 测试：运行 `pytest`（后端）或 `npm test`（前端）。