---
title: django
---

# Django React Template 项目

## 项目地址
[GitHub 项目地址](https://github.com/Terkea/django_react_template)

## 主要特性
- **前后端分离架构**：基于 Django 后端和 React 前端，提供现代化的 Web 开发模板，支持 API 驱动的开发模式。
- **集成工具链**：内置 Django REST Framework (DRF) 用于构建 RESTful API，结合 React 的组件化开发，支持热重载和快速迭代。
- **认证与授权**：预配置 JWT 或 Token-based 认证系统，便于用户管理和安全访问控制。
- **数据库支持**：默认使用 SQLite 或 PostgreSQL，支持 ORM 操作，便于数据模型定义和管理。
- **部署友好**：包含 Docker 配置和生产环境设置，支持一键部署到 Heroku 或其他云平台。
- **测试框架**：集成 Django 和 React 的测试工具，确保代码质量和可靠性。

## 主要功能
- **后端功能**：提供用户注册、登录、数据 CRUD 操作，以及 API 端点管理。通过 DRF 实现序列化、过滤和分页。
- **前端功能**：React 应用包括路由管理（React Router）、状态管理（Redux 或 Context API）、UI 组件库（可能集成 Material-UI 或 Ant Design），支持响应式设计。
- **跨域支持**：配置 CORS 允许前后端在不同端口或域下通信。
- **静态文件处理**：Django 处理静态资源，React 通过 Webpack 构建优化输出。
- **扩展性**：易于添加新模块，如文件上传、实时聊天或第三方集成（例如 Stripe 支付）。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/Terkea/django_react_template.git
   cd django_react_template
   ```

2. **安装依赖**：
   - 后端：进入 `backend` 目录，运行 `pip install -r requirements.txt`。
   - 前端：进入 `frontend` 目录，运行 `npm install` 或 `yarn install`。

3. **配置环境**：
   - 复制 `.env.example` 为 `.env`，设置数据库、密钥等变量（例如 `SECRET_KEY`、`DATABASE_URL`）。

4. **运行项目**：
   - 后端：`python manage.py migrate` 然后 `python manage.py runserver`（默认端口 8000）。
   - 前端：`npm start` 或 `yarn start`（默认端口 3000）。
   - 前端会代理后端 API，确保 CORS 配置正确。

5. **开发与测试**：
   - 使用 Django admin 管理数据模型。
   - 在 React 中调用 API，例如通过 Axios 发送请求到 `/api/` 端点。
   - 运行测试：后端 `python manage.py test`，前端 `npm test`。

6. **部署**：
   - 使用 Docker：运行 `docker-compose up`。
   - 生产环境：构建 React（`npm run build`），将输出复制到 Django 的 static 文件夹，然后部署 Django 应用。

此模板适合快速启动 Django + React 项目，适用于博客、电商或管理系统开发。