---
title: milvus
---


# Milvus

**Project 地址**: https://github.com/milvus-io/milvus

## 概述

Milvus 是基于向量搜索的开源数据库，致力于为大规模高维向量数据提供高速、低延迟以及高可扩展性的检索服务。它在 AI、推荐系统、自然语言处理等场景中广泛应用。

## 主要特性

| 特性 | 说明 |
|------|------|
| **高性能向量检索** | 支持百万级向量的实时检索，查询延迟通常在毫秒级别。 |
| **多种索引结构** | - IVF+PQ（倒排文件+乘积量化）<br>- HNSW（层次化近似最近邻）<br>- ANNOY、NSG、Flat 等索引算法可选。 |
| **分布式架构** | 支持水平扩展、负载均衡与容错，适用于云原生部署。 |
| **多种数据类型** | 支持浮点向量、整数向量以及混合向量。 |
| **丰富的检索模式** | - 单个向量检索<br>- 向量集合检索<br>- 带过滤器（Metadata）的矢量检索 |
| **多语言 SDK** | 提供 Python、Java、Go、Rust、C++、Node.js 等 SDK。 |
| **可视化客户端** | 提供 Milvus Console，支持向量上传、索引管理与查询可视化。 |
| **兼容性** | 与 SQL 与 NoSQL 系统集成，支持 DataNode、QueryNode、IndexNode 等组件，兼容 OpenAI 的 API 规范。 |

## 功能模块

| 模块 | 作用 |
|------|------|
| **DataNode** | 负责存储向量数据与元数据。 |
| **QueryNode** | 接收查询请求并执行向量检索。 |
| **IndexNode** | 负责索引构建与维护。 |
| **Proxy** | 提供统一的请求入口，做路由、负载均衡与监控。 |

## 快速上手

1. **安装**

   ```bash
   # Docker 快速启动
   docker run -d --name milvus \
     -p 19530:19530 -p 19121:19121 \
     milvusdb/milvus:v2.5 x.x.x
   ```

2. **Python SDK 示例**

   ```python
   from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType

   # 连接 Milvus
   connections.connect(host="localhost", port="19530")

   # 定义字段
   fields = [
       FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
       FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=128),
   ]

   # 创建集合
   schema = CollectionSchema(fields=fields, description="示例向量集合")
   collection = Collection(name="example_collection", schema=schema)

   # 插入向量
   import numpy as np
   vectors = np.random.rand(10, 128).astype(np.float32)
   collection.insert([vectors])

   # 建立索引
   index_params = {"index_type": "IVF_FLAT", "metric_type": "L2", "params": {"nlist": 128}}
   collection.create_index(field_name="embeddings", index_params=index_params)

   # 检索
   query_vectors = np.random.rand(2, 128).astype(np.float32)
   search_params = {"metric_type": "L2", "params": {"ef": 256}}
   result = collection.search(query_vectors, "embeddings", param=search_params, limit=5)
   print(result)
   ```

3. **使用 SDK 进行多表检索、过滤等高级场景**  
   参考官方文档：[Milvus Docs](https://milvus.io/docs/overview.md)

## 常见使用场景

- **推荐系统**：用用户画像或商品特征向量做相似度检索，实时生成相关推荐。  
- **语义检索**：通过文本编码器生成文本向量，支持海量文本的检索。  
- **图像检索**利用 CNN 生成图像特征向量，可完成图片相似度搜索。  
- **异常检测**：对时间序列或业务日志进行向量化，检索异常模式。  

> **Tip**：开启 `Collection.load()` 可以将整个集合预加载到内存，提高查询速度。

## 开发与扩展

- **插件机制**：可自定义索引、距离度量或元数据过滤器。  
- **自定义索引**：实现 `IIndex` 接口插入自研算法。  
- **Kubernetes 部署**：支持 Helm chart，轻松实现多节点部署。  

如需详细配置与高级特性，可查看官方 GitHub 仓库 Readme 与 Wiki。