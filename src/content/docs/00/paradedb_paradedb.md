
---
title: paradedb
---

**Parade DB**（GitHub 地址：<https://github.com/paradedb/paradedb>）

## 主要特性
- **基于 PostgreSQL**：在传统关系数据库中直接嵌入向量搜索功能，兼容现有 SQL 语句与工具。
- **高效向量索引**：支持 HNSW、IVF+PQ、Flat 等多种索引算法，满足不同精度与性能需求。
- **近似最近邻（ANN）查询**：通过 `vector_search`、`vector_match` 等函数实现向量相似度搜索。
- **向量运算**：提供内置向量算子（如 `||` 合并、点积 `*`、余弦相似度 cos × 1）与配套的 `vector` 数据类型。
- **与大模型无缝集成**：可与 OpenAI、Anthropic 等 LLM 对接，直接在 PostgreSQL 中使用 embeddings。
- **事务一致性**：向量数据与传统表遵循 PostgreSQL 的 ACID 特性。
- **SQL 兼容**：创建 & 更新向量索引、查询与常规表操作使用相同语法。

## 核心功能
| 功能 | 简述 |
|------|-------|
| **索引创建** | `SELECT paradedb_create_index(table_name, column_name, 'hnsw')` |
| **向量插入** | `INSERT INTO table(df-field) VALUES(vector[...])` |
| **相似度搜索** | `SELECT * FROM table WHERE vector_match(vector_col, $1, 10)` |
| **聚合/过滤** | `WHERE` 子句中可使用向量距离（`distance(vector, $1) < value`）|
| **量化** | `paradedb_index_options('ivf', k=200, nprobe=10)` |

## 简易使用步骤
1. **安装**  
   ```bash
   pip install paradedb
   ```  
   或使用 PostgreSQL Docker 镜像：
   ```bash
   docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=yourpwd paradedb/paradedb:latest
   ```

2. **连接数据库**  
   ```sql
   \c postgres
   ```

3. **创建表与索引**  
   ```sql
   CREATE TABLE items (
     id serial PRIMARY KEY,
     content text,
     embedding vector(384) -- 以 vector 数据类型存储
   );
   SELECT paradedb_create_index('items', 'embedding', 'hnsw');
   ```

4. **插入向量数据**  
   ```sql
   INSERT INTO items(content, embedding)
   VALUES ('sample text', vector[0.12, 0.45, ...]);
   ```

5. **执行相似度查询**  
   ```sql
   SELECT id, content
   FROM items
   WHERE vector_match(embedding, vector[0.10, 0.40, ...], 5);
   ```

6. **使用向量距离**（可与常规过滤结合）  
   ```sql
   SELECT *
   FROM items
   WHERE distance(embedding, vector[0.10, 0.40, ...]) < 0.2;
   ```

7. **维护索引**（重建、删除）  
   ```sql
   SELECT paradedb_rebuild_index('items', 'embedding');
   SELECT paradedb_drop_index('items', 'embedding');
   ```

> **说明**：上述示例默认向量维度为 384，可根据实际需求修改 `vector(n)` 的维度大小。所有向量操作均基于 PostgreSQL 扩展实现，性能与 PostgreSQL 原生语法保持一致。  

---  

**GitHub 地址**: <https://github.com/paradedb/paradedb>