---
title: fastapi
---

# fastapi_amis_admin 项目

## 项目地址
[GitHub 项目地址](https://github.com/amisadmin/fastapi_amis_admin)

## 主要特性
- **基于 FastAPI 和 Amis 框架**：结合 FastAPI 的高性能 API 框架与 Amis 的低代码前端构建工具，实现快速开发后台管理系统。
- **自动生成 CRUD 接口**：支持基于 SQLAlchemy 模型自动生成增删改查（CRUD）操作，简化后端开发。
- **可视化页面配置**：使用 Amis 的 JSON 配置方式，轻松构建复杂的前端页面，无需编写前端代码。
- **权限管理和用户认证**：内置 JWT 认证、角色-based 访问控制（RBAC），支持自定义权限策略。
- **多数据库支持**：兼容 SQLAlchemy 支持的各种数据库，如 SQLite、PostgreSQL、MySQL 等。
- **插件化架构**：可扩展插件系统，便于集成第三方服务或自定义功能。
- **实时预览和调试**：提供开发模式下的实时页面预览和 API 调试工具。

## 主要功能
- **后台管理面板**：一键生成完整的 Admin 界面，包括数据列表、表单编辑、搜索过滤等。
- **API 文档自动生成**：集成 Swagger/OpenAPI，支持自动生成交互式 API 文档。
- **文件上传与管理**：支持多文件上传、存储策略配置（如本地或云存储）。
- **国际化支持**：内置多语言切换功能，便于全球化应用开发。
- **日志和监控**：记录操作日志，提供基本的性能监控和错误追踪。
- **自定义扩展**：允许开发者通过 Python 代码或 Amis 配置扩展页面和功能。

## 用法
1. **安装依赖**：
   - 确保 Python 3.8+ 环境。
   - 使用 pip 安装：`pip install fastapi_amis_admin`。
   - 安装数据库驱动（如 `pip install sqlalchemy`）。

2. **项目初始化**：
   - 创建 FastAPI 应用实例：`from fastapi import FastAPI; app = FastAPI()`。
   - 导入并配置 AmisAdmin：`from fastapi_amis_admin.admin import amis_admin; admin = amis_admin(app)`。
   - 定义 SQLAlchemy 模型，例如用户模型，并注册到 Admin 中：`admin.add_model(User)`。

3. **运行应用**：
   - 使用 Uvicorn 启动：`uvicorn main:app --reload`。
   - 访问 `http://localhost:8000/admin/` 进入管理面板。
   - 配置数据库连接：在 `app.add_middleware` 或模型中设置。

4. **自定义页面**：
   - 使用 Amis JSON Schema 配置页面，例如在路由中返回 Amis 页面定义。
   - 示例：`@admin.page("/custom") def custom_page(): return {"type": "page", "body": {...}}`。

5. **扩展与部署**：
   - 添加自定义 API 路由：`@app.get("/api/custom")`。
   - 部署时配置环境变量，如数据库 URL 和密钥。
   - 参考官方文档中的高级用法，如集成 Redis 缓存或自定义认证。