---
title: fastapi-admin
---

# FastAPI-Admin 项目

## 项目地址
[GitHub 项目地址](https://github.com/fastapi-admin/fastapi-admin)

## 主要特性
FastAPI-Admin 是一个基于 FastAPI 框架的开源后台管理系统，提供了一个快速构建和管理后台界面的解决方案。它支持现代化的 Web 开发特性，包括异步处理、高性能 API 和响应式前端。主要特性包括：

- **可视化管理界面**：内置 Admin 界面，支持拖拽式配置，无需编写大量前端代码。
- **权限管理**：集成 RBAC（基于角色的访问控制）系统，支持用户、角色和权限的动态管理。
- **CRUD 操作支持**：自动生成增删改查（Create, Read, Update, Delete）界面，适用于各种数据模型。
- **多数据源支持**：兼容 SQLAlchemy、Tortoise-ORM 等 ORM 框架，便于集成现有数据库。
- **插件扩展**：模块化设计，支持自定义插件，如文件上传、图表展示等。
- **国际化与主题**：支持多语言切换和自定义主题，提升用户体验。
- **高性能**：利用 FastAPI 的异步特性，确保高效处理请求。

## 主要功能
- **用户认证与授权**：内置 JWT 认证，支持 OAuth2 集成，实现安全的登录和 API 访问控制。
- **数据模型管理**：通过 Pydantic 模型定义数据结构，自动生成 Admin 面板，支持搜索、过滤、分页和排序。
- **仪表盘与报告**：提供自定义仪表盘，支持实时数据可视化和报表生成。
- **日志与审计**：记录操作日志，便于追踪系统活动和审计。
- **API 文档**：集成 Swagger UI，自动生成交互式 API 文档。
- **部署友好**：支持 Docker 容器化部署，便于在生产环境中运行。

## 用法
### 安装
1. 确保 Python 版本 >= 3.8，并安装 FastAPI 和相关依赖。
2. 使用 pip 安装：
   ```
   pip install fastapi-admin
   ```

### 快速启动
1. 创建一个基本的 FastAPI 应用文件（如 `main.py`）：
   ```python
   from fastapi import FastAPI
   from fastapi_admin.app import app as admin_app
   from fastapi_admin.resources import Resource

   app = FastAPI(title="My Admin")

   # 定义资源（例如，用户模型）
   class UserResource(Resource):
       # 配置字段、操作等
       pass

   # 注册 Admin 应用
   app.mount("/admin", admin_app)

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)
   ```

2. 运行应用：
   ```
   python main.py
   ```

3. 访问 Admin 界面：打开浏览器，访问 `http://localhost:8000/admin`，默认使用 SQLite 数据库进行演示。初次访问需创建超级管理员账户。

### 配置与扩展
- **自定义资源**：继承 `Resource` 类，定义模型字段、显示列和操作按钮。
- **数据库集成**：配置 SQLAlchemy 或其他 ORM，替换默认数据库。
- **权限设置**：在 Admin 配置中定义角色和菜单权限。
- **高级用法**：参考官方文档，集成第三方插件或自定义视图。项目提供详细的示例代码和迁移指南，便于扩展到复杂应用场景。