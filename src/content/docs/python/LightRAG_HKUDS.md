---
title: LightRAG
---

## 项目简介

LightRAG 是一个简单且快速的检索增强生成（Retrieval-Augmented Generation, RAG）系统，由香港大学数据科学与工程实验室（HKUDS）开发。该项目旨在提供一个高效的知识图谱驱动的RAG解决方案，能够从文档中提取实体和关系，并支持多种查询模式。

## 主要功能

### 核心特性

- **简单快速**：相比传统RAG，LightRAG对大语言模型（LLM）的能力要求更高，但实现更简洁高效
- **知识图谱驱动**：自动从文档中提取实体和关系，构建知识图谱
- **多种查询模式**：支持本地、全局、混合、朴素等多种检索模式
- **多模态支持**：通过RAG-Anything集成，支持处理PDF、图片、表格等多种格式文档
- **可视化界面**：提供Web UI用于文档索引、知识图谱探索和查询

### 存储支持

- **向量存储**：支持NanoVectorDB、PostgreSQL、Milvus、Faiss、Qdrant等多种向量数据库
- **图存储**：支持NetworkX、Neo4J、PostgreSQL AGE等多种图数据库
- **KV存储**：支持JSON、Redis、MongoDB等多种键值存储

### LLM集成

- **OpenAI兼容API**：支持GPT系列模型
- **Hugging Face**：支持本地Hugging Face模型
- **Ollama**：支持本地Ollama部署的模型

## 安装方法

### 从PyPI安装

```bash
# 安装核心版本
pip install lightrag-hku

# 安装包含API服务器的完整版本
pip install "lightrag-hku[api]"

# 安装包含可观测性的版本
pip install "lightrag-hku[observability]"
```

### 从源码安装

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
pip install -e ".[api,observability]"
```

## 基本用法

### 初始化RAG实例

```python
import asyncio
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.utils import EmbeddingFunc

async def initialize_rag():
    rag = LightRAG(
        working_dir="./rag_storage",
        embedding_func=EmbeddingFunc(
            embedding_dim=1536,
            func=openai_embed
        ),
        llm_model_func=gpt_4o_mini_complete,
    )

    # 重要：必须初始化存储和管道状态
    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag
```

### 插入文档

```python
# 插入单个文档
await rag.ainsert("这是要插入的文档内容")

# 批量插入
await rag.ainsert(["文档1", "文档2", "文档3"])
```

### 查询文档

```python
from lightrag import QueryParam

# 混合查询模式
result = await rag.aquery(
    "文档中的主要主题是什么？",
    param=QueryParam(mode="hybrid")
)
print(result)
```

## 高级用法

### 使用Neo4J存储

```bash
export NEO4J_URI="neo4j://localhost:7687"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="password"
```

```python
rag = LightRAG(
    working_dir=WORKING_DIR,
    graph_storage="Neo4JStorage",
    # ... 其他配置
)
```

### 多模态文档处理

```python
# 安装RAG-Anything
pip install raganything

from raganything import RAGAnything

rag_anything = RAGAnything(lightrag=rag_instance)
await rag_anything.process_document_complete("document.pdf")
```

### 实体和关系管理

```python
# 创建实体
entity = await rag.acreate_entity("Google", {
    "description": "一家全球性的科技公司",
    "entity_type": "company"
})

# 创建关系
relation = await rag.acreate_relation("Google", "Gmail", {
    "description": "Google开发了Gmail服务",
    "weight": 2.0
})
```

## 配置要求

### LLM要求

- 参数量至少320亿
- 上下文长度至少32K（推荐64K）
- 不推荐使用推理模型进行文档索引

### 嵌入模型

- 推荐使用高性能多语言嵌入模型，如BAAI/bge-m3或text-embedding-3-large

### 环境变量

```bash
# OpenAI配置
export OPENAI_API_KEY="your-api-key"

# Neo4J配置
export NEO4J_URI="neo4j://localhost:7687"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="password"
```

## 评估和性能

LightRAG在多个数据集上表现出色，特别是在农业、计算机科学、法律和混合领域的数据集上，相比传统RAG方法在全面性、多样性和赋权性方面有显著提升。

## 相关项目

- [RAG-Anything](https://github.com/HKUDS/RAG-Anything)：多模态RAG系统
- [VideoRAG](https://github.com/HKUDS/VideoRAG)：视频RAG系统
- [MiniRAG](https://github.com/HKUDS/MiniRAG)：极简RAG系统

## 引用

如果您在研究中使用LightRAG，请引用以下论文：

```bibtex
@article{guo2024lightrag,
title={LightRAG: Simple and Fast Retrieval-Augmented Generation},
author={Zirui Guo and Lianghao Xia and Yanhua Yu and Tu Ao and Chao Huang},
year={2024},
eprint={2410.05779},
archivePrefix={arXiv},
primaryClass={cs.IR}
}
```
