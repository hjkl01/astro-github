
---
title: superset
---

# Apache Superset

**GitHub项目地址:** [https://github.com/apache/superset](https://github.com/apache/superset)

## 主要特性

Apache Superset 是一个开源的数据可视化和探索平台，由 Apache 软件基金会维护。它支持多种数据源，提供交互式仪表板和 SQL 编辑器，帮助用户快速分析和可视化大数据。主要特性包括：

- **多数据源支持**：兼容 SQL 数据库（如 PostgreSQL、MySQL）、NoSQL（如 Druid、Elasticsearch）、云数据仓库（如 Snowflake、BigQuery）和 CSV/Excel 文件等。
- **丰富的可视化类型**：内置 40 多种图表类型，包括柱状图、折线图、地图、桑基图、热力图等，支持自定义可视化插件。
- **交互式仪表板**：拖拽式构建仪表板，支持过滤器、钻取和跨图表交互，实现动态数据探索。
- **SQL 编辑器**：内置 SQL Lab，支持编写、保存和共享 SQL 查询，提供自动补全和结果可视化。
- **安全性与权限**：角色-based 访问控制（RBAC），支持 LDAP、OAuth 等认证集成，确保数据安全。
- **扩展性**：基于 Python 和 React 构建，支持插件系统和 API 接口，便于二次开发。
- **性能优化**：异步查询、缓存机制和 Celery 任务队列，支持大规模数据集处理。
- **多语言支持**：包括中文界面，易于国际化使用。

## 主要功能

- **数据连接与探索**：连接各种数据源，进行元数据管理、数据集创建和虚拟度量定义。
- **查询与分析**：通过 SQL Lab 执行复杂查询，或使用 Explore 模式进行无代码可视化。
- **仪表板构建**：创建可共享的仪表板，支持嵌入网站或导出为 PDF/图像。
- **警报与调度**：设置数据警报和报告调度，实现自动化通知。
- **协作与共享**：用户协作编辑、版本控制和公共/私有仪表板共享。
- **移动端适配**：响应式设计，支持移动设备访问。

## 用法指南

1. **安装部署**：
   - **前提**：Python 3.8+、Node.js 和数据库（如 PostgreSQL 用于元数据存储）。
   - **Docker 方式**（推荐新手）：克隆仓库后运行 `docker-compose up`，快速启动开发环境。
   - **手动安装**：安装依赖 `pip install apache-superset`，初始化数据库 `superset db upgrade`，创建管理员用户 `superset fab create-admin`，启动服务器 `superset run -h 0.0.0.0 -p 8088`。
   - 详细文档：参考 [官方安装指南](https://superset.apache.org/docs/installation)。

2. **基本使用流程**：
   - **连接数据源**：登录后，进入“Sources > Databases”，添加数据库连接（如 JDBC/ODBC URL）。
   - **创建数据集**：在“Sources > Datasets”中选择表或编写 SQL 创建虚拟数据集。
   - **构建可视化**：进入“Charts > + Chart”，选择数据集和图表类型，配置度量和维度，保存。
   - **组装仪表板**：进入“Dashboards > + Dashboard”，拖拽图表添加，支持 Markdown 文本和过滤器。
   - **执行 SQL**：使用 SQL Lab 编写查询，运行后直接可视化结果或保存为图表。
   - **管理与共享**：通过“Settings”配置角色和权限，分享链接或嵌入代码。

3. **高级用法**：
   - **自定义主题**：修改 CSS 或使用 Superset 的主题配置 API。
   - **API 集成**：使用 REST API（如 `/api/v1/chart/`）自动化创建图表。
   - **插件开发**：扩展可视化类型，通过 `superset-frontend` 仓库贡献代码。
   - **生产部署**：使用 Gunicorn + Nginx 配置，支持 Kubernetes 部署。

更多细节请参考官方文档：[https://superset.apache.org/docs](https://superset.apache.org/docs)。项目活跃维护，社区支持强大，适合数据分析师、BI 工程师使用。