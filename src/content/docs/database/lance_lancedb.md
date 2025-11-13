---
title: lance
---

# Lance（LanceDB）

**GitHub地址**：<https://github.com/lancedb/lance>

## 项目简介
Lance 是一个高性能、可扩展的向量数据库，基于 Rust 实现，提供 Python API 与 SQL 支持。其核心采用 Lance 格式（基于 Apache Arrow）实现高效存储和压缩，并通过多种 ANN（近似最近邻）索引实现快速相似度搜索。适用于大规模向量检索、检索式生成、向量化数据库等场景。

## 主要特性
- **高性能存储**：Lance 格式使用磁盘映射、列式压缩，IO 与 CPU 利用率高，读取速度可达数 GB/s。
- **多种索引**：支持 IVF、HNSW、PQ 等 ANN 索引；可根据业务需求自定义索引策略。
- **SQL 与 Python API**：直接使用 SQL 语句 (`SELECT`, `INSERT`, `DELETE`, `UPDATE`) 与 Python 对象交互，兼容 DuckDB 等查询引擎。
- **向量与元数据混合查询**：支持向量相似度 + 过滤条件组合查询。
- **可插拔存储后端**：本地文件、S3、Azure Blob、GCS 等多种存储后端。
- **多模态支持**：可存储多维向量、文本、图片等多种数据类型。
- **与 ML 框架集成**：提供 PyTorch、TensorFlow、JAX 等框架的向量转换与批量写入工具。

## 快速上手

### 1. 安装
```bash
pip install lance
```

### 2. Python 示例

```python
import lance
import numpy as np

# 创建表
schema = lance.schema(
    [
        lance.field("id", "int64"),
        lance.field("embedding", "float32", dimensions=128),
        lance.field("meta", "string"),
    ]
)

# 生成示例向量
vectors = np.random.rand(10, 128).astype(np.float32)
ids = np.arange(10)
meta = ["sample"] * 10

# 写入
table = lance.Table.create("s3://bucket/lance_table", schema, overwrite=True)
table.write_batch(
    {
        "id": ids,
        "embedding": vectors,
        "meta": meta,
    }
)

# 查询：最近 5 个相似向量
query_vec = np.random.rand(1, 128).astype(np.float32)
result = table.search(query_vec, limit=5)
print(result)  # DataFrame 包含 id, embedding, meta
```

### 3. SQL 示例

```sql
-- 创建表（LanceDB 兼容 DuckDB）
CREATE TABLE vectors (
    id BIGINT,
    embedding VECTOR(128),
    meta STRING
);

-- 插入
INSERT INTO vectors VALUES (1, repeat(0.1::FLOAT, 128), 'sample');

-- 向量相似度查询
SELECT *
FROM vectors
ORDER BY vector_distance(embedding, [0.2, 0.2, ..., 0.2])  -- 128 维向量
LIMIT 10;
```

## 常见用法

| 用例 | 说明 |
|------|------|
| **批量写入** | `table.write_batch(...)` 支持 NumPy、Pandas、PyArrow Table 等多种输入 |
| **向量搜索** | `table.search(query_vec, limit=N)` 或 `SELECT ... ORDER BY vector_distance(...)` |
| **过滤查询** | `table.filter("meta = 'sample'")` 与向量搜索结合 |
| **索引管理** | `table.create_index(name='ivf', params={...})` 或 `table.drop_index(name)` |
| **表合并** | `table.merge(other_table)` |
| **元数据更新** | `table.update({"meta": "new_value"}, filter_condition)` |

## 集成与生态

- **LangChain**：可作为向量存储后端直接调用 `LanceVectorStore`.
- **FastAPI**：提供 RESTful 接口简易部署。
- **Apache Spark**：通过 PyArrow 与 Spark DataFrame 交互。
- **CLI 工具**：`lance` 命令行支持数据导入、索引构建、查询等操作。

## 参考文档
- 官方文档: <https://lancedb.github.io>
- 学术论文: 《Lance: A Columnar Format for Efficient Vector Search》  
- 示例代码: <https://github.com/lancedb/lance/tree/main/examples>

---