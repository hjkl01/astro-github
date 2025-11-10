---
title: llm-app
---

# llm-app

## 功能介绍

llm-app 是 Pathway 提供的 AI 管道模板库，提供 ready-to-run 的云端模板，用于构建 RAG（Retrieval-Augmented Generation）、AI 管道和企业级搜索应用。这些模板支持实时数据同步，能够处理来自文件系统、Google Drive、Sharepoint、S3、Kafka、PostgreSQL 和实时数据 API 的数据。

主要功能包括：

- **高精度 RAG 和 AI 企业搜索**：支持大规模文档处理（可扩展到数百万页文档）。
- **实时数据同步**：自动同步数据源中的新增、删除和更新操作。
- **内置数据索引**：提供向量搜索、混合搜索和全文搜索，所有操作都在内存中进行，并支持缓存。
- **Docker 友好**：应用可以作为 Docker 容器运行，无需额外基础设施依赖。
- **多模态支持**：支持处理 PDF、DOCX 等文档，包括图表和表格的提取。

提供的应用模板包括：

- **Question-Answering RAG App**：基本的端到端 RAG 应用，用于回答文档查询。
- **Live Document Indexing**：实时文档索引管道，作为向量存储服务。
- **Multimodal RAG pipeline with GPT4o**：使用 GPT-4o 的多模态 RAG，用于处理金融文档等。
- **Unstructured-to-SQL pipeline**：将非结构化数据转换为 SQL 并支持自然语言查询。
- **Adaptive RAG App**：使用自适应 RAG 技术降低 token 成本。
- **Private RAG App with Mistral and Ollama**：完全私有的本地 RAG 应用。
- **Slides AI Search App**：用于检索幻灯片的索引管道。

## 用法

1. **选择模板**：从 [templates](/pathwaycom/llm-app/blob/main/templates) 目录中选择合适的模板，每个模板都有详细的 README.md 说明。

2. **运行应用**：
   - 应用可以作为 Docker 容器运行。
   - 暴露 HTTP API 用于前端连接。
   - 部分模板提供可选的 Streamlit UI 用于快速测试和演示。

3. **配置数据源**：连接到所需的数据源，如 Google Drive、Sharepoint 等，应用会自动同步数据。

4. **部署**：支持云端部署（GCP、AWS、Azure、Render 等）或本地部署。

5. **集成**：可以与 Langchain 或 Llamaindex 集成，或作为检索后端使用。

更多详细信息和代码模板，请访问 [Pathway 开发者模板页面](https://pathway.com/developers/templates/)。
