
---
title: KrillinAI
---


# KrillinAI

> 项目地址: [https://github.com/krillinai/KrillinAI](https://github.com/krillinai/KrillinAI)

## 项目概述  
KrillinAI 是一套轻量级、可扩展的 AI 开发框架，旨在帮助开发者快速搭建具备自然语言理解与生成能力的应用。框架集成了 LLM（大型语言模型）调用、检索增强生成（RAG）、自定义 Prompt 以及多模型融合等核心技术，支持从本地部署到云端微服务的一键式部署。

## 核心特性  

| 特性 | 说明 |
|------|------|
| **多模型支持** | 兼容 OpenAI、Google Gemini、Anthropic 等主流 LLM，支持自定义模型 URL。 |
| **检索增强生成 (RAG)** | 内置向量检索（FAISS、Milvus 等）与知识库加载，支持文档检索 + 生成式回答。 |
| **Prompt 管理** | 通过 YAML/JSON 配置文件管理 Prompt 模板，支持占位符和条件逻辑。 |
| **链式调用（Chain）** | 轻量级链式编排，支持多轮对话、工具调用（如外部 API、数据库查询）。 |
| **CLI 与 SDK** | 提供命令行工具快速启动服务、调试模型；Python SDK 可直接在代码中调用。 |
| **Docker & Kubernetes** | 官方 Docker 镜像，支持 Helm Chart，适配云原生部署。 |
| **监控与日志** | 集成 OpenTelemetry，支持 Prometheus 监控与 Loki 日志。 |
| **多语言** | 支持中文、英文、日文等多语言 Prompt 与输出。 |

## 主要功能模块  

1. **model_loader** – 统一 LLM 加载器，支持模型选择与参数调优。  
2. **retriever** – 文档检索器，支持文本、PDF、Markdown 等多种格式。  
3. **prompt_engine** – Prompt 生成引擎，支持模板渲染与动态变量。  
4. **chain** – 业务链路编排，内置对话管理、工具调用、后处理。  
5. **api_server** – FastAPI + Uvicorn API 服务器，提供 REST 和 WebSocket 接口。  
6. **cli** – 命令行工具，包含 `krillinai start`、`krillinai train`、`krillinai test` 等子命令。  

## 快速上手  

```bash
# 克隆仓库
git clone https://github.com/krillinai/KrillinAI.git
cd KrillinAI

# 创建虚拟环境并安装依赖
python -m venv venv
source venv/bin/activate
pip install -e .

# 配置模型（示例：OpenAI GPT-4）
cat > config.yaml <<EOF
model:
  type: openai
  api_key: YOUR_OPENAI_API_KEY
  name: gpt-4
retriever:
  type: faiss
  index_path: ./data/faiss.index
prompt:
  template: |
    你是一名专业的 AI 助手。请回答以下问题：
    {question}
EOF

# 启动 API 服务器
krillinai start --config config.yaml
```

- 访问 `http://localhost:8000/docs` 查看 Swagger 文档。  
- 通过 `curl` 或前端页面发送 POST 请求到 `/chat`，即可得到生成式回答。  

## 贡献与维护  

- 代码遵循 PEP8，使用 `black`、`isort` 进行格式化。  
- 所有功能均通过单元测试覆盖，运行 `pytest` 进行测试。  
- Issues 与 PR 均欢迎，遵循 `CONTRIBUTING.md` 指南。  

## 许可证  

KrillinAI 采用 MIT 许可证发布，详情请参见 `LICENSE` 文件。  

---  

> 本文件为 `src/content/docs/00/KrillinAI_krillinai.md` 的内容，已包含项目地址、主要特性、功能及用法。