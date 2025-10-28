
---
title: cookiecutter-flask-skeleton
---

# Cookiecutter Flask Skeleton 项目

## 项目地址
[GitHub 项目地址](https://github.com/testdrivenio/cookiecutter-flask-skeleton)

## 主要特性
- **基于 Cookiecutter 的 Flask 项目模板**：这是一个使用 Cookiecutter 工具生成的 Flask 应用骨架，旨在快速启动现代化的 Web 应用开发，支持 Python 3.x 环境。
- **集成 Flask-Login 和 Flask-SQLAlchemy**：内置用户认证系统和 ORM 支持，便于处理用户登录、注册和数据库操作。
- **RESTful API 支持**：提供 API 蓝图，易于构建和扩展 RESTful 接口。
- **测试框架集成**：预配置 pytest 和工厂模式，便于编写单元测试和集成测试。
- **部署友好**：支持 Docker 容器化、Gunicorn 服务器和环境变量配置，适合生产环境部署。
- **模块化结构**：项目目录组织清晰，包括 models、views、templates 等标准 Flask 结构，便于维护和扩展。
- **其他特性**：包含 Celery 任务队列（可选）、Flask-Migrate 数据库迁移、Black 代码格式化，以及基本的错误处理和日志记录。

## 主要功能
- **用户认证**：支持用户注册、登录、登出和密码重置，通过 Flask-Login 实现会话管理。
- **数据库管理**：使用 SQLAlchemy 处理模型定义，支持 SQLite、PostgreSQL 等数据库，后端通过 Flask-Migrate 进行 schema 迁移。
- **API 开发**：内置 API 路由，支持 JSON 数据交换，适用于前后端分离应用。
- **任务处理**：可选集成 Celery，用于异步任务如邮件发送或后台处理。
- **测试与 CI/CD**：预设测试脚本，支持 GitHub Actions 等 CI 工具自动化测试和部署。
- **静态文件与模板**：集成 Bootstrap 或其他前端框架，处理 HTML 模板和资产管理。

## 用法
1. **安装依赖**：
   - 确保安装 Cookiecutter：`pip install cookiecutter`。
   - 可选安装 Git 以克隆仓库。

2. **生成项目**：
   - 运行命令：`cookiecutter https://github.com/testdrivenio/cookiecutter-flask-skeleton`。
   - 根据提示输入项目名称、应用名称、数据库类型等配置选项，生成自定义项目结构。

3. **设置环境**：
   - 进入生成的项目目录：`cd your-project-name`。
   - 创建虚拟环境：`python -m venv venv` 并激活。
   - 安装依赖：`pip install -r requirements.txt`。

4. **初始化数据库**：
   - 设置环境变量（如 `DATABASE_URL`）。
   - 运行迁移：`flask db upgrade`。

5. **运行应用**：
   - 开发模式：`flask run` 或使用 `python manage.py runserver`。
   - 生产模式：使用 Gunicorn，如 `gunicorn 'create_app:create_app()' -b 0.0.0.0:5000`。

6. **测试**：
   - 运行测试：`pytest`。

7. **部署**：
   - 使用 Docker：构建镜像 `docker build -t your-app .` 并运行容器。
   - 支持 Heroku、AWS 等平台，通过提供的 Procfile 和 Dockerfile 简化部署。

此模板适合初学者和经验开发者快速构建 Flask 应用，强调最佳实践和可扩展性。