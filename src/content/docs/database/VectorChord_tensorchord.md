---
title: VectorChord
---

# VectorChord

VectorChord 是一个 PostgreSQL 扩展，用于可扩展、高性能和磁盘高效的向量相似性搜索。它是 pgvecto.rs 的继任者，提供更好的稳定性和性能。

## 功能

- **增强性能**：查询速度比 pgvector 的 HNSW 实现快 5 倍，插入吞吐量高 16 倍，索引构建快 16 倍。
- **经济实惠的向量搜索**：使用仅 32GB 内存查询 1 亿个 768 维向量，实现 35ms P50 延迟，top10 recall@95%。
- **无缝集成**：与 pgvector 数据类型和语法完全兼容，提供开箱即用的最佳默认值，无需手动参数调整。
- **加速索引构建**：使用 IVF 进行外部索引构建（例如在 GPU 上），结合 RaBitQ 压缩以高效存储向量，同时通过自主重排序维护搜索质量。
- **长向量支持**：支持高达 60,000 维的向量，便于使用 text-embedding-3-large 等高维模型。
- **按需扩展**：基于水平扩展，5M/100M 768 维向量的查询可以轻松扩展到 10,000+ QPS，top10 recall@90%。
- **生产验证**：在生产环境中处理 30 亿+ 向量。

## 用法

### 使用 Docker 快速开始

运行 Docker 容器：

```bash
docker run \
  --name vectorchord-demo \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d ghcr.io/tensorchord/vchord-postgres:pg18-v0.5.3
```

连接到数据库：

```bash
psql -h localhost -p 5432 -U postgres
```

### 基本操作

1. 创建扩展：

```sql
CREATE EXTENSION IF NOT EXISTS vchord CASCADE;
```

2. 创建带有向量列的表：

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

3. 插入示例数据：

```sql
INSERT INTO items (embedding) SELECT ARRAY[random(), random(), random()]::real[] FROM generate_series(1, 1000);
```

4. 创建索引：

```sql
CREATE INDEX ON items USING vchordrq (embedding vector_l2_ops);
```

5. 执行向量搜索：

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

有关更多高级用法，请参阅[官方文档](https://docs.vectorchord.ai/vectorchord/)。
