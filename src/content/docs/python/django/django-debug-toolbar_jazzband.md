---
title: django-debug-toolbar
---

# Django Debug Toolbar

**GitHub 项目地址:** [https://github.com/jazzband/django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

## 主要特性
Django Debug Toolbar 是一个用于 Django 项目的调试工具栏，它在浏览器中显示一个浮动面板，提供实时调试信息，帮助开发者诊断和优化应用。主要特性包括：
- **性能监控**：显示 SQL 查询、缓存操作、模板渲染等耗时统计，帮助识别瓶颈。
- **SQL 查询分析**：列出所有执行的 SQL 语句，包括执行时间、参数和重复查询，便于优化数据库交互。
- **请求/响应信息**：展示 HTTP 请求头、响应状态、Cookie、会话数据和信号日志。
- **模板和静态文件追踪**：跟踪模板加载、上下文变量和静态文件使用情况。
- **缓存和信号面板**：监控缓存命中率和信号发送记录。
- **自定义面板支持**：允许开发者添加自定义调试面板。
- **非侵入性**：仅在开发环境中启用，不会影响生产代码。

## 功能
该工具栏主要用于开发阶段，提供以下核心功能：
- **实时调试**：在页面加载后自动弹出工具栏，显示调试数据，无需修改代码。
- **查询优化**：高亮慢查询和 N+1 查询问题，支持复制 SQL 语句。
- **资源使用统计**：包括内存使用、渲染时间和重定向追踪。
- **集成性强**：兼容 Django 的 ORM、第三方库（如 Celery），并支持自定义配置。
- **可视化界面**：工具栏可折叠、拖拽，支持主题切换（浅色/深色模式）。

## 用法
### 安装
1. 通过 pip 安装：
   ```
   pip install django-debug-toolbar
   ```

2. 在 `settings.py` 中添加应用：
   ```python
   INSTALLED_APPS = [
       # ... 其他应用
       'debug_toolbar',
   ]
   ```

3. 添加中间件（Django 3.2+）：
   ```python
   MIDDLEWARE = [
       # ... 其他中间件
       'debug_toolbar.middleware.DebugToolbarMiddleware',
   ]
   ```

4. 配置内部 IP（仅开发环境）：
   ```python
   INTERNAL_IPS = ['127.0.0.1']
   ```

### 配置
- 可选：自定义工具栏面板，在 `settings.py` 中设置 `DEBUG_TOOLBAR_PANELS` 列表。
- 启用后，重启开发服务器，访问 Django 页面时工具栏将自动出现（需确保 `DEBUG=True`）。

### 使用示例
在浏览器中，工具栏会显示在页面右侧。点击面板可展开详细信息，例如 SQL 面板会列出所有查询，便于复制和分析。生产环境中，通过 `DEBUG=False` 或移除中间件禁用。