---
title: SurfSense
---

# SurfSense

## 项目简介

SurfSense 是一个开源的 AI 研究代理工具，是 NotebookLM 和 Perplexity 的替代品。它允许用户将个人知识库与外部来源（如搜索引擎、Slack、Linear、Jira、ClickUp、Confluence、Notion、YouTube、GitHub、Discord 等）连接起来，进行高度可定制的 AI 研究。

项目地址：[https://github.com/MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)

官方网站：[https://www.surfsense.com](https://www.surfsense.com)

## 主要功能

### 💡 核心理念

- 提供高度可定制的私有 NotebookLM 和 Perplexity，集成个人知识库。

### 📁 多格式文件上传支持

- 支持上传个人文件（文档、图像、视频），涵盖 50+ 文件扩展名。
- 构建个人知识库。

### 🔍 强大的搜索功能

- 在保存的内容中快速研究或查找信息。

### 💬 与保存内容聊天

- 使用自然语言与内容互动，获取引用答案。

### 📄 引用答案

- 提供类似 Perplexity 的引用答案。

### 🔔 隐私与本地 LLM 支持

- 支持 Ollama 本地 LLM，确保隐私。

### 🏠 自托管能力

- 开源且易于本地部署。

### 🎙️ 播客生成

- 快速生成播客（3 分钟播客可在 20 秒内生成）。
- 将聊天对话转换为音频内容。
- 支持本地 TTS 提供商（如 Kokoro TTS）和多个 TTS 提供商（OpenAI、Azure、Google Vertex AI）。

### 📊 高级 RAG 技术

- 支持 100+ LLM 模型。
- 支持 6000+ 嵌入模型。
- 支持主要重排序器（Pinecode、Cohere、Flashrank 等）。
- 使用分层索引（2 层 RAG 设置）。
- 利用混合搜索（语义 + 全文搜索结合互惠排名融合）。

### ℹ️ 外部来源集成

- 搜索引擎（Tavily、LinkUp、SearxNG 自托管实例）。
- Slack、Linear、Jira、ClickUp、Confluence、Notion、Gmail、YouTube、GitHub、Discord、Airtable、Google Calendar、Luma、Elasticsearch 等。

### 🔖 跨浏览器扩展

- SurfSense 扩展可用于保存任何网页。
- 主要用于保存受认证保护的网页。

## 支持的文件格式

### 文档与文本

- LlamaCloud：.pdf, .doc, .docx 等（50+ 格式）。
- Unstructured：.doc, .docx, .odt, .rtf, .pdf, .xml, .txt, .md 等（34+ 格式）。
- Docling：.pdf, .docx, .html 等（核心格式，本地处理，无需 API 密钥）。

### 演示文稿

- LlamaCloud：.ppt, .pptx 等。
- Unstructured：.ppt, .pptx。
- Docling：.pptx。

### 电子表格与数据

- LlamaCloud：.xlsx, .xls 等。
- Unstructured：.xls, .xlsx, .csv, .tsv。
- Docling：.xlsx, .csv。

### 图像

- LlamaCloud：.jpg, .jpeg, .png 等。
- Unstructured：.jpg, .jpeg, .png, .bmp, .tiff, .heic。
- Docling：.jpg, .jpeg, .png, .bmp, .tiff, .tif, .webp。

### 音频与视频

- .mp3, .mpga, .m4a, .wav, .mp4, .mpeg, .webm（始终支持）。

### 电子邮件与通信

- Unstructured：.eml, .msg, .p7s。

## 安装与使用

### 安装选项

1. **SurfSense Cloud**：[https://www.surfsense.com/login](https://www.surfsense.com/login)
   - 最简单的方式，无需安装。
   - 即时访问所有功能。

2. **Docker 安装（推荐自托管）**：[https://www.surfsense.net/docs/docker-installation](https://www.surfsense.net/docs/docker-installation)
   - 包含 pgAdmin 用于数据库管理。
   - 支持通过 .env 文件自定义环境变量。
   - 灵活的部署选项（完整堆栈或仅核心服务）。

3. **手动安装**：[https://www.surfsense.net/docs/manual-installation](https://www.surfsense.net/docs/manual-installation)
   - 适用于需要更多控制或自定义部署的用户。

### 先决条件

- 认证设置。
- 文件处理 ETL 服务（选择一个）：
  - Unstructured.io API 密钥（支持 34+ 格式）。
  - LlamaIndex API 密钥（增强解析，支持 50+ 格式）。
  - Docling（本地处理，无需 API 密钥，支持 PDF、Office 文档、图像、HTML、CSV）。
- 其他必需的 API 密钥。

## 技术栈

### 后端

- FastAPI、PostgreSQL with pgvector、SQLAlchemy、Alembic、FastAPI Users、LangGraph、LangChain、LiteLLM、Redis、Celery、Flower、Chonkie 等。

### 前端

- Next.js 15.2.3、React 19.0.0、TypeScript、Tailwind CSS、Shadcn、Lucide React、Framer Motion 等。

### DevOps

- Docker、Docker Compose、pgAdmin。

### 扩展

- Manifest v3 on Plasmo。

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](https://github.com/MODSetter/SurfSense/blob/main/CONTRIBUTING.md) 以获取详细的贡献指南。

加入 Discord：[https://discord.gg/ejRNvftDp9](https://discord.gg/ejRNvftDp9)

## 许可证

Apache-2.0 License
