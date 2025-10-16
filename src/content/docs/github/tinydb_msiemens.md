
---
title: tinydb
---

# TinyDB 项目

**GitHub 项目地址:** [https://github.com/msiemens/tinydb](https://github.com/msiemens/tinydb)

## 主要特性
TinyDB 是一个轻量级的、文档导向的数据库，完全用纯 Python 实现，无需外部依赖或服务器。它将数据存储在本地 JSON 文件中，适合小型应用、原型开发或嵌入式场景。主要特性包括：
- **纯 Python 实现**：无需安装额外数据库软件，只需 Python 环境即可运行。
- **文档存储**：数据以 JSON 文档形式存储，支持嵌套结构和灵活的查询。
- **简单易用**：API 设计简洁，类似于 MongoDB，但更轻量。
- **原子操作**：支持事务，确保数据一致性。
- **查询语言**：内置查询语法，支持条件过滤、排序和聚合。
- **持久化**：数据自动保存到磁盘文件，支持备份和恢复。
- **无外部依赖**：不依赖 SQL 或其他数据库引擎，体积小巧（仅几 KB）。

## 主要功能
- **数据插入与更新**：支持插入单个文档、批量插入，以及更新特定文档。
- **数据查询**：使用 where() 方法进行条件查询，支持相等、范围、包含等操作符；可结合 all()、get()、search() 等方法检索数据。
- **数据删除**：根据条件移除文档，支持批量删除。
- **索引支持**：可选创建索引以加速查询（基于文档字段）。
- **事务管理**：使用 read/write 事务确保操作的原子性和隔离性。
- **扩展性**：可自定义存储后端（如内存存储），并支持插件式查询操作。
- **备份与恢复**：内置方法导出/导入数据到 JSON 文件。

## 用法示例
安装 TinyDB：`pip install tinydb`

### 基本用法
```python
from tinydb import TinyDB, Query

# 初始化数据库（默认存储在 db.json 文件中）
db = TinyDB('db.json')

# 插入数据
db.insert({'name': 'Alice', 'age': 30})
db.insert_multiple([{'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}])

# 查询数据
User = Query()
results = db.search(User.age > 28)  # 查询年龄大于 28 的用户
print(results)  # [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# 更新数据
db.update({'age': User.age + 1}, User.name == 'Alice')

# 删除数据
db.remove(User.age < 30)

# 关闭数据库（可选，自动保存）
db.close()
```

更多高级用法详见官方文档，包括自定义查询、事务嵌套和存储配置。该项目适用于需要简单持久化存储的 Python 项目，如 CLI 工具或小型 Web 应用。