
---
title: databases
---

# Databases 项目

## 项目地址
[GitHub 项目地址](https://github.com/encode/databases)

## 主要特性
- **异步支持**：基于 async/await 语法，提供全异步的数据库操作，适用于高性能的异步 Web 框架如 Starlette 和 FastAPI。
- **多数据库兼容**：支持 PostgreSQL、MySQL、SQLite 等常见关系型数据库，以及 Redis 等 NoSQL 数据库。
- **ORM 风格**：提供类似 SQLAlchemy 的对象关系映射 (ORM) 接口，简化数据库模型定义和查询操作。
- **连接池管理**：内置高效的连接池，支持自动连接管理和事务处理，提高并发性能。
- **类型提示**：集成 Python 类型提示 (typing)，增强代码的可读性和 IDE 支持。
- **轻量级**：设计简洁，不依赖过多外部库，便于集成到现有项目中。

## 主要功能
- **模型定义**：允许用户定义数据库模型类，支持字段类型、关系（如一对多、多对多）和约束。
- **CRUD 操作**：提供创建 (Create)、读取 (Read)、更新 (Update) 和删除 (Delete) 的异步方法，支持批量操作。
- **查询构建**：使用链式 API 构建复杂查询，支持过滤、排序、分页和聚合函数。
- **事务支持**：自动管理数据库事务，确保数据一致性。
- **迁移工具**：集成 Alembic 支持数据库 schema 迁移。
- **测试友好**：内置测试数据库支持，便于单元测试。

## 用法示例
### 安装
```bash
pip install databases[postgresql]  # 以 PostgreSQL 为例
```

### 基本用法
1. **配置数据库 URL**：
   ```python
   from databases import Database

   database = Database("postgresql://user:password@localhost/dbname")
   ```

2. **定义模型**（使用 Pydantic 或直接 SQL）：
   ```python
   import databases
   import sqlalchemy

   metadata = sqlalchemy.MetaData()

   users = sqlalchemy.Table(
       "users",
       metadata,
       sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
       sqlalchemy.Column("name", sqlalchemy.String(32)),
       sqlalchemy.Column("email", sqlalchemy.String(255)),
   )
   ```

3. **连接和查询**：
   ```python
   import asyncio

   async def main():
       await database.connect()
       query = users.select()
       results = await database.fetch_all(query)
       for result in results:
           print(result)
       await database.disconnect()

   asyncio.run(main())
   ```

4. **插入数据**：
   ```python
   async def insert_user():
       query = users.insert().values(name="Alice", email="alice@example.com")
       last_record_id = await database.execute(query)
   ```

更多细节请参考项目文档。