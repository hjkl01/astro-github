
---
title: flask-security
---

# Flask-Security 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/Flask-Middleware/flask-security/)

## 主要特性
Flask-Security 是一个基于 Flask 的安全扩展库，旨在为 Flask 应用程序提供全面的安全功能。它集成了用户认证、授权和会话管理等核心组件，简化了 Web 应用的身份验证开发。主要特性包括：
- **用户认证与授权**：支持基于角色的访问控制 (RBAC)，允许定义用户角色和权限。
- **密码管理**：内置密码哈希、验证和重置功能，使用 Werkzeug 或其替代库进行加密。
- **会话管理**：集成 Flask-Login，支持记住我 (Remember Me) 功能和安全的会话处理。
- **多因素认证 (MFA)**：可选支持如 Google Authenticator 的两步验证。
- **OAuth 支持**：易于集成第三方 OAuth 提供商，如 Google、Facebook 等。
- **邮件集成**：自动发送注册确认、密码重置等通知邮件。
- **可扩展性**：模块化设计，支持自定义视图、模型和模板，兼容 Flask-SQLAlchemy 等 ORM。

该项目强调安全最佳实践，如 CSRF 保护、速率限制和输入验证，适用于中小型 Web 应用的安全需求。

## 主要功能
- **用户注册与登录**：提供现成的表单和视图，支持电子邮件验证。
- **密码重置与更改**：通过邮件链接处理密码恢复流程。
- **角色与权限管理**：定义用户组和权限检查，确保资源访问安全。
- **会话与注销**：处理登录状态、超时和安全注销。
- **API 保护**：支持 JWT 或基于会话的 API 认证。
- **国际化支持**：多语言模板和消息。

## 用法
### 安装
使用 pip 安装：
```
pip install flask-security
```

### 基本配置
1. **初始化 Flask 应用**：
   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_security import Security, SQLAlchemyUserDatastore
   from flask_security.models import User, Role

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'your-secret-key'
   app.config['SECURITY_PASSWORD_SALT'] = 'your-salt'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
   db = SQLAlchemy(app)

   # 定义用户和角色模型（可选，自定义）
   user_datastore = SQLAlchemyUserDatastore(db, User, Role)
   security = Security(app, user_datastore)
   ```

2. **数据库迁移**：
   初始化数据库并创建表：
   ```python
   @app.before_first_request
   def create_tables():
       db.create_all()
   ```

3. **路由与视图**：
   Flask-Security 自动提供路由，如 `/login`、`/register`。自定义模板需在 `templates/security/` 目录下放置文件。

4. **保护视图**：
   使用装饰器保护路由：
   ```python
   from flask_security import login_required, roles_required

   @app.route('/admin')
   @login_required
   @roles_required('admin')
   def admin():
       return 'Admin page'
   ```

5. **运行应用**：
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

更多高级用法详见项目文档，包括自定义模型和集成其他扩展。建议结合 Flask-Principal 等库增强功能。