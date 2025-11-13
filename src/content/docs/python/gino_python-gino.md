---
title: gino
---

# GINO 项目

## 项目地址
[GitHub 项目地址](https://github.com/python-gino/gino)

## 主要特性
GINO 是一个轻量级的 Python 异步 ORM（对象关系映射）框架，专为异步编程设计。它基于 SQLAlchemy 的核心概念，但完全异步化，支持 asyncio 和 async/await 语法。主要特性包括：
- **异步支持**：无缝集成 Python 的 asyncio 生态，提供异步数据库操作，避免阻塞 I/O。
- **SQLAlchemy 兼容**：继承 SQLAlchemy 的模型定义、查询构建和关系处理，但使用异步执行器。
- **轻量级设计**：核心库小巧，易于扩展，不引入过多抽象层。
- **多数据库支持**：兼容 PostgreSQL、MySQL、SQLite 等常见数据库，通过 asyncpg、aiomysql 等异步驱动实现。
- **类型提示**：内置对 Python 类型提示的支持，便于 IDE 开发和代码检查。
- **事务管理**：提供异步事务上下文，支持嵌套事务和回滚。

## 主要功能
GINO 的核心功能围绕异步数据库交互展开：
- **模型定义**：使用装饰器或类继承方式定义数据库模型，支持主键、外键、索引和自定义类型。
- **CRUD 操作**：异步的创建（create）、读取（select/all/first）、更新（update）和删除（delete）操作，支持批量处理。
- **查询构建**：链式查询 API，如 `select().where()`，支持 JOIN、子查询和聚合函数。
- **关系映射**：处理一对多、多对多关系，通过异步加载器实现懒加载或预加载。
- **迁移工具**：集成 Alembic 支持数据库迁移，但需手动配置异步执行。
- **连接池管理**：内置异步连接池，自动管理连接生命周期，支持配置最大连接数和超时。

## 用法示例
### 安装
```bash
pip install gino
```

### 基本用法
1. **定义模型**：
```python
from gino import Gino

db = Gino()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
```

2. **创建数据库和表**（异步上下文）：
```python
import asyncio

async def main():
    async with db.create_engine('postgresql://user:pass@localhost/dbname') as conn:
        await db.gino.create_all(conn)  # 创建表

asyncio.run(main())
```

3. **CRUD 操作**：
```python
async def example():
    async with db:
        # 创建
        user = await User.create(name='Alice')
        
        # 查询
        users = await User.query.gino.all()
        user = await User.get(1)
        
        # 更新
        await user.update(name='Bob').apply()
        
        # 删除
        await user.delete()
```

更多细节请参考官方文档：https://python-gino.org/