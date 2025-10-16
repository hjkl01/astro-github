
---
title: django-grappelli
---

# Django Grappelli 项目

## 项目地址
[GitHub 项目地址](https://github.com/sehmaschine/django-grappelli)

## 主要特性
Django Grappelli 是一个流行的 Django 管理界面（Admin）皮肤和增强工具包。它基于 Django 的内置 Admin 系统，提供了一个更现代、用户友好的界面设计。主要特性包括：
- **现代化界面**：采用响应式设计，支持移动设备，界面更美观、直观，使用 jQuery UI 和其他前端库增强交互性。
- **改进的导航和布局**：优化了侧边栏导航、搜索栏和过滤器，支持可折叠的菜单和更好的面包屑导航。
- **增强的功能**：内置文件上传器（支持拖拽上传）、内联编辑（Inline）改进、自动完成功能，以及更好的权限管理和用户界面自定义。
- **主题支持**：提供默认主题，并允许开发者自定义 CSS 和模板以匹配项目需求。
- **兼容性**：支持 Django 的多个版本（从 1.11 到最新），并与第三方应用集成良好，如 Django 的文件管理器。

## 功能
- **Admin 界面美化**：替换默认的 Django Admin 模板，提供更专业的后台管理面板。
- **文件和媒体管理**：集成 Grappelli 的文件浏览器，支持图片预览和批量操作。
- **搜索和过滤优化**：增强搜索功能，支持 AJAX 加载和高级过滤器。
- **权限和用户管理**：改进用户组、权限分配的界面，便于管理员操作。
- **插件扩展**：可以与其他 Django 扩展结合，如 django-filebrowser，用于更高级的文件处理。
- **国际化支持**：支持多语言，包括中文界面翻译。

## 用法
1. **安装**：
   - 使用 pip 安装：`pip install django-grappelli`。
   - 在 Django 项目的 `settings.py` 中添加 `'grappelli'` 到 `INSTALLED_APPS` 的首位（在 `'django.contrib.admin'` 之前）：
     ```
     INSTALLED_APPS = [
         'grappelli',
         'django.contrib.admin',
         # 其他应用
     ]
     ```

2. **配置 URL**：
   - 在 `urls.py` 中包含 Grappelli 的 URL 配置：
     ```
     from django.contrib import admin
     from django.urls import path

     urlpatterns = [
         path('grappelli/', include('grappelli.urls')),
         path('admin/', admin.site.urls),
     ]
     ```

3. **运行迁移**：
   - 执行 `python manage.py migrate` 以应用任何必要的数据库变更。

4. **自定义**：
   - 在 `settings.py` 中配置 Grappelli 选项，例如：
     ```
     GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
         'yourapp.YourModel': ['field1', 'field2']
     }
     ```
   - 访问 `/admin/` 即可看到新界面。开发者可以覆盖模板文件（在 `templates/admin/`）进行进一步自定义。

5. **注意事项**：
   - 确保 jQuery 和其他依赖已加载（Grappelli 会自动处理）。
   - 如果使用与其他 Admin 皮肤冲突的应用，可能需要调整加载顺序。
   - 文档详见 GitHub 仓库的 README 和官方文档。