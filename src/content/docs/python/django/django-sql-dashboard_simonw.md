---
title: django-sql-dashboard
---

# Django SQL Dashboard 项目

## 项目地址
[https://github.com/simonw/django-sql-dashboard](https://github.com/simonw/django-sql-dashboard)

## 主要特性
Django SQL Dashboard 是一个轻量级的 Django 应用，允许用户通过 Web 界面直接运行 SQL 查询并查看结果。它类似于 Airtable 或 Google Sheets 的查询功能，但专注于 SQL 执行。主要特性包括：
- **SQL 查询执行**：支持在浏览器中编写和运行 SQL 查询，直接连接到 Django 的数据库。
- **结果可视化**：查询结果以表格形式显示，支持排序、过滤和分页。
- **CSV 导出**：轻松将查询结果导出为 CSV 文件，便于进一步分析或分享。
- **参数化查询**：支持使用参数使查询更灵活和安全，避免 SQL 注入。
- **仪表板集成**：可以保存查询作为仪表板，便于重复使用和团队协作。
- **权限控制**：集成 Django 的认证系统，控制谁可以运行查询。
- **简单安装**：无需复杂配置，即插即用，支持 PostgreSQL、MySQL 等常见数据库。

该项目强调简单性和实用性，适合数据分析师、开发者或需要快速数据库查询的团队使用。它不是完整的 BI 工具，而是专注于 SQL 的快速原型和探索。

## 功能
- **查询编辑器**：内置 SQL 编辑器，支持语法高亮和自动完成（有限）。
- **历史记录**：保存最近运行的查询，便于回顾。
- **共享查询**：允许用户分享查询链接或保存为公共仪表板。
- **错误处理**：提供清晰的 SQL 错误消息，帮助调试。
- **性能优化**：限制查询时间和结果行数，防止资源滥用。
- **扩展性**：可以与 Django 的其他应用（如 Django Admin）集成。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install django-sql-dashboard`
   - 在 Django 的 `settings.py` 中添加 `'sql_dashboard'` 到 `INSTALLED_APPS`。
   - 运行迁移：`python manage.py migrate`。
   - 在 `urls.py` 中包含 URL：`path('dashboard/', include('sql_dashboard.urls'))`。

2. **配置**：
   - 可选：在 `settings.py` 中设置 `SQL_DASHBOARD` 字典来配置如最大查询时间、允许的数据库等。
   - 确保用户有数据库访问权限（通过 Django 的权限系统）。

3. **使用**：
   - 启动 Django 服务器：`python manage.py runserver`。
   - 访问 `/dashboard/` URL（需登录）。
   - 在界面中编写 SQL 查询，点击执行查看结果。
   - 保存查询：点击保存按钮，创建可重用的仪表板。
   - 导出：运行查询后，选择 CSV 导出。

更多细节请参考项目 README。