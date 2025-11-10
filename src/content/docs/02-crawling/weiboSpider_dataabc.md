---
title: weiboSpider
---

# weiboSpider 项目

**项目地址**: [https://github.com/dataabc/weiboSpider](https://github.com/dataabc/weiboSpider)

## 主要特性
- **高效爬取**: 支持多线程和高并发模式，快速获取新浪微博数据，避免IP封禁。
- **灵活过滤**: 内置去重、时间范围过滤和关键词过滤功能，确保数据质量。
- **数据存储**: 支持导出为CSV、JSON或MySQL数据库，便于后续分析。
- **用户友好**: 提供图形界面（GUI）和命令行两种操作模式，适合不同用户。
- **开源免费**: 基于Python开发，代码开源，支持自定义扩展。

## 主要功能
- **用户数据爬取**: 根据用户ID或昵称，爬取用户个人信息、微博列表、评论和转发数据。
- **关键词搜索**: 通过关键词搜索微博，支持高级查询如时间段、位置等。
- **热搜与话题**: 爬取微博热搜榜、话题讨论和实时热点数据。
- **评论与互动**: 提取微博下的评论、点赞和转发信息。
- **反爬虫绕过**: 集成Cookie管理和代理池，模拟真实浏览器行为。

## 用法
1. **环境准备**:
   - 安装Python 3.6+。
   - 克隆仓库: `git clone https://github.com/dataabc/weiboSpider.git`。
   - 安装依赖: `pip install -r requirements.txt`（包括selenium、requests等）。

2. **配置**:
   - 编辑`config.py`文件，设置Cookie（从浏览器获取微博登录Cookie）、代理IP和数据库连接。
   - 对于GUI模式，无需命令行，直接运行`python gui.py`。

3. **命令行用法**:
   - 爬取用户微博: `python weibo.py --user <用户ID> --count <微博数量>`。
   - 关键词搜索: `python search.py --keyword <关键词> --start <开始日期> --end <结束日期>`。
   - 导出数据: 使用`--output csv`指定格式。

4. **GUI用法**:
   - 运行`python gui.py`，输入用户ID或关键词，点击“开始爬取”。
   - 数据自动保存到指定目录。

注意: 使用前需遵守微博使用条款，避免滥用导致账号封禁。项目文档详见仓库README。