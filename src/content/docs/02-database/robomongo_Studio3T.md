
---
title: robomongo
---

# RoboMongo 项目描述

## 项目地址
[https://github.com/Studio3T/robomongo](https://github.com/Studio3T/robomongo)

## 主要特性
RoboMongo（现更名为 Robo 3T）是一个开源的 MongoDB 管理工具，专为 MongoDB 数据库设计，提供图形化界面来简化数据库操作。它支持跨平台（Windows、macOS、Linux），并集成了 MongoDB Shell 的功能，允许用户在 GUI 和命令行之间无缝切换。主要特性包括：
- **图形化数据管理**：可视化浏览和编辑 MongoDB 集合（collections），支持 JSON 格式的文档查看和修改。
- **查询构建器**：内置查询编辑器，支持构建复杂查询、聚合管道和地图-归约操作。
- **MongoDB Shell 集成**：直接在应用内运行 JavaScript 命令，支持 IntelliShell 提供代码补全和语法高亮。
- **导入/导出支持**：轻松导入 JSON、CSV、 BSON 等格式的数据，并导出为多种格式。
- **连接管理**：支持连接到本地或远程 MongoDB 实例，包括副本集（replica sets）和分片集群（sharded clusters）。
- **自定义界面**：可自定义主题、字体和布局，支持多标签页管理多个数据库。
- **安全性**：支持 SSL/TLS 加密连接和认证机制。

## 主要功能
- **数据库连接与探索**：快速连接 MongoDB 服务器，浏览数据库、集合和索引。
- **数据操作**：插入、更新、删除文档，支持批量操作和全文搜索。
- **聚合与分析**：使用聚合框架进行数据管道处理，提供可视化结果预览。
- **脚本执行**：运行自定义 JavaScript 脚本，实现高级自动化任务。
- **备份与恢复**：通过 mongodump/mongorestore 集成进行数据备份。
- **监控与诊断**：查看服务器状态、性能指标和日志。

## 用法指南
1. **下载与安装**：
   - 从 GitHub Releases 页面下载适用于您操作系统的二进制文件（.exe、.dmg 或 .deb/.rpm）。
   - 安装后启动应用。

2. **连接数据库**：
   - 点击“Connect”按钮，输入 MongoDB 连接字符串（如 `mongodb://localhost:27017`）或配置主机、端口、认证信息。
   - 对于云服务如 MongoDB Atlas，支持直接连接。

3. **浏览数据**：
   - 连接成功后，在左侧树状结构中展开数据库和集合。
   - 双击集合查看文档列表，支持树形（Tree）、JSON 或自定义视图。

4. **执行查询**：
   - 在查询栏输入 MongoDB 查询语法（如 `{ "name": "example" }`），点击“Find”执行。
   - 使用聚合选项卡构建管道：添加阶段（如 $match、$group），实时预览结果。

5. **编辑与保存**：
   - 选中文档，修改字段后保存更改。
   - 对于脚本，使用 Shell 标签运行命令，如 `db.collection.find()`。

6. **高级用法**：
   - 导入数据：选择“Import”菜单，上传文件并映射字段。
   - 导出数据：右键集合，选择“Export”并指定格式。
   - 自定义：通过“Options”菜单调整设置，如启用自动补全或更改默认端口。

Robo 3T 适合开发者和 DBA 使用，提供从初学者到专家的友好体验。更多细节请参考项目 README 或官方文档。