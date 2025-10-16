
---
title: open-lovable
---

# Open-Lovable 项目

**GitHub 项目地址:** [https://github.com/firecrawl/open-lovable](https://github.com/firecrawl/open-lovable)

## 主要特性
Open-Lovable 是一个开源项目，旨在提供一个可爱的、易于使用的 AI 驱动工具集。它基于 Firecrawl 的爬虫技术，专注于简化网页数据提取和处理。核心特性包括：
- **网页爬取与解析**：高效爬取网站内容，支持 Markdown、HTML 和结构化数据输出。
- **AI 集成**：内置 AI 模型支持，用于内容总结、提取和转换。
- **开源与可扩展**：使用 Rust 编写，模块化设计，便于开发者自定义和扩展。
- **轻量级部署**：支持 Docker 和本地运行，适合个人或小型团队使用。
- **隐私优先**：强调数据本地处理，避免第三方依赖。

## 主要功能
- **爬虫引擎**：自动处理 JavaScript 渲染页面，提取文本、图像和链接。
- **数据转换**：将爬取内容转换为 Markdown、JSON 等格式，便于后续处理。
- **API 接口**：提供 RESTful API，支持批量任务和实时查询。
- **监控与日志**：内置任务队列和错误日志，帮助调试和优化爬取过程。
- **集成示例**：与 LangChain、LlamaIndex 等 AI 框架无缝集成，用于构建 RAG（Retrieval-Augmented Generation）应用。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/firecrawl/open-lovable.git`
   - 进入目录：`cd open-lovable`
   - 使用 Cargo 构建（需安装 Rust）：`cargo build --release`

2. **运行**：
   - 本地启动服务器：`cargo run --release`
   - 或使用 Docker：`docker build -t open-lovable . && docker run -p 3000:3000 open-lovable`

3. **基本使用**：
   - 通过 API 爬取页面：发送 POST 请求到 `/crawl` 端点，参数包括 URL 和输出格式。
     示例（使用 curl）：
     ```
     curl -X POST http://localhost:3000/crawl \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com", "format": "markdown"}'
     ```
   - 处理响应：API 返回爬取的数据，可直接用于 AI 模型输入或存储。

4. **高级用法**：
   - 配置爬虫规则：在 `config.toml` 中自定义排除路径、深度限制等。
   - 集成到项目：导入 Rust 库或使用 Python 绑定（若可用），例如在脚本中调用爬取函数。
   - 监控任务：访问 `/status` 端点查看队列状态。

更多细节请参考仓库的 README 和文档。