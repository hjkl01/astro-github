---
title: DrissionPage
---

# DrissionPage 项目介绍

## 项目地址
[https://github.com/g1879/DrissionPage](https://github.com/g1879/DrissionPage)

## 主要特性
DrissionPage 是一个开源的 Python 网页自动化库，结合了 Selenium 和 Requests 的优势，提供高效、灵活的网页浏览和数据采集功能。主要特性包括：
- **双核支持**：无缝集成 Chromium 浏览器内核（类似 Selenium）和无头 Requests 模式，支持动态和静态网页处理。
- **智能元素定位**：内置多种选择器（如 CSS、XPath、文本匹配），并支持元素等待和交互自动化。
- **页面控制**：支持页面导航、表单提交、JavaScript 执行、截屏和下载管理。
- **易用性和扩展性**：API 设计简洁，支持多线程、代理设置和自定义配置；兼容 Python 3.7+。
- **轻量高效**：无需额外安装浏览器驱动，内置 Chromium 驱动管理，资源占用低。

## 主要功能
- **浏览器自动化**：模拟用户操作，如点击、输入、滚动和切换窗口。
- **数据采集**：提取页面元素、HTML 源码、JSON 数据，支持 AJAX 加载处理。
- **网络请求**：发送 HTTP 请求，处理 cookies、会话和重定向。
- **调试工具**：提供页面快照、日志记录和元素高亮功能，便于开发调试。
- **高级应用**：支持文件上传/下载、弹出窗口处理和跨域资源访问。

## 用法
1. **安装**：使用 pip 安装库：
   ```
   pip install DrissionPage
   ```

2. **基本示例**（使用 Chromium 模式打开页面并提取标题）：
   ```python
   from DrissionPage import ChromiumPage

   page = ChromiumPage()
   page.get('https://www.example.com')
   title = page.title
   print(title)
   page.quit()
   ```

3. **Requests 模式示例**（无头获取页面内容）：
   ```python
   from DrissionPage import SessionPage

   page = SessionPage()
   page.get('https://www.example.com')
   html = page.html
   print(html)
   ```

4. **元素操作示例**（定位并点击按钮）：
   ```python
   from DrissionPage import ChromiumPage

   page = ChromiumPage()
   page.get('https://www.example.com')
   button = page.ele('#submit-btn')  # 使用 CSS 选择器
   button.click()
   ```

详细文档和更多示例请参考 GitHub 仓库的 README 和 examples 文件夹。