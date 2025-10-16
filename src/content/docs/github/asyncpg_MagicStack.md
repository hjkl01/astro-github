
---
title: asyncpg
---

# asyncpg 项目

**GitHub 项目地址:** [https://github.com/MagicStack/asyncpg](https://github.com/MagicStack/asyncpg)

## 主要特性
asyncpg 是一个高效的、纯 Python 实现的 PostgreSQL 数据库适配器，专为异步编程设计。它基于 asyncio，支持高性能的数据库操作，具有以下核心特性：
- **高性能**：使用纯 C 实现协议解析和编码，支持二进制格式传输，性能接近于原生 libpq 库。
- **异步支持**：完全兼容 Python 的 asyncio 框架，支持协程（async/await）语法，实现非阻塞的数据库交互。
- **类型安全**：内置对 PostgreSQL 数据类型的原生支持，包括复合类型、数组和自定义类型，提供类型提示和验证。
- **连接池管理**：内置高效的连接池，支持自动重连和负载均衡。
- **无外部依赖**：不依赖于 PostgreSQL 的 C 库（如 libpq），纯 Python 实现，便于部署和分发。
- **事务支持**：完整支持事务、保存点和错误恢复机制。
- **安全性**：支持 SSL 加密、认证机制（如 SCRAM-SHA-256）和参数化查询，防范 SQL 注入。

## 主要功能
- **连接与查询**：建立异步连接，执行 SELECT、INSERT、UPDATE、DELETE 等 SQL 查询，支持批量操作和游标。
- **数据类型处理**：自动处理 PostgreSQL 的丰富数据类型，如 JSONB、UUID、几何类型等，并与 Python 类型无缝映射。
- **准备语句**：支持预编译语句，提高重复查询效率。
- **监听/通知**：实现 PostgreSQL 的 LISTEN/NOTIFY 机制，用于实时事件处理。
- **扩展支持**：兼容 PostgreSQL 扩展，如 hstore、postgis 等。
- **错误处理**：提供详细的异常类，如 PostgresConnectionError、QueryError 等，便于调试。

## 用法示例
安装：`pip install asyncpg`

### 基本连接和查询
```python
import asyncio
import asyncpg

async def main():
    # 建立连接
    conn = await asyncpg.connect(user='user', password='password',
                                 database='database', host='127.0.0.1')
    
    # 执行查询
    rows = await conn.fetch('SELECT * FROM table WHERE id = $1', 42)
    for row in rows:
        print(row['column'])
    
    # 插入数据（使用参数化查询）
    await conn.execute('INSERT INTO table (column) VALUES ($1)', 'value')
    
    # 关闭连接
    await conn.close()

asyncio.run(main())
```

### 使用连接池
```python
async def main():
    pool = await asyncpg.create_pool(user='user', password='password',
                                     database='database', host='127.0.0.1',
                                     min_size=1, max_size=10)
    
    async with pool.acquire() as conn:
        result = await conn.fetchval('SELECT count(*) FROM table')
        print(result)
    
    await pool.close()

asyncio.run(main())
```

更多用法请参考官方文档和 GitHub 仓库中的示例。