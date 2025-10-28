
---
title: dianping_spider
---

# 大众点评爬虫项目

## 项目地址
[GitHub 项目地址](https://github.com/Sniper970119/dianping_spider)

## 主要特性
- **高效爬取**：基于 Scrapy 框架，实现对大众点评网站的批量数据采集，支持店铺信息、评论和评分等数据的结构化提取。
- **模块化设计**：项目结构清晰，包括 spiders、items、pipelines 和 settings 等模块，便于扩展和维护。
- **反爬虫处理**：集成代理 IP 池、User-Agent 随机切换和延迟控制等机制，降低被封禁的风险。
- **数据持久化**：支持将爬取数据导出为 JSON、CSV 或数据库存储，便于后续分析。
- **开源免费**：纯 Python 实现，无需额外付费工具，适合学习和二次开发。

## 主要功能
- **店铺信息采集**：爬取指定城市或类别的店铺详情，包括名称、地址、星级、价格水平和标签。
- **用户评论抓取**：提取店铺的评论内容、评论者信息、时间戳和情感倾向，支持分页加载。
- **图片和媒体下载**：可选下载店铺照片或用户上传的图片资源。
- **搜索和过滤**：通过关键词或地理位置过滤目标数据，支持自定义爬取范围。
- **数据清洗**：内置 pipelines 进行数据去重、格式标准化和错误处理。

## 用法
1. **环境准备**：
   - 安装 Python 3.x 和 Scrapy：`pip install scrapy`。
   - 克隆项目：`git clone https://github.com/Sniper970119/dianping_spider.git`。
   - 进入项目目录：`cd dianping_spider`。

2. **配置设置**：
   - 编辑 `settings.py` 文件，设置目标城市、爬取深度、代理配置等参数。
   - 如需数据库存储，配置 MySQL 或 MongoDB 连接。

3. **运行爬虫**：
   - 基本命令：`scrapy crawl dianping`（替换 `dianping` 为具体 spider 名称）。
   - 指定输出：`scrapy crawl dianping -o output.json`。
   - 测试模式：`scrapy crawl dianping -s LOG_LEVEL=INFO`。

4. **注意事项**：
   - 遵守大众点评的使用条款，避免高频请求导致 IP 封禁。
   - 项目可能需根据网站更新调整 XPath 或 CSS 选择器。
   - 建议在虚拟环境中运行，以管理依赖。