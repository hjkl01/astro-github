---
title: Chroma
---

# Chroma

Chroma 是一个开源的嵌入数据库，是构建 Python 或 JavaScript LLM 应用的最快方式。它提供了向量搜索和全文搜索功能，支持内存模式和持久化存储。

## 功能特性

- **简单易用**：完全类型化、测试完整、文档齐全。
- **集成支持**：与 LangChain、LlamaIndex 等工具集成。
- **多环境支持**：从开发、测试到生产环境，使用相同的 API。
- **功能丰富**：支持查询、过滤、正则表达式等。
- **免费开源**：Apache 2.0 许可证。

## 用法

### 安装

```bash
pip install chromadb  # Python 客户端
# JavaScript: npm install chromadb
# 客户端-服务器模式: chroma run --path /chroma_db_path
```

### 基本 API 使用

Chroma 的核心 API 只有 4 个函数：

```python
import chromadb

# 设置 Chroma 内存模式，便于原型开发。可以轻松添加持久化！
client = chromadb.Client()

# 创建集合。也支持 get_collection, get_or_create_collection, delete_collection
collection = client.create_collection("all-my-documents")

# 向集合添加文档。也支持更新和删除。行式 API 即将推出！
collection.add(
    documents=["这是文档1", "这是文档2"],  # 我们自动处理分词、嵌入和索引。您也可以跳过这些并添加自己的嵌入
    metadatas=[{"source": "notion"}, {"source": "google-docs"}],  # 可以按这些过滤！
    ids=["doc1", "doc2"],  # 每个文档唯一
)

# 查询/搜索 2 个最相似的结果。您也可以按 ID 获取
results = collection.query(
    query_texts=["这是一个查询文档"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"},  # 可选过滤
    # where_document={"$contains": "search_string"}  # 可选过滤
)
```

### 使用场景

例如，“与您的数据聊天” 使用场景：

1. 将文档添加到数据库。您可以传入自己的嵌入、嵌入函数，或让 Chroma 为您嵌入。
2. 使用自然语言查询相关文档。
3. 将文档组合到 LLM（如 GPT-4）的上下文窗口中，以进行额外总结或分析。

## 嵌入

嵌入是将图像/文本/音频转换为数字列表的过程。Chroma 默认使用 Sentence Transformers 进行嵌入，但也支持 OpenAI 嵌入、Cohere 多语言嵌入或您自己的嵌入。

更多信息请参考 [文档](https://docs.trychroma.com)。
