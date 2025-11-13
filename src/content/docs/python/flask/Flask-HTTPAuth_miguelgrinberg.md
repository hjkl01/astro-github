---
title: Flask-HTTPAuth
---

# Flask-HTTPAuth 项目

## 项目地址
[GitHub 项目地址](https://github.com/miguelgrinberg/Flask-HTTPAuth)

## 主要特性
Flask-HTTPAuth 是一个轻量级的 Flask 扩展，用于实现 HTTP 认证机制。它支持基本的 HTTP 认证协议，包括 Basic Authentication 和 Digest Authentication，提供简单、灵活的方式为 Flask 应用添加身份验证功能。主要特性包括：
- **Basic Authentication 支持**：使用用户名和密码进行简单认证，适用于内部网络或简单场景。
- **Digest Authentication 支持**：提供更安全的哈希认证，防止密码明文传输。
- **自定义认证逻辑**：允许开发者轻松定义认证回调函数，集成自定义用户验证（如数据库查询）。
- **错误处理**：内置认证失败时的 HTTP 响应处理，支持自定义错误消息。
- **兼容性强**：与 Flask 框架无缝集成，轻量级，无需额外依赖。
- **易于扩展**：支持多种认证方案，如令牌认证或多因素认证的自定义实现。

## 主要功能
- **认证验证**：通过装饰器（如 `@auth.login_required`）保护路由，确保只有认证用户才能访问。
- **用户加载**：提供 `verify_password` 和 `load_user` 回调，用于验证凭据和加载用户对象。
- **挑战响应**：自动发送 WWW-Authenticate 头，触发浏览器认证对话框。
- **集成 Flask-Login**：可与 Flask-Login 等扩展结合，实现会话管理。
- **测试友好**：支持在测试环境中模拟认证头，便于单元测试。

## 用法
### 安装
使用 pip 安装：
```
pip install Flask-HTTPAuth
```

### 基本用法示例
1. **初始化扩展**：
   ```python
   from flask import Flask
   from flask_httpauth import HTTPBasicAuth

   app = Flask(__name__)
   auth = HTTPBasicAuth()

   users = {
       "admin": "password"  # 示例用户字典
   }

   @auth.verify_password
   def verify_password(username, password):
       if username in users and users[username] == password:
           return username
       return None

   @app.route('/')
   @auth.login_required
   def index():
       return f"欢迎, {auth.current_user()}!"
   ```

2. **Digest Authentication 示例**：
   ```python
   from flask_httpauth import HTTPDigestAuth

   auth = HTTPDigestAuth()

   @auth.get_password
   def get_password(username):
       if username == "admin":
           return "password"
       return None

   @auth.verify_password
   def verify_password(username, password):
       return get_password(username) == password
   ```

3. **运行应用**：
   访问受保护路由时，浏览器会弹出认证对话框。输入正确凭据后即可访问。

更多高级用法详见项目文档，包括自定义 realm、错误处理器和与数据库集成。