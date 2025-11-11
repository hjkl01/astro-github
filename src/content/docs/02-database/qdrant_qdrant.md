---
title: qdrant
---

# Qdrant

## 功能介绍

Qdrant 是一个高性能、大规模的向量数据库和向量搜索引擎，专为下一代 AI 应用设计。它提供了一个生产就绪的服务，具有便捷的 API 来存储、搜索和管理点（向量及其附加负载）。Qdrant 支持扩展过滤，使其适用于各种神经网络或语义匹配、面搜索和其他应用。

Qdrant 使用 Rust 编写，即使在高负载下也能保持快速和可靠。它可以将嵌入或神经网络编码器转化为完整的匹配、搜索、推荐等应用。

Qdrant 还提供完全托管的 [Qdrant Cloud](https://cloud.qdrant.io/)，包括免费层。

### 主要特性

- **过滤和负载**：可以附加任何 JSON 负载到向量，支持基于负载值的存储和过滤。支持关键字匹配、全文过滤、数值范围、地理位置等。
- **混合搜索与稀疏向量**：支持稀疏向量以克服密集向量在特定关键字搜索中的局限性。
- **向量量化与磁盘存储**：提供多种选项使向量搜索更便宜、更高效。内置向量量化可将 RAM 使用减少高达 97%。
- **分布式部署**：支持水平扩展，通过分片和复制增强大小和吞吐量。
- **其他特性**：查询规划和负载索引、SIMD 硬件加速、异步 I/O、预写日志等。

## 用法

### 快速开始

#### Python

安装客户端：

```bash
pip install qdrant-client
```

使用内存实例（用于测试）：

```python
from qdrant_client import QdrantClient
qdrant = QdrantClient(":memory:")
```

或持久化到磁盘：

```python
client = QdrantClient(path="path/to/db")
```

#### 客户端-服务器

运行 Docker 容器：

```bash
docker run -p 6333:6333 qdrant/qdrant
```

连接到实例：

```python
qdrant = QdrantClient("http://localhost:6333")
```

### 客户端库

官方客户端：

- [Go](https://github.com/qdrant/go-client)
- [Rust](https://github.com/qdrant/rust-client)
- [JavaScript/TypeScript](https://github.com/qdrant/qdrant-js)
- [Python](https://github.com/qdrant/qdrant-client)
- [.NET/C#](https://github.com/qdrant/qdrant-dotnet)
- [Java](https://github.com/qdrant/java-client)

社区客户端：

- Elixir, PHP, Ruby 等。

### API

- **REST**：在线 OpenAPI 3.0 文档 [here](https://api.qdrant.tech/)。
- **gRPC**：用于更快的生产级搜索，文档 [here](https://qdrant.tech/documentation/interfaces/#grpc-interface)。

### 演示项目

- 语义文本搜索
- 相似图像搜索（食物发现）
- 极致分类（电商产品分类）

### 集成

与 Cohere, DocArray, Haystack, LangChain, LlamaIndex, OpenAI, Microsoft Semantic Kernel 等集成。

更多信息请参考 [官方文档](https://qdrant.tech/documentation/)。
