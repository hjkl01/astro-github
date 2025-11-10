---
title: crawlee-python
---

# Crawlee Python 项目

## 项目地址
[https://github.com/apify/crawlee-python](https://github.com/apify/crawlee-python)

## 主要特性
Crawlee Python 是 Apify 开发的开源网络爬虫和浏览器自动化库，专为 Python 语言设计。它基于 Actor 模型，提供高效的爬取工具，支持多种爬虫类型和自动化场景。主要特性包括：

- **多源爬虫支持**：内置 HTTP 爬虫、Puppeteer 爬虫（基于 Chromium 浏览器）和 Playwright 爬虫，支持处理 JavaScript 渲染的动态网站。
- **内置队列和存储**：自动管理请求队列、数据存储和键值存储，支持持久化数据和去重。
- **浏览器自动化**：集成 Puppeteer 和 Playwright，实现 headless 或 headful 浏览器操作，处理登录、表单提交和复杂交互。
- **代理和反检测**：内置代理轮换、指纹管理和反爬虫绕过功能，提高爬取成功率。
- **并发和可扩展性**：支持多线程/异步并发爬取，适用于大规模任务。
- **易集成**：与 Apify 平台无缝集成，可部署为云端 Actor；也支持本地运行。
- **类型安全和插件系统**：提供类型提示（Type Hints），易于扩展自定义爬虫逻辑。

该库强调可靠性、性能和开发者友好性，适合从简单数据提取到复杂自动化任务。

## 主要功能
- **请求管理和爬取**：自动处理 URL 队列、HTTP 请求和响应解析，支持自定义钩子（如 beforeRequest、afterResponse）。
- **数据提取**：内置数据集存储，支持 JSON、CSV 等格式导出；可使用 Cheerio 或 JSDOM 解析 HTML。
- **浏览器交互**：模拟用户行为，如点击、滚动、截屏和 PDF 生成。
- **错误处理和重试**：内置重试机制、日志记录和监控。
- **配置管理**：通过 LaunchContext 配置浏览器、代理和超时等参数。
- **集成工具**：支持与外部库如 BeautifulSoup 或 Selenium 结合使用。

## 用法
安装 Crawlee Python 需要 Python 3.8+。以下是基本用法示例：

1. **安装**：
   ```
   pip install crawlee
   ```

2. **基本 HTTP 爬虫示例**（爬取网站并提取标题）：
   ```python
   from crawlee.http_crawler import HttpCrawler
   from crawlee.models import RequestOptions

   async def main():
       crawler = HttpCrawler()

       @crawler.router.default_handler
       async def request_handler(context):
           title = await context.page.title()
           context.log.info(f'Title: {title}')
           # 将数据推送到数据集
           await context.push_data({'title': title})

       await crawler.run(['https://example.com'])

   if __name__ == '__main__':
       import asyncio
       asyncio.run(main())
   ```

3. **浏览器爬虫示例**（使用 Playwright 爬取动态内容）：
   ```python
   from crawlee.playwright_crawler import PlaywrightCrawler

   async def main():
       crawler = PlaywrightCrawler()

       @crawler.router.default_handler
       async def request_handler(context):
           # 等待页面加载
           await context.page.wait_for_selector('h1')
           title = await context.page.title()
           context.log.info(f'Title: {title}')
           await context.push_data({'title': title})

       await crawler.run(['https://example.com'])

   if __name__ == '__main__':
       import asyncio
       asyncio.run(main())
   ```

4. **运行和配置**：
   - 使用 `crawler.run(start_urls)` 启动爬取。
   - 配置代理：`context.launch_context.proxy_configuration = ProxyConfiguration({'proxyUrls': ['http://proxy1:port']})`。
   - 数据导出：爬取后，数据自动保存到 `./storage/datasets/default`。

详细文档和高级用法请参考 GitHub 仓库的 README 和示例文件夹。