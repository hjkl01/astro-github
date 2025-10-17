
---
title: cookiecutter-django
---

# Cookiecutter Django 项目

## 项目地址
[https://github.com/pydanny/cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

## 主要特性
Cookiecutter Django 是一个基于 Cookiecutter 模板的 Django 项目骨架，旨在帮助开发者快速构建生产级别的 Django Web 应用。它遵循 Django 最佳实践，集成多种常用工具和库，支持模块化架构。核心特性包括：
- **模块化项目结构**：自动生成清晰的目录结构，包括 apps、核心模块、用户管理、静态文件处理等，支持多应用开发。
- **内置安全与认证**：集成 Django 的用户认证系统，支持第三方登录（如社交媒体）、密码重置和权限管理。
- **部署友好**：预配置 Docker 支持、环境变量管理，以及与 Heroku、AWS 等平台的兼容性，便于从开发到生产环境的过渡。
- **测试与 CI/CD 集成**：内置 pytest 测试框架、tox 支持，以及 GitHub Actions 或 Travis CI 的配置模板。
- **前端集成**：可选集成 Bootstrap 或其他 CSS 框架，支持静态文件压缩和 CDN 分发。
- **可扩展性**：支持自定义应用添加、数据库迁移、API 开发（使用 Django REST Framework），并兼容 Celery 任务队列和 Redis 缓存。

## 主要功能
- **项目生成**：通过 Cookiecutter 模板快速创建 Django 项目，包括核心功能如首页、用户注册/登录、管理员界面。
- **环境管理**：支持开发、测试、生产环境的分离，使用环境变量和 .env 文件管理配置（如数据库、秘密密钥）。
- **API 和后端服务**：内置 RESTful API 支持，便于构建前后端分离的应用。
- **静态与媒体文件处理**：集成 WhiteNoise 或 AWS S3 用于静态文件服务。
- **监控与日志**：预置 Sentry 错误跟踪和日志记录功能。
- **国际化支持**：内置 i18n 和 l10n 配置，支持多语言应用。

## 用法
1. **安装依赖**：
   - 确保安装 Cookiecutter：`pip install cookiecutter`。
   - 可选安装 Docker 以支持容器化开发。

2. **生成项目**：
   - 运行命令：`cookiecutter https://github.com/pydanny/cookiecutter-django`。
   - 在交互式提示中输入项目名称、描述、作者等信息，选择功能选项（如是否启用 Docker、PostgreSQL 等）。

3. **初始化和运行**：
   - 进入生成的项目目录：`cd your_project_name`。
   - 创建虚拟环境：`python -m venv venv` 并激活。
   - 安装依赖：`pip install -r requirements/local.txt`。
   - 运行迁移：`python manage.py migrate`。
   - 创建超级用户：`python manage.py createsuperuser`。
   - 启动服务器：`python manage.py runserver`。

4. **开发与部署**：
   - 添加自定义 app：使用 `python manage.py startapp myapp`。
   - 测试：运行 `pytest`。
   - 部署：使用 Docker Compose 或直接推送到 Heroku，根据模板配置调整 settings.py。

此模板适合中大型 Django 项目，开发者可根据需要自定义选项以避免过度工程化。