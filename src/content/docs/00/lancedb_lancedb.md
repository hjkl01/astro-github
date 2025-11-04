
---
title: lancedb
---


# Lancedb

> **GitHub 地址**: <https://github.com/lancedb/lancedb>

Lancedb 是一个轻量级、可嵌入的向量数据库，适用于需要高效存储、检索和管理向量数据的场景。它基于 Apache Arrow 进行内存映射，支持 SQL 语法和向量搜索，并且可以在多种编程语言（Python、Rust、Go 等）中使用。

## 主要特性

| 特性 | 说明 |
|------|------|
| **向量搜索** | 支持 k‑Nearest Neighbor (kNN) 搜索，支持多种距离度量（欧氏、余弦、曼哈顿等）。 |
| **SQL 接口** | 通过 `SELECT * FROM table WHERE vector @@ kNN(vector, 10)` 等语法执行向量查询。 |
| **内存映射** | 使用 Apache Arrow 的 IPC 文件格式，读取时仅映射文件的一部分，内存占用低。 |
| **高性能** | 利用 SIMD 指令集、并行化搜索，查询延迟通常在毫秒级。 |
| **可嵌入** | 轻量级二进制文件，无需额外服务或数据库服务器。 |
| **持久化** | 数据以 Arrow 文件形式持久化，支持增量写入、版本回滚。 |
| **多语言 SDK** | Python、Rust、Go 等官方 SDK，支持跨语言调用。 |
| **可扩展** | 通过插件机制支持自定义索引、距离函数等。 |
| **事务支持** | 通过乐观锁实现事务一致性，支持批量写入。 |

## 核心功能

1. **创建和管理表**  
   ```sql
   CREATE TABLE embeddings (
       id BIGINT PRIMARY KEY,
       vector FLOAT[512],
       metadata MAP<VARCHAR, VARCHAR>
   );
   ```

2. **插入向量**  
   ```sql
   INSERT INTO embeddings (id, vector, metadata) VALUES
   (1, [0.1, 0.2, ...], {'name': 'foo'}),
   (2, [0.3, 0.4, ...], {'name': 'bar'});
   ```

3. **向量搜索**  
   ```sql
   SELECT id, vector, metadata
   FROM embeddings
   WHERE vector @@ kNN([0.15, 0.25, ...], k=5);
   ```

4. **过滤 + 搜索**  
   ```sql
   SELECT id, vector
   FROM embeddings
   WHERE metadata['category'] = 'image'
     AND vector @@ kNN([0.15, 0.25, ...], k=10);
   ```

5. **增量索引**  
   ```sql
   ALTER TABLE embeddings
   ADD INDEX idx_vector ON vector;
   ```

6. **事务**  
   ```sql
   BEGIN TRANSACTION;
   INSERT INTO embeddings ...
   COMMIT;
   ```

## 快速开始（Python）

```bash
pip install lancedb
```

```python
import lancedb
import numpy as np

# 创建或打开数据库
db = lancedb.connect("mydb")

# 创建表
table = db.create_table(
    name="embeddings",
    schema={"id": "int64", "vector": "float32[128]"},
    primary_key="id"
)

# 插入数据
vectors = np.random.rand(10, 128).astype(np.float32)
table.add({"id": np.arange(10), "vector": vectors})

# 向量搜索
query_vector = np.random.rand(1, 128).astype(np.float32)
results = table.search(query_vector, k=3)
print(results)
```

## 进一步阅读

- 官方文档: <https://lancedb.github.io>
- 示例代码: <https://github.com/lancedb/lancedb/tree/main/examples>
- API 参考: <https://lancedb.github.io/api/python>

> **注意**：本项目仍在积极开发中，建议查看官方仓库的最新 README、CHANGELOG 与 Issue 跟踪获取最新信息。