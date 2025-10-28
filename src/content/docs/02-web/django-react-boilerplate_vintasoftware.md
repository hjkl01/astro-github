
---
title: django-react-boilerplate
---

# Django React Boilerplate 项目

## 项目地址
[GitHub 项目地址](https://github.com/vintasoftware/django-react-boilerplate)

## 主要特性
- **前后端分离架构**：基于 Django（后端）和 React（前端）的现代 Web 应用 boilerplate，支持快速开发全栈应用。
- **集成工具链**：内置 Webpack 用于前端资源打包，支持热重载（Hot Reload）和代码分割，提升开发效率。
- **认证系统**：使用 Django REST Framework (DRF) 提供 JWT 或 Token 认证，支持用户注册、登录和权限管理。
- **API 开发**：DRF 提供 RESTful API 接口，便于前后端数据交互。
- **数据库支持**：默认使用 PostgreSQL，支持 Django ORM 进行模型定义和迁移。
- **测试框架**：集成 Django 测试工具和 Jest（前端测试），确保代码质量。
- **部署友好**：包含 Docker 配置，支持容器化部署；生产环境优化如静态文件收集和 Gunicorn 服务器。
- **其他特性**：ESLint 和 Prettier 代码规范、环境变量管理、CORS 处理。

## 主要功能
- **后端功能**：用户认证、API 端点管理、数据库模型（如用户、内容等）、管理员面板（Django Admin）。
- **前端功能**：React 组件化开发、路由（React Router）、状态管理（可选 Redux）、表单处理（Formik 等）。
- **开发功能**：实时开发服务器（Django + React 代理）、自动构建和测试运行。
- **扩展功能**：易于集成第三方库，如 Celery（任务队列）或 Redis（缓存）。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/vintasoftware/django-react-boilerplate.git
   cd django-react-boilerplate
   ```

2. **安装依赖**：
   - 后端：创建虚拟环境，安装 Python 依赖：
     ```
     python -m venv venv
     source venv/bin/activate  # Linux/Mac
     pip install -r requirements.txt
     ```
   - 前端：安装 Node 依赖：
     ```
     npm install
     ```

3. **配置环境**：
   - 复制 `.env.example` 为 `.env`，设置数据库、密钥等变量（如 `DATABASE_URL`、`SECRET_KEY`）。

4. **运行迁移和创建超级用户**：
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **启动开发服务器**：
   - 后端：`python manage.py runserver`
   - 前端：`npm start`（默认代理到后端端口 8000）
   - 访问 `http://localhost:3000` 查看前端，`/admin/` 访问 Django 后台。

6. **构建和生产部署**：
   - 构建前端：`npm run build`，静态文件将收集到 Django 的 `static` 目录。
   - 使用 Docker：`docker-compose up` 启动服务。
   - 生产环境：配置 Nginx/Gunicorn，运行 `python manage.py collectstatic`。

更多细节请参考项目 README。