
---
title: mem0
---


# mem0 – 适用于 LLM 的模块化记忆框架

> 项目地址: [https://github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)

## 1 项目简介
mem0 是一个开源的、可扩展的记忆框架，旨在为大型语言模型（LLM）提供高效、可插拔的知识存储与检索能力。它通过统一的 API 与多种存储后端（如向量数据库、文件系统、数据库等）集成，帮助开发者在对话、搜索、问答等场景中实现智能记忆。

## 2 主要特性
- **模块化设计**：核心功能拆分为 `MemoryStore`, `Retriever`, `Ranker`, `Formatter` 等组件，支持自定义实现。
- **多后端支持**：内置向量数据库（如 Milvus, Pinecone, Weaviate）、SQL/NoSQL 数据库、文件系统等存储方案。
- **高效检索**：基于向量检索的近似最近邻（ANN）算法，支持多种距离度量。
- **上下文管理**：自动维护对话上下文、知识片段，支持时间戳、标签等元数据。
- **插件化**：通过 `mem0-plugin` 机制可轻松接入第三方服务（如搜索引擎、知识图谱）。
- **Python、Rust 双实现**：Python SDK 便于快速集成，Rust 实现提供高性能后端。

## 3 关键模块
| 模块 | 作用 |
|------|------|
| `MemoryStore` | 抽象数据持久化层，负责存储、更新、删除知识片段 |
| `Retriever` | 根据查询文本检索相关片段，支持向量检索与布尔检索 |
| `Ranker` | 对检索结果进行排序，结合语义相似度、权重等 |
| `Formatter` | 生成 LLM 可直接使用的提示模板，支持多轮对话 |
| `Pipeline` | 将上述组件串联，形成完整的记忆-检索-生成流程 |

## 4 快速上手

### 4.1 安装
```bash
pip install mem0
```

### 4.2 基本使用示例
```python
from mem0 import Mem0, MemoryStore, Retriever, Formatter

# 1. 初始化存储（使用默认内存存储）
store = MemoryStore()

# 2. 添加知识片段
store.add(
    key="mem0_docs",
    value="mem0 是一个开源的记忆框架，支持多后端存储。",
    metadata={"source": "GitHub"}
)

# 3. 初始化检索器
retriever = Retriever(store=store)

# 4. 查询
query = "mem0是什么"
results = retriever.search(query, top_k=3)

# 5. 格式化为 LLM 提示
formatter = Formatter()
prompt = formatter.format(query, results)

print(prompt)
```

### 4.3 高级用法
- **自定义后端**：实现 `MemoryStore` 的子类，支持自定义数据库或文件系统。
- **多轮对话**：使用 `Formatter` 的 `conversation` 模式，自动维护上下文。
- **插件**：在 `mem0.plugin` 目录下实现插件接口，接入外部 API。

## 5 文档与资源
- 官方文档: https://mem0.ai/docs
- 示例代码: https://github.com/mem0ai/mem0/tree/main/examples
- 社区讨论: https://github.com/mem0ai/mem0/discussions

## 6 贡献
欢迎在 GitHub 上提交 Issue 或 PR。请遵循项目的贡献指南和编码规范。

--- 

> 本文件仅为快速参考，详情请参阅官方文档与源代码。
