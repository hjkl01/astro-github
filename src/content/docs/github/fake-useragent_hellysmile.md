
---
title: fake-useragent
---

# Fake-UserAgent 项目

## 项目地址
[https://github.com/hellysmile/fake-useragent](https://github.com/hellysmile/fake-useragent)

## 主要特性
- **随机生成User-Agent**：该项目是一个Python库，用于生成假的浏览器User-Agent字符串，支持多种浏览器和操作系统组合，帮助模拟真实用户行为。
- **轻量级和易用**：无需外部依赖，仅需Python环境即可运行，支持快速集成到爬虫或自动化脚本中。
- **自定义支持**：允许用户自定义User-Agent列表，或从内置数据库中随机选取，增强隐私保护和反检测能力。
- **开源免费**：基于MIT许可，社区维护，用户可自由贡献和修改。

## 主要功能
- **生成随机User-Agent**：通过简单API调用，返回模拟Chrome、Firefox、Safari等浏览器的User-Agent字符串。
- **支持版本多样性**：内置大量真实User-Agent模板，包括桌面、移动端和不同操作系统（如Windows、macOS、Android、iOS）。
- **批量生成**：可一次性生成多个User-Agent，用于大规模请求场景。
- **数据更新**：项目定期更新User-Agent数据库，以适应浏览器版本变化。

## 用法
1. **安装**：
   使用pip安装库：
   ```
   pip install fake-useragent
   ```

2. **基本用法**：
   - 导入库并生成单个User-Agent：
     ```python
     from fake_useragent import UserAgent
     ua = UserAgent()
     user_agent = ua.random  # 返回随机User-Agent字符串
     print(user_agent)
     ```
   - 生成特定浏览器User-Agent：
     ```python
     chrome_ua = ua.chrome  # Chrome浏览器
     firefox_ua = ua.firefox  # Firefox浏览器
     ```

3. **高级用法**：
   - 禁用缓存（默认启用以提高性能）：
     ```python
     ua = UserAgent(cache=False)
     ```
   - 指定操作系统：
     ```python
     ua = UserAgent(browsers=['chrome'], os=['windows'])
     user_agent = ua.random
     ```
   - 在HTTP请求中使用（例如与requests库结合）：
     ```python
     import requests
     from fake_useragent import UserAgent
     ua = UserAgent()
     headers = {'User-Agent': ua.random}
     response = requests.get('https://example.com', headers=headers)
     ```

更多细节请参考项目README文档。