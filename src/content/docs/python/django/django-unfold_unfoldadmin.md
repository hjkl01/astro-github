---
title: django-unfold
---

# Django Unfold 项目

**GitHub 项目地址:** [https://github.com/unfoldadmin/django-unfold](https://github.com/unfoldadmin/django-unfold)

## 主要特性
Django Unfold 是一个现代化的 Django 管理界面（Admin）主题，旨在提升 Django 默认管理界面的用户体验。它基于 Material Design 原则，提供简洁、直观的设计，支持响应式布局，适用于桌面和移动设备。主要特性包括：
- **现代 UI 设计**：采用 Material Design 风格，包含卡片式布局、阴影效果和流畅的动画，提升视觉吸引力。
- **响应式与移动友好**：界面自动适应不同屏幕尺寸，支持触摸操作，便于在手机或平板上管理数据。
- **自定义主题**：支持浅色和深色模式切换，用户可根据偏好调整界面主题。
- **增强功能集成**：无缝集成 Django 的内置功能，如搜索、过滤、排序和分页，同时优化了表单和列表视图的交互。
- **易扩展**：允许开发者自定义图标、颜色和布局，而不影响核心代码。
- **性能优化**：轻量级实现，加载速度快，不增加显著的性能开销。
- **国际化支持**：兼容 Django 的 i18n 框架，支持多语言界面。

## 功能
Django Unfold 主要用于替换或增强 Django 的默认管理后台，提供以下核心功能：
- **管理模型界面**：改进模型列表、详情和编辑页面，支持批量操作和快速导航。
- **侧边栏导航**：引入左侧侧边栏，用于快速访问不同应用和模型，减少页面跳转。
- **搜索与过滤**：增强搜索栏，支持高级过滤器和实时结果预览。
- **表单处理**：优化表单渲染，包括内联编辑、文件上传和验证反馈。
- **权限管理**：保留 Django 的用户权限系统，同时提供更直观的权限界面。
- **仪表盘**：可选的自定义仪表盘，用于显示关键指标和快捷链接。
- **集成第三方**：兼容流行 Django 扩展，如 Django REST Framework 的管理视图。

## 用法
1. **安装**：
   - 通过 pip 安装：`pip install django-unfold`
   - 或从 GitHub 克隆仓库并安装。

2. **配置 Django 项目**：
   - 在 `settings.py` 中添加 `'unfold'` 到 `INSTALLED_APPS` 的顶部（在 `'django.contrib.admin'` 之前）：
     ```python
     INSTALLED_APPS = [
         'unfold',
         'django.contrib.admin',
         # 其他应用
     ]
     ```
   - 添加 Unfold 的 URL 配置到 `urls.py`：
     ```python
     from django.urls import path, include

     urlpatterns = [
         path('admin/', include('unfold.urls')),
         path('unfold/', include('unfold.urls')),  # 可选，用于独立入口
     ]
     ```

3. **自定义（可选）**：
   - 在 `settings.py` 中配置主题选项，例如：
     ```python
     UNFOLD = {
         "SITE_TITLE": "我的管理后台",
         "SITE_HEADER": "欢迎使用 Unfold",
         "SITE_URL": "/",
         "SITE_ICON": {
             "light": "/static/myapp/favicon-light.svg",
             "dark": "/static/myapp/favicon-dark.svg",
         },
         "COLORS": {
             "primary": "#007bff",
         },
         "ENABLED_THEMES": ["dark", "light"],
     }
     ```
   - 为模型添加自定义图标或样式：在模型的 `Meta` 类中指定 `unfold` 属性。

4. **运行与访问**：
   - 运行 Django 开发服务器：`python manage.py runserver`
   - 通过 `/admin/` 访问增强的管理界面。首次登录需创建超级用户：`python manage.py createsuperuser`。

更多细节请参考项目文档：https://github.com/unfoldadmin/django-unfold/blob/main/README.md