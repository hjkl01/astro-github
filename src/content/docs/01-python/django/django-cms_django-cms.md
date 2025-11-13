---
title: django-cms
---

# django-cms 项目描述

## 项目地址
[https://github.com/django-cms/django-cms](https://github.com/django-cms/django-cms)

## 主要特性
django-cms 是一个开源的内容管理系统（CMS），基于 Python 的 Django 框架构建。它提供了灵活的网站内容管理和编辑功能，支持多语言、多站点部署，以及插件式扩展。主要特性包括：
- **页面管理和编辑**：直观的拖拽式界面，支持实时预览和版本控制。
- **多语言支持**：内置国际化功能，允许轻松创建多语言网站。
- **插件系统**：可扩展的插件架构，支持自定义内容类型，如文本、图片、视频等。
- **用户权限管理**：细粒度的权限控制，适合团队协作。
- **SEO 优化**：内置搜索引擎优化工具，如元标签和 URL 结构管理。
- **响应式设计**：兼容现代前端框架，确保移动端友好。
- **安全性**：集成 Django 的安全机制，防范常见 Web 攻击。

## 主要功能
- **内容创建与发布**：用户可以通过 WYSIWYG 编辑器创建和管理页面、文章和静态内容。
- **模板系统**：支持自定义 HTML 模板和主题，允许开发者调整布局。
- **前端集成**：无缝集成 Bootstrap 或其他 CSS 框架，提供现成的前端组件。
- **API 支持**：通过 Django REST Framework 扩展，提供 RESTful API 用于移动应用集成。
- **工作流管理**：支持内容审核流程，确保发布前内容质量。
- **数据迁移**：内置迁移工具，便于从其他 CMS 迁移数据。

## 用法
1. **安装**：
   - 确保安装 Python 3.8+ 和 pip。
   - 创建虚拟环境：`python -m venv env` 并激活。
   - 安装 django-cms：`pip install django-cms`。
   - 创建 Django 项目：`django-admin startproject mysite`。
   - 在 `settings.py` 中添加 `'cms'` 到 `INSTALLED_APPS`，并配置数据库（推荐 PostgreSQL 或 SQLite）。

2. **配置**：
   - 运行迁移：`python manage.py migrate`。
   - 创建超级用户：`python manage.py createsuperuser`。
   - 安装 CMS：`python manage.py cms init`（可选，用于初始化默认页面）。

3. **运行和使用**：
   - 启动开发服务器：`python manage.py runserver`。
   - 访问 `http://127.0.0.1:8000/admin/` 登录后台。
   - 在后台创建页面：选择“Pages” > “Add Page”，添加内容插件（如 Text 或 Picture）。
   - 发布页面：保存后，页面将自动生成 URL，可通过前端访问。
   - 扩展：创建自定义插件，参考官方文档 [docs.django-cms.org](https://docs.django-cms.org)。

更多细节请参考项目 README 和官方文档。