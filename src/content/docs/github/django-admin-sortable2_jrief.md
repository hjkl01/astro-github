
---
title: django-admin-sortable2
---

# django-admin-sortable2 项目

## 项目地址
[GitHub 项目地址](https://github.com/jrief/django-admin-sortable2)

## 主要特性
django-admin-sortable2 是一个 Django 扩展库，旨在为 Django 管理后台（Admin）提供拖拽排序功能。它基于 Sortable.js 库实现，支持模型实例的顺序调整，提高了数据管理的效率。主要特性包括：
- **拖拽排序支持**：在 Admin 界面中，用户可以通过拖拽直接调整模型记录的顺序，无需手动编辑数值字段。
- **嵌套排序**：支持多级嵌套的排序，例如树状结构模型（如菜单或分类）。
- **批量操作集成**：与 Django Admin 的批量操作无缝集成，便于大规模数据排序。
- **自定义排序字段**：允许指定自定义的排序字段（如 `order` 或 `position`），并自动维护排序值。
- **兼容性强**：适用于 Django 的 Inline 模式（TabularInline 和 StackedInline），并支持多模型关联。
- **无侵入性**：最小化对现有模型的修改，只需简单配置即可启用。

## 主要功能
- **Admin 列表视图排序**：在模型的 changelist 视图中启用拖拽排序，用户可以直观地重新排列记录。
- **Inline 排序**：在父模型的编辑页面中，对子模型实例进行拖拽排序，例如在文章编辑中排序标签或图片。
- **树状结构支持**：通过 `TreeAdmin` 类处理具有父子关系的模型，实现层级拖拽。
- **AJAX 更新**：排序操作通过 AJAX 实时更新数据库，避免页面刷新。
- **权限控制**：继承 Django Admin 的权限系统，仅允许有权限的用户进行排序操作。

## 用法
### 安装
1. 通过 pip 安装：
   ```
   pip install django-admin-sortable2
   ```
2. 在 Django 的 `settings.py` 中添加应用：
   ```python
   INSTALLED_APPS = [
       # ... 其他应用
       'sortables',
       # ... 你的应用
   ]
   ```

### 配置模型
1. 在模型中添加排序字段（可选，如果未指定将使用默认）：
   ```python
   from django.db import models

   class MyModel(models.Model):
       name = models.CharField(max_length=100)
       order = models.PositiveIntegerField(default=0, blank=True, null=True)
       class Meta:
           ordering = ['order']
   ```

2. 在 `admin.py` 中注册 Admin 类：
   ```python
   from sortables.admin import SortableAdmin
   from .models import MyModel

   @admin.register(MyModel)
   class MyModelAdmin(SortableAdmin):
       list_display = ['name']
       sortable_field_name = 'order'  # 指定排序字段
   ```

### Inline 使用
对于 Inline 排序：
```python
from sortables.admin import SortableTabularInline
from .models import ChildModel

class ChildModelInline(SortableTabularInline):
    model = ChildModel
    sortable_field_name = 'order'
    extra = 1
```

### 树状模型
如果模型有父子关系，使用 `TreeSortableAdmin`：
```python
from sortables.admin import TreeSortableAdmin

@admin.register(MyTreeModel)
class MyTreeModelAdmin(TreeSortableAdmin):
    pass
```

更多细节请参考项目文档。