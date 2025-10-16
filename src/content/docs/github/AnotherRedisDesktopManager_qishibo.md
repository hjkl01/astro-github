
---
title: AnotherRedisDesktopManager
---

# Another Redis Desktop Manager

## 项目地址
[GitHub 项目地址](https://github.com/qishibo/AnotherRedisDesktopManager)

## 主要特性
Another Redis Desktop Manager 是一个现代化的 Redis 桌面管理工具，采用 Electron-Vue 框架构建，支持跨平台（Windows、macOS 和 Linux）。其主要特性包括：
- **高性能连接管理**：支持 SSH 隧道、SSL/TLS 加密连接，确保安全访问 Redis 服务器。
- **直观的用户界面**：简洁的树状视图显示键值对，支持实时搜索和过滤。
- **多数据库支持**：轻松切换 Redis 数据库，支持集群模式（Redis Cluster）和哨兵模式（Sentinel）。
- **高级功能**：内置 Lua 脚本编辑器、键值编辑器（支持 JSON、字符串、二进制等格式）、Pub/Sub 消息订阅、慢查询日志查看。
- **自定义主题**：支持浅色和深色模式，界面响应式设计。
- **开源免费**：完全开源，无需付费，支持插件扩展。

## 主要功能
- **连接与管理**：添加、编辑、删除 Redis 连接，支持批量操作和导出/导入配置。
- **键值浏览与编辑**：可视化显示键列表，支持排序、搜索；编辑值时提供语法高亮和格式化工具。
- **监控工具**：实时查看服务器信息、内存使用、命令统计、客户端连接列表。
- **脚本执行**：集成 Redis CLI，支持运行自定义命令和 Lua 脚本。
- **数据导出/导入**：支持将键值数据导出为 JSON、CSV 等格式，或从文件导入。
- **安全特性**：密码管理、连接测试、自动重连机制。

## 用法
1. **下载与安装**：
   - 从 GitHub Releases 页面下载对应平台的安装包（.exe、.dmg 或 .AppImage）。
   - 运行安装程序，启动应用。

2. **添加连接**：
   - 点击“Connections”面板的“+”按钮。
   - 输入 Redis 服务器的 Host、Port、用户名/密码（如果适用）。
   - 对于高级连接，选择 SSH 或 SSL 选项配置隧道/加密。
   - 点击“Test Connection”验证后保存。

3. **浏览数据**：
   - 选择连接，双击展开数据库。
   - 在键列表中搜索或浏览键值，使用右键菜单编辑/删除键。
   - 对于复杂值（如 List、Set、Hash），使用内置编辑器修改。

4. **执行命令**：
   - 打开“CLI”面板，直接输入 Redis 命令（如 `SET key value`）并执行。
   - 或使用 Lua 编辑器编写并运行脚本。

5. **监控与维护**：
   - 在“Server Info”视图查看实时统计。
   - 使用“Pub/Sub”订阅频道接收消息。
   - 定期备份数据通过导出功能。

更多细节请参考项目 README 或官方文档。