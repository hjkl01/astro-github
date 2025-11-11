---
title: Deepwiki Open
---

# DeepWiki-Open

**DeepWiki** 是一个开源的 AI 驱动的 Wiki 生成器，专为 GitHub、GitLab 和 Bitbucket 仓库设计。它可以自动分析代码结构，生成全面的文档，创建视觉图表，并将所有内容组织成易于导航的交互式 Wiki。

## ✨ 主要功能

- **即时文档生成**：只需输入仓库名称，即可将任何 GitHub、GitLab 或 Bitbucket 仓库转换为 Wiki
- **私有仓库支持**：使用个人访问令牌安全访问私有仓库
- **智能分析**：AI 驱动的代码结构和关系理解
- **美丽图表**：自动生成 Mermaid 图表以可视化架构和数据流
- **易于导航**：简单直观的界面探索 Wiki
- **问答功能**：使用 RAG 驱动的 AI 与仓库聊天，获取准确答案
- **深度研究**：多轮研究过程，深入调查复杂主题
- **多模型提供商支持**：支持 Google Gemini、OpenAI、OpenRouter 和本地 Ollama 模型
- **灵活嵌入**：选择 OpenAI、Google AI 或本地 Ollama 嵌入以获得最佳性能

## 🚀 快速开始

### 使用 Docker（推荐）

1. 克隆仓库：

   ```bash
   git clone https://github.com/AsyncFuncAI/deepwiki-open.git
   cd deepwiki-open
   ```

2. 创建 `.env` 文件并添加 API 密钥：

   ```bash
   echo "GOOGLE_API_KEY=your_google_api_key" > .env
   echo "OPENAI_API_KEY=your_openai_api_key" >> .env
   # 可选：使用 Google AI 嵌入而不是 OpenAI（推荐使用 Google 模型时）
   echo "DEEPWIKI_EMBEDDER_TYPE=google" >> .env
   ```

3. 使用 Docker Compose 运行：
   ```bash
   docker-compose up
   ```

### 手动设置

1. **设置 API 密钥**：在项目根目录创建 `.env` 文件，包含必要的 API 密钥。

2. **启动后端**：

   ```bash
   python -m pip install poetry==1.8.2 && poetry install -C api
   python -m api.main
   ```

3. **启动前端**：

   ```bash
   npm install
   npm run dev
   ```

4. **使用 DeepWiki**：
   - 打开浏览器访问 `http://localhost:3000`
   - 输入 GitHub、GitLab 或 Bitbucket 仓库 URL（如 `https://github.com/openai/codex`）
   - 对于私有仓库，点击 "+ 添加访问令牌" 并输入个人访问令牌
   - 点击 "生成 Wiki" 观看魔法发生！

## 🔍 工作原理

DeepWiki 使用 AI 来：

1. 克隆和分析 GitHub、GitLab 或 Bitbucket 仓库（包括使用令牌认证的私有仓库）
2. 为智能检索创建代码嵌入
3. 使用上下文感知 AI 生成文档（支持 Google Gemini、OpenAI、OpenRouter、Azure OpenAI 或本地 Ollama 模型）
4. 创建视觉图表解释代码关系
5. 将所有内容组织成结构化 Wiki
6. 通过问答功能启用与仓库的智能对话
7. 通过 DeepResearch 提供深入研究能力

## 🛠️ 项目结构

```
deepwiki/
├── api/                  # 后端 API 服务器
│   ├── main.py           # API 入口点
│   ├── api.py            # FastAPI 实现
│   ├── rag.py            # 检索增强生成
│   └── data_pipeline.py  # 数据处理工具
├── src/                  # 前端 Next.js 应用
│   ├── app/              # Next.js 应用目录
│   └── components/       # React 组件
├── public/               # 静态资源
└── .env                  # 环境变量（需要创建）
```

## 🤖 支持的提供商和模型

- **Google**：默认 `gemini-2.5-flash`，还支持 `gemini-2.5-flash-lite`、`gemini-2.5-pro` 等
- **OpenAI**：默认 `gpt-4o-mini`，还支持 `gpt-4o`、`gpt-4` 等
- **OpenRouter**：通过统一 API 访问多个模型，包括 Claude、Llama、Mistral 等
- **Azure OpenAI**：默认 `gpt-4o`，还支持 `gpt-4o-mini` 等
- **Ollama**：支持本地运行的开源模型，如 `llama3`

## 📱 截图

![DeepWiki 主界面](https://gh.hjkl01.cn/https://raw.githubusercontent.com/AsyncFuncAI/deepwiki-open/main/screenshots/Interface.png)

_DeepWiki 的主界面_

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/LICENSE) 文件。

## 关于

开源 DeepWiki：GitHub/GitLab/Bitbucket 仓库的 AI 驱动 Wiki 生成器。加入 Discord：[https://discord.gg/gMwThUMeme](https://discord.gg/gMwThUMeme)
