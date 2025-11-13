---
title: MediaCrawler
---

# MediaCrawler 项目

## 项目地址
https://github.com/NanmiCoder/MediaCrawler

## 主要特性
MediaCrawler 是一个基于 Python 的媒体爬虫工具，主要用于从各种社交媒体平台（如 Twitter、Instagram、TikTok 等）爬取图片、视频和相关元数据。它支持多线程爬取、高效的代理管理和数据持久化存储，具有以下核心特性：
- **多平台支持**：兼容多种社交媒体 API 和网页抓取接口，覆盖主流平台。
- **高效爬取**：使用异步编程和多线程机制，实现快速批量下载媒体文件。
- **数据过滤与去重**：内置过滤器，支持按关键词、用户或时间范围筛选内容，并自动去重避免重复下载。
- **代理与反爬虫**：集成代理池和 User-Agent 轮换，增强爬取的稳定性和匿名性。
- **存储灵活**：支持本地文件存储、数据库（如 SQLite 或 MySQL）持久化和 JSON 导出。
- **模块化设计**：易于扩展，支持自定义爬虫模块和插件。

## 主要功能
- **用户/话题爬取**：根据指定用户 ID 或话题标签，爬取其发布的媒体内容。
- **媒体下载**：自动下载图片、视频和 GIF，支持高清质量和批量处理。
- **元数据提取**：捕获帖子描述、点赞数、评论等附加信息。
- **调度与监控**：内置任务调度器，可设置定时爬取，并提供日志监控和错误重试机制。
- **导出与可视化**：生成报告文件，支持 CSV/JSON 格式导出，便于后续分析。

## 用法
1. **环境准备**：
   - 克隆仓库：`git clone https://github.com/NanmiCoder/MediaCrawler.git`
   - 安装依赖：`pip install -r requirements.txt`（需 Python 3.8+）

2. **配置**：
   - 编辑 `config.py` 文件，设置平台 API 密钥、代理列表和目标平台。
   - 示例配置：
     ```python
     PLATFORMS = ['twitter', 'instagram']
     PROXY_LIST = ['http://proxy1:port', 'http://proxy2:port']
     DOWNLOAD_PATH = './downloads'
     ```

3. **运行爬虫**：
   - 基本命令：`python main.py --platform twitter --query "关键词" --limit 100`
   - 高级选项：
     - 用户爬取：`python main.py --platform instagram --user username --type video`
     - 批量任务：使用 `tasks.json` 定义多个任务，然后运行 `python scheduler.py`

4. **注意事项**：
   - 遵守平台使用条款，避免滥用导致 IP 封禁。
   - 对于大规模爬取，建议使用 VPS 并监控资源消耗。
   - 详细文档见仓库的 `README.md` 和 `docs/` 目录。