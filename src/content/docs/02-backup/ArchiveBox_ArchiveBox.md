---
title: ArchiveBox
---

# ArchiveBox 项目概述

## 项目地址
[https://github.com/ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)

## 主要特性
ArchiveBox 是一个开源的自托管网页归档工具，旨在帮助用户保存网页内容以防链接失效或内容更改。它支持多种归档格式，包括 HTML、PDF、截图、媒体文件等。主要特性包括：
- **自动化归档**：通过 RSS 订阅、书签导入或 URL 列表自动捕获和保存网页。
- **多格式支持**：使用工具如 wkhtmltopdf、singlefile、readability 等生成 PDF、单文件 HTML、纯文本提取等。
- **搜索和索引**：内置搜索功能，支持全文搜索和元数据索引，便于查找归档内容。
- **自托管**：基于 Docker 或 Python 运行，支持在本地服务器或云环境中部署。
- **扩展性**：可自定义配置，支持插件和钩子以扩展功能。
- **数据导出**：支持导出到 IPFS、JSON 或其他格式，便于备份和迁移。

## 主要功能
- **输入来源**：从浏览器书签（Chrome、Firefox 等）、RSS/Atom 订阅、Twitter 列表或手动 URL 导入内容。
- **归档过程**：自动下载网页的 HTML、CSS、JS、图像、视频和音频；生成截图、PDF 和存档版本；提取文章正文以去除广告。
- **管理界面**：Web 界面用于查看、搜索和组织归档，支持批量操作和删除。
- **调度和维护**：内置 cron 作业支持定期更新归档；数据去重以避免重复保存。
- **隐私与安全**：所有数据本地存储，不依赖第三方服务；支持密码保护和 HTTPS。

## 用法
1. **安装**：
   - 使用 Docker（推荐）：运行 `docker run -v $PWD:/data -it archivebox/archivebox init --setup` 初始化。
   - 或使用 pip：`pip install archivebox` 后运行 `archivebox init`。

2. **配置**：
   - 编辑 `ArchiveBox/config.json` 文件设置归档选项，如启用/禁用特定提取器（e.g., `USE_WKHTMLTOPDF = True`）。
   - 添加输入：`archivebox add 'https://example.com'` 或导入书签文件 `archivebox add bookmarks.html`。

3. **运行归档**：
   - 启动服务器：`archivebox server` 访问 Web 界面（默认 http://localhost:8000）。
   - 调度更新：`archivebox schedule` 设置自动任务。
   - 手动归档：`archivebox archive` 处理队列中的 URL。

4. **管理**：
   - 搜索内容：通过 Web 界面或 CLI `archivebox search "关键词"`。
   - 导出/备份：`archivebox export` 生成 JSON 或其他格式。
   - 更多详情参考官方文档：项目 README 和 Wiki。