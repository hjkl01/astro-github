
---
title: lin-cms-flask
---

# Lin CMS Flask 项目

## 项目地址
[GitHub 项目地址](https://github.com/TaleLin/lin-cms-flask)

## 主要特性
Lin CMS Flask 是一个基于 Flask 框架的轻量级 CMS（内容管理系统）后端项目，专为快速开发内容管理系统设计。它采用模块化架构，支持 RESTful API 接口，强调简洁性和可扩展性。主要特性包括：
- **权限管理**：内置角色-based 访问控制（RBAC），支持用户、角色和权限的灵活配置。
- **多用户支持**：支持用户注册、登录、权限分配，适用于多租户场景。
- **内容管理**：提供文章、页面、分类等内容模型的 CRUD 操作。
- **插件化设计**：易于扩展，支持自定义模块和插件。
- **接口友好**：所有功能通过 API 暴露，便于前端集成（如 Vue.js 或 React）。
- **数据库支持**：默认使用 SQLAlchemy ORM，支持 MySQL、PostgreSQL 等数据库。
- **安全性**：集成 JWT 认证、密码加密和 CSRF 防护。

## 主要功能
- **用户管理**：用户创建、编辑、删除、登录/登出、个人信息管理。
- **角色与权限**：角色分配、权限组管理、动态权限检查。
- **内容模块**：文章发布、编辑、标签/分类管理、富文本编辑支持。
- **日志与审计**：操作日志记录、系统事件跟踪。
- **文件上传**：支持图片、文件上传和存储管理（集成云存储可选）。
- **API 文档**：内置 Swagger 或类似工具生成接口文档。
- **配置管理**：系统参数配置、环境变量支持。

## 用法
### 安装与环境准备
1. 克隆仓库：`git clone https://github.com/TaleLin/lin-cms-flask.git`
2. 进入项目目录：`cd lin-cms-flask`
3. 安装依赖：`pip install -r requirements.txt`（确保 Python 3.6+ 和虚拟环境）
4. 配置数据库：在 `config.py` 或环境变量中设置数据库连接（如 `SQLALCHEMY_DATABASE_URI`）。

### 运行项目
1. 初始化数据库：运行 `flask db init`、`flask db migrate` 和 `flask db upgrade`（需安装 Flask-Migrate）。
2. 创建超级管理员：使用脚本或命令行创建初始用户（参考 `manage.py` 或文档）。
3. 启动服务器：`flask run` 或 `python app.py`，默认监听 `http://127.0.0.1:5000`。
4. 测试 API：使用 Postman 或 curl 调用接口，例如登录：`POST /api/v1/auth/login`。

### 开发与扩展
- **自定义功能**：在 `app/modules` 目录下添加新模块，注册 Blueprint。
- **前端集成**：项目提供 API，可与 Lin CMS 前端（如 Vue 版）对接。
- **部署**：支持 Docker 部署（查看 `Dockerfile`），或使用 Gunicorn + Nginx 在生产环境运行。
- **文档参考**：项目 README 和 `/docs` 目录提供详细 API 示例和配置指南。

更多细节请查看项目 GitHub 仓库的 README.md 文件。