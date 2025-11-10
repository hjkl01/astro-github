# DeepWiki-Open

## 项目简介

DeepWiki-Open 是一个开源的 AI 驱动的 Wiki 生成器，专为 GitHub、GitLab 和 Bitbucket 仓库设计。它可以自动分析代码结构，生成全面的文档，并创建可视化图表来解释代码的工作原理。

## 主要功能

- **即时文档生成**：只需输入仓库名称，即可将任何 GitHub、GitLab 或 Bitbucket 仓库转换为 Wiki
- **私有仓库支持**：使用个人访问令牌安全访问私有仓库
- **智能分析**：AI 驱动的代码结构和关系理解
- **美观图表**：自动生成 Mermaid 图表来可视化架构和数据流
- **易于导航**：简单直观的界面来探索 Wiki
- **问答功能**：使用 RAG 驱动的 AI 与仓库聊天，获取准确答案
- **深度研究**：多轮研究过程，深入调查复杂主题
- **多种模型提供商**：支持 Google Gemini、OpenAI、OpenRouter 和本地 Ollama 模型
- **灵活嵌入**：在 OpenAI、Google AI 或本地 Ollama 嵌入之间选择，以获得最佳性能

## 快速开始

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
   # 可选：添加 OpenRouter API 密钥
   echo "OPENROUTER_API_KEY=your_openrouter_api_key" >> .env
   # 可选：添加 Ollama 主机
   echo "OLLAMA_HOST=your_ollama_host" >> .env
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
   - 在浏览器中打开 http://localhost:3000
   - 输入 GitHub、GitLab 或 Bitbucket 仓库 URL（如 `https://github.com/openai/codex`）
   - 对于私有仓库，点击 "+ 添加访问令牌" 并输入个人访问令牌
   - 点击 "生成 Wiki" 并观看魔法发生！

## 工作原理

DeepWiki 使用 AI 来：

1. 克隆和分析 GitHub、GitLab 或 Bitbucket 仓库（包括使用令牌认证的私有仓库）
2. 为智能检索创建代码嵌入
3. 使用 Google Gemini、OpenAI、OpenRouter、Azure OpenAI 或本地 Ollama 模型生成上下文感知文档
4. 创建可视化图表来解释代码关系
5. 将所有内容组织成结构化 Wiki
6. 通过问答功能启用对仓库的智能 Q&A
7. 提供深度研究功能

## 支持的模型提供商

- **Google**：默认 `gemini-2.5-flash`，也支持 `gemini-2.5-flash-lite`、`gemini-2.5-pro` 等
- **OpenAI**：默认 `gpt-5-nano`，也支持 `gpt-5`、`4o` 等
- **OpenRouter**：通过统一 API 访问多个模型，包括 Claude、Llama、Mistral 等
- **Azure OpenAI**：默认 `gpt-4o`，也支持 `o4-mini` 等
- **Ollama**：支持本地运行的开源模型，如 `llama3`

## 环境变量

- `GOOGLE_API_KEY`：Google Gemini API 密钥
- `OPENAI_API_KEY`：OpenAI API 密钥
- `OPENROUTER_API_KEY`：OpenRouter API 密钥
- `AZURE_OPENAI_API_KEY`、`AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_VERSION`：Azure OpenAI 凭据
- `OLLAMA_HOST`：Ollama 主机（默认：http://localhost:11434）
- `DEEPWIKI_EMBEDDER_TYPE`：嵌入类型（`openai`、`google` 或 `ollama`）

## 许可证

MIT License
