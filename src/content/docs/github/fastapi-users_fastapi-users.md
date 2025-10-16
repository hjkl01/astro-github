
---
title: fastapi-users
---

# FastAPI Users 项目

## 项目地址
[GitHub 项目地址](https://github.com/fastapi-users/fastapi-users)

## 主要特性
FastAPI Users 是一个用于 FastAPI 框架的开源用户认证和授权库，旨在简化用户管理流程。它基于 FastAPI 的依赖注入系统，提供高效、现代化的认证解决方案。主要特性包括：
- **多认证后端支持**：内置 JWT（JSON Web Tokens）和 Cookie 认证，支持 OAuth2 集成（如 Google、GitHub 等）。
- **用户模型灵活性**：支持 SQLAlchemy、Tortoise-ORM、MongoDB 等数据库后端，用户模型可自定义。
- **完整 CRUD 操作**：提供用户创建、读取、更新、删除（CRUD）的 API 端点，自动生成 OpenAPI 文档。
- **密码安全**：集成 Argon2 等哈希算法，确保密码安全存储和验证。
- **角色与权限管理**：支持用户角色分配和基于角色的访问控制（RBAC）。
- **异步支持**：完全异步设计，与 FastAPI 的高性能特性无缝集成。
- **易于扩展**：模块化设计，便于添加自定义逻辑，如电子邮件验证或双因素认证。

## 主要功能
- **用户注册与登录**：处理用户注册、登录、注销，支持电子邮件/用户名认证。
- **用户管理 API**：自动生成 RESTful API，用于管理用户数据，包括密码重置和个人信息更新。
- **认证中间件**：提供依赖注入的认证装饰器，确保 API 端点的安全性。
- **OAuth2 集成**：简化第三方登录流程，支持社交媒体认证。
- **事件系统**：允许在用户生命周期事件（如注册后）触发自定义操作，例如发送欢迎邮件。
- **多租户支持**：可扩展为支持多租户架构。

## 用法
### 安装
使用 pip 安装核心库和所需数据库后端：
```
pip install fastapi-users[sqlalchemy]  # 示例：SQLAlchemy 后端
```

### 基本配置
1. **定义用户模型**：使用 SQLAlchemy 或其他 ORM 创建用户模型，例如：
   ```python
   from fastapi_users.db import SQLAlchemyBaseUserTable
   from sqlalchemy import Column, Integer, String

   class User(SQLAlchemyBaseUserTable[int], table_args=None):
       id = Column(Integer, primary_key=True, index=True)
       email = Column(String, nullable=False)
       hashed_password = Column(String, nullable=False)
   ```

2. **创建数据库和用户管理器**：
   ```python
   from fastapi_users import FastAPIUsers
   from fastapi_users.authentication import JWTAuthentication
   from fastapi_users.db import SQLAlchemyUserDatabase

   SECRET = "your-secret-key"
   database = SQLAlchemyUserDatabase(User, database_url="sqlite:///./test.db")
   jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
   fastapi_users = FastAPIUsers(
       [jwt_authentication],
       [database],
       User,
       UserCreate,
       UserUpdate,
       UserDB,
   )
   ```

3. **集成到 FastAPI 应用**：
   ```python
   from fastapi import FastAPI

   app = FastAPI()
   app.include_router(
       fastapi_users.get_auth_router(jwt_authentication),
       prefix="/auth/jwt",
       tags=["auth"],
   )
   app.include_router(
       fastapi_users.get_register_router(),
       prefix="/auth",
       tags=["auth"],
   )
   app.include_router(
       fastapi_users.get_users_router(),
       prefix="/users",
       tags=["users"],
   )
   ```

4. **保护路由**：
   ```python
   current_user = fastapi_users.current_user(active=True)
   @app.get("/protected-route")
   def protected_route(current_user: User = Depends(current_user)):
       return f"Hello, {current_user.email}"
   ```

### 高级用法
- **自定义验证**：在用户模型中添加 before_create 钩子进行电子邮件验证。
- **OAuth2 路由**：添加 `get_oauth_router(google_oauth_client)` 以支持 Google 登录。
- **测试**：库提供测试工具，如模拟数据库用于单元测试。

更多细节请参考官方文档：https://fastapi-users.github.io/fastapi-users/