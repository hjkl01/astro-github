---
title: django-guardian
---

# django-guardian 项目

**GitHub 项目地址:** [https://github.com/django-guardian/django-guardian](https://github.com/django-guardian/django-guardian)

## 主要特性

django-guardian 是一个 Django 应用程序，提供基于对象的权限系统。它允许为特定对象实例分配权限，而不是仅限于模型级别的权限。核心特性包括：

- **对象级权限 (Object-Level Permissions)**: 支持为单个模型实例（如特定文章或用户）分配细粒度权限，例如“可以编辑这个特定帖子”或“可以删除这个特定文件”。
- **无缝集成 Django 权限系统**: 扩展了 Django 内置的权限框架，无需修改现有代码即可使用。
- **高效查询支持**: 通过自定义的 `get_objects_for_user` 方法，优化权限检查查询，避免 N+1 查询问题。
- **匿名用户支持**: 可以为匿名用户分配对象权限。
- **缓存机制**: 支持可选的权限缓存，提高性能。
- **管理界面集成**: 提供 Django Admin 的扩展，便于在后台管理对象权限。
- **测试友好**: 包含测试工具和示例，帮助开发者快速集成。

该项目遵循 Django 的最佳实践，支持 Django 3.x 及以上版本，并提供详细的文档和示例。

## 主要功能

- **权限分配与检查**: 使用 `assign_perm` 和 `remove_perm` 函数分配/移除权限；通过 `has_perm` 方法检查用户是否具有特定权限。
- **批量操作**: 支持批量分配权限给多个对象或用户。
- **Queryset 过滤**: `get_objects_for_user` 函数返回用户有权限访问的对象 Queryset，支持自定义过滤器。
- **权限组**: 可以将权限分配给用户组，实现组级对象权限管理。
- **自定义后端**: 提供 `ObjectPermissionBackend`，可作为 Django 认证后端的补充。

这些功能使 django-guardian 特别适合需要复杂访问控制的应用，如内容管理系统 (CMS)、协作工具或多租户系统。

## 用法

### 安装

1. 通过 pip 安装：
   ```
   pip install django-guardian
   ```

2. 在 Django 的 `settings.py` 中添加应用：
   ```python
   INSTALLED_APPS = [
       # ... 其他应用
       'guardian',
   ]
   ```

3. 添加 Guardian 到认证后端：
   ```python
   AUTHENTICATION_BACKENDS = (
       'django.contrib.auth.backends.ModelBackend',  # 默认后端
       'guardian.backends.ObjectPermissionBackend',  # 对象权限后端
   )
   ```

4. 运行迁移：
   ```
   python manage.py migrate guardian
   ```

### 基本用法示例

假设有一个模型 `Article`：

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
```

#### 分配权限

```python
from guardian.shortcuts import assign_perm

# 为用户分配“可以更改”特定文章的权限
article = Article.objects.get(id=1)
user = User.objects.get(username='alice')
assign_perm('change_article', user, article)
```

#### 检查权限

```python
from guardian.shortcuts import get_objects_for_user

# 检查用户是否有权限
if user.has_perm('change_article', article):
    print("用户可以编辑此文章")

# 获取用户有权限更改的所有文章
articles = get_objects_for_user(user, 'change_article', Article)
for article in articles:
    print(article.title)
```

#### 在视图中使用

在 Django 视图中集成权限检查：

```python
from django.shortcuts import get_object_or_404
from guardian.mixins import PermissionRequiredMixin
from django.views.generic import DetailView

class ArticleDetailView(PermissionRequiredMixin, DetailView):
    model = Article
    permission_required = 'change_article'  # 或使用 get_required_objects_perm
    pk_url_kwarg = 'pk'
```

### 高级用法

- **自定义过滤器**: 使用 `GuardianQueryset` 来自定义权限过滤逻辑。
- **Admin 集成**: 在 `admin.py` 中注册模型并启用 Guardian 的权限管理：
  ```python
  from guardian.admin import GuardedModelAdmin

  class ArticleAdmin(GuardedModelAdmin):
      pass

  admin.site.register(Article, ArticleAdmin)
  ```
- **缓存配置**: 在 `settings.py` 中设置 `GUARDIAN_CACHE_ALL_PERMS = True` 以启用全局权限缓存。

更多细节请参考项目文档：[https://github.com/django-guardian/django-guardian/blob/main/README.rst](https://github.com/django-guardian/django-guardian/blob/main/README.rst)。