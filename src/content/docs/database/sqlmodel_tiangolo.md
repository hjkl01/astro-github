
---
title: sqlmodel
---

# SQLModel 项目

## 项目地址
[GitHub 项目地址](https://github.com/tiangolo/sqlmodel)

## 主要特性
SQLModel 是由 Tiango 开发的 Python 库，它结合了 SQLAlchemy 的 ORM 功能和 Pydantic 的数据验证能力。主要特性包括：
- **无缝集成**：将数据库模型与 Pydantic 模型统一，支持类型提示和自动验证。
- **类型安全**：充分利用 Python 的类型系统，确保代码的可靠性和 IDE 支持。
- **简单高效**：简化数据库操作，支持异步操作（通过 SQLAlchemy 的异步支持）。
- **灵活性**：支持关系型数据库如 PostgreSQL、SQLite 等，提供声明式模型定义。
- **验证与序列化**：内置数据验证、序列化和反序列化功能，减少 boilerplate 代码。

## 主要功能
- **模型定义**：使用装饰器 `@sqlmodel` 定义数据库表模型，同时作为 Pydantic 模型使用。
- **CRUD 操作**：提供创建、读取、更新、删除（Create, Read, Update, Delete）数据库记录的便捷方法。
- **查询构建**：支持复杂的 SQL 查询，通过链式 API 构建查询。
- **关系管理**：处理模型间的关系，如一对多、多对多。
- **事务支持**：集成 SQLAlchemy 的会话管理和事务处理。
- **异步支持**：兼容 async/await 语法，适用于高性能应用。

## 用法
### 安装
```bash
pip install sqlmodel
```

### 基本用法示例
1. **定义模型**：
   ```python
   from sqlmodel import SQLModel, Field, create_engine, Session
   from typing import Optional

   class Hero(SQLModel, table=True):
       id: Optional[int] = Field(default=None, primary_key=True)
       name: str
       secret_name: str
       age: Optional[int] = None
   ```

2. **创建数据库和会话**：
   ```python
   engine = create_engine("sqlite:///database.db")
   SQLModel.metadata.create_all(engine)

   with Session(engine) as session:
       hero = Hero(name="Deadpond", secret_name="Dive Wilson")
       session.add(hero)
       session.commit()
       session.refresh(hero)
       print(hero.id)
   ```

3. **查询数据**：
   ```python
   with Session(engine) as session:
       heroes = session.exec(select(Hero)).all()
       for hero in heroes:
           print(hero.name)
   ```

更多用法请参考官方文档：https://sqlmodel.tiangolo.com/