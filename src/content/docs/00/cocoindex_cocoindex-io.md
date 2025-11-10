---
title: cocoindex
---

# CocoIndex

## 功能介绍

CocoIndex 是一个专为 AI 设计的高性能数据转换框架，核心引擎采用 Rust 编写，支持增量处理和数据血缘追踪。它超越了传统 SQL，能够轻松构建向量索引、知识图谱或进行自定义数据转换。

### 主要特性

- **高性能**：核心引擎用 Rust 编写，提供卓越的性能表现
- **增量处理**：支持增量索引，只重新计算必要的部分，最大化利用缓存
- **数据血缘**：内置数据血缘追踪，所有转换前后的数据都可观测
- **开发效率**：通过数据流编程模型，只需 ~100 行 Python 代码即可定义转换
- **即插即用**：提供标准化的源、目标和转换组件接口，一行代码即可切换组件
- **生产就绪**：从第一天起即可投入生产使用

### 支持的功能

- 向量索引构建（用于 RAG）
- 知识图谱构建
- 自定义数据转换
- 多种数据源支持（本地文件、S3、Azure Blob、Google Drive 等）
- 多种目标支持（PostgreSQL、Qdrant、LanceDB 等）
- 文本嵌入、图像嵌入、LLM 提取等转换

## 用法

### 安装

```bash
pip install -U cocoindex
```

需要安装 PostgreSQL 用于增量处理。

### 基本用法

1. 定义数据流：

```python
import cocoindex

@cocoindex.flow_def(name="TextEmbedding")
def text_embedding_flow(flow_builder: cocoindex.FlowBuilder, data_scope: cocoindex.DataScope):
    # 添加数据源
    data_scope["documents"] = flow_builder.add_source(cocoindex.sources.LocalFile(path="markdown_files"))

    # 添加收集器
    doc_embeddings = data_scope.add_collector()

    # 数据转换
    with data_scope["documents"].row() as doc:
        # 分割文档
        doc["chunks"] = doc["content"].transform(
            cocoindex.functions.SplitRecursively(),
            language="markdown", chunk_size=2000, chunk_overlap=500)

        # 处理每个块
        with doc["chunks"].row() as chunk:
            # 生成嵌入
            chunk["embedding"] = chunk["text"].transform(
                cocoindex.functions.SentenceTransformerEmbed(
                    model="sentence-transformers/all-MiniLM-L6-v2"))

            # 收集数据
            doc_embeddings.collect(filename=doc["filename"], location=chunk["location"],
                                   text=chunk["text"], embedding=chunk["embedding"])

    # 导出到向量索引
    doc_embeddings.export(
        "doc_embeddings",
        cocoindex.targets.Postgres(),
        primary_key_fields=["filename", "location"],
        vector_indexes=[
            cocoindex.VectorIndexDef(
                field_name="embedding",
                metric=cocoindex.VectorSimilarityMetric.COSINE_SIMILARITY)])
```

2. 运行索引：

```python
# 构建和运行流
flow = cocoindex.build_flow(text_embedding_flow)
flow.execute()
```

### 示例应用

- 文本文档嵌入索引（语义搜索）
- 代码嵌入索引
- PDF 文档处理和嵌入
- 多模态搜索（文本+图像）
- 知识图谱构建
- 产品推荐系统
- 人脸识别
- 论文元数据索引

更多示例请参考项目仓库的 examples 目录。

## 文档和资源

- [官方文档](https://cocoindex.io/docs)
- [快速开始指南](https://cocoindex.io/docs/getting_started/quickstart)
- [GitHub 仓库](https://github.com/cocoindex-io/cocoindex)
- [Discord 社区](https://discord.com/invite/zpA9S2DR7s)
