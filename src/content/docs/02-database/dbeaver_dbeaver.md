---
title: dbeaver
---

# DBeaver

## 简介

DBeaver 是一个免费的多平台数据库工具和 SQL 客户端，专为开发者、SQL 程序员、数据库管理员和分析师设计。它提供了丰富的功能，支持多种数据库，并集成了 AI 辅助功能。

## 功能

- **多数据库支持**：支持超过 100 个数据库驱动，包括 MySQL、PostgreSQL、Oracle、SQL Server 等。还支持任何具有 JDBC 或 ODBC 驱动的数据库。
- **SQL 编辑器**：强大的 SQL 编辑器，支持语法高亮、智能补全和 AI 代码生成（与 OpenAI 或 Copilot 集成）。
- **数据编辑器**：直观的数据查看和编辑界面，支持大数据集。
- **模式编辑器**：可视化数据库模式编辑，包括 ER 图。
- **数据导入/导出/迁移**：支持多种格式的数据导入、导出和迁移。
- **SQL 执行计划**：分析和可视化 SQL 查询执行计划。
- **数据库管理工具**：包括数据库仪表板、空间数据查看器、代理和 SSH 隧道、自定义数据库驱动编辑器等。
- **AI 集成**：支持智能 AI 补全和代码生成。
- **扩展性**：基于 OSGI 和 Eclipse RCP，支持插件扩展。

## 用法

### 下载和安装

1. 从 [官方网站](https://dbeaver.io/download) 或 [GitHub Releases](https://github.com/dbeaver/dbeaver/releases) 下载最新版本的安装程序。
2. 运行安装程序（或解压存档文件）。
3. DBeaver 需要 Java 运行，默认包含 OpenJDK 21。如需更改 JDK 版本，可替换安装文件夹中的 `jre` 目录。

### 运行

运行 `dbeaver` 可执行文件启动应用程序。

### 基本使用

1. **连接数据库**：启动后，点击 "New Database Connection" 选择数据库类型，输入连接信息（如主机、端口、用户名、密码）。
2. **浏览数据库**：在左侧面板浏览数据库结构，包括表、视图、存储过程等。
3. **执行 SQL**：使用 SQL 编辑器编写和执行查询。支持多标签页。
4. **编辑数据**：右键表选择 "View Data" 或 "Edit Data" 查看和修改数据。
5. **导入/导出**：使用工具菜单进行数据导入导出。
6. **ER 图**：右键数据库或表生成 ER 图。

### 高级功能

- **SSH 隧道**：在连接设置中配置 SSH 隧道以安全连接远程数据库。
- **AI 助手**：在 SQL 编辑器中启用 AI 补全和代码生成（需要配置 API 密钥）。
- **插件**：通过 Eclipse Marketplace 安装额外插件扩展功能。

### 文档和支持

- [官方文档](https://dbeaver.com/docs/dbeaver/)
- [WIKI](https://github.com/dbeaver/dbeaver/wiki)
- [问题跟踪](https://github.com/dbeaver/dbeaver/issues)
- [讨论区](https://github.com/dbeaver/dbeaver/discussions)

DBeaver 是一个功能强大且易用的数据库工具，适合各种数据库管理需求。
