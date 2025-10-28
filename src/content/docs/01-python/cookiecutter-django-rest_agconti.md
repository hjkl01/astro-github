
---
title: cookiecutter-django-rest
---

# Cookiecutter Django REST 项目

## 项目地址
[GitHub 项目地址](https://github.com/agconti/cookiecutter-django-rest)

## 主要特性
- **基于 Cookiecutter 的模板生成器**：这是一个 Django REST Framework 的项目模板，使用 Cookiecutter 工具快速创建生产就绪的 Django 项目结构。
- **模块化设计**：生成的项目包括用户认证、API 端点、管理员界面等模块，支持扩展和自定义。
- **集成常用库**：内置 Django REST Framework、PostgreSQL 支持、Celery 任务队列、Redis 缓存，以及 Docker 配置，便于开发和部署。
- **安全与最佳实践**：默认包含 CSRF 保护、CORS 配置、OAuth 支持，以及测试框架集成。
- **响应式前端**：可选集成 Bootstrap 或其他 CSS 框架，提供基本的 Web 界面。

## 主要功能
- **API 开发**：快速生成 RESTful API，支持序列化、视图集和路由配置。
- **用户管理**：内置用户注册、登录、权限控制和 JWT/OAuth 认证。
- **后台任务**：通过 Celery 和 Redis 处理异步任务，如邮件发送或数据处理。
- **数据库支持**：默认使用 PostgreSQL，支持迁移和模型定义。
- **部署友好**：包含 Docker Compose 文件、Gunicorn 和 Nginx 配置，便于容器化部署。
- **测试与文档**：集成 pytest 测试框架和 API 文档生成工具（如 DRF Spectacular）。

## 用法
1. **安装 Cookiecutter**：
   ```
   pip install cookiecutter
   ```

2. **生成项目**：
   ```
   cookiecutter https://github.com/agconti/cookiecutter-django-rest
   ```
   运行后，按照提示输入项目名称、描述、作者等信息，生成项目文件夹。

3. **安装依赖**：
   进入生成的项目目录，运行：
   ```
   pip install -r requirements/local.txt
   ```

4. **运行开发服务器**：
   ```
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
   访问 `http://127.0.0.1:8000/` 查看项目。

5. **自定义与扩展**：
   - 编辑 `settings/` 中的配置文件。
   - 在 `apps/` 目录添加新应用和 API 端点。
   - 使用 Docker：运行 `docker-compose up` 启动服务。

此模板适合快速启动 Django REST API 项目，支持从开发到生产的完整流程。