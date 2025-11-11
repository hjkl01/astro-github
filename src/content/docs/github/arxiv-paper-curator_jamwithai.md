---
title: ArXiv Paper Curator
---

## 项目简介

ArXiv Paper Curator 是一个专注于学习者的项目，通过动手实现教你构建现代AI系统的核心技能：检索增强生成（RAG）。该项目将自动获取学术论文、理解其内容，并基于你的研究问题提供智能回答。

## 主要功能

- **自动论文获取**：从arXiv API获取最新学术论文，支持分类过滤和日期范围查询
- **智能文档处理**：使用Docling解析PDF文档，提取结构化内容（文本、表格、图片）
- **混合搜索系统**：结合BM25关键词搜索和向量语义搜索，实现高效检索
- **完整RAG管道**：集成本地LLM（Ollama），支持流式响应和交互式界面
- **生产级监控**：使用Langfuse进行管道追踪，Redis缓存优化性能
- **工作流自动化**：Apache Airflow管理数据摄取和处理任务

## 技术栈

- **后端**：FastAPI (REST API), PostgreSQL (数据存储), OpenSearch (搜索引擎)
- **AI/ML**：Ollama (本地LLM), Jina AI (嵌入生成), Langfuse (监控)
- **基础设施**：Docker Compose, Apache Airflow, Redis (缓存)
- **开发工具**：UV (包管理), Ruff/MyPy (代码质量), Pytest (测试)

## 快速开始

### 环境要求

- Docker Desktop
- Python 3.12+
- UV 包管理器
- 8GB+ RAM 和 20GB+ 磁盘空间

### 安装步骤

1. **克隆项目**

   ```bash
   git clone https://github.com/jamwithai/arxiv-paper-curator.git
   cd arxiv-paper-curator
   ```

2. **配置环境**

   ```bash
   cp .env.example .env
   # 编辑 .env 文件，设置必要配置
   ```

3. **安装依赖**

   ```bash
   uv sync
   ```

4. **启动服务**

   ```bash
   docker compose up --build -d
   ```

5. **验证安装**
   ```bash
   curl http://localhost:8000/health
   ```

## 使用方法

### API 接口

- **健康检查**：`GET /health`
- **获取论文**：`GET /api/v1/papers`
- **关键词搜索**：`POST /api/v1/search`
- **混合搜索**：`POST /api/v1/hybrid-search/`
- **RAG问答**：`POST /api/v1/ask` (标准) 或 `/api/v1/stream` (流式)

### 交互界面

- **API文档**：http://localhost:8000/docs
- **Gradio界面**：http://localhost:7861
- **Langfuse监控**：http://localhost:3000
- **Airflow管理**：http://localhost:8080

### 示例用法

**搜索论文**

```bash
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "transformer attention mechanism", "max_results": 5}'
```

**RAG问答**

```bash
curl -X POST "http://localhost:8000/api/v1/ask" \
  -H "Content-Type: application/json" \
  -d '{"query": "What are transformers in machine learning?", "top_k": 3}'
```

## 学习路径

项目按周组织学习内容：

1. **Week 1**：基础设施搭建 (Docker, FastAPI, PostgreSQL, OpenSearch)
2. **Week 2**：数据摄取管道 (arXiv API, PDF解析, Airflow)
3. **Week 3**：关键词搜索 (BM25算法, OpenSearch集成)
4. **Week 4**：分块与混合搜索 (智能分块, 向量嵌入, RRF融合)
5. **Week 5**：完整RAG系统 (本地LLM, 流式响应, Gradio界面)
6. **Week 6**：生产监控与缓存 (Langfuse追踪, Redis缓存)

## 许可证

MIT License
