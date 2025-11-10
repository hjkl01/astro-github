---
title: sqlalchemy
---

# SQLAlchemy 项目

## 项目地址
[GitHub 项目地址](https://github.com/sqlalchemy/sqlalchemy)

## 主要特性
SQLAlchemy 是一个开源的 Python SQL 工具包和对象关系映射 (ORM) 库。它提供了高效、灵活的数据库交互方式，支持多种数据库后端。主要特性包括：
- **ORM 支持**：将 Python 对象映射到数据库表，实现对象与数据库的无缝交互，避免直接编写 SQL。
- **SQL 表达式语言**：核心层允许构建类型安全的 SQL 表达式，支持动态查询构建和复杂查询优化。
- **数据库独立性**：兼容多种数据库，如 PostgreSQL、MySQL、SQLite、Oracle 等，通过统一的 API 处理差异。
- **连接池和事务管理**：内置连接池机制，提高性能；支持事务回滚和提交，确保数据一致性。
- **迁移工具**：集成 Alembic，支持数据库模式迁移和版本控制。
- **高性能**：使用 C 扩展优化，适用于大规模应用。
- **扩展性**：支持事件监听、自定义类型和第三方集成，如与 Flask、Django 等框架结合。

## 主要功能
- **核心 (Core)**：提供低级数据库操作，包括引擎创建、元数据定义和 SQL 执行。
- **ORM**：高层抽象，支持模型定义、会话管理、查询构建和关系映射（如一对多、多对多）。
- **Schema 定义**：使用 Python 类定义表结构、约束和索引。
- **查询接口**：通过 Query 对象或 select() 函数构建查询，支持过滤、排序、分组和聚合。
- **事务与隔离**：管理数据库会话，支持嵌套事务和自动提交。
- **类型系统**：内置多种数据类型映射，确保 Python 与数据库类型兼容。

## 用法示例
### 安装
```bash
pip install sqlalchemy
```

### 基本用法
1. **创建引擎和连接**：
   ```python
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///example.db')  # 使用 SQLite 示例
   ```

2. **定义模型 (ORM)**：
   ```python
   from sqlalchemy import Column, Integer, String, create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   Base = declarative_base()

   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String(50))
       email = Column(String(100))

   Base.metadata.create_all(engine)  # 创建表
   ```

3. **使用会话进行 CRUD 操作**：
   ```python
   Session = sessionmaker(bind=engine)
   session = Session()

   # 创建
   new_user = User(name='Alice', email='alice@example.com')
   session.add(new_user)
   session.commit()

   # 查询
   users = session.query(User).filter(User.name == 'Alice').all()
   for user in users:
       print(user.name)

   # 更新
   user = session.query(User).filter(User.id == 1).first()
   if user:
       user.email = 'new@example.com'
       session.commit()

   # 删除
   session.delete(user)
   session.commit()

   session.close()
   ```

4. **核心层查询 (非 ORM)**：
   ```python
   from sqlalchemy import text
   with engine.connect() as conn:
       result = conn.execute(text("SELECT * FROM users WHERE name = :name"), {"name": "Alice"})
       for row in result:
           print(row)
   ```

更多细节请参考官方文档：https://docs.sqlalchemy.org/