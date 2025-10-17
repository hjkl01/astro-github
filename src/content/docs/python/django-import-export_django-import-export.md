
---
title: django-import-export
---

# django-import-export 项目

## 项目地址
[GitHub 项目地址](https://github.com/django-import-export/django-import-export)

## 主要特性
django-import-export 是一个 Django 应用程序，旨在提供导入和导出数据的工具。它支持多种数据格式，并与 Django 的模型和管理员界面无缝集成。主要特性包括：

- **多种格式支持**：内置支持 CSV、JSON、YAML、XLS 和 XLSX 等格式，便于数据交换。
- **模型集成**：直接与 Django ORM 模型交互，支持自定义导入/导出逻辑。
- **管理员界面集成**：在 Django Admin 中提供导入/导出按钮，简化数据管理。
- **自定义资源类**：通过 Resource 类定义数据映射、验证和转换规则。
- **批量处理**：支持大批量数据导入/导出，优化性能。
- **错误处理**：提供详细的错误报告和验证机制，确保数据完整性。
- **插件扩展**：支持第三方插件，如用于更高级格式的扩展。

## 主要功能
- **数据导出**：从 Django 模型导出数据到指定格式的文件，支持过滤和自定义字段。
- **数据导入**：从文件导入数据到模型，支持干运行（dry-run）模式预览更改。
- **验证与转换**：在导入过程中验证数据类型、唯一性和自定义规则，并允许数据转换。
- **Admin 集成**：在模型的 Admin 类中添加导入/导出功能，无需额外视图。
- **命令行支持**：通过 Django 管理命令实现自动化导入/导出任务。

## 用法
### 安装
1. 通过 pip 安装：
   ```
   pip install django-import-export
   ```
2. 在 `settings.py` 中添加应用：
   ```python
   INSTALLED_APPS = [
       # ...
       'import_export',
   ]
   ```

### 基本用法
1. **定义 Resource 类**：为模型创建一个 Resource 子类。
   ```python
   from import_export import resources
   from .models import Book

   class BookResource(resources.ModelResource):
       class Meta:
           model = Book
           fields = ('id', 'title', 'author', 'price')
   ```

2. **在 Admin 中集成**：
   ```python
   from django.contrib import admin
   from import_export.admin import ImportExportModelAdmin
   from .resources import BookResource

   @admin.register(Book)
   class BookAdmin(ImportExportModelAdmin):
       resource_class = BookResource
   ```

3. **导出数据**：
   - 在 Admin 界面点击“Export”按钮，选择格式下载文件。
   - 程序化导出：
     ```python
     from .resources import BookResource
     dataset = BookResource().export()
     print(dataset.csv)
     ```

4. **导入数据**：
   - 在 Admin 界面点击“Import”按钮，上传文件并预览。
   - 程序化导入：
     ```python
     from io import StringIO
     from .resources import BookResource

     data = StringIO("id,title,author,price\n1,Django Book,Author1,29.99")
     result = BookResource().import_data(data, dry_run=True)  # dry_run=True 为预览模式
     ```

### 高级用法
- **自定义字段处理**：在 Resource 中重写 `dehydrate`（导出时）和 `for_row`（导入时）方法。
- **使用管理命令**：运行 `python manage.py import_export_action` 来处理导入/导出任务。
- **处理大文件**：使用 `import_export.formats.base.Format` 自定义格式，或启用分页以避免内存问题。

更多细节请参考项目文档。