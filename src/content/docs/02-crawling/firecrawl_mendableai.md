
---
title: firecrawl
---

# Firecrawl 项目

**项目地址**: [https://github.com/mendableai/firecrawl](https://github.com/mendableai/firecrawl)

## 主要特性
Firecrawl 是一个开源的网络爬虫和抓取工具，专为 AI 应用设计。它将网站内容转换为适合大型语言模型 (LLM) 处理的格式，如 Markdown 或结构化数据。主要特性包括：
- **智能爬取**：支持爬取整个网站、单个页面或特定 URL，支持动态内容和 JavaScript 渲染。
- **格式转换**：自动将 HTML 转换为干净的 Markdown，支持提取纯文本、图像和元数据。
- **API 集成**：提供简单易用的 API 接口，便于集成到 AI 工作流中。
- **可扩展性**：处理大规模爬取任务，支持代理、延迟控制和错误处理。
- **开源与免费**：基于 Node.js 构建，易于自托管或使用托管版本。

## 主要功能
- **爬取模式**：包括“scrape”（单页抓取）、“crawl”（全站爬取）和“map”（站点映射）。
- **数据提取**：提取链接、标题、内容，支持自定义选择器和过滤器。
- **输出格式**：支持 Markdown、JSON 和纯文本输出，便于 LLM 摄取。
- **高级选项**：处理登录、CAPTCHA、速率限制，以及多语言支持。
- **监控与日志**：提供爬取进度跟踪和错误日志。

## 用法
1. **安装**：
   - 克隆仓库：`git clone https://github.com/mendableai/firecrawl.git`
   - 安装依赖：`npm install`

2. **基本用法（API 示例）**：
   - 使用 Node.js 脚本或直接调用 API。
   - 示例（爬取单个页面）：
     ```javascript
     const { FirecrawlApp } = require('@mendable/firecrawl-js');

     const app = new FirecrawlApp({ apiKey: 'your-api-key' });

     async function scrapePage() {
       const result = await app.scrapeUrl('https://example.com');
       console.log(result.data); // 输出 Markdown 或 JSON
     }

     scrapePage();
     ```
   - 全站爬取示例：
     ```javascript
     const crawlResult = await app.crawlUrl('https://example.com', { crawlerOptions: { excludes: ['/admin*'] } });
     ```

3. **自托管**：
   - 运行本地服务器：`npm run dev`
   - 配置环境变量（如 API 密钥、代理设置）。

4. **集成**：
   - 与 LangChain 或其他 AI 框架结合使用。
   - 托管版本：通过 Firecrawl 的云服务获取 API 密钥（免费额度可用）。

更多细节请参考项目 README。