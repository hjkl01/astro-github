
---
title: django-sql-explorer
---

# Django SQL Explorer 项目

## 项目地址
[GitHub 项目地址](https://github.com/groveco/django-sql-explorer)

## 主要特性
Django SQL Explorer 是一个 Django 应用程序，用于安全地探索和分析数据库。它提供了一个 Web 界面，允许用户运行 SQL 查询，而无需直接访问数据库控制台。主要特性包括：
- **SQL 查询执行**：支持运行任意 SQL 查询，并以表格形式显示结果。
- **查询历史记录**：自动保存查询历史，便于重用和跟踪。
- **参数化查询**：支持参数化 SQL 以防止 SQL 注入，提高安全性。
- **导出功能**：结果可导出为 CSV、Excel 等格式。
- **权限控制**：集成 Django 的权限系统，限制用户访问特定查询或数据库。
- **查询优化**：内置工具帮助优化查询性能，如显示执行时间和行数。
- **搜索和过滤**：支持对查询结果进行搜索、排序和分页。
- **多数据库支持**：兼容多种后端数据库，如 PostgreSQL、MySQL 等。

## 主要功能
- **查询管理**：创建、编辑、保存和共享 SQL 查询。
- **结果可视化**：以交互式表格显示查询结果，支持实时更新。
- **日志和审计**：记录所有查询操作，便于审计和调试。
- **集成友好**：易于集成到现有 Django 项目中，支持自定义主题和扩展。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install django-sql-explorer`
   - 在 Django 的 `settings.py` 中添加 `'sql_explorer'` 到 `INSTALLED_APPS`。
   - 运行迁移：`python manage.py migrate sql_explorer`。

2. **配置**：
   - 在 `urls.py` 中包含 URL 配置：`path('sql-explorer/', include('sql_explorer.urls'))`。
   - 可选：在 `settings.py` 中配置权限和数据库别名。

3. **使用**：
   - 访问 Web 界面（例如 `/sql-explorer/`）。
   - 输入 SQL 查询，点击执行查看结果。
   - 保存查询以便后续使用，或导出数据。
   - 通过 Django 管理员面板管理用户权限，确保只有授权用户能访问。

此项目适用于数据分析师和开发者在生产环境中安全探索数据库。