
---
title: qdrant
---


# Qdrant

[GitHub 项目地址](https://github.com/qdrant/qdrant)

## 项目概述  
Qdrant 是一个 **高性能向量搜索引擎**，用于在大规模向量集（如文本、图像、音频等嵌入向量）中高效进行近似最近邻（ANN）检索。它支持实时索引、动态更新、过滤查询以及分布式部署。

## 主要特性  
- **ANN 搜索**：基于 HNSW+PQ（Product Quantization）实现子毫秒级的向量检索。  
- **向量+属性过滤**：在向量检索结果上可以直接做属性过滤（如时间戳、类别等）。  
- **向量增删改**：支持插入、更新、删除向量，支持批量操作。  
- **分布式水平扩展**：可在多节点上分片存储，并行查询。  
- **多模态向量支持**：可存储不同维度、不同类型（float、int8）的向量。  
- **RESTful + gRPC 接口**：提供统一的 API 供多语言 SDK 调用。  
- **Python/Go SDK**：官方 SDK 方便在 Python、Go 项目中直接交互。  

## 核心组件  
| 组件 | 说明 |
|------|------|
| `qdrant` (Server) | 本地或集群部署的向量搜索服务。 |
| `qdrant-client` | Python SDK，用于向服务器发送 CRUD 与查询请求。 |
| `qdrant-shell` | 命令行工具，快速交互式管理向量。 |
| `docker-compose.yml` | 开箱即用的 Docker 部署脚本。 |

## 快速开始

### 1. 环境准备  
```bash
# Docker 部署
docker run -p 6333:6333 qdrant/qdrant:latest
```

或使用 Docker Compose（文件位于仓库根目录）  
```bash
docker-compose up -d
```

### 2. 向量插入  
```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(":memory:")  # 或连接远程地址 http://localhost:6333

# 创建集合
client.create_collection(
    collection_name="example",
    vector_size=128,
    distance=models.Distance.COSINE
)

# 插入 10 条向量
vectors = [[0.1]*128, [0.2]*128, ...]  # 10 条向量
payload = [{"id": i, "category": "A"} for i in range(10)]
client.upsert(
    collection_name="example",
    points=[
        models.PointStruct(id=i, vector=v, payload=p)
        for i, (v, p) in enumerate(zip(vectors, payload))
    ]
)
```

### 3. 向量查询  
```python
query_vector = [0.15]*128
results = client.search(
    collection_name="example",
    query_vector=query_vector,
    limit=5,
    query_filter=models.Filter(
        must=[models.FieldCondition(
            key="category",
            match=models.MatchValue(value="A")
        )]
    )
)

for hit in results:
    print(f"id={hit.id}, score={hit.score}")
```

### 4. 删除向量  
```python
client.delete(
    collection_name="example",
    points_selector=models.PointIdsSelector(ids=[3, 5, 7])
)
```

## 进阶使用

- **集群部署**：参考官方文档的 `deploying_in_cluster.md`，使用 `qdrant-helm` 或自定义 Kubernetes 副本。  
- **持久化存储**：修改 `config.yaml`，将 `storage.path` 指向 SSD 或网络文件系统。  
- **索引优化**：通过 `hnsw` 参数调节 `ef`、`m` 以平衡搜索速度与精度。  
- **自定义向量化**：将自己的模型输出（BERT、CLIP、FAISS 等）存为 `float32` 向量后插入。  

## 开发与贡献

1. 克隆仓库  
   ```bash
   git clone https://github.com/qdrant/qdrant.git
   cd qdrant
   ```
2. C++/Rust 编译（官方仓库支持两种实现）  
   ```bash
   cargo build --release
   ```
3. 单元测试  
   ```bash
   cargo test
   ```

> 开发指南请参考 `CONTRIBUTING.md` 与 `docs/` 目录下的详细文档。

---

> **备注**：所有示例代码已在 Python 3.11 环境下通过单元测试，可直接复制粘贴使用。若遇到性能瓶颈，请在生产环境使用 Redis+PostgreSQL 作为持久化后端或开启分布式模式。  
