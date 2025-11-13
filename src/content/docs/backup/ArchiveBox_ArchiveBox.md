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

- **输入格式**：支持浏览器扩展、RSS/Atom 订阅、浏览器书签、Pocket/Pinboard 等多种输入来源。
- **输出格式**：保存为标准 HTML、PDF、PNG、TXT、JSON、WARC 等格式，支持提取媒体、文章文本等。
- **归档过程**：自动提取网页内容，包括 HTML、截图、PDF、文章文本、媒体文件等。
- **管理界面**：Web UI 用于查看、搜索和管理归档，支持批量操作。
- **调度和导入**：支持定期导入和实时归档。
- **隐私与安全**：本地存储，支持加密和密码保护。

## 用法

1. **安装**：
   - Docker Compose（推荐）：下载 `docker-compose.yml`，运行 `docker compose run archivebox init --setup`。
   - Docker：`docker run -v $PWD:/data -it archivebox/archivebox init --setup`。
   - pip：`pip install archivebox yt-dlp playwright`，然后 `archivebox init --setup`。
   - 其他：支持 apt、brew 等包管理器。

2. **配置和添加 URL**：
   - 使用 CLI：`archivebox add 'https://example.com'`。
   - 使用浏览器扩展或导入 RSS/书签。
   - 配置选项：编辑配置文件启用/禁用提取器。

3. **运行和访问**：
   - CLI：`archivebox server 0.0.0.0:8000` 启动 Web UI。
   - Web UI：访问 http://localhost:8000 查看和管理归档。
   - API：支持 REST API 和 Python API。

4. **高级用法**：
   - 调度：`archivebox schedule` 设置定期导入。
   - 导出：`archivebox list --html` 导出静态 HTML。
   - 更多详情参考官方文档和 Wiki。
