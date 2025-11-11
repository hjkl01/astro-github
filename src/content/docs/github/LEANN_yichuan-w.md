---
title: LEANN
---

# LEANN

LEANN 是一个创新的向量数据库，通过图基选择性重计算和高程度保留修剪技术，实现个人AI的民主化。它能够在不损失准确性的情况下，使用传统解决方案97%的存储空间，将您的笔记本电脑转变为强大的RAG系统。

## 主要功能

- **极低存储占用**：索引6000万个文本块仅需6GB存储空间，而传统向量数据库需要201GB。
- **完全私有**：数据永远不会离开您的设备，无需云服务或API密钥。
- **轻量级**：图基重计算消除重嵌入存储，同时智能图修剪最小化图存储开销。
- **可移植**：在设备之间传输整个知识库，几乎没有成本。
- **可扩展**：轻松处理混乱的个人数据，能够管理不断增长的个性化数据和代理生成内存。
- **无准确性损失**：在相同搜索质量下，使用97%更少的存储。

## 支持的数据源

LEANN 支持对各种数据源进行RAG，包括：

- **文档**：PDF、TXT、MD文件
- **电子邮件**：Apple Mail
- **浏览器历史**：Chrome浏览器历史
- **聊天历史**：WeChat、iMessage、ChatGPT、Claude
- **实时数据**：通过MCP（Model Context Protocol）连接Slack、Twitter等平台
- **代码库**：与Claude Code集成，提供语义代码搜索

## 安装

### 先决条件：安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 快速安装

克隆仓库并安装：

```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
uv venv
source .venv/bin/activate
uv pip install leann
```

### 从源码构建（推荐用于开发）

```bash
git clone https://github.com/yichuan-w/LEANN.git leann
cd leann
git submodule update --init --recursive
uv sync --extra diskann
```

## 快速开始

LEANN 的声明式API使RAG变得简单：

```python
from leann import LeannBuilder, LeannSearcher, LeannChat
from pathlib import Path

INDEX_PATH = str(Path("./").resolve() / "demo.leann")

# 构建索引
builder = LeannBuilder(backend_name="hnsw")
builder.add_text("LEANN saves 97% storage compared to traditional vector databases.")
builder.add_text("Tung Tung Tung Sahur called—they need their banana‑crocodile hybrid back")
builder.build_index(INDEX_PATH)

# 搜索
searcher = LeannSearcher(INDEX_PATH)
results = searcher.search("fantastical AI-generated creatures", top_k=1)

# 与数据聊天
chat = LeannChat(INDEX_PATH, llm_config={"type": "hf", "model": "Qwen/Qwen3-0.6B"})
response = chat.ask("How much storage does LEANN save?", top_k=1)
```

## 使用示例

### 文档RAG

处理任何文档目录：

```bash
source .venv/bin/activate
python -m apps.document_rag --query "What are the main techniques LEANN explores?"
```

### 电子邮件RAG

搜索Apple Mail：

```bash
python -m apps.email_rag --query "What's the food I ordered by DoorDash or Uber Eats mostly?"
```

### 浏览器历史RAG

搜索Chrome浏览器历史：

```bash
python -m apps.browser_rag --query "Tell me my browser history about machine learning?"
```

### WeChat RAG

搜索WeChat聊天记录：

```bash
python -m apps.wechat_rag --query "Show me all group chats about weekend plans"
```

### ChatGPT历史RAG

搜索ChatGPT对话：

```bash
python -m apps.chatgpt_rag --export-path chatgpt_export.html --query "How do I create a list in Python?"
```

### Claude Code集成

与Claude Code集成进行代码搜索：

```bash
uv tool install leann-core --with leann
claude mcp add --scope user leann-server -- leann_mcp
```

## CLI界面

LEANN 提供强大的CLI用于文档处理和搜索：

```bash
# 构建索引
leann build my-docs --docs ./your_documents

# 搜索文档
leann search my-docs "machine learning concepts"

# 交互式聊天
leann ask my-docs --interactive

# 列出所有索引
leann list

# 删除索引
leann remove my-docs
```

## 架构原理

LEANN 通过图基选择性重计算实现存储节省：

- **图基选择性重计算**：仅在搜索路径中计算节点的嵌入
- **高程度保留修剪**：保持重要"枢纽"节点，同时移除冗余连接
- **动态批处理**：高效批处理嵌入计算以利用GPU
- **两级搜索**：智能图遍历，优先考虑有前景的节点

支持两种后端：

- **HNSW**（默认）：适用于大多数数据集，通过完全重计算实现最大存储节省
- **DiskANN**：高级选项，具有卓越的搜索性能，使用基于PQ的图遍历和实时重排序以获得最佳速度-准确性权衡

## 基准测试

| 系统           | DPR (2.1M) | Wiki (60M) | Chat (400K) | Email (780K) | Browser (38K) |
| -------------- | ---------- | ---------- | ----------- | ------------ | ------------- |
| 传统向量数据库 | 3.8 GB     | 201 GB     | 1.8 GB      | 2.4 GB       | 130 MB        |
| LEANN          | 324 MB     | 6 GB       | 64 MB       | 79 MB        | 6.4 MB        |
| 节省           | 91%        | 97%        | 97%         | 97%          | 95%           |

## 许可证

MIT License
