
---
title: pydoll
---

# PyDoll 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/autoscrape-labs/pydoll)

## 主要特性
PyDoll 是一个基于 Python 的自动化工具库，专注于网页爬取和数据提取。其核心特性包括：
- **自动化浏览器控制**：集成 Selenium 或 Playwright，支持无头模式运行，模拟真实用户行为。
- **智能元素定位**：使用 CSS 选择器、XPath 或 AI 辅助的元素识别，适应动态网页。
- **数据处理与存储**：内置数据清洗、JSON/CSV 导出，支持数据库集成（如 SQLite 或 MySQL）。
- **反爬虫绕过**：提供代理旋转、User-Agent 随机化和延迟控制，减少被封禁风险。
- **模块化设计**：易于扩展，支持自定义脚本和插件开发。
- **跨平台兼容**：适用于 Windows、macOS 和 Linux，支持 Python 3.8+。

## 主要功能
- **网页爬取**：自动访问 URL，提取文本、图像、表格等内容。
- **表单交互**：模拟登录、搜索和提交表单，实现复杂交互任务。
- **分页处理**：自动处理多页结果，支持无限滚动页面。
- **API 集成**：可与外部 API 结合，用于数据验证或补充。
- **错误处理**：内置重试机制和日志记录，确保任务鲁棒性。
- **批量任务**：支持多线程或异步执行，提高效率。

## 用法
1. **安装**：
   ```
   pip install pydoll
   ```

2. **基本用法示例**（Python 脚本）：
   ```python
   from pydoll import Browser, Scraper

   # 初始化浏览器
   browser = Browser(headless=True)  # 无头模式

   # 创建爬取器
   scraper = Scraper(browser)

   # 访问 URL 并提取数据
   url = "https://example.com"
   data = scraper.extract(url, selector=".content")  # 使用 CSS 选择器

   # 保存数据
   scraper.save_to_json(data, "output.json")

   # 关闭浏览器
   browser.close()
   ```

3. **高级用法**：
   - 配置代理：`browser.set_proxy("http://proxy:port")`。
   - 自定义脚本：继承 `Scraper` 类，重写 `parse` 方法处理特定逻辑。
   - 运行任务：使用 CLI 工具 `pydoll run config.yaml`，配置文件支持 YAML 格式定义任务。

更多细节请参考 GitHub 仓库的 README 和文档。