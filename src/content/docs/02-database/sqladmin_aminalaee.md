
---
title: sqladmin
---

# SQLAdmin 项目

**GitHub 项目地址:** [https://github.com/aminalaee/sqladmin](https://github.com/aminalaee/sqladmin)

## 主要特性
SQLAdmin 是一个基于 Python 的轻量级 SQL 数据库管理界面，专为 FastAPI 框架设计。它提供了一个现代化的 Web 界面，用于管理和操作 SQL 数据库，而无需编写额外的后端代码。主要特性包括：
- **自动生成的 CRUD 接口**：基于数据库模型自动生成创建、读取、更新和删除操作的界面。
- **支持多种数据库**：兼容 SQLAlchemy 支持的数据库，如 PostgreSQL、MySQL、SQLite 等。
- **集成 FastAPI**：无缝集成到 FastAPI 应用中，支持异步操作。
- **响应式 UI**：使用现代前端技术（如 Vue.js）构建，界面简洁、响应迅速，支持移动端访问。
- **权限控制**：内置用户认证和角色管理，支持 JWT 或其他认证方式。
- **搜索和过滤**：提供高级搜索、排序和过滤功能，便于数据浏览。
- **自定义扩展**：允许开发者自定义视图、字段和行为。

## 主要功能
- **数据库浏览和管理**：可视化显示表结构、数据记录，支持分页和实时查询。
- **模型管理**：自动从 SQLAlchemy 模型生成管理面板，支持关系型数据（如外键）的可视化编辑。
- **批量操作**：支持批量导入、导出数据，以及执行自定义 SQL 查询。
- **监控和日志**：内置查询日志和性能监控，帮助优化数据库操作。
- **主题和国际化**：支持自定义主题和多语言（包括中文）。

## 用法
1. **安装**：
   使用 pip 安装：`pip install sqladmin`。

2. **基本配置**：
   在 FastAPI 应用中导入并初始化：
   ```python
   from fastapi import FastAPI
   from sqladmin import Admin, ModelView
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   engine = create_engine("sqlite:///example.db")
   SessionLocal = sessionmaker(bind=engine)
   Base = declarative_base()

   # 定义模型
   class User(Base):
       __tablename__ = "users"
       id = Column(Integer, primary_key=True)
       name = Column(String)

   Base.metadata.create_all(engine)

   app = FastAPI()
   admin = Admin(app, engine)

   # 注册模型视图
   class UserAdmin(ModelView, model=User):
       column_list = [User.id, User.name]

   admin.add_view(UserAdmin)
   ```

3. **运行应用**：
   启动 FastAPI 服务器：`uvicorn main:app --reload`。访问 `/admin` 路径即可进入管理界面。

4. **高级用法**：
   - 配置认证：通过 `Admin` 的 `auth_view` 参数添加登录页面。
   - 自定义视图：继承 `ModelView` 类重写方法，如添加搜索字段或验证逻辑。
   - 部署：支持 Docker 部署，参考项目文档中的示例。

更多细节请参考项目 README 和官方文档。