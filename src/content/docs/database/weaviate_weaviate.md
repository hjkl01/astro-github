---
title: weaviate
---


# Weaviate

**GitHub 项目地址**: https://github.com/weaviate/weaviate

## 简介  
Weaviate 是一个基于向量搜索的、分布式的、开源的文档数据库，旨在让开发者能够轻松构建 AI 驱动的应用。它利用向量表示、图数据库以及可扩展的微服务架构，为语义搜索、知识图谱和多模态应用提供统一的解决方案。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **向量化查询** | 支持 `向量搜索` 与 `文本搜索` 混合查询，能够基于语义相似度返回结果。 |
| **多模态支持** | 兼容、文本、音频、文件等多种数据源；可使用模型将非文本数据转换为向量。 |
| **Schema 定义** | 通过 GraphQL 继承的 Schema 形式定义数据结构、属性类型、向量大小及索引方式。 |
| **可插拔向量索引** | 默认支持 HNSW、FAISS、Milvus 等索引引擎，可根据需求自由切换。 |
| **可扩展插件体系** | 通过 `Weaviate GraphQL API` 与 `REST API` 以及 `Client SDKs`（Go、Java、Python 等）实现对接和自定义插件。 |
| **自带知识图谱** | 通过 `Concepts`、`Classes` 和 `Relationships` 自动构建知识图谱，支持多跳查询。 |
| **聚合与可视化** | 内置仪表盘（Grafana）可实时监控向量查询性能与索引状态。 |
| **安全与权限** | 支持 JWT/OIDC、角色权限系统以及 TLS 加密。 |
| **云原生部署** | 官方 Helm Chart、Docker Compose、Kubernetes Operator 等，支持多云迁移与弹性伸缩。 |
| **离线与GPU支持** | 可根据硬件条件选择 CPU/GPU 版本，支持离线推理。 |

## 典型用例  

| 场景 | 用法示例 |
|------|----------|
| **智能问答** | 将模型产生的“问题向量”与知识库向量进行匹配，返回最相似答案。 |
| **推荐系统** | 通过用户兴趣向量搜索相似产品、文章或内容。 |
| **图像相似搜索** | 将图像经 CLIP 向量化后存入 Weaviate，支持相似图像查询。 |
| **多模态检索** | 结合文本、图像、音频向量，支持跨模态检索与组合查询。 |
| **业务分析** | 通过向量聚类、相似度分析，对客户群体或产品进行细分。 |

## 快速上手  

```bash
# 1. Clone 并进入项目
git clone https://github.com/weaviate/weaviate.git
cd weaviate

# 2. 通过 Docker Compose 启动本地实例
docker compose up -d

# 3. 创建 Schema（示例）
curl -X POST http://localhost:8080/v1/schema \
  -H "Content-Type: application/json" \
  -d '{
        "class" : "Article",
        "properties" : [
          {
            "name" : "title",
            "dataType" : [ "string" ]
          },
          {
            "name" : "content",
            "dataType" : [ "text" ]
          },
          {
            "name" : "embedding",
            "dataType" : [ "text[]"],   # 向量数据
            "vectorIndexType": "hnsw",
            "moduleConfig" : {}
          }
        ]
      }'

# 4. 存储对象
curl -X POST http://localhost:8080/v1/objects/Article \
  -H "Content-Type: application/json" \
  -d '{
        "id": "article-001",
        "vector": [0.12, 0.25, ...], # 512 维向量
        "properties": {"title":"Hello","content":"Welcome to Weaviate"}
      }'

# 5. 向量查询（例）
curl -X POST http://localhost:8080/v1/objects/Article/query \
  -H "Content-Type: application/json" \
  -d '{
        "nearVector": {"vector":[0.1,0.2,...],"certainty":0.8},
        "limit": 5
      }'
```

> 详细文档请参阅官方仓库 README 与 API 文档。

---
**作者**: Weaviate 团队  
**许可**: Apache-2.0  
```
