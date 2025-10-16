
---
title: flask-jwt-extended
---

# Flask-JWT-Extended 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/vimalloc/flask-jwt-extended)

## 主要特性
Flask-JWT-Extended 是 Flask 应用程序的 JWT（JSON Web Token）认证扩展库，旨在提供更灵活和强大的 JWT 处理功能。它基于 PyJWT 库构建，支持多种 JWT 实现方式，包括访问令牌（Access Token）和刷新令牌（Refresh Token）。主要特性包括：
- **多令牌支持**：同时处理访问令牌和刷新令牌，允许用户在令牌过期时无缝刷新。
- **自定义声明（Claims）**：支持在 JWT 中添加自定义数据，如用户角色、权限等。
- **黑名单和令牌撤销**：内置黑名单机制，用于立即撤销特定令牌，提高安全性。
- **多种存储后端**：支持 Redis、SQLAlchemy 等后端存储黑名单和刷新令牌。
- **保护视图**：易于使用装饰器（如 `@jwt_required()`）保护 Flask 路由，支持可选令牌验证。
- **令牌位置灵活**：令牌可以从请求头、Cookie、查询参数或 JSON 体中提取。
- **异常处理**：提供详细的异常类，便于自定义错误响应。
- **OAuth2 支持**：兼容 OAuth2 风格的令牌验证。

该库强调安全性，默认使用 HS256 算法签名，并支持 RSA/EC 等非对称加密。

## 主要功能
- **令牌生成**：创建访问令牌和刷新令牌，支持设置过期时间和自定义负载。
- **令牌验证**：验证令牌的有效性、签名和过期状态，支持获取当前用户身份。
- **令牌刷新**：自动或手动刷新过期访问令牌，使用刷新令牌生成新令牌。
- **用户身份管理**：通过 `current_identity` 获取当前认证用户，支持多用户上下文。
- **令牌黑名单**：将无效令牌加入黑名单，防止重用。
- **视图保护**：装饰器保护路由，支持角色-based 访问控制（RBAC）。
- **集成扩展**：与 Flask-Login、SQLAlchemy 等无缝集成。

## 用法示例
### 安装
```bash
pip install flask-jwt-extended
```

### 基本配置
在 Flask 应用中初始化：
```python
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 生产环境使用环境变量
jwt = JWTManager(app)
```

### 生成令牌
```python
from flask_jwt_extended import create_access_token, create_refresh_token

@app.route('/login', methods=['POST'])
def login():
    # 假设验证用户凭证成功
    access_token = create_access_token(identity='user_id')  # identity 可以是用户 ID 或对象
    refresh_token = create_refresh_token(identity='user_id')
    return {'access_token': access_token, 'refresh_token': refresh_token}
```

### 保护路由
```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/protected')
@jwt_required()  # 要求访问令牌
def protected():
    current_user_id = get_jwt_identity()
    return {'message': f'Hello, {current_user_id}!'}, 200
```

### 刷新令牌
```python
from flask_jwt_extended import jwt_required, create_access_token, get_jwt

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # 要求刷新令牌
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return {'access_token': new_access_token}
```

### 自定义声明
```python
access_token = create_access_token(
    identity='user_id',
    additional_claims={'roles': ['admin']}  # 添加自定义声明
)
```

更多高级用法，请参考项目文档中的完整指南。