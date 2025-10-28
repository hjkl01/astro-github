
---
title: simpleui
---

# SimpleUI 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/newpanjing/simpleui)

## 主要特性
SimpleUI 是一个基于 Django 的简单、现代化的后台管理界面框架，主要用于快速构建 Web 后台管理系统。它采用 Vue.js 前端框架，提供美观的 UI 组件和响应式设计，支持自定义主题和多语言。核心特性包括：
- **简洁界面**：采用扁平化设计，易于上手，减少开发者的 UI 定制工作。
- **模块化组件**：内置表格、表单、图表等常用组件，支持拖拽和富文本编辑。
- **权限管理**：集成 Django 的权限系统，支持用户角色和菜单动态配置。
- **多主题支持**：提供暗黑模式和自定义颜色方案，提升用户体验。
- **高性能**：优化了加载速度，支持分页、搜索和排序功能。

## 主要功能
- **后台管理面板**：快速生成 CRUD（创建、读取、更新、删除）操作界面，支持模型自动注册。
- **数据可视化**：集成 ECharts 等库，实现图表展示，如柱状图、折线图等。
- **文件上传与管理**：支持图片、文件上传，内置预览和下载功能。
- **API 接口集成**：易于与 Django REST Framework 结合，提供 RESTful API 支持。
- **国际化**：支持中文、英文等多语言切换，便于全球部署。
- **扩展性**：允许开发者自定义插件和模板，适用于电商、CMS 等各种后台应用。

## 用法
1. **安装依赖**：
   - 确保已安装 Python 3.6+ 和 Django 2.0+。
   - 通过 pip 安装：`pip install django-simpleui`。

2. **项目集成**：
   - 在 Django 的 `settings.py` 中添加 `'simpleui'` 到 `INSTALLED_APPS`。
   - 配置 URL：在 `urls.py` 中包含 `path('admin/', include('simpleui.urls'))`。

3. **运行项目**：
   - 执行 `python manage.py migrate` 进行数据库迁移。
   - 启动服务器：`python manage.py runserver`。
   - 访问 `http://127.0.0.1:8000/admin/` 进入管理后台，默认使用 Django 超级用户登录。

4. **自定义配置**：
   - 在 `settings.py` 中设置 `SIMPLEUI_CONFIG` 来调整主题、菜单等，例如：
     ```
     SIMPLEUI_CONFIG = {
         'system_keep': False,
         'menu_display': 'default',
         'theme': 'default',
     }
     ```
   - 对于模型注册，在 `admin.py` 中使用 `@register` 装饰器自动生成界面。

更多详情请参考项目 README 文档。