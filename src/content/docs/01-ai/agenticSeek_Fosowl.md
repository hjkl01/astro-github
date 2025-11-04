
---
title: agenticSeek
---


# agenticSeek（Fosowl）

[GitHub](https://github.com/Fosowl/agenticSeek)

## 项目概述

agenticSeek 是一个可插拔的 **多模态检索 + 增强型 LLM** 框架，旨在帮助开发者快速构建 **面向业务的检索增强对话系统**。它通过统一的插件体系，将外部知识库、检索器以及扩展算子组合成一个灵活的工作流，支持离线索引、实时检索与对话交互。

## 主要特性

| 特性 | 描述 |
|------|------|
| **插件化检索器** | 目前集成了 Elastic Search、OpenSearch、Pinecone、Milvus 等主流向量检索后端，支持自定义检索插件。 |
| **知识源适配** | 支持本地文本、Markdown、PDF、CSV、网页抓取等多种数据源，自动生成向量索引。 |
| **多轮对话管理** | 内置对话状态管理和上下文对齐，使用 OpenAI/Claude 等 LLM 进行意图解析与答案生成。 |
| **流式响应** | 对话输出可按流式方式返回，适配实时 UI。 |
| **可视化 UI** | 提供 Next.js/Froala 框架前端示例，展示检索结果与 LLM 交互。 |
| **可扩展算子** | 通过插件框架可以自由添加数据清洗、问答生成、外部 API 调用等算子。 |
| **安全与访问控制** | 支持 API Key、IP 白名单、速率限制等基本安全防护。 |

## 核心结构

```
agenticSeek/
├── src/
│   ├── core/        # 核心引擎
│   ├── plugins/     # 检索器 / 数据源插件
│   ├── processors/  # 对话处理器
│   └── utils/       # 工具类
└── frontend/        # Next.js UI 示例
```

## 使用方法

### 1. 环境准备

```bash
# 安装依赖
pip install -r requirements.txt

# 创建 .env
cp .env.example .env
# 填写你的 LLM API Key、检索后端配置等
```

### 2. 数据索引

```python
from agenticSeek import Indexer

# 以本地文本为例
indexer = Indexer("my_index")
files = ["docs/guide.txt", "docs/readme.md"]
indexer.index_files(files)
```

### 3. 启动后台服务

```bash
python -m agenticSeek.server
```

服务默认监听 `http://localhost:8000`。

### 4. 与 LLM 对话

```python
import requests

payload = {"question": "如何使用 agenticSeek 进行向量检索？"}
resp = requests.post("http://localhost:8000/api/chat", json=payload)
print(resp.json()["answer"])
```

### 5. 前端 Demo

```bash
cd frontend
npm install
npm run dev
```

然后在浏览器打开 `http://localhost:3000`。

## 随机命令与 Debug

- 查看日志：`python -m agenticSeek.server --debug`
- 检索器状态：`python -m agenticSeek.cli status`
- 重新索引：`python -m agenticSeek.cli reindex my_index`

## 贡献指南

请先 Fork → Clone → 新建分支 → PR，并遵循：

1. 代码规范：PEP8（Python）、Prettier（前端）
2. 单元测试：覆盖率 ≥ 80%
3. 文档更新：所有新增功能须附 Markdown 说明

如需更详细的使用手册，请参考 `docs/` 目录。

---

**更多信息**：  
🚀 访问仓库并 star 🌟  
GitHub：[Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek)
