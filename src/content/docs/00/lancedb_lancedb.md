---
title: Lancedb
---

# LanceDB

## 功能

LanceDB 是一个开发者友好的嵌入式检索引擎，专为多模态 AI 设计。它提供了高效的向量搜索、混合搜索和数据管理功能，支持搜索更多、管理更少。LanceDB 支持多种索引类型，如 HNSW、IVF 等，以优化搜索性能。它还集成了多种嵌入函数和重排序器，用于增强检索质量。适用于构建推荐系统、图像搜索、语义搜索等应用。

## 用法

### 基本用法

首先，安装 LanceDB：

```bash
pip install lancedb
```

连接到数据库并创建表：

```python
import lancedb

# 连接到数据库
db = lancedb.connect("data/sample-lancedb")

# 创建表并添加数据
table = db.create_table("my_table", [
    {"id": 1, "vector": [0.1, 1.0], "item": "foo", "price": 10.0},
    {"id": 2, "vector": [3.9, 0.5], "item": "bar", "price": 20.0}
])

# 进行向量搜索
results = table.search([0.1, 0.3]).limit(20).to_list()
print(results)
```

### 高级用法

- **混合搜索**：结合 BM25 和语义搜索。

```python
from lancedb.rerankers import BM25Reranker

bm25_reranker = BM25Reranker()
results = table.search(query).rerank(bm25_reranker).limit(10).to_list()
```

- **创建索引**：使用 HNSW-SQ 索引。

```python
from lancedb.index import HnswSq

table.create_index("vector_col", index_type=HnswSq, M=16, ef_construction=64)
```

更多示例和文档请参考 [LanceDB GitHub](https://github.com/lancedb/lancedb)。
