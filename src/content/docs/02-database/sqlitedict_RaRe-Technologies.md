---
title: sqlitedict
---

# sqlitedict 项目

**项目地址:** https://github.com/RaRe-Technologies/sqlitedict

## 主要特性
sqlitedict 是一个轻量级的 Python 库，它将 SQLite 数据库包装成一个类似于 Python 内置 `dict` 的接口。主要特性包括：
- **持久化字典**：使用 SQLite 作为后端存储，提供键值对的持久化操作，支持自动创建和维护数据库文件。
- **线程安全**：内置支持多线程访问，确保数据一致性。
- **自动事务管理**：所有读写操作自动处理事务，无需手动管理。
- **简单易用**：接口与 Python `dict` 高度兼容，支持常见的字典方法如 `get()`、`setdefault()`、`keys()` 等。
- **高效存储**：适合存储中等规模的数据集，避免了纯内存字典的内存消耗和文件操作的复杂性。
- **跨平台**：依赖标准 SQLite，无需额外安装数据库服务器。

## 主要功能
- **键值存储**：支持字符串、整数、浮点数、列表、字典等 Python 基本数据类型的存储和检索。
- **批量操作**：提供 `update()` 方法批量更新多个键值对。
- **迭代支持**：可以迭代所有键、值或键值对。
- **备份与恢复**：支持数据库文件的备份和从备份恢复。
- **自定义表名**：允许指定 SQLite 表名，便于多字典共存于同一数据库文件。
- **内存模式**：可选的内存模式（:memory:），用于临时数据存储。

## 用法示例
安装库：`pip install sqlitedict`

### 基本用法
```python
from sqlitedict import SqliteDict

# 创建或打开数据库文件
with SqliteDict('mydatabase.sqlite') as sqdict:
    # 添加键值对
    sqdict['key1'] = 'value1'
    sqdict['key2'] = 42
    
    # 读取值
    print(sqdict['key1'])  # 输出: value1
    
    # 检查键是否存在
    if 'key2' in sqdict:
        print(sqdict.get('key2'))  # 输出: 42
    
    # 迭代键
    for key in sqdict.keys():
        print(key)

# 数据库自动保存并关闭
```

### 持久化使用（非上下文管理器）
```python
sqdict = SqliteDict('mydatabase.sqlite', autocommit=True)
sqdict['newkey'] = 'newvalue'
sqdict.commit()  # 手动提交事务
sqdict.close()   # 关闭数据库
```

### 自定义表名
```python
with SqliteDict('mydatabase.sqlite', tablename='my_table') as sqdict:
    sqdict['key'] = 'value'
```

更多细节请参考项目 README。