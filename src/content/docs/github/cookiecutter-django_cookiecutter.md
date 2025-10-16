
---
title: cookiecutter-django
---

# Cookiecutter Django 项目

**项目地址**: [https://github.com/cookiecutter/cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)

## 主要特性
Cookiecutter Django 是一个基于 Cookiecutter 模板的 Django 项目启动器，专为快速构建生产级 Django 应用而设计。它提供了以下主要特性：
- **模块化结构**：生成一个高度模块化的 Django 项目结构，包括用户认证、API 支持、静态文件处理等预配置组件，便于扩展和维护。
- **生产就绪**：内置生产环境配置，如 Docker 支持、数据库迁移、缓存系统（Redis）、任务队列（Celery）和监控工具（Sentry），无需从零开始设置。
- **灵活自定义**：通过交互式提示，用户可以选择是否包含特定功能，如 REST API（Django REST Framework）、静态站点生成（Wagtail）或自定义用户模型。
- **最佳实践集成**：遵循 Django 最佳实践，包括安全配置、测试框架（pytest）、代码质量工具（pre-commit hooks）和部署脚本。
- **跨平台支持**：兼容多种数据库（PostgreSQL、SQLite）和部署环境，支持本地开发和云部署。

## 功能
该项目的主要功能是通过模板生成一个完整的 Django 项目骨架，涵盖：
- **认证与授权**：集成 Django Allauth，支持社交登录、邮箱验证和权限管理。
- **API 开发**：可选集成 Django REST Framework，提供序列化、视图集和认证后端。
- **资产管理**：使用 WhiteNoise 或 AWS S3 处理静态文件和媒体文件。
- **后台任务**：Celery 与 Redis 结合，实现异步任务和定时任务。
- **测试与 CI/CD**：预置 pytest 测试套件和 GitHub Actions 工作流，支持自动化测试和部署。
- **文档与日志**：内置文档生成（MkDocs）和日志记录（Loguru）。

这些功能使项目适合从小型应用到企业级 Web 应用的快速原型开发。

## 用法
1. **安装依赖**：
   - 确保安装 Python 3.8+ 和 Cookiecutter：`pip install cookiecutter`。

2. **创建项目**：
   - 运行命令：`cookiecutter https://github.com/cookiecutter/cookiecutter-django`。
   - 根据交互提示输入项目名称、作者信息、是否使用 Docker 等选项。

3. **初始化与运行**：
   - 进入生成的项目目录：`cd your-project-name`。
   - 安装依赖：`pip install -r requirements/local.txt`（或使用 Docker Compose）。
   - 运行迁移：`python manage.py migrate`。
   - 创建超级用户：`python manage.py createsuperuser`。
   - 启动开发服务器：`python manage.py runserver`。

4. **开发与部署**：
   - 自定义模板文件以调整功能。
   - 对于生产部署，使用提供的 Docker 配置或部署到 Heroku/AWS 等平台。
   - 参考项目 README 中的详细指南进行测试、文档生成和钩子设置。

此模板大大简化了 Django 项目的启动过程，适合初学者和经验开发者。