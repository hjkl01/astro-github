
---
title: flask-admin
---

# Flask-Admin 项目

## 项目地址
[https://github.com/flask-admin/flask-admin](https://github.com/flask-admin/flask-admin)

## 主要特性
Flask-Admin 是一个完全可配置的管理界面框架，专为 Flask 网络应用设计。它提供了一个快速构建管理界面的工具，支持模型管理、自定义视图和扩展集成。主要特性包括：
- **简单易用**：基于 Flask 的扩展，易于集成到现有项目中。
- **模型驱动**：自动生成 CRUD（创建、读取、更新、删除）界面，支持 SQLAlchemy、MongoEngine 等 ORM。
- **高度可定制**：允许自定义菜单、视图、表单和模板，支持 Bootstrap 等前端框架。
- **安全集成**：内置用户认证和权限控制，支持 Flask-Login 等扩展。
- **扩展支持**：提供文件上传、WTF 表单集成和 AJAX 支持等功能。
- **多语言支持**：内置国际化（i18n）功能，便于多语言环境部署。

## 主要功能
- **模型管理**：自动为数据库模型生成管理页面，包括列表视图、编辑表单和详情页。
- **自定义视图**：支持创建自定义页面，如仪表盘、图表或 API 端点。
- **搜索和过滤**：内置搜索栏和过滤器，支持复杂查询。
- **批量操作**：允许批量编辑、删除或导出数据。
- **媒体管理**：集成文件上传和缩略图生成。
- **权限控制**：基于角色的访问控制（RBAC），可限制特定用户的操作。

## 用法
### 安装
使用 pip 安装：
```
pip install flask-admin
```

### 基本用法
1. **初始化 Admin**：
   ```python
   from flask import Flask
   from flask_admin import Admin
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'your_secret_key'
   db = SQLAlchemy(app)

   admin = Admin(app, name='My Admin', template_mode='bootstrap3')
   ```

2. **添加模型视图**：
   ```python
   from flask_admin.contrib.sqla import ModelView

   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(50))

   admin.add_view(ModelView(User, db.session))
   ```

3. **自定义视图**：
   ```python
   from flask_admin.base import BaseView, expose

   class MyView(BaseView):
       @expose('/')
       def index(self):
           return self.render('admin/myview.html')

   admin.add_view(MyView(name='My View', category='Custom'))
   ```

4. **运行应用**：
   ```python
   if __name__ == '__main__':
       db.create_all()
       app.run(debug=True)
   ```
   访问 `/admin` 路径即可看到管理界面。可以通过配置自定义 URL 前缀和模板路径进一步调整。详细文档见项目 README 和官方文档。