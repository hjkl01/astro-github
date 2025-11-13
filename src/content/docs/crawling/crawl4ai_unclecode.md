---
title: crawl4ai
---

# Crawl4AI 项目

**GitHub 项目地址:** [https://github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)

## 主要特性
Crawl4AI 是一个开源的异步网络爬虫和抓取工具，专为 AI 应用设计。它以高效、可靠和易用为核心，提供以下关键特性：
- **异步处理**：支持高并发爬取，提高效率，适合大规模数据采集。
- **AI 友好**：集成 LLM（大型语言模型）提取功能，能智能解析网页内容，支持结构化输出如 JSON。
- **浏览器集成**：内置 Playwright 支持，可模拟真实浏览器行为，处理 JavaScript 渲染页面。
- **媒体与资源提取**：自动提取图像、视频、CSS 和 JS 等资源，支持自定义过滤。
- **错误处理与重试**：内置鲁棒性机制，确保爬取稳定，支持代理和用户代理旋转。
- **扩展性**：模块化设计，便于自定义钩子（hooks）和策略，适用于研究、数据分析和 AI 训练。

## 主要功能
- **网页爬取**：从 URL 抓取 HTML、文本和元数据，支持深度爬取（多页）。
- **内容提取**：使用 CSS 选择器或 XPath 提取特定元素；集成 LLM 进行语义提取，如总结、实体识别。
- **多媒体处理**：下载并解析媒体文件，支持本地存储或云上传。
- **数据清洗**：去除噪声、规范化输出，支持 Markdown 或 JSON 格式。
- **监控与日志**：提供详细日志和进度跟踪，便于调试。
- **集成支持**：兼容 Python 生态，如 LangChain、FastAPI 等，易于嵌入 AI 管道。

## 用法
Crawl4AI 使用 Python 实现，安装简单。以下是基本用法指南：

### 安装
```bash
pip install crawl4ai
```

### 基本示例
1. **简单爬取**：
   ```python
   from crawl4ai import AsyncWebCrawler

   async def main():
       async with AsyncWebCrawler() as crawler:
           result = await crawler.arun(url="https://example.com")
           print(result.markdown)  # 输出 Markdown 格式内容

   import asyncio
   asyncio.run(main())
   ```

2. **使用 LLM 提取**：
   ```python
   from crawl4ai import AsyncWebCrawler
   import asyncio

   async def main():
       async with AsyncWebCrawler(verbose=True) as crawler:
           result = await crawler.arun(
               url="https://example.com",
               extraction_strategy="llm_extraction",  # 使用 LLM 策略
               llm_model="gpt-4"  # 指定模型（需配置 API 密钥）
           )
           print(result.extracted_content)  # 输出提取的结构化数据

   asyncio.run(main())
   ```

3. **高级配置**：
   - 支持 `js_code` 参数注入 JavaScript 执行。
   - 使用 `hook_non_dom` 处理非 DOM 内容。
   - 配置代理：`crawler_config={"proxy": "http://proxy.example.com"}`。
   - 更多细节见官方文档：项目 README 和 examples 目录。

项目适合开发者快速构建 AI 数据管道，代码开源，欢迎贡献。