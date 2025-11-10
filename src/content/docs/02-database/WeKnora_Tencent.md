---
title: WeKnora
---

# WeKnora

项目地址: https://github.com/Tencent/WeKnora

## 主要特性

- **知识图谱核心引擎**：支持 RDF/OWL 语义模型，提供高性能的图数据存储与查询。
- **多模态数据接入**：支持 CSV、JSON、RDF 等多种数据格式的快速导入与映射。
- **推理与规则引擎**：内置基于 OWL 2 DL 的推理机制，可扩展自定义规则（SWRL、SPARQL 规则）。
- **灵活查询**：提供 SPARQL、GraphQL 及 RESTful 接口，支持复杂路径查询与聚合。
- **安全与权限管理**：细粒度访问控制，支持 RBAC、OAuth2 等安全机制。
- **可视化管理后台**：Web UI 可视化图谱探索、节点关系浏览、数据质量监控。
- **高可用与水平扩展**：支持分布式部署，复制、分区与热备份，兼容 Kubernetes。
- **与微信生态集成**：提供微信小程序 SDK 与公众号插件，方便在微信内部使用知识图谱服务。

## 关键功能模块

| 模块 | 说明 |
|------|------|
| **Core Engine** | 图数据存储、索引、查询与推理 |
| **API Server** | REST / gRPC / GraphQL 接口，支持批量 CRUD 与查询 |
| **Ingestor** | 数据导入工具，支持多源异步加载 |
| **Reasoner** | 推理服务，支持即时推理与定时批量推理 |
| **Web Console** | 图谱可视化、权限管理、监控面板 |
| **SDK** | Python、JavaScript 等语言 SDK，简化业务集成 |

## 快速使用

### 1. 环境准备

```bash
# 需要 Docker 和 Docker Compose
docker pull tencent/weknora:latest
```

### 2. 启动服务

```bash
docker-compose up -d
```

服务默认监听：

- `http://localhost:8000` – API 接口
- `http://localhost:3000` – Web Console

### 3. 数据导入示例

```bash
# 通过 REST API 导入 CSV
curl -X POST http://localhost:8000/api/import \
     -H "Content-Type: multipart/form-data" \
     -F "file=@data.csv" \
     -F "mapping=csv_to_graph.yaml"
```

### 4. 查询示例

```bash
# SPARQL 查询
curl -X POST http://localhost:8000/api/sparql \
     -H "Content-Type: application/sparql-query" \
     -d "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
```

### 5. SDK 快速调用（Python）

```python
from weknora import WeKnoraClient

client = WeKnoraClient("http://localhost:8000")
result = client.sparql("SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 5")
print(result)
```

## 文档与支持

- 官方文档：<https://tencent.github.io/WeKnora/>
- 社区讨论：<https://github.com/Tencent/WeKnora/discussions>
- 代码仓库：<https://github.com/Tencent/WeKnora>