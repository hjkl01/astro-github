---
title: bitmagnet
---

# Bitmagnet 项目

**GitHub 项目地址:** [https://github.com/bitmagnet-io/bitmagnet](https://github.com/bitmagnet-io/bitmagnet)

## 主要特性
Bitmagnet 是一个开源的磁力链接索引器和 API，提供高效的 BitTorrent 生态系统搜索和数据管理功能。主要特性包括：
- **磁力链接索引**：自动爬取和索引 BitTorrent 元数据，支持大规模数据存储和快速检索。
- **RESTful API 接口**：提供标准化的 API，用于查询 torrent 信息、元数据和搜索结果，支持 JSON 格式输出。
- **高性能架构**：基于 Go 语言开发，使用 PostgreSQL 数据库和 Redis 缓存，实现高效的索引和查询性能。
- **模块化设计**：支持插件扩展，包括 RSS 订阅、P2P 爬虫和自定义搜索过滤器。
- **数据丰富性**：索引 torrent 文件的详细信息，如文件列表、大小、种子数、评论等，支持多语言和多源数据聚合。
- **自托管友好**：易于部署在 Docker 或 Kubernetes 环境中，无需复杂配置。

## 主要功能
- **搜索功能**：通过 API 或 Web 界面搜索 torrent，支持关键词、类别、标签和高级过滤（如文件大小、上传日期）。
- **元数据管理**：存储和更新 torrent 元数据，包括健康度评估（基于种子/下载者比率）和自动验证。
- **API 集成**：暴露 endpoints 如 `/search`、`/torrent/{id}` 和 `/stats`，便于与其他工具（如 qBittorrent 或 Deluge）集成。
- **监控与统计**：提供系统统计、索引进度和错误日志功能，支持警报和通知。
- **数据导入/导出**：支持批量导入现有 torrent 数据，并导出为 JSON 或 CSV 格式。
- **安全性**：内置认证机制（如 API 密钥）和数据加密，确保隐私保护。

## 用法
1. **安装与部署**：
   - 使用 Docker 快速启动：运行 `docker run -p 8080:8080 bitmagnet/bitmagnet`（参考官方文档获取完整配置）。
   - 手动安装：克隆仓库，安装 Go 环境，运行 `go build` 和 `./bitmagnet`。配置 PostgreSQL 和 Redis 连接。

2. **配置**：
   - 编辑 `config.yaml` 文件，设置数据库连接、API 端口和爬虫参数（如索引源列表）。
   - 启用 RSS 馈送或 P2P 爬虫模块，通过环境变量调整性能（如并发数）。

3. **使用 API**：
   - 搜索示例：`GET /api/v1/search?q=example&category=movies` 返回匹配的 torrent 列表。
   - 获取 torrent 详情：`GET /api/v1/torrent/{hash}`。
   - 认证：使用 API 密钥在请求头中添加 `Authorization: Bearer <token>`。

4. **Web 界面**（可选）：
   - 访问 `http://localhost:8080` 使用内置 UI 进行搜索和浏览，无需额外工具。

5. **维护**：
   - 运行索引任务：`bitmagnet index --all` 更新数据库。
   - 监控日志：通过 `docker logs` 或文件查看运行状态。
   - 扩展：添加自定义爬虫插件到 `/plugins` 目录并重启服务。

详细文档和示例请参考项目仓库的 README 和 API 规范。