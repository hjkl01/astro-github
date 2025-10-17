
---
title: django-mongoengine
---

# django-mongoengine 项目

**项目地址:** [https://github.com/MongoEngine/django-mongoengine](https://github.com/MongoEngine/django-mongoengine)

## 主要特性
django-mongoengine 是一个将 MongoEngine（一个 Python 的 MongoDB ODM 库）与 Django 框架集成的扩展。它允许开发者在 Django 项目中使用 MongoDB 作为后端数据库，而无需依赖传统的 SQL 关系型数据库。主要特性包括：

- **无缝集成 Django ORM**：支持 Django 的模型定义、迁移和查询语法，同时使用 MongoDB 的 NoSQL 特性。
- **MongoDB 原生支持**：利用 MongoEngine 的文档式数据模型，提供灵活的 schema 设计、嵌入式文档和地理空间查询等功能。
- **Django 管理界面兼容**：自动生成 Django Admin 接口，支持 MongoDB 数据的 CRUD 操作。
- **查询优化**：结合 Django 的 QuerySet API 和 MongoEngine 的查询方法，实现高效的数据检索和聚合。
- **认证与授权**：集成 Django 的用户认证系统，支持基于 MongoDB 的用户模型。
- **测试支持**：提供测试工具，便于在 Django 测试环境中使用 MongoDB。
- **兼容性**：支持 Django 3.x+ 版本和 PyMongo 驱动，确保与现代 Django 生态兼容。

## 主要功能
- **模型定义**：使用 `Document` 类（继承自 MongoEngine）定义 Django 模型，支持字段类型如字符串、整数、数组、引用等。
- **数据库连接**：通过 Django 的 `settings.py` 配置 MongoDB 连接，支持多数据库和副本集。
- **查询与操作**：支持 Django 风格的过滤、排序、分页，以及 MongoDB 的高级查询如聚合管道（aggregation）。
- **表单集成**：与 Django Forms 兼容，允许基于 MongoDB 模型生成表单。
- **中间件与信号**：提供信号处理和中间件扩展，支持自定义行为如预保存钩子。
- **REST API 支持**：易于与 Django REST Framework 结合，构建基于 MongoDB 的 API。

## 用法
1. **安装**：
   ```
   pip install django-mongoengine
   ```

2. **配置 Django 设置**（在 `settings.py` 中）：
   ```python
   from mongoengine import connect

   DATABASES = {
       'default': {
           'ENGINE': 'djongo',  # 或直接使用 mongoengine 连接
           'NAME': 'your_db_name',
       }
   }

   # MongoEngine 连接
   connect('your_db_name', host='mongodb://localhost:27017/')
   ```

3. **定义模型**（在 `models.py` 中）：
   ```python
   from mongoengine import Document, StringField, IntField
   from django_mongoengine import Document as DjangoDocument

   class User(DjangoDocument):
       name = StringField(max_length=50)
       age = IntField()

       meta = {'collection': 'users'}  # 指定集合名
   ```

4. **使用查询**：
   ```python
   from .models import User

   # 创建对象
   user = User(name='Alice', age=30)
   user.save()

   # 查询
   users = User.objects.filter(age__gt=25)
   for user in users:
       print(user.name)
   ```

5. **Admin 集成**（在 `admin.py` 中）：
   ```python
   from django.contrib import admin
   from .models import User

   admin.site.register(User)
   ```

6. **运行迁移**：由于 MongoDB 无 schema 迁移，直接使用 `python manage.py runserver` 启动应用。更多高级用法请参考项目文档。