---
title: CloudBeaver
---

# CloudBeaver

CloudBeaver 是一个开源的云数据库管理器社区版，提供丰富的 Web 界面用于数据库管理。它是一个基于 Java 的 Web 服务器，前端使用 TypeScript 和 React 构建，支持多种数据库的连接和管理。

## 主要功能

- **数据库连接管理**：支持创建和管理多种数据库连接，包括 MySQL、PostgreSQL、ClickHouse、DuckDB、Databend 等。
- **SQL 编辑器**：提供强大的 SQL 编辑器，支持语法高亮、自动补全、查询执行和结果查看。
- **数据编辑器**：允许查看、编辑和导出数据，支持 GIS 数据可视化、数据传输等功能。
- **用户权限管理**：支持多用户环境下的权限配置和会话管理。
- **数据传输**：支持数据库间的数据导入导出。
- **主题和界面定制**：支持明暗主题切换、多行标签页等界面优化。

## 用法

### Docker 运行

CloudBeaver 提供了官方 Docker 镜像，可以轻松部署：

```bash
docker run -d -p 8978:8978 dbeaver/cloudbeaver
```

访问 `http://localhost:8978` 即可使用。

### 演示服务器

可以访问在线演示服务器：https://demo.cloudbeaver.io 来体验功能。

### 配置和部署

详细的部署说明请参考 [CloudBeaver Wiki](https://github.com/dbeaver/cloudbeaver/wiki/CloudBeaver-Deployment)。

## 支持的数据库

CloudBeaver 支持多种数据库驱动，包括但不限于：

- MySQL / MariaDB
- PostgreSQL
- ClickHouse
- DuckDB
- Databend
- SQL Server
- 以及其他 JDBC 兼容数据库

## 许可证

CloudBeaver 采用 Apache 2.0 许可证，完全免费开源。
