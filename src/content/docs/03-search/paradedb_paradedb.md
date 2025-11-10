---
title: paradedb
---

# ParadeDB

## 项目简介

ParadeDB 是一个现代的 Elasticsearch 替代品，基于 PostgreSQL 构建。它专为实时、高更新工作负载设计，提供强大的全文搜索和向量搜索功能。

## 主要功能

### 全文搜索

- 支持 BM25 索引算法
- 多种查询类型：匹配查询、短语查询、布尔查询、正则表达式查询
- 自定义分词器（包括 N-gram、ICU 等）
- 高亮显示搜索结果
- 相似文档搜索（More Like This）

### 向量搜索

- 支持密集向量（vector 数据类型，最大维度 2000）
- 支持稀疏向量（sparsevec 数据类型，最大非零元素 1000）
- 多种距离度量：L2 距离、余弦距离、内积

### 高级查询功能

- 范围查询
- 存在查询
- 常量分数查询
- 聚合推送（COUNT 等）

## 安装和使用

### 安装

从源码构建并安装 pg_search 扩展：

```bash
cargo pgrx install --release
```

启用 ICU 分词器（开发模式）：

```bash
cargo pgrx run --features icu
```

### 创建索引

创建 BM25 索引：

```sql
CREATE INDEX search_idx ON mock_items
USING bm25 (id, description, category)
WITH (
    key_field = 'id',
    text_fields = '{
        "description": {
            "tokenizer": {"type": "ngram", "min_gram": 2, "max_gram": 3, "prefix_only": false}
        },
        "category": {
            "tokenizer": {"type": "default"}
        }
    }'
);
```

### 基本查询

全文搜索：

```sql
SELECT description, rating, category
FROM mock_items
WHERE description @@@ 'running shoes';
```

使用函数语法：

```sql
SELECT description, rating, category
FROM mock_items
WHERE id @@@ paradedb.match('description', 'running shoes');
```

JSON 语法：

```sql
SELECT description, rating, category
FROM mock_items
WHERE id @@@
'{ "match": { "field": "description", "value": "running shoes" } }'::jsonb;
```

### 短语搜索

基本短语搜索：

```sql
SELECT description, rating, category
FROM mock_items
WHERE description @@@ '"plastic keyboard"';
```

带 slop 的短语搜索（允许词间距）：

```sql
SELECT description, rating, category
FROM mock_items
WHERE description @@@ '"ergonomic keyboard"~1';
```

### 向量搜索

创建向量列：

```sql
-- 密集向量
SELECT '[1,2,3]'::vector;

-- 稀疏向量
SELECT '{1:3,3:1,5:2}/5'::sparsevec;
```

向量相似性搜索：

```sql
-- L2 距离
SELECT * FROM items ORDER BY embedding <-> '{1:3,3:1,5:2}/5' LIMIT 5;

-- 余弦距离
SELECT * FROM items ORDER BY embedding <=> '{1:3,3:1,5:2}/5' LIMIT 5;

-- 内积
SELECT * FROM items ORDER BY embedding <#> '{1:3,3:1,5:2}/5' LIMIT 5;
```

### 高亮显示

生成高亮片段：

```sql
SELECT id, paradedb.snippet(description)
FROM mock_items
WHERE description @@@ 'shoes'
LIMIT 5;
```

自定义高亮标签：

```sql
SELECT id, paradedb.snippet(description, start_tag => '<i>', end_tag => '</i>')
FROM mock_items
WHERE description @@@ 'shoes'
LIMIT 5;
```

### 相似文档搜索

基于文档 ID：

```sql
SELECT description, rating, category
FROM mock_items
WHERE id @@@ paradedb.more_like_this(
  document_id => 3,
  min_term_frequency => 1
);
```

基于字段值：

```sql
SELECT description, rating, category
FROM mock_items
WHERE id @@@ paradedb.more_like_this(
  document_fields => '{"description": "shoes"}',
  min_doc_frequency => 0,
  max_doc_frequency => 100,
  min_term_frequency => 1
);
```

### 范围查询

```sql
SELECT description, rating, category
FROM mock_items
WHERE id @@@ paradedb.range(
    field => 'rating',
    range => int4range(1, 3, '[)')
);
```

### 布尔查询

隐式 OR：

```sql
SELECT description, rating, category
FROM mock_items
WHERE description @@@ 'keyboard headphones';
```

### 聚合查询

启用 COUNT 聚合推送：

```sql
SET paradedb.enable_aggregate_custom_scan TO ON;
```

COUNT 查询：

```sql
SELECT COUNT(*) FROM mock_items
WHERE description @@@ 'shoes';
```

## 部署选项

### Kubernetes 部署

安装 CloudNativePG Operator：

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --atomic --install cnpg \
--create-namespace \
--namespace cnpg-system \
--set monitoring.podMonitorEnabled=true \
--set monitoring.grafanaDashboard.create=true \
cnpg/cloudnative-pg
```

## 性能和优化

- 支持实时索引更新
- 优化的 BM25 算法实现
- 向量搜索支持多种距离度量
- 聚合查询推送以提高性能

## 许可证

开源项目，具体许可证请参考项目仓库。
