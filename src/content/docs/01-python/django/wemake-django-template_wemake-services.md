---
title: wemake-django-template
---

# wemake-django-template 项目

## 项目地址
[GitHub 项目地址](https://github.com/wemake-services/wemake-django-template)

## 主要特性
wemake-django-template 是一个现代化的 Django 项目模板，旨在帮助开发者快速构建高质量、可维护的 Django Web 应用。它强调代码质量、自动化和最佳实践，基于 Cookiecutter 模板生成器创建项目结构。主要特性包括：

- **严格的代码质量控制**：集成 flake8、mypy 和其他 linter 工具，确保代码符合 PEP 8 标准和类型提示，支持零警告开发。
- **现代化工具栈**：内置 Docker 支持（开发、生产环境）、pre-commit hooks、black 格式化器，以及 poetry 或 pipenv 依赖管理。
- **安全与最佳实践**：默认启用 Django 的安全中间件、CSRF 保护、HTTPS 重定向，并提供环境变量配置以避免硬编码敏感信息。
- **测试驱动开发**：预配置 pytest 测试框架，支持单元测试、集成测试和覆盖率报告。
- **可扩展结构**：模块化的项目布局，包括 apps、settings、templates 和静态文件组织，便于团队协作和扩展。
- **CI/CD 友好**：集成 GitHub Actions 或其他 CI 工具的示例配置，支持自动化测试和部署。

该模板适用于从零开始构建 Django 项目，特别适合注重代码规范的企业级应用开发。

## 主要功能
- **项目生成**：使用 Cookiecutter 快速 scaffolding 一个完整的 Django 项目骨架，包括核心应用、数据库迁移和初始配置。
- **开发环境管理**：通过 Docker Compose 运行本地开发服务器，支持 PostgreSQL、Redis 等常见服务。
- **生产部署准备**：提供 Gunicorn、Nginx 配置示例，以及环境-specific settings（dev、prod）。
- **代码审查自动化**：pre-commit 钩子在提交前自动检查代码风格、类型和安全问题。
- **国际化与静态文件**：内置 i18n 支持和 WhiteNoise 用于静态文件服务。
- **文档与日志**：预设 logging 配置和 Sphinx 文档生成工具。

这些功能帮助开发者避免常见 pitfalls，专注于业务逻辑而非 boilerplate 代码。

## 用法
1. **安装依赖**：
   - 确保安装 Cookiecutter：`pip install cookiecutter`。
   - 可选：安装 Git 和 Docker 以支持完整功能。

2. **生成项目**：
   - 运行命令：`cookiecutter https://github.com/wemake-services/wemake-django-template`。
   - 根据提示输入项目名称、描述、作者等信息。模板会自动创建项目目录。

3. **初始化和开发**：
   - 进入项目目录：`cd your-project-name`。
   - 安装依赖：`poetry install`（或 `pip install -r requirements.txt`）。
   - 运行迁移：`python manage.py migrate`。
   - 启动开发服务器：`docker-compose up`（或 `python manage.py runserver`）。

4. **测试和提交**：
   - 运行测试：`pytest`。
   - 安装 pre-commit：`pre-commit install`，然后提交代码以触发检查。
   - 构建文档：`make docs`（如果启用 Sphinx）。

5. **部署**：
   - 配置环境变量（.env 文件）。
   - 使用 Docker 构建镜像并部署到服务器，或集成到 CI/CD 管道。

更多细节请参考项目 README 和文档。建议在生成项目后阅读生成的 `README.md` 以获取自定义指导。