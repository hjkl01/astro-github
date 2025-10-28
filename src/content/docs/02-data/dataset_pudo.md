
---
title: dataset
---

# GitHub项目：dataset

**项目地址：** [https://github.com/pudo/dataset](https://github.com/pudo/dataset)

## 主要特性
dataset 是一个轻量级的 Python 库，用于简化数据存储和检索任务。它设计用于处理结构化数据，如 CSV、JSON 或 SQL 等格式，支持内存中和磁盘上的数据操作。主要特性包括：
- **简单的数据集管理**：将数据视为表格结构，支持行和列的快速访问和修改。
- **多种后端支持**：兼容 SQLite、CSV、JSON 等格式，便于数据导入和导出。
- **事务性操作**：提供 ACID 兼容的事务支持，确保数据一致性。
- **轻量级和无依赖**：核心功能依赖标准库，几乎无外部依赖，便于集成。
- **查询和过滤**：内置类似 SQL 的查询接口，支持过滤、排序和聚合操作。
- **跨平台兼容**：适用于 Python 2 和 3，支持 Windows、macOS 和 Linux。

## 主要功能
- **创建和管理数据集**：从各种来源（如文件或内存）初始化数据集，支持动态添加/删除行和列。
- **数据导入/导出**：轻松从 CSV、JSON 或 SQL 数据库导入数据，并导出到相同格式。
- **查询操作**：使用 Pythonic 接口进行数据查询，例如过滤行（`dataset.table.find_one(field=value)`）或迭代记录。
- **更新和删除**：支持批量更新记录或删除匹配项，确保操作原子性。
- **连接管理**：通过 URI（如 `sqlite:///memory://` 或 `csv:///path/to/file`）连接不同存储后端。
- **扩展性**：可与 Pandas 或 SQLAlchemy 等库结合使用，增强数据分析能力。

## 用法示例
安装库：`pip install dataset`

### 基本用法
```python
import dataset

# 连接内存数据库
db = dataset.connect('sqlite:///:memory:')

# 创建表
table = db['users']

# 插入数据
table.insert(dict(name='Alice', age=30))
table.insert(dict(name='Bob', age=25))

# 查询数据
results = table.find()  # 获取所有记录
for row in results:
    print(row['name'], row['age'])

# 过滤查询
user = table.find_one(name='Alice')
print(user['age'])  # 输出: 30

# 更新数据
table.update(dict(age=31), name='Alice')

# 删除数据
table.delete(name='Bob')
```

### 文件-based 用法
```python
# 使用 CSV 文件
db = dataset.connect('csv:////path/to/data.csv')
table = db['data']
# 后续操作同上
```

更多细节请参考项目文档和示例。