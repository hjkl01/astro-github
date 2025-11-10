---
title: facebook-scraper
---

# facebook-scraper 项目

## 项目地址
[https://github.com/kevinzg/facebook-scraper](https://github.com/kevinzg/facebook-scraper)

## 主要特性
- **无需登录**：无需提供 Facebook 凭证，即可从 Facebook 页面提取数据，避免账户风险。
- **高效抓取**：使用 Selenium 或无头浏览器模拟访问，支持提取帖子、评论和反应等内容。
- **数据格式化**：返回结构化数据，如 JSON 或 Pandas DataFrame，便于后续处理和分析。
- **模块化设计**：提供简单 API 接口，支持自定义抓取参数，如时间范围、帖子数量等。
- **开源免费**：基于 Python 实现，MIT 许可，易于扩展和集成。

## 主要功能
- **提取帖子**：从指定 Facebook 页面或群组抓取帖子内容，包括文本、图片、视频链接、发布时间和作者信息。
- **获取评论**：针对特定帖子提取评论及其回复，支持嵌套评论结构。
- **反应统计**：收集帖子的点赞、爱心、哈哈等反应计数。
- **搜索支持**：可根据关键词或日期过滤帖子，实现针对性数据采集。
- **错误处理**：内置重试机制和异常捕获，应对 Facebook 的反爬虫措施。

## 用法
1. **安装**：
   ```bash
   pip install facebook-scraper
   ```

2. **基本示例**（提取页面帖子）：
   ```python
   from facebook_scraper import get_posts

   for post in get_posts('nasa', pages=5):  # 提取 NASA 页面的前 5 页帖子
       print(post['text'][:50])  # 输出帖子文本的前 50 个字符
       print(post['likes'])
   ```

3. **提取评论**：
   ```python
   from facebook_scraper import get_posts

   post = next(get_posts('nasa', pages=1))  # 获取第一个帖子
   post_id = post['post_id']
   for comment in get_comments(post_id):
       print(comment['text'])
   ```

4. **高级用法**（指定选项）：
   ```python
   from facebook_scraper import get_posts

   options = {
       'allow_extra_requests': False,  # 禁用额外请求以提高速度
       'timeout': 10,  # 设置超时时间
       'reactors': True  # 启用反应统计
   }

   for post in get_posts('nasa', options=options, pages=3):
       print(post['reactions'])
   ```

注意：由于 Facebook 的政策变化，建议定期检查项目更新以确保兼容性。使用时遵守 Facebook 的服务条款，避免滥用。